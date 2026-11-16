# GitHub profile visual assets

All v2 assets are **original, text-editable, lightweight SVG illustrations** for the profile README. **Charts and data tiles are conceptual illustrations**, not actual screenshots, verified business metrics or live contribution results.

## Currently used v2 assets

| Purpose | Path |
|---|---|
| Hero banner | [v2/hero/hero-banner.svg](v2/hero/hero-banner.svg) |
| Analytics workflow | [v2/workflow/analytics-workflow.svg](v2/workflow/analytics-workflow.svg) |
| Technology overview | [v2/technologies/stack.svg](v2/technologies/stack.svg) |
| Project cards | [v2/projects/](v2/projects/) |
| Five-step approach | [v2/workflow/approach.svg](v2/workflow/approach.svg) |
| Illustrative GitHub activity | [v2/banners/activity.svg](v2/banners/activity.svg) |
| Contact banner | [v2/banners/contact.svg](v2/banners/contact.svg) |
| Optional five-step motion | [v2/animations/analytics-flow.gif](v2/animations/analytics-flow.gif) |

Six project cards correspond exactly to these real repository names: `UrbanCartAnalysis`, `Pizza_Sales_Analysis`, `EdTech-Analysis`, `End-To-End-Data-Management`, `Python-Data_Anlysis` and `ERP-Reporting-Data-Analysis-using-Microsoft-Dynamics-365-F-O`.

## Preserved legacy assets

Existing `branding/`, `projects/` and `diagrams/` remain intact for version history and possible rollback. The current README uses the v2 artwork and an optional GIF; the profile photo remains in GitHub's native sidebar rather than being duplicated inside the README.

## Maintenance

Use descriptive `alt` text and keep key facts in Markdown prose. Do not invent certifications, stars, deployment statuses or contribution numbers. GitHub sanitizes HTML, CSS and scripts; use static SVG artwork, not custom UI. Run `python scripts/validate_profile.py` after changes. See [design system](../design/design-system.md).

Do not alter the standalone portfolio website repositories as part of profile art maintenance.

## Motion and contrast

The GIF is 480 × 70 px and is collapsed by default in README, where the static workflow stays visible. No custom JS, external image service or animated SVG is required. All essential copy has a high-contrast dark area behind it so the graphics do not cover labels.
