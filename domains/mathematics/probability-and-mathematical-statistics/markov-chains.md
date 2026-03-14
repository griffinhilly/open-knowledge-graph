---
id: markov-chains
title: Markov Chains
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: independence-sigma-algebras
  type: hard
- id: conditional-expectation
  type: hard
builds-toward:
- stationary-distributions
- martingales-introduction
tags:
- markov-chains
- stochastic-processes
- probability
stage: abstract-reasoning
status: draft
---

# Markov Chains

## Core Idea
A Markov chain {Xₙ} satisfies the Markov property: P(Xₙ₊₁ ∈ A | Xₙ = x, Xₙ₋₁, ..., X₀) = P(Xₙ₊₁ ∈ A | Xₙ = x). The transition kernel P(x, A) = P(Xₙ₊₁ ∈ A | Xₙ = x) fully specifies the chain. Markov chains are widely used to model random processes with limited dependence on history.
