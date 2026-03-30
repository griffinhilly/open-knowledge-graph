---
id: s-matrix-scattering-amplitudes
title: S-Matrix and Scattering Amplitudes
domain: physics
course: quantum-field-theory
prerequisites:
- id: feynman-diagrams-systematic
  type: hard
- id: fock-space-particle-interpretation
  type: hard
tags:
- s-matrix
- scattering
- amplitudes
stage: expert
status: validated
---

# S-Matrix and Scattering Amplitudes

## Core Idea
The S-matrix (scattering matrix) maps initial states of incoming particles to final states of outgoing particles. Its matrix elements encode all observable scattering information. The S-matrix is decomposed as S = 1 + iT, where T contains the non-trivial scattering amplitude M related to physical cross sections and decay rates.

## Questions

```yaml
- question: "The S-matrix is written as S = 1 + iT. What does the '1' represent, and why must it be separated from the scattering amplitude T?"
  type: multiple-choice
  options:
    - "The 1 represents the contribution from single-particle exchange"
    - "The 1 represents the case where particles pass through each other without interacting — it must be subtracted because cross sections measure deviations from free propagation, not the free propagation itself"
    - "The 1 is a normalization factor required by unitarity"
    - "The 1 represents the vacuum energy contribution"
  answer: 1
  explanation: "If particles do not interact, the final state is identical to the initial state: S = 1 (the identity operator on Fock space). The interesting physics is in the deviation from this, encoded in iT. The matrix element <f|iT|i> = i(2pi)^4 delta^4(p_f - p_i) M_{fi} contains the scattering amplitude M (also called the invariant amplitude or matrix element), where the delta function enforces overall energy-momentum conservation. Physical observables like cross sections depend on |M|^2, not on S directly."

- question: "Unitarity of the S-matrix (S-dagger S = 1) implies the optical theorem, which relates the imaginary part of the forward scattering amplitude to the total cross section. What is the physical content of this relation?"
  type: multiple-choice
  options:
    - "It says that the probability of scattering forward equals the probability of scattering backward"
    - "It says that the total probability of all possible outcomes (elastic + inelastic) must equal 1 — probability is conserved, and any loss from the forward beam must go into some scattering channel"
    - "It says that the S-matrix must be diagonal in the momentum basis"
    - "It says that virtual particles contribute as much as real particles"
  answer: 1
  explanation: "The optical theorem is a direct consequence of probability conservation (unitarity). It states: Im M(forward) = 2E p_cm sigma_total. The imaginary part of the forward amplitude accounts for the depletion of the beam due to all possible scattering processes. If the total cross section is large, the forward amplitude must have a correspondingly large imaginary part to account for the probability that flows into other channels. This provides a powerful consistency check on calculations and connects seemingly different quantities."

- question: "The LSZ (Lehmann-Symanzik-Zimmermann) reduction formula provides the rigorous connection between the S-matrix elements and the time-ordered correlation functions of the interacting field theory."
  type: true-false
  answer: true
  explanation: "The LSZ formula states that S-matrix elements are obtained by taking the Fourier transform of the time-ordered Green's functions, amputating the external propagators (removing the poles corresponding to the external on-shell particles), and multiplying by appropriate wave function renormalization factors. This is the formal justification for the Feynman diagram approach: you compute correlation functions using Feynman rules, then extract the S-matrix elements via LSZ. Without LSZ, the connection between the field-theoretic correlation functions and the observable scattering amplitudes would be an unproven assumption."

- question: "Explain why the S-matrix, rather than the Hamiltonian or the field operators, is considered the fundamental observable quantity in relativistic quantum field theory."
  type: short-answer
  answer: "In relativistic QFT, particles are created and destroyed, so the notion of 'the state of the system at time t' is complicated — the number of particles can change. What is operationally measurable is the outcome of scattering experiments: you prepare particles with definite momenta in the far past, let them interact, and measure what comes out in the far future. The S-matrix encodes exactly this: the probability amplitude for going from any initial state to any final state. It is Lorentz invariant, unitary (probability-conserving), and directly connected to measurable cross sections and decay rates. The field operators and Hamiltonian are intermediate tools used to compute S-matrix elements, but the S-matrix itself is the bridge to experiment."
  explanation: "This perspective, championed by Heisenberg and later by the S-matrix program of the 1960s, emphasizes that the fundamental data of particle physics are scattering amplitudes. Modern approaches like the amplitudes program and on-shell methods take this further, computing S-matrix elements directly without reference to fields or Lagrangians."
```

## Explainer

The **S-matrix** is the central object connecting quantum field theory to experiment. In a scattering experiment, you prepare an initial state |i> of incoming particles with definite momenta long before the interaction, and you measure the final state |f> of outgoing particles long after. The S-matrix element <f|S|i> gives the probability amplitude for this transition, and the probability is |<f|S|i>|^2. Every measurement in particle physics -- every cross section, branching ratio, and decay rate -- is extracted from S-matrix elements.

The S-matrix is decomposed as S = 1 + iT, where the identity represents the trivial case of no interaction (particles pass through without scattering). The T-matrix encodes the non-trivial scattering. For a specific process, the matrix element is <f|iT|i> = i(2pi)^4 delta^4(p_i - p_f) M_{fi}, where the delta function enforces total energy-momentum conservation and M is the **invariant amplitude** (or Feynman amplitude). The Feynman diagram expansion computes M order by order in the coupling constant: each diagram at a given order contributes a term to M.

Two fundamental properties of the S-matrix constrain all of physics. **Unitarity** (S-dagger S = 1) is the statement that total probability is conserved: the probabilities of all possible final states must sum to 1. This leads to the **optical theorem**, which relates the imaginary part of the forward scattering amplitude to the total cross section, and to cutting rules (Cutkosky rules) that relate loop diagrams to products of tree-level diagrams. **Lorentz invariance** requires that S-matrix elements are the same in all inertial frames, which constrains the form of the amplitude M.

The formal connection between S-matrix elements and the field-theoretic correlation functions is provided by the **LSZ reduction formula**. It shows that S-matrix elements are obtained from time-ordered Green's functions by going on-shell (setting the external momenta to satisfy the mass-shell condition p^2 = m^2) and amputating external propagators. This justifies the Feynman diagram approach: you compute the amputated, connected Green's function using Feynman rules, evaluate it with on-shell external momenta, and the result is the scattering amplitude M. The LSZ formula also introduces wave function renormalization factors that account for the difference between the bare fields in the Lagrangian and the physical particle states.
