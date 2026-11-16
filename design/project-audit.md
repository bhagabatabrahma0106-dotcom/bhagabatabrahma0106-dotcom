# Brahma-Analytics — source audit

**Audit date:** 2026-11-16  
**Working branch:** `feat/premium-profile-redesign`  
**Primary source:** profile repository's `main` branch as of the start of this redesign. The live portfolio source was inspected separately.

## Current repository

Profile repository: [bhagabatabrahma0106-dotcom/bhagabatabrahma0106-dotcom](https://github.com/bhagabatabrahma0106-dotcom/bhagabatabrahma0106-dotcom).

Existing root:
- `README.md`: complete dark analytics profile README with ten markdown H2 sections and six linked featured project cards.
- `assets/branding/`: previous SVG hero and CTA.
- `assets/projects/`: six legacy SVG cards.
- `assets/diagrams/`: current-focus and workflow SVG diagrams.
- `assets/v2/hero/`: one styled hero SVG.
- `assets/v2/projects/`: six styled project-card SVG illustrations.
- `assets/v2/technologies/`: stack SVG.
- `assets/v2/workflow/`: workflow and process SVGs.
- `assets/v2/animations/`: an optional 480×70 GIF.
- `assets/v2/banners/`: activity and contact SVGs.
- `design/`, `docs/`, `scripts/validate_profile.py`, and `.github/workflows/validate-profile.yml`: source documentation and CI integrity check.

## Existing README sections

1. About me
2. Analytics workflow
3. Technology stack
4. Featured projects
5. Technical toolkit
6. How I approach data work
7. Experience & education
8. Currently exploring
9. GitHub activity
10. Let's connect

The hero precedes these H2 sections. Six project images and README content have existing explanatory alt text and source links.

## Existing project destinations

| Project | Repository |
|---|---|
| UrbanCart | [UrbanCartAnalysis](https://github.com/bhagabatabrahma0106-dotcom/UrbanCartAnalysis) |
| Pizza Sales | [Pizza_Sales_Analysis](https://github.com/bhagabatabrahma0106-dotcom/Pizza_Sales_Analysis) |
| EdTech App | [EdTech-Analysis](https://github.com/bhagabatabrahma0106-dotcom/EdTech-Analysis) |
| SuperStore | [End-To-End-Data-Management](https://github.com/bhagabatabrahma0106-dotcom/End-To-End-Data-Management) |
| Banking | [Python-Data_Anlysis](https://github.com/bhagabatabrahma0106-dotcom/Python-Data_Anlysis) |
| Dynamics F&O | [ERP-Reporting-Data-Analysis-using-Microsoft-Dynamics-365-F-O](https://github.com/bhagabatabrahma0106-dotcom/ERP-Reporting-Data-Analysis-using-Microsoft-Dynamics-365-F-O) |

The existing profile also links to a [portfolio](https://bhagabata-brahma-data-analyst.vercel.app/), [LinkedIn](https://www.linkedin.com/in/bhagabata-brahma/), and an email contact. No verified resume URL was found in the README, so no resume CTA will be fabricated.

## Factual identity (as instructed, not independently credential-verified)

- Bhagabata Brahma — Data Analyst / Power BI Developer / Data Quality & Governance.
- B.Tech CSE, Satyasai Engineering College (BPUT), 2022–2026, CGPA 8.04, consistent with the supplied latest project brief and current live portfolio data.
- Existing profile describes Data Gyan Data Analyst internship Oct 2025–Feb 2026 and Gohra Technologies trainee/intern exposure Oct 2025–present, including limited scope and caution around production evidence.
- Public repository READMEs, not the decorative graphics, supply factual project scope.

## Live portfolio source inspected

`Bhagabata-Portfolio-Data-Analyst` is a React 19 + Vite 8 + TypeScript portfolio, with Tailwind, Framer Motion, GSAP and Recharts already present. Canonical domain in `index.html` matches the supplied live Vercel URL. Existing sections include Hero, Statistics, Projects, Experience, Skills, About, Certificates, Services, SkillLab and Contact. There is already animation and UI complexity; do not replace the framework or remove current sections.

**Risk:** portions of the existing React `Projects.tsx` display demo-like counters labeled “LIVE” and numerical analytics examples. They require independent reconciliation before any factual KPI claims. This redesign will avoid republishing those as real business outcomes. The user's previous requirement to preserve portfolio source is respected by changing only an isolated review branch, with no production merge or deployment.

## Design gaps / changes required

- Create source-controlled project audit, unified tokens and exportable frame/spec references.
- Correct crowded or hard-to-read text zones, preserve existing work.
- Add source-compliant hero and six project thumbnails with image fallbacks.
- Add three **illustrative** GIF motion stories and static fallbacks; use reduced-motion-friendly CSS on the website.
- Add a self-contained interactive portfolio showcase on a feature branch without rewriting the existing React application.
- Expand source integrity validation and accurately report its scope.
- Do not alter GitHub native sidebar/avatar or invent follower/stars, production KPIs, deployments or real project screenshots.

## Technical / QA limitations

- GitHub profile README cannot execute arbitrary HTML, custom CSS or JS. Animated GIFs may move without a reduced-motion hook; provide static fallbacks and optional motion controls where possible.
- Figma connector unavailable in the current connected tool inventory; provide Figma-ready frame definitions, SVGs, measurement specs and component library.
- The connected GitHub API can commit source and assets, but a passing GitHub Actions static check is not equivalent to a screenshot-based visual or Power BI/SQL/Python/Tableau runtime review.
- Site branch changes are review-only; no GitHub branch merge, Vercel production deploy or modification to the other two portfolio repos.

## Preserve

Original main branch, all README history, all legacy `assets/`, existing six source repositories, original portfolio app components and dependency versions, existing CI, contact and project references. No destructive action is planned.

## Checklist

- [x] Inspect profile README and repository structure
- [x] Inspect six project destinations from profile
- [x] Inspect live website's framework, README, package and key component architecture
- [x] Create dedicated feature branches
- [x] Generate and validate new assets
- [x] Implement branch-only README/website changes
- [x] Run static and browser checks; correct failures
- [x] Write final delivery report with evidence and limitations
