---
id: markov-chains-convergence
title: Convergence of Markov Chains
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: stationary-distributions
  type: hard
- id: convergence-in-distribution
  type: soft
tags:
- markov-chains
- convergence
- mixing
stage: advanced
status: validated
---

# Convergence of Markov Chains

## Core Idea
An irreducible, aperiodic Markov chain converges in distribution to its stationary distribution π: P(X_n = j) → π(j). The convergence rate depends on the spectral gap (largest minus second-largest eigenvalue of P); larger gaps mean faster mixing. Convergence ensures MCMC samples approach the target distribution.

## Questions

```yaml
- question: "A Markov chain on five states has a unique stationary distribution π and is irreducible, but every state returns to itself only at even time steps. What happens as n → ∞?"
  type: multiple-choice
  options:
    - "P(X_n = j) → π(j) for all j, because a unique stationary distribution guarantees convergence"
    - "The chain oscillates and P^n does not converge, even though π is the unique stationary distribution"
    - "The chain converges because irreducibility is sufficient to guarantee convergence"
    - "The chain converges to π only if it starts in π"
  answer: 1
  explanation: "A periodic chain fails to converge even when a unique stationary distribution exists and the chain is irreducible. In this example the chain is bipartite — it alternates between two groups of states every step — so the distribution oscillates between two patterns rather than settling to π. Convergence to π requires both irreducibility AND aperiodicity. A unique stationary distribution guarantees there is a target to converge to, but without aperiodicity the chain never stops oscillating around that target."

- question: "Chain A has a spectral gap of 0.9 and chain B has a spectral gap of 0.05. Both are irreducible and aperiodic. What do these spectral gaps tell you about their practical behavior?"
  type: multiple-choice
  options:
    - "Chain A reaches stationarity much faster than chain B; chain B may require exponentially more steps to mix"
    - "Both chains converge at the same rate because both satisfy the convergence conditions"
    - "Chain B converges faster because a smaller spectral gap means more eigenvalues are contributing to the dynamics"
    - "The spectral gap only matters for continuous-time chains, not discrete-time"
  answer: 0
  explanation: "The spectral gap — the difference between the largest eigenvalue (1) and the second-largest in absolute value — directly controls the mixing time. Chain A's gap of 0.9 means the non-stationary components of the distribution decay by factor 0.1 per step, so the chain mixes in O(1/0.9) ≈ 1 steps relative to the gap scale. Chain B's gap of 0.05 means those components decay by 0.95 per step, requiring O(1/0.05) = 20 steps per e-fold of decay — mixing can take orders of magnitude longer. In MCMC practice, a near-zero spectral gap (slow mixing) is the main practical obstacle."

- question: "If a Markov chain has a unique stationary distribution, it will converge to that distribution from any starting state."
  type: true-false
  answer: false
  explanation: "False. Having a unique stationary distribution is necessary but not sufficient for convergence. A periodic chain has a unique stationary distribution but oscillates rather than converging (e.g., a chain that alternates A→B→A→B cycles has a unique stationary distribution but never settles). Similarly, a reducible chain may have multiple stationary distributions but even one that is unique won't guarantee convergence from all starts if the chain can get trapped in a subset of states. Both irreducibility and aperiodicity are required."

- question: "The burn-in period discarded at the start of an MCMC run corresponds to the time needed for the chain's distribution to approach stationarity from its arbitrary starting state."
  type: true-false
  answer: true
  explanation: "True. MCMC constructs a chain whose stationary distribution equals the target distribution, but if the chain starts far from stationarity, early samples are drawn from a distribution that still reflects the starting state rather than the target. Burn-in discards these early samples, keeping only those collected after the chain has had enough steps (relative to the mixing time) to forget its starting point. The required burn-in length depends on the spectral gap: chains with near-zero spectral gaps need very long burn-ins, which is a major practical challenge in Bayesian computation."

- question: "Why is aperiodicity required for a Markov chain to converge to its stationary distribution, even when the chain is irreducible and has a unique stationary distribution?"
  type: short-answer
  answer: "A periodic chain cycles through groups of states with a fixed period. Even if the long-run averages match π, the instantaneous distribution at time n oscillates depending on n mod d (where d is the period). The chain never 'settles' — at any given time step, only certain states are accessible. Aperiodicity breaks this cycling structure so that after enough steps, every state can be reached at every time, allowing the distribution to converge rather than oscillate."
  explanation: "Consider a two-state chain with transitions A→B and B→A only. This is irreducible (both states are reachable) and has a unique stationary distribution (0.5, 0.5). But starting in state A, at even times you're in A and at odd times you're in B — the distribution oscillates between (1,0) and (0,1) and never converges to (0.5, 0.5). Adding a small self-loop probability (lazy chain) immediately restores aperiodicity and convergence."
```

## Explainer

From stationary distributions, you know that a distribution π is stationary if πP = π — the chain, once started in π, stays in π forever. But that raises a practical question: if the chain starts somewhere far from π, does it eventually converge to π regardless of where it starts? And if so, how fast? These questions are the subject of Markov chain convergence theory.

Two structural conditions on the transition matrix P jointly guarantee convergence. **Irreducibility** means every state can reach every other state in some finite number of steps — the chain cannot be trapped in a subset of states. **Aperiodicity** means no state forces the chain to return only at regular intervals (e.g., always at even steps). A chain that oscillates between two groups of states every other step is periodic and fails to converge; it oscillates around the stationary distribution rather than settling into it. When a finite Markov chain is irreducible and aperiodic, the Perron-Frobenius theorem guarantees that the transition matrix P has a unique stationary distribution π and that P^n converges to the matrix with π repeated in every row — meaning every starting state produces the same long-run distribution.

The rate of convergence is governed by the **spectral gap**: the difference between the largest eigenvalue of P (which is always 1 for a stochastic matrix) and the second-largest eigenvalue in absolute value. A spectral gap close to 1 means the chain mixes rapidly — within a few steps the distribution is close to π. A gap close to 0 means slow mixing — the chain might take exponentially many steps to forget its starting state. You can visualize this with a lazy random walk: if the chain almost always stays in place and rarely moves, the spectral gap is small and convergence is glacially slow. A well-connected chain with many transitions per step has a larger spectral gap and mixes faster.

This theory underpins **Markov Chain Monte Carlo (MCMC)**: methods like the Metropolis-Hastings algorithm and Gibbs sampling construct a Markov chain whose stationary distribution equals a target distribution (often a Bayesian posterior) that is otherwise hard to sample from directly. Convergence theory tells you that after a **burn-in** period — long enough for the starting point to be forgotten — subsequent samples are approximately drawn from the target. In practice, diagnosing whether a chain has converged is a major challenge: you cannot observe convergence directly, only measure symptoms like the effective sample size (related to the spectral gap) and trace plot mixing. Understanding the theoretical guarantee — irreducibility, aperiodicity, and spectral gap — is what lets you reason carefully about when MCMC output can and cannot be trusted.
