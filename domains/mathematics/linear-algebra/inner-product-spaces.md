---
id: inner-product-spaces
title: Inner Product Spaces
domain: mathematics
course: linear-algebra
prerequisites:
- id: dot-product
  type: hard
- id: vector-spaces
  type: hard
- id: matrix-transpose-properties
  type: soft
builds-toward:
- orthogonality-in-linear-algebra
- symmetric-matrices
tags:
- inner product
- norm
- Cauchy-Schwarz
- angle
- abstract dot product
stage: formal-systems
status: validated
---
# Inner Product Spaces

## Core Idea
An inner product on a vector space V is a function ⟨u, v⟩ satisfying four axioms: symmetry (⟨u,v⟩ = ⟨v,u⟩), linearity in the first argument, positive definiteness (⟨v,v⟩ > 0 for v ≠ 0), and ⟨0,0⟩ = 0. The standard dot product on Rⁿ is the prototype, but inner products can be defined on spaces of functions, matrices, and polynomials. The norm induced by an inner product is ‖v‖ = √⟨v,v⟩, and the angle between vectors is determined by cos θ = ⟨u,v⟩/(‖u‖‖v‖). The Cauchy-Schwarz inequality |⟨u,v⟩| ≤ ‖u‖‖v‖ holds in every inner product space.

## How It's Best Learned
Verify all four axioms for the standard dot product, then explore an inner product on polynomials defined by integration. This demonstrates how the abstract framework encompasses very different contexts with the same theorems.

## Common Misconceptions
- An inner product is NOT just multiplication of scalars — it is a bilinear form satisfying specific axioms.
- The axiom often called 'conjugate symmetry' in complex spaces becomes plain symmetry in real spaces, which can cause confusion when reading complex-vector-space texts.
- Positive definiteness requires ⟨v,v⟩ > 0 for NONZERO v; zero is the only vector with zero inner product with itself.
