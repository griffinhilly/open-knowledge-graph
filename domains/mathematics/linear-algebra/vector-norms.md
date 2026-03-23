---
id: vector-norms
title: Vector Norms and Magnitude
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-operations
  type: hard
- id: square-roots-intro
  type: hard
builds-toward:
- dot-product
- orthogonality-and-orthonormal-sets
- matrix-norms
tags:
- vectors
- norms
- magnitude
- distance
stage: formal-systems
status: validated
---

# Vector Norms and Magnitude

## Core Idea
The norm (or magnitude) of a vector is a real number measuring its length, computed as ||v|| = √(v₁² + v₂² + ... + vₙ²). Norms generalize distance to n-dimensional space and satisfy key properties: ||cv|| = |c| ||v|| and the triangle inequality. Unit vectors (norm 1) form the basis for orthonormal sets.

## How It's Best Learned
Start with 2D and 3D visualization of distance formula. Then extend algebraically to R^n. Normalize vectors by dividing by their norm to create unit vectors in the same direction.

## Questions

```yaml
- question: "What is the distance between vectors u = (1, 3, −2) and v = (4, 7, −2) in ℝ³?"
  type: multiple-choice
  options:
    - "||u|| − ||v||"
    - "||u + v|| = √(5² + 10² + (−4)²)"
    - "||u − v|| = √((1−4)² + (3−7)² + (−2−(−2))²) = √(9 + 16 + 0) = 5"
    - "√(1² + 3² + (−2)²) − √(4² + 7² + (−2)²)"
  answer: 2
  explanation: "Distance between two vectors is defined as ||u − v||, the norm of the displacement vector. Here u − v = (1−4, 3−7, −2−(−2)) = (−3, −4, 0), so ||u − v|| = √(9 + 16 + 0) = 5. Subtracting individual norms (options A and D) confuses the distance between vectors with the difference of their lengths — a common error that produces a different, generally meaningless quantity."

- question: "If v = (−3, 4), what is ||−2v||?"
  type: multiple-choice
  options:
    - "−10, because scaling by −2 makes the norm negative"
    - "0, because −2 and v have opposite signs that cancel"
    - "5, because negating v doesn't change its norm, so multiplying by −2 and negating cancels out"
    - "10, because ||cv|| = |c| ||v||, so ||−2v|| = |−2| × ||v|| = 2 × 5 = 10"
  answer: 3
  explanation: "The scaling property of norms is ||cv|| = |c| ||v||, using the absolute value of the scalar. Here ||v|| = √(9 + 16) = 5, so ||−2v|| = |−2| × 5 = 10. Norms are always non-negative — a norm can never be negative, so option A is impossible. Option C makes the error of thinking −2 and the negation cancel; they don't, because |−2| = 2, not 0."

- question: "The triangle inequality for norms states that ||u + v|| = ||u|| + ||v|| for any two vectors."
  type: true-false
  answer: false
  explanation: "The triangle inequality is ||u + v|| ≤ ||u|| + ||v||, with equality holding only when u and v point in exactly the same direction. Geometrically: the direct path (||u + v||) is never longer than the two-leg detour (going ||u|| then ||v||), but it is shorter whenever the two vectors are not collinear and pointing the same way. The inequality is ≤, not =."

- question: "Dividing any nonzero vector by its norm produces a unit vector that points in the same direction as the original vector."
  type: true-false
  answer: true
  explanation: "This is the normalization procedure: v̂ = v/||v||. Its norm is ||v/||v||| = (1/||v||)||v|| = 1, confirming it is a unit vector. Dividing by a positive scalar (||v|| > 0 for nonzero v) preserves direction. Normalization lets you separate a vector's direction from its magnitude, which is fundamental to defining orthonormal bases and unit direction vectors."

- question: "Why does the scaling property use |c| (absolute value of the scalar) rather than just c, and what geometric fact does this reflect?"
  type: short-answer
  answer: "The absolute value is necessary because length is always non-negative. If c = −3, scaling v by −3 reverses its direction but triples its length — the result has length 3||v||, not −3||v||. Geometrically, negating a vector flips its direction but leaves its length unchanged, and multiplying by a negative scalar scales the length by the magnitude of that scalar. The absolute value |c| captures the 'how much stretching' while ignoring the sign that encodes direction reversal."
  explanation: "This is a subtle but important point about how norms interact with scalar multiplication. Norms measure geometric length, which is orientation-independent — the length of a displacement doesn't change if you flip its direction. The absolute value in ||cv|| = |c|||v|| is what ensures norms stay non-negative and measure pure magnitude, consistent with all three norm properties."
```

## Explainer

You already know how to work with vectors in ℝⁿ — adding them, scaling them, working with their components. The **norm** gives you the one thing that's been missing: a way to measure how *long* a vector is. In ℝ² and ℝ³ you've likely seen this as the distance formula from the origin: if v = (3, 4), its length is √(3² + 4²) = √25 = 5. The norm simply extends this to any number of dimensions: for v = (v₁, v₂, ..., vₙ), we define **||v|| = √(v₁² + v₂² + ... + vₙ²)**. This is called the Euclidean norm or L2 norm.

The norm satisfies three properties that any reasonable notion of "length" should have. First, ||v|| ≥ 0, with equality only when v is the zero vector — a nonzero displacement always has positive length. Second, scaling: **||cv|| = |c| ||v||**, so doubling a vector doubles its length and negating it doesn't change the length (the absolute value of the scalar is what matters, not its sign). Third, the **triangle inequality**: ||u + v|| ≤ ||u|| + ||v||. This is the geometric fact that the straight-line path is never longer than the two-leg detour — a constraint that turns out to be essential in more abstract settings.

One immediate application is **normalization**: given any nonzero vector v, the vector v/||v|| has norm 1 and points in exactly the same direction as v. This is called a **unit vector**. Unit vectors let you separate "direction" from "magnitude" — useful whenever you care about orientation without caring about scale (as in defining orthonormal bases). The standard basis vectors e₁ = (1, 0, ..., 0), e₂ = (0, 1, ..., 0), and so on are the canonical unit vectors in ℝⁿ.

The norm also gives you distance between two vectors: d(u, v) = ||u − v||, the length of the displacement vector from v to u. This distance formula underpins nearest-neighbor algorithms, error measurements in least squares, and convergence criteria throughout analysis. When you move to inner product spaces and orthogonality, you'll see that the Euclidean norm is derived from the dot product via ||v|| = √(v · v) — so norms and inner products are tightly linked.
