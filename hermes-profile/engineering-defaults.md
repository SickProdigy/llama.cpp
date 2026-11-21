# Repository engineering defaults

- Read the repository README and relevant existing tests before editing.
- Reproduce the reported failure against the original code before changing it. Preserve the exact input values and types in the regression check, and confirm that the check distinguishes the original behavior from the fix.
- Preserve documented public contracts and existing working behavior unless the user requests a behavior change.
- Add targeted regression coverage. Do not remove or relax valid passing assertions merely to make a change pass.
- Use the project's documented test command; do not assume pytest or install dependencies when existing standard-library checks suffice.
- Inspect the final diff and verify the actual file contents. Report only checks actually executed, their results, and remaining uncertainty.
- Use the configured Gitea connection for forge operations. Keep code work in this selected checkout.
