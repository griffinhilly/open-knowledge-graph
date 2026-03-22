---
id: fokker-planck-equation
title: Fokker-Planck Equation
domain: physics
course: statistical-mechanics
prerequisites:
- id: langevin-equation-stochastic
  type: hard
builds-toward:
- master-equation
tags:
- stochastic
- probability
- evolution
stage: advanced
status: draft
---

# Fokker-Planck Equation

## Core Idea
The Fokker-Planck equation describes how the probability distribution P(x,t) evolves under stochastic dynamics. Derived from the Langevin equation, it generalizes the diffusion equation to include drift due to external forces, and appears in many contexts from Brownian motion to population dynamics.

## Questions

```yaml
- question: "A Brownian particle is confined in a harmonic potential V = ½kx² and coupled to a thermal reservoir. After a long time, what does the Fokker-Planck equation predict for the stationary probability distribution P(x)?"
  type: multiple-choice
  options:
    - "A uniform distribution across all positions, since noise can push the particle anywhere"
    - "A delta function at x = 0, since the potential minimum attracts all trajectories"
    - "The Boltzmann distribution P_eq ∝ exp(−V/k_BT), a Gaussian centered at x = 0"
    - "No stationary distribution exists — thermal noise prevents the system from settling"
  answer: 2
  explanation: "The Fokker-Planck equation with harmonic drift A(x) = −kx/γ and thermal diffusion has a stationary solution where drift and diffusion balance: P_eq ∝ exp(−kx²/2k_BT) = exp(−V/k_BT). This is the Boltzmann distribution, confirming that stochastic dynamics with thermal noise correctly recovers equilibrium statistical mechanics."

- question: "What physical effect does the drift term −∂/∂x[A(x) P] represent in the Fokker-Planck equation?"
  type: multiple-choice
  options:
    - "Random spreading of the probability distribution due to thermal fluctuations"
    - "Deterministic flow of the probability density under a systematic external force"
    - "Decay of total probability over time as particles escape the system"
    - "Coupling between the velocity and position degrees of freedom"
  answer: 1
  explanation: "The drift term is a continuity equation: −∂/∂x[A(x) P] = −∇·(AP), describing how probability flows with the deterministic velocity field A(x). If all particles are pushed right by a force, the probability density shifts right. The diffusion term ∂²/∂x²[D P] separately handles the stochastic spreading."

- question: "The Fokker-Planck equation is a deterministic partial differential equation, even though it describes an inherently stochastic process."
  type: true-false
  answer: true
  explanation: "This is the core advantage of the Fokker-Planck approach. Although the underlying dynamics are random, the probability density P(x,t) evolves deterministically according to a PDE. This lets you apply PDE machinery (Green's functions, eigenfunction expansions, numerical solvers) to a problem that started as a stochastic one."

- question: "The Fokker-Planck equation and the Langevin equation describe the same stochastic system at the same level of description — they are just different notations for the same mathematical object."
  type: true-false
  answer: false
  explanation: "They describe the same physics but at different levels. The Langevin equation describes individual stochastic trajectories x(t), requiring noise terms and statistical averaging. The Fokker-Planck equation describes the probability density P(x,t) directly — a deterministic PDE. Deriving the Fokker-Planck from the Langevin requires computing moments of the displacement and taking a continuum limit."

- question: "A free Brownian particle starts at x = 0 at t = 0 (so P(x,0) = δ(x)) with no external force. Using the structure of the Fokker-Planck equation, describe qualitatively how P(x,t) evolves over time."
  type: short-answer
  answer: "With no external force, A = 0 and the drift term vanishes. The Fokker-Planck equation reduces to the diffusion equation ∂P/∂t = D ∂²P/∂x². Starting from a delta function at the origin, P(x,t) spreads into a Gaussian with mean 0 (no drift) and variance 2Dt growing linearly in time. The probability density stays symmetric and centered at x = 0 but broadens indefinitely."
  explanation: "The diffusion term spreads the distribution; without drift, the mean stays fixed at 0. The solution P(x,t) = (4πDt)^{−1/2} exp(−x²/4Dt) is the fundamental solution of the diffusion equation — a broadening Gaussian. This matches the physical picture of random-walk diffusion."
```

## Explainer

From the Langevin equation, you know how to describe a single stochastic trajectory: the velocity of a Brownian particle satisfies ṁv = −γv + η(t), where γ is friction and η(t) is white noise. But tracking individual trajectories is impractical when you want to know the distribution of outcomes — where a particle is likely to be at time t, given where it started. The **Fokker-Planck equation** describes the evolution of the probability density P(x, t) directly, without following individual trajectories.

The derivation proceeds by asking: how does P(x, t) change over a short time dt? Particles drift deterministically due to external forces, and they spread stochastically due to noise. Both effects can be captured in terms of the first and second moments of the displacement over dt: the **drift coefficient** A(x) = ⟨Δx⟩/dt and the **diffusion coefficient** D(x) = ⟨(Δx)²⟩/(2dt). The Fokker-Planck equation is then ∂P/∂t = −∂/∂x[A(x) P] + ∂²/∂x²[D(x) P]. The first term is a **continuity equation** for probability under drift — if all particles are pushed to the right by a force, the probability density shifts right. The second term is a **diffusion equation** — noise spreads the distribution.

Connecting back to Brownian motion: for a free particle in a fluid (no external force, A = 0, D = k_BT/γ by the fluctuation-dissipation theorem), the Fokker-Planck equation reduces to the ordinary diffusion equation, and an initially sharp distribution broadens as a Gaussian with variance 2Dt. Add a harmonic confining potential V = ½kx², and A(x) = −kx/γ; the distribution relaxes toward a stationary Gaussian centered at x = 0 — the Boltzmann equilibrium distribution P_eq ∝ exp(−V/k_BT). This illustrates a general result: the stationary solution of the Fokker-Planck equation with thermal noise is always the Boltzmann distribution, providing a direct link between stochastic dynamics and equilibrium statistical mechanics.

The Fokker-Planck equation is a **deterministic partial differential equation** for a probability density, even though it describes an inherently random process. This is its great advantage over the Langevin equation: you can use all the tools of PDEs — Green's functions, eigenfunction expansions, numerical methods — to compute distributions, mean first-passage times, escape rates, and correlation functions. Its reach extends far beyond physics: the Black-Scholes equation in finance, the Kolmogorov forward equation in probability theory, and models of neural firing rates and gene expression are all Fokker-Planck equations in disguise.
