# Gematria for the Hebrew Bible

<p class="lead">Explore the numerical values of biblical Hebrew and Aramaic words, with every result connected to its text in BHSA.</p>

**gematria_TF** is a ready-made [Text-Fabric](https://annotation.github.io/text-fabric/tf/) dataset. It adds gematria values to the existing word nodes of the [ETCBC BHSA](https://etcbc.github.io/bhsa/) Hebrew Bible, so you can study numerical equivalences alongside the text’s vocabulary, morphology, and passages.

<div class="facts" aria-label="Dataset at a glance">
  <div><strong>426,590</strong><span>BHSA word slots</span></div>
  <div><strong>5</strong><span>numerical methods</span></div>
  <div><strong>36</strong><span>Text-Fabric features</span></div>
</div>

<div class="actions">
  <a class="button" href="getting-started.md">Start using the dataset</a>
  <a class="button secondary" href="features.md">Browse the features</a>
</div>

## The same word, different methods

Gematria assigns numerical values to letters. The value of a word depends on the method you choose. This dataset names the method explicitly, rather than treating one number as “the” gematria of a word.

<section class="sample" aria-label="Values of shalom in five methods">
  <div class="sample-heading"><h2>Shalom · “peace”</h2><span class="hebrew" lang="he" dir="rtl">שלום</span></div>
  <dl class="sample-values">
    <div><dt>Hechrechi</dt><dd>376</dd></div>
    <div><dt>Gadol</dt><dd>936</dd></div>
    <div><dt>Sidduri</dt><dd>52</dd></div>
    <div><dt>Katan</dt><dd>16</dd></div>
    <div><dt>Katan Mispari</dt><dd>7</dd></div>
  </dl>
</section>

[Read how each method works](methods.md), including the treatment of final letters and reduced values.

## Choose the text you want to compare

The dataset keeps **the text representation** separate from **the numerical method**.

Representation | What it measures | Useful for
---|---|---
Lexeme | The dictionary form recorded by BHSA | Comparing vocabulary independently of its inflection
Word | The consonants of an individual BHSA word slot | Studying the form that occurs in a passage
Full form | Adjacent slots that make up a written word under the documented grouping rule | Including attached prefixes and suffix letters already in the text

For example, BHSA divides <span lang="he" dir="rtl">בראשית</span> into two slots: <span lang="he" dir="rtl">ב</span> and <span lang="he" dir="rtl">ראשית</span>. Their standard values are **2** and **911**; the full form is **913**. [See worked examples](examples.md).

## What is included?

The published files contain **25 numerical features** and **11 supporting features**: the five methods applied to lexemes, wordforms, and full forms, with separate **ketiv** (written) and **qere** (recorded reading) values where relevant. Lexemes are shared between readings.

Both Biblical Hebrew and Aramaic are included. The base is **BHSA 2021**, verified as the latest upstream data version on 1 October 2026. The exact source snapshot is recorded for reproducibility. These files extend BHSA; they do not replace it.

<div class="note"><p><strong>Interpreting results.</strong> Full-form values repeat on each constituent slot, so count each group once. One malformed qere in the source is flagged as unavailable; its ketiv value remains present. The <a href="representations.md">representation guide</a> explains both cases.</p></div>

## Further reading

- [Getting started](getting-started.md): obtain the files and load them in Text-Fabric.
- [Methods and conventions](methods.md): understand what each number means.
- [Technical reference](technical.md): feature catalogue, representation specification, source audit, and validation.
- [Sources and citation](sources.md): acknowledge BHSA and the scholarly and software references.
- [Licenses](legal.md): terms for using the data, code, and documentation.

Try the [Genesis 1 duplicate-gematria notebook](../genesis1_duplicate_gematria.ipynb) to find matching word values and the verses containing them, using Hechrechi and Gadol.
