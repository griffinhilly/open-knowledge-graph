---
id: population-growth-models
title: 'Population Growth Models: Exponential and Logistic'
domain: biology
course: ecology-and-evolution
prerequisites:
- id: population-ecology-intro
  type: hard
- id: exponential-functions-and-graphs
  type: soft
- id: differential-equations-intro-separable
  type: soft
- id: exponential-growth-and-decay
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- carrying-capacity
- population-regulation
- predator-prey-dynamics
tags:
- exponential-growth
- logistic-growth
- intrinsic-rate
- population-dynamics
stage: formal-systems
status: validated
---

# Population Growth Models: Exponential and Logistic

## Core Idea
Exponential growth (dN/dt = rN) models population growth when resources are unlimited, where r is the intrinsic rate of natural increase. Logistic growth (dN/dt = rN(K−N)/K) incorporates carrying capacity K — the maximum sustainable population size given resource constraints. As population size approaches K, growth rate declines due to density-dependent limitations. Real populations rarely exhibit pure logistic growth; oscillations, time lags, and overshooting are common.

## How It's Best Learned
Graph both models and compare J-shaped (exponential) vs. S-shaped (logistic) curves. Solve differential equations at various values of N relative to K. Use bacterial growth or yeast fermentation data as empirical examples before moving to complex wildlife data.

## Common Misconceptions
- Carrying capacity K is not fixed — it changes with environmental conditions.
- Logistic growth does not predict that populations stabilize exactly at K; real populations fluctuate around K.
- A high r does not always mean rapid growth to K — time lags can cause cycles or chaos.

## Questions

```yaml
- question: "A population currently at N = K/2 is growing logistically. At what population size is the instantaneous growth rate dN/dt at its maximum?"
  type: multiple-choice
  options:
    - "N = 0 (growth is fastest when the population is smallest)"
    - "N = K/4"
    - "N = K/2 (the population is already at the maximum growth rate)"
    - "N = K (growth is fastest just before the ceiling)"
  answer: 2
  explanation: "The logistic growth rate dN/dt = rN(K−N)/K is a quadratic function of N with a maximum at N = K/2. At this midpoint, N is large enough to contribute many births but (K−N)/K is still large enough that density-dependent limitation hasn't strongly kicked in. Below K/2, growth is limited by low N; above K/2, it is limited by resource scarcity. The population in this question is already at its peak growth rate."

- question: "Once a logistically growing population reaches carrying capacity K, it will stabilize exactly at K and remain there."
  type: true-false
  answer: false
  explanation: "The logistic equation predicts that dN/dt = 0 at N = K, making K a theoretical equilibrium. But real populations overshoot K due to time lags between resource depletion and reduced reproduction, then undershoot as mortality catches up. Environmental stochasticity (variable rainfall, disease outbreaks) also continuously shifts the effective K. Real populations fluctuate around K rather than settling at it."

- question: "Why does exponential growth (dN/dt = rN) eventually become an unrealistic model for real biological populations?"
  type: short-answer
  answer: "Exponential growth assumes unlimited resources — that every individual always finds food, space, and mates. In reality, as population density increases, resources become limiting, competition intensifies, and disease spreads more easily. These density-dependent factors cause birth rates to fall and death rates to rise, slowing growth below the exponential rate. No environment has truly unlimited resources."
  explanation: "The exponential model captures the biology accurately only at low densities when resources genuinely aren't limiting — early bacterial colonization, introduced species before competitors arrive. As density rises, density-dependent regulation kicks in, and the logistic model's (K−N)/K term captures this deceleration. The switch from J-shaped to S-shaped growth reflects the shift from resource-unlimited to resource-limited conditions."
```

## Explainer

Population growth models translate a simple biological question — how does population size change over time? — into mathematical form. The two foundational models, exponential and logistic, represent a progression from an idealized world to a more realistic one.

**Exponential growth** starts from a single observation: each individual in a population contributes to producing new individuals at rate r (the intrinsic rate of natural increase, equal to birth rate minus death rate). If N is population size, then dN/dt = rN. This produces a J-shaped curve — growth accelerates as N grows because there are more individuals contributing offspring. The solution is N(t) = N₀eʳᵗ, the same exponential function you encountered in algebra. Exponential growth is realistic when resources are genuinely unlimited: a few bacteria introduced to a fresh flask of nutrients, or a small introduced species population with no predators. But no environment is unlimited indefinitely.

**Logistic growth** modifies the exponential model by adding a density-dependent brake: dN/dt = rN(K−N)/K. The term (K−N)/K is the fraction of carrying capacity not yet used. When N is small, this term is close to 1 and growth is nearly exponential. As N approaches K, the term shrinks toward 0, and growth slows. At N = K, growth stops entirely. This produces an S-shaped (sigmoidal) curve. The carrying capacity K is not a biological constant — it represents the maximum population the environment can sustain given current resource availability, and it shifts with drought, habitat loss, or resource addition.

A key insight from the logistic model is that maximum population growth rate occurs at N = K/2, not at N ≈ 0. This counterintuitive result has real management implications: fish populations harvested down to K/2 can actually recover fastest, which is why K/2 is the theoretical maximum sustainable yield in fisheries management.

Real populations rarely behave as cleanly as either model predicts. Time lags — the delay between resource depletion and reduced reproduction — can cause populations to overshoot K before crashing back. With a high r and a significant time lag, populations can enter limit cycles (oscillating perpetually) or even chaotic dynamics. These complications don't invalidate the logistic model; they reveal that it is a first approximation from which richer models are built by adding species interactions (predation, competition) and environmental stochasticity.

## Notes
