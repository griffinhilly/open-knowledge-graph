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
- id: single-nucleotide-polymorphisms-snps
  type: soft
builds-toward:
- genetic-heterogeneity-locus
tags:
- variant-annotation
- variant-interpretation
- vcf-format
- functional-prediction
- clinical-significance
stage: formal-systems
status: validated
---

# Variant Annotation and Interpretation

## Core Idea
Variant annotation assigns functional consequence to detected variants: whether they cause missense/nonsense changes, affect splicing, disrupt regulatory regions, or create/destroy transcription factor binding sites. Interpretation requires considering population frequency (rare variants more likely pathogenic), computational predictions (PolyPhen, SIFT scores), evolutionary conservation, and segregation in families. The ACMG classification system categorizes variants as pathogenic, likely pathogenic, uncertain significance, likely benign, or benign.

## Questions

```yaml
- question: "A patient with a rare genetic disorder has a missense variant in a disease-relevant gene. The SIFT algorithm predicts the variant is 'damaging' with 95% confidence. A clinician asks whether this variant is pathogenic. What is the correct response?"
  type: multiple-choice
  options:
    - "Yes — SIFT confidently predicts pathogenicity, so the variant should be classified as pathogenic"
    - "Not necessarily — SIFT provides supporting computational evidence but pathogenicity requires integration with population frequency, conservation, functional data, and family segregation"
    - "Yes — a damaging missense variant in a relevant gene is pathogenic by definition under ACMG criteria"
    - "No — computational predictions like SIFT are unreliable and should not be used in clinical interpretation"
  answer: 1
  explanation: "SIFT and PolyPhen-2 provide computational supporting evidence — one line of evidence among many — not standalone pathogenicity determinations. ACMG classification requires weighing population frequency (is the variant common in gnomAD?), evolutionary conservation, experimental functional data, family segregation, and phenotype match, among other criteria. A SIFT 'damaging' call can be provided by perfectly benign variants at positions that happen to be conserved for structural reasons unrelated to the disease. Many SIFT-predicted-damaging variants are found in healthy individuals, confirming they are benign."

- question: "Why does population frequency serve as the most powerful initial filter when interpreting a variant's pathogenicity for a rare Mendelian disease?"
  type: multiple-choice
  options:
    - "Because rare variants undergo stronger purifying selection and are therefore more likely to be harmful"
    - "Because a variant present at high frequency in healthy people cannot be causing a rare disease — disease prevalence logic makes it mathematically impossible"
    - "Because population databases like gnomAD include functional studies of each variant they list"
    - "Because common variants are tagged by GWAS studies, allowing direct disease association testing"
  answer: 1
  explanation: "The logic is straightforward: if a variant causes a rare disease (say, 1 in 100,000 individuals), it cannot be present in 5% of healthy individuals. Rare Mendelian diseases have population frequencies far below 1%, so any variant found at >0.1–1% in gnomAD healthy controls is almost certainly benign — regardless of what computational tools predict. This is why population frequency is the first filter applied and why finding a variant in gnomAD at appreciable frequency is considered strong evidence of benignity (ACMG criterion BA1/BS1)."

- question: "A variant classified as a VUS (variant of uncertain significance) may be reclassified as pathogenic or benign over time as additional evidence accumulates from more cases and functional studies."
  type: true-false
  answer: true
  explanation: "VUS classification reflects current evidence insufficiency, not a permanent property of the variant. As more patients are sequenced, the variant may be observed multiple times in affected individuals with the same phenotype (increasing pathogenicity evidence) or found in healthy individuals (increasing benignity evidence). Functional experiments can demonstrate whether the variant disrupts protein function. The ACMG framework explicitly accommodates reclassification as evidence evolves, and large-scale reclassification projects have moved thousands of VUS to more definitive categories. VUS does not mean 'unknown forever' — it means 'we don't have enough evidence yet.'"

- question: "A de novo variant (not present in either parent) found in a patient with a matching disease phenotype should automatically be classified as pathogenic under ACMG guidelines."
  type: true-false
  answer: false
  explanation: "De novo status in a disease-relevant gene with a matching phenotype is strong evidence for pathogenicity (ACMG criterion PS2), but it does not automatically yield a 'pathogenic' classification. The framework requires integration of multiple lines of evidence using a weighted point system. A de novo missense variant in a gene where only loss-of-function variants cause disease might still be classified as VUS. Additionally, some de novo variants occur by chance in genes that happen to be expressed in the brain without causing the observed phenotype. Automatic classification would skip the critical integration step that protects against misinterpretation."

- question: "Why is a very rare variant not automatically pathogenic, and what additional lines of evidence are required before classifying it as pathogenic?"
  type: short-answer
  answer: "Rarity is necessary but not sufficient for pathogenicity. Most rare variants in the human genome are simply rare neutral variants that never rose to common frequency by chance — the vast majority of sequence differences between individuals are benign. To classify a rare variant as pathogenic, interpreters look for: (1) functional evidence that it disrupts protein activity, splicing, or regulatory function; (2) evolutionary conservation suggesting the position is intolerant of change; (3) prior literature or ClinVar reports linking the same variant or gene to the disease; (4) family segregation showing the variant tracks with disease across generations; and (5) phenotype match confirming the patient's presentation is consistent with variants in this gene."
  explanation: "The ACMG framework assigns weighted criteria across these evidence types — strong, moderate, and supporting — and requires sufficient cumulative evidence before crossing the threshold to 'likely pathogenic' or 'pathogenic.' This system reflects the clinical reality that misclassification has direct consequences: incorrectly labeling a benign variant as pathogenic can lead to unnecessary surveillance, surgeries, or distress, while missing a true pathogenic variant delays diagnosis and treatment."
```

## Explainer

After next-generation sequencing produces a list of millions of positions where a patient's DNA differs from the reference genome, the immediate question is: which of these differences matter? Most variants are benign — common polymorphisms shared across healthy populations. A handful may be clinically significant. **Variant annotation** is the systematic process of attaching biological meaning to each variant, and **variant interpretation** is the reasoning framework that determines whether a variant is likely to cause disease.

Annotation begins by mapping each variant to its genomic context. Using your knowledge of mutation types, you can classify the consequence: does the variant change an amino acid (**missense**), introduce a premature stop codon (**nonsense**), disrupt a splice site, fall in a regulatory region, or land in a non-coding stretch with no obvious function? Tools like Ensembl's Variant Effect Predictor (VEP) or SnpEff automate this step by cross-referencing variant coordinates against gene models. But knowing the consequence category is just the beginning — a missense variant might be perfectly tolerated or devastatingly pathogenic, depending on where it falls in the protein and how it affects structure and function.

To narrow the field, interpreters apply several lines of evidence. **Population frequency** is the first filter: if a variant appears in 5% of healthy individuals in gnomAD, it is almost certainly benign — common variants are too frequent to cause rare Mendelian disease. **Computational prediction tools** like **SIFT** and **PolyPhen-2** estimate whether an amino acid substitution disrupts protein function by analyzing evolutionary conservation and structural properties. A variant at a position conserved across vertebrates for 400 million years is more likely damaging than one at a position that varies freely. **Functional data** — laboratory experiments showing the variant disrupts enzyme activity, protein folding, or splicing — provides the strongest evidence but is not always available.

The **ACMG/AMP classification framework** synthesizes all these lines of evidence into a five-tier system: **pathogenic**, **likely pathogenic**, **variant of uncertain significance (VUS)**, **likely benign**, and **benign**. Each classification uses weighted criteria — for example, a de novo variant in a gene known to cause a matching phenotype counts as strong evidence for pathogenicity, while absence from population databases counts as moderate supporting evidence. The VUS category is clinically challenging: it means the evidence is insufficient to classify the variant in either direction, and the patient's clinician cannot act on it definitively. Over time, as more cases are sequenced and functional studies are performed, many VUS are reclassified — but this process can take years, making variant interpretation an evolving rather than static discipline.
