---
id: systems-of-first-order-linear-odes
title: Systems of First-Order Linear Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- matrix-exponential-method
- eigenvalue-method-for-systems
- higher-order-linear-odes
tags:
- systems
- linear
- matrix-form
stage: formal-systems
status: draft
---

# Systems of First-Order Linear Differential Equations

## Core Idea
A system of first-order linear ODEs can be written in matrix form: y' = Ay + b(t), where y is a vector, A is a matrix, and b(t) is a forcing vector. This unified framework handles coupled equations and higher-order ODEs (converted to systems) via eigenvalue analysis.

## Questions

```yaml
- question: "In the system y' = Ay + b(t), what does the matrix A encode?"
  type: multiple-choice
  options: ["The initial conditions of the system", "How each variable contributes to the rate of change of the others", "The solutions of the individual equations", "The number of independent variables"]
  answer: 1
  explanation: "Each entry A_ij captures how the j-th variable contributes to the rate of change of the i-th variable. This coupling between equations is exactly what distinguishes a system from a collection of independent scalar ODEs, and it is why scalar methods must be extended using linear algebra."

- question: "A single second-order ODE y'' = f(t, y, y') can always be converted into a system of two first-order ODEs."
  type: true-false
  answer: true
  explanation: "Setting y₁ = y and y₂ = y' transforms the equation into the system y₁' = y₂ and y₂' = f(t, y₁, y₂). This reduction is why first-order systems are the fundamental object of study — every higher-order ODE reduces to one, so methods for systems apply universally."

- question: "Why is matrix form y' = Ay useful for solving systems of linear ODEs?"
  type: short-answer
  answer: "Matrix form unifies the system into a single equation structurally identical to the scalar case y' = ay, enabling eigenvalue decomposition to find solutions of the form e^(λt)v, where λ is an eigenvalue of A and v is the corresponding eigenvector."
  explanation: "The scalar ODE y' = ay has solution y = Ce^(at). For the matrix system, the role of a is played by A, and solutions take the form e^(λt)v where λ and v are eigenvalue-eigenvector pairs of A. The matrix form makes this analogy explicit and systematic."
```

## Explainer

When you studied first-order linear ODEs, each equation involved a single unknown function. Real systems — from predator-prey dynamics to electrical circuits — involve multiple coupled unknowns that influence each other's rates of change. A system of first-order linear ODEs captures exactly this: you have n unknown functions y₁, y₂, ..., yₙ, and each derivative yᵢ' depends linearly on all the others.

The key insight is that such a system can be written as a single matrix equation y' = Ay + b(t), where y is a vector of unknowns and A is a matrix whose entries encode the coupling. This is structurally identical to the scalar equation y' = ay + b(t) that you already know how to solve. The matrix A plays the same role as the scalar constant a — it governs how fast and in what direction the system evolves. This analogy is not just suggestive; the solution methods are direct generalizations.

One of the most powerful applications of this framework is converting higher-order ODEs into first-order systems. A second-order equation y'' = f(t, y, y') can be rewritten by introducing y₁ = y and y₂ = y', turning one second-order equation into two coupled first-order equations. This means every technique you develop for first-order systems — including eigenvalue methods and matrix exponentials — automatically applies to second-order and higher-order problems as well.

The solution to the homogeneous system y' = Ay (with b = 0) is built from the eigenvalues and eigenvectors of A. If A has eigenvalue λ with eigenvector v, then y(t) = e^(λt)v is a solution — you can verify this by differentiating. The general solution is a linear combination of such solutions, one per eigenvalue. The eigenvalue method, which you will study next, makes this systematic: it translates the ODE problem entirely into linear algebra, where you already have the tools to proceed.
