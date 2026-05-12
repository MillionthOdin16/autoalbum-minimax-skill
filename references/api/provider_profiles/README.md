# Provider Profiles

These JSON files are the machine-readable constraint layer for MiniMax Music 2.6 provider routes. Every packet export must select one provider profile and pass `references/delegated/26_minimax_parameter_audit.md` plus `34_prompt_budget_and_compression.md` before rendering.

Provider profiles prevent false assumptions. The direct MiniMax API, CLI, and third-party wrappers can expose different controls. Do not rely on a global MiniMax profile when exporting payloads.
