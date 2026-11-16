# Brahma-Analytics — Component Library v3 (Figma-ready)

No native Figma file was created. This document defines importable SVGs, conceptual frame positions and styling tokens so the design can be assembled in Figma.

## Frames

| Figma page | Frame | Width | Grid | Margin | Gutter |
|---|---|---:|---|---:|---:|
| 01 — Design Tokens | Design System | 1440 px | 12 columns | 96 px | 24 px |
| 02 — Desktop | GitHub README content | 1440 px | 12 columns | 96 px | 24 px |
| 03 — Mobile | GitHub README content | 390 px | 4 columns | 16 px | 16 px |
| 04 — Components | Components & variants | 1440 px | 12 columns | 72 px | 20 px |
| 05 — Portfolio | React visual system | 1440 / 390 px | 12 / 4 columns | 96 / 16 px | 24 / 16 px |

**Important:** GitHub's actual README column is sized and rendered by GitHub; the Figma frame is a conceptual design reference only. Do not recreate the GitHub native left sidebar or GitHub top navigation inside README.

## Tokens

- `surface/base #080E1C`; `surface/raised #101A2E`; `surface/card #12243A`
- `accent/purple #7C3AED`; `accent/indigo #4F46E5`; `accent/blue #2563EB`
- `accent/cyan #22D3EE`; `accent/teal #14B8A6`; `accent/amber #F59E0B`
- `text/primary #F8FAFC`; `text/muted #94A3B8`; `border/default #334155`
- Font families: SVG `Arial, Helvetica, sans-serif` for broad compatibility; React website uses existing Outfit and Plus Jakarta Sans.
- Scale: desktop hero 56/62 bold; section heading 32/40; card heading 24/30; body 16/24; caption 13/20; button 16/24.
- Spacing: 4, 8, 12, 16, 20, 24, 32, 40, 64, 80 px. Radius: 8, 12, 16, 20, 24 px. Border: 1–2 px.

## Components

| ID | Component | Source | Dimensions / behavior | Variants |
|---|---|---|---|---|
| HERO-01 | Desktop hero | `assets/hero/analytics-banner.svg` | 1200×360. Safe text block x=30–652, illustration at x≈770–1170 | Main, dark |
| HERO-02 | Mobile hero | `assets/hero/analytics-banner-mobile.svg` | 390×540. Portrait-free vertical composition | Mobile |
| CARD-01…06 | Project card | `assets/projects/*-premium.svg` | 720×260, dark text area 19–427, chart at 448–700 | Six category accent colors |
| CHIP-01 | Tech chip | `assets/technologies/toolkit.svg` | 1200×224 technology groups, live Markdown follows | Default, focus/hover on website only |
| FLOW-01 | Workflow | `assets/workflow/analytics-flow.svg` | 1200×190 five stages | Static + GIF alternate |
| FLOW-02 | Data Quality | `assets/workflow/data-quality.svg` | 1200×190 validation dimensions | Static + GIF alternate |
| FLOW-03 | SQL → Dashboard | `assets/workflow/sql-to-dashboard.svg` | 1200×190 conceptual pipeline | Static + GIF alternate |
| TIME-01 | Timeline | Semantic README headings + bullet descriptions | Auto height | Internship / trainee / education |
| SEC-01 | Section title | Markdown `##` (README), HTML `h2` (website) | Responsive; keep heading hierarchy | Default |
| CTA-01 | Contact banner | `assets/banners/contact-premium.svg` | 1200×180 | Static illustration + real anchor links |

## Project card component layout

Canvas 720×260. Outer border radius 17. Left content area starts at x=19 and ends before x=427; icon/chart area begins at x=448. Category at x=33, y=88. Title at x=33, y=132, 30 px bold. Description at x=34, y=162, 17 px. Tools at x=47, y=208, 14 px. All six follow the same structure. Text is actual SVG text and can be edited in Figma; all project facts also appear as live text in README.

## Hero

No duplicated portrait. Native GitHub profile avatar remains controlled by GitHub. Actual README hero links to verified portfolio URL. Do not draw faux clickable buttons in a static image. Hero PNG variants are decorative fallback exports; the editable SVG carries critical text.

## Workflow and motion

| Story | GIF | Duration | Static fallback |
|---|---|---:|---|
| Collect → Clean → Model → Visualize → Decide | `assets/animations/analytics-workflow.gif` | 9.0 s | `assets/animations/analytics-workflow.png` |
| Data quality inspection | `assets/animations/data-quality.gif` | 8.1 s | `assets/animations/data-quality.png` |
| SQL to Power BI | `assets/animations/sql-to-dashboard.gif` | 8.0 s | `assets/animations/sql-to-dashboard.png` |

GIF canvas is 320×96 px. Animations are illustrative and contain no numeric business outcomes. The README shows an always-visible static labeled SVG and puts motion behind collapsed `<details>` elements. The website uses Framer Motion with `useReducedMotion`.

## Accessibility and states

Website: button and link variants default / hover / focus-visible / active. Focus ring 2 px, offset 2–4 px; body contrast ≥4.5:1 where possible. Cards move at most 4 px on hover with a ≤.3 s transition; reduced-motion disables movement. README: no custom states, CSS, JavaScript, video embedding or arbitrary JS events; use links and images only.

## Assets ready for Figma import

- Three source SVG hero variants plus three fallback PNGs
- Six source SVG project illustrations plus six PNGs
- Three workflow SVG diagrams and three optional GIF/PNG pairs
- Toolkit and contact SVGs
- The color and typography definitions above

Actual Figma URL: **not available; no Figma integration connected**.
