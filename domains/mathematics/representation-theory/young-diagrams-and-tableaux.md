---
id: young-diagrams-and-tableaux
title: Young Diagrams and Tableaux
domain: mathematics
course: representation-theory
prerequisites:
- id: representations-of-symmetric-groups
  type: hard
builds-toward: []
tags:
- young-diagram
- young-tableau
- partition
- hook-length-formula
- specht-module
stage: expert
status: validated
---

# Young Diagrams and Tableaux

## Core Idea
A Young diagram is a graphical representation of a partition λ = (λ₁ ≥ λ₂ ≥ ··· ≥ λₖ) as left-justified rows of boxes. A Young tableau fills these boxes with numbers according to specified rules. Standard Young tableaux (entries increase along rows and down columns) count the dimension of the corresponding Specht module, while semistandard tableaux arise in the theory of symmetric functions and Schur-Weyl duality.

## Questions

```yaml
- question: "How many standard Young tableaux exist for the partition (3, 2) of 5?"
  type: multiple-choice
  options:
    - "3"
    - "5"
    - "7"
    - "10"
  answer: 1
  explanation: "Using the hook length formula: dim = 5! / (h₁₁·h₁₂·h₁₃·h₂₁·h₂₂). The hook lengths for the (3,2) diagram are: h₁₁=4, h₁₂=3, h₁₃=1, h₂₁=2, h₂₂=1. So dim = 120/(4·3·1·2·1) = 120/24 = 5. One can verify by listing: the 5 standard fillings of a 3-box row atop a 2-box row with {1,2,3,4,5} increasing along rows and down columns."

- question: "A standard Young tableau must have entries increasing along rows (left to right) and down columns (top to bottom). If a filling violates the column condition but satisfies the row condition, is it still a standard tableau?"
  type: true-false
  answer: false
  explanation: "A standard Young tableau requires BOTH conditions: strict increase along rows and strict increase down columns. A filling satisfying only the row condition is not standard. The column condition is essential — it ensures that the corresponding element in the group algebra generates an irreducible submodule. Dropping either condition changes the combinatorial count and breaks the connection to representation theory."

- question: "The hook length of a box in position (i, j) of a Young diagram counts:"
  type: multiple-choice
  options:
    - "The number of boxes directly below the box"
    - "The number of boxes directly to its right"
    - "The number of boxes directly to its right, directly below it, plus the box itself"
    - "The total number of boxes in row i plus column j"
  answer: 2
  explanation: "The hook of box (i,j) consists of the box itself, all boxes directly to its right in the same row, and all boxes directly below it in the same column. The hook length h(i,j) is the count of these boxes. For the partition (3,2), the box at position (1,1) has hook {(1,1),(1,2),(1,3),(2,1)} — 2 boxes to the right, 1 box below, plus itself — giving h(1,1) = 4."

- question: "Why do Young diagrams appear in the representation theory of both Sₙ and GL_n(ℂ)?"
  type: short-answer
  answer: "Schur-Weyl duality establishes that the actions of Sₙ and GL_n(ℂ) on tensor space (ℂⁿ)^{⊗n} are mutual centralizers. Decomposing this tensor space under both actions simultaneously produces a correspondence: irreducible representations of Sₙ (indexed by partitions of n) pair with irreducible polynomial representations of GL_n (indexed by the same partitions). Young diagrams serve as the common indexing set for both."
  explanation: "This is one of the deepest connections in representation theory. The partition λ labels a Specht module for Sₙ and a Schur functor for GL_n. The semistandard Young tableaux of shape λ with entries in {1,...,n} index a basis for the GL_n-representation, while the standard tableaux of shape λ index a basis for the Sₙ-representation. The combinatorics of tableaux thus serves as a bridge between two seemingly different representation theories."
```

## Explainer

A **Young diagram** of a partition λ = (λ₁, λ₂, …, λₖ) is an array of boxes arranged in left-justified rows, with λᵢ boxes in row i. For example, the partition (3, 2, 1) of 6 gives a staircase pattern: 3 boxes on top, 2 in the middle, 1 on the bottom. The visual language of Young diagrams translates partition arithmetic into geometry, making combinatorial arguments intuitive.

A **Young tableau** fills the boxes of a Young diagram with entries (typically positive integers). A **standard Young tableau** (SYT) uses each of the numbers 1, …, n exactly once, with entries increasing left-to-right along each row and top-to-bottom down each column. The number of SYTs of shape λ equals the dimension of the Specht module Sλ, and is computed by the **hook length formula**: f^λ = n! / ∏ h(i,j), where h(i,j) is the hook length of box (i,j) — the number of boxes directly to its right plus those directly below it plus one (for the box itself). This formula, discovered by Frame, Robinson, and Thrall, is a remarkable combinatorial identity.

The construction of Specht modules uses tableaux directly. Given a Young tableau T of shape λ, define the **row symmetrizer** a_T = Σ_{σ∈R(T)} σ (sum over permutations preserving each row) and the **column antisymmetrizer** b_T = Σ_{σ∈C(T)} sgn(σ)·σ (signed sum over permutations preserving each column). The **Young symmetrizer** is c_T = a_T · b_T, an element of the group algebra ℂ[Sₙ]. The left ideal ℂ[Sₙ]·c_T is isomorphic to the Specht module Sλ — an explicit construction of the irreducible representation from combinatorial data.

**Semistandard Young tableaux** (SSYTs) relax the conditions: entries weakly increase along rows and strictly increase down columns, and entries can repeat. SSYTs of shape λ with entries in {1, …, m} index a basis for the irreducible polynomial representation of GL_m corresponding to λ, and their generating function is the **Schur polynomial** s_λ(x₁, …, x_m). This dual role — standard tableaux for Sₙ, semistandard for GL_m — is the combinatorial manifestation of Schur-Weyl duality, and it places Young diagrams at the intersection of representation theory, algebraic combinatorics, and symmetric function theory.
