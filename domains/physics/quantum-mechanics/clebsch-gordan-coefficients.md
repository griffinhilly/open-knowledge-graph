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
status: draft
---

# Clebsch-Gordan Coefficients

## Core Idea
Clebsch-Gordan coefficients ⟨j₁, m₁; j₂, m₂ | j, m_j⟩ expand coupled angular momentum states as linear combinations of uncoupled states and encode all angular momentum composition algebra.

## Explainer

From your study of angular momentum coupling, you know that when two angular momenta j₁ and j₂ are combined, the total angular momentum J can take any integer value between |j₁ − j₂| and j₁ + j₂. You also know that the same physical system can be described in two equivalent bases: the **uncoupled basis** |j₁, m₁; j₂, m₂⟩, which labels each particle separately, and the **coupled basis** |J, M⟩, which labels the total. **Clebsch-Gordan coefficients** are simply the numbers that convert between these two descriptions — they are the inner products ⟨j₁, m₁; j₂, m₂ | J, M⟩.

The most important practical constraint is that M = m₁ + m₂ always. The z-components of angular momentum add, so any uncoupled state |j₁, m₁; j₂, m₂⟩ only connects to coupled states with M = m₁ + m₂. This selection rule dramatically limits which coefficients are nonzero. As a concrete example, consider combining two spin-½ particles (j₁ = j₂ = ½). The uncoupled basis has four states: |↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩. The coupled basis has a **triplet** (J = 1, M = 1, 0, −1) and a **singlet** (J = 0, M = 0). The CG coefficients give: |J=1, M=0⟩ = (1/√2)(|↑↓⟩ + |↓↑⟩) and |J=0, M=0⟩ = (1/√2)(|↑↓⟩ − |↓↑⟩). The coefficients 1/√2 here are CG coefficients; they encode the fact that the symmetric and antisymmetric combinations have different total spin.

In practice, CG coefficients are looked up in standard tables rather than computed from scratch. They appear in almost every calculation involving composite angular momentum: **atomic spectroscopy** (coupling orbital and spin angular momenta to get total J), **nuclear physics** (coupling proton and neutron angular momenta), and **addition rules for multiplet structure**. When computing matrix elements of vector operators, the **Wigner-Eckart theorem** reduces everything to a product of a CG coefficient and a reduced matrix element, making CG tables indispensable. The key skill is recognizing which basis is natural for a given problem and using the coefficients to transform fluently between them.
