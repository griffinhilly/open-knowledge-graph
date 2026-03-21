---
id: null-space
title: Null Space and Kernel
domain: mathematics
course: linear-algebra
prerequisites:
- id: subspaces
  type: hard
- id: gaussian-elimination
  type: hard
builds-toward:
- rank-and-nullity-theorem
tags:
- null-space
- kernel
- homogeneous-solutions
stage: formal-systems
status: draft
---

# Null Space and Kernel

## Core Idea
The null space nul(A) is the set of all solutions to Ax = 0, found by Gaussian elimination. It is a subspace and equals the kernel of the linear transformation x ↦ Ax. Nullity(A) is the dimension of nul(A), equal to the number of free variables in RREF.

## Questions

```yaml
- question: "A 4×6 matrix A has rank 3. What is the dimension of its null space?"
  type: multiple-choice
  options:
    - "3"
    - "1"
    - "4"
    - "Cannot be determined without more information"
  answer: 0
  explanation: "By the rank-nullity theorem, rank(A) + nullity(A) = n, where n is the number of *columns*. Here n = 6 and rank = 3, so nullity = 6 − 3 = 3. The common error is using the number of rows (4) instead of columns (6): students subtract rank from 4 and get 1. The number of rows tells you the dimension of the output space (R⁴), not the dimension of the input space; nullity concerns free variables in the *input* space R⁶."

- question: "A student defines the null space as: 'the set of all x satisfying Ax = b for some right-hand side b.' What is wrong with this definition?"
  type: multiple-choice
  options:
    - "Nothing — this is equivalent to the correct definition"
    - "The null space is specifically the solutions to Ax = 0 (the zero vector), not Ax = b for a general b"
    - "The null space is a matrix, not a set of vectors"
    - "The null space only exists when A is square and invertible"
  answer: 1
  explanation: "The null space is exclusively the solution set of the *homogeneous* system Ax = 0. Allowing an arbitrary b on the right-hand side gives a different object: the solution set of a non-homogeneous system, which is either empty or an affine subspace (not passing through the origin). Only the homogeneous solution set is guaranteed to be a subspace — it always contains the zero vector and is closed under addition and scalar multiplication. The null space is defined by b = 0 specifically."

- question: "If the null space of matrix A contains only the zero vector, then the linear transformation T(x) = Ax is injective (one-to-one)."
  type: true-false
  answer: true
  explanation: "Injectivity means T(x₁) = T(x₂) implies x₁ = x₂. If Ax₁ = Ax₂, then A(x₁ − x₂) = 0, so x₁ − x₂ is in the null space. If the null space is trivial (only the zero vector), then x₁ − x₂ = 0, i.e., x₁ = x₂. Conversely, a non-trivial null space directly witnesses non-injectivity: any non-zero vector in nul(A) maps to 0 along with the zero vector itself."

- question: "The nullity of a matrix A equals the number of rows in its reduced row echelon form."
  type: true-false
  answer: false
  explanation: "Nullity equals the number of *free variables* in the RREF of A, not the number of rows. Free variables correspond to columns without pivot positions. If A is m×n with rank r, then there are n − r free variables, so nullity = n − r. The number of rows is m and determines the dimension of the output space; it has no direct relationship to the null space dimension."

- question: "A matrix A, when row-reduced to RREF, yields 4 free variables. What does this tell you about the null space, and what does it mean geometrically?"
  type: short-answer
  answer: "The null space has dimension 4 — it is a 4-dimensional subspace of the input space. Each free variable parameterizes one independent direction in the solution set of Ax = 0. Geometrically, the null space is a 4-dimensional flat (hyperplane through the origin) consisting of all vectors that A collapses to zero."
  explanation: "Each free variable contributes exactly one basis vector to nul(A). You find these basis vectors by setting each free variable to 1 (and others to 0) and solving for the pivot variables. The geometric picture is important: a 4-dimensional null space means A 'destroys' 4 independent directions — it collapses a 4-dimensional family of vectors to zero. The larger the null space, the more information A discards."
```

## Explainer

The **null space** of a matrix A, written nul(A), is the set of all vectors x such that Ax = 0. You already know from Gaussian elimination how to solve this: row-reduce A to RREF and read off the solutions. What the null space concept adds is a structural observation — the solution set is not just a collection of vectors, it is a **subspace**. It contains the zero vector, it is closed under addition (if Ax = 0 and Ay = 0, then A(x + y) = 0), and it is closed under scalar multiplication. Every solution you find inherits this geometric structure.

The connection to subspaces from your prerequisite makes this concrete. When you row-reduce Ax = 0 and find free variables, each free variable corresponds to one independent direction within the null space. If there are two free variables, the null space is a plane through the origin; if one, it is a line; if none, only the zero vector satisfies Ax = 0. The number of free variables is the **nullity** — the dimension of nul(A). This is why nullity counts free variables precisely: each free variable parameterizes one independent direction in the solution set.

The term **kernel** (from linear transformation theory) refers to the same object. When you think of A not as a grid of numbers but as a function T(x) = Ax that maps R^n → R^m, the kernel is everything that maps to zero — the set of inputs that A "collapses." A large null space means A collapses many directions; a trivial null space (only the zero vector) means A is injective. The nullity therefore measures how much information A destroys.

To find a basis for nul(A), row-reduce to RREF, express pivot variables in terms of free variables, then write x as a linear combination of vectors — one per free variable. These vectors are the basis for nul(A). This procedure is mechanical, but the key insight is conceptual: the free variables are the degrees of freedom in the solution, and each one contributes exactly one dimension to the null space.
