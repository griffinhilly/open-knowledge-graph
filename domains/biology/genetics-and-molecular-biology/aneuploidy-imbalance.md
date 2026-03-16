---
id: aneuploidy-imbalance
title: Aneuploidy and Chromosomal Imbalance
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: meiosis
  type: hard
- id: cell-cycle-overview
  type: hard
builds-toward:
- haploinsufficiency-dosage
tags:
- aneuploidy
- monosomy
- trisomy
- chromosomal-imbalance
- gene-dosage
stage: formal-systems
status: draft
---

# Aneuploidy and Chromosomal Imbalance

## Core Idea
Aneuploidy is abnormal chromosome number resulting from nondisjunction during meiosis or mitosis. Monosomy (loss of one chromosome) is usually lethal except for sex chromosomes; trisomy is often viable but causes imbalance in dosage-sensitive genes. Autosomal trisomies (like trisomy 21/Down syndrome) cause widespread developmental abnormalities due to ~50% increase in expression of ~300 genes. Aneuploidies become increasingly common with maternal age, particularly meiosis I nondisjunction.

## Explainer

From your study of meiosis, you know that homologous chromosomes pair up and then separate into daughter cells during meiosis I, and sister chromatids separate during meiosis II. **Nondisjunction** occurs when this separation fails — either homologs fail to separate in meiosis I or sister chromatids fail to separate in meiosis II. The result is gametes with one too many or one too few chromosomes. When such a gamete is fertilized by a normal gamete, the resulting embryo has an abnormal chromosome count: **trisomy** (three copies of a chromosome, 2n+1) or **monosomy** (one copy, 2n−1). Unlike polyploidy, where the entire genome is multiplied proportionally, aneuploidy disrupts the *ratio* of gene products between chromosomes, and it is this imbalance that causes harm.

Why is dosage imbalance so damaging? Consider that cells have evolved to function with precisely two copies of each autosomal gene. Many gene products participate in multi-protein complexes, signaling pathways, or regulatory networks where the relative amounts matter. In trisomy 21 (Down syndrome), the extra copy of chromosome 21 leads to roughly 50% more of every protein encoded on that chromosome — around 300 genes. Some of these proteins are components of dosage-sensitive pathways: transcription factors, adhesion molecules, and enzymes whose overexpression disrupts the balance of developmental programs. The phenotype is not caused by any single gene but by the cumulative effect of many genes being slightly overexpressed simultaneously, which is why trisomy produces a syndrome of many features rather than a single defect.

**Monosomy** is generally more severe than trisomy because losing 50% of a gene's output is often more disruptive than gaining 50%. Most autosomal monosomies in humans are lethal before implantation. The major exception is the X chromosome: females with Turner syndrome (45,X) are viable because of **X-inactivation** — the mechanism that normally silences one X in XX females means that having only one functional X is survivable, though not without consequences. Similarly, sex chromosome trisomies (XXX, XXY, XYY) tend to be milder than autosomal trisomies because the extra X is largely inactivated, limiting dosage imbalance.

The increasing incidence of aneuploidy with **maternal age** is one of the most clinically significant aspects of this topic. The risk of trisomy 21 rises from about 1 in 1,250 at maternal age 25 to 1 in 100 at age 40. The primary cause is age-related degradation of the cohesin proteins that hold homologous chromosomes together during the extended prophase I arrest of oocytes. Human oocytes begin meiosis I before birth and remain arrested for decades — cohesin deteriorates over this time, leading to premature separation of homologs and an increased rate of nondisjunction. This explains why nondisjunction at meiosis I accounts for the majority of age-related aneuploidies and why paternal age has a much smaller effect (spermatocytes do not experience decades-long arrest).
