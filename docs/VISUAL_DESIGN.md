# Visual design and maintenance notes

This profile has a future-friendly visual layer while preserving the original README's factual text, link destinations, section hierarchy and project table.

## Local assets

- [Profile hero](../assets/profile-header.svg) — portfolio-linked header, names/skills from the original README.
- [Six project cards](../assets/) — each separately linked to its corresponding GitHub repository.
- [Skills overview](../assets/skills-overview.svg) — categories already documented in the README; no proficiency percentages are claimed.
- [Career timeline](../assets/career-timeline.svg) — same education and employment dates as README (not an invented chronology).
- [Data workflow](../assets/data-workflow.svg) — visual companion to the unchanged five-step text workflow.
- [Portfolio call to action](../assets/portfolio-cta.svg) — links to the established live-portfolio URL.

## Motion, compatibility and accessibility

The hero contains decorative SVG animation with a readable static state. **GitHub's SVG image proxy, security policies, or accessibility preferences may prevent animation from displaying.** Never rely on motion to convey important information. The hero has an accessible title/description, visual images have alt text, and the project cards remain separate clickable links. All source details remain visible in text without loading the images.

GitHub Markdown does not provide general JavaScript interactivity, editable web-app widgets, or custom CSS page controls. Use the hosted portfolio for richer browser interactions.

## Maintenance

- Preserve the existing factual claims and original project table when updating visuals.
- Use the official repository URL for each clickable project card.
- Do not introduce fabricated metrics, visitor counters, credentials, certifications or other unsupported claims.
- Prefer local SVG graphics over external services.
- Check all links and images periodically.
- The profile repository is the target of this styling update; project repositories and external deployments were not modified.

[Return to GitHub profile](../README.md).
