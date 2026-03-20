---
id: hardy-weinberg-equilibrium
title: Hardy-Weinberg Equilibrium
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-genetics-intro
  type: hard
- id: mendelian-genetics
  type: hard
- id: gene-flow
  type: soft
- id: genetic-drift
  type: soft
- id: simple-probability
  type: soft
- id: solving-quadratics-by-factoring
  type: soft
- id: algebraic-and-transcendental-elements
  type: soft
builds-toward:
- speciation
- molecular-evolution
tags:
- population-genetics
- allele-frequency
- null-model
- evolution
stage: advanced
status: validated
---

# Hardy-Weinberg Equilibrium

## Core Idea
Hardy-Weinberg equilibrium predicts that allele and genotype frequencies remain constant across generations in a large, randomly mating population with no selection, mutation, migration, or drift. Given allele frequencies p and q (p + q = 1), genotype frequencies are p², 2pq, and q². This null model is a baseline — deviations from it signal that evolutionary forces are acting. It is used to infer allele frequencies from genotype data and vice versa.

## How It's Best Learned
Practice calculating expected genotype frequencies from observed allele frequencies, then compare to observed genotypes to test for equilibrium. Work through violations — a population under directional selection will show systematic departures from HWE predictions.

## Common Misconceptions
- Hardy-Weinberg equilibrium does not mean evolution is impossible — it describes what happens when evolution is absent.
- The equation p² + 2pq + q² = 1 applies to diploid, sexually reproducing organisms under specific conditions.
- A population in HWE is not 'frozen' — phenotypes can vary; it is allele frequencies that are stable.

## Questions

```yaml
- question: "A population has allele frequencies p = 0.6 (dominant A) and q = 0.4 (recessive a). What is the expected frequency of heterozygotes (Aa) under Hardy-Weinberg equilibrium?"
  type: multiple-choice
  options: ["0.36", "0.16", "0.48", "0.24"]
  answer: 2
  explanation: "The frequency of heterozygotes is 2pq = 2(0.6)(0.4) = 0.48. A common error is computing pq = 0.24 and forgetting to multiply by 2, which accounts for both Aa and aA configurations."

- question: "If a population is in Hardy-Weinberg equilibrium, it means that no evolution is occurring and none can occur in the future."
  type: true-false
  answer: false
  explanation: "HWE describes a snapshot in which allele frequencies are currently stable because the five conditions are met. It makes no claim about the future — as soon as any condition is violated (e.g., migration brings new alleles), frequencies will shift and evolution resumes. HWE is a null model, not a permanent state."

- question: "A population shows observed genotype frequencies that deviate significantly from Hardy-Weinberg expectations. What does this tell you?"
  type: short-answer
  answer: "One or more evolutionary forces are acting on the population — such as natural selection, genetic drift, non-random mating, gene flow, or mutation."
  explanation: "HWE predicts stable frequencies only when all five conditions hold. A significant deviation is evidence that at least one condition is violated. Identifying which condition helps diagnose the evolutionary mechanism at work — for example, excess heterozygotes suggest heterozygote advantage (balancing selection), while a deficit suggests inbreeding."
```

## Explainer

Hardy-Weinberg equilibrium is best understood as a null model — a prediction of what allele and genotype frequencies look like when evolution is *not* happening. It was developed independently by G.H. Hardy and Wilhelm Weinberg in 1908 to counter a then-common misconception that dominant alleles would automatically increase in frequency over time. They showed this is wrong: in a large, randomly mating population free from selection, mutation, migration, and drift, allele frequencies stay constant indefinitely.

The mathematics is built on Mendelian probability. If allele A has frequency p and allele a has frequency q, and p + q = 1, then random mating is like drawing two alleles independently from a pool. The probability of getting AA is p × p = p², getting aa is q × q = q², and getting Aa is 2 × p × q = 2pq (the factor of 2 accounts for both orders: Aa and aA). Adding these gives the Hardy-Weinberg identity: p² + 2pq + q² = 1. This equation lets you move in either direction — given allele frequencies, predict genotype frequencies; given genotype frequencies, infer allele frequencies.

The five conditions for HWE (large population, random mating, no selection, no mutation, no migration) are never perfectly met in nature. That is the point. When you test a real population against HWE predictions and find a significant departure, you know an evolutionary force is operating. For example, if you observe far fewer heterozygotes than 2pq predicts, inbreeding or assortative mating is a likely explanation. If heterozygotes are in excess, balancing selection may be maintaining both alleles. HWE is a diagnostic tool, not a description of reality.

A common confusion is thinking that HWE and evolution are opposites — that a population either evolves or is in equilibrium. In fact, HWE is just describing the baseline for one specific quantity (allele frequency). A population in HWE can still have enormous phenotypic variation, experience births and deaths, and undergo ecological change. What it is *not* doing is shifting the frequency of alleles from generation to generation. The moment any of the five conditions is disrupted — say, a drought kills all short-necked individuals — the allele frequencies change, and the population departs from equilibrium.
