---
id: wahlund-effect
title: Wahlund Effect and Population Substructure
domain: biology
course: evolutionary-biology
prerequisites:
- id: population-genetics-intro
  type: hard
- id: hardy-weinberg-equilibrium
  type: hard
- id: gene-flow
  type: hard
builds-toward:
- effective-population-size
- coalescent-theory
tags:
- population-structure
- heterozygosity
- subpopulations
stage: advanced
status: draft
---

# Wahlund Effect and Population Substructure

## Core Idea
Subdivided populations show reduced heterozygosity compared to Hardy-Weinberg prediction due to allele frequency variation among subpopulations. This heterozygote deficiency increases with population subdivision and isolation.

## Questions

```yaml
- question: "A population geneticist samples 1,000 individuals from a large geographic region and finds a significant heterozygote deficiency relative to Hardy-Weinberg expectations. The most common explanation a student offers is inbreeding within the population. What alternative explanation should the geneticist consider first?"
  type: multiple-choice
  options:
    - "Selection against heterozygotes, since this is the most common cause of heterozygote deficiency"
    - "The Wahlund effect — the sample may have been drawn from multiple subpopulations with different allele frequencies, and pooling them produces apparent heterozygote deficiency even if each subpopulation is individually in HWE"
    - "Genetic drift in a small founder population that colonized the region recently"
    - "Assortative mating based on genotype, which is common in most species"
  answer: 1
  explanation: "When a heterozygote deficiency is observed in a large sample drawn from a broad geographic area, the Wahlund effect is one of the first explanations to consider — often before inbreeding. If the sample unknowingly pools individuals from multiple subpopulations with different allele frequencies, the pooled sample will always show a heterozygote deficit relative to what you'd predict from the overall allele frequency, even if random mating occurs within each subpopulation. This is a mathematical consequence of population structure, not a biological process occurring within individuals. Distinguishing Wahlund effect from inbreeding requires examining whether the sample is geographically or genetically structured."

- question: "Two isolated subpopulations are combined into a single sample for a population genetics study. In subpopulation X, the frequency of allele A is 0.9. In subpopulation Y, the frequency of allele A is 0.1. Both populations are in Hardy-Weinberg equilibrium. What will happen when their genotype data are pooled?"
  type: multiple-choice
  options:
    - "The pooled sample will also be in HWE, since both source populations are in HWE"
    - "The pooled sample will show excess heterozygotes, since crossing divergent populations produces hybrid vigor"
    - "The pooled sample will show a heterozygote deficiency — fewer heterozygotes than predicted by HWE given the pooled allele frequency of 0.5"
    - "The pooled sample will show no deviation from HWE because the allele frequency differences cancel out"
  answer: 2
  explanation: "HWE within each subpopulation does not guarantee HWE in the pooled sample. In subpopulation X (p=0.9), expected heterozygosity = 2(0.9)(0.1) = 0.18. In subpopulation Y (p=0.1), expected heterozygosity = 2(0.1)(0.9) = 0.18. The actual heterozygosity in the pooled sample averages to 0.18. But the pooled allele frequency is 0.5, and HWE would predict 2(0.5)(0.5) = 0.50 heterozygotes. Observed = 0.18, predicted = 0.50 — a dramatic heterozygote deficiency. The more divergent the allele frequencies between subpopulations, the larger the Wahlund deficit."

- question: "If a population sample shows a heterozygote deficiency compared to Hardy-Weinberg prediction, this is sufficient evidence that mating within the sampled population is non-random."
  type: true-false
  answer: false
  explanation: "This is the classic Wahlund effect misconception. Heterozygote deficiency can arise from non-random mating (inbreeding, assortative mating), selection against heterozygotes, or the Wahlund effect — pooling of subpopulations with different allele frequencies. The Wahlund effect requires no departure from random mating within any subpopulation; it is a statistical artifact of treating a structured sample as a single unit. A forensic geneticist, conservation biologist, or medical association study researcher who ignores the Wahlund effect and assumes any heterozygote deficiency indicates inbreeding will draw incorrect conclusions."

- question: "Two subpopulations can each individually satisfy Hardy-Weinberg equilibrium while the pooled sample from both subpopulations shows a heterozygote deficiency."
  type: true-false
  answer: true
  explanation: "This is the core mathematical claim of the Wahlund effect. HWE within a population requires only that allele frequencies predict genotype frequencies through random mating within that population — it says nothing about what happens when you mix two populations with different allele frequencies. The heterozygote deficiency in the pooled sample is a consequence of Jensen's inequality: when you average across groups with different allele frequencies, the mean of the squared (homozygote) terms exceeds the square of the mean allele frequency, leaving less 'room' for heterozygotes. Each subpopulation can be in perfect HWE while the pooled sample shows a substantial deficit."

- question: "Explain why pooling two populations with different allele frequencies always produces fewer heterozygotes in the pooled sample than Hardy-Weinberg predicts, even when each population individually is in perfect Hardy-Weinberg equilibrium."
  type: short-answer
  answer: "HWE predicts heterozygote frequency as 2pq, where p and q are the overall allele frequencies in the pooled sample. But the actual heterozygote frequency in the pooled sample is the average of heterozygote frequencies within each subpopulation — each calculated using that subpopulation's local allele frequencies. Because heterozygosity (2pq) is a concave function of allele frequency, the average of local heterozygosities is always less than the heterozygosity you'd predict from the average allele frequency. Mathematically, variance in allele frequencies among subpopulations directly reduces observed heterozygosity. The more divergent the subpopulations' allele frequencies, the larger the deficit."
  explanation: "This result follows from Jensen's inequality applied to the concave 2pq function. It means that any time you see a heterozygote deficiency in a geographically broad sample, population substructure (Wahlund effect) must be considered alongside inbreeding and selection. F_ST — the standard measure of population differentiation — is essentially a formalization of this variance in allele frequencies, quantifying how much heterozygosity is lost to subdivision."
```

## Explainer

From Hardy-Weinberg equilibrium, you know that in a single, randomly mating population with allele frequencies *p* and *q*, the expected genotype frequencies are *p²*, *2pq*, and *q²*. The **Wahlund effect** shows what happens when you mistakenly treat a subdivided population as if it were a single unit: you observe fewer heterozygotes than Hardy-Weinberg predicts, even if each subpopulation individually is in perfect equilibrium.

The mathematics behind this are surprisingly simple. Imagine two isolated subpopulations of equal size. In population A, the frequency of allele *A* is 0.8 (so *q* = 0.2), giving an expected heterozygosity of 2(0.8)(0.2) = 0.32. In population B, the frequency of allele *A* is 0.2 (so *q* = 0.8), giving the same heterozygosity of 0.32. Each subpopulation has 32% heterozygotes. Now pool them together. The overall allele frequency is (0.8 + 0.2)/2 = 0.5, and Hardy-Weinberg would predict 2(0.5)(0.5) = 0.50, or 50% heterozygotes. But the actual heterozygosity in the pooled sample is just the average of the two subpopulations: (0.32 + 0.32)/2 = 0.32. The pooled sample shows a **heterozygote deficiency** of 0.18 — not because anything is wrong with mating within each group, but because averaging across groups with different allele frequencies always reduces heterozygosity relative to the overall mean frequency.

This result follows from a basic mathematical property: the **mean of squared values is always greater than or equal to the square of the mean** (Jensen's inequality applied to a convex function). Since homozygote frequencies are squared terms (*p²* and *q²*), pooling populations with different allele frequencies inflates the average homozygote frequency and correspondingly deflates heterozygosity. The more divergent the subpopulations' allele frequencies, the larger the deficit. If all subpopulations have identical allele frequencies, the Wahlund effect disappears entirely.

In practice, the Wahlund effect is both a diagnostic tool and a cautionary tale. When geneticists observe a heterozygote deficiency in a sample, the Wahlund effect is one of the first explanations to consider — alongside inbreeding, assortative mating, or selection against heterozygotes. Distinguishing among these causes requires examining whether the sample was drawn from a structured population. Forensic genetics, conservation biology, and association studies all must account for population substructure to avoid spurious conclusions. The Wahlund effect also connects forward to **F-statistics** and the concept of effective population size: F_ST, which measures genetic differentiation among subpopulations, is essentially a formalization of the Wahlund effect, quantifying how much heterozygosity is lost due to subdivision relative to a hypothetical panmictic population.
