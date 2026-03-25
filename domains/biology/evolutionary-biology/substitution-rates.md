---
id: substitution-rates
title: Substitution Rates and Neutral Theory
domain: biology
course: evolutionary-biology
prerequisites:
- id: molecular-clock
  type: hard
- id: dna-sequence-divergence
  type: hard
- id: mutation-selection-balance
  type: soft
builds-toward:
- molecular-evolution-rates
- molecular-clock
tags:
- molecular-clock
- substitution
- neutral-theory
- mutation
stage: advanced
status: validated
---

# Substitution Rates and Neutral Theory

## Core Idea
At neutral sites, substitution rate K equals twice the mutation rate (K = 2μ). Under purifying selection, K < 2μ. This fundamental relationship enables inference of mutation rates and selection strength from genetic sequences.

## Questions

```yaml
- question: "Two isolated populations of the same species have the same per-site neutral mutation rate μ, but one population has N=500 individuals and the other has N=500,000. Under neutral theory, which population accumulates neutral substitutions faster?"
  type: multiple-choice
  options:
    - "The large population, because it generates far more new mutations per generation"
    - "The small population, because each new mutation has a much higher probability of drifting to fixation"
    - "Both populations accumulate neutral substitutions at the same rate"
    - "The large population, but only at synonymous sites; the small population is faster at nonsynonymous sites"
  answer: 2
  explanation: "The neutral substitution rate K = 2Nμ × 1/(2N) = μ for diploids, canceling population size entirely. The large population generates 1000× more mutations per generation, but each has 1/1000 the probability of drifting to fixation. These effects exactly cancel, yielding the same substitution rate μ regardless of N. This counterintuitive result — that neutral evolution proceeds at the same pace in small and large populations — is the foundational insight of Kimura's neutral theory and the theoretical basis of the molecular clock."

- question: "A researcher compares substitution rates at synonymous versus nonsynonymous sites in a protein-coding gene and finds that the nonsynonymous rate is far below the synonymous rate. What does this indicate?"
  type: multiple-choice
  options:
    - "Nonsynonymous mutations are less likely to occur because the genetic code is structured to make them rare"
    - "Purifying selection removes most nonsynonymous mutations before they can fix, because amino acid changes tend to be deleterious"
    - "Positive selection is driving rapid amino acid evolution at these sites"
    - "The gene has a low GC content, which reduces nonsynonymous mutation rates"
  answer: 1
  explanation: "When K_nonsynonymous << K_synonymous ≈ 2μ, it means most amino acid changes are eliminated by purifying selection before reaching fixation. Synonymous sites are approximately neutral (same amino acid regardless of nucleotide), so they serve as the neutral baseline (K ≈ 2μ). The ratio dN/dS = K_nonsynonymous / K_synonymous < 1 indicates constraint. If positive selection were driving amino acid evolution, we'd expect K_nonsynonymous > K_synonymous (dN/dS > 1), which is rare and localized."

- question: "A large population accumulates neutral substitutions faster per generation than a small population because it generates more new mutations per generation."
  type: true-false
  answer: false
  explanation: "This is the central misconception about neutral substitution rates. While a large population generates more mutations per generation (2Nμ vs. 2nμ for smaller n), each individual mutation has a proportionally lower probability of fixing by drift (1/2N vs. 1/2n). The two effects cancel exactly, yielding K = 2Nμ × 1/(2N) = μ for all population sizes. This independence from N is precisely what makes the molecular clock work across organisms of vastly different population sizes."

- question: "The molecular clock hypothesis is theoretically grounded in the neutral theory finding that the substitution rate at neutral sites equals the neutral mutation rate."
  type: true-false
  answer: true
  explanation: "If K = μ (neutral substitution rate equals per-site mutation rate), and μ is approximately constant per generation across lineages, then the number of neutral differences accumulated between two species is proportional to the number of generations since divergence. This proportionality — neutral differences accumulate like a clock ticking at rate μ — is the theoretical foundation. By comparing neutral or near-neutral sequence differences (synonymous sites, pseudogenes, intergenic regions) between species with known divergence times (from fossils), we can calibrate μ and then use it to date other divergences."

- question: "Explain why neutral substitution rate is independent of population size, showing how the two population-size-dependent factors cancel in the derivation."
  type: short-answer
  answer: "In a diploid population of size N, there are 2N gene copies. Each generation produces 2Nμ new mutations across all copies (mutation rate per copy per generation is μ). Each new neutral mutation has probability 1/(2N) of eventually drifting to fixation by genetic drift, since it starts as a single copy out of 2N. The substitution rate is the product of these: K = (2Nμ) × (1/2N) = μ. Population size N appears in both the numerator and denominator and cancels exactly. The result is that neutral evolution proceeds at a rate set only by the mutation rate, independent of how large or small the population is."
  explanation: "The cancellation is exact under ideal Wright-Fisher conditions. In reality, variation in population size, generation length, and mutation rate create noise in the molecular clock. But the theoretical independence from N is what makes the clock concept viable at all — otherwise, we would need to know historical population sizes (which are very difficult to estimate) to use sequence divergence as a time measure."
```

## Explainer

From your study of the molecular clock and DNA sequence divergence, you know that species accumulate genetic differences over time at roughly predictable rates. **Substitution rate** is the formal measure of this process: the rate at which mutations become fixed in a population and show up as permanent differences between lineages. Understanding what controls this rate connects mutation, drift, and selection into a single quantitative framework.

The foundational result comes from neutral theory. In a diploid population of size N, each new neutral mutation arises at rate 2Nμ per generation across all individuals (2N gene copies, each mutating at rate μ). The probability that any single neutral mutation drifts to fixation is 1/(2N). Multiply these together and the population size cancels: **K = 2Nμ × 1/(2N) = μ**. For a haploid, K = μ directly; for a diploid, K = 2μ when counting per-site rates across both alleles. This elegant cancellation means that **neutral substitution rate is independent of population size** — it depends only on the mutation rate. A large population produces more mutations but each has a proportionally smaller chance of fixing, and these effects exactly balance.

This result is what makes the molecular clock possible. If neutral substitution rate equals the mutation rate, and mutation rate is roughly constant per generation, then the number of neutral differences between two species is proportional to their divergence time. By comparing sequences at sites presumed neutral (pseudogenes, synonymous sites, intergenic regions), you can estimate divergence times or, conversely, calibrate the mutation rate using fossil-dated divergences.

When selection is operating, the picture changes predictably. **Purifying selection** removes deleterious mutations before they can fix, so K drops below the neutral expectation. The stronger the constraint, the lower K falls. **Positive selection** can push K above the neutral rate temporarily, but this is rare and localized. By comparing substitution rates at different classes of sites — synonymous versus nonsynonymous, conserved versus variable regions — you can directly measure the strength and direction of selection. Sites evolving at or near the neutral rate serve as the baseline against which all departures from neutrality are measured, making substitution rate theory the quantitative backbone of molecular evolution.
