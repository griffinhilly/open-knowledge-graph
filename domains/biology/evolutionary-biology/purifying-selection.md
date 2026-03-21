---
id: purifying-selection
title: Purifying Selection and Deleterious Mutation Removal
domain: biology
course: evolutionary-biology
prerequisites:
- id: natural-selection
  type: hard
- id: selection-coefficient
  type: hard
- id: population-genetics-intro
  type: soft
builds-toward:
- mutation-selection-balance
- efficacy-selection-finite-populations
tags:
- selection
- constraint
- molecular-evolution
- fitness
stage: advanced
status: draft
---

# Purifying Selection and Deleterious Mutation Removal

## Core Idea
Purifying selection removes or reduces frequency of deleterious mutations by eliminating individuals carrying them. Explains why functional regions of genomes evolve slowly compared to neutral sites.

## Questions

```yaml
- question: "A comparative genomics study finds that the active site of an enzyme evolves 15x more slowly than nearby intergenic DNA across 50 mammalian species. The most parsimonious explanation is:"
  type: multiple-choice
  options:
    - "The active site is under strong positive selection, with beneficial mutations being fixed faster than in non-coding regions"
    - "The active site has an intrinsically lower mutation rate than intergenic DNA due to its GC content"
    - "The active site is under purifying selection — most mutations there are deleterious and are removed before they can accumulate, while intergenic DNA accumulates mutations freely"
    - "The active site is evolving neutrally, but constrained by structural requirements that happen to match ancestral sequence"
  answer: 2
  explanation: "Slow evolution relative to neutral sites (like intergenic DNA) is the signature of purifying selection, not positive selection. Positive selection would accelerate substitution rates, not decelerate them. The logic is: if an enzyme's active site performs a critical function, most amino acid changes will disrupt that function, reducing fitness. Those mutations are eliminated before they can accumulate in the population. By contrast, intergenic DNA can accumulate mutations freely because most changes have no fitness consequence. Option B is tempting but wrong: mutation rates do vary by sequence context, but a 15x difference in *substitution* rate across 50 species reflects selection against fixation, not reduced mutation."

- question: "A mildly deleterious mutation (selection coefficient s = −0.001) arises in a small island population of 40 individuals. Compared to a large mainland population of 200,000 individuals, what is most likely to happen to this mutation?"
  type: multiple-choice
  options:
    - "The mutation will be eliminated faster in the small population because natural selection is more efficient with fewer competing alleles"
    - "The mutation's fate is essentially identical in both populations since the selection coefficient is the same"
    - "In the small population, genetic drift may overpower weak purifying selection, allowing the mutation to drift to fixation; in the large population, purifying selection efficiently removes it"
    - "The mutation will reach higher frequency in the large population due to mutation-selection balance dynamics"
  answer: 2
  explanation: "Whether selection or drift dominates depends on the product Nes (effective population size × selection coefficient). When Nes >> 1, selection is efficient; when Nes << 1, drift dominates. For N=40 and s=0.001: Nes ≈ 0.04 — drift is ~25x stronger than selection, and the mutation is likely to drift to fixation or loss by chance. For N=200,000 and s=0.001: Nes ≈ 200 — selection strongly dominates, and the mutation is efficiently purged. This interaction between drift and purifying selection explains why small, isolated populations accumulate more deleterious mutations over time — a process called Muller's ratchet."

- question: "Purifying selection and positive selection can act simultaneously on different sites within the same gene — some positions are under strong constraint against change while others are favored for adaptive divergence."
  type: true-false
  answer: true
  explanation: "This is routinely observed in comparative genomics. A classic example is immune genes like MHC: the antigen-binding groove shows elevated nonsynonymous substitution rates (positive selection for diversity), while the structural scaffold of the protein shows strong conservation (purifying selection against structural disruption). Another example: viral surface proteins often show positive selection at antibody-binding sites and purifying selection at sites critical for receptor binding. The dN/dS ratio, calculated separately for different codons, can detect both signatures simultaneously, which is why this ratio varies substantially across sites within a single gene."

- question: "Evolutionary conservation of a DNA sequence is direct evidence that the sequence has been positively selected for beneficial functions."
  type: true-false
  answer: false
  explanation: "Conservation indicates purifying selection AGAINST deleterious changes, not positive selection FOR beneficial ones. A conserved sequence is one where mutations are removed because they reduce fitness — the sequence works, and changes break it. Positive selection, by contrast, drives the accumulation of new beneficial variants, which typically increases divergence rates rather than decreasing them. While it is true that conserved sequences are usually functionally important (which is why mutations there are deleterious), functional importance is the underlying reason for conservation, not a form of positive selection. Confusing conservation with positive selection is a common error in genomics interpretation."

- question: "Why do third codon positions evolve faster than first and second codon positions, and what does this difference reveal about purifying selection?"
  type: short-answer
  answer: "The genetic code is redundant — multiple codons encode the same amino acid. Most synonymous substitutions (those that don't change the amino acid) occur at third positions due to wobble. Because these changes are often phenotypically neutral, purifying selection does not efficiently remove them, and they accumulate at rates approaching the neutral mutation rate. First and second codon positions more frequently produce nonsynonymous changes (amino acid substitutions), which are more likely to disrupt protein structure or function. Purifying selection removes these at higher rates, so they evolve more slowly. The ratio dN/dS < 1 for most genes is direct evidence of this: nonsynonymous changes are eliminated faster than synonymous ones."
  explanation: "This codon position rate difference is one of the strongest pieces of evidence for the pervasiveness of purifying selection at the molecular level. It also validates a key prediction of neutral theory: sequences evolve at rates proportional to how much of their variation is selectively neutral. The practical implication is that synonymous substitution rates serve as a molecular clock approximation while nonsynonymous rates reflect the balance of drift and selection on protein-coding sequences."
```

## Explainer

You already know from your study of natural selection that individuals with higher fitness leave more offspring, and from the selection coefficient that the magnitude of a fitness difference determines how quickly allele frequencies change. **Purifying selection** (also called **negative selection**) is the most pervasive form of natural selection in molecular evolution, but it works by removing rather than promoting — it eliminates harmful mutations before they can spread.

Consider a protein that performs an essential function, like hemoglobin carrying oxygen. Most random amino acid changes to this protein will disrupt its structure or function, reducing the organism's fitness. When such a **deleterious mutation** arises, individuals carrying it tend to survive less well or reproduce less successfully than those with the functional version. Over generations, the mutant allele is driven to low frequency or eliminated entirely. This is purifying selection in action: not favoring a new beneficial variant, but policing against damage to something that already works.

The signature of purifying selection is **evolutionary constraint** — functional sequences evolve more slowly than expected under neutrality. Compare the substitution rate of a critical enzyme's active site to a nearby stretch of junk DNA: the junk DNA accumulates mutations freely because changes there have no fitness consequence, while the active site remains nearly frozen across millions of years because almost every mutation there is deleterious and gets removed. The strength of purifying selection is quantified by the selection coefficient (s): a mutation with s = −0.01 reduces fitness by 1%, which in a large population is more than enough for selection to efficiently eliminate it. However, in small populations, drift can overpower weak purifying selection, allowing mildly deleterious mutations to drift to fixation — a critical interaction between drift and selection that shapes genome evolution.

Purifying selection explains several major patterns in comparative genomics. Protein-coding genes evolve slower than intergenic regions. First and second codon positions (which usually change the amino acid) evolve slower than third positions (which often don't). Regulatory elements critical for gene expression are conserved across species separated by hundreds of millions of years. Whenever you see a stretch of DNA that is more conserved than its surroundings, purifying selection is the most likely explanation — the sequence is doing something important, and mutations that break it are being culled. This logic underlies one of the most powerful tools in genomics: identifying functional elements by their evolutionary conservation.
