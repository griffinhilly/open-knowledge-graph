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
status: validated
---

# Fixation Probability and Diffusion Models

## Core Idea
The probability a mutant allele fixes depends on selection strength and population size. New beneficial mutations have fixation probability ≈ 2s in large populations; neutral mutations fix with probability 1/(2Ne). Diffusion equations model this stochastic process.

## Questions

```yaml
- question: "A beneficial mutation with selection coefficient s = 0.02 appears as a single copy in a population with effective size Ne = 10,000. What is the approximate probability that this mutation will eventually reach fixation?"
  type: multiple-choice
  options:
    - "Nearly 100% — selection is strong enough to guarantee fixation in a large population"
    - "About 50% — beneficial alleles have roughly even chances of fixing or being lost"
    - "About 4% — even beneficial mutations are usually lost to drift while they are rare"
    - "Exactly 1/20,000 — the same as a neutral mutation, because drift dominates in large populations"
  answer: 2
  explanation: "Using the approximation 2s = 2 × 0.02 = 0.04, the fixation probability is about 4%. This means the mutation will be lost ~96% of the time. This counterintuitive result arises because when the mutation first appears as a single copy among 20,000 alleles, it is highly vulnerable to chance elimination — the carrier might die before reproducing or happen to pass on the other allele. Selection becomes reliably effective only once the allele has drifted to a high enough frequency to avoid stochastic loss. Option A (the most tempting wrong answer) incorrectly assumes selection guarantees fixation regardless of frequency."

- question: "A weakly deleterious mutation with s = -0.0001 appears in a bacterial pathogen with effective population size Ne = 100 during a bottleneck. What is the likely fate of this mutation?"
  type: multiple-choice
  options:
    - "It will be rapidly purged — natural selection efficiently removes all deleterious mutations regardless of population size"
    - "It will behave approximately as a neutral mutation and may fix by drift, because Ne × s is much less than 1"
    - "It will be maintained at intermediate frequency indefinitely by balancing selection"
    - "It cannot fix because a negative selection coefficient means fixation probability is exactly zero"
  answer: 1
  explanation: "Ne × s = 100 × 0.0001 = 0.01, which is much less than 1. When this product is << 1, drift overwhelms selection and the allele behaves essentially as neutral — it may fix, be lost, or drift to intermediate frequencies by chance, with selection having minimal effect. This is the key practical implication of the Ne × s threshold: in small populations (bottlenecks, endangered species, pathogens), mildly deleterious mutations accumulate as if they were neutral, with important consequences for fitness and disease evolution."

- question: "A new neutral mutation arising as a single copy in a diploid population of effective size Ne has a fixation probability of 1/(2Ne)."
  type: true-false
  answer: true
  explanation: "In a diploid population with Ne individuals, there are 2Ne allele copies. Each copy has an equal probability of being ancestral to all future alleles, so a new neutral mutation (present once) has probability 1/(2Ne) of fixing. This is a foundational result of neutral theory. It also leads to the elegant conclusion that neutral mutations fix at a rate equal to the mutation rate itself, independent of population size — because although larger populations have lower per-allele fixation probability, they also produce proportionally more new mutations."

- question: "A strongly beneficial mutation with a large selection coefficient is virtually guaranteed to fix once it appears in a population, because strong selection overcomes drift."
  type: true-false
  answer: false
  explanation: "The fixation probability is approximately 2s regardless of how large s is within biologically realistic ranges. A mutation with s = 0.10 has only ~20% fixation probability; a mutation with s = 0.20 has ~40%. Even very strongly beneficial mutations are usually lost — because when a mutation first appears as a single copy, it is at the mercy of drift before selection has a chance to act. 'Virtually guaranteed' would require a fixation probability near 100%, which never occurs for a single new mutation. Most beneficial mutations are simply unlucky in their early generations."

- question: "What does the product Ne × s reveal about the fate of a mutation, and why does this product matter more than the selection coefficient s alone?"
  type: short-answer
  answer: "Ne × s marks the boundary between drift-dominated and selection-dominated evolution. When Ne × s >> 1, selection reliably determines allele fate — beneficial alleles tend to fix and deleterious alleles tend to be purged. When Ne × s << 1, drift dominates and even deleterious alleles can fix as if they were neutral. The selection coefficient s alone is insufficient because what matters is whether selection is strong relative to drift, and drift strength is inversely proportional to Ne. A mutation with s = 0.001 is strongly favored in a population of Ne = 10,000 (Ne × s = 10) but effectively invisible to selection in a population of Ne = 100 (Ne × s = 0.1)."
  explanation: "This threshold is why population size matters so much for evolutionary outcomes. Large populations purge mildly deleterious mutations efficiently and can selectively fix weakly beneficial ones. Small populations (endangered species, populations through bottlenecks, some pathogens) accumulate deleterious mutations and lose beneficial ones to drift — with real consequences for adaptation, fitness, and disease evolution."
```

## Explainer

From your study of genetic drift, you know that allele frequencies wander randomly in finite populations and that smaller populations experience stronger random fluctuations. From effective population size, you know that N_e — not census size — determines the strength of drift. Fixation probability brings these ideas together quantitatively: given a new mutation appearing as a single copy in a population, what is the chance it eventually reaches a frequency of 100% and becomes fixed?

For a **neutral mutation** — one with no fitness effect — the answer is straightforward. Every allele copy in the population has an equal chance of being the ancestor of all future copies. In a diploid population of N_e individuals, there are 2N_e allele copies, so a new neutral mutation (present in one copy) has a fixation probability of **1/(2N_e)**. This is small in large populations — one in a million for N_e = 500,000 — but crucially, neutral mutations arise frequently, and the rate at which they fix equals the mutation rate itself. This elegant result from neutral theory means the molecular clock ticks at a rate determined solely by mutation, independent of population size.

For a **beneficial mutation** with selection coefficient *s* (meaning carriers have fitness 1 + s relative to non-carriers), the fixation probability in a large population is approximately **2s**. A mutation conferring a 1% fitness advantage (s = 0.01) fixes with about 2% probability. This seems remarkably low — even strongly beneficial mutations are usually lost to drift while rare. The reason is that when a new mutation exists in a single copy, it is highly vulnerable to chance elimination. The carrier might die before reproducing, or happen to pass on the other allele copy. Only once the mutation reaches a frequency high enough that drift can no longer easily eliminate it does selection reliably carry it to fixation. The formula 2s captures this: stronger selection gives the mutation a larger initial "push" past the danger zone of low frequency.

The boundary between drift-dominated and selection-dominated dynamics is set by the product **N_e × s**. When N_e × s >> 1, selection is the dominant force and the allele behaves approximately deterministically — beneficial alleles tend to fix, deleterious ones tend to be purged. When N_e × s << 1, drift dominates and even deleterious alleles can fix by chance — their fate is effectively that of a neutral allele. This threshold is critical for understanding molecular evolution: in small populations, mildly deleterious mutations accumulate because selection cannot effectively remove them, while in large populations, even very weakly beneficial mutations can be favored. **Diffusion models** formalize this by treating allele frequency change as a continuous stochastic process, yielding exact solutions for fixation probability, expected fixation time, and the distribution of allele frequencies across populations — connecting population genetics to the mathematics of random walks and Brownian motion.
