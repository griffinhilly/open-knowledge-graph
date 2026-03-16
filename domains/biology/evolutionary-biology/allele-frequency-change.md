---
id: allele-frequency-change
title: Allele Frequency Change and Evolutionary Dynamics
domain: biology
course: evolutionary-biology
prerequisites:
- id: evolutionary-genetics-foundations
  type: hard
- id: population-genetics-intro
  type: hard
- id: probability-distributions
  type: soft
builds-toward:
- hardy-weinberg-advanced
- genetic-drift-process
- mutation-selection-balance
tags:
- population-genetics
- allele-frequency
- evolution
stage: advanced
status: draft
---

# Allele Frequency Change and Evolutionary Dynamics

## Core Idea
Allele frequencies are the fundamental currency of evolution; changes in these frequencies constitute evolutionary change at the molecular level. The change in allele frequency in one generation depends on selection coefficients, mutation rates, migration rates, and drift. Multiple evolutionary forces can act simultaneously, and their relative strengths determine the net direction and speed of evolution.

## How It's Best Learned
Use spreadsheet simulations to model allele frequency changes under different forces. Plot allele frequency trajectories for weak selection, strong drift, and balanced forces.

## Common Misconceptions
- A favorable allele will definitely increase in frequency; in small populations or with weak selection, drift can overpower selection.
- Allele frequencies change primarily by mutation; mutation is typically the weakest force of evolution.

## Explainer

From your work in population genetics, you know that a population's genetic state can be described by its **allele frequencies** — the proportions of different variants at each gene locus. Evolution, at its most fundamental level, is simply a change in these frequencies over time. If allele A₁ makes up 40% of the gene pool this generation and 42% the next, evolution has occurred at that locus, regardless of whether the change is visible in the organisms' appearance. This reframing — evolution as bookkeeping of allele frequencies — is what makes population genetics so powerful, because it lets us write equations that predict how fast and in what direction populations will change.

Four forces drive allele frequency change, and they differ enormously in strength and direction. **Natural selection** is the only consistently directional force: if one allele confers higher fitness, it increases in frequency at a rate proportional to its **selection coefficient** (s), which measures the fitness difference between genotypes. A selection coefficient of 0.01 means carriers of the favored allele have a 1% survival or reproduction advantage — seemingly tiny, but over hundreds of generations this compounds into near-complete replacement. **Mutation** introduces new alleles but does so at rates typically around 10⁻⁵ to 10⁻⁹ per locus per generation, making it by far the weakest force for shifting frequencies at any single locus. Its importance lies in supplying the raw genetic variation that other forces act upon. **Gene flow** (migration) can be strong and directional, rapidly pulling recipient population frequencies toward those of the source population. And **genetic drift** — random sampling error in finite populations — is directionless but powerful in small populations, capable of fixing or eliminating alleles regardless of their fitness effects.

The critical insight is that these forces act **simultaneously**, and the outcome depends on their relative magnitudes. In a large population under strong selection with little migration, selection dominates and allele frequencies change predictably. In a small, isolated population, drift can overpower weak selection: an allele with a slight fitness advantage may nonetheless be lost by chance, while a slightly deleterious allele may drift to fixation. The rough rule is that selection is effective when the product of population size (N) and selection coefficient (s) is much greater than 1 (Ns >> 1); when Ns is near or below 1, drift dominates and allele trajectories become essentially random.

You can visualize these dynamics by imagining allele frequency as a ball on a landscape. Selection creates slopes — the ball rolls toward the favored allele. Drift adds random jostling — in a large population the jostles are tiny and the ball follows the slope reliably, but in a small population the jostles are violent enough to knock the ball uphill against selection. Mutation gently nudges alleles into existence at the edges, and gene flow acts like a rope pulling the ball toward whatever frequency the neighboring population has. The trajectory of any real allele reflects the net effect of all these pushes and pulls operating together, which is why predicting evolutionary outcomes requires knowing not just which forces are present but how strong each one is relative to the others.
