# Security Policy

Graphite Mountain is primarily an instruction and workflow project, but unsafe guidance, prompt-injection weaknesses, secret exposure, destructive defaults, or misleading deployment claims can still create real risk.

## Reporting

Please use GitHub's private vulnerability-reporting or security-advisory feature when available. Do not publish exploit details, secrets, personal data, customer information, or active credentials in a public issue.

Include:

- affected file and version;
- risk and plausible impact;
- safe reproduction details;
- suggested mitigation, when known.

## Scope

Relevant reports include:

- instructions that enable unauthorised destructive actions;
- missing authority checks for push, merge, deploy, migration, deletion, DNS, secrets, spending, or public communication;
- prompt-injection paths that override repository or user constraints;
- guidance that could disclose secrets or confidential data;
- false assurance about tests, deployments, recovery, or production state;
- unsafe security, privacy, or legal defaults.

## Disclosure

Maintainers should acknowledge credible reports, assess impact, prepare a correction, validate it, and coordinate disclosure proportionate to the risk. No response-time guarantee is made for this volunteer project.
