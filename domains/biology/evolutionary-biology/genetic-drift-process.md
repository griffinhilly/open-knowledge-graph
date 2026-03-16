---
id: genetic-drift-process
title: 'Genetic Drift: Process and Population Effects'
domain: biology
course: evolutionary-biology
prerequisites:
- id: genetic-drift
  type: hard
- id: allele-frequency-change
  type: hard
- id: probability-axioms
  type: soft
builds-toward:
- effective-population-size
- peripatric-speciation
tags:
- drift
- stochastic-evolution
- population-size
stage: advanced
status: draft
---

# Genetic Drift: Process and Population Effects

## Core Idea
Genetic drift is random sampling of alleles in finite populations, causing random fluctuations in allele frequency regardless of selection. The strength of drift (measured by its variance) is inversely proportional to population size: larger populations experience weaker drift. Drift can fix neutral alleles, eliminate beneficial alleles, and preserve deleterious alleles, making it a major driver of molecular evolution.

## How It's Best Learned
Run Monte Carlo simulations of drift in populations of varying sizes. Observe fixation and loss of alleles and note that time to fixation increases with population size.

## Common Misconceptions
- Drift only matters in very small populations; drift affects all populations and is particularly important for neutral evolution.
- Drift causes alleles to predictably increase; drift causes random changes with no directional bias.

## Explainer

You already know from studying genetic drift that allele frequencies can change by chance alone, and from allele frequency change that populations evolve when allele frequencies shift across generations. This topic deepens your understanding of the **process mechanics** of drift — how and why random sampling in finite populations produces the patterns we observe, and what those patterns mean for evolution.

Think of reproduction as drawing marbles from a jar. A population of diploid organisms has a "jar" of 2N gene copies. The next generation is formed by randomly sampling 2N copies from this jar. If the jar contains 50% red and 50% blue marbles, you would expect the sample to be roughly 50/50 — but "roughly" is the key word. In a jar of 20 marbles, a sample might easily come out 60/40 or 40/60 by chance. In a jar of 20,000, a 51/49 split would be unusual. This is why **drift is inversely proportional to population size**: the sampling error is larger when fewer copies are drawn. The variance in allele frequency change per generation is approximately *p(1-p)/2N*, where p is the current allele frequency and N is the population size.

Over many generations, drift causes allele frequencies to wander unpredictably — a **random walk**. Eventually, every allele either drifts to fixation (frequency = 1.0) or loss (frequency = 0). For a neutral allele, the probability of fixation equals its current frequency, and the average time to fixation is 4N generations. This means drift is both inevitable and slow in large populations but rapid and powerful in small ones. A neutral allele at 10% frequency has a 10% chance of eventually fixing — regardless of population size — but it takes vastly longer in a population of a million than in a population of a hundred.

The evolutionary consequences are profound. Drift can **fix mildly deleterious alleles** that selection alone would eliminate, because in small populations the random noise of drift can overpower weak selective pressures. This happens when the selection coefficient (s) is smaller than roughly 1/2N — the allele behaves as if it were neutral. Drift can also **eliminate beneficial alleles** before they have a chance to spread, especially when they are rare and selection is weak. At the molecular level, the neutral theory of molecular evolution argues that most substitutions between species are neutral alleles fixed by drift, not beneficial alleles fixed by selection. Understanding drift is therefore essential for interpreting DNA sequence divergence, designing conservation strategies for small populations, and recognizing the limits of natural selection's power.
