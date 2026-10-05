"""Write a reproducible stratified audit of 100 BHSA word slots.

Run from the repository root: python scripts/audit_bhsa.py
"""
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gematria_tf.bhsa import load_source
from gematria_tf.normalization import normalize
from gematria_tf.representations import qere_errors, read_words, represent


def main():
    api, lock = load_source()
    words = read_words(api)
    ketiv, kstart, kend = represent(words, "ketiv")
    qere, qstart, qend = represent(words, "qere", invalid_qere="omit")
    errors = qere_errors(words)
    categories = {
        "opening": lambda w: w.node <= 12,
        "prefix_group": lambda w: kstart[w.node] != kend[w.node],
        "suffix": lambda w: bool(api.F.g_prs_utf8.v(w.node)),
        "qere": lambda w: w.qere is not None,
        "qere_boundary": lambda w: w.qere_trailer is not None and w.qere_trailer != w.trailer,
        "aramaic": lambda w: w.language == "arc",
        "maqaf": lambda w: "־" in w.trailer,
        "empty_surface": lambda w: not ketiv["word"][w.node],
        "final_letter": lambda w: any(c in "ךםןףץ" for c in ketiv["word"][w.node]),
        "inflection": lambda w: ketiv["lexeme"][w.node] != ketiv["word"][w.node],
        "invalid_qere": lambda w: w.node in errors,
    }
    selected = {}
    category_counts = {}
    for category, predicate in categories.items():
        matches = [w for w in words if predicate(w)]
        category_counts[category] = len(matches)
        for word in matches[:10]:
            selected.setdefault(word.node, []).append(category)
    # Some strata overlap; fill deterministically with evenly spaced corpus nodes.
    for word in words[::max(1, len(words) // 100)]:
        if len(selected) >= 100:
            break
        selected.setdefault(word.node, []).append("corpus_spread")
    rows = []
    for word in words:
        if word.node not in selected:
            continue
        n = word.node
        rows.append(dict(node=n, section=api.T.sectionFromNode(n), categories=selected[n],
                         language=word.language, lexeme=ketiv["lexeme"][n],
                         word_ketiv=ketiv["word"][n], full_ketiv=ketiv["full"][n],
                         ketiv_group=[kstart[n], kend[n]], word_qere=qere["word"][n],
                         full_qere=qere["full"][n], qere_group=[qstart[n], qend[n]],
                         raw_suffix=api.F.g_prs_utf8.v(n), trailer=word.trailer,
                         qere=word.qere, qere_trailer=word.qere_trailer))
    result = dict(source=lock, wordCount=len(words), languages=dict(Counter(w.language for w in words)),
                  qereEntries=sum(w.qere is not None for w in words),
                  emptyQereEntries=sum(w.qere == "" for w in words),
                  qereErrors=errors,
                  pointedConsonantMismatches=sum(normalize(api.F.g_word_utf8.v(w.node)) != ketiv["word"][w.node] for w in words),
                  categories=category_counts, sampleCount=len(rows), examples=rows)
    path = Path("docs/bhsa-audit.json")
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("source", "examples")}))


if __name__ == "__main__":
    main()
