---
id: angular-momentum-coupling
title: Angular Momentum Coupling
domain: physics
course: quantum-mechanics
prerequisites:
- id: total-angular-momentum
  type: hard
builds-toward:
- clebsch-gordan-coefficients
tags:
- angular-momentum
- coupling
stage: abstract-reasoning
status: draft
---

# Angular Momentum Coupling

## Core Idea
When two angular momenta couple, J⃗ = J⃗₁ + J⃗₂ has quantum number j ranging from |j₁ − j₂| to j₁ + j₂. The basis transformation uses Clebsch-Gordan coefficients.

## Explainer

From your study of total angular momentum, you know that a single quantum rotor has states |j, m⟩ where j is the angular momentum quantum number and m ranges in integer steps from −j to +j. Now suppose you have two independent rotors — say, an electron's orbital angular momentum with quantum number l and its spin with s = ½. Physically, they interact (the electron moves in an electromagnetic field that couples l and s), so you need to work in a basis that respects the coupled system. Angular momentum coupling is the procedure for constructing that basis.

The classical analogy helps: if you add two vectors of length r₁ and r₂, the length of their sum can range from |r₁ − r₂| (pointing opposite) to r₁ + r₂ (pointing same). Quantum mechanics enforces the same triangle inequality, but only discrete values are allowed. The total quantum number **j** takes values |j₁ − j₂|, |j₁ − j₂| + 1, …, j₁ + j₂. For l = 1 and s = ½, the coupled values are j = ½ and j = 3/2. Each value of j then has its own (2j + 1) states with m_j ranging from −j to +j. You can verify that the total number of states is the same in both bases: (2l+1)(2s+1) = (2j₁+1)(2j₂+1).

The two natural bases are the **uncoupled basis** |j₁, m₁; j₂, m₂⟩, which labels each subsystem separately, and the **coupled basis** |j, m_j; j₁, j₂⟩, which labels the total angular momentum. The uncoupled basis is convenient when the subsystems do not interact; the coupled basis is convenient when there is a coupling Hamiltonian like spin-orbit interaction, because J² and J_z then commute with H, making j and m_j good quantum numbers.

**Clebsch-Gordan coefficients** are the matrix elements of the unitary transformation between these two bases: |j, m_j⟩ = Σ C(j₁, m₁; j₂, m₂ | j, m_j) |j₁, m₁; j₂, m₂⟩. These coefficients are tabulated and appear everywhere in atomic, nuclear, and particle physics when you need to add angular momenta. For the simple case j₁ = j₂ = ½ (two spin-½ particles), the coupled states are the spin triplet (j = 1, three states) and spin singlet (j = 0, one state) — the singlet combination |↑↓⟩ − |↓↑⟩ has the antisymmetry required for identical fermions.
