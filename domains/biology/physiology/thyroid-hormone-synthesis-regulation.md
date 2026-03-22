---
id: thyroid-hormone-synthesis-regulation
title: Thyroid Hormone Synthesis and Regulation
domain: biology
course: physiology
prerequisites:
- id: endocrine-system-overview
  type: hard
- id: hypothalamus-pituitary-axis
  type: hard
tags:
- thyroid-hormone
- tsh
- iodine
stage: advanced
status: draft
---

# Thyroid Hormone Synthesis and Regulation

## Core Idea
The thyroid synthesizes thyroid hormones T3 (triiodothyronine) and T4 (thyroxine) from iodine and the amino acid tyrosine through tyrosyl iodination and coupling reactions, with production regulated by TSH from the anterior pituitary. Thyroid hormones increase metabolic rate and are essential for normal growth, development, and thermoregulation.

## Questions

```yaml
- question: "A patient presents with fatigue, weight gain, cold intolerance, and slow reflexes. Lab results show elevated TSH but low T4. What does the elevated TSH indicate?"
  type: multiple-choice
  options:
    - "The pituitary is malfunctioning and over-releasing TSH despite normal thyroid output"
    - "The thyroid is overactive and TSH is rising in response to excess T4"
    - "The negative feedback loop is intact — the pituitary is increasing TSH to try to stimulate an underperforming thyroid"
    - "TSH elevation is a direct cause of the patient's fatigue, independent of T4 levels"
  answer: 2
  explanation: "Elevated TSH with low T4 is the hallmark of primary hypothyroidism. The negative feedback loop is working correctly: low T4 means insufficient inhibition of the hypothalamus and pituitary, so TSH rises as the pituitary 'pushes harder' on an underperforming gland. TSH is the most sensitive early marker precisely because it amplifies before T4 levels drop dramatically. The elevated TSH is a consequence of low T4, not a cause of symptoms."

- question: "The thyroid gland releases mostly T4 into circulation, even though T3 is far more biologically active. What is the functional significance of this arrangement?"
  type: multiple-choice
  options:
    - "T4 is more stable and easier to synthesize, so the body produces it first and converts as needed"
    - "T4 acts as a circulating reservoir; peripheral tissues use deiodinase enzymes to convert T4 to T3, allowing local fine-tuning of hormone activity"
    - "T4 and T3 bind different receptors, so releasing mostly T4 targets different tissue types"
    - "Releasing inactive T4 prevents thyroid hormones from affecting the pituitary during transport"
  answer: 1
  explanation: "T4 (thyroxine) is relatively inactive and long-lived in circulation, serving as a prohormone reservoir. Peripheral tissues — particularly liver and kidney — express deiodinase enzymes that remove one iodine to convert T4 into the active T3. This gives individual tissues a degree of autonomous control over how much active hormone they receive, independent of what the thyroid is producing. It adds a regulatory layer beyond the central TRH→TSH→T4 axis."

- question: "In Graves disease, where antibodies mimic TSH and chronically stimulate the thyroid, TSH levels are suppressed."
  type: true-false
  answer: true
  explanation: "The negative feedback loop remains intact in Graves disease — the thyroid is being driven not by TSH but by antibodies (TSI) that bind and activate TSH receptors. The resulting excess T3 and T4 inhibit both TRH and TSH through normal feedback, suppressing pituitary TSH release. So in hyperthyroidism from Graves disease, the pattern is: high T4/T3, low TSH. This is the clinical opposite of primary hypothyroidism (low T4/T3, high TSH)."

- question: "T4 is the most potent thyroid hormone because it is the primary form secreted directly by the thyroid gland."
  type: true-false
  answer: false
  explanation: "T3 (triiodothyronine) is the more potent form — it binds thyroid hormone receptors with much higher affinity. T4 is the predominant form secreted by the thyroid (~90% of output), but it functions primarily as a circulating prohormone that peripheral tissues convert to T3 via deiodinases. The fact that T4 is secreted more does not make it more potent; it makes it a reservoir for generating the active hormone where it is needed."

- question: "How does the hypothalamic-pituitary-thyroid negative feedback loop maintain stable thyroid hormone levels, and what happens to TSH when thyroid hormone production falls?"
  type: short-answer
  answer: "The hypothalamus releases TRH, which stimulates the anterior pituitary to secrete TSH, which drives thyroid hormone synthesis and release. Rising T3 and T4 feed back to inhibit both TRH and TSH secretion, reducing stimulation of the gland. When thyroid hormone production falls (e.g., iodine deficiency or gland destruction), the inhibitory feedback weakens, TRH and TSH are released in greater amounts, and TSH rises — attempting to whip the underperforming gland into greater output."
  explanation: "This is a classic closed-loop negative feedback system. TSH is the most sensitive readout because it amplifies small changes: even a modest decline in T4 causes a disproportionate rise in TSH. Clinically, TSH is measured first when thyroid dysfunction is suspected, because it detects subclinical dysfunction before T4 falls outside the normal range."
```

## Explainer

From the endocrine system overview, you know that hormones are chemical signals that regulate distant target cells, and from the hypothalamic-pituitary axis, you understand that the hypothalamus controls many endocrine glands through a two-step relay via the pituitary. Thyroid hormone regulation is one of the clearest examples of this hierarchical control system, and the thyroid gland itself has a unique synthetic mechanism — it is the only endocrine gland that stores large quantities of preformed hormone extracellularly, in a protein-rich colloid within follicles.

The thyroid gland is organized into spherical **follicles**, each lined by a single layer of follicular epithelial cells surrounding a lumen filled with **thyroglobulin** — a large glycoprotein that serves as the scaffold for hormone synthesis. The process begins with **iodide trapping**: the sodium-iodide symporter (NIS) on the basolateral membrane actively concentrates iodide from the blood into follicular cells (to 20–40 times plasma levels). Iodide is then transported across the apical membrane into the colloid, where the enzyme **thyroid peroxidase (TPO)** oxidizes it and attaches it to tyrosine residues on thyroglobulin. A single iodine attachment creates monoiodotyrosine (MIT); a second creates diiodotyrosine (DIT). TPO then couples these iodinated tyrosines: two DIT molecules couple to form **T4 (thyroxine)**, while one MIT and one DIT couple to form **T3 (triiodothyronine)**. The iodinated thyroglobulin remains stored in the colloid — the gland holds weeks' worth of hormone supply.

When thyroid hormones are needed, follicular cells endocytose colloid droplets, fuse them with lysosomes, and proteolyze thyroglobulin to liberate T4 and T3. The gland releases mostly T4 (about 90%), which is relatively inactive — it serves as a circulating reservoir. Peripheral tissues, especially the liver and kidneys, convert T4 to the more potent T3 using **deiodinase enzymes** that remove one iodine atom. This peripheral conversion means that target cells can locally regulate their own thyroid hormone exposure, adding a layer of fine-tuning beyond what the central axis provides.

The entire system is governed by a classic negative feedback loop. The hypothalamus releases **thyrotropin-releasing hormone (TRH)**, which stimulates the anterior pituitary to secrete **thyroid-stimulating hormone (TSH)**. TSH binds receptors on follicular cells and stimulates every step of hormone production — iodide uptake, thyroglobulin synthesis, TPO activity, colloid endocytosis, and hormone release. As circulating T3 and T4 levels rise, they inhibit both TRH and TSH secretion, reducing thyroid stimulation. This feedback keeps thyroid hormone levels remarkably stable. In **hypothyroidism** (insufficient hormone), TSH rises as the pituitary tries to whip an underperforming gland into action — elevated TSH is the most sensitive early marker. In **hyperthyroidism** (excess hormone, as in Graves disease where antibodies mimic TSH), TSH is suppressed because the feedback loop is intact but the gland is being driven by an autonomous stimulus.
