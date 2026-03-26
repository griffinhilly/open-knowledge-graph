---
id: stability-classification
title: Stability Classification of Linear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: phase-portraits-linear-systems
  type: hard
builds-toward:
- linearization-of-nonlinear-systems
tags:
- stability
- equilibrium
- classification
stage: formal-systems
status: validated
---

# Stability Classification of Linear Systems

## Core Idea
For dx/dt = Ax with equilibrium at x = 0, stability is determined by eigenvalues: asymptotically stable if all Re(λ) < 0 (decay to origin); unstable if any Re(λ) > 0 (grow unbounded); marginally stable if Re(λ) = 0 with geometric multiplicity equal to algebraic multiplicity. Stability is geometric and visible in phase portraits, making it the lens for understanding system behavior.

## Questions

```yaml
- question: "A 2×2 linear system x' = Ax has eigenvalues λ = ±3i (purely imaginary, distinct). What is the stability classification of the origin?"
  type: multiple-choice
  options:
    - "Asymptotically stable, because the zero real part means solutions neither grow nor decay, which satisfies the stability definition"
    - "Marginally stable (center), because the eigenvalues are distinct, the matrix is non-defective, and solutions are purely oscillatory"
    - "Unstable, because imaginary eigenvalues always indicate oscillatory growth in linear systems"
    - "Cannot be determined without also knowing the eigenvectors"
  answer: 1
  explanation: "Purely imaginary eigenvalues give marginal stability if and only if the matrix is non-defective (geometric multiplicity = algebraic multiplicity for each eigenvalue). Here the two eigenvalues ±3i are distinct, so the matrix must be diagonalizable over ℂ — non-defective by definition. Solutions take the form c₁e^(3it) + c₂e^(-3it), which are bounded oscillations that neither grow nor decay. If the eigenvalues were repeated and the matrix defective, terms like te^(3it) would appear, growing without bound and making the origin unstable despite purely imaginary eigenvalues."

- question: "For a 2×2 linear system, tr(A) = 0 and det(A) = 9. What is the stability classification of the origin, and why?"
  type: multiple-choice
  options:
    - "Asymptotically stable, because zero trace means eigenvalues sum to zero, so they must have negative real parts"
    - "Marginally stable (center), because tr = 0 and det > 0 imply purely imaginary eigenvalues with no real part"
    - "Unstable, because positive determinant with zero trace indicates a saddle point"
    - "Stability cannot be determined from trace and determinant alone"
  answer: 1
  explanation: "For a 2×2 system, the eigenvalues satisfy λ² − tr(A)λ + det(A) = 0. With tr = 0 and det = 9: λ² + 9 = 0, giving λ = ±3i. Purely imaginary eigenvalues → all Re(λ) = 0. Since the eigenvalues are distinct (non-defective), the origin is a center — marginally stable. The trace-determinant diagram codifies this: det > 0 and tr = 0 places the system exactly on the boundary between stable and unstable spirals, giving a center."

- question: "A linear system can be unstable even if all eigenvalues have zero real part, provided the matrix is defective."
  type: true-false
  answer: true
  explanation: "This is the subtle condition for marginal stability. When a matrix has a repeated eigenvalue λ with Re(λ) = 0 but insufficient independent eigenvectors (geometric multiplicity < algebraic multiplicity), the general solution contains terms like tⁿe^(λt). Even with Re(λ) = 0, the polynomial factor tⁿ grows without bound as t → ∞, and trajectories escape to infinity. Marginal stability requires both Re(λ) = 0 for all eigenvalues AND that the matrix is non-defective. The purely imaginary condition alone is not enough."

- question: "For a 2×2 linear system where det(A) > 0 and tr(A) < 0, the origin is marginally stable."
  type: true-false
  answer: false
  explanation: "With det > 0 and tr < 0, consider the eigenvalue equation λ² − tr(A)λ + det(A) = 0. Since tr < 0, −tr > 0, and since det > 0, the product of eigenvalues is positive and their sum is negative. Either both eigenvalues are real and negative, or they are complex conjugates with negative real part (stable spiral). In either case, all Re(λ) < 0, making the origin asymptotically stable — trajectories decay to the origin. Marginal stability requires tr = 0 (with det > 0) to get purely imaginary eigenvalues."

- question: "The condition Re(λ) = 0 for all eigenvalues is necessary but not sufficient for marginal stability. What additional condition is required, and what goes wrong when it fails?"
  type: short-answer
  answer: "The additional condition is that the matrix must be non-defective: for every eigenvalue, its geometric multiplicity (the number of linearly independent eigenvectors) must equal its algebraic multiplicity (its multiplicity as a root of the characteristic polynomial). When this fails — when the matrix is defective — the solution contains generalized eigenvector terms of the form tⁿe^(λt). Even when Re(λ) = 0, the polynomial factor tⁿ grows without bound as t → ∞. Trajectories that start near the origin move away from it, so the origin is unstable despite the purely imaginary eigenvalues. The canonical example is a 2×2 matrix with a single repeated eigenvalue λ = 0i and only one independent eigenvector; the solution then contains a term growing linearly in time. Marginal stability requires the system to be able to produce purely oscillatory solutions with no polynomial growth, which demands a complete set of independent eigenvectors."
```

## Explainer

From your work with phase portraits, you have seen how trajectories of x' = Ax behave geometrically: spiraling inward or outward, flowing toward or away from the origin, or orbiting around it. **Stability classification** systematizes these observations by connecting the geometry you saw in phase portraits directly to the eigenvalues of A — the same eigenvalues that determined the qualitative form of the solution e^(λt).

The fundamental rule is governed by the **real parts** of the eigenvalues. If all eigenvalues satisfy Re(λ) < 0, every solution decays to the origin as t → ∞, regardless of where it starts. This is **asymptotic stability**: the equilibrium at the origin acts as an attractor for all nearby trajectories. Physically, think of a damped oscillator — any perturbation dissipates, and the system returns to rest. If any eigenvalue has Re(λ) > 0, that mode grows exponentially, and the equilibrium is **unstable**: trajectories starting arbitrarily close to the origin eventually escape. A saddle point is the canonical example — stable in some directions, unstable in others, making it unstable overall.

The subtle case is **marginal stability**: all eigenvalues are purely imaginary (Re(λ) = 0), and each has geometric multiplicity equal to algebraic multiplicity. This second condition ensures the matrix is diagonalizable over ℂ, so no polynomial factors like te^(iωt) appear in the solution — only pure oscillatory terms e^(iωt). The center equilibrium of an undamped harmonic oscillator is the canonical example: solutions orbit forever without growing or shrinking. If the multiplicities fail to match (a **defective** matrix), the solution contains factors like te^(λt), which grow even when Re(λ) = 0, making the equilibrium unstable despite purely imaginary eigenvalues.

For 2×2 systems, the classification condenses into a concrete decision tree using the **trace** tr(A) = λ₁ + λ₂ and **determinant** det(A) = λ₁λ₂. Plotting regions in the (tr, det) plane reveals the full taxonomy: det < 0 → saddle (unstable); det > 0 and tr < 0 → stable node or spiral; det > 0 and tr > 0 → unstable node or spiral; det > 0 and tr = 0 → center (marginally stable). The boundary curves separate these regions, and this single diagram unifies every phase portrait type you studied geometrically into one algebraic picture.
