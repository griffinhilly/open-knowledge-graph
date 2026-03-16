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

## Explainer

From Hardy-Weinberg equilibrium, you know that in a single, randomly mating population with allele frequencies *p* and *q*, the expected genotype frequencies are *p²*, *2pq*, and *q²*. The **Wahlund effect** shows what happens when you mistakenly treat a subdivided population as if it were a single unit: you observe fewer heterozygotes than Hardy-Weinberg predicts, even if each subpopulation individually is in perfect equilibrium.

The mathematics behind this are surprisingly simple. Imagine two isolated subpopulations of equal size. In population A, the frequency of allele *A* is 0.8 (so *q* = 0.2), giving an expected heterozygosity of 2(0.8)(0.2) = 0.32. In population B, the frequency of allele *A* is 0.2 (so *q* = 0.8), giving the same heterozygosity of 0.32. Each subpopulation has 32% heterozygotes. Now pool them together. The overall allele frequency is (0.8 + 0.2)/2 = 0.5, and Hardy-Weinberg would predict 2(0.5)(0.5) = 0.50, or 50% heterozygotes. But the actual heterozygosity in the pooled sample is just the average of the two subpopulations: (0.32 + 0.32)/2 = 0.32. The pooled sample shows a **heterozygote deficiency** of 0.18 — not because anything is wrong with mating within each group, but because averaging across groups with different allele frequencies always reduces heterozygosity relative to the overall mean frequency.

This result follows from a basic mathematical property: the **mean of squared values is always greater than or equal to the square of the mean** (Jensen's inequality applied to a convex function). Since homozygote frequencies are squared terms (*p²* and *q²*), pooling populations with different allele frequencies inflates the average homozygote frequency and correspondingly deflates heterozygosity. The more divergent the subpopulations' allele frequencies, the larger the deficit. If all subpopulations have identical allele frequencies, the Wahlund effect disappears entirely.

In practice, the Wahlund effect is both a diagnostic tool and a cautionary tale. When geneticists observe a heterozygote deficiency in a sample, the Wahlund effect is one of the first explanations to consider — alongside inbreeding, assortative mating, or selection against heterozygotes. Distinguishing among these causes requires examining whether the sample was drawn from a structured population. Forensic genetics, conservation biology, and association studies all must account for population substructure to avoid spurious conclusions. The Wahlund effect also connects forward to **F-statistics** and the concept of effective population size: F_ST, which measures genetic differentiation among subpopulations, is essentially a formalization of the Wahlund effect, quantifying how much heterozygosity is lost due to subdivision relative to a hypothetical panmictic population.
