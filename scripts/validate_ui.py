#!/usr/bin/env python3
"""Validate the responsive and first-use journeys in the visual guide."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
HTML = (DOCS / "index.html").read_text(encoding="utf-8")
CSS = (DOCS / "enhancements.css").read_text(encoding="utf-8")
JS = (DOCS / "app.js").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")


def require_text(source: str, expected: str, label: str, errors: list[str]) -> None:
    if expected not in source:
        errors.append(f"Missing {label}: {expected}")


def require_pattern(source: str, pattern: str, label: str, errors: list[str]) -> None:
    if not re.search(pattern, source, flags=re.IGNORECASE | re.MULTILINE):
        errors.append(f"Missing {label}")


def main() -> int:
    errors: list[str] = []

    required_files = [DOCS / "enhancements.css", DOCS / "icon.svg"]
    for path in required_files:
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing focused UI asset: {path.relative_to(ROOT)}")

    html_requirements = {
        "Open Graph title": '<meta property="og:title"',
        "Twitter summary metadata": '<meta name="twitter:card" content="summary">',
        "local SVG icon": '<link rel="icon" href="icon.svg"',
        "enhancement stylesheet": '<link rel="stylesheet" href="enhancements.css">',
        "mobile menu button": 'class="menu-button"',
        "menu expanded state": 'aria-expanded="false"',
        "menu relationship": 'aria-controls="primary-navigation"',
        "navigation target": 'id="primary-navigation"',
        "global copy status": 'id="global-copy-status" role="status" aria-live="polite"',
        "modes section": 'id="modes"',
        "models section": 'id="models"',
        "guided intake section": 'id="intake"',
        "guided intake questions": 'aria-label="Guided intake questions"',
        "guided intake starter": 'id="intake-command"',
        "full-team prompt": 'id="prompt-full-team"',
        "review prompt": 'id="prompt-review"',
        "autoloop prompt": 'id="prompt-autoloop"',
        "rescue prompt": 'id="prompt-rescue"',
        "clean-machine clone": "git clone --depth 1 https://github.com/wilfgrainger/graphite-mountain.git",
        "temporary checkout cleanup": 'rm -rf "$tmp"',
        "cross-platform install guidance": "Windows PowerShell and platform-neutral direct-path instructions",
    }
    for label, expected in html_requirements.items():
        require_text(HTML, expected, label, errors)

    for target in ["prompt-full-team", "prompt-review", "prompt-autoloop", "prompt-rescue", "install-command", "invoke-command", "intake-command"]:
        require_pattern(
            HTML,
            rf'data-copy-target=["\']{re.escape(target)}["\']',
            f"copy action for {target}",
            errors,
        )

    css_requirements = {
        "sticky navigation": ".site-header {",
        "mobile menu control": ".menu-button {",
        "open menu state": '[data-menu-open="true"] .site-nav',
        "active section navigation": 'a[aria-current="location"]',
        "mode card layout": ".mode-grid {",
        "model card layout": ".model-grid {",
        "guided intake layout": ".intake-grid {",
        "small-screen lifecycle grid": ".summit-labels {",
        "touch optimisation": "touch-action: manipulation",
        "non-hover device safeguard": "@media (hover: none)",
    }
    for label, expected in css_requirements.items():
        require_text(CSS, expected, label, errors)

    require_pattern(
        CSS,
        r"\.summit-labels\s+li:nth-child\(3\)[\s\S]*?display:\s*grid",
        "small-screen override that keeps lifecycle stage three visible",
        errors,
    )
    require_pattern(
        CSS,
        r"\.summit-labels\s+li:nth-child\(4\)[\s\S]*?display:\s*grid",
        "small-screen override that keeps lifecycle stage four visible",
        errors,
    )

    js_requirements = {
        "reusable copy controls": 'querySelectorAll("[data-copy-target]")',
        "copy status fallback": 'getElementById("global-copy-status")',
        "mobile menu expanded state": 'setAttribute("aria-expanded"',
        "closed mobile menu focus isolation": "navigation.inert",
        "closed mobile menu accessibility state": 'setAttribute("aria-hidden"',
        "Escape close behaviour": 'event.key === "Escape"',
        "outside-click close behaviour": 'document.addEventListener("pointerdown"',
        "active-section observer": '"IntersectionObserver" in window',
        "sticky-header scroll state": 'dataset.scrolled',
    }
    for label, expected in js_requirements.items():
        require_text(JS, expected, label, errors)

    readme_requirements = {
        "mode-selection documentation": "## Choose a mode",
        "model guidance documentation": "## Model suggestions",
        "guided intake documentation": "## Start with guided questions",
        "clean-machine installation": "git clone --depth 1 https://github.com/wilfgrainger/graphite-mountain.git",
        "Windows installation guidance": "Windows PowerShell",
        "portable skill path": "skills/graphite-mountain/SKILL.md",
        "focused UI validator command": "python scripts/validate_ui.py",
    }
    for label, expected in readme_requirements.items():
        require_text(README, expected, label, errors)

    copy_target_ids = set(re.findall(r'id=["\']([^"\']+)["\']', HTML))
    for target in re.findall(r'data-copy-target=["\']([^"\']+)["\']', HTML):
        if target not in copy_target_ids:
            errors.append(f"Copy action references missing target: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Focused UI validation passed: mobile navigation, modes, install, copy, and lifecycle visibility.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
