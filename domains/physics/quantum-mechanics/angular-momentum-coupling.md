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
stage: advanced
status: validated
---

# Angular Momentum Coupling

## Core Idea
When two angular momenta couple, J⃗ = J⃗₁ + J⃗₂ has quantum number j ranging from |j₁ − j₂| to j₁ + j₂. The basis transformation uses Clebsch-Gordan coefficients.

## Questions

```yaml
- question: "An electron has orbital angular momentum quantum number l = 2 and spin s = 1/2. What are the possible values of the total angular momentum quantum number j?"
  type: multiple-choice
  options:
    - "j = 5/2 only — total angular momentum is always the sum of the individual angular momenta"
    - "j = 3/2 and j = 5/2 — j ranges from |l − s| = |2 − 1/2| = 3/2 to l + s = 5/2 in integer steps"
    - "j = 0, 1, 2, 3, 4 — total angular momentum takes all integer values up to l + s"
    - "j = 2 and j = 1/2 — you retain each subsystem's quantum number independently"
  answer: 1
  explanation: "The triangle rule for angular momentum coupling states that j takes values |j₁ − j₂|, |j₁ − j₂| + 1, …, j₁ + j₂ in integer steps. For l = 2 and s = 1/2: minimum is |2 − 1/2| = 3/2, maximum is 2 + 1/2 = 5/2, and the step between them is 1. So j = 3/2 and j = 5/2. You can verify: the uncoupled basis has (2l+1)(2s+1) = 5 × 2 = 10 states; the coupled basis has (2·(3/2)+1) + (2·(5/2)+1) = 4 + 6 = 10 states. The total count is preserved."

- question: "Why is the coupled basis |j, m_j⟩ preferred over the uncoupled basis |m_l, m_s⟩ when analyzing the spin-orbit interaction in hydrogen?"
  type: multiple-choice
  options:
    - "The coupled basis uses fewer quantum numbers and is therefore simpler to write down"
    - "The spin-orbit Hamiltonian H_SO ∝ L⃗·S⃗ commutes with J² and J_z but not with L_z or S_z separately, making j and m_j good quantum numbers in the coupled basis while m_l and m_s are not"
    - "The uncoupled basis does not span the complete state space for a hydrogen electron"
    - "The coupled basis is always the preferred choice in quantum mechanics regardless of the physical system"
  answer: 1
  explanation: "The criterion for a 'good' quantum number is that the corresponding operator commutes with the Hamiltonian. L⃗·S⃗ = (J² − L² − S²)/2, so H_SO commutes with J², L², and S² but NOT with L_z or S_z individually (since rotating the system changes both m_l and m_s). In the uncoupled basis, m_l and m_s are not conserved — H_SO mixes states with different m_l and m_s. In the coupled basis, j and m_j are conserved — H_SO is diagonal in blocks labeled by j. This is why energy levels split into j-labeled doublets rather than (m_l, m_s)-labeled states."

- question: "When coupling angular momenta j₁ and j₂, the total number of states (2j₁+1)(2j₂+1) is the same whether counted in the uncoupled or coupled basis."
  type: true-false
  answer: true
  explanation: "The Clebsch-Gordan transformation is a unitary change of basis — it rotates the state space without changing its dimension. The uncoupled basis has (2j₁+1)(2j₂+1) states labeled by (m₁, m₂). The coupled basis has Σ(2j+1) states summed over j from |j₁−j₂| to j₁+j₂, and this sum equals (2j₁+1)(2j₂+1) by a standard identity. For example, coupling two spin-1/2 particles: (2·½+1)² = 4; coupled: triplet (j=1, 3 states) + singlet (j=0, 1 state) = 4. State counting is always preserved."

- question: "When two angular momenta j₁ and j₂ are coupled, the total angular momentum quantum number j must equal j₁ + j₂."
  type: true-false
  answer: false
  explanation: "j = j₁ + j₂ is the maximum possible value, not the only value. The full range is j = |j₁ − j₂|, |j₁ − j₂| + 1, …, j₁ + j₂, in integer steps. For two spin-1/2 particles (j₁ = j₂ = 1/2), coupling gives j = 0 (the singlet) and j = 1 (the triplet) — not just j = 1. The existence of the lower j values is physically important: the spin singlet state has different symmetry, energy, and magnetic properties than the triplet. Assuming j always equals j₁ + j₂ would miss half the physics."

- question: "What determines whether the coupled basis or the uncoupled basis is more convenient for a given problem, and why does the spin-orbit interaction in hydrogen favor the coupled basis?"
  type: short-answer
  answer: "The convenient basis is determined by which quantum numbers are conserved by the Hamiltonian — i.e., which operators commute with H. If H commutes with J², J_z, L², and S² but not with L_z or S_z individually (as with spin-orbit coupling H_SO ∝ L⃗·S⃗), then j and m_j are good quantum numbers but m_l and m_s are not. The coupled basis, which diagonalizes J² and J_z, makes H_SO block-diagonal and easy to handle. The uncoupled basis, which diagonalizes L_z and S_z, mixes states under H_SO, producing off-diagonal matrix elements that complicate calculations. In general: use the basis whose quantum numbers are preserved by the dominant interaction."
  explanation: "This principle extends throughout atomic, nuclear, and particle physics. When there is no coupling interaction, the uncoupled basis is fine — the subsystems evolve independently and their individual quantum numbers are conserved. Once an interaction couples the subsystems, you switch to the coupled basis where the total angular momentum is conserved instead. The Clebsch-Gordan coefficients are the mathematical tool that converts between these two natural descriptions."
```

## Explainer

From your study of total angular momentum, you know that a single quantum rotor has states |j, m⟩ where j is the angular momentum quantum number and m ranges in integer steps from −j to +j. Now suppose you have two independent rotors — say, an electron's orbital angular momentum with quantum number l and its spin with s = ½. Physically, they interact (the electron moves in an electromagnetic field that couples l and s), so you need to work in a basis that respects the coupled system. Angular momentum coupling is the procedure for constructing that basis.

The classical analogy helps: if you add two vectors of length r₁ and r₂, the length of their sum can range from |r₁ − r₂| (pointing opposite) to r₁ + r₂ (pointing same). Quantum mechanics enforces the same triangle inequality, but only discrete values are allowed. The total quantum number **j** takes values |j₁ − j₂|, |j₁ − j₂| + 1, …, j₁ + j₂. For l = 1 and s = ½, the coupled values are j = ½ and j = 3/2. Each value of j then has its own (2j + 1) states with m_j ranging from −j to +j. You can verify that the total number of states is the same in both bases: (2l+1)(2s+1) = (2j₁+1)(2j₂+1).

The two natural bases are the **uncoupled basis** |j₁, m₁; j₂, m₂⟩, which labels each subsystem separately, and the **coupled basis** |j, m_j; j₁, j₂⟩, which labels the total angular momentum. The uncoupled basis is convenient when the subsystems do not interact; the coupled basis is convenient when there is a coupling Hamiltonian like spin-orbit interaction, because J² and J_z then commute with H, making j and m_j good quantum numbers.

**Clebsch-Gordan coefficients** are the matrix elements of the unitary transformation between these two bases: |j, m_j⟩ = Σ C(j₁, m₁; j₂, m₂ | j, m_j) |j₁, m₁; j₂, m₂⟩. These coefficients are tabulated and appear everywhere in atomic, nuclear, and particle physics when you need to add angular momenta. For the simple case j₁ = j₂ = ½ (two spin-½ particles), the coupled states are the spin triplet (j = 1, three states) and spin singlet (j = 0, one state) — the singlet combination |↑↓⟩ − |↓↑⟩ has the antisymmetry required for identical fermions.
