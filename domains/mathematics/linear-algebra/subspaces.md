---
id: subspaces
title: Subspaces
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces
  type: hard
builds-toward:
- linear-independence
- basis-and-dimension
- null-space
- column-space
tags:
- subspaces
- vector-subspace
- closure
stage: formal-systems
status: validated
---

# Subspaces

## Core Idea
A subspace W of vector space V is a nonempty subset closed under addition and scalar multiplication. Equivalently, W is nonempty and cw₁ + w₂ ∈ W for all scalars c and w₁, w₂ ∈ W. Examples include lines and planes through the origin in R³, the null space of a matrix, and polynomial subspaces.

## Questions

```yaml
- question: "The set S = {(x, y) ∈ ℝ² : x + y = 1} is proposed as a subspace of ℝ². What is the correct verdict?"
  type: multiple-choice
  options:
    - "It is a subspace because it is a line and lines are subspaces of ℝ²"
    - "It is not a subspace because it fails closure under scalar multiplication: 0·(1, 0) = (0, 0) ∉ S"
    - "It is not a subspace because it contains uncountably many vectors"
    - "It is a subspace because any two vectors in S can be added together"
  answer: 1
  explanation: "The failure is immediately detected by the zero vector test: every subspace must contain the zero vector (since c·w = 0 when c = 0), but (0,0) does not satisfy x + y = 1. Also, addition fails: (1,0) and (0,1) are both in S but their sum (1,1) has 1+1=2 ≠ 1. Option A contains the key misconception — lines are subspaces only when they pass through the origin."

- question: "To verify that a nonempty subset W of vector space V is a subspace, the minimum you need to check is:"
  type: multiple-choice
  options:
    - "W contains the zero vector and all additive inverses of its elements"
    - "W is closed under addition and closed under scalar multiplication"
    - "W satisfies all eight vector space axioms applied to its elements"
    - "W is closed under addition and contains the zero vector"
  answer: 1
  explanation: "Closure under addition and scalar multiplication is both necessary and sufficient. The zero vector follows automatically: if w ∈ W, then 0·w = 0 must be in W by scalar closure. Additive inverses follow: −w = (−1)·w must be in W. All other axioms are inherited from the ambient space V. Option D is the common shortcut error — you do not need to verify the zero vector separately; it is a consequence of scalar closure."

- question: "Every subspace of ℝⁿ must contain the zero vector."
  type: true-false
  answer: true
  explanation: "True. If W is a nonempty subspace and w ∈ W, then 0·w = 0 must be in W by closure under scalar multiplication. The zero vector is guaranteed — it is a theorem, not an extra axiom. A subset that does not contain 0 cannot be a subspace, which is why the fastest way to disprove a subspace claim is to check whether 0 is in the set."

- question: "A nonempty subset of ℝ² that is closed under vector addition must be a subspace."
  type: true-false
  answer: false
  explanation: "False. Closure under addition alone is insufficient — you also need closure under scalar multiplication. Consider the set of all vectors with integer coordinates: {(m, n) : m, n ∈ ℤ}. This is closed under addition, but (0.5)·(1, 0) = (0.5, 0) is not in the set, so it fails scalar closure. Both conditions are required."

- question: "Explain why a plane in ℝ³ that does not pass through the origin cannot be a subspace, using the closure conditions."
  type: short-answer
  answer: "A plane not through the origin fails closure under scalar multiplication: if p is any vector on the plane, then 0·p = 0 must belong to the plane by closure, but the zero vector is not on a plane that misses the origin. Equivalently, adding two vectors on the plane generally leaves the plane (their sum shifts to double the displacement from the origin). Subspaces must pass through the origin because scaling any vector by 0 must yield the zero vector, which must stay in the set."
  explanation: "The origin requirement is a theorem, not an arbitrary restriction. It distinguishes subspaces (vector-space-compatible subsets) from affine subspaces (translates of subspaces). A plane at height z = 1 is an affine subspace — it has the right shape but is displaced from the origin — and fails both closure conditions. Geometrically, any subset closed under scaling must include 0 (the limit as the scalar approaches 0), so it must pass through the origin."
```

## Explainer

From your prerequisite on vector spaces, you know that the defining property of a vector space is **closure**: adding two vectors or scaling a vector always stays within the space. A **subspace** is simply a subset that inherits this same closure property — it is a vector space in its own right, living inside a larger one. The subspace does not need its own separate set of axioms; it borrows everything from the ambient space, and you only need to verify that it does not "escape" when you add or scale.

The two closure conditions — closed under addition and closed under scalar multiplication — are the only things you need to check beyond the subset being nonempty. Every other vector space property follows automatically. The zero vector is guaranteed: if w is in W, then 0·w = 0 must be in W by closure under scalar multiplication. Additive inverses are guaranteed: −w = (−1)·w must be in W for the same reason. This is a major shortcut — instead of verifying eight axioms, you verify two conditions and nonemptiness.

The geometric picture in R³ makes the origin condition intuitive. Lines and planes through the origin are subspaces; lines and planes that miss the origin are not. This is not arbitrary. If a subset does not contain 0, it cannot be closed under scalar multiplication: scaling any vector by 0 must give 0, but 0 is not in the subset. Equivalently, a plane at height z = 1 fails to be a subspace because it is not closed under addition: take two vectors on the plane, add them, and you land at z = 2, outside the plane.

Subspaces are the raw material for virtually everything that follows in linear algebra. The **null space** of a matrix (all vectors x with Ax = 0) is a subspace — it captures the "lost information" in the transformation. The **column space** (all vectors Ax as x ranges over all inputs) is a subspace — it captures the "reachable outputs." Together, the null space and column space answer the questions "when does Ax = b have a solution?" and "how many solutions does it have?" Understanding subspaces is the structural foundation on which basis, dimension, rank, and the fundamental theorem of linear algebra are all built.
