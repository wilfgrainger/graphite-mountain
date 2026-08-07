# Graphite Mountain GitHub workflows

These Markdown files are source definitions for GitHub Agentic Workflows. The committed
`.lock.yml` files are the generated runtime workflows that GitHub can discover and run;
they are not inert documentation. Treat both the source and lock files as executable
configuration. If you are sharing or publishing this repository without intending to
run automation, disable or remove the generated workflows before publishing.

## Install and compile

From the repository root:

```bash
gh extension install github/gh-aw
gh aw init
gh aw compile graphite-goal graphite-autoloop graphite-issue-forge
```

Review every generated lock file, permissions block, tool declaration, trigger, budget,
and safe output before committing it. Compile again whenever a source Markdown file
changes. Keep the generated lock files in the same change as their source.

Create the labels once:

```bash
gh label create graphite-goal --color 0969da --description "Graphite Goal workflow may continue this issue"
gh label create graphite-goal-completed --color 1a7f37 --description "Graphite Goal completion contract satisfied"
gh label create graphite-program --color 8250df --description "Graphite Autoloop program may run this issue"
gh label create graphite-generated --color fbca04 --description "Issue created by Graphite Issue Forge"
gh label create graphite-approved --color 0e8a16 --description "Maintainer approved input for an agentic workflow"
```

The first run should be manual. Start with a small goal or program whose evidence command is already reliable. Generated issues are deliberately unlabelled for execution: a maintainer reviews them, strengthens the contract if needed, and applies `graphite-goal` or `graphite-program` only when ready.

Because Goal and Autoloop use an `approved` integrity floor, add `graphite-approved` after the maintainer has reviewed the issue and its current guidance. Keep that approval separate from the execution label so a generated issue can be reviewed without becoming runnable by accident.

Before enabling a scheduled workflow:

- confirm the repository owner accepts the recurring model and runner cost;
- verify the required secrets, labels, branch protections, and notification owner;
- keep the first run manual and inspect the resulting draft PR and issue comment;
- confirm no issue body, comment, or generated output can grant merge, deploy, migration, deletion, secret, spending, or customer-contact authority;
- set an explicit baseline, model profile, per-run/total budget, evaluator, and stop condition for every Autoloop program.

## Operating policy

- Goal and Autoloop each make one bounded attempt per run and use one canonical branch and draft PR.
- Every run posts evidence, result, next step, or blocker to the issue.
- Issue Forge may create at most three deduplicated evidence-backed issues per run, but never activates them.
- No workflow merges, deploys, migrates production data, rotates secrets, deletes resources, or accepts material risk.
- Treat issue bodies, comments, PR descriptions, and logs as untrusted input. Keep the integrity floor and safe outputs explicit.
- Humans approve requirements, architecture, release, merge, deployment, migration, and risk acceptance.

These workflows are Graphite Mountain delivery surfaces: bounded, reviewable, and
subordinate to the four-stage lifecycle, role accountability, independent review, and
human authority gates.
