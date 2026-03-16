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
status: draft
---

# Subspaces

## Core Idea
A subspace W of vector space V is a nonempty subset closed under addition and scalar multiplication. Equivalently, W is nonempty and cw₁ + w₂ ∈ W for all scalars c and w₁, w₂ ∈ W. Examples include lines and planes through the origin in R³, the null space of a matrix, and polynomial subspaces.

## Explainer

From your prerequisite on vector spaces, you know that the defining property of a vector space is **closure**: adding two vectors or scaling a vector always stays within the space. A **subspace** is simply a subset that inherits this same closure property — it is a vector space in its own right, living inside a larger one. The subspace does not need its own separate set of axioms; it borrows everything from the ambient space, and you only need to verify that it does not "escape" when you add or scale.

The two closure conditions — closed under addition and closed under scalar multiplication — are the only things you need to check beyond the subset being nonempty. Every other vector space property follows automatically. The zero vector is guaranteed: if w is in W, then 0·w = 0 must be in W by closure under scalar multiplication. Additive inverses are guaranteed: −w = (−1)·w must be in W for the same reason. This is a major shortcut — instead of verifying eight axioms, you verify two conditions and nonemptiness.

The geometric picture in R³ makes the origin condition intuitive. Lines and planes through the origin are subspaces; lines and planes that miss the origin are not. This is not arbitrary. If a subset does not contain 0, it cannot be closed under scalar multiplication: scaling any vector by 0 must give 0, but 0 is not in the subset. Equivalently, a plane at height z = 1 fails to be a subspace because it is not closed under addition: take two vectors on the plane, add them, and you land at z = 2, outside the plane.

Subspaces are the raw material for virtually everything that follows in linear algebra. The **null space** of a matrix (all vectors x with Ax = 0) is a subspace — it captures the "lost information" in the transformation. The **column space** (all vectors Ax as x ranges over all inputs) is a subspace — it captures the "reachable outputs." Together, the null space and column space answer the questions "when does Ax = b have a solution?" and "how many solutions does it have?" Understanding subspaces is the structural foundation on which basis, dimension, rank, and the fundamental theorem of linear algebra are all built.
