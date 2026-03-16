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
status: draft
---

# Convergence of Markov Chains

## Core Idea
An irreducible, aperiodic Markov chain converges in distribution to its stationary distribution π: P(X_n = j) → π(j). The convergence rate depends on the spectral gap (largest minus second-largest eigenvalue of P); larger gaps mean faster mixing. Convergence ensures MCMC samples approach the target distribution.

## Explainer

From stationary distributions, you know that a distribution π is stationary if πP = π — the chain, once started in π, stays in π forever. But that raises a practical question: if the chain starts somewhere far from π, does it eventually converge to π regardless of where it starts? And if so, how fast? These questions are the subject of Markov chain convergence theory.

Two structural conditions on the transition matrix P jointly guarantee convergence. **Irreducibility** means every state can reach every other state in some finite number of steps — the chain cannot be trapped in a subset of states. **Aperiodicity** means no state forces the chain to return only at regular intervals (e.g., always at even steps). A chain that oscillates between two groups of states every other step is periodic and fails to converge; it oscillates around the stationary distribution rather than settling into it. When a finite Markov chain is irreducible and aperiodic, the Perron-Frobenius theorem guarantees that the transition matrix P has a unique stationary distribution π and that P^n converges to the matrix with π repeated in every row — meaning every starting state produces the same long-run distribution.

The rate of convergence is governed by the **spectral gap**: the difference between the largest eigenvalue of P (which is always 1 for a stochastic matrix) and the second-largest eigenvalue in absolute value. A spectral gap close to 1 means the chain mixes rapidly — within a few steps the distribution is close to π. A gap close to 0 means slow mixing — the chain might take exponentially many steps to forget its starting state. You can visualize this with a lazy random walk: if the chain almost always stays in place and rarely moves, the spectral gap is small and convergence is glacially slow. A well-connected chain with many transitions per step has a larger spectral gap and mixes faster.

This theory underpins **Markov Chain Monte Carlo (MCMC)**: methods like the Metropolis-Hastings algorithm and Gibbs sampling construct a Markov chain whose stationary distribution equals a target distribution (often a Bayesian posterior) that is otherwise hard to sample from directly. Convergence theory tells you that after a **burn-in** period — long enough for the starting point to be forgotten — subsequent samples are approximately drawn from the target. In practice, diagnosing whether a chain has converged is a major challenge: you cannot observe convergence directly, only measure symptoms like the effective sample size (related to the spectral gap) and trace plot mixing. Understanding the theoretical guarantee — irreducibility, aperiodicity, and spectral gap — is what lets you reason carefully about when MCMC output can and cannot be trusted.
