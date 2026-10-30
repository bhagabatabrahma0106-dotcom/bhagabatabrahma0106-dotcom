# Profile visual assets

These illustrations support the public GitHub profile README. **They are not screenshots of actual project dashboards** and do not claim measured results.

## Organized folders

- [branding/](branding/) — profile banner and clickable portfolio call-to-action.
- [projects/](projects/) — six separately linked cards for the six existing featured repositories.
- [diagrams/](diagrams/) — a simplified five-step data-workflow illustration.

Each SVG uses a fixed viewBox, a single consistent visual system, generous text margins, and a static layout suitable for GitHub's SVG image renderer. Full project information remains in the [README](../README.md), including the original project comparison table.

If changing any title, measure its available width before publishing. Prefer short titles and two distinct lines, keeping all text away from the right-side icon. Do not add fictional project results, certifications, ratings or other unverified claims.

For richer animation and interactive controls, link readers to the separately hosted [portfolio website](https://bhagabata-brahma-data-analyst.vercel.app/) rather than embedding JavaScript in GitHub README.

## Icon alignment rule

The six project icons use the same right-hand 112 × 112 SVG panel, with their content centered and an interior margin of at least 12 px after accounting for stroke width. The [automated profile validator](../scripts/validate_profile.py) parses the icon geometry and checks this inset. Keep icon shapes within these bounds when making later edits.
