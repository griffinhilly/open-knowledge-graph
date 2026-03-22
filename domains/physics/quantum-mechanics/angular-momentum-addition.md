---
id: angular-momentum-addition
title: Addition of Angular Momenta
domain: physics
course: quantum-mechanics
prerequisites:
- id: angular-momentum-quantization
  type: hard
builds-toward:
- clebsch-gordan-coefficients
tags:
- angular-momentum
- composition
stage: advanced
status: draft
---

# Addition of Angular Momenta

## Core Idea
When combining two angular momenta J₁ and J₂, the total J = J₁ + J₂ has quantum numbers ranging from |ℓ₁ - ℓ₂| to ℓ₁ + ℓ₂. Reexpressing uncoupled eigenstates in the coupled basis requires Clebsch-Gordan coefficients, essential for understanding atomic fine structure.

## Questions

```yaml
- question: "A composite system has two subsystems with angular momentum quantum numbers j₁ = 3/2 and j₂ = 1. What are the possible values of the total angular momentum quantum number j?"
  type: multiple-choice
  options:
    - "j = 1/2, 3/2, 5/2"
    - "j = 0, 1/2, 1, 3/2, 2, 5/2"
    - "j = 5/2 only — the maximum total angular momentum"
    - "j = 1/2, 1, 3/2, 2, 5/2 — all values between the minimum and maximum"
  answer: 0
  explanation: "The triangular rule gives j from |j₁ − j₂| to j₁ + j₂ in integer steps: |3/2 − 1| = 1/2 and 3/2 + 1 = 5/2, so j = 1/2, 3/2, 5/2. Option B is the common error — assuming all values from 0 up to j₁ + j₂ are allowed. The lower bound is |j₁ − j₂|, not 0. Dimension check confirms: (2·½+1) + (2·3/2+1) + (2·5/2+1) = 2 + 4 + 6 = 12 = (2·3/2+1)(2·1+1) = 4·3 ✓."

- question: "An atom has spin-orbit coupling described by a term proportional to L·S in the Hamiltonian. Why is the coupled basis {|j, M⟩} preferred over the uncoupled basis {|mₗ, mₛ⟩} for computing energy levels?"
  type: multiple-choice
  options:
    - "The coupled basis is mathematically simpler for all Hamiltonians, regardless of the physical interaction"
    - "L·S commutes with J² and Jz but not with Lz or Sz individually, so j and M are good quantum numbers while mₗ and mₛ are not"
    - "The uncoupled basis fails to span the full state space when spin-orbit coupling is present"
    - "The coupled basis eliminates the need for Clebsch-Gordan coefficients once the basis change is made"
  answer: 1
  explanation: "L·S = (J² − L² − S²)/2, which commutes with J², Jz, L², and S² but not with Lz or Sz. This means j and M are conserved quantities (good quantum numbers) under spin-orbit coupling, while mₗ and mₛ are not. In the coupled basis, L·S is diagonal, yielding energy eigenvalues directly. In the uncoupled basis, spin-orbit coupling mixes states, requiring diagonalization. The physical energy splitting (fine structure) is indexed by j, not by mₗ and mₛ separately."

- question: "When combining two spin-1/2 particles, the possible values of the total spin quantum number include j = 0, 1/2, and 1."
  type: true-false
  answer: false
  explanation: "Applying the triangular rule: |1/2 − 1/2| = 0 and 1/2 + 1/2 = 1, with integer steps, gives j = 0 and j = 1 only. The value j = 1/2 is not allowed. This is a common error — students assume all values between 0 and the maximum are accessible, but the rule requires integer steps from |j₁ − j₂|, not all fractions. The result is a triplet (j = 1, three states M = −1, 0, +1) and a singlet (j = 0, one state M = 0), totaling 4 = 2×2 states."

- question: "The coupled basis and uncoupled basis for a composite angular momentum system span the same Hilbert space and have the same total number of states."
  type: true-false
  answer: true
  explanation: "Both are complete orthonormal bases for the same (2j₁+1)(2j₂+1)-dimensional tensor product space. The Clebsch-Gordan coefficients are the entries of the unitary transformation connecting them — no states are created or lost by changing basis. This is why the dimension count always works out: the sum Σⱼ(2j+1) over all allowed j values must equal (2j₁+1)(2j₂+1)."

- question: "State the triangular rule for combining angular momenta j₁ and j₂, and explain why the minimum total angular momentum is |j₁ − j₂| rather than 0."
  type: short-answer
  answer: "The total angular momentum j ranges from |j₁ − j₂| to j₁ + j₂ in integer steps. The minimum is |j₁ − j₂|, not 0, because angular momenta add vectorially and must obey the triangle inequality. When j₁ ≠ j₂, the larger angular momentum always has a component that the smaller cannot cancel, so j = 0 is impossible. Only when j₁ = j₂ can the two exactly oppose to give j = 0."
  explanation: "The classical analogy is clear: two vectors of lengths 3 and 4 combine to give a resultant between 1 and 7, never 0, because the longer vector has more magnitude. The quantum triangular rule is the analog of the classical triangle inequality, with the additional quantization constraint that j must be integer or half-integer. The dimension check — verifying that state counts are preserved — is a reliable way to confirm the allowed j values."
```

## Explainer

From your study of angular-momentum quantization, you know that a single angular momentum operator Ĵ has simultaneous eigenstates |j, m⟩ where j = 0, 1/2, 1, 3/2, … and m = -j, -j+1, …, j. The quantum number j tells you the magnitude and m tells you the z-component. Now consider a physical situation with two separate angular momenta — for example, an electron's orbital angular momentum L and its spin S, or two particles each with their own spin. Each lives in its own Hilbert space, with quantum numbers (ℓ₁, m₁) and (ℓ₂, m₂). The combined system lives in the tensor product of these spaces, and the question is: what are the eigenstates of the total **total angular momentum** J = J₁ + J₂?

The answer to "what values can j take?" is the triangular rule: j runs from |j₁ - j₂| to j₁ + j₂ in integer steps. This is analogous to vector addition in classical mechanics — two vectors of length 3 and 4 can combine to give a resultant between 1 and 7 — but quantization forces j to be either an integer or half-integer, and only specific values are allowed. Equally important, the total z-projection M = m₁ + m₂ is always conserved, so all states with a given M contribute to a specific total j. For example, combining spin-1/2 (s₁ = 1/2) with spin-1/2 (s₂ = 1/2) gives a triplet (j = 1) with three states M = -1, 0, +1, and a singlet (j = 0) with one state M = 0. The four-dimensional uncoupled space exactly fills the combined 3 + 1 = 4 dimensions of the coupled space — nothing is lost.

The **uncoupled basis** describes the system in terms of the individual quantum numbers: |j₁, m₁⟩ ⊗ |j₂, m₂⟩. The **coupled basis** describes it in terms of the total: |j, M⟩. Both span the same space; they are just different ways of labeling the states. Converting between them requires **Clebsch-Gordan coefficients** ⟨j₁, m₁; j₂, m₂ | j, M⟩. These are tabulated numbers that tell you how much of each uncoupled state goes into each coupled state. For the spin-1/2 case, the triplet M = 0 state is (1/√2)(|↑↓⟩ + |↓↑⟩) and the singlet is (1/√2)(|↑↓⟩ - |↓↑⟩) — the 1/√2 factors are the Clebsch-Gordan coefficients.

Why does this matter physically? The Hamiltonian of real atoms includes **spin-orbit coupling**, a term proportional to L·S. This interaction mixes the uncoupled basis states, so neither mₗ nor mₛ is a good quantum number in an atom — but j (the total angular momentum) is. Working in the coupled basis where L·S = (J² - L² - S²)/2 is diagonal directly yields the energy splitting responsible for the fine structure of spectral lines. Angular momentum addition is the bridge from idealized single-particle quantum mechanics to the spectroscopy of real atoms.
