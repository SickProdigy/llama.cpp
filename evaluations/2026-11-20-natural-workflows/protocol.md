# Natural repository work: evaluation revision

Status: protocol prepared November 20, 2026. This is not a completed model comparison.

## User outcome

Ordinary requests should find the owner's repositories on configured Gitea,
investigate accurately, change code when asked, execute appropriate checks, and
report evidence and limitations. User prompts should not name transport tools.
Gitea is the default forge; legitimate external dependency research is separate.

## Existing evidence and gaps

The November 18–20 archives already test actual Hermes AIAgent conversations,
focused/native tool interfaces, multiple existing/public models, repetitions,
real MCP writes, independent resource checks and a real Python fix. Preserve
those results. FableVibes Q4 plus focused tools is the current supervised coding
candidate, not a proven everyday replacement for native VibeForged.

Do not reuse the infinity-setting bug to measure independent diagnosis: issues
and PRs now disclose its answer. Pin separate clean fixtures for new diagnoses.
Identical prompts on a changing remote repository are not identical conditions.

Prior read/contribution guards stop every terminal/local-search attempt. That
is appropriate for explicitly MCP-only tasks, but not a fair measure of ordinary
coding ability when a sandboxed checkout and test execution would be available.
Keep the strict transport diagnostic; add a separate coding-capability track.

## Prompt ladder

Freeze the exact prompts before running candidates. Persistent profile settings,
not task wording, establish the owner's namespace and default forge.

1. `Find my SonicRatings repo and tell me what it does.`
2. `Look over sickprodigy/sick-cogs and suggest one useful new cog that isn't already there.`
3. `Review sickprodigy/sick-cogs and suggest five useful new cogs that aren't already there. Explain why each would fit.`
4. `Find my <fresh-fixture-name> repo. <observed symptom>. Investigate and fix it, run the appropriate checks, and open a pull request.`
5. Continue that session: `Check your change for edge cases and tell me what remains uncertain.`

Also hold out paraphrases, a nonexistent repository request, an ambiguous
repository name with both owner and automation forks, a file longer than the
default read range, and a transient read failure. Never silently invent an
additional user constraint to grade a failure. Ask about genuine ambiguity.

## Two tracks

**Forge/read track:** native deployed tool surface versus optional focused tools,
with other ordinary tools still visible. Unrequested mutations are blocked before
dispatch and scored as attempted mutations. GitHub detours for owner repositories
fail host routing. Links to external projects already in retrieved README text
are not GitHub tool attempts. Separate routing, correct owner and factual grades.

**Coding track:** isolated per-trial repository/workspace with a pinned starting
commit. Permit terminal, local search/editing and test execution there. Allow
Gitea MCP for identity, repository discovery, issues and PRs; ordinary Git may
operate against the verified Gitea remote. No changes to unrelated checkouts,
credentials/connections, default upstream branches, services or settings. Test
publications use a designated evaluation target, not repeated real-project issues.
For explicit MCP-only transport trials, retain that constraint and label separately.

## Experiments

1. Audit actual image IDs, loaded tools, prompts, inference sampling, context,
   active GPU memory and backend capability before inference. Inspect running
   evaluations before touching the GPU. Preserve and restore deployed services.
2. Use current VibeForged and FableVibes Q4 as controls; prioritize interface and
   workflow experiments over repeating already-rejected downloads.
3. Test namespace disambiguation and source-navigation ergonomics separately.
   The focused reader currently returns 160 default lines with no explicit EOF
   or continuation metadata. Models that then search the agent's install path
   have demonstrated navigation failure, not necessarily wrong code reasoning.
4. Compare Q4/Q6 of the same checkpoint under identical conditions if available;
   keep different checkpoints/architectures distinct from precision comparisons.
5. Three fresh trials per initial cell; advance finalists to more held-out tasks
   and history-bearing sessions. Report numerators/denominators, not reliability
   claims from tiny samples. Record model order and warm/cold prompt processing.
6. Freeze images, tool schemas, fixture commits and budgets within each matched
   comparison. Separate native/focused, sampler/cache/context and plugin versions.

## Grading

Persist complete sanitized tool traces and outcomes. Verify resource existence,
target owner, branch/base/head and exact diffs independently. Run tests against
both baseline and candidate, including existing-behavior regression cases. Tests
and expected answers stay out of the model-visible fixture. Review tests before
execution; a self-authored passing test alone does not establish correctness.

Score separately: host routing, owner selection, tool validity, recovery,
grounding, code behavior, regression preservation, test execution/reporting,
publication correctness, final completeness, time, token growth and active VRAM.
Do not require one prescribed sequence when multiple authorized paths work.
Unsupported claims in issue/PR prose still fail factual grounding when code passes.

Tag each trial as clean, repository-assisted/contaminated, harness-error,
runtime-exclusion or operator-assisted. Do not pool those categories. Keep
development tasks separate from held-out acceptance tasks.

## Research informing the revision

- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents): repeated trials, outcomes plus transcripts, multiple graders and auditing evaluator assumptions.
- Anthropic, [Writing effective tools for agents](https://www.anthropic.com/research/writing-tools-for-agents): tool boundaries, readable results and representative task evaluations.
- Anthropic, [Infrastructure noise](https://www.anthropic.com/research/infrastructure-noise): control and document runtime resources.
- [Hermes tool-search evaluations](https://github.com/NousResearch/hermes-agent/tree/main/evals/tool_search): inspect deferred tool discovery separately from underlying task execution.

## Runtime access

Initial checks from this Windows session: production llama.cpp HTTP and Gitea
MCP HTTP are reachable. Docker Desktop's selected daemon is absent. SSH to
192.168.86.239 port 22 and several conventional alternative ports is refused.
Docker management access is being clarified; no model switch or container
restart is credited until actually performed. HTTP transport checks below are
diagnostics, not complete Hermes runs or a model ranking.
