# Brahma-Analytics — design system v2

**Purpose:** premium, readable dark analytics identity for the GitHub profile README, derived from the supplied visual reference. Static SVGs are illustrations, not actual Power BI screens or business metrics. The real GitHub profile avatar is used separately in README.

## Tokens

| Role | Value | Use |
|---|---|---|
| Primary background | `#080E1C` | Overall dark backdrop |
| Secondary background | `#101A2E` | Card surfaces |
| Brand purple | `#7C3AED` | Hero/project accents |
| Indigo | `#4F46E5` | Secondary emphasis |
| Electric blue | `#2563EB` | Process/data panels |
| Cyan | `#22D3EE` | Informational highlights |
| Teal | `#14B8A6` | Data-quality accents |
| Amber | `#F59E0B` | Power BI and retail accents |
| Primary text | `#F8FAFC` | Titles and copy |
| Muted text | `#94A3B8` | Supporting labels |

**Typography:** Inter is preferred in a website/Figma composition; README embedded SVGs use Arial/Helvetica sans-serif for broad renderer compatibility. Display 48–60 px (Figma desktop), section title 28–32, card title 22–26, body 16/24, caption 13/20. SVG artwork uses proportionally larger text because it scales down in README.

**Spacing scale:** 4, 8, 12, 16, 20, 24, 32, 40, 64 px. Base card radius 16 px, large banner 24 px, chips 999 px. Borders 1–2 px low-contrast accent color. Shadows/glows belong to separate web use; SVG artwork uses restrained tinted highlights.

## Component definitions

| Component | Figma desktop base | Figma mobile behavior | Source asset / README |
|---|---|---|---|
| Hero | 1200 × 360 SVG, 24 radius | Full width image, followed by live-text intro and avatar | `assets/v2/hero/hero-banner.svg` |
| Workflow | 1200 × 194 SVG | Textual five-stage fallback below illustration | `assets/v2/workflow/analytics-workflow.svg` |
| Technology group | 1200 × 250 SVG | Accessible Markdown tool list below graphic | `assets/v2/technologies/stack.svg` |
| Project card | 1000 × 276 SVG | **Single column** to keep title legible on GitHub mobile | `assets/v2/projects/{name}.svg` |
| Approach | 1200 × 186 SVG | Text steps beside graphic in linear order | `assets/v2/workflow/approach.svg` |
| Activity | 1200 × 164 SVG | Illustrative grid; real stats only via GitHub profile link | `assets/v2/banners/activity.svg` |
| Contact banner | 1200 × 209 SVG | Full width with semantic text links underneath | `assets/v2/banners/contact.svg` |

### States and interactions

GitHub README: image is not an interactive component itself. Wrap hero/project graphic with a real `<a href>` only when destination exists. All real controls are ordinary Markdown links. No fake buttons, custom CSS, JS, hover effects, external widget counters or fake live dashboard metrics.

Portfolio website *plan only* (not implemented): links have default / hover / focus-visible / pressed / disabled states; contrast at least WCAG AA for body text; hover motion 120–180 ms; `prefers-reduced-motion: reduce` disables movement.

## Design quality rules

- Alt text describes the visual or destination; don't claim graphics are genuine dashboard screenshots.
- Never show static illustrated contributions as real GitHub statistics.
- Preserve source README descriptions and disclaimers.
- Validate SVG XML; no `script`, `foreignObject`, external fonts, external SVG images, CSS animations or native JavaScript.
- Keep logos illustrative rather than misrepresenting brand ownership or certification.
