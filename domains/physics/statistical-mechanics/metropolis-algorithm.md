---
id: metropolis-algorithm
title: The Metropolis Algorithm
domain: physics
course: statistical-mechanics
prerequisites:
- id: monte-carlo-statistical-mechanics
  type: hard
- id: canonical-ensemble
  type: soft
tags:
- metropolis
- markov-chain
- detailed-balance
stage: advanced
status: draft
---

# The Metropolis Algorithm

## Core Idea
The Metropolis algorithm constructs a Markov chain that samples from the canonical ensemble. Proposed moves are accepted with probability min(1, exp(-ΔE/kT)). Detailed balance is satisfied, ensuring the stationary distribution is the Boltzmann distribution. The algorithm is simple, scalable, and has become standard for simulating classical statistical systems.

## Explainer

The core problem of statistical mechanics is computing thermal averages: ⟨A⟩ = Σ A(s) e^{−E(s)/kT} / Z over all microstates s. For a system with N spins, the number of microstates is 2^N — roughly 10^{300} for a modest N = 1000. Exact enumeration is hopeless. What you need is a way to *sample* microstates with probability proportional to their Boltzmann weight e^{−E/kT}, so that ⟨A⟩ ≈ (1/M) Σ A(sᵢ) over your sampled states. The **Metropolis algorithm**, invented in 1953 at Los Alamos, is a remarkably simple procedure that accomplishes exactly this without ever computing the partition function Z.

The algorithm works as follows. Start from any microstate s. **Propose** a small random change — flip one spin, move one particle. Compute the energy difference ΔE = E(s_new) − E(s_old). If ΔE ≤ 0, the new state has lower energy and is more probable: **accept** it unconditionally. If ΔE > 0, the new state is less probable by a factor e^{−ΔE/kT}: accept it with probability e^{−ΔE/kT} (draw a uniform random number r ∈ [0,1]; accept if r < e^{−ΔE/kT}). Repeat millions of times. This is the **acceptance rule**: min(1, e^{−ΔE/kT}).

The algorithm works because it satisfies **detailed balance**: the rate of transitions from state s to state s′ equals the rate of the reverse transition. Formally, P(s)·A(s→s′) = P(s′)·A(s′→s), where P(s) ∝ e^{−E(s)/kT} is the Boltzmann weight and A is the acceptance probability. You can verify this: A(s→s′) = min(1, e^{−ΔE/kT}) and A(s′→s) = min(1, e^{+ΔE/kT}) = min(1, e^{ΔE/kT}). Plugging in, e^{−E(s)/kT} · min(1, e^{−ΔE/kT}) = e^{−E(s)/kT} · min(1, e^{(E(s)−E(s′))/kT}) = e^{−E(s′)/kT} · min(1, e^{(E(s′)−E(s))/kT}) = e^{−E(s′)/kT} · min(1, e^{−ΔE_reverse/kT}). Detailed balance with an ergodic proposal scheme guarantees that the Markov chain's **stationary distribution is exactly the Boltzmann distribution** — not an approximation to it.

In practice, the Metropolis algorithm requires an **equilibration period** before averages are meaningful: the chain must forget its initial state and reach the typical high-probability configurations. After equilibration, successive samples are still correlated — only after a correlation time τ are they approximately independent. You typically collect M samples spaced by several τ to estimate ⟨A⟩ with statistical error ∝ 1/√M. The computational cost scales with system size only as O(N) per sweep (not exponentially), which is why Metropolis Monte Carlo remains the workhorse of classical statistical mechanics simulations even after 70 years.
