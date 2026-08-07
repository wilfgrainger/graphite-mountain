#!/usr/bin/env python3
"""Validate the Graphite Mountain repository contract and static visual guide."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
SKILL = ROOT / "skills" / "graphite-mountain"
SITE = ROOT / "docs"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "NOTICE.md",
    ROOT / "CHANGELOG.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "AGENTS.md",
    ROOT / ".github" / "agents" / "agentic-workflows.md",
    ROOT / ".github" / "skills" / "agentic-workflows" / "SKILL.md",
    SKILL / "SKILL.md",
    SKILL / "MODELS.md",
    SKILL / "WORKFLOW.md",
    SKILL / "WORKFLOWS.md",
    SKILL / "team" / "jared.md",
    SKILL / "team" / "richard-hendricks.md",
    SKILL / "team" / "dinesh.md",
    SKILL / "team" / "gilfoyle.md",
    SKILL / "team" / "jian-yang.md",
    SKILL / "team" / "erlich-bachman.md",
    ROOT / ".github" / "aw" / "instructions.md",
    SITE / "index.html",
    SITE / "styles.css",
    SITE / "app.js",
    SITE / "README.md",
    ROOT / ".github" / "workflows" / "README.md",
    ROOT / ".github" / "workflows" / "graphite-goal.md",
    ROOT / ".github" / "workflows" / "graphite-autoloop.md",
    ROOT / ".github" / "workflows" / "graphite-issue-forge.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "graphite-goal.yml",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "graphite-program.yml",
]

TEAM_NAMES = [
    "Jared",
    "Richard Hendricks",
    "Dinesh",
    "Gilfoyle",
    "Jian-Yang",
    "Erlich Bachman",
]

LIFECYCLE_STAGES = [
    "Requirements",
    "Architecture",
    "Construction & Verification",
    "Deployment & Operations",
]

def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def extract_local_assets(html_text: str) -> set[str]:
    """Return relative src/href assets that should exist in docs/."""
    assets: set[str] = set()
    for attribute, value in re.findall(
        r"""\b(src|href)=["']([^"'#?]+)["']""",
        html_text,
        flags=re.IGNORECASE,
    ):
        parsed = urlparse(value)
        if parsed.scheme or parsed.netloc or value.startswith(("/", "mailto:", "tel:")):
            continue
        if attribute.casefold() == "href" and not Path(value).suffix:
            continue
        assets.add(value)
    return assets


def validate_site(errors: list[str]) -> None:
    html_text = (SITE / "index.html").read_text(encoding="utf-8")
    css_text = (SITE / "styles.css").read_text(encoding="utf-8")
    js_text = (SITE / "app.js").read_text(encoding="utf-8")

    required_html = {
        "language declaration": r"<html[^>]+\blang=[\"']en[\"']",
        "UTF-8 metadata": r"<meta[^>]+\bcharset=[\"']utf-8[\"']",
        "responsive viewport": r"<meta[^>]+\bname=[\"']viewport[\"']",
        "page description": r"<meta[^>]+\bname=[\"']description[\"']",
        "main landmark": r"<main\b",
        "primary heading": r"<h1\b",
        "skip link": r"class=[\"'][^\"']*\bskip-link\b",
        "navigation label": r"<nav[^>]+\baria-label=",
        "live copy status": r"\baria-live=[\"']polite[\"']",
        "unofficial-project disclaimer": r"not affiliated",
    }
    for label, pattern in required_html.items():
        if not re.search(pattern, html_text, flags=re.IGNORECASE):
            fail(f"docs/index.html missing {label}", errors)

    for name in TEAM_NAMES:
        if name not in html_text:
            fail(f"docs/index.html does not present team member: {name}", errors)

    site_stage_labels = [
        "Requirements",
        "Architecture",
        "Construct &amp; verify",
        "Deploy &amp; operate",
    ]
    for stage in site_stage_labels:
        if stage not in html_text:
            fail(f"docs/index.html missing lifecycle stage: {stage}", errors)

    for asset in extract_local_assets(html_text):
        asset_path = (SITE / asset).resolve()
        try:
            asset_path.relative_to(SITE.resolve())
        except ValueError:
            fail(f"docs/index.html references asset outside docs/: {asset}", errors)
            continue
        if not asset_path.is_file():
            fail(f"docs/index.html references missing local asset: {asset}", errors)

    if re.search(
        r"""<(?:script|link)\b[^>]+(?:src|href)=["']https?://""",
        html_text,
        flags=re.IGNORECASE,
    ):
        fail("docs/index.html must not load external script or stylesheet dependencies", errors)

    if "prefers-reduced-motion" not in css_text:
        fail("docs/styles.css must support prefers-reduced-motion", errors)
    if ":focus-visible" not in css_text:
        fail("docs/styles.css must define visible keyboard focus", errors)
    if "@media" not in css_text:
        fail("docs/styles.css must include responsive media queries", errors)
    if "navigator.clipboard" not in js_text:
        fail("docs/app.js must provide the install-command copy enhancement", errors)

    combined_site = "\n".join([html_text, css_text, js_text])
    for placeholder in ["TODO", "FIXME", "lorem ipsum"]:
        if placeholder.casefold() in combined_site.casefold():
            fail(f"Static site contains unfinished placeholder: {placeholder}", errors)


def validate_agentic_workflows(errors: list[str]) -> None:
    workflow_dir = ROOT / ".github" / "workflows"
    required_terms = {
        "graphite-goal.md": ["graphite-goal", "Completion Contract", "safe-outputs", "min-integrity", "GRAPHITE:GOAL-STATUS"],
        "graphite-autoloop.md": ["graphite-program", "numeric evaluator", "baseline", "model profile", "budget", "retain:", "reject:", "blocked:"],
        "graphite-issue-forge.md": ["graphite-generated", "deduplicated", "Do not add `graphite-goal`"],
    }
    for filename, terms in required_terms.items():
        path = workflow_dir / filename
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            fail(f"{path.relative_to(ROOT)} must have YAML frontmatter", errors)
        for term in terms:
            if term.casefold() not in text.casefold():
                fail(f"{path.relative_to(ROOT)} missing workflow contract: {term}", errors)

    for filename in ["graphite-goal.yml", "graphite-program.yml"]:
        text = (ROOT / ".github" / "ISSUE_TEMPLATE" / filename).read_text(encoding="utf-8")
        for term in ["Completion Contract", "Evidence / Verification", "Scope and Constraints", "Blocked Stop Condition"]:
            if term.casefold() not in text.casefold():
                fail(f".github/ISSUE_TEMPLATE/{filename} missing field: {term}", errors)

    program_text = (ROOT / ".github" / "ISSUE_TEMPLATE" / "graphite-program.yml").read_text(encoding="utf-8")
    for term in ["Baseline", "Model profile and run budget"]:
        if term.casefold() not in program_text.casefold():
            fail(f".github/ISSUE_TEMPLATE/graphite-program.yml missing field: {term}", errors)

    overlay_text = (ROOT / ".github" / "aw" / "instructions.md").read_text(encoding="utf-8")
    for term in ["AGENTS.md", "untrusted input", "one bounded checkpoint", "graphite-generated", "gh aw compile", "human authority"]:
        if term.casefold() not in overlay_text.casefold():
            fail(f".github/aw/instructions.md missing repository overlay rule: {term}", errors)

    adapter_checks = {
        ROOT / ".github" / "agents" / "agentic-workflows.md": ["Graphite-authored adapter", "AGENTS.md", "gh-aw", "untrusted input"],
        ROOT / ".github" / "skills" / "agentic-workflows" / "SKILL.md": ["repository-owned router", "AGENTS.md", "gh-aw", "human"],
    }
    for path, terms in adapter_checks.items():
        adapter_text = path.read_text(encoding="utf-8")
        for term in terms:
            if term.casefold() not in adapter_text.casefold():
                fail(f"{path.relative_to(ROOT)} missing adapter contract: {term}", errors)


def validate_documentation_references(errors: list[str]) -> None:
    """Catch documentation commands that refer to scripts absent from the repository."""
    documentation = [
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "docs" / "README.md",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "graphite-goal.yml",
        ROOT / ".github" / "ISSUE_TEMPLATE" / "graphite-program.yml",
    ]
    pattern = re.compile(r"(?<![\w/])scripts/([A-Za-z0-9_.-]+\.py)\b")
    for path in documentation:
        text = path.read_text(encoding="utf-8")
        for script_name in sorted(set(pattern.findall(text))):
            script_path = ROOT / "scripts" / script_name
            if not script_path.is_file():
                fail(f"{path.relative_to(ROOT)} references missing script: scripts/{script_name}", errors)


def main() -> int:
    errors: list[str] = []

    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", VERSION):
        fail(f"VERSION must be a semantic version, found {VERSION!r}", errors)

    for path in REQUIRED:
        if not path.is_file():
            fail(f"Missing required file: {path.relative_to(ROOT)}", errors)
        elif not path.read_text(encoding="utf-8").strip():
            fail(f"Required file is empty: {path.relative_to(ROOT)}", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    workflow_text = (SKILL / "WORKFLOW.md").read_text(encoding="utf-8")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")

    version_match = re.search(r"^version:\s*(\S+)\s*$", skill_text, re.MULTILINE)
    if not version_match:
        fail("SKILL.md frontmatter has no version", errors)
    elif version_match.group(1) != VERSION:
        fail(
            f"SKILL.md version {version_match.group(1)!r} does not match VERSION {VERSION!r}",
            errors,
        )

    for name in TEAM_NAMES:
        if name not in skill_text:
            fail(f"SKILL.md does not load team member: {name}", errors)
        if name not in readme_text:
            fail(f"README.md does not describe team member: {name}", errors)

    for index, stage in enumerate(LIFECYCLE_STAGES, start=1):
        heading = f"Stage {index} — {stage}"
        if heading not in workflow_text:
            fail(f"WORKFLOW.md missing lifecycle heading: {heading}", errors)

    if "not affiliated with" not in readme_text.casefold():
        fail("README.md must contain the unofficial-project disclaimer", errors)

    if "equal rights" not in skill_text.casefold():
        fail("SKILL.md must preserve equal team contribution rights", errors)

    models_text = (SKILL / "MODELS.md").read_text(encoding="utf-8")
    for term in ["Capability profiles", "Autoloop model pattern", "deterministic evaluator", "human approval"]:
        if term.casefold() not in models_text.casefold():
            fail(f"MODELS.md missing model contract: {term}", errors)

    validate_site(errors)
    validate_agentic_workflows(errors)
    validate_documentation_references(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Graphite Mountain v{VERSION}: validation passed "
        f"({len(REQUIRED)} required files, skill contract and visual guide)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
