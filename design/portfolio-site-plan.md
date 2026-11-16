# Separate interactive portfolio website — implementation plan only

**Scope boundary:** This file is a handoff. No changes are made to any of the three protected portfolio repositories.

## Suggested implementation

- Use the existing portfolio's framework and deployment pipeline; inspect it before choosing libraries.
- Design at 1440, 768 and 390 px; adapt the same token system from `design-system.md`.
- Hero and projects on the website can use CSS Grid and actual responsive breakpoints; the GitHub README cannot.
- Add lightweight hover/focus transitions, step timeline reveal and restrained SVG gradient movement only where supported.
- Honor `prefers-reduced-motion: reduce`.
- Wire project links to their current public repositories; only add real live demo URLs when verified.
- Include image compression, `loading="lazy"`, focus-visible styling, semantic landmarks, keyboard navigation and accessible text alternatives.
- Audit actual data claims and use real screenshots only after checking they match project files.
- Run Lighthouse, mobile viewport tests and deployment smoke tests before publication.

## Suggested sequence

1. Inventory framework, routes, data and current portfolio design (read-only).
2. Create design tokens and base responsive layout in a review branch.
3. Implement header, hero, case-study cards, toolkit, workflow, timeline and contact.
4. Add media assets and verified project links; no fabricated stats.
5. Validate accessibility, performance, content and responsive behavior.
6. Publish only with separate authorization to change the protected website repositories.

**Status:** Planning document only; not an implementation or a claim of deployment.

## v3 implementation status

The separate `Bhagabata-Portfolio-Data-Analyst` feature branch contains `PremiumStudio.tsx`, `PremiumLearning.tsx`, six local project artwork SVGs, and `App.tsx` changes to render evidence-led sections while preserving older source files. A branch-only GitHub Actions build is configured. No merge, production Vercel deployment, or modifications to the other portfolio repositories are claimed. This section supersedes the earlier plan-only status.
