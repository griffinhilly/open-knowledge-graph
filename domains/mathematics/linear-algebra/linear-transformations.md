---
id: linear-transformations
title: Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn
  type: hard
- id: matrices-intro
  type: soft
builds-toward:
- matrix-representation-linear-transformations
- composition-linear-transformations
- eigenvalues-and-eigenvectors
tags:
- linear-transformations
- functions
- preserves-structure
stage: formal-systems
status: validated
---

# Linear Transformations

## Core Idea
A linear transformation T: Rⁿ → Rᵐ satisfies T(cu + v) = cT(u) + T(v) for all scalars c and vectors u, v. Linear transformations preserve vector addition and scalar multiplication, making them algebraic homomorphisms. Every linear transformation is represented by a unique matrix A such that T(x) = Ax.

## Questions

```yaml
- question: "Which of the following functions T: ℝ² → ℝ² is a linear transformation?"
  type: multiple-choice
  options: ["T(x, y) = (x + 1, y)", "T(x, y) = (2x, 3y)", "T(x, y) = (x², y)", "T(x, y) = (x + y², x - y)"]
  answer: 1
  explanation: "T(x, y) = (2x, 3y) is linear: scaling and adding inputs produces scaled and added outputs. Option A fails because T(0, 0) = (1, 0) ≠ (0, 0) — a linear transformation must send the zero vector to zero. Option C fails because x² is not a linear operation. Option D fails because y² is not linear."

- question: "If T is a linear transformation, then T must send the zero vector to the zero vector."
  type: true-false
  answer: true
  explanation: "This follows directly from linearity. Setting c = 0 in T(cv) = cT(v) gives T(0) = T(0·v) = 0·T(v) = 0. This is a useful quick test: if a function doesn't send the zero vector to zero, it cannot be linear — which is exactly why T(x) = x + 1 fails despite looking almost linear."

- question: "What does it mean to say a linear transformation 'preserves structure', and which two operations does it preserve?"
  type: short-answer
  answer: "A linear transformation preserves vector addition and scalar multiplication. 'Preserving structure' means you get the same result whether you add or scale vectors first and then transform, or transform first and then add or scale."
  explanation: "Formally: T(u + v) = T(u) + T(v) and T(cv) = cT(v). This makes linear transformations algebraic homomorphisms — they respect the vector space structure. A non-linear function like T(x) = x² scrambles this structure: T(u + v) ≠ T(u) + T(v) in general."
```

## Explainer

You already know functions from earlier math — a function takes an input and produces an output. A linear transformation is a special kind of function that takes *vectors* as inputs and produces *vectors* as outputs, subject to two constraints that make it structurally well-behaved. These constraints are what give linear algebra its power.

The two conditions are: T(u + v) = T(u) + T(v), and T(cv) = cT(v). Together they can be compressed into the single condition T(cu + v) = cT(u) + T(v). Intuitively, this says it doesn't matter whether you "do the algebra first, then transform" or "transform first, then do the algebra" — you get the same answer. A transformation with this property is one we can analyze, compose, and invert in a clean, predictable way.

A critical consequence: every linear transformation sends the zero vector to the zero vector. Proof: T(0) = T(0·v) = 0·T(v) = 0. This gives you a quick test — if a function sends any input to a nonzero output when all inputs are zero, it is not linear. This disqualifies functions like T(x) = x + 1, which look almost linear but fail the zero-vector test.

The connection to matrices is fundamental: every linear transformation T: ℝⁿ → ℝᵐ can be represented by an m×n matrix A, where T(x) = Ax. To find A, you only need to know what T does to the standard basis vectors — linearity then determines T's behavior everywhere else. This matrix representation is the bridge to eigenvalues, determinants, and the rest of linear algebra.

Geometrically, linear transformations on ℝ² and ℝ³ include rotations, reflections, scaling, and projections — all operations that map straight lines to straight lines and keep the origin fixed. Non-linear operations like "shift everything right by 1" fail to be linear precisely because they move the origin. Keeping this geometric picture in mind helps you check whether a given transformation can possibly be linear.
