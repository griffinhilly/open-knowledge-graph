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

## Explainer

The **null space** of a matrix A, written nul(A), is the set of all vectors x such that Ax = 0. You already know from Gaussian elimination how to solve this: row-reduce A to RREF and read off the solutions. What the null space concept adds is a structural observation — the solution set is not just a collection of vectors, it is a **subspace**. It contains the zero vector, it is closed under addition (if Ax = 0 and Ay = 0, then A(x + y) = 0), and it is closed under scalar multiplication. Every solution you find inherits this geometric structure.

The connection to subspaces from your prerequisite makes this concrete. When you row-reduce Ax = 0 and find free variables, each free variable corresponds to one independent direction within the null space. If there are two free variables, the null space is a plane through the origin; if one, it is a line; if none, only the zero vector satisfies Ax = 0. The number of free variables is the **nullity** — the dimension of nul(A). This is why nullity counts free variables precisely: each free variable parameterizes one independent direction in the solution set.

The term **kernel** (from linear transformation theory) refers to the same object. When you think of A not as a grid of numbers but as a function T(x) = Ax that maps R^n → R^m, the kernel is everything that maps to zero — the set of inputs that A "collapses." A large null space means A collapses many directions; a trivial null space (only the zero vector) means A is injective. The nullity therefore measures how much information A destroys.

To find a basis for nul(A), row-reduce to RREF, express pivot variables in terms of free variables, then write x as a linear combination of vectors — one per free variable. These vectors are the basis for nul(A). This procedure is mechanical, but the key insight is conceptual: the free variables are the degrees of freedom in the solution, and each one contributes exactly one dimension to the null space.
