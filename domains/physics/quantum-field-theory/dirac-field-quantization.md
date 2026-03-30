---
id: dirac-field-quantization
title: Dirac Field Quantization
domain: physics
course: quantum-field-theory
prerequisites:
- id: dirac-equation
  type: hard
- id: fock-space-particle-interpretation
  type: hard
tags:
- dirac-field
- fermions
- anticommutation
stage: expert
status: validated
---

# Dirac Field Quantization

## Core Idea
Quantizing the Dirac field requires anticommutation relations (not commutation relations) for the creation and annihilation operators. This produces fermions obeying the Pauli exclusion principle and naturally yields both particles (electrons) and antiparticles (positrons) with opposite charge.

## Questions

```yaml
- question: "If you quantize the Dirac field using commutation relations (like a scalar field) instead of anticommutation relations, the resulting theory has a fatal problem. What is it?"
  type: multiple-choice
  options:
    - "The energy spectrum becomes continuous instead of discrete"
    - "The theory has no Lorentz invariance"
    - "The Hamiltonian is unbounded below — there is no ground state, and the theory is unstable"
    - "The propagator diverges for all momenta"
  answer: 2
  explanation: "The Dirac Hamiltonian has both positive and negative frequency solutions. If you use commutation relations, the negative-frequency modes contribute -E_p to the energy for each excitation. With bosonic statistics, you could put arbitrarily many quanta in these modes, driving the energy to negative infinity. Anticommutation relations solve this: the antiparticle creation operators (associated with negative-frequency solutions) contribute +E_p to the energy, and the Pauli exclusion principle prevents unlimited occupation. This is a deep connection between spin and statistics — spin-1/2 fields must be quantized with anticommutation relations for the theory to be stable."

- question: "The Dirac field operator psi(x) destroys a particle or creates an antiparticle; psi-bar(x) creates a particle or destroys an antiparticle. Why does a single field operator perform two seemingly different actions?"
  type: multiple-choice
  options:
    - "This is a mathematical artifact with no physical significance"
    - "Because the Dirac equation has both positive-frequency and negative-frequency solutions, and the field operator is a sum over both — positive-frequency components destroy particles, while negative-frequency components create antiparticles"
    - "Because particles and antiparticles are the same object moving in different directions in time"
    - "Because the field operator is not Hermitian"
  answer: 1
  explanation: "The Dirac field is expanded as psi(x) = sum_s integral [b_{p,s} u_s(p) e^{-ipx} + d-dagger_{p,s} v_s(p) e^{+ipx}] d^3p / (2pi)^3 (2E_p), where u_s and v_s are positive- and negative-frequency spinors. The operator b_{p,s} destroys an electron with momentum p and spin s; d-dagger_{p,s} creates a positron. Both are present because the Dirac equation requires both types of solutions for completeness. The field operator is the object that appears in the Lagrangian and in interaction vertices — its dual role is what makes charge-changing processes possible."

- question: "The quantized Dirac field has a vacuum with infinite negative energy (a filled Dirac sea of negative-energy states)."
  type: true-false
  answer: false
  explanation: "The Dirac sea was Dirac's original interpretation, in which all negative-energy states are filled and a 'hole' in the sea appears as a positron. Modern quantum field theory does not use the Dirac sea. Instead, anticommutation relations and the reinterpretation of negative-frequency modes as antiparticle creation operators ensure that the vacuum has zero energy (after normal ordering) and no particles. The positron is created by d-dagger, not by removing an electron from a filled sea. The two pictures give the same physical predictions, but the field-theoretic approach is cleaner and generalizes to all particle types."

- question: "Explain the role of the spin-statistics connection in the quantization of the Dirac field: why must spin-1/2 fields be quantized with anticommutators?"
  type: short-answer
  answer: "The spin-statistics theorem states that fields with half-integer spin must be quantized with anticommutation relations, and fields with integer spin with commutation relations. For the Dirac field specifically, the argument is that the Hamiltonian contains both positive- and negative-frequency contributions. With commutation relations, the negative-frequency sector would have an energy spectrum unbounded below, giving an unstable vacuum. Anticommutation relations flip the sign so that both particle and antiparticle excitations contribute positive energy. Additionally, microcausality (the requirement that field operators at spacelike separations commute or anticommute) requires anticommutators for half-integer spin fields to maintain Lorentz invariance."
  explanation: "The spin-statistics connection is not optional — it is a theorem provable from the axioms of relativistic quantum field theory (Lorentz invariance, locality, positive energy). Violating it leads to either negative-energy states or violations of causality. The fact that electrons are fermions is a consequence of their spin-1/2 nature combined with the requirements of a consistent relativistic quantum theory."
```

## Explainer

Quantizing the Dirac field follows the same canonical procedure as for the Klein-Gordon field, but with a critical difference: you must use **anticommutation relations** instead of commutation relations. The classical Dirac field psi(x) is a four-component spinor satisfying (i gamma^mu partial_mu - m)psi = 0. Its conjugate momentum is pi = i psi-dagger. The equal-time anticommutation relation is {psi_alpha(x, t), psi-dagger_beta(y, t)} = delta_{alpha beta} delta^3(x - y), where alpha and beta are spinor indices.

The field operator expands into positive- and negative-frequency parts: psi(x) = sum over spins s of integral [b_{p,s} u_s(p) e^{-ipx} + d-dagger_{p,s} v_s(p) e^{+ipx}] d^3p / ((2pi)^3 2E_p). Here u_s(p) and v_s(p) are the positive- and negative-frequency Dirac spinors, b_{p,s} destroys an electron with momentum p and spin s, and d-dagger_{p,s} creates a positron. The anticommutation relations are {b_{p,s}, b-dagger_{q,r}} = (2pi)^3 delta^3(p-q) delta_{sr} and {d_{p,s}, d-dagger_{q,r}} = (2pi)^3 delta^3(p-q) delta_{sr}, with all other anticommutators vanishing.

The reason anticommutation is mandatory (not a choice) is stability. The Dirac Hamiltonian has both positive and negative energy solutions. If you used bosonic commutation relations, each negative-energy mode would contribute -E_p per quantum, and since bosonic statistics allow unlimited occupation, you could drive the energy to negative infinity. With fermionic anticommutation relations, the reinterpretation of negative-frequency modes as antiparticle creation operators flips the energy sign: d-dagger creates a positron with positive energy +E_p. The Pauli exclusion principle then prevents unlimited occupation, and the vacuum is stable. This is a concrete manifestation of the **spin-statistics theorem**: half-integer spin fields must be quantized as fermions.

After quantization, the Dirac field naturally describes both particles and antiparticles. The electron field psi has two types of creation operators (b-dagger for electrons, d-dagger for positrons) and two types of annihilation operators (b for electrons, d for positrons). The conserved Noether current from the U(1) symmetry psi -> e^{i alpha} psi gives the electric charge operator Q = integral (b-dagger b - d-dagger d) d^3p, which counts electrons minus positrons. Every interaction vertex in QED involves psi and psi-bar, which is why every QED process conserves the number of electrons minus positrons (electric charge conservation).
