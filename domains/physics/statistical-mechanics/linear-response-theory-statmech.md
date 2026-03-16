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

## Explainer

From the canonical ensemble, you know how to calculate equilibrium averages using the partition function Z = Tr(e^(−βH)). But equilibrium averages only tell you the state with no external perturbation. What happens when you gently poke a system — apply a small magnetic field, a weak electric field, or a slight pressure variation — and ask how the system responds? **Linear response theory** answers this by exploiting the fact that for weak enough perturbations, the response is proportional to the perturbation, regardless of the underlying complexity of the system.

The central setup is this: add a small perturbation H' = −h(t)·A to the Hamiltonian, where h(t) is a time-dependent external field and A is the conjugate observable (for a magnetic system, h is the field and A is the magnetization operator). The induced change in the expectation value of B at time t is then ⟨ΔB(t)⟩ = ∫ χ_BA(t − t') h(t') dt'. This is a convolution, and **χ_BA(t − t')** is the **response function** or **retarded Green's function** — it encodes how the system's response at time t depends on the perturbation applied at all earlier times t'. The response is causal (no response before the perturbation) and linear in h.

The profound result is the **Kubo formula**: χ_BA(t) = iθ(t)⟨[B(t), A(0)]⟩₀/ℏ, where the expectation value is taken in the *unperturbed* equilibrium state and θ(t) is the step function enforcing causality. This says that the response to a weak external perturbation is entirely determined by the spontaneous fluctuations of the system in equilibrium. You never need to solve a perturbed problem — you just compute correlators in the unperturbed ensemble. This is the statistical mechanics version of the fluctuation-dissipation idea: a system that fluctuates easily also responds easily to external forcing.

In practice, the Fourier transform χ(ω) captures the frequency-dependent response. The imaginary part Im[χ(ω)] measures dissipation — how much energy is absorbed from a field oscillating at frequency ω. The real part gives the reactive (dispersive) response. This framework unifies many seemingly different phenomena: electrical conductivity (response of current to electric field), magnetic susceptibility (response of magnetization to magnetic field), viscosity (response of stress to velocity gradients), and compressibility — all are response functions computable from equilibrium correlators via the Kubo formula.
