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
stage: abstract-reasoning
status: draft
---

# Addition of Angular Momenta

## Core Idea
When combining two angular momenta J₁ and J₂, the total J = J₁ + J₂ has quantum numbers ranging from |ℓ₁ - ℓ₂| to ℓ₁ + ℓ₂. Reexpressing uncoupled eigenstates in the coupled basis requires Clebsch-Gordan coefficients, essential for understanding atomic fine structure.

## Explainer

From your study of angular-momentum quantization, you know that a single angular momentum operator Ĵ has simultaneous eigenstates |j, m⟩ where j = 0, 1/2, 1, 3/2, … and m = -j, -j+1, …, j. The quantum number j tells you the magnitude and m tells you the z-component. Now consider a physical situation with two separate angular momenta — for example, an electron's orbital angular momentum L and its spin S, or two particles each with their own spin. Each lives in its own Hilbert space, with quantum numbers (ℓ₁, m₁) and (ℓ₂, m₂). The combined system lives in the tensor product of these spaces, and the question is: what are the eigenstates of the total **total angular momentum** J = J₁ + J₂?

The answer to "what values can j take?" is the triangular rule: j runs from |j₁ - j₂| to j₁ + j₂ in integer steps. This is analogous to vector addition in classical mechanics — two vectors of length 3 and 4 can combine to give a resultant between 1 and 7 — but quantization forces j to be either an integer or half-integer, and only specific values are allowed. Equally important, the total z-projection M = m₁ + m₂ is always conserved, so all states with a given M contribute to a specific total j. For example, combining spin-1/2 (s₁ = 1/2) with spin-1/2 (s₂ = 1/2) gives a triplet (j = 1) with three states M = -1, 0, +1, and a singlet (j = 0) with one state M = 0. The four-dimensional uncoupled space exactly fills the combined 3 + 1 = 4 dimensions of the coupled space — nothing is lost.

The **uncoupled basis** describes the system in terms of the individual quantum numbers: |j₁, m₁⟩ ⊗ |j₂, m₂⟩. The **coupled basis** describes it in terms of the total: |j, M⟩. Both span the same space; they are just different ways of labeling the states. Converting between them requires **Clebsch-Gordan coefficients** ⟨j₁, m₁; j₂, m₂ | j, M⟩. These are tabulated numbers that tell you how much of each uncoupled state goes into each coupled state. For the spin-1/2 case, the triplet M = 0 state is (1/√2)(|↑↓⟩ + |↓↑⟩) and the singlet is (1/√2)(|↑↓⟩ - |↓↑⟩) — the 1/√2 factors are the Clebsch-Gordan coefficients.

Why does this matter physically? The Hamiltonian of real atoms includes **spin-orbit coupling**, a term proportional to L·S. This interaction mixes the uncoupled basis states, so neither mₗ nor mₛ is a good quantum number in an atom — but j (the total angular momentum) is. Working in the coupled basis where L·S = (J² - L² - S²)/2 is diagonal directly yields the energy splitting responsible for the fine structure of spectral lines. Angular momentum addition is the bridge from idealized single-particle quantum mechanics to the spectroscopy of real atoms.
