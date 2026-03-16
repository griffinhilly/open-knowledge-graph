---
id: stationary-distributions
title: Stationary Distributions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: markov-chains
  type: hard
- id: convergence-in-distribution
  type: soft
builds-toward:
- martingales-introduction
tags:
- stationary-distributions
- markov-chains
- probability
stage: formal-systems
status: draft
---

# Stationary Distributions

## Core Idea
A probability distribution π is stationary for a Markov chain with transition kernel P if π = πP, or equivalently ∫π(dx)P(x, A) = π(A) for all measurable A. For irreducible aperiodic chains, the distribution converges to a unique stationary distribution. Stationary distributions characterize long-run behavior.

## Explainer

From your study of Markov chains, you know the chain's state at each step depends only on the current state (the Markov property), and the transition matrix P describes how probability flows between states. If you start in state i, you are in state j after one step with probability P_{ij}. If you start with a distribution π₀ over states (a row vector), then after one step the distribution is π₀P, after two steps it is π₀P², and so on. A **stationary distribution** π is one that doesn't change: πP = π. If you start in a stationary distribution, you stay there forever.

The stationary distribution is a fixed point of the map π ↦ πP. In matrix terms, π is a left eigenvector of P with eigenvalue 1. Since every row of P sums to 1 (each state transitions somewhere), it is guaranteed that 1 is an eigenvalue — so a stationary distribution always exists (for finite chains). The interesting question is whether it is *unique* and whether the chain *converges* to it from any starting distribution. For a **finite, irreducible** (every state reachable from every other) and **aperiodic** (no cyclic trapping) chain, the answer to both is yes. This is the fundamental convergence theorem: P^n_{ij} → π_j as n → ∞, regardless of the starting state i.

A powerful sufficient condition for finding stationary distributions is **detailed balance**: π_i P_{ij} = π_j P_{ji} for all pairs i, j. This says the flow of probability from i to j equals the flow from j to i — a microscopic equilibrium. Any distribution satisfying detailed balance is automatically stationary (summing over j on both sides gives πP = π). Detailed balance is easier to verify than the full stationary equation and is the foundation for Markov Chain Monte Carlo (MCMC) algorithms, where you *design* a transition kernel whose stationary distribution is a target distribution you want to sample from.

For chains with infinitely many states (continuous state spaces), the story is more subtle — existence requires additional conditions, and convergence may be much slower. But the core intuition persists: the stationary distribution is the long-run fraction of time spent in each state, the "equilibrium" that the chain approaches. If you run a Markov chain long enough (past its **mixing time**), any sample from it looks approximately like a draw from π. This is the insight that makes Markov chains practical: if direct sampling from a distribution is hard, you can often construct a chain with that distribution as its stationary distribution and sample by simulating the chain.
