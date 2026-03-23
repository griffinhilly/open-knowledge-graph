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
status: validated
---

# Allele Frequency Change and Evolutionary Dynamics

## Core Idea
Allele frequencies are the fundamental currency of evolution; changes in these frequencies constitute evolutionary change at the molecular level. The change in allele frequency in one generation depends on selection coefficients, mutation rates, migration rates, and drift. Multiple evolutionary forces can act simultaneously, and their relative strengths determine the net direction and speed of evolution.

## How It's Best Learned
Use spreadsheet simulations to model allele frequency changes under different forces. Plot allele frequency trajectories for weak selection, strong drift, and balanced forces.

## Common Misconceptions
- A favorable allele will definitely increase in frequency; in small populations or with weak selection, drift can overpower selection.
- Allele frequencies change primarily by mutation; mutation is typically the weakest force of evolution.

## Questions

```yaml
- question: "A slightly beneficial allele (selection coefficient s = 0.01) appears independently in two wildflower populations: one with N = 10,000 individuals and one with N = 50. In which population is the allele more likely to increase to fixation, and why?"
  type: multiple-choice
  options:
    - "The small population — genetic bottlenecks accelerate fixation of any allele regardless of fitness"
    - "Both equally — the selection coefficient is the same in both populations, so the outcome should be the same"
    - "The large population — Ns = 100 >> 1, so selection is effective; in the small population Ns = 0.5, so drift dominates and may eliminate the allele despite its advantage"
    - "The small population — fewer competing alleles means the beneficial allele faces less competition"
  answer: 2
  explanation: "The key is the product Ns. In the large population, Ns = 10,000 × 0.01 = 100 >> 1, meaning selection is far stronger than drift and reliably drives the beneficial allele upward. In the small population, Ns = 50 × 0.01 = 0.5, meaning drift (random sampling error) is roughly as strong as selection — the allele's slight advantage becomes statistically invisible against the noise of random sampling. The allele may be lost by chance despite its fitness benefit. Population size, not just selection coefficient, determines evolutionary outcomes."

- question: "Of the four evolutionary forces (natural selection, mutation, gene flow, genetic drift), which is generally the weakest at shifting allele frequencies at a single locus per generation?"
  type: multiple-choice
  options:
    - "Genetic drift — it only affects small populations and has no directional tendency"
    - "Natural selection — it requires many generations to produce noticeable frequency changes"
    - "Mutation — typical per-locus mutation rates are only 10⁻⁵ to 10⁻⁹ per generation"
    - "Gene flow — most populations are geographically isolated and receive little migration"
  answer: 2
  explanation: "Mutation rates per locus per generation are typically 10⁻⁵ to 10⁻⁹ — meaning most generations see no new mutation at a given locus at all. While mutation is the ultimate source of all genetic variation, it changes allele frequencies at any single locus glacially slowly. Selection, gene flow, or drift can shift frequencies orders of magnitude faster. Mutation's evolutionary role is to supply the raw variation that other forces then act on, not to drive frequency change directly."

- question: "A 'favorable' allele — one that increases reproductive success — will always increase in frequency over time, because natural selection is a systematic, directional force."
  type: true-false
  answer: false
  explanation: "In small populations, genetic drift can overpower selection. When Ns (population size × selection coefficient) is near or below 1, allele trajectories become essentially random regardless of fitness. A slightly favorable allele (s = 0.01) in a population of N = 50 has Ns = 0.5 — drift dominates, and the allele may be lost by chance. In large populations, the statement approaches truth (Ns >> 1 makes selection effective), but the blanket claim 'favorable alleles always increase' ignores the critical role of population size."

- question: "Evolution at the molecular level is formally defined as a change in allele frequencies in a population — not as adaptation, morphological change, or the appearance of new species."
  type: true-false
  answer: true
  explanation: "This is the population genetics definition of evolution: a change in the frequency of alleles in a gene pool over time. If allele A₁ makes up 40% of the gene pool this generation and 42% the next, evolution has occurred at that locus — even if no organism looks or behaves differently. This definition is powerful because it allows precise mathematical treatment of evolutionary processes. Adaptation, speciation, and morphological change are downstream consequences of allele frequency change, not the definition itself."

- question: "Explain how a slightly beneficial allele could be permanently lost from a population despite natural selection favoring it."
  type: short-answer
  answer: "In small populations, genetic drift — random sampling error in which alleles happen to reproduce — can overpower weak selection. Each generation, the alleles that are transmitted to offspring are a random sample from the current generation. If the beneficial allele is rare and the population is small, random sampling may result in zero copies being transmitted, eliminating it permanently. The rough criterion is Ns: when population size (N) times selection coefficient (s) is much less than 1, drift dominates and allele trajectories become essentially random. The allele's slight advantage cannot overcome the noise of random sampling."
  explanation: "This is one of the most counterintuitive results in evolutionary biology. It means that 'survival of the fittest' is not guaranteed at the genetic level — beneficial alleles can be lost by chance, and mildly harmful alleles can become fixed. The outcome depends not just on fitness but on population size. This is why conservation genetics cares so deeply about population size: small populations lose beneficial variation and accumulate deleterious alleles by drift, regardless of selection pressures."
```

## Explainer

From your work in population genetics, you know that a population's genetic state can be described by its **allele frequencies** — the proportions of different variants at each gene locus. Evolution, at its most fundamental level, is simply a change in these frequencies over time. If allele A₁ makes up 40% of the gene pool this generation and 42% the next, evolution has occurred at that locus, regardless of whether the change is visible in the organisms' appearance. This reframing — evolution as bookkeeping of allele frequencies — is what makes population genetics so powerful, because it lets us write equations that predict how fast and in what direction populations will change.

Four forces drive allele frequency change, and they differ enormously in strength and direction. **Natural selection** is the only consistently directional force: if one allele confers higher fitness, it increases in frequency at a rate proportional to its **selection coefficient** (s), which measures the fitness difference between genotypes. A selection coefficient of 0.01 means carriers of the favored allele have a 1% survival or reproduction advantage — seemingly tiny, but over hundreds of generations this compounds into near-complete replacement. **Mutation** introduces new alleles but does so at rates typically around 10⁻⁵ to 10⁻⁹ per locus per generation, making it by far the weakest force for shifting frequencies at any single locus. Its importance lies in supplying the raw genetic variation that other forces act upon. **Gene flow** (migration) can be strong and directional, rapidly pulling recipient population frequencies toward those of the source population. And **genetic drift** — random sampling error in finite populations — is directionless but powerful in small populations, capable of fixing or eliminating alleles regardless of their fitness effects.

The critical insight is that these forces act **simultaneously**, and the outcome depends on their relative magnitudes. In a large population under strong selection with little migration, selection dominates and allele frequencies change predictably. In a small, isolated population, drift can overpower weak selection: an allele with a slight fitness advantage may nonetheless be lost by chance, while a slightly deleterious allele may drift to fixation. The rough rule is that selection is effective when the product of population size (N) and selection coefficient (s) is much greater than 1 (Ns >> 1); when Ns is near or below 1, drift dominates and allele trajectories become essentially random.

You can visualize these dynamics by imagining allele frequency as a ball on a landscape. Selection creates slopes — the ball rolls toward the favored allele. Drift adds random jostling — in a large population the jostles are tiny and the ball follows the slope reliably, but in a small population the jostles are violent enough to knock the ball uphill against selection. Mutation gently nudges alleles into existence at the edges, and gene flow acts like a rope pulling the ball toward whatever frequency the neighboring population has. The trajectory of any real allele reflects the net effect of all these pushes and pulls operating together, which is why predicting evolutionary outcomes requires knowing not just which forces are present but how strong each one is relative to the others.
