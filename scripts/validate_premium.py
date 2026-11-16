#!/usr/bin/env python3
"""Brahma-Analytics premium profile static and image decode QA.

This validates repository source and media. It does not guarantee mobile browser
rendering, external site uptime, or execution of Power BI/SQL/Python/Tableau.
"""
from __future__ import annotations
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET
import re
import sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OWNER = "bhagabatabrahma0106-dotcom"
PROJECTS = {
    "urbancart": "UrbanCartAnalysis",
    "pizza-sales": "Pizza_Sales_Analysis",
    "edtech": "EdTech-Analysis",
    "superstore": "End-To-End-Data-Management",
    "banking": "Python-Data_Anlysis",
    "dynamics-365-fo": "ERP-Reporting-Data-Analysis-using-Microsoft-Dynamics-365-F-O",
}
PNG_FILES = [
    "assets/hero/analytics-banner.png",
    "assets/hero/analytics-banner-mobile.png",
    "assets/hero/analytics-banner-dark.png",
] + [f"assets/projects/{name}.png" for name in PROJECTS]
GIF_STEMS = ["analytics-workflow", "data-quality", "sql-to-dashboard"]
GIF_FILES = [f"assets/animations/{name}.gif" for name in GIF_STEMS]
PNG_FILES += [f"assets/animations/{name}.png" for name in GIF_STEMS]
SVG_FILES = [
    "assets/hero/analytics-banner.svg",
    "assets/hero/analytics-banner-mobile.svg",
    "assets/hero/analytics-banner-dark.svg",
    "assets/workflow/analytics-flow.svg",
    "assets/workflow/data-quality.svg",
    "assets/workflow/sql-to-dashboard.svg",
    "assets/technologies/toolkit.svg",
    "assets/banners/contact-premium.svg",
] + [f"assets/projects/{name}-premium.svg" for name in PROJECTS]
DOCS = [
    "README.md",
    "design/project-audit.md",
    "design/design-system.md",
    "design/figma-handoff.md",
    "design/responsive-spec.md",
    "design/component-library.md",
    "scripts/validate_premium.py",
]
H2 = ["About me", "Analytics workflow", "Technology stack", "Featured projects",
      "Technical toolkit", "How I approach data work", "Experience & education",
      "Currently exploring", "GitHub activity", "Let's connect"]


class ImageLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.links = []
        self.stack = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "a":
            self.stack.append(d.get("href"))
            self.links.append(d.get("href"))
        if tag == "img":
            self.images.append((d.get("src"), d.get("alt"), self.stack[-1] if self.stack else None))

    def handle_endtag(self, tag):
        if tag == "a" and self.stack:
            self.stack.pop()


def local(tag):
    return tag.rsplit("}", 1)[-1]


def run():
    errors = []
    for rel in [*DOCS, *PNG_FILES, *SVG_FILES, *GIF_FILES]:
        p = ROOT / rel
        if not p.is_file() or p.stat().st_size <= 0:
            errors.append(f"Missing or empty: {rel}")
    if errors:
        return errors

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    headings = [m.group(1).strip() for m in re.finditer(r"^## (.+)$", readme, re.M)]
    indices = []
    for name in H2:
        matches = [i for i, item in enumerate(headings) if name in item]
        if len(matches) != 1:
            errors.append(f"Missing or duplicated section: {name}")
        else:
            indices.append(matches[0])
    if indices != sorted(indices):
        errors.append("README H2 section order changed")
    if readme.count("<details>") != readme.count("</details>"):
        errors.append("Malformed expandable details")
    if re.search(r"<(?:style|script|iframe|object|form)\\b", readme, re.I):
        errors.append("Unsupported README HTML element")
    if "avatars.githubusercontent.com" in readme:
        errors.append("Duplicate photo in README hero; use GitHub native sidebar")

    parser = ImageLinks()
    parser.feed(readme)
    for src, alt, href in parser.images:
        if not src or not alt:
            errors.append(f"Missing image src or alt: {src}")
        if src and src.startswith("assets/") and not (ROOT / src).is_file():
            errors.append(f"Broken local README image path: {src}")
    expected = {f"assets/projects/{key}-premium.svg": f"https://github.com/{OWNER}/{repo}" for key, repo in PROJECTS.items()}
    found = [(src, href) for src, alt, href in parser.images if src and src.startswith("assets/projects/") and src.endswith("-premium.svg")]
    if len(found) != 6:
        errors.append(f"Expected six featured card images; found {len(found)}")
    for src, url in found:
        if expected.get(src) != url:
            errors.append(f"Wrong project destination for {src}: {url}")
    if not all(f"assets/animations/{name}.gif" in readme for name in GIF_STEMS):
        errors.append("README missing one of three animation references")
    for name in PROJECTS.values():
        if f"https://github.com/{OWNER}/{name}" not in readme:
            errors.append(f"Missing source repository URL: {name}")
    for url in ["https://www.linkedin.com/in/bhagabata-brahma/",
                "https://bhagabata-brahma-data-analyst.vercel.app/",
                "mailto:bhagabatabrahma0106@gmail.com"]:
        if url not in readme:
            errors.append(f"Missing contact link: {url}")

    for rel in SVG_FILES:
        try:
            root = ET.parse(ROOT / rel).getroot()
            if local(root.tag) != "svg":
                errors.append(f"Not an SVG: {rel}")
            tags = {local(node.tag) for node in root.iter()}
            if tags.intersection({"script", "foreignObject", "animate", "animateTransform"}):
                errors.append(f"Unsupported inline SVG markup: {rel}")
            if "title" not in tags or "desc" not in tags:
                errors.append(f"Missing SVG accessible label: {rel}")
            if len(root.get("viewBox", "").split()) != 4:
                errors.append(f"Missing SVG viewBox: {rel}")
        except ET.ParseError as exc:
            errors.append(f"Broken XML for {rel}: {exc}")

    for rel in PNG_FILES:
        try:
            with Image.open(ROOT / rel) as img:
                if img.format != "PNG" or img.width < 100 or img.height < 50:
                    errors.append(f"Unexpected PNG image format or dimensions: {rel}")
                img.load()
        except Exception as exc:
            errors.append(f"Cannot decode PNG {rel}: {exc}")

    for rel in GIF_FILES:
        try:
            f = ROOT / rel
            if f.stat().st_size > 900_000:
                errors.append(f"GIF exceeds 900 KB budget: {rel}")
            with Image.open(f) as img:
                if img.format != "GIF" or img.n_frames < 24:
                    errors.append(f"GIF has insufficient frames: {rel}")
                duration = 0
                for i in range(img.n_frames):
                    img.seek(i)
                    img.load()  # Fully exercise the LZW decoder
                    duration += img.info.get("duration", 0)
                if not 7500 <= duration <= 10000:
                    errors.append(f"Unexpected animation duration {duration}ms: {rel}")
        except Exception as exc:
            errors.append(f"Cannot decode GIF {rel}: {exc}")

    return errors


if __name__ == "__main__":
    problems = run()
    if problems:
        print("Premium profile QA FAILED:")
        for issue in problems:
            print(" -", issue)
        sys.exit(1)
    print("Passed: 10 sections, 6 card links, local assets, image decode, GIF timing, SVG validity.")
    print("Not tested: external HTTP uptime, browser layout, runtime dashboards or private settings.")
