# Responsive implementation specification

## GitHub README — real constraints

GitHub renders and sanitizes Markdown and limited HTML. Arbitrary CSS, JavaScript, media queries, responsive card breakpoints, client-side animation and custom fonts cannot be relied upon.

Thus the **actual README** uses one-column project SVG cards, source links and plain-text content, rather than 3-column cards that shrink to illegible text on mobile. Native GitHub sidebar, profile photo, theme and header are not controlled by repository HTML.

| Context | Target | Behavior |
|---|---|---|
| Figma desktop concept | 1440 px wide | 12-col grid, 96 px margin, 24 px gap |
| Figma tablet concept | 768 px wide | 2 columns for interactive portfolio *only* |
| Mobile Figma concept | 390 px wide | 4-col grid, 16 px margins, stacked content |
| Real GitHub README desktop | Host-controlled width | Full-width image assets; prose directly below |
| Real GitHub README mobile | Host-controlled narrow width | Full-width stacked card images and short text links |

## Content order

Hero → About me → Analytics workflow → Technology stack → Featured projects (6) → Technical toolkit → How I approach data work → Experience & education → Currently exploring → GitHub activity → Let's connect.

## Accessibility

- All image tags have descriptive `alt`.
- Key content is repeated as accessible live text, not only embedded in SVG.
- Do not use tables for the whole layout or embed custom CSS.
- Keep the official GitHub account avatar in GitHub's native sidebar; do not duplicate it in README or use an AI-generated substitute.
- Represent missing demos as no link, not as a fake clickable action.
- Charts and heatmaps inside artwork are clearly labeled illustrative.

## Verification

Run `python scripts/validate_profile.py` after checkout. This validates structural Markdown, linked project cards, local assets and SVG safety. It does **not** perform browser pixel-diff checks, external uptime checks or Power BI / SQL / Python / Tableau runtime execution.

## Optional motion

An illustrative, looping GIF appears only in a `<details>` section, collapsed by default. The primary workflow image remains a static SVG and all five steps appear in Markdown. This avoids forcing autoplaying animation into the main reading flow; GitHub README itself cannot apply a custom reduced-motion media query.
