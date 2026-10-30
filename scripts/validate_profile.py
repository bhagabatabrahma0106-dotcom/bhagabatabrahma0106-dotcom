#!/usr/bin/env python3
"""Static, dependency-free validation for Bhagabata's GitHub profile graphics.

Tests files, links and conservative SVG title safe zones; not a screenshot test.
"""
from pathlib import Path
from xml.etree import ElementTree as ET
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "assets/README.md",
    "assets/branding/profile-header.svg",
    "assets/branding/portfolio-cta.svg",
    "assets/diagrams/data-workflow.svg",
    "assets/projects/urbancart.svg",
    "assets/projects/pizza.svg",
    "assets/projects/edtech.svg",
    "assets/projects/superstore.svg",
    "assets/projects/banking.svg",
    "assets/projects/dynamics.svg",
    "docs/VISUAL_DESIGN.md",
)
REPOSITORIES = (
    "UrbanCartAnalysis",
    "Pizza_Sales_Analysis",
    "EdTech-Analysis",
    "End-To-End-Data-Management",
    "Python-Data_Anlysis",
    "ERP-Reporting-Data-Analysis-using-Microsoft-Dynamics-365-F-O",
)
issues = []
for rel in REQUIRED:
    path = ROOT / rel
    if not path.is_file() or path.stat().st_size == 0:
        issues.append(f"Missing or empty: {rel}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for image_path in re.findall(r'<img[^>]+src="([^"]+)"', readme):
    if image_path.startswith("assets/") and not (ROOT / image_path).is_file():
        issues.append(f"Broken image: {image_path}")
for repository in REPOSITORIES:
    expected = f"https://github.com/bhagabatabrahma0106-dotcom/{repository}"
    if expected not in readme:
        issues.append(f"Missing project link: {repository}")
for section in ("Featured projects", "Technical toolkit",
                "Experience & education", "How I approach data work", "Connect"):
    if f"## {section}" not in readme:
        issues.append(f"Missing README section: {section}")

for path in sorted((ROOT / "assets").rglob("*.svg")):
    rel = path.relative_to(ROOT).as_posix()
    try:
        svg = ET.parse(path).getroot()
    except ET.ParseError as exc:
        issues.append(f"Malformed SVG {rel}: {exc}")
        continue
    if not svg.tag.endswith("svg"):
        issues.append(f"Not SVG: {rel}")
        continue
    try:
        minx, miny, w, h = map(float, svg.attrib["viewBox"].split())
        if w <= 0 or h <= 0:
            raise ValueError("non-positive dimensions")
    except (ValueError, KeyError):
        issues.append(f"Bad SVG viewBox: {rel}")
        continue
    names = {node.tag.split("}")[-1] for node in svg.iter()}
    if "script" in names or "foreignObject" in names or "animate" in names:
        issues.append(f"Unsupported SVG elements: {rel}")
    titles = [node for node in svg if node.tag.endswith("title")]
    descriptions = [node for node in svg if node.tag.endswith("desc")]
    if not titles or not descriptions:
        issues.append(f"Missing accessible SVG title/description: {rel}")
    # Conservative layout check: the 2 large title lines in 720px cards
    # must end well before the right icon panel beginning at x=579.
    if rel.startswith("assets/projects/"):
        if w != 720 or h != 224:
            issues.append(f"Unexpected card dimensions: {rel}")
        lines = []
        for node in svg.iter():
            if not node.tag.endswith("text"):
                continue
            try:
                x = float(node.attrib.get("x", "0"))
                y = float(node.attrib.get("y", "0"))
                size = float(node.attrib.get("font-size", "0"))
            except ValueError:
                issues.append(f"Unparseable text dimensions: {rel}")
                continue
            text = "".join(node.itertext()).strip()
            # An intentionally generous upper bound to catch title text
            # spilling into the icon (not a full font-layout engine).
            if size >= 30 and x < 100:
                width_estimate = len(text) * size * .62
                if x + width_estimate > 560:
                    issues.append(f"Possible title/icon overlap: {rel}: {text}")
                lines.append(y)
            if x >= 590 and size <= 15:
                if x + len(text) * size * .62 > w - 8:
                    issues.append(f"Right side label may clip: {rel}: {text}")
        if sorted(lines) != [98.0, 142.0]:
            issues.append(f"Card title baselines changed: {rel}: {lines}")

if issues:
    print("Profile validation FAILED:")
    for issue in issues:
        print(" -", issue)
    sys.exit(1)
print("Profile README links, required files, SVG syntax and conservative layout checks passed.")
print("Note: this is static checking, not a browser-rendered GitHub/mobile visual test.")
