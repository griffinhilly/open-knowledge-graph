---
id: compact-operators
title: Compact Operators
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: bounded-linear-operators
  type: hard
- id: compact-sets-heine-borel
  type: soft
builds-toward:
- spectral-theorem-compact-self-adjoint
tags:
- operators
- spectral-theory
stage: advanced
status: draft
---

# Compact Operators

## Core Idea
A bounded operator T: X → Y is compact if it maps bounded sets to relatively compact sets. Compact operators have discrete spectrum (except possibly 0) consisting of eigenvalues, behaving like infinite-dimensional matrices.

## Explainer

In finite dimensions, a linear operator on ℝⁿ is just a matrix, and the image of a bounded set under a matrix is always bounded and closed — hence compact, by Heine-Borel. This is so automatic in finite dimensions that it seems trivial. In infinite-dimensional spaces, it fails: the identity operator maps the closed unit ball to itself, which is not compact in infinite dimensions (no sequence of unit vectors must have a convergent subsequence). **Compact operators** are the class of operators that recover this finite-dimensional behavior even in infinite-dimensional spaces.

Formally, a **bounded linear operator** T: X → Y is **compact** if, for every bounded sequence (xₙ) in X, the image sequence (Txₙ) has a convergent subsequence in Y. Equivalently, T maps bounded sets to relatively compact sets (sets whose closure is compact). You can think of compact operators as those that "compress" the infinite-dimensional structure of X into something essentially finite-dimensional in Y — they squeeze an infinite amount of input data down to a compact, highly constrained output.

The spectral behavior of compact operators is the main reason they are studied. For a compact operator on a Banach or Hilbert space, the spectrum outside {0} consists entirely of **eigenvalues** forming a discrete set — either finite, or a sequence converging to 0. This is exactly the behavior of an eigenvalue decomposition for a finite matrix. In contrast, a general bounded operator can have continuous spectrum with no eigenvalues at all. This discreteness makes compact operators tractable: you can analyze them through their eigenvalues and eigenvectors, in close analogy with diagonalizing a matrix.

The canonical example is an **integral operator** Tf(x) = ∫ K(x, y) f(y) dy with a square-integrable kernel K. These arise throughout differential equations and mathematical physics, and their compactness (when K is sufficiently regular) is what makes spectral methods for integral equations work. Understanding compact operators is the gateway to the spectral theorem for compact self-adjoint operators — the infinite-dimensional analogue of symmetric matrix diagonalization.
