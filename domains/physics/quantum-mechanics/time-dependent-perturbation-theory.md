---
id: time-dependent-perturbation-theory
title: Time-Dependent Perturbation Theory
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-independent-perturbation-theory
  type: hard
- id: differential-equations-intro
  type: hard
- id: degenerate-perturbation-theory
  type: soft
builds-toward:
- fermi-golden-rule
tags:
- perturbation-theory
- time-dependent
stage: advanced
status: validated
---
# Time-Dependent Perturbation Theory

## Core Idea
Time-varying perturbations H'(t) cause state evolution; coefficients expand as c_n(t) ≈ c_n⁽⁰⟩ − (i/ℏ) ∫₀ᵗ dt' ⟨n|H'(t')|m⟩ e^{iω_{nm}t'} c_m⁽⁰⟩.

## Questions

```yaml
- question: "A quantum system starts in energy eigenstate |m⟩. A time-varying perturbation H'(t) = V₀ cos(ωt) is applied. The probability of transitioning to state |n⟩ is largest when which condition holds?"
  type: multiple-choice
  options:
    - "The perturbation amplitude V₀ is very large, regardless of frequency"
    - "The matrix element ⟨n|H'|m⟩ is non-zero AND the perturbation frequency ω is close to the Bohr frequency ω_{nm} = (E_n − E_m)/ℏ"
    - "The perturbation frequency ω is much larger than the Bohr frequency ω_{nm}"
    - "The system has remained in state |m⟩ for a long time before the perturbation is applied"
  answer: 1
  explanation: "Two conditions are needed for large transition probability: (1) a non-zero matrix element ⟨n|H'|m⟩ coupling the initial and final states, and (2) resonance — ω ≈ ω_{nm}. At resonance, the oscillating phase factor e^{i(ω_{nm} − ω)t'} in the transition amplitude integral becomes slowly varying and the integral accumulates coherently over time, giving transition probability growing as t². Off-resonance, the integrand oscillates rapidly and averages nearly to zero. Option A misses the resonance condition; large amplitude alone is insufficient."

- question: "In first-order time-dependent perturbation theory, what physically happens when the perturbation frequency is far from resonance (ω ≪ ω_{nm})?"
  type: multiple-choice
  options:
    - "The transition probability grows linearly with time"
    - "The system undergoes an instantaneous transition to state |n⟩"
    - "The oscillating phase factor in the transition amplitude causes the integrand to average nearly to zero, producing negligible transition probability"
    - "The perturbation shifts the energy levels rather than inducing transitions"
  answer: 2
  explanation: "The transition amplitude involves the integral ∫₀ᵗ ⟨n|H'(t')|m⟩ e^{i(ω_{nm} − ω)t'} dt'. When ω is far from ω_{nm}, the phase factor e^{i(ω_{nm} − ω)t'} oscillates rapidly and the positive and negative contributions nearly cancel — the integral stays small regardless of how long the perturbation acts. This is why radio waves don't drive optical transitions and vice versa: frequency matching (energy conservation) is required for coherent accumulation of transition amplitude."

- question: "Time-dependent perturbation theory addresses the same fundamental question as time-independent perturbation theory — finding corrected energy levels — but for Hamiltonians that vary with time."
  type: true-false
  answer: false
  explanation: "These two theories address fundamentally different questions. Time-independent perturbation theory finds corrected energy eigenvalues and eigenstates when a static perturbation modifies a known Hamiltonian. Time-dependent perturbation theory asks: given a system initially in one eigenstate of H₀, what is the probability of finding it in a *different* eigenstate after a time-varying perturbation acts? The second is a question about transitions between states, not corrections to energy levels."

- question: "At exact resonance (ω = ω_{nm}), the first-order transition probability grows with time because the phase factor in the transition amplitude integral becomes slowly varying, allowing coherent accumulation."
  type: true-false
  answer: true
  explanation: "At resonance, ω_{nm} − ω = 0, so e^{i(ω_{nm} − ω)t'} = 1 — the integrand is constant rather than oscillating. The integral grows linearly with t, making the transition probability grow as t² (|amplitude|²). This coherent accumulation is the mathematical signature of resonance, and it is the mechanism behind stimulated absorption and emission, NMR spin flipping, and all coherent quantum drives. The t² growth is only an approximation valid at short times; at longer times the first-order approximation breaks down."

- question: "Explain why resonance — the match between perturbation frequency and Bohr frequency — is essential for large transition probabilities in time-dependent perturbation theory."
  type: short-answer
  answer: "The transition amplitude involves integrating the matrix element times an oscillating phase factor e^{i(ω_{nm} − ω)t'}. When ω ≠ ω_{nm}, this phase oscillates rapidly and the positive and negative contributions cancel, keeping the amplitude near zero no matter how long the perturbation acts. When ω ≈ ω_{nm}, the phase factor is nearly constant and the integral grows linearly with time — coherent accumulation. The transition probability (amplitude squared) grows as t². Physically, resonance corresponds to the perturbation delivering energy quanta that match the level spacing, satisfying energy conservation for the transition."
  explanation: "This is the quantum mechanical foundation of spectroscopy and coherent control: only perturbations tuned to the right frequency drive transitions. The resonance condition is essentially energy conservation expressed in the time-domain through phase coherence."
```

## Explainer

In **time-independent perturbation theory** (your prerequisite), the Hamiltonian is H = H₀ + λH', where H' is constant. The goal is to find corrected energy eigenvalues and eigenstates. Time-dependent perturbation theory addresses a fundamentally different question: given a system that *starts* in an energy eigenstate of H₀, what is the probability of finding it in a *different* eigenstate after a time-varying perturbation H'(t) acts for a while? This is a question about **transitions**, not corrections.

The setup is to write the evolving state as |ψ(t)⟩ = Σ_n c_n(t) e^{−iE_n t/ℏ} |n⟩, where the exponential factors carry the known free-evolution phase and the coefficients c_n(t) encode any genuine change in the state due to the perturbation. Substituting into the Schrödinger equation and expanding to first order in the perturbation gives the coefficient formula in the Core Idea: c_n(t) picks up a correction proportional to the **matrix element** ⟨n|H'(t')|m⟩ — how strongly the perturbation couples the initial state |m⟩ to the final state |n⟩ — multiplied by an oscillating phase factor e^{iω_{nm}t'}, where ω_{nm} = (E_n − E_m)/ℏ is the **Bohr frequency** between the two levels.

The physics of the oscillating phase factor is crucial. When the perturbation oscillates at frequency ω (as in a light field H' ∝ cos ωt), the integrand oscillates at frequency ω_{nm} − ω. Most of the time this is a rapidly oscillating integral that averages nearly to zero — the perturbation is off-resonance and very little probability flows into state |n⟩. But when ω ≈ ω_{nm}, the integrand becomes slowly varying and the integral grows linearly with time: the probability of transition grows as t². This is **resonance**, and it is the mechanism behind stimulated absorption and emission of radiation, NMR, and any coherent drive of a quantum system.

From the first-order formula, **Fermi's Golden Rule** (which this topic builds toward) emerges by considering continuous final states and integrating over time. The transition rate becomes constant and proportional to |⟨n|H'|m⟩|² times the density of states at the resonant energy. This rate — not the probability — is what appears in practical calculations of spectral linewidths, scattering cross-sections, and decay rates. Time-dependent perturbation theory is therefore the bridge between the static energy-level structure you learned in time-independent theory and the dynamical, observable processes — photon absorption, scattering events, particle decays — that actually make quantum systems experimentally accessible.
