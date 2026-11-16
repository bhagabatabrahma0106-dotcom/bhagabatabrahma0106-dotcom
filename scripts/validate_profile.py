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
] + SVG_ASSETS
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
