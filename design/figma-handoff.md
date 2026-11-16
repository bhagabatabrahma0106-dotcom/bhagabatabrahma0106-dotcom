# Figma-ready handoff — Brahma-Analytics GitHub profile

This is an **editable design specification and SVG source package**, **not** a native Figma file. No Figma canvas was created through a connected Figma API.

## Pages / frames

1. **01 Design System** — color tokens, type scale, spacing, radii, icon usage; 1440 × 1100.
2. **02 Desktop README** — frame **1440 px wide**, 12-column layout; 96 px margins, 24 px gutters. GitHub's actual README content column will be narrower than the conceptual Figma frame.
3. **03 Mobile README** — frame **390 px wide**, 4-column layout; 16 px margins, 16 px gutters, all project cards stacked.
4. **04 Component Library** — hero, project card, technology group, workflow, five-step approach, timeline text treatment, activity note, contact banner.
5. **05 Site Plan** — separate interactive portfolio concepts only; no production code or deployment.

## Components

**Hero:** title, role, descriptive phrase and illustrative laptop chart (left copy/right chart). Real avatar is a separate user-owned GitHub profile photo linked by GitHub avatar URL in README. Do not replace or synthesize a person's face.

**Project card:** title, category, one-line business scope, tool line, decorative chart; real source/docs links are outside image in accessible Markdown. **Do not** add a demo link unless a real public demo is independently verified.

**Technology group:** 8 labeled cards. **Workflow:** 5 equal steps with number/color/label. **Approach:** five process steps. **Timeline:** semantically ordered text, not an image with tiny labels. **Contact banner:** artwork plus proper LinkedIn / portfolio / email links.

## Source handoff

SVG paths are in `assets/v2/`. They can be imported into Figma as vector images for further editing. GitHub HTML sanitization means README layout should stay Markdown-forward, full-width illustrations and semantic headings rather than trying to reproduce the entire mockup as HTML/CSS.

## QA and boundaries

- Check each of the six project sources and docs against the current repository README.
- Image caption/alt text must say illustrations are decorative or conceptual.
- Education in profile matches the repository's currently published detail: Satyasai Engineering College, BPUT, 2022–2026, CGPA 8.04. This is not independent verification of an academic transcript.
- No new awards, certifications, engagement totals, stars, deployments or work tenure.
- All three portfolio-site repositories remain out of scope.
