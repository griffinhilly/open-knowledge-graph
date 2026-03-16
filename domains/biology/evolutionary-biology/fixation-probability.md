---
id: fixation-probability
title: Fixation Probability and Diffusion Models
domain: biology
course: evolutionary-biology
prerequisites:
- id: genetic-drift
  type: hard
- id: population-genetics-intro
  type: hard
- id: effective-population-size
  type: hard
builds-toward:
- nearly-neutral-evolution
- adaptive-landscape-crossing
tags:
- drift
- probability
- fixation
- population-genetics
stage: advanced
status: draft
---

# Fixation Probability and Diffusion Models

## Core Idea
The probability a mutant allele fixes depends on selection strength and population size. New beneficial mutations have fixation probability ≈ 2s in large populations; neutral mutations fix with probability 1/(2Ne). Diffusion equations model this stochastic process.

## Explainer

From your study of genetic drift, you know that allele frequencies wander randomly in finite populations and that smaller populations experience stronger random fluctuations. From effective population size, you know that N_e — not census size — determines the strength of drift. Fixation probability brings these ideas together quantitatively: given a new mutation appearing as a single copy in a population, what is the chance it eventually reaches a frequency of 100% and becomes fixed?

For a **neutral mutation** — one with no fitness effect — the answer is straightforward. Every allele copy in the population has an equal chance of being the ancestor of all future copies. In a diploid population of N_e individuals, there are 2N_e allele copies, so a new neutral mutation (present in one copy) has a fixation probability of **1/(2N_e)**. This is small in large populations — one in a million for N_e = 500,000 — but crucially, neutral mutations arise frequently, and the rate at which they fix equals the mutation rate itself. This elegant result from neutral theory means the molecular clock ticks at a rate determined solely by mutation, independent of population size.

For a **beneficial mutation** with selection coefficient *s* (meaning carriers have fitness 1 + s relative to non-carriers), the fixation probability in a large population is approximately **2s**. A mutation conferring a 1% fitness advantage (s = 0.01) fixes with about 2% probability. This seems remarkably low — even strongly beneficial mutations are usually lost to drift while rare. The reason is that when a new mutation exists in a single copy, it is highly vulnerable to chance elimination. The carrier might die before reproducing, or happen to pass on the other allele copy. Only once the mutation reaches a frequency high enough that drift can no longer easily eliminate it does selection reliably carry it to fixation. The formula 2s captures this: stronger selection gives the mutation a larger initial "push" past the danger zone of low frequency.

The boundary between drift-dominated and selection-dominated dynamics is set by the product **N_e × s**. When N_e × s >> 1, selection is the dominant force and the allele behaves approximately deterministically — beneficial alleles tend to fix, deleterious ones tend to be purged. When N_e × s << 1, drift dominates and even deleterious alleles can fix by chance — their fate is effectively that of a neutral allele. This threshold is critical for understanding molecular evolution: in small populations, mildly deleterious mutations accumulate because selection cannot effectively remove them, while in large populations, even very weakly beneficial mutations can be favored. **Diffusion models** formalize this by treating allele frequency change as a continuous stochastic process, yielding exact solutions for fixation probability, expected fixation time, and the distribution of allele frequencies across populations — connecting population genetics to the mathematics of random walks and Brownian motion.
