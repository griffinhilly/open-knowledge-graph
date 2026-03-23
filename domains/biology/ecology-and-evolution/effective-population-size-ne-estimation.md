---
id: effective-population-size-ne-estimation
title: Effective Population Size (Ne) and Its Estimation
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-genetics-intro
  type: hard
- id: effective-population-size
  type: hard
- id: genetic-drift-in-small-populations
  type: soft
- id: statistics-rigorous
  type: soft
- id: sampling-distributions
  type: soft
- id: expected-value-theory
  type: soft
- id: probability-mass-functions
  type: soft
builds-toward:
- conservation-genetics-effective-size
- population-viability-analysis
tags:
- effective-population-size
- Ne
- drift
- estimation
stage: formal-systems
status: draft
---

# Effective Population Size (Ne) and Its Estimation

## Core Idea
Effective population size (Ne) is the number of individuals in an idealized population with the same genetic drift rate as the actual population. Ne is typically much smaller than census size (N) due to unequal sex ratios, variation in reproductive success, and fluctuating population size. Ne can be estimated from heterozygosity change, linkage disequilibrium, or molecular data. Ne < 50 risks inbreeding depression; Ne > 500 maintains evolutionary potential.

## Questions

```yaml
- question: "A population of 10,000 individuals crashes to 50 for a single generation due to a disease, then recovers to 10,000. What does the effective population size over this three-generation period most closely reflect?"
  type: multiple-choice
  options:
    - "The arithmetic average census size, approximately 6,683"
    - "The final recovered size, 10,000, since the crash was temporary"
    - "The harmonic mean, dominated by the bottleneck of 50"
    - "The initial size, 10,000, because the crash occurred after drift had already acted"
  answer: 2
  explanation: "Ne across multiple generations is the harmonic mean of per-generation sizes: 3 / (1/10,000 + 1/50 + 1/10,000) ≈ 3 / 0.0201 ≈ 149. The harmonic mean is dominated by the smallest value, so the bottleneck of 50 pulls Ne far below the arithmetic average. A single severe crash leaves a lasting genetic signature — the population loses alleles irreversibly during the bottleneck regardless of how quickly census size recovers afterward."

- question: "A wildlife manager counts 1,010 individuals in a harem-based breeding species. Only 10 males and 1,000 females actually breed each generation. Using Ne ≈ 4·Nm·Nf / (Nm+Nf), what is the approximate effective population size?"
  type: multiple-choice
  options:
    - "Approximately 1,010 — the same as census size, since all individuals are counted"
    - "Approximately 505 — half the census size, by a standard correction factor"
    - "Approximately 40 — dominated by the rare breeding sex"
    - "Approximately 200 — applying the typical Ne/N ratio of 0.2"
  answer: 2
  explanation: "Ne = 4·10·1000/(10+1000) = 40,000/1,010 ≈ 40. The unequal sex ratio formula shows that Ne is largely determined by the rarer breeding sex. With only 10 males contributing genetically, the effective size is close to 4×10 = 40 regardless of the thousand females. Options A and B treat Ne as a simple fraction of N, missing the mechanism: genetic drift is governed by who passes genes to offspring, and when one sex is the bottleneck, that sex's count dominates."

- question: "A species with a large census population size (N) is reliably protected against the genetic risks of inbreeding and loss of adaptive potential."
  type: true-false
  answer: false
  explanation: "Census size N overestimates genetic size whenever sex ratios are unequal, reproductive success varies among individuals, or the population has passed through bottlenecks. A population of 5,000 counted individuals might have an Ne of only 200, placing it below the threshold for maintaining evolutionary potential (Ne > 500 by the 50/500 rule). Conservation decisions based on head counts alone can be dangerously misleading — Ne is the quantity that governs drift, inbreeding, and loss of genetic diversity."

- question: "The linkage disequilibrium (LD) method for estimating Ne works because genetic drift in small populations creates non-random associations between alleles at different loci."
  type: true-false
  answer: true
  explanation: "In an infinitely large population, alleles at separate loci assort independently (linkage equilibrium). In small populations, genetic drift randomly samples gametes, creating associations between alleles at unlinked loci by chance. These non-random associations — linkage disequilibrium — persist and accumulate when Ne is small. By measuring the extent of LD in a single contemporary sample, researchers can infer Ne without needing historical samples. Higher LD implies smaller Ne, giving a window into effective population size from a single time point."

- question: "Explain why Ne is almost always smaller than census size N, and why this distinction matters for conservation biology."
  type: short-answer
  answer: "Ne is smaller than N because the idealized Wright-Fisher model assumes equal sex ratios, equal reproductive success, and constant size — conditions real populations violate. Unequal sex ratios (few breeding males), variance in reproductive success (some individuals produce many offspring), and population size fluctuations (harmonic mean is dominated by bottlenecks) all reduce Ne below N. Conservation matters because Ne governs genetic drift and inbreeding risk. A population with N=5,000 but Ne=200 may be genetically precarious despite appearing large by head count."
  explanation: "The Ne/N ratio commonly ranges from 0.1 to 0.3 in wildlife populations. The three main mechanisms are: (1) unequal sex ratio — Ne ≈ 4NmNf/(Nm+Nf), heavily influenced by the rarer breeding sex; (2) variance in reproductive success — when some individuals contribute many offspring and others none, drift is stronger than in equal-contribution populations; (3) bottlenecks — the harmonic mean formula means a single severe crash drives Ne toward that minimum. For conservation, the 50/500 rule uses Ne thresholds (not N) to assess inbreeding risk and evolutionary potential, making Ne estimation central to population viability analysis."
```

## Explainer

From population genetics, you know that genetic drift — random fluctuations in allele frequencies — is stronger in small populations, leading to loss of genetic variation and increased homozygosity. You also know the basic concept of effective population size. This topic takes that concept further: how do we actually **estimate** Ne from real-world data, and why does the estimate matter so much for conservation and evolutionary biology?

The key insight is that census population size (N) — the number of individuals you can count — almost always overestimates the genetic "size" of a population. **Effective population size (Ne)** asks: if we replaced this real, messy population with an idealized Wright-Fisher population (random mating, equal sex ratio, constant size, non-overlapping generations), how large would that idealized population need to be to experience the same rate of genetic drift? The answer is almost always smaller than N, often dramatically so. In many wildlife populations, Ne/N ratios range from 0.1 to 0.3, meaning the genetic effective size is only 10–30% of the census count. A population of 1,000 elephants might have an Ne of only 100–200.

Three main factors reduce Ne below N. First, **unequal sex ratio**: if only a few males breed (as in elephant seal harems), the effective size is dominated by the rarer breeding sex. The formula Ne = 4·Nm·Nf/(Nm + Nf) shows that when 10 males and 1,000 females breed, Ne ≈ 40 — far below the 1,010 census count. Second, **variance in reproductive success**: if some individuals produce many offspring while others produce none, drift is stronger than in a population where everyone contributes equally. Third, **fluctuating population size**: Ne is dominated by the smallest size the population passes through, calculated as the harmonic mean across generations. A population that crashes to 50 individuals for one generation and then recovers to 10,000 will have an Ne much closer to 50 than to 10,000 — the **bottleneck** leaves a lasting genetic signature.

Estimating Ne from data uses several approaches. The **temporal method** compares allele frequencies at the same loci across two or more time points; larger shifts imply smaller Ne. The **linkage disequilibrium method** measures non-random associations between alleles at different loci in a single sample — in small populations, drift creates more LD, so higher LD implies lower Ne. **Coalescent-based methods** use DNA sequence data to infer how quickly lineages merge backward in time, estimating long-term Ne from patterns of genetic diversity. Each method has assumptions and biases, and researchers often use multiple approaches to triangulate.

Why does this matter? Conservation biologists use Ne thresholds as management targets. The **50/500 rule** (now often revised to 100/1,000) suggests that Ne below 50 puts a population at immediate risk of **inbreeding depression** — reduced fitness from homozygosity of deleterious recessive alleles — while Ne above 500 is needed to maintain enough genetic variation for long-term evolutionary adaptation. When a conservation program reports a species has 5,000 individuals remaining, that sounds reassuring — but if Ne is only 200, the population is genetically precarious. Estimating Ne transforms conservation from a head-counting exercise into a genetically informed assessment of population viability.
