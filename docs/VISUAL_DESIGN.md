# GitHub profile: simplified visual design

The GitHub profile README keeps the **original factual text, links, and project description table**. Its illustrations are supplemental, not a replacement for accessible text.

## Design decisions

- Header text and illustration occupy separate, fixed regions; no elements are animated or repositioned.
- Six project cards share a common layout and use **short, two-line titles** instead of dense descriptions. The original Markdown project table provides detailed context.
- The skills and experience illustrations were removed from the README because they duplicated nearby text and added visual clutter. The original skills and career information is unchanged.
- Only one workflow graphic and one portfolio call-to-action remain in addition to the project cards and profile header.
- No JavaScript, external image services, fragile visitor counters or unverified KPI values are included.
- Individual card links point to source repositories; header and portfolio CTA link to the official [portfolio](https://bhagabata-brahma-data-analyst.vercel.app/).

## Asset structure

See [assets/README.md](../assets/README.md).

| Asset | Path |
| --- | --- |
| Header | [branding/profile-header.svg](../assets/branding/profile-header.svg) |
| Portfolio CTA | [branding/portfolio-cta.svg](../assets/branding/portfolio-cta.svg) |
| Workflow | [diagrams/data-workflow.svg](../assets/diagrams/data-workflow.svg) |
| Project cards | [projects/](../assets/projects/) |

## Compatibility and maintenance

All illustrations are static SVGs that retain a readable state when GitHub's SVG proxy disables scripts, styling or animation. Text descriptions and repository links remain present in README prose. Do not use complex animation, animated text position or tiny metrics in the artwork.

When updating projects, keep source descriptions accurate, test the card labels at GitHub column width (roughly half the README), and confirm the referenced files and links before committing.

No project repository, executable code, data assets, dashboards, or external deployment was modified by this design change.

## Project details and quality gate

The six visual cards remain immediately visible. The original project scope-and-stack table is inside an expandable **“View full project details”** block so readers can expand it without scrolling through repeated summaries. This preserves all six original project descriptions and links.

The updated [static profile validator](../scripts/validate_profile.py) checks each visual card against its **specific** GitHub repository, primary portfolio/contact links, local image references, supported SVG markup, and the icon geometry relative to its 112 × 112 px panel. It accounts for stroke padding and expects at least 12 px of interior space around the icon. The GitHub Actions workflow executes this validator automatically.

This is a static check, not an assertion that every browser or GitHub mobile layout has been pixel-tested. The README's factual claims should be reviewed when roles, projects or live URLs change.

## Option A visual refinement — October 2026

- The clickable hero has subtle line/dot motion that remains readable as a still image where GitHub strips SVG animation.
- The six project cards retain the same typography, link targets and precisely centered icon geometry. Only a restrained top-right accent and accessible text encoding were polished.
- One compact, static **Current focus** strip makes the three major skill priorities immediately visible without inventing new roles or metrics.
- The portfolio call-to-action has a clearer, consistently stroked action area. The entire image remains linked through the README.
- No layout-moving animations, JavaScript widgets or external graphic dependencies have been added.

These files are source-controlled, text-editable SVGs; the GitHub Actions validation remains the primary static quality gate.
