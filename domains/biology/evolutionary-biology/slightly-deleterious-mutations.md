---
id: slightly-deleterious-mutations
title: Slightly Deleterious Mutations and Mutational Load
domain: biology
course: evolutionary-biology
prerequisites:
- id: mutation-selection-balance
  type: hard
- id: genetic-drift
  type: hard
- id: population-genetics-intro
  type: soft
builds-toward:
- nearly-neutral-evolution
- efficacy-selection-finite-populations
tags:
- mutation
- deleterious
- load
- genome-evolution
stage: advanced
status: draft
---

# Slightly Deleterious Mutations and Mutational Load

## Core Idea
Mildly deleterious mutations accumulate in small populations because drift overwhelms weak purifying selection. This reduces population fitness (mutational load) and becomes critical in conservation biology and speciation.

## Explainer

You already understand mutation-selection balance: in large populations, selection efficiently removes deleterious alleles, maintaining them at low equilibrium frequencies. And from genetic drift, you know that random sampling effects are strongest in small populations. **Slightly deleterious mutations** sit at the intersection of these two forces, in a regime where neither dominates cleanly. These are mutations with small negative fitness effects — a selection coefficient (s) so tiny that drift can overpower selection in finite populations.

The critical threshold is the relationship between selection strength and population size. When the selection coefficient s is much larger than 1/(2Nₑ), where Nₑ is the effective population size, selection "sees" the mutation and can remove it efficiently. But when s is on the order of 1/(2Nₑ) or smaller, the mutation behaves almost as if it were neutral — drift pushes it up and down in frequency, and it may fix purely by chance despite being harmful. In a population of 10,000, a mutation with s = 0.00005 is effectively invisible to selection. In a population of 1,000,000, that same mutation is efficiently purged. The mutation hasn't changed; the population's ability to detect it has.

This has profound consequences. **Mutational load** — the cumulative fitness reduction caused by segregating deleterious alleles — builds up faster in small populations because their "filter" for weak selection is coarser. Imagine a quality control inspector examining widgets on an assembly line: a careful inspector (large population) catches tiny defects, while a rushed one (small population) misses them. Over time, the rushed inspector lets through many subtly flawed products. For real organisms, this means small populations gradually accumulate genetic damage that large populations would have eliminated.

The implications extend across biology. In conservation, endangered species with small population sizes face a **mutational meltdown** risk: as slightly deleterious mutations accumulate, fitness drops, which further reduces population size, which allows even more deleterious mutations to drift to fixation — a vicious cycle. In molecular evolution, the observation that most amino acid substitutions between species are slightly deleterious (not strictly neutral) led Tomoko Ohta to propose the **nearly neutral theory**, refining Kimura's original neutral model. The key prediction is that substitution rates for slightly deleterious mutations should be higher in lineages with smaller effective population sizes — a pattern confirmed across many taxonomic comparisons.
