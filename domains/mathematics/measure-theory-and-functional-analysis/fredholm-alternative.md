---
id: fredholm-alternative
title: Fredholm Alternative
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: spectral-theorem-compact-self-adjoint
  type: hard
tags:
- spectral-theory
stage: advanced
status: draft
---

# Fredholm Alternative

## Core Idea
For a compact operator T on a Banach space, either (I - T)(x) = y has a unique solution for every y, or (I - T)(x) = 0 has non-trivial solutions. This dichotomy determines solvability of integral equations.

## Explainer

The Fredholm Alternative is best understood by first recalling what happens in finite dimensions. If A is an n × n matrix and you want to solve Ax = b, there are two possibilities: either A is invertible, in which case there is a unique solution x = A⁻¹b for every b, or A is singular, in which case Ax = 0 has nontrivial solutions and Ax = b may have none at all. This is basic linear algebra. The Fredholm Alternative lifts this binary structure to infinite-dimensional function spaces, where the analysis is far less obvious.

Let T be a **compact operator** on a Banach space — the class of operators that map bounded sets to precompact sets. Your prerequisite work on the spectral theorem for compact self-adjoint operators prepared you for this: compactness provides the "almost finite-dimensional" behavior needed to recover the finite-dimensional dichotomy. The equation we study is (I − T)x = y, i.e., x − Tx = y. Here I − T is a perturbation of the identity by a compact operator. The theorem says: either I − T is bijective (unique solution for every y), or the homogeneous equation (I − T)x = 0 has nontrivial solutions. These two cases are mutually exclusive and exhaustive.

The deeper structure is even cleaner: if the null space of (I − T) is nontrivial, then the equation (I − T)x = y is solvable if and only if y is orthogonal (in the appropriate sense) to every solution of the adjoint homogeneous equation (I − T*)z = 0. This is the solvability condition, and it mirrors exactly the rank-nullity theorem you know from linear algebra: the equation Ax = b is solvable if and only if b is orthogonal to the null space of Aᵀ.

The **Fredholm Alternative** has direct applications to integral equations of the second kind: equations of the form x(t) − ∫K(t,s)x(s)ds = y(t). The integral operator is compact (under reasonable assumptions on K), so the abstract theorem applies immediately. Either the equation has a unique solution for every y, or the homogeneous equation has nontrivial solutions. In physics and engineering, this dichotomy determines whether a system has a unique steady state or exhibits resonance — the nontrivial solutions of (I − T)x = 0 are the "natural modes" of the system.

The proof uses the Baire category theorem and the spectral properties of compact operators to show that the spectrum of a compact operator consists of at most countably many eigenvalues accumulating only at zero, and that nonzero eigenvalues have finite-dimensional eigenspaces. This is why the finite-dimensional intuition survives: in the spectral directions corresponding to nonzero eigenvalues, T behaves like a finite matrix, and everywhere else, I − T is invertible. The Fredholm Alternative packages this structure into one clean solvability criterion.
