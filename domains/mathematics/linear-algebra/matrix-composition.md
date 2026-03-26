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

## Questions

```yaml
- question: "Matrix A represents a 90° counterclockwise rotation and matrix B represents a reflection across the x-axis. You want to apply the rotation FIRST and then the reflection. Which matrix product represents this composition?"
  type: multiple-choice
  options:
    - "AB — A is applied first, so it appears first (leftmost) in the product"
    - "BA — the first-applied transformation appears rightmost in the product"
    - "A + B — composition corresponds to matrix addition"
    - "Either AB or BA — matrix multiplication is commutative for rotations and reflections"
  answer: 1
  explanation: "For composition S ∘ T (apply T first, then S), the matrix product is BA where B is S's matrix and A is T's matrix. The rightmost matrix acts first, matching how function composition is written: S(T(x)) = B(Ax) = (BA)x. Option A is the most common error — students reason 'A goes first so it goes on the left,' which inverts the correct order. Option D is false: rotations and reflections generally do not commute."

- question: "You compute AB and BA for two non-identity transformation matrices and find AB ≠ BA. A classmate argues this is a flaw in the definition of matrix multiplication. The correct response is:"
  type: multiple-choice
  options:
    - "They're right — matrix multiplication should be made commutative to match scalar algebra"
    - "Non-commutativity is an error that only appears for certain matrix sizes"
    - "Non-commutativity directly reflects that applying transformation A then B gives a different result than B then A — it is geometrically necessary"
    - "This only happens for non-square matrices; square matrices always commute"
  answer: 2
  explanation: "Non-commutativity is not a flaw — it honestly reflects that geometric transformations generally do not commute. 'Rotate then reflect' and 'reflect then rotate' produce different outcomes; the matrices encode this asymmetry faithfully. Option D is false: most square matrices do not commute. The non-commutativity is a feature of the definition, not a bug."

- question: "Matrix multiplication is associative (A(BC) = (AB)C) because function composition is associative."
  type: true-false
  answer: true
  explanation: "Since matrix multiplication encodes function composition, all algebraic properties of function composition carry over directly. Composing three transformations gives the same result regardless of which pair you compute first — as long as you preserve their order. This directly explains why (AB)C = A(BC): both compute 'apply C, then B, then A' on any input vector."

- question: "If AB = BA for two matrices A and B, then A and B should represent the same transformation."
  type: true-false
  answer: false
  explanation: "Commutativity (AB = BA) holds for some pairs of distinct matrices without them being equal. Any matrix commutes with the identity matrix I and with scalar multiples of itself. Two matrices can commute while being completely different transformations. Commutativity is a special algebraic relationship, not evidence of equality or geometric similarity."

- question: "Why is the row-by-column dot product rule for matrix multiplication — which can seem arbitrary at first — actually the only sensible definition if matrices represent linear transformations?"
  type: short-answer
  answer: "Matrix multiplication must encode function composition. If A represents transformation T and B represents transformation S, the matrix for S ∘ T must satisfy M·v = B(Av) for all vectors v. Working out what entries M must have to satisfy this constraint forces exactly the row-by-column dot product formula. The rule isn't arbitrary — it is the unique formula you would derive by demanding that sequential application of transformations be representable as a single matrix-vector product."
  explanation: "Students who memorize the row-by-column rule without this motivation find matrix multiplication mysterious. Understanding the geometric underpinning makes it inevitable: multiply the matrices in the right order, and the product automatically encodes whatever combined transformation results from applying them in sequence."
```

## Explainer

The key insight is that matrix multiplication is not an arbitrary algebraic recipe — it is function composition in disguise. You've already learned that a matrix represents a linear transformation: a rule that rotates, scales, shears, or reflects every vector in the input space. Now suppose you want to apply two transformations in sequence: first T, then S. This is exactly what function composition means — (S ∘ T)(x) = S(T(x)) — and multiplying the matrices in the correct order is how that composition is encoded.

To build concrete intuition: suppose T rotates vectors 90° counterclockwise (represented by matrix A) and S reflects across the x-axis (represented by matrix B). Applying T then S to a vector **v** means computing S(T(**v**)) = B(A**v**) = (BA)**v**. The combined transformation "rotate then reflect" is captured by the single matrix BA. This is why the transformation applied first appears *rightmost* in the product: the rightmost matrix acts first, matching the way function composition is written right-to-left.

The **non-commutativity** of matrix multiplication (BA ≠ AB in general) is not an algebraic quirk — it directly reflects that "rotate then reflect" is a different transformation than "reflect then rotate." Test this geometrically: take the point (1, 0), rotate it 90° counterclockwise to (0, 1), then reflect across the x-axis to (0, −1). Now reverse the order: reflect (1, 0) to (1, 0) first (already on the x-axis), then rotate to (0, 1). Different result. The matrices are doing the honest arithmetic of this asymmetry.

**Associativity**, on the other hand, holds because function composition is associative: it doesn't matter how you group a chain of transformations, as long as you preserve their order. A(BC) = (AB)C because applying C, then B, then A gives the same result regardless of whether you compute B∘C first or A∘B first. This means you can parenthesize a long chain of matrix multiplications however is computationally convenient — but you can never reorder the factors.
