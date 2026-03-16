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

## Explainer

The key insight is that matrix multiplication is not an arbitrary algebraic recipe — it is function composition in disguise. You've already learned that a matrix represents a linear transformation: a rule that rotates, scales, shears, or reflects every vector in the input space. Now suppose you want to apply two transformations in sequence: first T, then S. This is exactly what function composition means — (S ∘ T)(x) = S(T(x)) — and multiplying the matrices in the correct order is how that composition is encoded.

To build concrete intuition: suppose T rotates vectors 90° counterclockwise (represented by matrix A) and S reflects across the x-axis (represented by matrix B). Applying T then S to a vector **v** means computing S(T(**v**)) = B(A**v**) = (BA)**v**. The combined transformation "rotate then reflect" is captured by the single matrix BA. This is why the transformation applied first appears *rightmost* in the product: the rightmost matrix acts first, matching the way function composition is written right-to-left.

The **non-commutativity** of matrix multiplication (BA ≠ AB in general) is not an algebraic quirk — it directly reflects that "rotate then reflect" is a different transformation than "reflect then rotate." Test this geometrically: take the point (1, 0), rotate it 90° counterclockwise to (0, 1), then reflect across the x-axis to (0, −1). Now reverse the order: reflect (1, 0) to (1, 0) first (already on the x-axis), then rotate to (0, 1). Different result. The matrices are doing the honest arithmetic of this asymmetry.

**Associativity**, on the other hand, holds because function composition is associative: it doesn't matter how you group a chain of transformations, as long as you preserve their order. A(BC) = (AB)C because applying C, then B, then A gives the same result regardless of whether you compute B∘C first or A∘B first. This means you can parenthesize a long chain of matrix multiplications however is computationally convenient — but you can never reorder the factors.
