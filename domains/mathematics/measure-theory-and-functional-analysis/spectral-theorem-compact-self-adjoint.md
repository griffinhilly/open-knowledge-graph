---
id: spectral-theorem-compact-self-adjoint
title: Spectral Theorem for Compact Self-Adjoint Operators
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: bounded-linear-operators
  type: hard
- id: hilbert-spaces-definition
  type: hard
tags:
- spectral-theorem
- operators
stage: advanced
status: draft
---

# Spectral Theorem for Compact Self-Adjoint Operators

## Core Idea
The spectral theorem for compact self-adjoint operators states that such an operator T on a Hilbert space has an orthonormal basis of eigenvectors with eigenvalues λₙ → 0. This is the infinite-dimensional analogue of matrix diagonalization and is foundational for applications.

## Explainer

In finite dimensions, the spectral theorem for symmetric (self-adjoint) matrices tells you something remarkable: every real symmetric matrix can be diagonalized by an orthonormal basis of eigenvectors, and all its eigenvalues are real. This is the foundation for principal component analysis, vibration analysis, and quantum mechanics in finite-dimensional settings. The spectral theorem for compact self-adjoint operators is the correct generalization to infinite-dimensional Hilbert spaces — but some care is needed, because infinite-dimensional spaces behave quite differently from finite-dimensional ones.

The setting is a Hilbert space H (such as L²([0,1]) or ℓ²) and a bounded linear operator T: H → H that is both **compact** and **self-adjoint**. Recall that T is self-adjoint if ⟨Tx, y⟩ = ⟨x, Ty⟩ for all x, y — the operator equals its own adjoint, mirroring the symmetric matrix condition aᵢⱼ = aⱼᵢ. Compactness means T maps bounded sets to precompact sets (sets with compact closure) — intuitively, T "squishes" the infinite-dimensional unit ball into something that is essentially finite-dimensional in the limit. Many naturally occurring operators in analysis are compact: integral operators with square-integrable kernels, for instance.

The theorem states that T has at most countably many eigenvalues, all real, and the eigenvalues **λₙ → 0** as n → ∞. This convergence to zero is forced by compactness: if eigenvalues did not go to zero, the corresponding unit eigenvectors would form a bounded sequence with no convergent subsequence, contradicting compactness. More importantly, the eigenvectors form an **orthonormal basis** for H (or for the closure of the range of T, accounting for the kernel). This means every vector x ∈ H can be written as x = Σₙ ⟨x, eₙ⟩ eₙ and T acts by Tx = Σₙ λₙ ⟨x, eₙ⟩ eₙ. This is exactly diagonalization, just with an infinite orthonormal basis.

The proof strategy mirrors the finite-dimensional case but requires the Bolzano-Weierstrass property provided by compactness. One first shows the norm ‖T‖ is achieved as an eigenvalue (using the fact that T is self-adjoint, so ‖T‖ = sup{|⟨Tx, x⟩| : ‖x‖ = 1}, and the supremum is attained). One then restricts T to the orthogonal complement of the first eigenvector and repeats. Compactness ensures the process produces eigenvalues converging to zero, while self-adjointness ensures eigenvectors for distinct eigenvalues are orthogonal.

In applications, this theorem appears throughout mathematical physics and analysis. In quantum mechanics, observable quantities are represented by self-adjoint operators (often compact or with compact resolvent), and their eigenvalues are the possible measurement outcomes — the spectrum. In the theory of integral equations, solving Tf = g reduces to understanding the spectral decomposition of T. The condition λₙ → 0 explains why high-frequency components of an expansion are damped by a compact operator — such operators are "smoothing" in a precise sense, and their spectrum encodes the rate of that smoothing.
