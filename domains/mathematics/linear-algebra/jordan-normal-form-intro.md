---
id: jordan-normal-form-intro
title: Jordan Normal Form and Generalized Eigenvectors
domain: mathematics
course: linear-algebra
prerequisites:
- id: diagonalization-similar-matrices
  type: hard
builds-toward:
- matrix-exponential
tags:
- jordan-form
- generalized-eigenvectors
- canonical-form
stage: formal-systems
status: draft
---

# Jordan Normal Form and Generalized Eigenvectors

## Core Idea
Not all matrices are diagonalizable. Jordan normal form J is block-diagonal with Jordan blocks (eigenvalue λ on diagonal, 1s on superdiagonal). Every matrix A is similar to its Jordan form: A = PJP⁻¹. Generalized eigenvectors extend eigenvectors to fill out Jordan blocks. Jordan form reveals algebraic and geometric multiplicities and enables computing matrix functions.

## Explainer

From diagonalization, you know the ideal situation: a matrix A is diagonalizable exactly when it has enough eigenvectors to form a basis. When that happens, A = PDP⁻¹ where D is diagonal, and everything simplifies — powers of A become powers of D, and the geometry is transparent. But many important matrices fail this test. The matrix [[2,1],[0,2]] has eigenvalue λ=2 with algebraic multiplicity 2, but only one linearly independent eigenvector. There is no invertible P that diagonalizes it. Jordan normal form is the structure theorem that salvages the situation: instead of a diagonal, you get something that is *almost* diagonal.

A **Jordan block** J_k(λ) is a k×k matrix with λ on every diagonal entry and 1 on every superdiagonal entry, and zeros everywhere else. A 2×2 Jordan block for λ=2 is exactly [[2,1],[0,2]]. Every square matrix A over ℂ is similar to a block-diagonal matrix built from Jordan blocks — this is its **Jordan normal form**. The sizes of the blocks are determined by the matrix itself, not by choice. Crucially, the number of distinct Jordan blocks for a given eigenvalue λ equals the geometric multiplicity (the dimension of the eigenspace), while the sum of their sizes equals the algebraic multiplicity. Diagonalizable matrices simply happen to have all Jordan blocks of size 1.

To fill out a Jordan block of size k, you need a chain of k vectors: a true eigenvector v₁ (satisfying (A − λI)v₁ = 0) together with **generalized eigenvectors** v₂, v₃, …, vₖ satisfying (A − λI)vᵢ = vᵢ₋₁. These generalized eigenvectors live in the **generalized eigenspace** — the kernel of (A − λI)^k for large enough k. They are not eigenvectors in the classical sense (applying A to them does not simply scale them), but they capture the "near-diagonal" action that the Jordan block encodes.

Jordan form unlocks matrix functions. To compute e^(At) or A^n, you write A = PJP⁻¹ and work with e^(Jt) or J^n. A Jordan block raised to a power produces a triangular matrix with polynomial entries — the 1s on the superdiagonal generate polynomial growth via the binomial theorem. This is why, for example, defective systems of differential equations (those without enough eigenvectors) produce solutions involving both exponentials and polynomial terms like te^(λt). The Jordan block is precisely the algebraic structure responsible for that behavior.

The key diagnostic numbers are the **algebraic multiplicity** (how often λ appears as a root of the characteristic polynomial) and the **geometric multiplicity** (the dimension of the eigenspace ker(A − λI)). If geometric = algebraic for every eigenvalue, the matrix is diagonalizable and all Jordan blocks are 1×1. If geometric < algebraic for any eigenvalue, at least one block has size ≥ 2, and you must use generalized eigenvectors. Finding the Jordan form of a specific matrix comes down to computing these multiplicities and solving the chain equations — a procedure that is conceptually clean once you understand what the blocks represent.
