---
id: gram-schmidt-process
title: Gram-Schmidt Orthogonalization Process
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonal-vectors-orthonormal-bases
  type: hard
builds-toward:
- least-squares-approximation
tags:
- gram-schmidt
- orthogonalization
- basis
stage: formal-systems
status: draft
---

# Gram-Schmidt Orthogonalization Process

## Core Idea
The Gram-Schmidt process converts any basis into an orthonormal basis by iterative orthogonalization: orthogonalize each vector against all previous ones. Starting with v₁, compute u_k = v_k − Σ_{j<k} ⟨v_k, e_j⟩e_j and normalize. The process yields an orthonormal basis spanning the same space.

## Explainer

You already know what an **orthonormal basis** is: a set of basis vectors that are mutually perpendicular (orthogonal) and each has length 1 (unit vectors). Working in an orthonormal basis makes calculations dramatically simpler — projections reduce to dot products, coordinates are just inner products, and many matrix algorithms become numerically stable. The Gram-Schmidt process is the algorithm for building such a basis starting from any ordinary basis you happen to have.

The key geometric idea is **projection and subtraction**. Suppose you have two vectors, v₁ and v₂, that are not perpendicular. Take v₁ as your first basis vector (just normalize it to get e₁). Now, v₂ points in some direction that has a component *along* e₁ and a component *perpendicular* to e₁. The component along e₁ is the projection: proj = ⟨v₂, e₁⟩ · e₁. If you subtract that projection from v₂, you get a new vector that is perpendicular to e₁ by construction — you've stripped out everything v₂ shared with the e₁ direction. Normalize what's left and you have e₂. Two orthonormal vectors, done.

The process extends by induction. For the k-th vector vₖ, subtract away its projection onto *every* basis vector already computed: uₖ = vₖ − ⟨vₖ, e₁⟩e₁ − ⟨vₖ, e₂⟩e₂ − … − ⟨vₖ, e_{k−1}⟩e_{k−1}. Each subtraction removes the component of vₖ that overlaps with a previously established direction, leaving a remainder that is perpendicular to all of them. Normalize this remainder to get eₖ. Crucially, the resulting orthonormal set spans exactly the same subspace as the original vectors — you haven't changed *what* space you're describing, only *how* you're describing it.

This process has a matrix factorization interpretation: Gram-Schmidt on the columns of a matrix A produces the **QR decomposition**, A = QR, where Q has orthonormal columns and R is upper triangular. The QR decomposition is one of the workhorses of numerical linear algebra — it underlies the standard algorithm for computing eigenvalues and is the basis of stable least-squares solvers. When you later study least-squares approximation, you'll see that the orthogonal projections Gram-Schmidt builds are exactly the geometry behind finding the best-fit solution when a system has no exact answer.
