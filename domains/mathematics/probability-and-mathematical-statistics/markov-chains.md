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
stage: formal-systems
status: draft
---

# Markov Chains

## Core Idea
A Markov chain {Xₙ} satisfies the Markov property: P(Xₙ₊₁ ∈ A | Xₙ = x, Xₙ₋₁, ..., X₀) = P(Xₙ₊₁ ∈ A | Xₙ = x). The transition kernel P(x, A) = P(Xₙ₊₁ ∈ A | Xₙ = x) fully specifies the chain. Markov chains are widely used to model random processes with limited dependence on history.

## Questions

```yaml
- question: "In a Markov chain, the probability of transitioning to set A at time n+1 depends on which of the following?"
  type: multiple-choice
  options: ["The full history X₀, X₁, ..., Xₙ", "Only the current state Xₙ", "Only the initial state X₀", "The time-averaged state over all past steps"]
  answer: 1
  explanation: "This is exactly the Markov property: P(Xₙ₊₁ ∈ A | X₀, ..., Xₙ) = P(Xₙ₊₁ ∈ A | Xₙ). The future distribution depends only on the present state, not the path taken to get there. This memoryless structure is what makes Markov chains analytically tractable."

- question: "A time-homogeneous Markov chain must have the same transition probabilities at every time step — this is part of the basic definition of a Markov chain."
  type: true-false
  answer: false
  explanation: "Time-homogeneity is an additional assumption, not part of the bare definition. A Markov chain is defined solely by the Markov property (independence of the future from the past given the present). Non-homogeneous chains, where P(Xₙ₊₁ ∈ A | Xₙ = x) may vary with n, satisfy the Markov property but not time-homogeneity. Most classical theorems (stationary distributions, ergodicity) add time-homogeneity as a separate assumption."

- question: "What information does the transition kernel P(x, A) encode, and why is it sufficient to fully specify a time-homogeneous Markov chain?"
  type: short-answer
  answer: "P(x, A) gives the probability of moving to set A in one step from state x. Because the Markov property guarantees the future depends only on the current state, composing this one-step kernel with itself (the Chapman-Kolmogorov equations) determines the n-step distribution for any n."
  explanation: "Multi-step probabilities satisfy P^n(x, A) = ∫ P^(n-1)(y, A) P(x, dy). For countable state spaces this is matrix multiplication Pⁿ. The kernel contains everything needed because the Markov property collapses all history-dependence into the current state."
```

## Explainer

A stochastic process is a sequence of random variables indexed by time: X₀, X₁, X₂, ... In general, predicting Xₙ₊₁ might require knowledge of the entire history X₀, ..., Xₙ — an unwieldy amount of information that grows without bound. A Markov chain is the simplest and most important class of stochastic processes, defined by one restriction: the conditional distribution of Xₙ₊₁ given the entire history depends only on the current state Xₙ. Formally, P(Xₙ₊₁ ∈ A | X₀, ..., Xₙ) = P(Xₙ₊₁ ∈ A | Xₙ) almost surely. The past is irrelevant once you know the present.

This memoryless structure connects directly to your prerequisite on conditional expectation. The Markov property is a statement about conditional distributions: conditioning on the full past σ-algebra σ(X₀, ..., Xₙ) gives the same result as conditioning on the current state σ(Xₙ). The independence ideas from σ-algebra theory make this precise — the future is conditionally independent of the remote past given the present. This collapsing of history into a single state variable is what makes Markov chains analytically tractable: everything about the future is encoded in where you are now.

The transition kernel P(x, A) = P(Xₙ₊₁ ∈ A | Xₙ = x) is the central object of the theory. For each fixed x, P(x, ·) is a probability measure on the state space; for each measurable set A, P(·, A) is a measurable function. For countable state spaces, the kernel reduces to a transition matrix Pᵢⱼ = P(Xₙ₊₁ = j | Xₙ = i), and n-step transition probabilities are just the matrix power Pⁿ. For general state spaces, the n-step kernel is defined by the Chapman-Kolmogorov equations: Pⁿ(x, A) = ∫ Pⁿ⁻¹(y, A) P(x, dy).

Time-homogeneity — the assumption that P(x, A) does not depend on the time index n — is a separate condition that is often imposed but not part of the bare definition. Most classical results assume it: with a fixed transition kernel, the long-run behavior is determined by the spectral properties of the transition operator. A stationary distribution π satisfies π(A) = ∫ P(x, A) π(dx) — it is a fixed point of the dynamics. Whether such a distribution exists and is unique (and whether the chain converges to it from any starting point) are the central questions of Markov chain ergodic theory, which you will explore when you study stationary distributions.

The two topics that build on this — stationary distributions and martingales — represent the two main directions of Markov chain theory. Stationary distributions answer the long-run question: where does the chain spend its time? Martingales answer a different question about processes with conserved conditional expectations, and many natural functions of Markov chains (hitting times, optional stopping) are martingales. Markov chains are the gateway to all of modern stochastic processes, appearing in queuing theory, statistical physics, Bayesian computation (MCMC), and reinforcement learning.
