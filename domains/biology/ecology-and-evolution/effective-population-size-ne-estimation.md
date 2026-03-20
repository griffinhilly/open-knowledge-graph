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
stage: advanced
status: draft
---

# Effective Population Size (Ne) and Its Estimation

## Core Idea
Effective population size (Ne) is the number of individuals in an idealized population with the same genetic drift rate as the actual population. Ne is typically much smaller than census size (N) due to unequal sex ratios, variation in reproductive success, and fluctuating population size. Ne can be estimated from heterozygosity change, linkage disequilibrium, or molecular data. Ne < 50 risks inbreeding depression; Ne > 500 maintains evolutionary potential.

## Explainer

From population genetics, you know that genetic drift — random fluctuations in allele frequencies — is stronger in small populations, leading to loss of genetic variation and increased homozygosity. You also know the basic concept of effective population size. This topic takes that concept further: how do we actually **estimate** Ne from real-world data, and why does the estimate matter so much for conservation and evolutionary biology?

The key insight is that census population size (N) — the number of individuals you can count — almost always overestimates the genetic "size" of a population. **Effective population size (Ne)** asks: if we replaced this real, messy population with an idealized Wright-Fisher population (random mating, equal sex ratio, constant size, non-overlapping generations), how large would that idealized population need to be to experience the same rate of genetic drift? The answer is almost always smaller than N, often dramatically so. In many wildlife populations, Ne/N ratios range from 0.1 to 0.3, meaning the genetic effective size is only 10–30% of the census count. A population of 1,000 elephants might have an Ne of only 100–200.

Three main factors reduce Ne below N. First, **unequal sex ratio**: if only a few males breed (as in elephant seal harems), the effective size is dominated by the rarer breeding sex. The formula Ne = 4·Nm·Nf/(Nm + Nf) shows that when 10 males and 1,000 females breed, Ne ≈ 40 — far below the 1,010 census count. Second, **variance in reproductive success**: if some individuals produce many offspring while others produce none, drift is stronger than in a population where everyone contributes equally. Third, **fluctuating population size**: Ne is dominated by the smallest size the population passes through, calculated as the harmonic mean across generations. A population that crashes to 50 individuals for one generation and then recovers to 10,000 will have an Ne much closer to 50 than to 10,000 — the **bottleneck** leaves a lasting genetic signature.

Estimating Ne from data uses several approaches. The **temporal method** compares allele frequencies at the same loci across two or more time points; larger shifts imply smaller Ne. The **linkage disequilibrium method** measures non-random associations between alleles at different loci in a single sample — in small populations, drift creates more LD, so higher LD implies lower Ne. **Coalescent-based methods** use DNA sequence data to infer how quickly lineages merge backward in time, estimating long-term Ne from patterns of genetic diversity. Each method has assumptions and biases, and researchers often use multiple approaches to triangulate.

Why does this matter? Conservation biologists use Ne thresholds as management targets. The **50/500 rule** (now often revised to 100/1,000) suggests that Ne below 50 puts a population at immediate risk of **inbreeding depression** — reduced fitness from homozygosity of deleterious recessive alleles — while Ne above 500 is needed to maintain enough genetic variation for long-term evolutionary adaptation. When a conservation program reports a species has 5,000 individuals remaining, that sounds reassuring — but if Ne is only 200, the population is genetically precarious. Estimating Ne transforms conservation from a head-counting exercise into a genetically informed assessment of population viability.
