---
id: matrix-exponential
title: Matrix Exponential and Differential Equations
domain: mathematics
course: linear-algebra
prerequisites:
- id: diagonalization-similar-matrices
  type: hard
builds-toward:
- applications-linear-algebra-modeling
tags:
- matrix-exponential
- odes
- systems
stage: formal-systems
status: draft
---

# Matrix Exponential and Differential Equations

## Core Idea
The matrix exponential eᴬ = Σ Aⁿ/n! solves the matrix ODE dX/dt = AX with initial condition X(0) = I, giving X(t) = eᴬᵗ. If A is diagonalizable, eᴬ = PeᴰPP⁻¹ where e^D is diagonal. Solutions to dx/dt = Ax are x(t) = eᴬᵗx₀. Jordan normal form provides formulas for eᴬᵗ in the non-diagonalizable case.

## Explainer

The scalar exponential e^(at) solves the ODE dx/dt = ax — it is the function that is its own derivative, up to the factor a. The **matrix exponential** eᴬᵗ is the natural generalization: a matrix-valued function that solves the system dx/dt = Ax with any initial condition x(0) = x₀. Just as e^(at) is defined by its power series e^(at) = Σ (at)ⁿ/n!, the matrix exponential is defined by eᴬ = Σ Aⁿ/n!. This series converges for every square matrix A, making the definition rigorous — though computing it directly from the series would require infinitely many matrix multiplications.

This is where your prerequisite, diagonalization, becomes essential. If A = PDP⁻¹ where D is diagonal, then Aⁿ = PDⁿP⁻¹ for every n, and the power series telescopes: eᴬ = P(Σ Dⁿ/n!)P⁻¹ = PeᴰP⁻¹. Since D is diagonal, eᴰ is simply the diagonal matrix with e^(λᵢ) on each diagonal entry — reducing the whole computation to scalar exponentials applied to eigenvalues. Diagonalization decouples the system into independent one-dimensional ODEs, one for each eigenvector direction, and the matrix exponential reassembles the solutions.

The payoff is that any system of linear ODEs, dx/dt = Ax, has the general solution x(t) = eᴬᵗx₀. The long-term behavior — whether solutions grow, decay, or oscillate — depends entirely on the eigenvalues of A. Eigenvalues with negative real part produce decay; positive real part produces growth; purely imaginary eigenvalues produce oscillation. The matrix exponential transforms the qualitative question "what does this system do over time?" into a purely algebraic question about the **spectrum** of A.

When A is not diagonalizable, Jordan normal form provides the fallback. A Jordan block for eigenvalue λ gives e^(Jt) = e^(λt) times an upper-triangular matrix whose off-diagonal entries involve polynomial factors: te^(λt), t²e^(λt)/2, and so on. These **resonant terms** are characteristic of degenerate systems and explain phenomena like resonance in coupled oscillators, where the response grows without bound even at bounded input. The matrix exponential thus unifies the classification of linear ODE behavior — stability, oscillation, and resonance — under a single computational framework.
