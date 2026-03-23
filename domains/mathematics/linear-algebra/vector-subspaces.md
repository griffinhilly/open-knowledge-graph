---
id: vector-subspaces
title: Subspaces and Closure Properties
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces-definition
  type: hard
builds-toward:
- span-spanning-set
- basis-definition
- dimension-vector-space
tags:
- subspaces
- closure
- subsets
stage: formal-systems
status: validated
---

# Subspaces and Closure Properties

## Core Idea
A subspace of a vector space V is a non-empty subset W that is closed under addition and scalar multiplication. Equivalently, W is a subspace if and only if for any u, v in W and scalar c, we have u + v and cu in W. Subspaces inherit all vector space properties from V.

## How It's Best Learned
Start with geometric examples: lines and planes through the origin in R^3 are subspaces. Test the closure conditions explicitly. Practice with null spaces and column spaces of matrices.

## Common Misconceptions
- Forgetting that subspaces must contain the zero vector.
- Thinking lines or planes not through the origin are subspaces; they are affine subsets, not subspaces.

## Questions

```yaml
- question: "Which of the following subsets of ℝ³ is a subspace?"
  type: multiple-choice
  options:
    - "W = {(x, y, z) | x + y + z = 1} (a plane not passing through the origin)"
    - "W = {(x, y, z) | x ≥ 0} (a half-space)"
    - "W = {(x, y, z) | x = y = 0} (the z-axis)"
    - "W = {(x, y, z) | x² + y² + z² = 1} (the unit sphere)"
  answer: 2
  explanation: "The z-axis passes through the origin, and any two vectors of the form (0,0,a) and (0,0,b) sum to (0,0,a+b), still on the z-axis; scalar multiples c(0,0,a) = (0,0,ca) stay on the z-axis. Both closure conditions hold. All other options fail the zero vector test: (0,0,0) does not satisfy x+y+z=1, x≥0 alone isn't sufficient for a subspace (the zero vector is in it but (1,0,0)+(−2,0,0)=(−1,0,0) which fails x≥0), or the sphere doesn't contain the zero vector."

- question: "A student notices that A = [[1,0],[0,0]] and B = [[0,0],[0,1]] both have determinant 0, and concludes the set S = {2×2 matrices with det = 0} is closed under addition. Why is this reasoning flawed?"
  type: multiple-choice
  options:
    - "The student is correct — the sum of two singular matrices is always singular"
    - "A+B = [[1,0],[0,1]], which has determinant 1 ≠ 0, so S is not closed under addition"
    - "The reasoning fails because the determinant is not defined for sums of matrices"
    - "The student is correct that S is closed under addition, but S still fails to be a subspace because it lacks the zero matrix"
  answer: 1
  explanation: "A+B equals the identity matrix, which has determinant 1, not 0. This single counterexample shows S is not closed under addition and therefore cannot be a subspace. Option D is wrong because the zero matrix (det = 0) IS in S — the closure failure is what disqualifies it. This illustrates a general principle: being in a set does not mean sums stay in the set."

- question: "The null space of any matrix A (the set of all vectors x with Ax = 0) is always a subspace."
  type: true-false
  answer: true
  explanation: "All three conditions hold: (1) A·0 = 0, so the zero vector is in the null space. (2) If Au = 0 and Av = 0, then A(u+v) = Au+Av = 0+0 = 0, so u+v is in the null space. (3) If Au = 0, then A(cu) = c(Au) = c·0 = 0, so cu is in the null space. The null space is one of the fundamental subspaces of linear algebra, and its subspace property follows directly from the linearity of matrix multiplication."

- question: "A subset W of ℝ² that is closed under scalar multiplication must be a subspace."
  type: true-false
  answer: false
  explanation: "Closure under scalar multiplication alone is insufficient. A counterexample: W = {(x,0) | x ∈ ℝ} ∪ {(0,y) | y ∈ ℝ} (the union of the two coordinate axes). Any scalar multiple of a vector on the x-axis stays on the x-axis, and similarly for the y-axis — so W is closed under scalar multiplication. But (1,0) + (0,1) = (1,1), which is not on either axis. W fails closure under addition, so it is not a subspace. Both closure conditions are necessary."

- question: "Why must every subspace contain the zero vector? Show why this follows from the closure conditions rather than needing to be stated as a separate requirement."
  type: short-answer
  answer: "Since a subspace W is non-empty, it contains some vector v. By closure under scalar multiplication, 0·v must also be in W. Since 0·v = 0 (the zero vector), W must contain the zero vector. This means the zero-vector condition is actually redundant — it follows automatically from non-emptiness combined with closure under scalar multiplication. In practice, checking for the zero vector first is a useful shortcut: if the zero vector is absent, no further checking is needed."
  explanation: "This is a common point of confusion: the three conditions (contains zero, closed under addition, closed under scalar multiplication) are often listed separately, but the first is actually implied by the other two plus non-emptiness. The practical takeaway is to always check for the zero vector first — it's the fastest way to rule out a non-subspace — while understanding that its presence is forced by the deeper closure properties."
```

## Explainer

From your study of vector spaces, you know that a vector space comes with two operations — addition and scalar multiplication — and a list of axioms that govern them. A **subspace** is a subset of a vector space that is itself a vector space under the same operations. Instead of checking all eight or ten axioms from scratch, there is a shortcut: a non-empty subset W of a vector space V is a subspace if and only if it is **closed under addition** (u + v ∈ W whenever u, v ∈ W) and **closed under scalar multiplication** (cu ∈ W whenever c is a scalar and u ∈ W). Both conditions together force W to be a vector space in its own right.

The geometric picture in ℝ³ is the most direct way to build intuition. A line through the origin is a subspace: stretch or shrink any vector on the line and you stay on the line; add two vectors on the line and you stay on the line. A plane through the origin is likewise a subspace for the same reasons. But a line or plane that does NOT pass through the origin fails immediately — add the zero vector to any element and you leave the set (unless the set contains the zero vector, which an off-origin line doesn't). This is the key diagnostic: **every subspace must contain the zero vector**. If your candidate set doesn't, it's not a subspace.

Two of the most important subspaces attached to a matrix A are the **column space** and the **null space**. The column space (or image) of A is the set of all vectors of the form Ax — it's a subspace of the output space. The null space (or kernel) of A is the set of all x with Ax = 0 — it's a subspace of the input space. Both are worth checking against the two closure conditions as an exercise; they will become central objects when you study span, basis, and dimension, since a central theorem (the rank-nullity theorem) quantifies how these two subspaces divide up the total space.

When you test whether a given set is a subspace, work methodically: first verify the zero vector is present, then check both closure conditions with arbitrary elements. If any condition fails, you have found a counterexample. If all conditions hold, you have a subspace. This two-condition test is one of the first genuinely efficient theorems in linear algebra — it collapses what could be a ten-axiom verification into two checks.
