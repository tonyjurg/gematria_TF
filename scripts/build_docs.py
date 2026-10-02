"""Build the GitHub Pages documentation from Markdown and validate local links."""
import argparse
import html
import re
import shutil
from html.parser import HTMLParser
from pathlib import Path
from string import Template
from urllib.parse import quote, unquote, urlsplit, urlunsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPO = "https://github.com/tonyjurg/gematria_TF"
# File stem, page title, navigation group. A None group means a linked subpage.
PAGES = [
    ("index", "Overview", "Start here"),
    ("getting-started", "Using the dataset", "Start here"),
    ("methods", "Methods & conventions", "Explore"),
    ("examples", "Worked examples", "Explore"),
    ("features", "Feature catalogue", "Explore"),
    ("technical", "Technical reference", "Reference"),
    ("generate", "Regenerate or extend", "Reference"),
    ("sources", "Sources & citation", "Reference"),
    ("legal", "License & access", "Reference"),
    ("representations", "Representation specification", None),
    ("bhsa-audit", "Source audit", None),
    ("validation", "Validation results", None),
    ("publishing", "Building & publishing", None),
]


def link_target(url):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return url
    target = (DOCS / unquote(parts.path)).resolve()
    if target.is_relative_to(DOCS):
        if not target.is_file():
            raise ValueError(f"Missing documentation link target: {url}")
        local = target.relative_to(DOCS)
        if local.suffix == ".md":
            if local.stem not in {p[0] for p in PAGES}:
                raise ValueError(f"Markdown page not registered: {url}")
            local = local.with_suffix(".html")
        return urlunsplit(("", "", local.as_posix(), parts.query, parts.fragment))
    if not target.is_relative_to(ROOT) or not target.exists():
        raise ValueError(f"Missing repository link target: {url}")
    kind = "tree" if target.is_dir() else "blob"
    path = quote(target.relative_to(ROOT).as_posix())
    return f"{REPO}/{kind}/main/{path}" + (f"#{parts.fragment}" if parts.fragment else "")


def rewrite_links(body):
    return re.sub(r'(href|src)="([^"]+)"',
                  lambda m: f'{m[1]}="{html.escape(link_target(html.unescape(m[2])), quote=True)}"', body)


def navigation(current):
    result, previous = [], None
    for stem, title, group in PAGES:
        if group is None:
            continue
        if group != previous:
            if previous:
                result.append("</ul>")
            result.append(f'<p class="nav-group">{group}</p><ul>')
            previous = group
        active = ' aria-current="page"' if stem == current else ""
        result.append(f'<li><a href="{stem}.html"{active}>{html.escape(title)}</a></li>')
    result.append("</ul>")
    return "".join(result)


class PageLinks(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if "id" in attributes:
            if attributes["id"] in self.ids:
                raise ValueError(f"Duplicate id: {attributes['id']}")
            self.ids.add(attributes["id"])
        for attr in ("href", "src"):
            if attr in attributes:
                self.links.append(attributes[attr])


def validate(output):
    pages = {p.resolve(): PageLinks(p.read_text(encoding="utf-8")) for p in output.glob("*.html")}
    count = 0
    for path, page in pages.items():
        for url in page.links:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not target.is_relative_to(output.resolve()) or not target.is_file():
                raise ValueError(f"{path.name}: broken local link {url}")
            if parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                raise ValueError(f"{path.name}: missing anchor {url}")
            count += 1
    return count


def build(output):
    output = output.resolve()
    # Never write build results over source/reference files or outside output/.
    if not output.is_relative_to(ROOT / "output") or output == ROOT / "output":
        raise ValueError("Build destination must be a subdirectory of this repository's output folder")
    output.mkdir(parents=True, exist_ok=True)
    template = Template((DOCS / "_site/template.html").read_text(encoding="utf-8"))
    for stem, title, group in PAGES:
        source = DOCS / f"{stem}.md"
        body = markdown.markdown(source.read_text(encoding="utf-8"), extensions=["tables", "fenced_code", "toc"])
        body = rewrite_links(body).replace("<table>", '<div class="table-wrap" role="region" aria-label="Reference table" tabindex="0"><table>').replace("</table>", "</table></div>")
        result = template.substitute(title=html.escape(title), section=group or "Technical reference",
            description=html.escape(f"{title}: gematria_TF documentation for the BHSA Hebrew Bible dataset."),
            navigation=navigation(stem), body=body, source_url=f"{REPO}/blob/main/docs/{stem}.md")
        (output / f"{stem}.html").write_text(result, encoding="utf-8", newline="\n")
    shutil.copytree(DOCS / "assets", output / "assets", dirs_exist_ok=True)
    shutil.copy2(DOCS / "bhsa-audit.json", output / "bhsa-audit.json")
    (output / ".nojekyll").write_text("", encoding="utf-8")
    links = validate(output)
    print(f"Built {len(PAGES)} documentation pages; checked {links} local links: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "output/site")
    build(parser.parse_args().output)
