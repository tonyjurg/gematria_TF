import json
from pathlib import Path
import re


NOTEBOOK = Path(__file__).resolve().parents[1] / "genesis1_duplicate_gematria.ipynb"


def cells():
    return json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]


def test_all_notebook_menu_links_resolve():
    markdown = "\n".join("".join(c["source"]) for c in cells() if c["cell_type"] == "markdown")
    anchors = re.findall(r'id="([^"]+)"', markdown)
    links = re.findall(r'href="#([^"]+)"|\]\(#([^)]+)\)', markdown)
    assert len(anchors) == len(set(anchors)) == 10
    assert links and all((a or b) in anchors for a, b in links)


def run_grouping(different_forms_only):
    from collections import Counter, defaultdict
    namespace = {
        "Counter": Counter, "defaultdict": defaultdict,
        "METHODS": {"Hechrechi": "h", "Gadol": "g"},
        "ONLY_DIFFERENT_FORMS": different_forms_only,
        "occurrences": [
            {"node": 1, "text": "א", "verse": 1, "values": {"Hechrechi": 1, "Gadol": 1}},
            {"node": 2, "text": "ב", "verse": 2, "values": {"Hechrechi": 1, "Gadol": 2}},
            {"node": 3, "text": "א", "verse": 3, "values": {"Hechrechi": 1, "Gadol": 1}},
            {"node": 4, "text": "ג", "verse": 3, "values": {"Hechrechi": 3, "Gadol": 3}},
        ],
    }
    source = next("".join(c["source"]) for c in cells()
                  if c["cell_type"] == "code" and "".join(c["source"]).startswith("duplicate_groups = []"))
    exec(compile(source, str(NOTEBOOK), "exec"), namespace)
    return namespace["duplicate_groups"]


def test_duplicates_keep_all_verses_and_separate_methods():
    groups = run_grouping(False)
    assert [(g["method"], g["value"], g["count"], g["verses"]) for g in groups] == [
        ("Hechrechi", 1, 3, [1, 2, 3]), ("Gadol", 1, 2, [1, 3])]
    assert groups[0]["nodes"] == [1, 2, 3]
    assert groups[0]["forms"] == {"א": 2, "ב": 1}


def test_different_form_policy_excludes_repeated_spellings_only():
    groups = run_grouping(True)
    assert len(groups) == 1
    assert groups[0]["method"] == "Hechrechi" and groups[0]["verses"] == [1, 2, 3]
