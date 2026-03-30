---
id: fermi-golden-rule
title: The Fermi Golden Rule
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-dependent-perturbation-theory
  type: hard
tags:
- fermi-golden-rule
- transition-rates
stage: expert
status: validated
---

# The Fermi Golden Rule

## Core Idea
Transition rate to continuum: Γ_{i→f} = (2π/ℏ) |⟨f|H'|i⟩|² ρ(E_f), where ρ(E_f) is the density of final states. Predicts absorption, emission, decay, and scattering rates.

## Questions

```yaml
- question: "A quantum system has a very large matrix element |⟨f|H'|i⟩|² coupling initial and final states, yet it transitions extremely slowly. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "The perturbation H' is too weak to drive transitions despite the large matrix element"
    - "The density of final states ρ(E_f) is very small — few states are available at the transition energy"
    - "The elapsed time is too short for the long-time limit of Fermi's Golden Rule to apply"
    - "Energy is not conserved in this transition, so the delta function suppresses the rate to zero"
  answer: 1
  explanation: "The Fermi Golden Rule rate Γ = (2π/ℏ)|⟨f|H'|i⟩|²ρ(E_f) has two independent factors: the matrix element measures coupling strength, and ρ(E_f) measures how many final states are energetically accessible. If ρ(E_f) is very small — as in a bandgap, a confined geometry, or a transition to a very narrow energy range — the rate is suppressed regardless of how strongly the perturbation couples the states. This is why spontaneous emission can be dramatically slowed by placing an atom in a photonic crystal that suppresses the photon density of states at the transition frequency."

- question: "The delta function δ(E_f − E_i) that appears in Fermi's Golden Rule enforces:"
  type: multiple-choice
  options:
    - "Momentum conservation — only final states with the same momentum as the initial state contribute"
    - "Energy conservation — only final states at exactly the initial energy are accessible"
    - "Normalization of the final-state wavefunction to unity"
    - "The long-wavelength approximation used to simplify the matrix element"
  answer: 1
  explanation: "The delta function arises from the long-time behavior of the sinc-squared factor in first-order perturbation theory: as t → ∞, [sin(Δωt/2)/(Δω/2)]² → 2πt δ(E_f − E_i). This picks out only transitions where E_f = E_i — exact energy conservation. The perturbation mediates a transition between states at the same energy; it does not supply energy to the system. Momentum conservation, if required, must come separately from the structure of the matrix element."

- question: "For transitions to a continuum of final states, Fermi's Golden Rule predicts a transition probability that grows linearly in time, corresponding to a constant transition rate."
  type: true-false
  answer: true
  explanation: "When final states form a continuum, summing over them converts the oscillating sinc-squared factor into 2πt δ(E_f − E_i), making total transition probability proportional to t. Dividing by t gives a constant rate Γ independent of time — the system decays at a steady rate, as observed in radioactive decay, spontaneous emission, and scattering. This is in contrast to transitions between two discrete levels, where probability oscillates (Rabi oscillations)."

- question: "Fermi's Golden Rule applies equally well to transitions between two isolated discrete energy levels and to transitions into a continuum of final states."
  type: true-false
  answer: false
  explanation: "Fermi's Golden Rule specifically requires a continuum of final states. For two discrete levels, transition probability oscillates periodically (Rabi oscillations) rather than growing linearly in time — there is no constant rate. The Golden Rule emerges only when final states are dense enough that the sinc-squared factor can be approximated as a delta function, which requires many closely spaced final states near the transition energy."

- question: "Explain why a quantum system transitioning to a single discrete final state shows oscillatory probability over time, while a system transitioning to a continuum shows a constant transition rate."
  type: short-answer
  answer: "For a transition to a single discrete level, P(t) ∝ sin²(Δωt/2) oscillates as the system coherently tunnels back and forth between initial and final states — there is no irreversible decay. For a continuum, each final state individually oscillates with its own Δω. When you sum over all final states, the oscillations from states with different energies cancel by destructive interference, except near Δω = 0 (energy conservation). The result is incoherent, irreversible growth linear in t — a true constant rate."
  explanation: "The physics is analogous to why a coherently driven two-level system Rabi-flops while a system coupled to a large reservoir decays irreversibly. The continuum provides the reservoir: phase information leaks into the many final states and cannot be recovered, converting coherent oscillation into incoherent decay."
```

## Explainer

From time-dependent perturbation theory, you learned how to compute the probability that a perturbation H' drives a quantum system from an initial state |i⟩ to a specific final state |f⟩. The result at first order is P_{i→f}(t) = (1/ℏ²)|⟨f|H'|i⟩|² × [sin(Δωt/2)/(Δω/2)]², where Δω = (E_f − E_i)/ℏ. For transitions between two discrete levels, this oscillates — the system tunnels back and forth. But in many physical situations, the final state is not a single discrete level; it is a continuum of states (photons in free space, scattered particles at various angles, electrons in a conduction band). The Fermi Golden Rule handles this case.

When final states form a continuum, we sum P_{i→f}(t) over all final states within an energy window and ask: how does total transition probability grow with time? The key mathematical step is recognizing that as t → ∞, the factor [sin(Δωt/2)/(Δω/2)]² becomes sharply peaked around Δω = 0 and approaches 2πt δ(E_f − E_i). The delta function enforces **energy conservation** — only final states at exactly the initial energy can be reached. Dividing by time gives a constant **transition rate**:

**Γ_{i→f} = (2π/ℏ) |⟨f|H'|i⟩|² ρ(E_f)**

where ρ(E_f) is the **density of final states** — the number of states per unit energy available at the transition energy E_f = E_i.

The formula has two factors, each with clear physical meaning. The **matrix element** |⟨f|H'|i⟩|² measures how strongly the perturbation couples the initial and final states — a transition that H' cannot drive has zero matrix element and zero rate. The **density of states** ρ(E_f) measures how many final states are available — even a strong coupling produces a slow rate if final states are scarce. Both factors must be large for a fast transition. This structure explains why an atom in free space emits photons at a rate that depends on both the atomic dipole moment (matrix element) and the photon density of states (which goes as ω²), giving the familiar ω³ dependence of spontaneous emission. It also underlies scattering cross sections in nuclear and particle physics through the Born approximation, and governs electron-phonon scattering rates that determine electrical resistivity in metals.
