# Contributing

Thank you for helping improve Graphite Mountain.

## Standard

Contributions should make the team more useful, more accurate, safer, easier to operate, or easier to adopt. Character flavour is welcome only after the professional method is strong.

A good change:

- solves a specific delivery problem;
- preserves clear ownership and decision rights;
- improves evidence, requirements, architecture, construction, testing, deployment, or operations;
- keeps instructions portable across agent runtimes where practical;
- avoids speculative process and unnecessary files;
- includes proportionate validation.

## Fan-project boundary

Do not contribute:

- copied dialogue, scripts, catchphrases, episode text, screenshots, show logos, promotional images, music, actor likenesses, or voice imitation;
- text presented as official or endorsed;
- stereotypes, accents, ethnicity-based humour, harassment, humiliation, or abusive role-play;
- instructions that sacrifice safety, legality, privacy, accessibility, or accuracy for character performance.

Use original, restrained comedy based on professional tensions and working styles.

## Team-model changes

Every member may add context, challenge assumptions, propose corrections, and own explicitly assigned work. Changes must not create unbounded overlapping editors or remove the user's final authority.

Jared remains the standing delegated Product Owner, COO, and lifecycle chair unless a future major version deliberately changes the governance model.

## Pull requests

Please include:

```text
Problem: <what is weak or missing>
Change: <what the pull request does>
Lifecycle impact: <requirements, architecture, construction, deployment, or cross-stage>
Evidence: <validation performed>
Risk: <compatibility, safety, legal, or behavioural concern>
```

Run:

```bash
python scripts/validate.py
```

before submitting.

## Versioning

Graphite Mountain uses semantic versioning. During `0.x`, role and workflow contracts may evolve, but changes should still be documented and migration impact made explicit.
