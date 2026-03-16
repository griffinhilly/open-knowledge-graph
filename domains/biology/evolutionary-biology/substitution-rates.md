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
- molecular-clock-hypothesis
tags:
- molecular-clock
- substitution
- neutral-theory
- mutation
stage: advanced
status: draft
---

# Substitution Rates and Neutral Theory

## Core Idea
At neutral sites, substitution rate K equals twice the mutation rate (K = 2μ). Under purifying selection, K < 2μ. This fundamental relationship enables inference of mutation rates and selection strength from genetic sequences.

## Explainer

From your study of the molecular clock and DNA sequence divergence, you know that species accumulate genetic differences over time at roughly predictable rates. **Substitution rate** is the formal measure of this process: the rate at which mutations become fixed in a population and show up as permanent differences between lineages. Understanding what controls this rate connects mutation, drift, and selection into a single quantitative framework.

The foundational result comes from neutral theory. In a diploid population of size N, each new neutral mutation arises at rate 2Nμ per generation across all individuals (2N gene copies, each mutating at rate μ). The probability that any single neutral mutation drifts to fixation is 1/(2N). Multiply these together and the population size cancels: **K = 2Nμ × 1/(2N) = μ**. For a haploid, K = μ directly; for a diploid, K = 2μ when counting per-site rates across both alleles. This elegant cancellation means that **neutral substitution rate is independent of population size** — it depends only on the mutation rate. A large population produces more mutations but each has a proportionally smaller chance of fixing, and these effects exactly balance.

This result is what makes the molecular clock possible. If neutral substitution rate equals the mutation rate, and mutation rate is roughly constant per generation, then the number of neutral differences between two species is proportional to their divergence time. By comparing sequences at sites presumed neutral (pseudogenes, synonymous sites, intergenic regions), you can estimate divergence times or, conversely, calibrate the mutation rate using fossil-dated divergences.

When selection is operating, the picture changes predictably. **Purifying selection** removes deleterious mutations before they can fix, so K drops below the neutral expectation. The stronger the constraint, the lower K falls. **Positive selection** can push K above the neutral rate temporarily, but this is rare and localized. By comparing substitution rates at different classes of sites — synonymous versus nonsynonymous, conserved versus variable regions — you can directly measure the strength and direction of selection. Sites evolving at or near the neutral rate serve as the baseline against which all departures from neutrality are measured, making substitution rate theory the quantitative backbone of molecular evolution.
