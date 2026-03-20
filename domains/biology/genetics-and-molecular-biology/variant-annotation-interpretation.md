---
id: variant-annotation-interpretation
title: Variant Annotation and Interpretation
domain: biology
course: genetics-and-molecular-biology
prerequisites:
- id: next-generation-sequencing-ngs
  type: hard
- id: missense-nonsense-silent-mutation-effects
  type: hard
builds-toward:
- genetic-heterogeneity-locus
tags:
- variant-annotation
- variant-interpretation
- vcf-format
- functional-prediction
- clinical-significance
stage: advanced
status: draft
---

# Variant Annotation and Interpretation

## Core Idea
Variant annotation assigns functional consequence to detected variants: whether they cause missense/nonsense changes, affect splicing, disrupt regulatory regions, or create/destroy transcription factor binding sites. Interpretation requires considering population frequency (rare variants more likely pathogenic), computational predictions (PolyPhen, SIFT scores), evolutionary conservation, and segregation in families. The ACMG classification system categorizes variants as pathogenic, likely pathogenic, uncertain significance, likely benign, or benign.

## Explainer

After next-generation sequencing produces a list of millions of positions where a patient's DNA differs from the reference genome, the immediate question is: which of these differences matter? Most variants are benign — common polymorphisms shared across healthy populations. A handful may be clinically significant. **Variant annotation** is the systematic process of attaching biological meaning to each variant, and **variant interpretation** is the reasoning framework that determines whether a variant is likely to cause disease.

Annotation begins by mapping each variant to its genomic context. Using your knowledge of mutation types, you can classify the consequence: does the variant change an amino acid (**missense**), introduce a premature stop codon (**nonsense**), disrupt a splice site, fall in a regulatory region, or land in a non-coding stretch with no obvious function? Tools like Ensembl's Variant Effect Predictor (VEP) or SnpEff automate this step by cross-referencing variant coordinates against gene models. But knowing the consequence category is just the beginning — a missense variant might be perfectly tolerated or devastatingly pathogenic, depending on where it falls in the protein and how it affects structure and function.

To narrow the field, interpreters apply several lines of evidence. **Population frequency** is the first filter: if a variant appears in 5% of healthy individuals in gnomAD, it is almost certainly benign — common variants are too frequent to cause rare Mendelian disease. **Computational prediction tools** like **SIFT** and **PolyPhen-2** estimate whether an amino acid substitution disrupts protein function by analyzing evolutionary conservation and structural properties. A variant at a position conserved across vertebrates for 400 million years is more likely damaging than one at a position that varies freely. **Functional data** — laboratory experiments showing the variant disrupts enzyme activity, protein folding, or splicing — provides the strongest evidence but is not always available.

The **ACMG/AMP classification framework** synthesizes all these lines of evidence into a five-tier system: **pathogenic**, **likely pathogenic**, **variant of uncertain significance (VUS)**, **likely benign**, and **benign**. Each classification uses weighted criteria — for example, a de novo variant in a gene known to cause a matching phenotype counts as strong evidence for pathogenicity, while absence from population databases counts as moderate supporting evidence. The VUS category is clinically challenging: it means the evidence is insufficient to classify the variant in either direction, and the patient's clinician cannot act on it definitively. Over time, as more cases are sequenced and functional studies are performed, many VUS are reclassified — but this process can take years, making variant interpretation an evolving rather than static discipline.
