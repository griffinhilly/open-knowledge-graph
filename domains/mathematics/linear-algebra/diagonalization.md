---
id: diagonalization
title: Diagonalization
domain: mathematics
course: linear-algebra
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- least-squares-approximation
tags:
- diagonalization
- similarity
- powers
- exponentials
stage: formal-systems
status: draft
---

# Diagonalization

## Core Idea
Matrix A is diagonalizable if A = PDP⁻¹ where D is diagonal and P's columns are eigenvectors of A. Diagonalization simplifies computation: Aⁿ = PDⁿP⁻¹. An n × n matrix is diagonalizable iff it has n linearly independent eigenvectors, guaranteed if all eigenvalues are distinct.

## Explainer

From your work with eigenvalues and eigenvectors, you know that a vector **v** is an eigenvector of matrix A if Av = λv — multiplying by A just scales **v** by the eigenvalue λ. Diagonalization asks: what if *all* our basis vectors were eigenvectors? Then the matrix would be incredibly easy to work with, because it would just scale each coordinate independently.

Here is the construction. Suppose A is n × n and you can find n linearly independent eigenvectors **v₁, v₂, …, vₙ** with eigenvalues λ₁, λ₂, …, λₙ. Build matrix **P** by placing these eigenvectors as columns: P = [**v₁** | **v₂** | … | **vₙ**]. Build diagonal matrix **D** by placing the corresponding eigenvalues on the diagonal: D = diag(λ₁, λ₂, …, λₙ). Then A = PDP⁻¹. To verify: PDP⁻¹**vᵢ** = PD(**eᵢ**) = P(λᵢ**eᵢ**) = λᵢ**vᵢ** = A**vᵢ**, where **eᵢ** are standard basis vectors. The matrix P is the **change-of-basis** matrix from your basis of eigenvectors back to the standard basis.

The payoff is computation. Squaring A naively requires multiplying two full matrices. But A² = (PDP⁻¹)(PDP⁻¹) = PD²P⁻¹, and D² just squares the diagonal entries. More generally, **Aⁿ = PDⁿP⁻¹**, and Dⁿ is trivial: just raise each diagonal entry to the nth power. This turns computing the 100th power of a matrix from a nightmare into three multiplications. The same trick extends to matrix exponentials: e^(At) = Pe^(Dt)P⁻¹, which is the key to solving systems of differential equations.

The condition for diagonalizability is that A has **n linearly independent eigenvectors** — enough to form a full basis. This is guaranteed when all n eigenvalues are *distinct* (no repeated eigenvalues), because eigenvectors from distinct eigenvalues are always linearly independent. When eigenvalues repeat, diagonalizability is not guaranteed — you need to check whether the **geometric multiplicity** (dimension of the eigenspace) equals the **algebraic multiplicity** (number of times the eigenvalue appears as a root of the characteristic polynomial) for each eigenvalue. If any eigenspace is "too small," A is not diagonalizable — though it may still have a Jordan normal form, the closest diagonal-like structure available.
