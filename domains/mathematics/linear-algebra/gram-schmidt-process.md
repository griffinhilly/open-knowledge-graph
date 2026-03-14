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
