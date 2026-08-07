# Visual guide

This directory contains the dependency-free Graphite Mountain visual guide.

## Local preview

From the repository root:

```bash
python -m http.server 8000 --directory docs
```

Open `http://localhost:8000`.

Run both repository checks before proposing a change:

```bash
python scripts/validate.py
python scripts/validate_ui.py
```

## GitHub Pages

The site is designed to publish directly from the `docs/` directory on the `main` branch. In the repository settings, choose:

```text
Settings → Pages → Deploy from a branch → main → /docs
```

No build step, package manager, external font, analytics, cookie, account, or third-party runtime asset is required.

## File responsibilities

- `index.html` owns semantic content, metadata, navigation, lifecycle, modes, model guidance, team, install, and legal text.
- `styles.css` owns the original Graphite Mountain design system.
- `enhancements.css` owns the focused responsive and first-use uplift and can be removed as one rollback unit.
- `app.js` owns progressive copy actions, mobile navigation, sticky-header state, and section-aware navigation.
- `icon.svg` is the local dependency-free site icon.

## Quality constraints

- semantic HTML and a visible keyboard skip link;
- responsive layout down to 320px;
- every lifecycle stage remains visible at every supported width;
- an accessible mobile menu with a no-surprise keyboard close path;
- a guided intake that limits questions, reflects evidence, and pauses at lifecycle gates;
- keyboard-visible focus states;
- reduced-motion support;
- progressive enhancement for copy actions;
- a clean-machine install command rather than a command that assumes a prior clone;
- no external JavaScript, CSS, font, analytics, or tracking dependency;
- legal disclaimer retained in the footer and the sharing checklist.
