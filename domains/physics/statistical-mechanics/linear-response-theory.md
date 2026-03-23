---
id: linear-response-theory
title: Linear Response Theory
domain: physics
course: statistical-mechanics
prerequisites:
- id: fluctuation-dissipation-theorem
  type: hard
- id: canonical-ensemble
  type: soft
builds-toward:
- response-functions-susceptibilities
tags:
- response-function
- perturbation
- equilibrium
stage: expert
status: draft
---

# Linear Response Theory

## Core Idea
Linear response theory gives the response ⟨δA⟩ = χ_{AB} δB of an observable A to a small external perturbation δB as ⟨δA(t)⟩ = ∫ χ_{AB}(t−t') δB(t') dt'. The response function χ is given by the Kubo formula involving the equilibrium correlation of fluctuations, directly connecting the fluctuation-dissipation theorem to dynamics.

## Questions

```yaml
- question: "According to the Kubo formula, how is the linear response function χ_{AB}(t) calculated?"
  type: multiple-choice
  options:
    - "By solving the time-dependent Schrödinger equation for the full driven Hamiltonian H₀ − δB(t)B̂"
    - "By measuring the system's steady-state response to a constant field and dividing by field strength"
    - "From the equilibrium commutator ⟨[Â(t), B̂(0)]⟩₀ — computed in the unperturbed state, with no need to solve the driven problem"
    - "From the time-averaged fluctuations of A measured while the field δB is applied"
  answer: 2
  explanation: "The power of the Kubo formula is precisely that it eliminates the need to solve the driven problem. χ_{AB}(t) = −(i/ℏ)θ(t)⟨[Â(t), B̂(0)]⟩₀, where the expectation value is in the *unperturbed* equilibrium state. Compute this once and you have the response to any small perturbation. The Heaviside function θ(t) enforces causality: χ = 0 for t < 0 (no response before the perturbation). This is a dramatic simplification — equilibrium calculation gives all linear transport coefficients."

- question: "Why does the fluctuation-dissipation theorem imply that a material with large thermal fluctuations in magnetization will also respond strongly to an applied magnetic field?"
  type: multiple-choice
  options:
    - "Large fluctuations indicate the system is far from equilibrium, making it sensitive to small perturbations"
    - "The fluctuations and the response are driven by the same microscopic processes — modes that fluctuate strongly in equilibrium absorb strongly when driven at those frequencies"
    - "Large fluctuations imply weak restoring forces, so the system is easily displaced by external fields"
    - "Thermal fluctuations directly amplify applied fields through resonance at their natural frequency"
  answer: 1
  explanation: "The FDT identifies Im[χ(ω)] ∝ S(ω), the spectral density of equilibrium fluctuations of Â. A mode that fluctuates strongly in equilibrium (large S(ω)) also absorbs strongly when driven at that frequency (large imaginary part of χ). This is not a coincidence — it is the same microscopic dynamics in both cases. The processes responsible for thermal noise also carry driven dissipation. They are not separate phenomena but the same physics viewed from two angles."

- question: "The causality requirement — χ_{AB}(τ) = 0 for τ < 0 — implies mathematical constraints (Kramers-Kronig relations) linking the dispersive and absorptive parts of the susceptibility in frequency space."
  type: true-false
  answer: true
  explanation: "Causality is imposed by θ(t) in the Kubo formula: the response at time t depends only on the perturbation at earlier times t' < t. In the frequency domain, a function that is zero for negative times must satisfy Kramers-Kronig relations: the real part (dispersive, refractive) and imaginary part (absorptive, dissipative) of χ(ω) are related by Hilbert transforms. They are not independent. This is a rigorous consequence of causality alone, valid for any linear system."

- question: "Linear response theory provides exact results for any perturbation strength, as long as the perturbation is applied slowly (adiabatically)."
  type: true-false
  answer: false
  explanation: "Linear response is a small-perturbation approximation — the response is calculated to first order in δB. The validity condition is that the perturbation is *small* (δB small), not that it is applied slowly. For large perturbations, higher-order terms become significant and linear response fails regardless of how slowly the field is applied. Adiabatic switching is sometimes used to set up initial conditions, but it does not extend the regime of validity beyond small fields."

- question: "What is the key insight of linear response theory, and why does it make equilibrium calculations so powerful for understanding driven systems?"
  type: short-answer
  answer: "Linear response theory shows that for small perturbations, the full time-dependent response to any external field is completely determined by equilibrium properties — specifically, equilibrium time correlation functions via the Kubo formula. You never need to solve the complicated driven problem: one equilibrium calculation gives all linear transport coefficients (conductivity, susceptibility, diffusivity) for any small perturbation. The physical reason is that the microscopic dynamics producing equilibrium thermal fluctuations are identical to those carrying energy dissipation under a small external drive."
  explanation: "This unification is the framework's deepest achievement. Instead of solving electrical conduction, magnetic response, thermal transport, and diffusion as separate driven problems, all take the form of Kubo formulas — integrals of equilibrium time-correlation functions. The framework makes non-equilibrium transport a corollary of equilibrium statistical mechanics for the linear regime, which covers an enormous range of experimentally accessible conditions."
```

## Explainer

From the fluctuation-dissipation theorem, you know that the dissipative response of a system — how it absorbs energy from an external drive — is directly related to the spectrum of its equilibrium fluctuations. The same thermal noise that jiggles a resistor also determines its electrical resistance. Linear response theory provides the precise dynamical framework behind this statement: for any *small* perturbation, the system's full response — not just its steady-state value but its entire time history — is completely determined by equilibrium properties, computed once and reused for any perturbation.

The setup: the equilibrium Hamiltonian is H₀. A small time-dependent field δB(t) couples to observable B̂, adding −δB(t)B̂ to the Hamiltonian. First-order time-dependent perturbation theory gives ⟨δA(t)⟩ = ∫_{−∞}^{t} χ_{AB}(t − t') δB(t') dt'. This is a **convolution**: the current response depends on the entire history of the perturbation, weighted by the **response function** χ_{AB}(τ), which measures how strongly the system at time τ ago influences the present. The upper limit t (not +∞) enforces **causality**: χ_{AB}(τ) = 0 for τ < 0, meaning the response cannot precede its cause. In frequency space, causality imposes the **Kramers-Kronig relations**, linking the real (dispersive) and imaginary (absorptive) parts of the complex susceptibility χ(ω).

The **Kubo formula** is the central result: χ_{AB}(t) = −(i/ℏ)θ(t)⟨[Â(t), B̂(0)]⟩₀, where the expectation value is taken in the *unperturbed* equilibrium state and θ(t) is the Heaviside function enforcing causality. This means you never need to solve the driven problem: compute the commutator expectation in equilibrium, and you have the complete linear response to any small perturbation. The imaginary part of χ(ω) in frequency space gives the **dissipation spectrum** — how strongly the system absorbs at each frequency. The fluctuation-dissipation theorem then identifies Im[χ(ω)] ∝ S(ω), the **spectral density** of equilibrium fluctuations of Â. A mode that fluctuates strongly in equilibrium also absorbs strongly when driven — the same microscopic processes responsible for thermal noise also carry driven dissipation.

Linear response theory unifies an enormous range of transport phenomena. Electrical conductivity (the response of current density to an applied electric field), magnetic susceptibility (response of magnetization to an applied magnetic field), thermal conductivity (response of heat current to a temperature gradient), and the diffusion coefficient all take the form of Kubo formulas — integrals of equilibrium time-correlation functions. This is the foundation of modern non-equilibrium statistical mechanics: instead of solving complicated driven problems case by case, you extract all linear transport coefficients from a single equilibrium simulation or calculation. The framework breaks down when the perturbation is large enough to push the system into genuinely nonlinear territory, but for small fields it is exact.
