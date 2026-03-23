---
id: eigenvalue-method-for-systems
title: Eigenvalue Method for Systems of ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: systems-of-first-order-linear-odes
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- phase-portraits-for-linear-systems
tags:
- systems
- eigenvalue
- diagonalization
stage: formal-systems
status: validated
---

# Eigenvalue Method for Systems of ODEs

## Core Idea
To solve y' = Ay, find eigenvalues λ and eigenvectors v of A. Each eigenvalue-eigenvector pair gives a solution y = e^{λt}v. For complex eigenvalues, extract real and imaginary parts to form real-valued oscillating solutions.

## How It's Best Learned
Work through 2×2 systems step-by-step: compute det(A - λI) = 0, find λ, solve (A - λI)v = 0 for v. Construct the general solution and verify by substitution.

## Common Misconceptions
- Forgetting that real eigenvector entries are required for real-valued solutions; complex eigenvalues give oscillations. - Not recognizing that repeated eigenvalues may not have enough linearly independent eigenvectors (generalized eigenvectors needed). - Confusing eigenvectors of A with solutions to the ODE system.

## Questions

```yaml
- question: "When you substitute y = e^{λt}v into the system y' = Ay, both sides reduce to the same equation. What is that equation, and why does it make the eigenvalue method work?"
  type: multiple-choice
  options:
    - "It reduces to Av = v, meaning only unit eigenvectors are valid — this constrains which exponentials solve the system"
    - "It reduces to Av = λv, the eigenvalue equation — the system has a solution of this form exactly when v is an eigenvector of A with eigenvalue λ"
    - "It reduces to A = λI, meaning the method only works when A is a scalar multiple of the identity"
    - "It reduces to λv = 0, so only the trivial solution exists unless λ = 0"
  answer: 1
  explanation: "Substituting y = e^{λt}v gives y' = λe^{λt}v and Ay = Ae^{λt}v = e^{λt}Av. Setting these equal and dividing by the nonzero scalar e^{λt} gives Av = λv — the eigenvalue equation. This is why the method works: the exponential structure perfectly matches the system's structure. The scalar λ absorbs the time derivative, and the eigenvector condition ensures the matrix product Av produces the same vector back (scaled), so the equation is self-consistent."

- question: "The matrix A has a complex eigenvalue λ = 2 + 3i with eigenvector v = p + qi (p, q real vectors). How do you obtain real-valued solutions from this?"
  type: multiple-choice
  options:
    - "Use only the real part of e^{λt}v and discard the imaginary part"
    - "Replace λ with its real part 2 and ignore the imaginary part 3i entirely"
    - "Apply Euler's formula to e^{(2+3i)t}(p+qi) and take its real and imaginary parts as two independent real-valued solutions"
    - "Complex eigenvalues indicate the system has no real-valued solutions, so a different method is needed"
  answer: 2
  explanation: "Euler's formula gives e^{(2+3i)t}(p+qi) = e^{2t}[(cos 3t)p − (sin 3t)q] + ie^{2t}[(sin 3t)p + (cos 3t)q]. The real and imaginary parts are each real-valued solutions, and together they form two linearly independent solutions replacing the complex conjugate pair. This is why complex eigenvalues produce oscillatory behavior — the sin and cos terms encode rotation in the solution space. Option D is wrong: complex eigenvalues always occur in conjugate pairs for real A, and extracting real/imaginary parts always yields real solutions."

- question: "If the matrix A has 3 distinct real eigenvalues, the general solution to y' = Ay is a linear combination of 3 independent exponential-vector solutions e^{λ₁t}v₁, e^{λ₂t}v₂, e^{λ₃t}v₃."
  type: true-false
  answer: true
  explanation: "Distinct eigenvalues guarantee linearly independent eigenvectors, so the 3 solutions e^{λᵢt}vᵢ are independent and span the full 3-dimensional solution space. Every solution is a unique linear combination c₁e^{λ₁t}v₁ + c₂e^{λ₂t}v₂ + c₃e^{λ₃t}v₃, with the constants determined by initial conditions. This is the diagonalization of the system: in the eigenvector basis, the three equations decouple into independent scalar ODEs, each solved by its own exponential."

- question: "Complex eigenvalues of A mean the system y' = Ay has no real-valued solutions, and the eigenvalue method cannot be applied."
  type: true-false
  answer: false
  explanation: "Complex eigenvalues do not prevent real solutions — they guarantee oscillatory ones. When λ = α + βi is complex, the complex solution e^{λt}v is separated into real and imaginary parts using Euler's formula, yielding two real-valued solutions involving e^{αt}cos(βt) and e^{αt}sin(βt). The eigenvalue method applies exactly as before; the extra step is extracting these real-valued solutions from the complex result. Complex eigenvalues are in fact the typical case for systems with oscillatory behavior like springs, circuits, and predator-prey models."

- question: "Explain why the eigenvalue method effectively 'decouples' a system of coupled ODEs. What does working in the eigenvector basis reveal about the structure of the solutions?"
  type: short-answer
  answer: "In the eigenvector basis, the matrix A acts by simply scaling each coordinate by its corresponding eigenvalue. This means the n coupled equations separate into n independent scalar equations, each of the form z'ᵢ = λᵢzᵢ, solved independently by zᵢ = cᵢe^{λᵢt}. The coupling in the original coordinates disappears because eigenvectors are precisely the directions A doesn't rotate — only scales. The general solution is then a superposition of these decoupled exponentials, transformed back into original coordinates using the eigenvectors."
  explanation: "The coupling in y' = Ay comes from off-diagonal entries of A — the rate of change of one variable depends on others. Eigenvectors are the special directions where this cross-dependence vanishes: Avᵢ = λᵢvᵢ means A maps vᵢ back to itself (scaled), with no mixing into other directions. Expressing the solution as a combination of these directions diagonalizes A, separating the system into independent 1D problems. This is the deep connection between the eigenvalue method and matrix diagonalization."
```

## Explainer

To solve a single first-order linear ODE y' = ay, you know the answer is y = Ce^{at} — an exponential, where a is the coefficient. The eigenvalue method generalizes this to a system of n coupled equations written as y' = Ay, where y is a vector of n unknown functions and A is an n×n matrix. The key insight is the same: look for solutions of the form y = e^{λt}v, where λ is a scalar and v is a constant vector. Substituting y = e^{λt}v into y' = Ay gives λe^{λt}v = Ae^{λt}v, and dividing by the nonzero scalar e^{λt} gives Av = λv. This is exactly the **eigenvalue equation** from linear algebra: v must be an eigenvector of A with eigenvalue λ.

So the method is: find the eigenvalues and eigenvectors of the matrix A, then construct solutions. For a 2×2 system, you compute det(A − λI) = 0 to find two eigenvalues λ₁ and λ₂. For each eigenvalue λᵢ, you solve (A − λᵢI)v = 0 to find the corresponding eigenvector vᵢ. Each pair gives an independent solution y = e^{λᵢt}vᵢ. The general solution is their linear combination: y = c₁e^{λ₁t}v₁ + c₂e^{λ₂t}v₂. You determine the constants c₁ and c₂ from initial conditions.

When the eigenvalues are complex — which happens when the characteristic polynomial has no real roots — the solutions still work, but you must extract real-valued solutions. If λ = α + βi is a complex eigenvalue with eigenvector v = p + qi (where p and q are real vectors), then the complex solution e^{λt}v expands using Euler's formula: e^{(α+βi)t}(p + qi) = e^{αt}[(cos βt)p − (sin βt)q] + ie^{αt}[(sin βt)p + (cos βt)q]. The real and imaginary parts are each real-valued solutions, and together they replace the pair of complex solutions. This is why complex eigenvalues produce oscillatory behavior in the system — the sin and cos terms encode rotations in the solution space.

The eigenvalue method works because the exponential structure e^{λt}v perfectly matches the structure of the system y' = Ay — the derivative of an exponential is proportional to itself, and a matrix-vector product with an eigenvector is proportional to the same vector. When A has n linearly independent eigenvectors (which is guaranteed if all eigenvalues are distinct, and is the usual case), the n independent solutions span the full solution space, and every solution is a linear combination of them. This is the **diagonalization** of the system: in the eigenvector basis, A acts by simply scaling each component, so the coupled system decouples into n independent scalar equations, each solved by an exponential.
