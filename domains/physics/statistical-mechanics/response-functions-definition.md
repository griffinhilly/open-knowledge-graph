---
id: response-functions-definition
title: Response Functions and Linear Response
domain: physics
course: statistical-mechanics
prerequisites:
- id: time-correlation-functions
  type: hard
- id: linear-response-theory-statmech
  type: hard
builds-toward:
- green-kubo-formula
tags:
- response
- perturbation
- dynamics
stage: advanced
status: draft
---

# Response Functions and Linear Response

## Core Idea
Response functions describe how a system deviates from equilibrium when subjected to small external perturbations. Linear response theory states that observables respond linearly to weak driving forces, with the response function related to equilibrium fluctuations through the fluctuation-dissipation theorem.

## Questions

```yaml
- question: "A system at equilibrium shows large spontaneous fluctuations in its magnetization. According to linear response theory, what does this imply about the system's response to a small applied magnetic field?"
  type: multiple-choice
  options:
    - "Nothing — equilibrium fluctuations are unrelated to how the system responds to external fields"
    - "The system will show a large susceptibility, responding strongly to the applied field"
    - "The system will resist the applied field because the fluctuations saturate the response"
    - "The system needs to be driven out of equilibrium before its susceptibility can be measured"
  answer: 1
  explanation: "The fluctuation-dissipation theorem (FDT) directly connects equilibrium fluctuations to the response function. Large equilibrium fluctuations in magnetization indicate a large susceptibility — the system responds strongly to the same observable it fluctuates in. Option A is the common misconception: the Kubo formula shows that equilibrium fluctuations *are* the response, encoded in the time-correlation function. You don't need to apply a field to measure susceptibility — watching spontaneous fluctuations tells you everything."

- question: "Why can the linear response of a system to an external perturbation be computed entirely from an unperturbed equilibrium molecular dynamics simulation?"
  type: multiple-choice
  options:
    - "Because linear systems don't change when perturbed, so equilibrium and driven dynamics are identical"
    - "Because the Kubo formula shows the response function equals an equilibrium time-correlation function"
    - "Because thermal fluctuations in equilibrium are suppressed to zero, leaving only the driven response"
    - "Because the external field is too weak to affect the trajectories of individual particles"
  answer: 1
  explanation: "The Kubo formula, χ_{AB}(t) = (i/ℏ)θ(t)⟨[A(t),B(0)]⟩₀, expresses the response function as an equilibrium commutator expectation value. This means every linear response property — susceptibility, conductivity, viscosity — is encoded in fluctuations that occur spontaneously in equilibrium. The simulation never needs to apply any perturbation. Option A misunderstands linearity: linear response means the *output* is proportional to the input, not that the system is unchanged."

- question: "The imaginary part of the frequency-domain susceptibility χ''(ω) measures the energy stored (reactive response) in the system during periodic driving."
  type: true-false
  answer: false
  explanation: "This is a common sign confusion. χ''(ω) — the imaginary part — measures *dissipation*: how much energy is absorbed from the driving field per cycle and converted to heat. The real part χ'(ω) measures the in-phase reactive response (energy stored and returned). The FDT connects χ''(ω) directly to the power spectrum of equilibrium fluctuations: χ''(ω) ∝ S(ω)/T. A system that dissipates strongly at a frequency also fluctuates strongly at that frequency."

- question: "The response function χ(t − t') depends only on the time difference (t − t'), not on t and t' separately, because of time-translation invariance in equilibrium."
  type: true-false
  answer: true
  explanation: "At thermal equilibrium, there is no preferred moment in time — the statistical properties of the system don't depend on when you start the clock. This symmetry means the response to a perturbation at time t' depends only on how long ago that perturbation occurred (t − t'), not on the absolute times. This is what allows the convolution ⟨δA(t)⟩ = ∫χ(t−t')h(t')dt' to be written as a simple product χ̃(ω)h̃(ω) in Fourier space — a major simplification for periodic driving analysis."

- question: "Why is the fluctuation-dissipation theorem considered a profound result, rather than merely a convenient calculational shortcut? What does it reveal about the relationship between equilibrium and non-equilibrium physics?"
  type: short-answer
  answer: "The FDT reveals that equilibrium and linear non-equilibrium physics are not separate regimes — they are two views of the same microscopic dynamics. The same thermal collisions that produce random fluctuations in equilibrium also produce the friction and damping seen when the system is driven. Dissipation is not an 'extra' phenomenon requiring a separate theory; it is the microscopic noise that becomes visible at the macroscopic level. Quantitatively: χ''(ω) = (ω/2kT)S(ω), so measuring noise at equilibrium gives you the dissipation at that frequency. This means you can, in principle, predict the resistance of a resistor by measuring its thermal (Johnson) noise — without connecting it to any circuit."
  explanation: "The depth of the FDT lies in its unification: it abolishes the distinction between 'passive equilibrium physics' and 'active response to driving' in the linear regime. It also has practical implications — Green-Kubo relations let you compute transport coefficients (thermal conductivity, shear viscosity, diffusion coefficients) from equilibrium MD simulations, avoiding the need to simulate driven systems that are harder to control and interpret."
```

## Explainer

A **response function** answers the question: if I poke a system with a small external perturbation, how does it respond? The word "small" is key — small enough that the response is proportional to the perturbation, so that the relationship between cause and effect is linear. This linearity is not an approximation of last resort; it is the regime where equilibrium statistical mechanics makes clean, exact predictions. In the linear regime, the full response is encoded in equilibrium correlation functions that you can compute without ever applying the perturbation.

Concretely, suppose you apply a time-dependent field h(t) that couples to observable B in the Hamiltonian (i.e., H' = −h(t)B). The response of a different observable A is given by the linear response formula: ⟨δA(t)⟩ = ∫ χ_{AB}(t − t') h(t') dt', where χ_{AB}(t − t') is the **generalized susceptibility** or response function. The convolution structure reflects causality and time-translation invariance. The response at time t depends on the field at all past times t' < t, weighted by χ. In Fourier space this convolution becomes a simple product: δÃ(ω) = χ̃_{AB}(ω) h̃(ω), making frequency-domain analysis natural for periodic driving.

The deep result — due to Kubo — is that χ_{AB}(t) is entirely determined by **equilibrium time-correlation functions**. Specifically, χ_{AB}(t) = (i/ℏ) θ(t) ⟨[A(t), B(0)]⟩₀, where the expectation value is taken over the unperturbed equilibrium ensemble and θ(t) is the step function enforcing causality. This is the **Kubo formula**. It says you do not need to drive the system to measure its response — you can infer the entire linear response from fluctuations that spontaneously occur in thermal equilibrium. This is profound: the same thermal fluctuations that look like noise carry complete information about how the system will respond to external drives.

The imaginary part of the frequency-domain susceptibility χ''(ω) measures **dissipation** — how much energy the system absorbs from the driving field. The real part χ'(ω) measures the in-phase reactive response. The **fluctuation-dissipation theorem**, which you studied as a prerequisite, connects these: χ''(ω) is proportional to the power spectrum of equilibrium fluctuations S(ω) via χ''(ω) = (ω/2k_BT) S_{AB}(ω). Dissipation and fluctuations are two faces of the same microscopic dynamics. Familiar response functions — magnetic susceptibility, dielectric function, thermal conductivity, viscosity — are all special cases of this framework, and the Kubo formula provides the microscopic foundation for computing them all from equilibrium molecular dynamics.
