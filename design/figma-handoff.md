# Figma-ready handoff — Brahma-Analytics GitHub profile

This is an **editable design specification and SVG source package**, **not** a native Figma file. No Figma canvas was created through a connected Figma API.

## Pages / frames

1. **01 Design System** — color tokens, type scale, spacing, radii, icon usage; 1440 × 1100.
2. **02 Desktop README** — frame **1440 px wide**, 12-column layout; 96 px margins, 24 px gutters. GitHub's actual README content column will be narrower than the conceptual Figma frame.
3. **03 Mobile README** — frame **390 px wide**, 4-column layout; 16 px margins, 16 px gutters, all project cards stacked.
4. **04 Component Library** — hero, project card, technology group, workflow, five-step approach, timeline text treatment, activity note, contact banner.
5. **05 Site Plan** — separate interactive portfolio concepts only; no production code or deployment.

## Components

**Hero:** title, role, descriptive phrase and illustrative laptop chart (left copy/right chart). GitHub's own profile avatar remains in the native profile sidebar; the README hero intentionally does not duplicate a portrait. Do not synthesize the owner's face.

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

## Refinement and optional motion

The implementation now has dedicated opaque copy panels and conservative text-fit margins. The hero removes visual faux buttons because README graphics are not interactive controls. The GitHub profile's native photo remains unchanged. A subtle GIF version of five-step flow is available under an optional collapsed section (static SVG always visible), without JS or custom README CSS.

## v3 frame and component handoff

Full reusable component coordinates, variants and colors are in [component-library.md](component-library.md). Import the new SVGs from `assets/hero/`, `assets/projects/`, `assets/workflow/` and `assets/banners/` into frames **1440 desktop** and **390 mobile**. The native GitHub avatar/sidebar are intentionally excluded. The supplied rendered mockup informs the visual direction; it is not a Figma file or evidence of real business statistics. Current deliverable: Figma-ready source and specifications only.
