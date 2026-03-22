---
id: linear-response-theory-statmech
title: Linear Response Theory and Susceptibilities
domain: physics
course: statistical-mechanics
prerequisites:
- id: canonical-ensemble
  type: hard
- id: order-parameter-phase-transition
  type: soft
builds-toward:
- fluctuation-dissipation-theorem-general
tags:
- linear-response
- susceptibility
- kubo-formula
stage: advanced
status: draft
---

# Linear Response Theory and Susceptibilities

## Core Idea
When a weak external field is applied to a system in equilibrium, the response is proportional to the field (linear response) for small fields. The proportionality constant is the susceptibility χ, which measures the system's tendency to reorder. The Kubo formula expresses χ in terms of equilibrium correlation functions, unifying dynamics and equilibrium statistical mechanics.

## Questions

```yaml
- question: "A physicist wants to calculate how a material's magnetization responds to a weak oscillating magnetic field. According to the Kubo formula, what is the most direct way to compute this response?"
  type: multiple-choice
  options:
    - "Calculate the equilibrium magnetization-magnetization correlation function in the unperturbed system"
    - "Solve the Schrödinger equation for the perturbed Hamiltonian H − hA"
    - "Measure the magnetization in the presence of the field and divide by field strength"
    - "Expand the partition function in powers of h and keep the first-order term"
  answer: 0
  explanation: "The Kubo formula χ_BA(t) = iθ(t)⟨[B(t), A(0)]⟩₀/ℏ says the response function is an equilibrium correlator in the unperturbed system. You never need to solve the perturbed problem — the fluctuations of the system at equilibrium fully determine how it will respond to a weak external perturbation. This is the profound insight of linear response theory."

- question: "For a system's frequency-dependent susceptibility χ(ω), what does the imaginary part Im[χ(ω)] physically represent?"
  type: multiple-choice
  options:
    - "The energy dissipated (absorbed) from an oscillating field at frequency ω"
    - "The reactive (dispersive) response — the in-phase part of the system's reaction"
    - "The equilibrium fluctuation amplitude at frequency ω"
    - "The phase shift between the applied field and the system's response"
  answer: 0
  explanation: "Im[χ(ω)] measures dissipation — how much energy is absorbed per cycle from a field oscillating at frequency ω. The real part Re[χ(ω)] gives the reactive (dispersive) response, which is in phase with the field. This split between dissipative and reactive response is analogous to the resistance and reactance in an electrical circuit."

- question: "A system with large spontaneous fluctuations in magnetization (even without any applied field) will tend to have a large magnetic susceptibility."
  type: true-false
  answer: true
  explanation: "True. This is the core message of the fluctuation-dissipation connection embedded in the Kubo formula. A system that fluctuates easily in equilibrium is precisely one that can be easily pushed into a new state by a small external perturbation. Mathematically, susceptibility is proportional to the integral of the equilibrium correlation function, so large fluctuations mean large susceptibility."

- question: "To use the Kubo formula to calculate a system's linear response, you must first solve the dynamics of the perturbed Hamiltonian H + H'."
  type: true-false
  answer: false
  explanation: "False. This is the wrong approach that linear response theory supersedes. The Kubo formula expresses the response function entirely in terms of equilibrium expectation values in the unperturbed system — ⟨[B(t), A(0)]⟩₀ uses the unperturbed equilibrium state. The entire point is that you do not need to solve the perturbed problem; equilibrium correlators contain all the information about the linear response."

- question: "Why is the Kubo formula considered a unifying result in statistical mechanics? What does it reveal about the relationship between equilibrium and non-equilibrium behavior?"
  type: short-answer
  answer: "The Kubo formula shows that a system's response to any weak external perturbation is completely determined by its equilibrium fluctuations. This means apparently non-equilibrium quantities — electrical conductivity, magnetic susceptibility, viscosity — are all accessible from equilibrium calculations alone. Equilibrium and linear non-equilibrium behavior are not separate regimes requiring different theories; they are two faces of the same underlying physics, connected by the spontaneous fluctuations of the system."
  explanation: "Before Kubo's formula, computing transport and response coefficients seemed to require solving non-equilibrium problems. The formula reveals this is unnecessary for the linear regime: the retarded Green's function (response) equals the equilibrium commutator correlator, connecting dynamics to thermodynamics. This unifies conductivity, susceptibility, viscosity, and compressibility as instances of the same idea: a system that fluctuates easily at equilibrium responds easily to perturbations."
```

## Explainer

From the canonical ensemble, you know how to calculate equilibrium averages using the partition function Z = Tr(e^(−βH)). But equilibrium averages only tell you the state with no external perturbation. What happens when you gently poke a system — apply a small magnetic field, a weak electric field, or a slight pressure variation — and ask how the system responds? **Linear response theory** answers this by exploiting the fact that for weak enough perturbations, the response is proportional to the perturbation, regardless of the underlying complexity of the system.

The central setup is this: add a small perturbation H' = −h(t)·A to the Hamiltonian, where h(t) is a time-dependent external field and A is the conjugate observable (for a magnetic system, h is the field and A is the magnetization operator). The induced change in the expectation value of B at time t is then ⟨ΔB(t)⟩ = ∫ χ_BA(t − t') h(t') dt'. This is a convolution, and **χ_BA(t − t')** is the **response function** or **retarded Green's function** — it encodes how the system's response at time t depends on the perturbation applied at all earlier times t'. The response is causal (no response before the perturbation) and linear in h.

The profound result is the **Kubo formula**: χ_BA(t) = iθ(t)⟨[B(t), A(0)]⟩₀/ℏ, where the expectation value is taken in the *unperturbed* equilibrium state and θ(t) is the step function enforcing causality. This says that the response to a weak external perturbation is entirely determined by the spontaneous fluctuations of the system in equilibrium. You never need to solve a perturbed problem — you just compute correlators in the unperturbed ensemble. This is the statistical mechanics version of the fluctuation-dissipation idea: a system that fluctuates easily also responds easily to external forcing.

In practice, the Fourier transform χ(ω) captures the frequency-dependent response. The imaginary part Im[χ(ω)] measures dissipation — how much energy is absorbed from a field oscillating at frequency ω. The real part gives the reactive (dispersive) response. This framework unifies many seemingly different phenomena: electrical conductivity (response of current to electric field), magnetic susceptibility (response of magnetization to magnetic field), viscosity (response of stress to velocity gradients), and compressibility — all are response functions computable from equilibrium correlators via the Kubo formula.
