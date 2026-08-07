# Model guidance

Model choice is configuration, not methodology. Select by capability, risk, latency,
cost, tool access, and evidence. Do not present a model name as proof that a result is
good, safe, original, or production-ready.

## Record the choice

For any substantial or repeated run, record:

```text
Model profile: <frontier reasoning | coding agent | fast execution | evaluator | research>
Provider / model ID: <exact value, or runtime default unavailable>
Reasoning effort: <provider-native value, or not applicable>
Tools and data: <shell, web, repository, APIs, sensitive-data boundary>
Budget: <per-run and total token, time, or money limit>
Fallback: <what happens when the model, tool, quota, or evaluator is unavailable>
Evidence date: <when the recommendation was checked>
```

If the runtime does not expose the exact model or effort, say so. Never invent a
specific model string after the fact.

## Capability profiles

| Profile | Best fit | Typical effort | Guardrail |
|---|---|---|---|
| Frontier reasoning | Ambiguous requirements, architecture, security, legal/IP issue-spotting, and independent review | High; use the provider's extra-high setting only for consequential uncertainty | Human approval still owns gates and risk acceptance |
| Coding agent | Bounded implementation, integration, tests, and documentation changes | Medium or high, based on integration risk | Keep one checkpoint and inspect the actual diff |
| Fast execution | Mechanical edits, formatting, summaries, and well-specified transformations | None or low | Do not use it to decide architecture, legality, or release readiness |
| Deterministic evaluator | Numeric quality, performance, regression, accessibility, or policy checks | Not applicable | A model opinion cannot replace the declared metric command |
| Research model or workflow | Current laws, policies, APIs, market facts, and vendor capabilities | High when sources conflict or the question is high-stakes | Cite sources, check dates, and escalate legal decisions to counsel |

## Recommended profile by mode

| Mode | Suggested configuration | Why |
|---|---|---|
| `requirements`, `architecture`, `review` | Frontier reasoning plus repository evidence; high effort by default | These modes resolve ambiguity and expose assumptions before they become code |
| `construct` | Coding agent; medium for routine slices, high for cross-layer or migration work | The work is bounded execution, but integration failures still need judgement |
| `release` | Frontier review plus operator-controlled checks | A model may prepare a release decision; it does not create deployment authority |
| `goal` | Coding agent for one checkpoint, independent review before completion | Durable state needs continuity without turning the issue into an open-ended backlog |
| `autoloop` | Strong planner/reviewer, cheaper executor where safe, deterministic evaluator every run | The metric decides retain/reject; the model proposes one falsifiable experiment |
| `issue-forge` | Fast or medium analysis | It should identify evidence-backed opportunities, not implement them |

## Autoloop model pattern

Use three separable responsibilities:

1. A planner chooses one hypothesis and names the smallest candidate change.
2. An executor changes only the declared files.
3. A deterministic evaluator and independent reviewer decide whether the candidate is retained.

If the evaluator is missing, non-repeatable, or model-only, stop as `blocked`. A loop
may not retain a change because it is interesting, eloquent, larger, or preferred by the
model. Record the baseline, candidate metric, regression result, decision, budget used,
and stop reason.

## Current provider examples

Provider catalogs change. As a current OpenAI example, the official model catalog
describes GPT-5.6 Sol as the frontier option for complex reasoning and coding, GPT-5.6
Terra as the balance of intelligence and cost, and GPT-5.6 Luna as the cost-sensitive,
high-volume option. The catalog lists provider-supported reasoning values, including
`xhigh`, but support and pricing are model-specific. Verify the catalog at use time:

- [OpenAI model catalog](https://developers.openai.com/api/docs/models)
- [OpenAI model selection guidance](https://developers.openai.com/api/docs/guides/model-selection)
- [OpenAI reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)

Do not hard-code a claim such as “built with GPT-6 Luna on Extra High” unless the exact
model ID, setting, date, and run evidence exist. Prefer a truthful recommendation such
as “frontier reasoning profile; provider/model and effort recorded at run time.”

Model selection never grants permission to merge, publish, deploy, spend, contact
customers, accept legal risk, or remove a human gate.
