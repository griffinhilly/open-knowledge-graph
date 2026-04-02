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
stage: expert
status: validated
---

# Stationary Distributions

## Core Idea
A probability distribution π is stationary for a Markov chain with transition kernel P if π = πP, or equivalently ∫π(dx)P(x, A) = π(A) for all measurable A. For irreducible aperiodic chains, the distribution converges to a unique stationary distribution. Stationary distributions characterize long-run behavior.

## Questions

```yaml
- question: "For a finite, irreducible, aperiodic Markov chain with stationary distribution π, you run the chain for a very long time starting from state i. As the number of steps n → ∞, the probability of being in state j approaches:"
  type: multiple-choice
  options:
    - "P_{ij}, the one-step transition probability from i to j"
    - "π_j, the stationary probability of state j, regardless of the starting state i"
    - "1/k where k is the total number of states, since the chain visits all states equally"
    - "The probability depends on which state i you started in — there is no universal limit"
  answer: 1
  explanation: "The fundamental convergence theorem for Markov chains: for a finite irreducible aperiodic chain, P^n_{ij} → π_j as n → ∞, for every starting state i. The chain 'forgets' its initial state and converges to the same limiting distribution π regardless of where it started. This is not obvious — it requires both irreducibility (so every state is reachable) and aperiodicity (so there is no cyclic trapping). The stationary distribution is not just a fixed point but the universal attractor of the dynamics."

- question: "A Markov chain satisfies detailed balance: π_i P_{ij} = π_j P_{ji} for all states i and j. What can you conclude?"
  type: multiple-choice
  options:
    - "The chain is irreducible and will converge to π from any starting distribution"
    - "π is a stationary distribution for the chain, but detailed balance alone does not guarantee irreducibility or convergence"
    - "The chain must be reversible and have uniform stationary distribution"
    - "Detailed balance is equivalent to the chain being aperiodic"
  answer: 1
  explanation: "Detailed balance implies stationarity: summing π_i P_{ij} = π_j P_{ji} over all i gives (πP)_j = π_j, so π is stationary. However, detailed balance says nothing about irreducibility (whether all states communicate) or aperiodicity (whether the chain lacks periodic cycles). A chain could satisfy detailed balance while being decomposable into separate communicating classes, each with its own stationary distribution. Detailed balance is a sufficient condition for finding stationary distributions, not a guarantee of convergence to a unique one."

- question: "If you start a Markov chain in its stationary distribution π, the distribution of the chain's state at every future time step remains π."
  type: true-false
  answer: true
  explanation: "True — this is precisely what 'stationary' means. A distribution π is stationary if πP = π: applying the transition matrix once leaves π unchanged. Therefore if the chain starts with distribution π₀ = π, then after one step the distribution is π₀P = πP = π, and by induction it remains π at every step. The chain in stationarity is in a kind of probabilistic equilibrium: probabilities of being in each state do not change over time, even though individual realizations of the chain continue to transition between states."

- question: "A finite irreducible Markov chain can have two distinct stationary distributions if its transition probabilities are chosen carefully."
  type: true-false
  answer: false
  explanation: "False. For a finite irreducible chain, the stationary distribution is unique. Irreducibility means all states communicate (every state is reachable from every other), which ensures the chain cannot be decomposed into independent subchains each with its own stationary distribution. The stationary distribution for an irreducible chain satisfies π_j = 1/⟨T_j⟩ (the reciprocal of the mean return time to state j), which uniquely determines π. Adding aperiodicity ensures convergence to this unique stationary distribution, but uniqueness holds for irreducible chains regardless of periodicity."

- question: "Explain why the existence of a stationary distribution makes Markov Chain Monte Carlo (MCMC) a practical algorithm for sampling from complex probability distributions."
  type: short-answer
  answer: "MCMC works by constructing a Markov chain whose stationary distribution is exactly the target distribution you want to sample from (e.g., a Bayesian posterior). By the convergence theorem, the chain will eventually produce samples that look like draws from that target distribution, regardless of where it started. Even if direct sampling from the target is computationally intractable, you can often design a transition kernel satisfying detailed balance with respect to the target — ensuring stationarity — and then sample by simulating the chain past its mixing time."
  explanation: "The key insight is the reversal of the usual relationship: instead of starting with a chain and finding its stationary distribution, MCMC starts with a desired distribution and constructs a chain with that distribution as its stationary distribution. Detailed balance provides the design criterion: any transition kernel satisfying π_i P_{ij} = π_j P_{ji} has π as its stationary distribution. Algorithms like Metropolis-Hastings do exactly this, accepting or rejecting proposed moves in a way that guarantees detailed balance is satisfied. The only requirement for validity is that the chain is irreducible and aperiodic, so it actually converges."
```

## Explainer

From your study of Markov chains, you know the chain's state at each step depends only on the current state (the Markov property), and the transition matrix P describes how probability flows between states. If you start in state i, you are in state j after one step with probability P_{ij}. If you start with a distribution π₀ over states (a row vector), then after one step the distribution is π₀P, after two steps it is π₀P², and so on. A **stationary distribution** π is one that doesn't change: πP = π. If you start in a stationary distribution, you stay there forever.

The stationary distribution is a fixed point of the map π ↦ πP. In matrix terms, π is a left eigenvector of P with eigenvalue 1. Since every row of P sums to 1 (each state transitions somewhere), it is guaranteed that 1 is an eigenvalue — so a stationary distribution always exists (for finite chains). The interesting question is whether it is *unique* and whether the chain *converges* to it from any starting distribution. For a **finite, irreducible** (every state reachable from every other) and **aperiodic** (no cyclic trapping) chain, the answer to both is yes. This is the fundamental convergence theorem: P^n_{ij} → π_j as n → ∞, regardless of the starting state i.

A powerful sufficient condition for finding stationary distributions is **detailed balance**: π_i P_{ij} = π_j P_{ji} for all pairs i, j. This says the flow of probability from i to j equals the flow from j to i — a microscopic equilibrium. Any distribution satisfying detailed balance is automatically stationary (summing over j on both sides gives πP = π). Detailed balance is easier to verify than the full stationary equation and is the foundation for Markov Chain Monte Carlo (MCMC) algorithms, where you *design* a transition kernel whose stationary distribution is a target distribution you want to sample from.

For chains with infinitely many states (continuous state spaces), the story is more subtle — existence requires additional conditions, and convergence may be much slower. But the core intuition persists: the stationary distribution is the long-run fraction of time spent in each state, the "equilibrium" that the chain approaches. If you run a Markov chain long enough (past its **mixing time**), any sample from it looks approximately like a draw from π. This is the insight that makes Markov chains practical: if direct sampling from a distribution is hard, you can often construct a chain with that distribution as its stationary distribution and sample by simulating the chain.
