---
id: time-correlation-functions
title: Time-Correlation Functions and Relaxation
domain: physics
course: statistical-mechanics
prerequisites:
- id: two-point-correlation-functions
  type: hard
- id: ensemble-theory-fundamentals
  type: hard
builds-toward:
- green-kubo-formula
- response-functions-definition
tags:
- dynamics
- correlations
- relaxation
stage: expert
status: validated
---

# Time-Correlation Functions and Relaxation

## Core Idea
Time-correlation functions C(t) = ⟨A(t)A(0)⟩ measure how observables decorrelate in time for an equilibrium system. They characterize the timescale of fluctuations, relax to zero for ergodic systems, and provide access to dynamical properties like diffusion coefficients and viscosity through the fluctuation-dissipation theorem.

## Questions

```yaml
- question: "A liquid has a large initial velocity autocorrelation function C(0) but it decays extremely rapidly — faster than any other liquid you've measured. A student claims this means the liquid must have a large diffusion coefficient. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — C(0) sets the scale of the diffusion coefficient directly"
    - "No — the diffusion coefficient is the time integral ∫C(t)dt, so a large but rapidly decaying C(t) integrates to a small area and yields a small D"
    - "Yes — C(0) = kT/m by equipartition, and this ratio equals D"
    - "No — because C(t) decays to zero in ergodic systems, D must always be zero"
  answer: 1
  explanation: "The Green-Kubo relation D = (1/3) ∫₀^∞ ⟨v(t)·v(0)⟩ dt makes clear that what matters is the area under the time-correlation function, not its initial value. A large C(0) with a short relaxation time τ integrates to a small D. Transport is determined by both the fluctuation magnitude and the fluctuation lifetime together — neither alone is sufficient."

- question: "Which statement best describes the behavior of a time-correlation function C(t) = ⟨A(t)A(0)⟩ for an ergodic equilibrium system?"
  type: multiple-choice
  options:
    - "C(t) oscillates indefinitely because the system is in thermal equilibrium"
    - "C(t) grows over time as the system explores more of phase space"
    - "C(t) decays to zero as t → ∞ because the system explores all accessible phase space, erasing memory of the initial value"
    - "C(t) is constant for equilibrium systems because statistical properties don't change in time"
  answer: 2
  explanation: "Ergodicity means the system explores all regions of phase space over long times. Once many collisions have occurred, the current value of A(t) is statistically independent of the initial value A(0), so ⟨A(t)A(0)⟩ → ⟨A⟩² = 0 for zero-mean observables. The decay timescale encodes how long memory persists — the relaxation time τ. This is precisely what makes the time integral well-defined and finite."

- question: "The diffusion coefficient D can be computed entirely from equilibrium dynamics by integrating the equilibrium velocity autocorrelation function — a property known as a Green-Kubo relation."
  type: true-false
  answer: true
  explanation: "This is the central result connecting equilibrium fluctuations to non-equilibrium transport. D = (1/3) ∫₀^∞ ⟨v(t)·v(0)⟩ dt expresses a non-equilibrium property (how fast a diffusing particle spreads) purely in terms of equilibrium fluctuations. The fluctuation-dissipation theorem guarantees this connection: the same thermal fluctuations that randomize velocities at equilibrium also determine how energy is dissipated when the system is perturbed."

- question: "A time-correlation function C(t) that starts at a larger initial value C(0) generally corresponds to a larger transport coefficient."
  type: true-false
  answer: false
  explanation: "C(0) and the transport coefficient are not directly proportional. The transport coefficient is the time integral of C(t), which depends on both C(0) and the relaxation timescale τ. A system with a small C(0) but a very long τ (slow decay) can have a much larger diffusion coefficient than one with a large C(0) that decays almost instantly. The interplay between fluctuation magnitude and fluctuation lifetime determines transport, not either quantity alone."

- question: "Why can equilibrium time-correlation functions reveal non-equilibrium transport properties like diffusion coefficients and viscosity?"
  type: short-answer
  answer: "The fluctuation-dissipation theorem establishes that the same microscopic dynamics that govern equilibrium thermal fluctuations also determine how the system responds to and dissipates external perturbations. At equilibrium, molecules undergo constant thermal motion — velocities fluctuate and correlate over timescales set by collisions. These equilibrium fluctuations are statistically equivalent to the relaxation dynamics seen when the system is driven slightly out of equilibrium. Green-Kubo relations formalize this: they express each transport coefficient as the time integral of the relevant equilibrium correlation function, so measuring equilibrium dynamics gives complete information about non-equilibrium transport."
  explanation: "This is one of the deepest results in statistical mechanics. Non-equilibrium coefficients like D and η describe how the system relaxes when perturbed, but that relaxation is governed by the same molecular interactions that produce equilibrium fluctuations. You don't need to actually perturb the system — the equilibrium dynamics already contain all the information, accessible through time-correlation functions."
```

## Explainer

From your study of two-point correlation functions, you already understand how spatial correlations ⟨A(r)A(0)⟩ measure the degree to which fluctuations at one position are correlated with fluctuations at another. Time-correlation functions are the temporal analog: C(t) = ⟨A(t)A(0)⟩ measures how strongly the value of an observable A at time t is correlated with its value at time 0. For a system in thermal equilibrium, this average is taken over the equilibrium ensemble, and by time-translation invariance, C depends only on the time difference t, not the absolute time.

The intuition is straightforward with a concrete example. Consider the velocity of a single molecule in a gas: A = vx(t). At t = 0, you know exactly what vx is (say, 3 m/s). At t = ε (a tiny instant later), the molecule hasn't been hit by anything yet, so vx is still close to 3 m/s: C(ε) ≈ C(0). After many collisions — a time of order the **collision time** τ_c — the molecule's velocity is randomized. It might now be anything; its current velocity bears no memory of the initial value. So C(t) → 0 as t → ∞ for an **ergodic** system (one that explores all accessible phase space). The correlation function thus decays from C(0) = ⟨vx²⟩ = kT/m (by equipartition) to zero on the timescale τ_c. The shape of the decay — exponential, power-law, oscillatory — encodes the relaxation physics.

The power of time-correlation functions is the **Green-Kubo relations**, which connect equilibrium fluctuations to transport coefficients. For example, the **diffusion coefficient** D = (1/3) ∫₀^∞ ⟨v(t)·v(0)⟩ dt is the time integral of the velocity autocorrelation function. This is remarkable: D is a non-equilibrium transport property (how fast a particle spreads in a diffusing cloud), but it can be computed entirely from equilibrium dynamics. Similarly, shear viscosity is the time integral of the stress-stress correlation function. This bridge between equilibrium fluctuations and non-equilibrium response is the **fluctuation-dissipation theorem** in action.

From your ensemble theory background, you know that equilibrium systems fluctuate around their mean values, with the fluctuation magnitude set by thermodynamic quantities. The fluctuation-dissipation theorem generalizes this: the same thermal fluctuations that cause equilibrium noise also determine how the system dissipates energy when perturbed from equilibrium. A system that fluctuates a lot (large C(0)) will also respond strongly to perturbations and have large transport coefficients, unless the fluctuations are very short-lived. The interplay between fluctuation magnitude C(0) and relaxation timescale τ determines transport. Time-correlation functions are the central mathematical object that makes this connection precise, and computing them — whether analytically, via mode-coupling theory, or numerically via molecular dynamics simulation — is a core activity in modern statistical physics.
