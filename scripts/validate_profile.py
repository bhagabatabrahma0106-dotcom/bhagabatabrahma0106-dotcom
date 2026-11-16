#!/usr/bin/env python3
"""Static integrity checks for the public GitHub profile README.

This checks repository source integrity, not external HTTP uptime, GitHub's
rendered layout, or Power BI / SQL / Python / Tableau runtime behavior.
"""
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OWNER = "bhagabatabrahma0106-dotcom"
BASE = f"https://github.com/{OWNER}"
PROJECTS = {
    "urbancart": "UrbanCartAnalysis",
    "pizza": "Pizza_Sales_Analysis",
    "edtech": "EdTech-Analysis",
    "superstore": "End-To-End-Data-Management",
    "banking": "Python-Data_Anlysis",
    "dynamics": "ERP-Reporting-Data-Analysis-using-Microsoft-Dynamics-365-F-O",
}
ANIMATION = "assets/v2/animations/analytics-flow.gif"
SVG_ASSETS = [
    "assets/v2/hero/hero-banner.svg",
    "assets/v2/workflow/analytics-workflow.svg",
    "assets/v2/workflow/approach.svg",
    "assets/v2/technologies/stack.svg",
    "assets/v2/banners/contact.svg",
    "assets/v2/banners/activity.svg",
] + [f"assets/v2/projects/{slug}.svg" for slug in PROJECTS]
REQUIRED = [
    "README.md", "assets/README.md", "docs/VISUAL_DESIGN.md",
    "docs/PROFILE_MAINTENANCE.md", "scripts/validate_profile.py",
    ".github/workflows/validate-profile.yml",
    "design/design-system.md", "design/figma-handoff.md",
    "design/responsive-spec.md", "design/portfolio-site-plan.md",
] + SVG_ASSETS + [ANIMATION]
HEADINGS = [
    "About me", "Analytics workflow", "Technology stack", "Featured projects",
    "Technical toolkit", "How I approach data work", "Experience & education",
    "Currently exploring", "GitHub activity", "Let's connect",
]
ISSUES = []


def local(tag):
    return tag.rsplit("}", 1)[-1]


def validate():
    for path in REQUIRED:
        f = ROOT / path
        if not f.is_file() or not f.stat().st_size:
            ISSUES.append(f"Missing or empty required file: {path}")
    if ISSUES:
        return

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    headings = [s.strip() for s in re.findall(r"^## (.+)$", readme, re.M)]
    last_index = -1
    for target in HEADINGS:
        matching = [i for i, heading in enumerate(headings) if target in heading]
        if len(matching) != 1:
            ISSUES.append(f"Expected exactly one section: {target}")
        elif matching[0] <= last_index:
            ISSUES.append(f"Out-of-order section: {target}")
        else:
            last_index = matching[0]

    for url in (
        "https://bhagabata-brahma-data-analyst.vercel.app/",
        "https://www.linkedin.com/in/bhagabata-brahma/",
        "mailto:bhagabatabrahma0106@gmail.com",
    ):
        if url not in readme:
            ISSUES.append(f"Missing primary contact URL: {url}")

    if "avatars.githubusercontent.com" in readme:
        ISSUES.append("The hero must not include a duplicate profile portrait")
    if readme.count(ANIMATION) != 1:
        ISSUES.append("Missing or duplicated optional workflow GIF reference")
    if readme.count("<details>") != readme.count("</details>"):
        ISSUES.append("Unbalanced expandable details blocks")
    if re.search(r"<(script|style|iframe|object|form)\b", readme, re.I):
        ISSUES.append("Unsupported or unsafe HTML element in README")

    pairs = re.findall(
        r'<a\s+href="([^"]+)"[^>]*>\s*<img\s+src="([^"]+)"',
        readme, re.S,
    )
    linked_cards = [
        (url, path) for url, path in pairs
        if path.startswith("assets/v2/projects/")
    ]
    if len(linked_cards) != len(PROJECTS):
        ISSUES.append(
            f"Expected six clickable project cards, found {len(linked_cards)}"
        )
    seen = set()
    for href, src in linked_cards:
        slug = Path(src).stem
        if slug not in PROJECTS or slug in seen:
            ISSUES.append(f"Unexpected or repeated project card: {src}")
        else:
            expected = f"{BASE}/{PROJECTS[slug]}"
            if href != expected:
                ISSUES.append(f"Incorrect project URL for {slug}: {href}")
        seen.add(slug)
    for slug, name in PROJECTS.items():
        if slug not in seen:
            ISSUES.append(f"Project card missing: {slug}")
        if f"{BASE}/{name}" not in readme:
            ISSUES.append(f"Repository missing from README: {name}")
    for name in ("INTERVIEW-GUIDE", "Excel-Advanced-Website"):
        if f"{BASE}/{name}" not in readme:
            ISSUES.append(f"Related project link missing: {name}")

    for src in re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', readme):
        if src.startswith("assets/"):
            f = ROOT / src
            if not f.is_file() or f.stat().st_size == 0:
                ISSUES.append(f"Broken local image reference: {src}")
        elif src.startswith(("http://", "https://")):
            host = urlparse(src).netloc
            if host not in ("avatars.githubusercontent.com",):
                ISSUES.append(f"Unapproved external image host: {src}")
        else:
            ISSUES.append(f"Unexpected image reference: {src}")

    for href in re.findall(r'<a\b[^>]*\bhref="([^"]+)"', readme):
        if href.startswith("http"):
            parsed = urlparse(href)
            if parsed.scheme != "https" or not parsed.netloc:
                ISSUES.append(f"Unsafe external link: {href}")

    # GIF is optional to view, but the referenced asset must be valid and modest in size.
    gif = (ROOT / ANIMATION).read_bytes()
    if not gif.startswith((b"GIF89a", b"GIF87a")) or not gif.endswith(b";"):
        ISSUES.append("Workflow motion asset is not a valid GIF container")
    if len(gif) > 350_000:
        ISSUES.append("Optional workflow GIF exceeds 350 KB size budget")
    if len(gif) < 20 or int.from_bytes(gif[6:8], "little") != 480 or int.from_bytes(gif[8:10], "little") != 70:
        ISSUES.append("Workflow GIF has unexpected dimensions")
    if gif.count(bytes((0x21, 0xF9, 0x04))) < 2:
        ISSUES.append("Workflow GIF does not appear to have multiple frames")

    # Conservative text-boundary checks on the current artwork.
    # This checks gross geometry only; a rasterized browser review is still needed.
    def estimated_text_width(value, font_size):
        units = 0.0
        for ch in value:
            if ch in "ilI|!.,:; '":
                units += 0.29
            elif ch in "MW@%&":
                units += 0.86
            elif ch.isupper():
                units += 0.69
            elif ch in "fjrt":
                units += 0.43
            else:
                units += 0.58
        return units * font_size * 1.10

    for relative in SVG_ASSETS:
        svg = ET.parse(ROOT / relative).getroot()
        parts = [float(x) for x in svg.get("viewBox", "").split()]
        if len(parts) != 4:
            continue
        width = parts[2]
        for node in svg.iter():
            if local(node.tag) != "text":
                continue
            x = float(node.get("x", "0"))
            font_size = float(node.get("font-size", "16"))
            content = "".join(node.itertext())
            text_width = estimated_text_width(content, font_size)
            anchor = node.get("text-anchor", "start")
            left = x - text_width if anchor == "end" else (x - text_width / 2 if anchor == "middle" else x)
            right = left + text_width
            if left < 7 or right > width - 7:
                ISSUES.append(
                    f"Potential text clipping: {relative}: {content[:50]!r}"
                )
            if "/projects/" in relative and x < 625 and right > 628:
                ISSUES.append(
                    f"Project label intrudes into chart zone: {relative}: {content[:50]!r}"
                )
            if "/hero/" in relative and x < 650 and right > 665:
                ISSUES.append(
                    f"Hero label intrudes into illustration zone: {content[:50]!r}"
                )

    for f in sorted((ROOT / "assets").rglob("*.svg")):
        try:
            root = ET.parse(f).getroot()
            if local(root.tag) != "svg":
                ISSUES.append(f"Not SVG: {f}")
            tags = {local(node.tag) for node in root.iter()}
            if tags & {"script", "foreignObject", "animate", "animateTransform"}:
                ISSUES.append(f"Unsupported SVG element: {f}")
            for needed in ("title", "desc"):
                if not any(local(node.tag) == needed for node in root):
                    ISSUES.append(f"SVG lacks {needed}: {f}")
            viewbox = root.attrib.get("viewBox", "")
            if len(viewbox.split()) != 4:
                ISSUES.append(f"SVG missing four-value viewBox: {f}")
        except ET.ParseError as exc:
            ISSUES.append(f"Malformed SVG: {f}: {exc}")


if __name__ == "__main__":
    validate()
    if ISSUES:
        print("Profile static validation FAILED:")
        for issue in ISSUES:
            print(" -", issue)
        sys.exit(1)
    print("Passed: README sections/order, verified project destinations,")
    print("image paths, contact URLs and static SVG markup.")
    print("Not checked: HTTP uptime, GitHub rendering, or application runtimes.")
