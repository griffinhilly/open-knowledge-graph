---
id: aneuploidy-trisomy-monosomy-mechanisms
title: 'Aneuploidy: Trisomy, Monosomy, and Non-Disjunction'
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: meiosis
  type: hard
- id: chromosomal-aberrations-deletion-duplication
  type: soft
builds-toward:
- polyploidy-autopolyploidy-mechanisms
tags:
- aneuploidy
- trisomy
- monosomy
- non-disjunction
- meiosis
stage: advanced
status: draft
---

# Aneuploidy: Trisomy, Monosomy, and Non-Disjunction

## Core Idea
Aneuploidy (abnormal chromosome number) usually results from non-disjunction—failure of homologous chromosomes or sister chromatids to separate properly during meiosis I or II. Trisomy (three copies of a chromosome, e.g., Down syndrome/trisomy 21) and monosomy (one copy, e.g., Turner syndrome/45,X) cause severe gene dosage imbalances. Autosomes tolerate few aneuploidies; sex chromosomes tolerate more.

## How It's Best Learned
Diagram meiosis with non-disjunction in meiosis I and II, showing which gametes are unbalanced. Relate aneuploidy frequency to maternal age (increased in meiosis I due to age-related checkpoint failure). Consider why trisomy-21 is viable while trisomy of most other autosomes is lethal.

## Common Misconceptions
- Assuming all aneuploidies are viable; most autosomal aneuploidies (except 13, 18, 21) are embryonic lethal.
- Not recognizing the relationship between maternal age and non-disjunction in meiosis I.
- Thinking aneuploidy always causes severe phenotypes; some sex chromosome aneuploidies (e.g., 47,XXY) have minimal effects.

## Questions

```yaml
- question: "Non-disjunction occurs during meiosis I in an oocyte. How many of the four resulting gametes will have an abnormal chromosome number?"
  type: multiple-choice
  options:
    - "One — only the gamete that received the extra chromosome is abnormal"
    - "Two — one gamete gains a chromosome and one loses it"
    - "All four — meiosis I non-disjunction affects the entire gamete pool because it occurs before meiosis II"
    - "It depends on whether the non-disjunction affects a large or small chromosome"
  answer: 2
  explanation: "Meiosis I non-disjunction means both homologs of a chromosome pair move to the same pole rather than separating. After meiosis I, one secondary oocyte/spermatocyte has two copies of the chromosome and the other has zero. When each of these then undergoes meiosis II (which separates sister chromatids), the cell with two copies produces two gametes each with an extra chromosome, and the cell with zero copies produces two gametes each missing the chromosome. All four final gametes are abnormal. This contrasts with meiosis II non-disjunction, where only the one cell that fails to separate its sister chromatids produces two abnormal gametes — leaving the other two gametes normal."

- question: "Why are sex chromosome aneuploidies (e.g., XXY, 45,X) generally much better tolerated than autosomal aneuploidies of comparable chromosome size?"
  type: multiple-choice
  options:
    - "Because sex chromosomes are smaller than most autosomes and therefore carry fewer genes"
    - "Because X-inactivation silences extra X chromosomes, minimizing gene dosage imbalance, while autosomes have no equivalent dosage compensation"
    - "Because sex chromosomes are inherited only from one parent, reducing the conflict between paternal and maternal gene products"
    - "Because the Y chromosome is largely non-functional and its presence or absence has minimal effect on protein dosage"
  answer: 1
  explanation: "X-inactivation is the key mechanism. In mammals, one X chromosome in each somatic cell is randomly inactivated to equalize expression between XX females and XY males. This pre-existing dosage compensation means that in an XXY individual, one X is inactivated just as in a typical female, so dosage of most X-linked genes is essentially normal. Similarly, a 45,X individual has one active X — the same as both typical males and typical females. Autosomes have no such inactivation mechanism, so trisomy of any autosome means roughly 50% overproduction of every protein encoded on that chromosome, disrupting protein stoichiometry and regulatory networks."

- question: "Non-disjunction during meiosis I produces more unbalanced gametes than non-disjunction during meiosis II."
  type: true-false
  answer: true
  explanation: "Meiosis I non-disjunction prevents homologous chromosomes from separating, so the chromosome imbalance is present in both daughter cells after meiosis I. Both of these then undergo meiosis II, producing four gametes that are all abnormal (two with an extra chromosome, two with none). Meiosis II non-disjunction fails to separate sister chromatids in only one of the two meiosis I products, so only two of the four final gametes are abnormal while the other two receive a normal haploid set. This is also why meiosis I errors are more clinically significant: they have twice the impact on the gamete pool."

- question: "Trisomy 21 is compatible with live birth because chromosome 21 is gene-rich and has strong dosage compensation mechanisms similar to X-inactivation."
  type: true-false
  answer: false
  explanation: "This is incorrect. Trisomy 21 is compatible with live birth precisely because chromosome 21 is one of the smallest and most gene-poor of the human autosomes. There is no autosomal dosage compensation equivalent to X-inactivation. The reason some trisomies survive while most do not is simply that the dosage imbalance from a smaller chromosome with fewer genes is less disruptive to overall cellular stoichiometry. Trisomies 13, 18, and 21 are the only autosomal trisomies compatible with live birth — all three involve relatively gene-poor chromosomes — and even trisomies 13 and 18 are usually fatal within the first year."

- question: "Why are sex chromosome aneuploidies generally better tolerated than autosomal aneuploidies, even when involving the same number of extra chromosomes?"
  type: short-answer
  answer: "Because X-inactivation provides pre-existing dosage compensation for X chromosomes. In mammals, one X chromosome per cell is inactivated to equalize X-linked gene expression between XX females and XY males. When an extra X is present (as in XXY or XXX), it is simply inactivated like the second X in a normal female, so the dosage of most X-linked genes remains normal. Autosomes have no equivalent inactivation mechanism — an extra autosome means roughly 50% more expression of every gene on that chromosome, disrupting protein complex stoichiometry and gene regulatory networks throughout the cell."
  explanation: "The tolerance for sex chromosome aneuploidy is a direct consequence of a mechanism that already exists to handle dosage differences between sexes. X-inactivation converts the 'problem' of extra X chromosomes into a state the cell already knows how to manage. Without this pre-existing mechanism (as with autosomes), the cell has no way to buffer the extra gene dosage, and the resulting imbalances in protein complexes and transcription factor networks are typically incompatible with normal development."
```

## Explainer

You already know that meiosis carefully separates homologous chromosomes (in meiosis I) and sister chromatids (in meiosis II) to produce haploid gametes with exactly one copy of each chromosome. **Non-disjunction** is what happens when this separation fails — a pair of chromosomes or chromatids moves to the same pole instead of splitting apart. The result is gametes with the wrong number of chromosomes: one gamete gets an extra copy and the other gets none. When these abnormal gametes fuse with a normal gamete at fertilization, the resulting embryo is **aneuploid** — it has a chromosome number that is not an exact multiple of the haploid set.

The two most common forms of aneuploidy are **trisomy** (2n + 1, three copies of one chromosome) and **monosomy** (2n − 1, only one copy). The consequences depend on which chromosome is affected and whether the error occurred in meiosis I or meiosis II. Non-disjunction in meiosis I is more severe because it affects homologous chromosomes: both members of a pair go to the same daughter cell, so all four resulting gametes are unbalanced — two have an extra chromosome and two are missing one. Non-disjunction in meiosis II affects sister chromatids, so only two of the four gametes are abnormal while the other two are normal. In humans, the frequency of meiosis I errors increases dramatically with maternal age, particularly after age 35, because oocytes arrested in meiosis I for decades accumulate deterioration of the cohesin proteins that hold homologous chromosomes together.

Most autosomal aneuploidies are lethal during embryonic development because they create massive **gene dosage imbalances**. Having three copies of a chromosome means producing roughly 50% more of every protein encoded on that chromosome, which disrupts the stoichiometry of protein complexes and regulatory networks. Only three human autosomal trisomies are compatible with live birth: **trisomy 21** (Down syndrome), **trisomy 18** (Edwards syndrome), and **trisomy 13** (Patau syndrome) — and the latter two are usually fatal within the first year. These particular trisomies survive partly because chromosomes 13, 18, and 21 are among the smallest and most gene-poor human chromosomes, so the dosage imbalance is relatively mild. Autosomal monosomies are almost universally lethal because losing an entire chromosome's worth of gene products is even more disruptive than gaining extra copies.

**Sex chromosome aneuploidies** are far better tolerated, and the reason connects to a mechanism you may encounter later: X-inactivation. In mammals, one X chromosome in each female cell is already silenced to equalize dosage between XX females and XY males. This means an XXY individual (Klinefelter syndrome) inactivates one X just like a typical female, and a 45,X individual (Turner syndrome) has only one active X — the same as both typical males and females. The extra or missing sex chromosome therefore causes relatively subtle phenotypic effects compared to autosomal aneuploidy, though fertility is usually impaired.
