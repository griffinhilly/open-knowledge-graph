---
id: continuous-time-markov-chains
title: Continuous-Time Markov Chains
domain: mathematics
course: stochastic-processes
prerequisites:
- id: markov-chains
  type: hard
- id: poisson-processes
  type: hard
- id: differential-equations-intro
  type: soft
tags:
- ctmc
- generator-matrix
- transition-rates
- exponential-holding-times
stage: expert
status: validated
---

# Continuous-Time Markov Chains

## Core Idea
A continuous-time Markov chain (CTMC) is a Markov process on a countable state space where the process holds in each state for an Exponential(qᵢ) time, then jumps to state j with probability qᵢⱼ/qᵢ. The generator matrix Q (with off-diagonal entries qᵢⱼ ≥ 0 and rows summing to zero) encodes the dynamics. The forward equation dp/dt = pQ and backward equation dp/dt = Qp govern the evolution of transition probabilities, and the stationary distribution π satisfies πQ = 0.

## Questions

```yaml
- question: "In a CTMC, the holding time in state i is Exponential with rate qᵢ = Σ_{j≠i} qᵢⱼ. Why must the holding time be exponential for the Markov property to hold in continuous time?"
  type: multiple-choice
  options:
    - "Because the exponential distribution is the only continuous distribution with the memoryless property — P(T > t+s | T > t) = P(T > s)"
    - "Because the exponential distribution has the smallest variance among positive distributions, ensuring stability"
    - "Because the generator matrix requires positive off-diagonal entries, which forces exponential holding times"
    - "Any distribution would work; the exponential is chosen for mathematical convenience"
  answer: 0
  explanation: "The Markov property requires that the future depends only on the current state, not on how long the process has been in that state. If the holding time were non-exponential (say, uniformly distributed), then knowing the process has been in state i for time s would give information about the remaining holding time — violating the Markov property. The memoryless property of the exponential distribution ensures that 'time already spent' is irrelevant, making the current state a sufficient summary. This is the fundamental reason CTMCs must have exponential holding times."

- question: "The generator matrix Q of a CTMC has the property that each row sums to zero: Σⱼ qᵢⱼ = 0 for all i. This is analogous to what property of the transition matrix P in discrete-time Markov chains?"
  type: multiple-choice
  options:
    - "Each row of P sums to 1 (rows are probability distributions) — the zero row sums of Q reflect the fact that Q generates the rate of change, not the distribution itself"
    - "P is symmetric — the zero row sums enforce reversibility"
    - "P has eigenvalue 1 — the zero row sums ensure Q has eigenvalue 0"
    - "Both A and C are correct"
  answer: 3
  explanation: "The transition matrix P = e^{Qt} must have rows summing to 1 (it's a stochastic matrix). This requires Q to have rows summing to 0: the diagonal entry qᵢᵢ = -Σ_{j≠i} qᵢⱼ is the negative total exit rate. Equivalently, Q1 = 0 (the vector of ones is in the null space), which means 0 is an eigenvalue of Q — analogous to 1 being an eigenvalue of P. The relationship P(t) = e^{Qt} connects the discrete snapshot (transition probabilities over time t) to the continuous dynamics (instantaneous rates)."

- question: "A two-state CTMC has states {0,1} with transition rates q₀₁ = α and q₁₀ = β. Find the stationary distribution."
  type: short-answer
  answer: "The stationary distribution π = (π₀, π₁) satisfies πQ = 0 and π₀ + π₁ = 1. The generator Q has q₀₁ = α, q₁₀ = β, q₀₀ = -α, q₁₁ = -β. The equation π₀(-α) + π₁β = 0 gives π₀α = π₁β, so π₀/π₁ = β/α. With normalization: π₀ = β/(α+β) and π₁ = α/(α+β). The process spends time in each state proportional to the reciprocal of its exit rate — the state with slower exit rate (lower transition rate out) has higher stationary probability."
  explanation: "This is the continuous-time analogue of the discrete-time two-state chain. The stationary distribution depends on the ratio of transition rates, not their absolute magnitudes. Doubling both α and β speeds up the process but doesn't change the long-run fraction of time spent in each state. The absolute rates control the mixing time (how fast the process approaches stationarity), while the ratios control the stationary distribution."
```

## Explainer

A **continuous-time Markov chain** (CTMC) extends discrete-time Markov chains to continuous time. The process lives on a countable state space S and evolves by holding in the current state i for a random Exponential(qᵢ) time, then jumping to a new state j ≠ i with probability qᵢⱼ/qᵢ, where qᵢ = Σ_{j≠i} qᵢⱼ is the total exit rate. The exponential holding time is not a choice but a necessity: the memoryless property of the exponential is the only way to ensure the Markov property holds in continuous time.

The dynamics are encoded in the **generator matrix** (or Q-matrix) Q, where the off-diagonal entry qᵢⱼ ≥ 0 is the rate of transitioning from i to j, and the diagonal entry qᵢᵢ = -Σ_{j≠i} qᵢⱼ makes each row sum to zero. The transition probability matrix P(t) = e^{Qt} satisfies the **Kolmogorov equations**: forward dP/dt = P(t)Q and backward dP/dt = QP(t). For finite state spaces, these are systems of linear ODEs with the matrix exponential as the solution. The generator Q is the continuous-time analogue of the transition matrix P - I from discrete time: it describes instantaneous rates rather than one-step probabilities.

The **stationary distribution** π satisfies πQ = 0 with Σπᵢ = 1 — the continuous-time analogue of πP = π. For irreducible CTMCs on finite state spaces, a unique stationary distribution always exists. For birth-death processes (where transitions occur only between adjacent states), the stationary distribution has a product-form solution: πₙ = π₀ · (λ₀λ₁...λₙ₋₁)/(μ₁μ₂...μₙ), where λᵢ are birth rates and μᵢ are death rates. This is the foundation of queuing theory (M/M/1, M/M/c, and related queues) and population dynamics.

CTMCs are connected to both discrete-time chains and diffusion processes. The **embedded chain** Yₙ (the sequence of states visited, ignoring holding times) is a discrete-time Markov chain with transition matrix pᵢⱼ = qᵢⱼ/qᵢ for j ≠ i. The **uniformization** technique converts a CTMC into a discrete-time chain by embedding it in a Poisson process with rate q ≥ max qᵢ: the chain jumps at every Poisson event, possibly staying in the same state. In the other direction, when the state space is taken to the continuum and transition rates scale appropriately, CTMCs converge to diffusion processes — the Kolmogorov forward equation for CTMCs becomes the Fokker-Planck equation for diffusions.
