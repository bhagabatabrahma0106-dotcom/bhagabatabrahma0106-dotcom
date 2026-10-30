#!/usr/bin/env python3
"""Validate GitHub profile links, asset quality, and project-card safe zones.

This tool uses only Python's standard library and runs on each profile change.
It does not replace a browser screenshot review or check external HTTP uptime.
"""
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
OWNER = "bhagabatabrahma0106-dotcom"
PORTFOLIO = "https://bhagabata-brahma-data-analyst.vercel.app/"
LINKEDIN = "https://www.linkedin.com/in/bhagabata-brahma/"
PROJECTS = {
    "urbancart": "UrbanCartAnalysis",
    "pizza": "Pizza_Sales_Analysis",
    "edtech": "EdTech-Analysis",
    "superstore": "End-To-End-Data-Management",
    "banking": "Python-Data_Anlysis",
    "dynamics": "ERP-Reporting-Data-Analysis-using-Microsoft-Dynamics-365-F-O",
}
EXTRA_PROJECTS = ("INTERVIEW-GUIDE", "Excel-Advanced-Website")
REQUIRED = (
    "README.md", "assets/README.md",
    "assets/branding/profile-header.svg", "assets/branding/portfolio-cta.svg",
    "assets/diagrams/data-workflow.svg",
    "docs/VISUAL_DESIGN.md", "docs/PROFILE_MAINTENANCE.md",
    ".github/workflows/validate-profile.yml", "scripts/validate_profile.py",
) + tuple(f"assets/projects/{name}.svg" for name in PROJECTS)
ISSUES = []


def local(tag):
    return tag.rsplit("}", 1)[-1]


def number(node, attr, default=None):
    value = node.get(attr, default)
    return float(value) if value is not None else 0.0


def bounds_of_path(d):
    """Conservative extrema of supported absolute SVG path commands.

    Bézier control points are included, so the resulting bounds enclose curves.
    Unsupported or relative commands fail closed rather than silently passing.
    """
    tokens = re.findall(r"[A-Za-z]|[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?", d)
    points = []
    x = y = sx = sy = 0.0
    cmd = ""
    index = 0
    while index < len(tokens):
        if tokens[index].isalpha():
            cmd = tokens[index]
            index += 1
            if cmd in ("Z", "z"):
                x, y = sx, sy
                points.append((x, y))
                cmd = ""
                continue
        if cmd not in ("M", "L", "H", "V", "Q", "C"):
            raise ValueError(f"Unsupported path command {cmd!r} in {d!r}")
        count = {"M": 2, "L": 2, "H": 1, "V": 1, "Q": 4, "C": 6}[cmd]
        vals = list(map(float, tokens[index:index + count]))
        if len(vals) != count:
            raise ValueError("Incomplete SVG path")
        index += count
        if cmd in ("M", "L"):
            x, y = vals
            points.append((x, y))
            if cmd == "M":
                sx, sy = x, y
                cmd = "L"
        elif cmd == "H":
            x = vals[0]
            points.append((x, y))
        elif cmd == "V":
            y = vals[0]
            points.append((x, y))
        else:
            for a, b in zip(vals[::2], vals[1::2]):
                points.append((a, b))
            x, y = vals[-2:]
    if not points:
        raise ValueError("No points in SVG path")
    return points


def shape_points(group):
    """Get a conservative geometric envelope for the icon's direct children."""
    pts = []
    for node in group:
        kind = local(node.tag)
        if kind == "path":
            pts.extend(bounds_of_path(node.get("d", "")))
        elif kind == "rect":
            x, y, w, h = (number(node, p) for p in ("x", "y", "width", "height"))
            pts.extend(((x, y), (x + w, y + h)))
        elif kind == "circle":
            x, y, r = (number(node, p) for p in ("cx", "cy", "r"))
            pts.extend(((x - r, y - r), (x + r, y + r)))
        else:
            raise ValueError(f"Unexpected icon geometry {kind}")
    if not pts:
        raise ValueError("Icon has no geometry")
    return pts


def validate_card(name):
    path = ROOT / "assets" / "projects" / f"{name}.svg"
    svg = ET.parse(path).getroot()
    view = list(map(float, svg.attrib["viewBox"].split()))
    if view != [0.0, 0.0, 720.0, 224.0]:
        ISSUES.append(f"{name}: unexpected card viewBox")
    panels = [n for n in svg if local(n.tag) == "rect"
              and n.get("fill") == "#112E44"]
    if len(panels) != 1:
        ISSUES.append(f"{name}: icon panel missing or duplicated")
        return
    panel = panels[0]
    px, py, pw, ph = (number(panel, a) for a in ("x", "y", "width", "height"))
    if (px, py, pw, ph) != (572.0, 47.0, 112.0, 112.0):
        ISSUES.append(f"{name}: icon panel safe-area geometry changed")
    groups = [n for n in svg if local(n.tag) == "g" and n.get("transform")]
    if len(groups) != 1:
        ISSUES.append(f"{name}: expected exactly one icon group")
        return
    g = groups[0]
    match = re.fullmatch(
        r"translate\(([-+\d.]+) ([-+\d.]+)\) "
        r"scale\(([-+\d.]+)\) "
        r"translate\(([-+\d.]+) ([-+\d.]+)\)",
        g.get("transform", ""),
    )
    if match is None:
        ISSUES.append(f"{name}: icon transform no longer follows centering layout")
        return
    cx, cy, scale, offset_x, offset_y = map(float, match.groups())
    if scale <= 0 or scale > 0.75:
        ISSUES.append(f"{name}: icon scale exceeds safe range")
    pts = shape_points(g)
    xs = [cx + scale * (x + offset_x) for x, _ in pts]
    ys = [cy + scale * (y + offset_y) for _, y in pts]
    # Account for strokes on the icon boundary, conservatively.
    stroke_pad = 3.0
    left, right = min(xs) - stroke_pad, max(xs) + stroke_pad
    top, bottom = min(ys) - stroke_pad, max(ys) + stroke_pad
    margins = (left - px, px + pw - right, top - py, py + ph - bottom)
    if min(margins) < 12:
        ISSUES.append(f"{name}: icon too close to panel border ({min(margins):.1f}px)")
    if abs((left + right) / 2 - (px + pw / 2)) > 3:
        ISSUES.append(f"{name}: icon horizontally off-center")
    if abs((top + bottom) / 2 - (py + ph / 2)) > 3:
        ISSUES.append(f"{name}: icon vertically off-center")
    labels = [n for n in svg if local(n.tag) == "text"
              and "VIEW PROJECT" in "".join(n.itertext())]
    if len(labels) != 1 or number(labels[0], "x") < 575 or number(labels[0], "x") > 595:
        ISSUES.append(f"{name}: project link prompt not in safe area")


def validate():
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.is_file() or not path.stat().st_size:
            ISSUES.append(f"Missing or empty required file: {rel}")
    if ISSUES:
        return

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if readme.count("<details>") != readme.count("</details>"):
        ISSUES.append("Unbalanced expandable-details markup")
    if readme.count("| Project | Stack | What to explore |") != 1:
        ISSUES.append("Missing or duplicate detailed project table")
    for section in ("Featured projects", "Technical toolkit",
                    "Experience & education", "How I approach data work",
                    "Currently exploring", "Connect"):
        if f"## {section}" not in readme:
            ISSUES.append(f"Missing README section: {section}")

    for link in (PORTFOLIO, LINKEDIN, "mailto:bhagabatabrahma0106@gmail.com"):
        if link not in readme:
            ISSUES.append(f"Missing primary contact link: {link}")
    # Each project image must be wrapped by the correct clickable repository link.
    pairs = re.findall(
        r'<a\s+href="([^"]+)"[^>]*>\s*<img\s+src="([^"]+)"',
        readme, flags=re.DOTALL)
    card_pairs = [(href, src) for href, src in pairs
                  if src.startswith("assets/projects/")]
    if len(card_pairs) != len(PROJECTS):
        ISSUES.append(f"Expected {len(PROJECTS)} project card links, found {len(card_pairs)}")
    seen = set()
    for href, src in card_pairs:
        stem = Path(src).stem
        expected = PROJECTS.get(stem)
        if expected is None or stem in seen:
            ISSUES.append(f"Unknown or duplicate project card: {src}")
        elif href != f"https://github.com/{OWNER}/{expected}":
            ISSUES.append(f"Card {src} links to incorrect repository: {href}")
        seen.add(stem)
    if set(PROJECTS) != seen:
        ISSUES.append(f"Unlinked project cards: {sorted(set(PROJECTS) - seen)}")
    for name in (*PROJECTS.values(), *EXTRA_PROJECTS):
        if f"https://github.com/{OWNER}/{name}" not in readme:
            ISSUES.append(f"Missing repository in README: {name}")

    for src in re.findall(r'<img[^>]+src="([^"]+)"', readme):
        if src.startswith("assets/") and not (ROOT / src).is_file():
            ISSUES.append(f"Broken local image reference: {src}")
    for href in re.findall(r'<a\s+href="([^"]+)"', readme):
        if href.startswith("http"):
            parts = urlparse(href)
            if parts.scheme != "https" or not parts.netloc:
                ISSUES.append(f"Unsafe or malformed external link: {href}")

    for file in sorted((ROOT / "assets").rglob("*.svg")):
        try:
            root = ET.parse(file).getroot()
            if local(root.tag) != "svg":
                ISSUES.append(f"Not an SVG: {file}")
            tags = {local(elem.tag) for elem in root.iter()}
            if tags & {"script", "foreignObject", "animate", "animateTransform"}:
                ISSUES.append(f"Unsafe or fragile SVG element in {file}")
            if not any(local(x.tag) == "title" for x in root):
                ISSUES.append(f"Missing SVG title: {file}")
            if not any(local(x.tag) == "desc" for x in root):
                ISSUES.append(f"Missing SVG description: {file}")
        except ET.ParseError as exc:
            ISSUES.append(f"Malformed SVG: {file}: {exc}")
    for name in PROJECTS:
        try:
            validate_card(name)
        except (ValueError, ET.ParseError) as exc:
            ISSUES.append(f"{name}: cannot validate icon geometry: {exc}")


if __name__ == "__main__":
    validate()
    if ISSUES:
        print("Profile quality checks FAILED:")
        for issue in ISSUES:
            print(" -", issue)
        sys.exit(1)
    print("Passed: required files, SVG markup, image references,")
    print("exact card-to-repository links, contact links, and icon safe zones.")
    print("External HTTP availability and rendered browser layout were not tested.")
