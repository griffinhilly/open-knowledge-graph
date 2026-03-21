---
id: systems-first-order-linear-odes
title: Systems of First-Order Linear Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: matrix-operations
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- matrix-exponential-method
- phase-portraits-linear-systems
tags:
- systems
- matrix-form
- fundamental
stage: formal-systems
status: draft
---

# Systems of First-Order Linear Differential Equations

## Core Idea
A system dx/dt = Ax + f(t) in matrix form unifies high-order and coupled equations. The homogeneous solution x_h uses eigenvalues λ and eigenvectors v of A: x_h = Σ cᵢe^(λᵢt)vᵢ. Complex eigenvalues give oscillatory components; repeated eigenvalues require generalized eigenvectors. Systems are more general than high-order equations but reveal structure through linear algebra.

## Questions

```yaml
- question: "The system ẋ = Ax has matrix A with eigenvalues λ₁ = 3 and λ₂ = -1. What is the long-term behavior of solutions as t → ∞?"
  type: multiple-choice
  options:
    - "All solutions decay to zero, since one eigenvalue is negative"
    - "All solutions oscillate, since the eigenvalues have opposite signs"
    - "Solutions grow without bound unless the initial condition lies exactly along the eigenvector for λ₂ = -1"
    - "Solutions approach a constant nonzero value, balancing the growth and decay modes"
  answer: 2
  explanation: "The general solution is x(t) = c₁e^(3t)v₁ + c₂e^(-t)v₂. As t → ∞, the e^(-t) term decays to zero while e^(3t) grows without bound. Unless c₁ = 0 — which requires the initial condition to lie exactly on the eigenvector v₂ — the e^(3t) component dominates and solutions grow. This is the dominant eigenvalue principle: the eigenvalue with the largest real part controls long-term behavior. Option A is wrong because having *one* negative eigenvalue doesn't guarantee decay — the positive eigenvalue dominates."

- question: "A 2×2 matrix A has eigenvalues 2 ± 3i. What form do the real-valued solutions of ẋ = Ax take?"
  type: multiple-choice
  options:
    - "Pure oscillations: c₁cos(3t) and c₂sin(3t) terms"
    - "Pure exponential growth: terms proportional to e^(2t)"
    - "Growing oscillations: e^(2t) terms multiplied by cos(3t) and sin(3t)"
    - "Decaying oscillations, since complex eigenvalues always indicate a stable system"
  answer: 2
  explanation: "Complex eigenvalues α ± βi give solutions involving e^(αt)cos(βt) and e^(αt)sin(βt) via Euler's formula: e^((α+βi)t) = e^(αt)(cos(βt) + i·sin(βt)). With α = 2 > 0 and β = 3, the solutions oscillate (cos/sin with frequency 3) while the amplitude grows exponentially (factor e^(2t)). The real part α governs growth/decay; the imaginary part β governs oscillation frequency. Option A omits the exponential envelope; option D reverses the stability criterion — complex eigenvalues indicate oscillation, and stability requires α < 0."

- question: "Converting a second-order ODE y'' + py' + qy = 0 into a first-order system introduces additional solutions not present in the original equation."
  type: true-false
  answer: false
  explanation: "The conversion is an exact equivalence — no new solutions are introduced. Setting x₁ = y and x₂ = y' rewrites the second-order ODE as a 2×2 system whose characteristic polynomial is identical to the original ODE's characteristic equation. The eigenvalues of the system matrix are the same roots as the characteristic equation, and every solution of the system corresponds exactly to a solution of the original ODE. The system form simply exposes the underlying linear algebra more explicitly."

- question: "If the system matrix A has purely imaginary eigenvalues ±βi, the solutions of ẋ = Ax oscillate with constant amplitude — neither growing nor decaying."
  type: true-false
  answer: true
  explanation: "Purely imaginary eigenvalues ±βi give solutions of the form cos(βt) and sin(βt) — pure oscillations with constant amplitude. The growth/decay factor e^(αt) reduces to e^(0·t) = 1 when the real part α = 0, so amplitude is constant. This is the undamped oscillator case, corresponding to a center in the phase portrait, and it sits exactly at the boundary between stable spiral (α < 0, amplitude decays) and unstable spiral (α > 0, amplitude grows)."

- question: "How does the solution structure x_h = Σ cᵢe^(λᵢt)vᵢ for a matrix system generalize the scalar solution Ce^(at)? Explain the role of each component."
  type: short-answer
  answer: "The scalar solution Ce^(at) for dx/dt = ax has two components: the exponential e^(at) governs the rate of growth/decay (controlled by scalar a), and C is a constant set by the initial condition. In the matrix case, each eigenvalue λᵢ plays the role of the scalar a — giving its own exponential mode e^(λᵢt). The eigenvector vᵢ plays the role of direction: it fixes which direction in state space that mode evolves along. The scalar cᵢ, set by initial conditions, controls how much of each mode is present. The full solution superimposes all eigenmodes."
  explanation: "This parallel is the core insight of the topic. The scalar ODE is a special case where A is a 1×1 matrix with one eigenvalue. In the vector case, each eigenvalue-eigenvector pair defines an 'eigensolution' — a direction in state space that evolves purely by scaling (no rotation) over time. Initial conditions determine how to mix these eigensolutions. This structure also explains why the system and characteristic equation approaches to higher-order ODEs are the same method: converting the ODE to a system matrix makes the eigenvalue structure explicit, but the eigenvalues themselves are identical to the roots of the characteristic equation."
```

## Explainer

You already know how to solve a single first-order linear ODE like dx/dt = ax: the solution is x(t) = Ce^(at). A system of first-order linear ODEs is a collection of such equations that are coupled — the rate of change of each variable depends on the current values of all variables. The matrix form dx/dt = Ax compresses this coupling into a single equation that looks exactly like the scalar case, and the solution strategy follows the same pattern, powered by the eigenvalue theory you know from linear algebra.

Consider two coupled equations: dx₁/dt = 2x₁ + x₂ and dx₂/dt = x₁ + 2x₂. Written as a system, this is ẋ = Ax where A = [[2,1],[1,2]]. The **eigenvalues** of A are the values λ for which Av = λv has a nonzero solution v. They govern the long-term behavior: eigenvalue 3 gives a solution that grows like e^(3t), eigenvalue 1 gives e^(t). For each eigenvalue λᵢ with eigenvector vᵢ, the vector function x(t) = e^(λᵢt)vᵢ is a solution to the homogeneous system. This is the matrix analogue of Ce^(at) — instead of a scalar constant C, the direction is fixed by the eigenvector. The general homogeneous solution combines all such solutions: x_h = c₁e^(λ₁t)v₁ + c₂e^(λ₂t)v₂ + ···, with constants determined by initial conditions.

**Complex eigenvalues** arise when the matrix has no real eigenvectors — the system is naturally oscillatory. A pair α ± βi gives complex exponential solutions e^((α+βi)t)v, which you unpack using Euler's formula into real-valued solutions involving e^(αt)cos(βt) and e^(αt)sin(βt). This is exactly what you saw in second-order ODEs with complex characteristic roots — the system form reveals the same phenomenon through the matrix's eigenvalues.

The connection to higher-order equations is direct and important. Any nth-order ODE y^(n) = f(y, y', ..., y^(n-1)) can be rewritten as a first-order system by introducing variables x₁ = y, x₂ = y', ..., xₙ = y^(n-1). The system matrix A has a specific "companion matrix" structure whose characteristic polynomial matches the original ODE's characteristic equation exactly. This means the eigenvalue approach and the characteristic equation approach are not two separate methods — they are the same method, with the system view exposing the underlying linear algebra more explicitly. The eigendecomposition of A also leads directly to the **matrix exponential** e^(At), which gives the solution x(t) = e^(At)x₀ in a form that unifies all cases and connects deeply to the structure of the coefficient matrix.
