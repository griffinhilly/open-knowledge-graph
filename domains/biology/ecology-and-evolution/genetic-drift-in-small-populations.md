---
id: genetic-drift-in-small-populations
title: Genetic Drift and Random Change in Small Populations
domain: biology
course: ecology-and-evolution
prerequisites:
- id: genetic-drift
  type: hard
- id: effective-population-size
  type: soft
- id: population-genetics-intro
  type: soft
- id: probability-axioms
  type: soft
- id: probability-rules-for-events
  type: soft
- id: stochastic-processes
  type: soft
builds-toward:
- mutation-as-evolutionary-force
- population-genetic-structure-metapopulations
- conservation-genetics-effective-size
tags:
- genetic-drift
- random-sampling
- bottleneck
- founder-effect
stage: formal-systems
status: draft
---

# Genetic Drift and Random Change in Small Populations

## Core Idea
Genetic drift is random change in allele frequencies due to sampling error in small populations. In small Ne (effective population size), drift overwhelms weak selection and can fix neutral mutations. Bottlenecks and founder effects cause rapid drift and loss of genetic diversity. Drift is inversely proportional to population size.

## Questions

```yaml
- question: "A population of 10,000 individuals is reduced to 20 by a catastrophic event, then recovers to 10,000 over the next century. Which statement best describes the genetic outcome?"
  type: multiple-choice
  options:
    - "The population recovers its original genetic diversity quickly as numbers rebound"
    - "The bottleneck causes permanent loss of alleles that existed only in the individuals who died"
    - "Natural selection acts more strongly during the bottleneck because the population is small"
    - "Genetic drift has no lasting effect because the final population size is the same as the original"
  answer: 1
  explanation: "Alleles carried only by individuals who did not survive are permanently lost — no amount of subsequent population growth can recreate them. Genetic diversity is determined by which alleles passed through the bottleneck, not by the recovery in numbers. Selection actually becomes less effective (not more) in small populations because drift dominates."

- question: "In a large population, a neutral mutation (no fitness effect) will almost certainly be lost to drift before it spreads."
  type: true-false
  answer: true
  explanation: "In any finite population, a new neutral mutation starts at a frequency of 1/(2N). The probability that it fixes (reaches 100%) is equal to its starting frequency — 1/(2N) — which is very small in a large population. The vast majority of neutral mutations are lost by chance. This is why effective population size strongly shapes how much neutral variation persists."

- question: "How does a founder effect differ from a population bottleneck, and what do they share in common?"
  type: short-answer
  answer: "A founder effect occurs when a small group colonizes a new habitat, establishing a population from just a few individuals. A bottleneck is a drastic reduction in an existing population's size. Both result in a population rebuilt from a small sample of the original gene pool, causing loss of alleles, reduced heterozygosity, and accelerated genetic drift."
  explanation: "The key shared mechanism is sampling error: a small subset of individuals cannot carry all the alleles present in the original population. The difference is context — founder events involve geographic dispersal and isolation, while bottlenecks involve mortality or other reductions in place. Both leave lasting genetic signatures in the surviving lineage."
```

## Explainer

You already know that genetic drift describes random fluctuations in allele frequencies — the genetic equivalent of a coin flip not landing 50/50 every time just because the odds say it should. The key insight of this topic is that the *size* of the population determines how much drift dominates evolutionary change. In a large population, random sampling errors average out across thousands of reproductions. In a small population, they do not: a single unlucky generation can eliminate an allele entirely, no matter how fit it is.

The mathematics here connects directly to probability. When you draw a sample from a gene pool, the variance in allele frequency from one generation to the next is p(1−p)/(2Ne), where Ne is the effective population size. As Ne shrinks, variance explodes. This means that in small populations, allele frequencies bounce around wildly — and eventually, by chance, any given allele either disappears (frequency = 0) or takes over (frequency = 1). This endpoint is called *fixation*. Once an allele is fixed, no further change is possible at that locus without new mutation.

A *population bottleneck* is a temporary but severe reduction in population size — a plague, a habitat destruction event, a mass die-off. The survivors carry only a subset of the original alleles. When the population recovers numerically, it cannot recover the alleles that were lost. Think of pouring a bucket of colored marbles through a funnel: only the colors that made it through the narrow neck are available afterward, no matter how large the bucket on the other side becomes. The Cheetah is a famous example — the species shows almost no genetic variation across individuals, a legacy of a severe bottleneck tens of thousands of years ago.

A *founder effect* is similar in mechanism but different in context: a small number of individuals colonize a new area, founding a population that carries only the alleles those few individuals happened to possess. Island populations, immigrant communities, and religious isolates all show founder effects — for instance, the Amish have unusually high rates of certain rare genetic diseases because their founding population was small and happened to carry those alleles.

The deeper point is that drift and selection are not independent forces — they compete. Selection favoring a beneficial allele can reliably push that allele toward fixation in a large population, but in a small population, drift may overpower selection and eliminate the beneficial allele anyway. This has serious consequences for conservation biology: small isolated populations lose the genetic variation needed to adapt to new diseases, climate shifts, and environmental changes, making them more vulnerable to extinction even after their numbers recover.
