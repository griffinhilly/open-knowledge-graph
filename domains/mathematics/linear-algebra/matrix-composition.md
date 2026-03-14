---
id: matrix-composition
title: Composition of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: transformation-matrices
  type: hard
- id: composition-of-functions
  type: soft
builds-toward:
- diagonalization
- change-of-basis
tags:
- composition
- matrix multiplication
- successive transformations
- order of operations
stage: formal-systems
status: validated
---

# Composition of Linear Transformations

## Core Idea
The composition of two linear transformations T: Rⁿ → Rᵐ and S: Rᵐ → Rᵖ is the linear transformation S ∘ T: Rⁿ → Rᵖ given by (S ∘ T)(x) = S(T(x)). If A is the standard matrix of T and B is the standard matrix of S, then the standard matrix of S ∘ T is the matrix product BA. This reveals why matrix multiplication is defined the way it is: it encodes function composition. Because function composition is not commutative, matrix multiplication is generally not commutative either (BA ≠ AB).

## How It's Best Learned
Apply two successive geometric transformations (e.g., rotate then reflect) and observe that the combined effect equals multiplication by the product of the two matrices in the correct order. Experiment with reversing the order to see non-commutativity explicitly.

## Common Misconceptions
- The order of composition is reversed in matrix multiplication: applying T first then S gives BA, not AB.
- Students confuse 'linear combination of matrices' (componentwise) with 'matrix product' (composition); these are entirely different operations.
- Matrix multiplication is associative (A(BC) = (AB)C), which directly mirrors the associativity of function composition.
