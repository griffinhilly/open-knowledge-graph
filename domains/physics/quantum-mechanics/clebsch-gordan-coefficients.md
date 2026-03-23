---
id: clebsch-gordan-coefficients
title: Clebsch-Gordan Coefficients
domain: physics
course: quantum-mechanics
prerequisites:
- id: angular-momentum-coupling
  type: hard
builds-toward:
- hydrogen-energy-levels
tags:
- angular-momentum
- coupling
stage: advanced
status: validated
---

# Clebsch-Gordan Coefficients

## Core Idea
Clebsch-Gordan coefficients ⟨j₁, m₁; j₂, m₂ | j, m_j⟩ expand coupled angular momentum states as linear combinations of uncoupled states and encode all angular momentum composition algebra.

## Questions

```yaml
- question: "An orbital electron has orbital angular momentum j₁ = 1 and spin j₂ = 1/2. What are the possible values of total angular momentum J?"
  type: multiple-choice
  options:
    - "J = 1 only, because spin-½ is a small perturbative correction"
    - "J = 3/2 and J = 1/2"
    - "J = 2 and J = 1"
    - "J = 1/2 only, because spin dominates the coupling"
  answer: 1
  explanation: "When combining angular momenta j₁ and j₂, total J ranges in integer steps from |j₁ − j₂| to j₁ + j₂. Here: |1 − 1/2| = 1/2 and 1 + 1/2 = 3/2, giving J = 3/2 (4 states) and J = 1/2 (2 states). The total count is 4 + 2 = 6 = (2×1+1)(2×1/2+1) = 3 × 2, as required. Options A and D incorrectly treat one angular momentum as dominant; they always combine vectorially, with all values between the min and max allowed."

- question: "You want to expand |j₁=1, m₁=1; j₂=1/2, m₂=−1/2⟩ in the coupled basis. Which coupled states |J, M⟩ can appear in this expansion?"
  type: multiple-choice
  options:
    - "Any state with J between 1/2 and 3/2"
    - "Only states with M = m₁ + m₂ = +1/2, specifically |J=3/2, M=1/2⟩ and |J=1/2, M=1/2⟩"
    - "Only |J=3/2, M=1/2⟩ because the higher-J state is dominant"
    - "States with any M value, since the full expansion sums over all coupled states"
  answer: 1
  explanation: "The most important CG selection rule is M = m₁ + m₂. The z-components of angular momentum add, so an uncoupled state |m₁, m₂⟩ can only contribute to coupled states with M = m₁ + m₂ = 1 + (−1/2) = +1/2. Both J = 3/2 and J = 1/2 have M = +1/2 states, so both appear with nonzero coefficients. The actual coefficients require looking up CG tables, but the selection rule immediately eliminates all M ≠ +1/2 states — most of the table."

- question: "The selection rule M = m₁ + m₂ in Clebsch-Gordan decomposition reflects the fact that the z-component of total angular momentum equals the sum of the individual z-components."
  type: true-false
  answer: true
  explanation: "The z-component operator is Jz = J₁z + J₂z. The uncoupled state |j₁, m₁; j₂, m₂⟩ is an eigenstate of J₁z with eigenvalue ℏm₁ and of J₂z with eigenvalue ℏm₂, so it is an eigenstate of Jz with eigenvalue ℏ(m₁ + m₂). Since coupled states |J, M⟩ are eigenstates of Jz with eigenvalue ℏM, only coupled states with M = m₁ + m₂ are non-orthogonal to the uncoupled state. This is an exact selection rule — not an approximation — and it eliminates most CG coefficients from the outset."

- question: "For two spin-½ particles, the Clebsch-Gordan decomposition yields four total states, all of which are symmetric under exchange of particle labels."
  type: true-false
  answer: false
  explanation: "The decomposition yields a triplet (J=1) and a singlet (J=0). The three triplet states |1,1⟩, |1,0⟩, |1,−1⟩ are symmetric under particle exchange, but the singlet |0,0⟩ = (1/√2)(|↑↓⟩ − |↓↑⟩) is antisymmetric — it reverses sign when particle labels are swapped. The CG coefficient structure encodes this symmetry difference: a + sign in the triplet M=0 state, a − sign in the singlet. This matters because identical fermions require antisymmetric total wavefunctions, constraining which spin states are available for a given spatial state."

- question: "What does the Clebsch-Gordan coefficient ⟨j₁, m₁; j₂, m₂ | J, M⟩ physically represent, and why does the selection rule M = m₁ + m₂ guarantee that most of these coefficients are exactly zero?"
  type: short-answer
  answer: "The coefficient ⟨j₁, m₁; j₂, m₂ | J, M⟩ is the inner product between the uncoupled state |j₁, m₁; j₂, m₂⟩ and the coupled state |J, M⟩. It gives the probability amplitude for finding the system in the coupled state |J, M⟩ when the particles are individually in states |m₁⟩ and |m₂⟩. The selection rule M = m₁ + m₂ follows from the additivity of Jz: any coupled state with M ≠ m₁ + m₂ is a Jz eigenstate with a different eigenvalue and is therefore orthogonal to the uncoupled state, making the inner product exactly zero."
  explanation: "The interpretation as probability amplitudes makes CG coefficients central to any quantum measurement involving composite angular momentum. If you prepare two particles in |m₁, m₂⟩ and measure total J, the probability of obtaining J = 3/2 is |⟨j₁, m₁; j₂, m₂ | 3/2, m₁+m₂⟩|². The Wigner-Eckart theorem extends this further: matrix elements of tensor operators between angular momentum states factor into a CG coefficient times a reduced matrix element, which is why CG tables appear in nearly every spectroscopy and atomic physics calculation."
```

## Explainer

From your study of angular momentum coupling, you know that when two angular momenta j₁ and j₂ are combined, the total angular momentum J can take any integer value between |j₁ − j₂| and j₁ + j₂. You also know that the same physical system can be described in two equivalent bases: the **uncoupled basis** |j₁, m₁; j₂, m₂⟩, which labels each particle separately, and the **coupled basis** |J, M⟩, which labels the total. **Clebsch-Gordan coefficients** are simply the numbers that convert between these two descriptions — they are the inner products ⟨j₁, m₁; j₂, m₂ | J, M⟩.

The most important practical constraint is that M = m₁ + m₂ always. The z-components of angular momentum add, so any uncoupled state |j₁, m₁; j₂, m₂⟩ only connects to coupled states with M = m₁ + m₂. This selection rule dramatically limits which coefficients are nonzero. As a concrete example, consider combining two spin-½ particles (j₁ = j₂ = ½). The uncoupled basis has four states: |↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩. The coupled basis has a **triplet** (J = 1, M = 1, 0, −1) and a **singlet** (J = 0, M = 0). The CG coefficients give: |J=1, M=0⟩ = (1/√2)(|↑↓⟩ + |↓↑⟩) and |J=0, M=0⟩ = (1/√2)(|↑↓⟩ − |↓↑⟩). The coefficients 1/√2 here are CG coefficients; they encode the fact that the symmetric and antisymmetric combinations have different total spin.

In practice, CG coefficients are looked up in standard tables rather than computed from scratch. They appear in almost every calculation involving composite angular momentum: **atomic spectroscopy** (coupling orbital and spin angular momenta to get total J), **nuclear physics** (coupling proton and neutron angular momenta), and **addition rules for multiplet structure**. When computing matrix elements of vector operators, the **Wigner-Eckart theorem** reduces everything to a product of a CG coefficient and a reduced matrix element, making CG tables indispensable. The key skill is recognizing which basis is natural for a given problem and using the coefficients to transform fluently between them.
