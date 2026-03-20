---
id: time-dependent-perturbation-theory
title: Time-Dependent Perturbation Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-independent-perturbation-theory
  type: hard
- id: differential-equations
  type: hard
builds-toward:
- fermi-golden-rule
tags:
- perturbation-theory
- time-dependent
stage: advanced
status: draft
---

# Time-Dependent Perturbation Theory

## Core Idea
Time-varying perturbations H'(t) cause state evolution; coefficients expand as c_n(t) ≈ c_n⁽⁰⟩ − (i/ℏ) ∫₀ᵗ dt' ⟨n|H'(t')|m⟩ e^{iω_{nm}t'} c_m⁽⁰⟩.

## Explainer

In **time-independent perturbation theory** (your prerequisite), the Hamiltonian is H = H₀ + λH', where H' is constant. The goal is to find corrected energy eigenvalues and eigenstates. Time-dependent perturbation theory addresses a fundamentally different question: given a system that *starts* in an energy eigenstate of H₀, what is the probability of finding it in a *different* eigenstate after a time-varying perturbation H'(t) acts for a while? This is a question about **transitions**, not corrections.

The setup is to write the evolving state as |ψ(t)⟩ = Σ_n c_n(t) e^{−iE_n t/ℏ} |n⟩, where the exponential factors carry the known free-evolution phase and the coefficients c_n(t) encode any genuine change in the state due to the perturbation. Substituting into the Schrödinger equation and expanding to first order in the perturbation gives the coefficient formula in the Core Idea: c_n(t) picks up a correction proportional to the **matrix element** ⟨n|H'(t')|m⟩ — how strongly the perturbation couples the initial state |m⟩ to the final state |n⟩ — multiplied by an oscillating phase factor e^{iω_{nm}t'}, where ω_{nm} = (E_n − E_m)/ℏ is the **Bohr frequency** between the two levels.

The physics of the oscillating phase factor is crucial. When the perturbation oscillates at frequency ω (as in a light field H' ∝ cos ωt), the integrand oscillates at frequency ω_{nm} − ω. Most of the time this is a rapidly oscillating integral that averages nearly to zero — the perturbation is off-resonance and very little probability flows into state |n⟩. But when ω ≈ ω_{nm}, the integrand becomes slowly varying and the integral grows linearly with time: the probability of transition grows as t². This is **resonance**, and it is the mechanism behind stimulated absorption and emission of radiation, NMR, and any coherent drive of a quantum system.

From the first-order formula, **Fermi's Golden Rule** (which this topic builds toward) emerges by considering continuous final states and integrating over time. The transition rate becomes constant and proportional to |⟨n|H'|m⟩|² times the density of states at the resonant energy. This rate — not the probability — is what appears in practical calculations of spectral linewidths, scattering cross-sections, and decay rates. Time-dependent perturbation theory is therefore the bridge between the static energy-level structure you learned in time-independent theory and the dynamical, observable processes — photon absorption, scattering events, particle decays — that actually make quantum systems experimentally accessible.
