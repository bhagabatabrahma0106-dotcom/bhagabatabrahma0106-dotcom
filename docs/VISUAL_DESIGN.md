# GitHub profile — premium dark analytics redesign (v2)

## Scope

The live profile README was redesigned to follow the owner's supplied premium dark Analytics / Business Intelligence visual reference. The public GitHub README content—not GitHub's native left sidebar, top header, account bio or avatar image—has been changed.

The owner's actual GitHub avatar is referenced via GitHub's avatar service; no AI-generated substitute portrait was published. The three standalone portfolio website repositories were not modified.

## Sections implemented

1. Hero and authentic avatar
2. About me
3. Analytics workflow
4. Technology stack
5. Six featured projects with verified code and documentation links
6. Technical toolkit
7. Five-step data-work approach
8. Experience and education
9. Currently exploring
10. GitHub activity (illustrative, linked to actual profile activity)
11. Let's connect

Each chart-like artwork is explicitly **illustrative**. The README does not invent contribution totals, follower counts, stars, certifications or public dashboard deployments.

## Source asset organization

- `assets/v2/hero/hero-banner.svg`
- `assets/v2/workflow/analytics-workflow.svg`
- `assets/v2/technologies/stack.svg`
- `assets/v2/projects/urbancart.svg`, `pizza.svg`, `edtech.svg`, `superstore.svg`, `banking.svg`, `dynamics.svg`
- `assets/v2/workflow/approach.svg`
- `assets/v2/banners/activity.svg`, `contact.svg`

Legacy assets under `assets/branding/`, `assets/diagrams/` and `assets/projects/` remain present and unmodified for traceability/rollback.

## README rendering approach

- GitHub-compatible Markdown and supported `<a>` / `<img>` / `<details>` / basic HTML only.
- **No custom CSS, JavaScript or custom animation** in the README.
- Full-width stacked illustrated project cards maintain better mobile readability than the three-column Figma concept.
- All significant identity, project and career details appear in readable Markdown, not image text alone.
- Project cards link to actual repository paths; separate Docs links point to files named in each project README.
- No synthetic chart is passed off as a screenshot of a running Power BI dashboard.

## Accuracy and QA

- Role, education and experience copy retained from the existing profile README and the owner's latest instructions.
- Education shown as Satyasai Engineering College, BPUT, 2022–2026, CGPA 8.04 per owner's supplied design brief. No transcript was checked.
- SuperStore is described as having a screenshot/video, **not** a committed editable PBIX.
- EdTech market-analysis source is historical sample data; UrbanCart uses synthetic retail data.
- Dynamics F&O exports still require an appropriate licensed/authorized sandbox.
- `python scripts/validate_profile.py` checks source file existence, profile section order, expected project card URLs, image references, SVG markup and primary contact links.
- Static validation cannot substitute for external uptime tests, desktop/mobile visual inspection, or Power BI, SQL Server, Python or Tableau runtime execution.

See [design system](../design/design-system.md), [Figma-ready handoff](../design/figma-handoff.md) and [responsive guidance](../design/responsive-spec.md).
