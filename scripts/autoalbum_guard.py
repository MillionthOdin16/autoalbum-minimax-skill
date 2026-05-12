#!/usr/bin/env python3
"""AutoAlbum agent-native workflow guard v24.

This helper enforces the non-creative parts of the AutoAlbum pipeline:
project setup, phase routing, gate checks, schema validation, artifact hashes,
review freshness, quote grounding, style catalog grounding, tournament
consistency, prompt linting, renderable variants, payload export, state
reconciliation, snapshots, rollback, and result logging.

It intentionally does not write songs or judge musical taste. It makes sure the
agent cannot claim readiness with stale, invalid, ungrounded, or non-renderable
artifacts.
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple, Optional

try:
    import jsonschema  # type: ignore
except Exception:
    jsonschema = None

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
PHASE_PATH = SKILL_DIR / "references" / "controller" / "phase_order.json"
GATE_PATH = SKILL_DIR / "references" / "controller" / "gate_requirements.json"
APPLICABILITY_PATH = SKILL_DIR / "references" / "controller" / "phase_applicability.json"

PROJECT_DIRS = [
    "style_catalog_outputs", "foundation", "planning", "tracks", "generation/payloads",
    "covers", "ops/response_archive", "ops/hashes", "reviews/controller", "reviews/verifier",
    "release_package/audio", "release_package/prompts", "release_package/packets",
    "release_package/provenance",
]

RESULTS_FIELDS = [
    "timestamp", "phase", "artifact_id", "track_number", "variant", "score_type",
    "score", "status", "decision", "path", "notes",
]

ROOT_SCHEMA_MAP = {
    "state.json": "references/schemas/state.schema.json",
    "project_config.json": "references/schemas/project_config.schema.json",
    "project_manifest.json": "references/schemas/project_manifest.schema.json",
}
ARTIFACT_SCHEMA_BY_NAME = {
    "generation_packet.json": "references/schemas/generation_packet.schema.json",
    "style_card.json": "references/schemas/track_style_card.schema.json",
    "prosody_review.json": "references/schemas/prosody_review.schema.json",
    "prompt_budget_report.json": "references/schemas/prompt_budget_report.schema.json",
    "candidate_comparison.json": "references/schemas/candidate_comparison.schema.json",
    "selected_candidate.json": "references/schemas/selected_candidate.schema.json",
    "album_canon.json": "references/schemas/album_canon.schema.json",
    "unified_eval.json": "references/schemas/unified_eval.schema.json",
    "line_polish_review.json": "references/schemas/line_polish_review.schema.json",
    "lyrics_verifier_review.json": "references/schemas/independent_verifier_review.schema.json",
    "prompt_packet_verifier_review.json": "references/schemas/independent_verifier_review.schema.json",
    "completion_verifier_review.json": "references/schemas/independent_verifier_review.schema.json",
    "prompt_lint_report.json": "references/schemas/prompt_lint_report.schema.json",
    "style_catalog_verification.json": "references/schemas/style_catalog_verification.schema.json",
}
VARIANT_RE = re.compile(r"^tracks/tr_\d{2}/variants/.+\.json$")
PAYLOAD_RE = re.compile(r"^generation/payloads/.+\.json$")
EVAL_NAME_RE = re.compile(r"(eval|review|audit|verifier|polish|lint|adversarial)", re.I)
CJK_RE = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")


def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", name.strip().lower()).strip("-")
    return s or "autoalbum-project"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def load_phases() -> List[Dict[str, Any]]:
    return load_json(PHASE_PATH)["phases"]


def phase_ids() -> List[str]:
    return [p["id"] for p in load_phases()]


def load_gates() -> Dict[str, Any]:
    return load_json(GATE_PATH)


def load_applicability() -> Dict[str, Any]:
    return load_json(APPLICABILITY_PATH) if APPLICABILITY_PATH.exists() else {"scope_defaults": {}, "output_goal_overrides": {}, "quality_mode_overrides": {}, "values": {}}


def _resolve_copy(table: Dict[str, Any], key: str) -> Dict[str, str]:
    row = dict(table.get(key, {}))
    seen = set()
    while "__copy__" in row and row["__copy__"] not in seen:
        seen.add(row["__copy__"])
        base = dict(table.get(row.pop("__copy__"), {}))
        base.update(row)
        row = base
    row.pop("__copy__", None)
    return row


def project_path_arg(value: str) -> Path:
    return Path(value).expanduser().resolve()


def read_project_config(project: Path) -> Dict[str, Any]:
    p = project / "project_config.json"
    return load_json(p) if p.exists() else {}


def phase_applicability(project: Path, phase: str) -> Tuple[str, str]:
    app = load_applicability()
    cfg = read_project_config(project)
    scope = cfg.get("project_scope") or cfg.get("scope") or "album"
    output_goal = cfg.get("output_goal") or "release_package"
    quality_mode = cfg.get("quality_mode") or "standard"
    scope_row = _resolve_copy(app.get("scope_defaults", {}), scope)
    value = scope_row.get(phase, "C")
    quality_row = _resolve_copy(app.get("quality_mode_overrides", {}), quality_mode)
    value = quality_row.get(phase, value)
    goal_row = _resolve_copy(app.get("output_goal_overrides", {}), output_goal)
    value = goal_row.get(phase, value)
    return value, app.get("values", {}).get(value, value)


def next_phase(current: str) -> Optional[str]:
    ids = phase_ids()
    if current not in ids:
        return None
    i = ids.index(current)
    return ids[i + 1] if i + 1 < len(ids) else None


def iter_files(project: Path) -> Iterable[Path]:
    skip_parts = {".autoalbum_snapshots", "__pycache__"}
    for p in project.rglob("*"):
        if any(part in skip_parts for part in p.parts):
            continue
        if p.is_file():
            yield p


def track_numbers(project: Path, state: Optional[Dict[str, Any]] = None) -> List[str]:
    if state is None and (project / "state.json").exists():
        state = load_json(project / "state.json")
    nums: List[str] = []
    if state:
        tracks = state.get("tracks", {})
        for key in tracks.keys():
            if str(key).isdigit():
                nums.append(f"{int(key):02d}")
        total = int(state.get("tracks_total") or state.get("track_count") or 0)
        if total and not nums:
            nums = [f"{i:02d}" for i in range(1, total + 1)]
    if not nums and (project / "tracks").exists():
        for p in sorted((project / "tracks").glob("tr_*")):
            m = re.search(r"tr_(\d+)", p.name)
            if m:
                nums.append(f"{int(m.group(1)):02d}")
    return sorted(set(nums), key=lambda x: int(x))


def artifact_category(path: Path) -> str:
    return path.parts[0] if path.parts else "root"


def schema_for_rel(rel: str) -> Optional[str]:
    if rel in ROOT_SCHEMA_MAP:
        return ROOT_SCHEMA_MAP[rel]
    if VARIANT_RE.match(rel):
        return "references/schemas/generation_packet.schema.json"
    if PAYLOAD_RE.match(rel):
        return "references/schemas/minimax_payload.schema.json"
    return ARTIFACT_SCHEMA_BY_NAME.get(Path(rel).name)


def guess_schema(rel: str) -> Optional[str]:
    return schema_for_rel(rel)


def refresh_manifest(project: Path, quiet: bool = False) -> int:
    manifest_path = project / "project_manifest.json"
    manifest = load_json(manifest_path) if manifest_path.exists() else {
        "project_name": project.name,
        "project_slug": project.name,
        "project_root": str(project),
        "created_at": now_iso(),
        "current_state_path": "state.json",
        "artifacts": [],
    }
    artifacts = []
    for p in sorted(iter_files(project)):
        rel = p.relative_to(project).as_posix()
        if rel == "project_manifest.json":
            continue
        track_number = None
        m = re.search(r"tracks/tr_(\d+)", rel)
        if m:
            track_number = int(m.group(1))
        artifacts.append({
            "artifact_id": re.sub(r"[^a-zA-Z0-9]+", "_", rel).strip("_"),
            "path": rel,
            "category": artifact_category(Path(rel)),
            "track_number": track_number,
            "variant_id": (Path(rel).stem if "/variants/" in rel else None),
            "version": None,
            "status": "present",
            "schema": guess_schema(rel),
            "sha256": sha256_file(p),
            "notes": "",
        })
    manifest["updated_at"] = now_iso()
    manifest["artifacts"] = artifacts
    write_json(manifest_path, manifest)
    if not quiet:
        print(f"Manifest refreshed: {manifest_path} ({len(artifacts)} artifacts)")
    return 0


def append_result(project: Path, row: Dict[str, Any]) -> None:
    path = project / "results.tsv"
    exists = path.exists()
    with path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=RESULTS_FIELDS, delimiter="\t", extrasaction="ignore")
        if not exists:
            writer.writeheader()
        out = {k: "" for k in RESULTS_FIELDS}
        out.update({k: "" if v is None else str(v) for k, v in row.items()})
        if not out.get("timestamp"):
            out["timestamp"] = now_iso()
        writer.writerow(out)


def create_project(args: argparse.Namespace) -> int:
    slug = args.slug or slugify(args.name)
    root = project_path_arg(args.root) / slug
    if root.exists() and not args.force:
        print(f"ERROR: project already exists: {root}\nUse --force to initialize missing files only.", file=sys.stderr)
        return 2
    root.mkdir(parents=True, exist_ok=True)
    for d in PROJECT_DIRS:
        (root / d).mkdir(parents=True, exist_ok=True)
    for i in range(1, args.tracks + 1):
        tr = root / "tracks" / f"tr_{i:02d}"
        for d in ["versions", "variants", "renders/raw", "renders/selected", "renders/rejected"]:
            (tr / d).mkdir(parents=True, exist_ok=True)
    project_id = hashlib.sha1(f"{slug}:{now_iso()}".encode()).hexdigest()[:12]
    tracks = {
        f"{i:02d}": {
            "title": "",
            "status": "not_started",
            "paths": {},
            "scores": {},
            "variants": {},
            "renders": {"candidate_count": 0, "selected_render_id": None},
            "decision": "not_started",
        }
        for i in range(1, args.tracks + 1)
    }
    provider_id = Path(args.provider_profile).stem
    config = {
        "project_name": args.name,
        "project_slug": slug,
        "project_root": str(root),
        "project_scope": args.scope,
        "scope": args.scope,
        "execution_mode": args.execution_mode,
        "output_goal": args.output_goal,
        "quality_mode": args.quality_mode,
        "album_type": args.album_type or args.scope,
        "track_count": args.tracks,
        "tracks_total": args.tracks,
        "target_model": args.model,
        "model": args.model,
        "target_provider": provider_id,
        "provider_profile_path": args.provider_profile,
        "provider_profile": args.provider_profile,
        "tag_profile": args.tag_profile,
        "lyric_language": args.lyric_language,
        "prompt_language": args.prompt_language,
        "reference_policy": args.reference_policy,
        "lyrics_optimizer_policy": "disabled_except_diagnostic_baseline",
        "target_quality_bar": args.target_quality_bar,
        "agent_expertise_assumption": "non_expert_agent_requires_embedded_training",
        "require_artifact_freshness": True,
        "require_quote_verification": True,
        "require_complete_variant_packets": True,
        "require_api_payload_export_for_minimax_ready": True,
        "created_at": now_iso(),
        "assumptions_to_document": args.assumption or [],
        "assumptions": args.assumption or [],
    }
    state = {
        "project_id": project_id,
        "project_name": args.name,
        "project_slug": slug,
        "project_root": str(root),
        "phase": "intake",
        "output_goal": args.output_goal,
        "overall_status": "in_progress",
        "artifact_root": str(root),
        "tracks_total": args.tracks,
        "tracks": tracks,
        "album": {"foundation_score": None, "style_map_score": None, "sequence_score": None, "final_aandr_status": "not_ready"},
        "album_canon": {"path": None, "open_debts": []},
        "propagation_debts": [],
        "controller": {
            "phase_order_path": "references/controller/phase_order.json",
            "gate_requirements_path": "references/controller/gate_requirements.json",
            "phase_applicability_path": "references/controller/phase_applicability.json",
            "last_gate_check": None,
            "last_validation": None,
            "last_snapshot": None,
            "last_reconcile": None,
        },
        "blocking_issues": [],
        "next_actions": ["Complete intent intake and project configuration artifacts."],
        "updated_at": now_iso(),
    }
    manifest = {
        "project_name": args.name,
        "project_slug": slug,
        "project_root": str(root),
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "current_state_path": "state.json",
        "artifacts": [],
    }
    write_json(root / "project_config.json", config)
    write_json(root / "state.json", state)
    write_json(root / "project_manifest.json", manifest)
    if not (root / "intent_intake.json").exists():
        write_json(root / "intent_intake.json", {"status": "pending", "created_at": now_iso(), "user_request_summary": "", "material_assumptions": []})
    if not (root / "seed.txt").exists():
        (root / "seed.txt").write_text(args.name + "\n", encoding="utf-8")
    if not (root / "source_notes.md").exists():
        (root / "source_notes.md").write_text("# Source Notes\n\n", encoding="utf-8")
    if not (root / "results.tsv").exists():
        with (root / "results.tsv").open("w", encoding="utf-8", newline="") as f:
            csv.DictWriter(f, fieldnames=RESULTS_FIELDS, delimiter="\t").writeheader()
    refresh_manifest(root, quiet=True)
    print(f"Initialized AutoAlbum project: {root}")
    return 0


def json_sanity(project: Path) -> List[str]:
    errors = []
    for p in iter_files(project):
        if p.suffix.lower() in {".json", ".jsonl"}:
            rel = p.relative_to(project).as_posix()
            try:
                if p.suffix.lower() == ".jsonl":
                    for idx, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
                        if line.strip():
                            json.loads(line)
                else:
                    load_json(p)
            except Exception as e:
                errors.append(f"{rel}: {e}")
    return errors


def schema_validation(project: Path) -> List[str]:
    errors: List[str] = []
    if jsonschema is None:
        return ["jsonschema package not available; schema validation skipped"]
    for p in iter_files(project):
        if p.suffix.lower() != ".json":
            continue
        rel = p.relative_to(project).as_posix()
        schema_rel = schema_for_rel(rel)
        if not schema_rel:
            continue
        schema_path = SKILL_DIR / schema_rel
        if not schema_path.exists():
            errors.append(f"{rel}: schema missing at {schema_rel}")
            continue
        try:
            jsonschema.validate(instance=load_json(p), schema=load_json(schema_path))
        except Exception as e:
            errors.append(f"{rel}: schema validation failed against {schema_rel}: {e}")
    return errors


def required_paths_for_phase(project: Path, phase: str) -> List[str]:
    req = load_gates()["requirements"].get(phase, {})
    state = load_json(project / "state.json") if (project / "state.json").exists() else {}
    paths = list(req.get("all", []))
    for nn in track_numbers(project, state):
        for pattern in req.get("track", []):
            paths.append(pattern.replace("{NN}", nn))
    return paths


def check_gate(project: Path, phase: str) -> Tuple[bool, List[str], List[str]]:
    if phase not in phase_ids():
        return False, [f"Unknown phase: {phase}"], []
    missing = []
    present = []
    for rel in required_paths_for_phase(project, phase):
        p = project / rel
        if p.exists():
            if p.is_dir() and rel.endswith("renders/raw"):
                if any(p.iterdir()):
                    present.append(rel)
                else:
                    missing.append(rel + " (directory exists but contains no render files)")
            else:
                present.append(rel)
        else:
            missing.append(rel)
    return not missing, missing, present


def gate_needed_for_phase(project: Path, phase: str, force: bool = False) -> Tuple[bool, str, str]:
    code, label = phase_applicability(project, phase)
    if code == "S" and not force:
        return False, code, label
    return True, code, label


def collect_artifact_hashes(project: Path) -> Dict[str, str]:
    return {p.relative_to(project).as_posix(): sha256_file(p) for p in iter_files(project)}


def hash_artifacts_cmd(args: argparse.Namespace) -> int:
    project = project_path_arg(args.project)
    hashes = collect_artifact_hashes(project)
    out = {"project": str(project), "generated_at": now_iso(), "hashes": hashes}
    write_json(project / "ops" / "hashes" / "artifact_hashes.json", out)
    refresh_manifest(project, quiet=True)
    print(f"Hashed {len(hashes)} artifacts -> {project / 'ops/hashes/artifact_hashes.json'}")
    return 0


def _json_artifacts(project: Path) -> Iterable[Tuple[Path, Dict[str, Any]]]:
    for p in iter_files(project):
        if p.suffix.lower() == ".json":
            try:
                yield p, load_json(p)
            except Exception:
                continue


def _find_review_metadata(obj: Any) -> List[Dict[str, Any]]:
    metas=[]
    def rec(x: Any):
        if isinstance(x, dict):
            if "evaluated_artifact_path" in x and "evaluated_artifact_hash" in x:
                metas.append(x)
            for v in x.values(): rec(v)
        elif isinstance(x, list):
            for v in x: rec(v)
    rec(obj)
    return metas


def verify_freshness(project: Path) -> List[str]:
    errors=[]
    for p,obj in _json_artifacts(project):
        rel=p.relative_to(project).as_posix()
        # Only enforce metadata for evaluation-like JSONs that explicitly claim to be reviews/evals/lints.
        if EVAL_NAME_RE.search(p.name) or any(part in {"reviews"} for part in p.relative_to(project).parts):
            metas=_find_review_metadata(obj)
            # If a generated eval lacks metadata, warn/fail for known important eval files.
            if not metas and p.name in {"line_polish_review.json","lyrics_verifier_review.json","prompt_packet_verifier_review.json","prompt_lint_report.json","prompt_budget_report.json","unified_eval.json","adversarial_song_edit.json","adversarial_packet_edit.json","songcraft_eval.json","minimax_eval.json","style_fidelity_report.json","prosody_review.json"}:
                errors.append(f"{rel}: missing evaluated_artifact_path/evaluated_artifact_hash metadata")
            for meta in metas:
                art=meta.get("evaluated_artifact_path")
                expected=meta.get("evaluated_artifact_hash")
                if not art or not expected:
                    errors.append(f"{rel}: incomplete evaluated artifact metadata")
                    continue
                art_path=project/art
                if not art_path.exists():
                    errors.append(f"{rel}: evaluated artifact does not exist: {art}")
                    continue
                actual=sha256_file(art_path)
                if actual != expected:
                    errors.append(f"{rel}: stale review for {art}; expected {expected}, current {actual}")
    return errors


def verify_freshness_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors=verify_freshness(project)
    report={"project":str(project),"checked_at":now_iso(),"passed":not errors,"errors":errors}
    write_json(project/"reviews/controller/freshness_verification.json",report)
    if errors:
        print("Freshness FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("Freshness PASS")
    return 0


def _flatten_strings(obj: Any) -> Iterable[Tuple[str,str]]:
    def rec(x: Any, path: str):
        if isinstance(x, dict):
            for k,v in x.items():
                yield from rec(v, f"{path}.{k}" if path else str(k))
        elif isinstance(x, list):
            for i,v in enumerate(x):
                yield from rec(v, f"{path}[{i}]")
        elif isinstance(x, str):
            yield path, x
    yield from rec(obj, "")


def likely_quote_key(path: str) -> bool:
    p=path.lower()
    return any(k in p for k in ["quoted", "quote", "line", "excerpt", "source_line", "weak_lines", "evidence"])


def verify_quotes(project: Path) -> List[str]:
    errors=[]
    required_meta_names={"line_polish_review.json","lyrics_verifier_review.json","prompt_packet_verifier_review.json","prompt_budget_report.json","unified_eval.json","adversarial_song_edit.json","adversarial_packet_edit.json","songcraft_eval.json","minimax_eval.json","style_fidelity_report.json","prosody_review.json"}
    for p,obj in _json_artifacts(project):
        rel=p.relative_to(project).as_posix()
        metas=_find_review_metadata(obj)
        if not metas:
            if p.name in required_meta_names:
                errors.append(f"{rel}: cannot verify quotes because evaluated_artifact_path/evaluated_artifact_hash metadata is missing")
            continue
        # Use first evaluated artifact as source text for quote grounding.
        art=metas[0].get("evaluated_artifact_path")
        if not art or not (project/art).exists():
            continue
        source=(project/art).read_text(encoding="utf-8", errors="ignore")
        for key,s in _flatten_strings(obj):
            if not likely_quote_key(key):
                continue
            candidate=s.strip()
            if len(candidate)<8 or len(candidate)>200:
                continue
            # Skip issue descriptions that are obviously not quotes.
            if any(word in key.lower() for word in ["issue","rationale","decision","action","path","hash","type"]):
                continue
            if candidate.startswith("sha256:"):
                continue
            # If it contains newlines, check each substantial line.
            parts=[x.strip() for x in candidate.splitlines() if len(x.strip())>=8]
            for part in parts[:8]:
                if part not in source:
                    # Allow partial punctuation normalization.
                    norm=lambda z: re.sub(r"\s+"," ",re.sub(r"[^\w\s']","",z)).strip().lower()
                    if norm(part) and norm(part) not in norm(source):
                        errors.append(f"{rel}: quoted/evidence line not found in {art}: {part[:100]}")
    return errors


def verify_quotes_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors=verify_quotes(project)
    report={"project":str(project),"checked_at":now_iso(),"passed":not errors,"errors":errors}
    write_json(project/"reviews/controller/quote_verification.json",report)
    if errors:
        print("Quote verification FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("Quote verification PASS")
    return 0


def style_selection_obj(project: Path) -> Dict[str, Any]:
    p=project/"style_catalog_outputs/style_selection.json"
    return load_json(p) if p.exists() else {}


def find_selected_catalog_files(obj: Any) -> List[str]:
    files=[]
    def rec(x: Any):
        if isinstance(x, dict):
            for k,v in x.items():
                if k in {"selected_catalog_files","catalog_files","source_catalog_files","required_catalog_files"} and isinstance(v,list):
                    files.extend([str(i) for i in v])
                else:
                    rec(v)
        elif isinstance(x, list):
            for v in x: rec(v)
    rec(obj)
    return files


def find_style_weights(obj: Any) -> List[Tuple[str,float]]:
    out=[]
    def consider(d: Dict[str,Any]):
        name=d.get("style") or d.get("name") or d.get("label") or d.get("style_id")
        w=d.get("weight") or d.get("weight_percent") or d.get("percentage")
        if name is not None and isinstance(w,(int,float)):
            out.append((str(name), float(w)))
    def rec(x: Any):
        if isinstance(x, dict):
            consider(x)
            for v in x.values(): rec(v)
        elif isinstance(x, list):
            for v in x: rec(v)
    rec(obj)
    return out


def verify_style(project: Path) -> Tuple[List[str], Dict[str, Any]]:
    errors=[]
    obj=style_selection_obj(project)
    if not obj:
        return ["style_catalog_outputs/style_selection.json missing or empty"], {}
    files=find_selected_catalog_files(obj)
    valid_files=[]
    for f in files:
        clean=f.strip().lstrip("/")
        if not clean.startswith("references/style_catalog/"):
            errors.append(f"selected catalog file is not under references/style_catalog/: {f}")
            continue
        if not (SKILL_DIR/clean).exists():
            errors.append(f"selected catalog file does not exist: {f}")
            continue
        valid_files.append(clean)
    # If style implies rap, require rap_current catalog.
    text=json.dumps(obj, ensure_ascii=False).lower()
    rap_terms=["rap","hip-hop","hiphop","trap","drill","rage","pluggnb","memphis","florida"]
    if any(t in text for t in rap_terms) and not any("references/style_catalog/rap_current" in f for f in valid_files):
        errors.append("rap/hip-hop/trap style selected but no references/style_catalog/rap_current file was loaded")
    weights=find_style_weights(obj)
    if weights:
        total=sum(w for _,w in weights)
        if not (99 <= total <= 101 or 0.99 <= total <= 1.01):
            errors.append(f"style weights do not sum to 100% or 1.0: {total}")
        for name,w in weights:
            if w>0 and not any(name.lower().replace(" ","_") in Path(f).name.lower() or name.lower().split()[0] in f.lower() for f in valid_files):
                # not fatal for artist-file profiles, but flag if obviously invented composite and no selected files at all.
                if not valid_files:
                    errors.append(f"weighted style component lacks a loaded fingerprint: {name} ({w})")
    report={
        "selected_catalog_files_valid": not errors,
        "style_weights_valid": not any("weights" in e for e in errors),
        "selected_catalog_files": files,
        "valid_catalog_files": valid_files,
        "blocking_issues": errors,
        "approved": not errors,
        "checked_at": now_iso(),
    }
    return errors, report


def verify_style_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors,report=verify_style(project)
    write_json(project/"style_catalog_outputs/style_catalog_verification.json",report)
    if errors:
        print("Style catalog verification FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("Style catalog verification PASS")
    return 0


def score_from_candidate(c: Dict[str,Any]) -> Optional[float]:
    for key in ["score","aggregate_score","overall_score","total_score","weighted_score"]:
        v=c.get(key)
        if isinstance(v,(int,float)):
            return float(v)
    # Average numeric scorecard
    for key in ["scores","scorecard"]:
        d=c.get(key)
        if isinstance(d,dict):
            nums=[float(v) for v in d.values() if isinstance(v,(int,float))]
            if nums: return sum(nums)/len(nums)
    return None


def candidate_name(c: Dict[str,Any]) -> str:
    for key in ["id","candidate_id","name","title","hook","concept","label"]:
        if key in c: return str(c[key])
    return ""


def verify_tournaments(project: Path) -> List[str]:
    errors=[]
    for p in iter_files(project):
        if "tournament" not in p.name.lower() or p.suffix.lower() != ".json":
            continue
        rel=p.relative_to(project).as_posix()
        try: obj=load_json(p)
        except Exception: continue
        candidates=obj.get("candidates") or []
        if not isinstance(candidates,list) or not candidates:
            continue
        selected=str(obj.get("selected_candidate") or obj.get("selected_hook") or obj.get("winner") or "")
        scored=[]
        for c in candidates:
            if isinstance(c,dict):
                sc=score_from_candidate(c)
                nm=candidate_name(c)
                if sc is not None and nm:
                    scored.append((nm,sc))
        if scored and selected:
            top=max(scored,key=lambda x:x[1])
            sel_score=next((s for n,s in scored if selected in n or n in selected), None)
            if sel_score is not None and sel_score + 1e-9 < top[1]:
                override=obj.get("override_reason") or obj.get("selection_override_reason") or obj.get("rationale")
                if not override or len(str(override).strip())<30:
                    errors.append(f"{rel}: selected {selected!r} scored {sel_score}, below top {top[0]!r} {top[1]}, without explicit override_reason")
        scope=str(obj.get("scope") or read_project_config(project).get("project_scope") or "").lower()
        criteria_text=json.dumps(obj.get("criteria") or obj.get("score_dimensions") or {}, ensure_ascii=False).lower()
        if scope in {"single_track","lead_single"} and any(x in criteria_text for x in ["album depth","album arc","album sequencing","album expansion"]):
            errors.append(f"{rel}: single/lead-single tournament uses album-only criteria")
    return errors


def verify_tournaments_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors=verify_tournaments(project)
    report={"project":str(project),"checked_at":now_iso(),"passed":not errors,"errors":errors}
    write_json(project/"reviews/controller/tournament_verification.json",report)
    if errors:
        print("Tournament verification FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("Tournament verification PASS")
    return 0


def provider_profile(project: Path) -> Dict[str,Any]:
    cfg=read_project_config(project)
    pp=cfg.get("provider_profile_path") or cfg.get("provider_profile") or "references/api/provider_profiles/direct_minimax_api.json"
    p=SKILL_DIR/pp
    return load_json(p) if p.exists() else {"provider_id": Path(pp).stem}


def prompt_and_lyrics_paths(project: Path, nn: str) -> Tuple[Path, Path]:
    tr=project/"tracks"/f"tr_{nn}"
    return tr/"prompt_minimax.txt", tr/"lyrics_minimax.txt"


def lint_prompt_for_track(project: Path, nn: str) -> Dict[str,Any]:
    cfg=read_project_config(project)
    prof=provider_profile(project)
    prompt_path, lyrics_path = prompt_and_lyrics_paths(project, nn)
    prompt=prompt_path.read_text(encoding="utf-8", errors="ignore") if prompt_path.exists() else ""
    lyrics=lyrics_path.read_text(encoding="utf-8", errors="ignore") if lyrics_path.exists() else ""
    errors=[]; warnings=[]
    prompt_lang=str(cfg.get("prompt_language","English")).lower()
    lyric_lang=str(cfg.get("lyric_language","English")).lower()
    if "english" in prompt_lang and CJK_RE.search(prompt):
        errors.append("Prompt contains CJK/non-English characters in an English-prompt project")
    if not prompt_path.exists() or not prompt.strip():
        errors.append("Prompt file missing or empty")
    if len(prompt)>2000:
        errors.append(f"Prompt exceeds direct MiniMax 2000 character guideline: {len(prompt)}")
    if lyrics and len(lyrics)>3500:
        errors.append(f"Lyrics exceed MiniMax 3500 character guideline: {len(lyrics)}")
    if re.search(r"avoid loops", prompt, re.I):
        warnings.append("Prompt says 'avoid loops'; clarify this for loop-based genres as 'avoid a static one-loop arrangement'")
    precise_terms=["exactly", "db", "compressor", "eq at", "reverb at", "pitch shift", "pitch slightly", "light reverb"]
    if any(t in prompt.lower() for t in precise_terms):
        warnings.append("Prompt may contain over-precise engineering controls; phrase as perceptual sonic intent")
    if prompt.count("-")>18 or prompt.count(";")>12:
        warnings.append("Prompt may be too spec-sheet-like; MiniMax usually benefits from vivid concise prose")
    report={
        "track_number": int(nn),
        "prompt_path": prompt_path.relative_to(project).as_posix(),
        "prompt_hash": sha256_file(prompt_path) if prompt_path.exists() else "",
        "evaluated_artifact_path": prompt_path.relative_to(project).as_posix(),
        "evaluated_artifact_hash": sha256_file(prompt_path) if prompt_path.exists() else "",
        "provider_profile": prof.get("provider_id") or prof.get("name") or "unknown",
        "prompt_char_count": len(prompt),
        "lyrics_char_count": len(lyrics),
        "blocking_issues": errors,
        "warnings": warnings,
        "approved": not errors,
        "checked_at": now_iso(),
    }
    return report


def lint_prompt_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    all_errors=[]
    for nn in track_numbers(project):
        report=lint_prompt_for_track(project,nn)
        write_json(project/"tracks"/f"tr_{nn}"/"prompt_lint_report.json", report)
        all_errors.extend([f"tr_{nn}: {e}" for e in report["blocking_issues"]])
    if all_errors:
        print("Prompt lint FAIL")
        for e in all_errors: print(f"  - {e}")
        return 1
    print("Prompt lint PASS")
    return 0


def variant_paths(project: Path, nn: str) -> List[Path]:
    vdir=project/"tracks"/f"tr_{nn}"/"variants"
    return sorted(vdir.glob("*.json")) if vdir.exists() else []


def verify_variants(project: Path) -> List[str]:
    errors=[]
    if jsonschema is None:
        return ["jsonschema package not available; cannot validate variants"]
    schema=load_json(SKILL_DIR/"references/schemas/generation_packet.schema.json")
    for nn in track_numbers(project):
        variants=variant_paths(project,nn)
        needed={"A_on_brief","B_hook_forward","C_bold"}
        present={p.stem for p in variants}
        missing=needed-present
        for m in sorted(missing):
            errors.append(f"tracks/tr_{nn}/variants/{m}.json missing")
        for p in variants:
            rel=p.relative_to(project).as_posix()
            try:
                obj=load_json(p)
                jsonschema.validate(instance=obj, schema=schema)
                if obj.get("track_number") != int(nn):
                    errors.append(f"{rel}: track_number does not match folder tr_{nn}")
                if not obj.get("prompt") or not obj.get("audio_setting"):
                    errors.append(f"{rel}: not a complete renderable packet")
            except Exception as e:
                errors.append(f"{rel}: variant packet invalid: {e}")
    return errors


def verify_variants_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors=verify_variants(project)
    report={"project":str(project),"checked_at":now_iso(),"passed":not errors,"errors":errors}
    write_json(project/"reviews/controller/variant_verification.json",report)
    if errors:
        print("Variant verification FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("Variant verification PASS")
    return 0


def packet_to_payload(packet: Dict[str,Any]) -> Dict[str,Any]:
    payload={
        "model": packet.get("model","music-2.6"),
        "prompt": packet.get("prompt",""),
        "lyrics_optimizer": bool(packet.get("lyrics_optimizer", False)),
        "is_instrumental": bool(packet.get("is_instrumental", False)),
        "audio_setting": packet.get("audio_setting", {"sample_rate":44100,"bitrate":256000,"format":"mp3"}),
    }
    if not payload["is_instrumental"] and not payload["lyrics_optimizer"]:
        payload["lyrics"] = packet.get("lyrics", "")
    if packet.get("provider") == "direct_minimax_api" or packet.get("output_format"):
        payload["output_format"] = packet.get("output_format","url")
        payload["stream"] = bool(packet.get("stream", False))
    return payload


def export_payloads_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    outdir=project/"generation/payloads"
    outdir.mkdir(parents=True, exist_ok=True)
    jsonl=[]; errors=[]
    for nn in track_numbers(project):
        tr=project/"tracks"/f"tr_{nn}"
        packets=[]
        base=tr/"generation_packet.json"
        if base.exists():
            packets.append(("base", base))
        for p in variant_paths(project,nn):
            packets.append((p.stem, p))
        schema = load_json(SKILL_DIR/"references/schemas/generation_packet.schema.json") if (SKILL_DIR/"references/schemas/generation_packet.schema.json").exists() else None
        for variant,path in packets:
            try:
                packet=load_json(path)
                if jsonschema is not None and schema is not None:
                    jsonschema.validate(instance=packet, schema=schema)
                payload=packet_to_payload(packet)
                name=f"tr_{nn}_{variant}_take_01.json" if variant!="base" else f"tr_{nn}_base_take_01.json"
                # For canonical required variants, exact names expected by gates.
                if variant in {"A_on_brief","B_hook_forward","C_bold"}:
                    name=f"tr_{nn}_{variant}_take_01.json"
                dest=outdir/name
                write_json(dest,payload)
                jsonl.append(payload | {"_autoalbum_payload_path": dest.relative_to(project).as_posix(), "_source_packet": path.relative_to(project).as_posix()})
            except Exception as e:
                errors.append(f"{path.relative_to(project).as_posix()}: {e}")
    with (project/"generation/api_payloads.jsonl").open("w",encoding="utf-8") as f:
        for row in jsonl:
            f.write(json.dumps(row,ensure_ascii=False)+"\n")
    refresh_manifest(project, quiet=True)
    if errors:
        print("Payload export completed with errors")
        for e in errors: print(f"  - {e}")
        return 1
    print(f"Exported {len(jsonl)} payloads")
    return 0

def verify_payloads(project: Path) -> List[str]:
    errors=[]
    cfg=read_project_config(project)
    output_goal=cfg.get("output_goal") or "release_package"
    requires_payloads=output_goal in {"minimax_ready_packets","generated_candidates","selected_album_sequence","release_package"}
    if not requires_payloads:
        return errors
    jsonl_path=project/"generation/api_payloads.jsonl"
    if not jsonl_path.exists():
        errors.append("generation/api_payloads.jsonl missing for output goal requiring MiniMax-ready payloads")
    schema_path=SKILL_DIR/"references/schemas/minimax_payload.schema.json"
    schema=load_json(schema_path) if schema_path.exists() else None
    for nn in track_numbers(project):
        for variant in ["A_on_brief","B_hook_forward","C_bold"]:
            rel=f"generation/payloads/tr_{nn}_{variant}_take_01.json"
            p=project/rel
            if not p.exists():
                errors.append(f"{rel} missing")
                continue
            if jsonschema is not None and schema is not None:
                try:
                    jsonschema.validate(instance=load_json(p), schema=schema)
                except Exception as e:
                    errors.append(f"{rel}: payload schema invalid: {e}")
    return errors


def verify_payloads_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors=verify_payloads(project)
    report={"project":str(project),"checked_at":now_iso(),"passed":not errors,"errors":errors}
    write_json(project/"reviews/controller/payload_verification.json",report)
    if errors:
        print("Payload verification FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("Payload verification PASS")
    return 0


def verify_state_consistency(project: Path) -> List[str]:
    errors=[]
    sp=project/"state.json"
    if not sp.exists():
        return ["state.json missing"]
    state=load_json(sp)
    if state.get("phase")=="complete" and state.get("overall_status")!="complete":
        errors.append("state phase is complete but overall_status is not complete")
    for nn in track_numbers(project,state):
        tr=project/"tracks"/f"tr_{nn}"
        packet=(tr/"generation_packet.json").exists()
        variants=variant_paths(project,nn)
        st=state.get("tracks",{}).get(nn,{})
        if packet and variants and st.get("status") in {"not_started","lyrics_ready",None,""}:
            errors.append(f"tracks.{nn}.status is {st.get('status')!r} despite packet/variants existing; run reconcile-state")
        if packet and st.get("decision") in {"not_started",None,""}:
            errors.append(f"tracks.{nn}.decision is {st.get('decision')!r} despite packet existing; run reconcile-state")
    return errors


def verify_state_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors=verify_state_consistency(project)
    report={"project":str(project),"checked_at":now_iso(),"passed":not errors,"errors":errors}
    write_json(project/"reviews/controller/state_consistency_verification.json",report)
    if errors:
        print("State consistency FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("State consistency PASS")
    return 0


def full_content_validation(project: Path) -> List[str]:
    errors=[]
    errors.extend(json_sanity_and_schema(project))
    errors.extend(verify_freshness(project))
    errors.extend(verify_quotes(project))
    errors.extend(verify_tournaments(project))
    errors.extend(verify_variants(project))
    if (project/"style_catalog_outputs/style_selection.json").exists():
        errors.extend(verify_style(project)[0])
    errors.extend(verify_payloads(project))
    errors.extend(verify_state_consistency(project))
    for nn in track_numbers(project):
        rep=lint_prompt_for_track(project,nn)
        errors.extend([f"tr_{nn}: {e}" for e in rep.get("blocking_issues",[])])
    return errors


def preflight_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    if args.reconcile and (project/"state.json").exists():
        reconcile_state(project)
    refresh_manifest(project, quiet=True)
    errors=full_content_validation(project)
    report={"project":str(project),"checked_at":now_iso(),"passed":not errors,"errors":errors}
    write_json(project/"reviews/controller/production_preflight.json",report)
    if errors:
        print("Production preflight FAIL")
        for e in errors: print(f"  - {e}")
        return 1
    print("Production preflight PASS")
    return 0



def reconcile_state(project: Path) -> Dict[str,Any]:
    state=load_json(project/"state.json")
    tracks=state.setdefault("tracks",{})
    for nn in track_numbers(project,state):
        tr=project/"tracks"/f"tr_{nn}"
        item=tracks.setdefault(nn,{"paths":{},"scores":{},"variants":{},"renders":{},"status":"not_started","decision":"not_started"})
        paths=item.setdefault("paths",{})
        def mark(key, rel):
            if (project/rel).exists(): paths[key]=rel
        mark("lyrics_working",f"tracks/tr_{nn}/lyrics_working.md")
        mark("lyrics_minimax",f"tracks/tr_{nn}/lyrics_minimax.txt")
        mark("prompt_minimax",f"tracks/tr_{nn}/prompt_minimax.txt")
        mark("generation_packet",f"tracks/tr_{nn}/generation_packet.json")
        mark("line_polish_review",f"tracks/tr_{nn}/line_polish_review.json")
        mark("prompt_lint_report",f"tracks/tr_{nn}/prompt_lint_report.json")
        variants=variant_paths(project,nn)
        item["variants"]={p.stem:p.relative_to(project).as_posix() for p in variants}
        renders=list((tr/"renders/raw").glob("*")) if (tr/"renders/raw").exists() else []
        item.setdefault("renders",{})["candidate_count"]=len([p for p in renders if p.is_file()])
        # derive status
        if paths.get("generation_packet") and item["variants"]:
            item["status"]="packet_ready"
            item["decision"]="ready_for_payload_export"
        elif paths.get("lyrics_minimax") or paths.get("lyrics_working"):
            item["status"]="lyrics_ready"
            item["decision"]="needs_packet"
        else:
            item["status"]="not_started"
            item["decision"]="not_started"
    state["updated_at"]=now_iso()
    state.setdefault("controller",{})["last_reconcile"]=now_iso()
    # Completion status sanity
    if state.get("phase")=="complete" and state.get("overall_status")!="complete":
        state.setdefault("blocking_issues",[]).append("phase is complete but overall_status is not complete")
    write_json(project/"state.json", state)
    refresh_manifest(project, quiet=True)
    return state


def reconcile_state_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    state=reconcile_state(project)
    print(json.dumps({"project":str(project),"phase":state.get("phase"),"overall_status":state.get("overall_status"),"tracks":state.get("tracks")},indent=2))
    return 0


def json_sanity_and_schema(project: Path) -> List[str]:
    errors=[]
    for required in ["state.json","project_config.json","project_manifest.json","results.tsv"]:
        if not (project/required).exists():
            errors.append(f"Missing root artifact: {required}")
    errors.extend(json_sanity(project))
    errors.extend(schema_validation(project))
    return errors


def validate_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    errors=json_sanity_and_schema(project)
    if args.deep:
        errors = full_content_validation(project)
    if not errors:
        sp=project/"state.json"
        if sp.exists():
            state=load_json(sp); state.setdefault("controller",{})["last_validation"]=now_iso(); state["updated_at"]=now_iso(); write_json(sp,state)
        print(f"Validation PASS: {project}")
        return 0
    print(f"Validation FAIL: {project}")
    for e in errors: print(f"  - {e}")
    return 1


def gate_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    phase=args.phase or load_json(project/"state.json").get("phase","intake")
    code,label=phase_applicability(project,phase)
    if code=="S" and not args.force:
        result={"project":str(project),"phase":phase,"passed":True,"skipped":True,"applicability":label,"present_count":0,"missing":[],"checked_at":now_iso()}
        print(json.dumps(result,indent=2) if args.json else f"Gate check: {phase} -> SKIP ({label})")
        if args.write_report: write_json(project/"reviews/controller"/f"gate_{phase}.json",result)
        return 0
    ok,missing,present=check_gate(project,phase)
    # content validators at sensitive gates.
    extra=[]
    if phase in {"style_resolution","completion_fit"} and (project/"style_catalog_outputs/style_selection.json").exists():
        extra.extend(verify_style(project)[0])
    if phase in {"concept_option_search","hook_title_tournament","completion_fit"}:
        extra.extend(verify_tournaments(project))
    if phase in {"line_polish","adversarial_song_edit","adversarial_packet_edit","packet_evaluation","completion_fit"}:
        extra.extend(verify_freshness(project)); extra.extend(verify_quotes(project))
    if phase in {"packet_evaluation","completion_fit"}:
        # run lint but don't write unless command called; check reports or current prompt.
        for nn in track_numbers(project):
            rep=lint_prompt_for_track(project,nn)
            extra.extend([f"tr_{nn}: {e}" for e in rep["blocking_issues"]])
    if phase in {"variant_strategy","payload_export","completion_fit"}:
        extra.extend(verify_variants(project))
    if phase in {"payload_export","completion_fit"}:
        extra.extend(verify_payloads(project))
    if phase == "completion_fit":
        # Completion must pass the same deep content checks as production preflight.
        extra.extend(full_content_validation(project))
    missing_all=missing+extra
    result={"project":str(project),"phase":phase,"passed":not missing_all,"skipped":False,"applicability":label,"present_count":len(present),"missing":missing_all,"checked_at":now_iso()}
    if args.json: print(json.dumps(result,indent=2))
    else:
        print(f"Gate check: {phase} -> {'PASS' if not missing_all else 'FAIL'} ({label})")
        for m in missing_all: print(f"  - {m}")
    if args.write_report: write_json(project/"reviews/controller"/f"gate_{phase}.json",result)
    return 0 if not missing_all else 1


def advance_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    state=load_json(project/"state.json")
    current=state.get("phase","intake")
    target=args.to or next_phase(current)
    if not target:
        print(f"ERROR: cannot determine next phase from {current}",file=sys.stderr); return 2
    ids=phase_ids()
    if target not in ids:
        print(f"ERROR: unknown target phase {target}",file=sys.stderr); return 2
    expected=next_phase(current)
    if args.to and target!=expected and not args.allow_jump:
        print(f"ERROR: refusing non-sequential advance {current} -> {target}. Expected next phase: {expected}. Use --allow-jump only for documented recovery/replanning.",file=sys.stderr); return 2
    if args.require_gate:
        should,code,label=gate_needed_for_phase(project,current)
        if should:
            ok,missing,_=check_gate(project,current)
            extra=[]
            if current in {"style_resolution","completion_fit"} and (project/"style_catalog_outputs/style_selection.json").exists():
                extra.extend(verify_style(project)[0])
            if current in {"concept_option_search","hook_title_tournament","completion_fit"}:
                extra.extend(verify_tournaments(project))
            if current in {"line_polish","adversarial_song_edit","adversarial_packet_edit","packet_evaluation","completion_fit"}:
                extra.extend(verify_freshness(project)); extra.extend(verify_quotes(project))
            if current in {"packet_evaluation","completion_fit"}:
                for nn in track_numbers(project):
                    rep=lint_prompt_for_track(project,nn)
                    extra.extend([f"tr_{nn}: {e}" for e in rep["blocking_issues"]])
            if current in {"variant_strategy","payload_export","completion_fit"}:
                extra.extend(verify_variants(project))
            if current in {"payload_export","completion_fit"}:
                extra.extend(verify_payloads(project))
            if current == "completion_fit":
                extra.extend(full_content_validation(project))
            all_missing=missing+extra
            if all_missing:
                print(f"Cannot advance; current phase gate failed: {current} ({label})")
                for m in all_missing: print(f"  - {m}")
                return 1
        else:
            append_result(project,{"timestamp":now_iso(),"phase":current,"status":"skipped_gate","decision":f"advance_allowed:{code}","path":"state.json","notes":label})
    state["phase"]=target; state["updated_at"]=now_iso(); state["next_actions"]=[f"Complete phase: {target}"]
    write_json(project/"state.json",state)
    append_result(project,{"timestamp":now_iso(),"phase":current,"status":"advanced","decision":f"advance_to:{target}","path":"state.json"})
    refresh_manifest(project,quiet=True)
    print(f"Advanced {project.name}: {current} -> {target}")
    return 0


def status_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    state=load_json(project/"state.json")
    phase=state.get("phase","intake")
    should,code,label=gate_needed_for_phase(project,phase)
    ok=True; missing=[]
    if should: ok,missing,_=check_gate(project,phase)
    print(json.dumps({"project":str(project),"phase":phase,"phase_applicability":label,"phase_applicability_code":code,"overall_status":state.get("overall_status"),"output_goal":state.get("output_goal"),"tracks_total":state.get("tracks_total"),"current_gate_passed":ok,"current_gate_skipped":not should,"missing_for_current_phase":missing,"next_phase":next_phase(phase),"blocking_issues":state.get("blocking_issues",[]),"next_actions":state.get("next_actions",[])},indent=2))
    return 0 if ok else 1


def snapshot_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project); label=slugify(args.label or "snapshot")
    ts=_dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest=project/".autoalbum_snapshots"/f"{ts}_{label}"; dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copytree(project,dest,ignore=lambda d,n: {".autoalbum_snapshots"}&set(n))
    state=load_json(project/"state.json"); state.setdefault("controller",{})["last_snapshot"]=dest.name; write_json(project/"state.json",state)
    append_result(project,{"timestamp":now_iso(),"phase":state.get("phase"),"status":"snapshot","decision":label,"path":str(dest.relative_to(project))})
    print(f"Snapshot created: {dest}")
    return 0


def rollback_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project); snap_dir=project/".autoalbum_snapshots"
    snap=snap_dir/args.snapshot if args.snapshot else (sorted([p for p in snap_dir.glob("*") if p.is_dir()])[-1] if snap_dir.exists() and list(snap_dir.glob("*")) else None)
    if not snap or not snap.exists(): print("ERROR: snapshot not found",file=sys.stderr); return 2
    before=snap_dir/(now_iso().replace(":","")+"_pre_rollback_backup")
    shutil.copytree(project,before,ignore=lambda d,n: {".autoalbum_snapshots"}&set(n))
    for item in project.iterdir():
        if item.name==".autoalbum_snapshots": continue
        if item.is_dir(): shutil.rmtree(item)
        else: item.unlink()
    for item in snap.iterdir():
        dest=project/item.name
        if item.is_dir(): shutil.copytree(item,dest)
        else: shutil.copy2(item,dest)
    print(f"Rolled back to {snap.name}; pre-rollback backup: {before.name}")
    return 0


def route_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    state=load_json(project/"state.json") if (project/"state.json").exists() else {}
    output_goal=args.output_goal or state.get("output_goal") or "release_package"
    phases=load_phases(); route=[]
    for p in phases:
        if p["id"]=="complete": continue
        code,label=phase_applicability(project,p["id"])
        route.append({"phase":p["id"],"label":p.get("label",""),"stage_doc":p.get("stage_doc"),"applicability_code":code,"applicability":label})
    print(json.dumps({"project":str(project),"output_goal":output_goal,"route":route},indent=2))
    return 0


def list_phases_cmd(args: argparse.Namespace) -> int:
    for p in load_phases(): print(f"{p['id']}\t{p['label']}")
    return 0


def record_result_cmd(args: argparse.Namespace) -> int:
    project=project_path_arg(args.project)
    row={"timestamp":now_iso(),"phase":args.phase or (load_json(project/"state.json").get("phase") if (project/"state.json").exists() else ""),"artifact_id":args.artifact_id or "","track_number":args.track_number or "","variant":args.variant or "","score_type":args.score_type or "","score":args.score if args.score is not None else "","status":args.status or "recorded","decision":args.decision or "","path":args.path or "","notes":args.notes or ""}
    append_result(project,row); print(f"Recorded result in {project/'results.tsv'}"); return 0


def completion_score_cap_cmd(args: argparse.Namespace) -> int:
    """Diagnostic command: prints objective score caps implied by current artifacts."""
    project=project_path_arg(args.project); caps=[]
    if verify_freshness(project): caps.append({"dimension":"stale_reviews","cap":4.0})
    if verify_quotes(project): caps.append({"dimension":"quote_grounding","cap":3.0})
    if verify_variants(project): caps.append({"dimension":"variant_readiness","cap":5.0})
    if (project/"style_catalog_outputs/style_selection.json").exists() and verify_style(project)[0]: caps.append({"dimension":"style_resolution","cap":5.0})
    if verify_payloads(project): caps.append({"dimension":"payload_readiness","cap":5.5})
    if verify_state_consistency(project): caps.append({"dimension":"completion_consistency","cap":6.0})
    for nn in track_numbers(project):
        rep=lint_prompt_for_track(project,nn)
        if rep["blocking_issues"]: caps.append({"dimension":f"tr_{nn}_prompt_readiness","cap":6.0,"issues":rep["blocking_issues"]})
    print(json.dumps({"project":str(project),"score_caps":caps},indent=2))
    return 0 if not caps else 1


def main(argv: Optional[List[str]]=None) -> int:
    parser=argparse.ArgumentParser(description="AutoAlbum agent-native workflow guard v24")
    sub=parser.add_subparsers(dest="cmd",required=True)
    p=sub.add_parser("init",help="Initialize a project root and control files"); p.add_argument("name"); p.add_argument("--root",default="."); p.add_argument("--slug"); p.add_argument("--scope",default="album"); p.add_argument("--output-goal",default="release_package"); p.add_argument("--quality-mode",default="release_grade"); p.add_argument("--execution-mode",default="autonomous_full_pipeline"); p.add_argument("--album-type",default=None); p.add_argument("--model",default="music-2.6"); p.add_argument("--provider-profile",default="references/api/provider_profiles/direct_minimax_api.json"); p.add_argument("--tag-profile",default="direct_minimax_music_generation"); p.add_argument("--lyric-language",default="English"); p.add_argument("--prompt-language",default="English"); p.add_argument("--reference-policy",default="preserve_user_style_request_and_expand_to_musical_controls"); p.add_argument("--target-quality-bar",default="professional_major_release"); p.add_argument("--tracks",type=int,default=10); p.add_argument("--assumption",action="append"); p.add_argument("--force",action="store_true"); p.set_defaults(func=create_project)
    p=sub.add_parser("validate",help="Validate root files, JSON/JSONL syntax, known schemas; use --deep for freshness/style/tournament/variant checks"); p.add_argument("project"); p.add_argument("--deep",action="store_true"); p.set_defaults(func=validate_cmd)
    p=sub.add_parser("gate",help="Check required artifacts and content validators for a phase"); p.add_argument("project"); p.add_argument("--phase"); p.add_argument("--json",action="store_true"); p.add_argument("--write-report",action="store_true"); p.add_argument("--force",action="store_true"); p.set_defaults(func=gate_cmd)
    p=sub.add_parser("advance",help="Advance state.json to next/specified phase"); p.add_argument("project"); p.add_argument("--to"); p.add_argument("--require-gate",action="store_true"); p.add_argument("--allow-jump",action="store_true"); p.set_defaults(func=advance_cmd)
    p=sub.add_parser("status",help="Print current project state and gate status"); p.add_argument("project"); p.set_defaults(func=status_cmd)
    p=sub.add_parser("manifest",help="Refresh project_manifest.json with hashes"); p.add_argument("project"); p.set_defaults(func=lambda a: refresh_manifest(project_path_arg(a.project)))
    p=sub.add_parser("snapshot",help="Create transaction snapshot"); p.add_argument("project"); p.add_argument("--label",default="snapshot"); p.set_defaults(func=snapshot_cmd)
    p=sub.add_parser("rollback",help="Rollback project root to latest/named snapshot"); p.add_argument("project"); p.add_argument("--snapshot"); p.set_defaults(func=rollback_cmd)
    p=sub.add_parser("record-result",help="Append structured result row"); p.add_argument("project"); p.add_argument("--phase"); p.add_argument("--artifact-id"); p.add_argument("--track-number"); p.add_argument("--variant"); p.add_argument("--score-type"); p.add_argument("--score",type=float); p.add_argument("--status"); p.add_argument("--decision"); p.add_argument("--path"); p.add_argument("--notes"); p.set_defaults(func=record_result_cmd)
    p=sub.add_parser("route",help="Print phase route with applicability"); p.add_argument("project"); p.add_argument("--output-goal"); p.set_defaults(func=route_cmd)
    p=sub.add_parser("list-phases",help="List phase IDs"); p.set_defaults(func=list_phases_cmd)
    p=sub.add_parser("hash-artifacts",help="Write ops/hashes/artifact_hashes.json and refresh manifest"); p.add_argument("project"); p.set_defaults(func=hash_artifacts_cmd)
    p=sub.add_parser("verify-freshness",help="Fail stale review/eval artifacts"); p.add_argument("project"); p.set_defaults(func=verify_freshness_cmd)
    p=sub.add_parser("verify-quotes",help="Fail reviews quoting lines absent from current artifact"); p.add_argument("project"); p.set_defaults(func=verify_quotes_cmd)
    p=sub.add_parser("verify-style",help="Verify style_selection uses actual style catalog files"); p.add_argument("project"); p.set_defaults(func=verify_style_cmd)
    p=sub.add_parser("verify-tournaments",help="Verify tournament score/winner/scope consistency"); p.add_argument("project"); p.set_defaults(func=verify_tournaments_cmd)
    p=sub.add_parser("lint-prompt",help="Lint current MiniMax prompts and write prompt_lint_report.json"); p.add_argument("project"); p.set_defaults(func=lint_prompt_cmd)
    p=sub.add_parser("verify-variants",help="Verify variants are complete renderable generation packets"); p.add_argument("project"); p.set_defaults(func=verify_variants_cmd)
    p=sub.add_parser("export-payloads",help="Export provider-ready API payloads from packets and variants"); p.add_argument("project"); p.set_defaults(func=export_payloads_cmd)
    p=sub.add_parser("verify-payloads",help="Verify provider-ready API payloads exist and validate"); p.add_argument("project"); p.set_defaults(func=verify_payloads_cmd)
    p=sub.add_parser("verify-state",help="Verify state.json matches actual project artifacts"); p.add_argument("project"); p.set_defaults(func=verify_state_cmd)
    p=sub.add_parser("reconcile-state",help="Update state.json from actual artifacts"); p.add_argument("project"); p.set_defaults(func=reconcile_state_cmd)
    p=sub.add_parser("preflight",help="Run full production-test readiness checks; optionally reconcile state first"); p.add_argument("project"); p.add_argument("--reconcile",action="store_true"); p.set_defaults(func=preflight_cmd)
    p=sub.add_parser("score-caps",help="Show objective score caps implied by current blockers"); p.add_argument("project"); p.set_defaults(func=completion_score_cap_cmd)
    args=parser.parse_args(argv)
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
