---
id: genetic-drift
title: Genetic Drift
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-genetics-intro
  type: hard
- id: natural-selection
  type: soft
- id: probability-axioms-and-rules
  type: soft
- id: statistics-probability
  type: soft
- id: probability-rules-for-events
  type: soft
builds-toward:
- speciation
- hardy-weinberg-equilibrium
- molecular-evolution
tags:
- evolution
- stochastic
- allele-frequency
- small-populations
stage: advanced
status: validated
---

# Genetic Drift

## Core Idea
Genetic drift is the random change in allele frequencies caused by chance sampling events, particularly powerful in small populations. Unlike natural selection, drift is not driven by fitness — neutral or even slightly deleterious alleles can become fixed by chance. The bottleneck effect (population crash) and founder effect (new colony from few individuals) are important special cases. Drift reduces genetic diversity over time.

## How It's Best Learned
Simulate allele frequency changes in small vs. large populations using coin-flip models or software. Compare outcomes of drift vs. selection across many replicate populations. Pay attention to how effective population size (Ne) differs from census size.

## Common Misconceptions
- Genetic drift is not random mutation — it is random sampling of existing alleles.
- Drift can fix maladaptive alleles; evolution does not always move toward 'improvement'.
- Large populations are not immune to drift, but its effects are minor compared to small populations.

## Questions

```yaml
- question: "Which of the following best describes the mechanism of genetic drift?"
  type: multiple-choice
  options:
    - "Natural selection favoring adaptive traits in small populations"
    - "Random sampling error in allele transmission between generations"
    - "Directed mutations accumulating in isolated populations"
    - "Gene flow introducing new alleles from neighboring populations"
  answer: 1
  explanation: "Genetic drift is a statistical sampling phenomenon — each generation, by chance, some alleles are over- or under-represented in offspring relative to their frequency in the parents. It is not driven by fitness (that is natural selection), does not create new variants (that is mutation), and is not caused by migration (that is gene flow)."

- question: "Genetic drift will always push a population toward better-adapted alleles over time, because random chance tends to eliminate harmful variants."
  type: true-false
  answer: false
  explanation: "Drift is fitness-blind — it operates on allele frequencies by chance alone, regardless of whether an allele is beneficial, neutral, or harmful. A deleterious allele can increase in frequency or even reach fixation purely by chance, especially in small populations. Evolution through drift does not trend toward improvement."

- question: "Why does genetic drift have a stronger effect on small populations than on large ones?"
  type: short-answer
  answer: "In small populations, each individual represents a larger fraction of the gene pool, so chance events in reproduction cause larger swings in allele frequency. In large populations, random fluctuations tend to cancel out, keeping allele frequencies closer to expected values — the same reason a coin flipped 10 times can easily give 8 heads, but 10,000 flips reliably give near 50%."
  explanation: "This is the law of large numbers applied to population genetics. Genetic drift is sampling error, and sampling error decreases as sample size increases. The bottleneck effect and founder effect are powerful precisely because they drastically reduce effective population size, magnifying drift."
```

## Explainer

You already know from population genetics that a population's allele frequencies change over time through mechanisms like mutation, selection, and migration. Genetic drift is a fourth mechanism — and unlike natural selection, it has nothing to do with fitness. It is pure statistical noise.

Imagine a small island population of 10 beetles, 5 carrying a red allele and 5 carrying a brown allele. If a storm randomly kills 3 red-allele carriers but no brown ones, the red allele frequency drops — not because brown is more adaptive, but because of chance. In the next generation, that skewed starting point compounds the effect. Drift is essentially sampling error in allele transmission: each generation is a random draw from the previous one, and small samples are noisier than large ones.

The expected *direction* of allele frequency change from drift is zero — it does not push alleles toward fixation or elimination in any predictable direction. But the *variance* is large in small populations and small in large ones. This is why the bottleneck effect (a population crash leaving only a few survivors) and founder effect (a few individuals colonizing a new area) are such powerful evolutionary forces: they create tiny effective population sizes (Ne), turning up the volume on drift. An allele present at 10% frequency in a large population might be entirely absent — or the only allele remaining — after a bottleneck.

Given enough generations, drift will eventually fix one allele and eliminate all others at a given locus. For a neutral allele, the probability that it reaches fixation equals its current frequency. So a rare allele has only a small chance of fixing, but if it does, it happened by chance rather than fitness advantage. This is a key insight of the neutral theory of molecular evolution: many amino acid substitutions observed between species appear to be neutral changes that were fixed by drift, not selected for by the environment.

A critical distinction to keep straight: genetic drift reshuffles the frequencies of *existing alleles* — it does not create new variants. Mutation is what introduces new alleles into a population; drift determines whether those alleles spread, persist, or disappear. Confusing these two processes is one of the most common errors when reasoning about evolutionary change.
