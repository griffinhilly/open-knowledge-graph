---
id: stability-classification
title: Stability Classification of Linear Systems
domain: mathematics
course: differential-equations
prerequisites:
- id: phase-portraits-linear-systems
  type: hard
builds-toward:
- linearization-nonlinear-systems
tags:
- stability
- equilibrium
- classification
stage: advanced
status: draft
---

# Stability Classification of Linear Systems

## Core Idea
For dx/dt = Ax with equilibrium at x = 0, stability is determined by eigenvalues: asymptotically stable if all Re(λ) < 0 (decay to origin); unstable if any Re(λ) > 0 (grow unbounded); marginally stable if Re(λ) = 0 with geometric multiplicity equal to algebraic multiplicity. Stability is geometric and visible in phase portraits, making it the lens for understanding system behavior.

## Explainer

From your work with phase portraits, you have seen how trajectories of x' = Ax behave geometrically: spiraling inward or outward, flowing toward or away from the origin, or orbiting around it. **Stability classification** systematizes these observations by connecting the geometry you saw in phase portraits directly to the eigenvalues of A — the same eigenvalues that determined the qualitative form of the solution e^(λt).

The fundamental rule is governed by the **real parts** of the eigenvalues. If all eigenvalues satisfy Re(λ) < 0, every solution decays to the origin as t → ∞, regardless of where it starts. This is **asymptotic stability**: the equilibrium at the origin acts as an attractor for all nearby trajectories. Physically, think of a damped oscillator — any perturbation dissipates, and the system returns to rest. If any eigenvalue has Re(λ) > 0, that mode grows exponentially, and the equilibrium is **unstable**: trajectories starting arbitrarily close to the origin eventually escape. A saddle point is the canonical example — stable in some directions, unstable in others, making it unstable overall.

The subtle case is **marginal stability**: all eigenvalues are purely imaginary (Re(λ) = 0), and each has geometric multiplicity equal to algebraic multiplicity. This second condition ensures the matrix is diagonalizable over ℂ, so no polynomial factors like te^(iωt) appear in the solution — only pure oscillatory terms e^(iωt). The center equilibrium of an undamped harmonic oscillator is the canonical example: solutions orbit forever without growing or shrinking. If the multiplicities fail to match (a **defective** matrix), the solution contains factors like te^(λt), which grow even when Re(λ) = 0, making the equilibrium unstable despite purely imaginary eigenvalues.

For 2×2 systems, the classification condenses into a concrete decision tree using the **trace** tr(A) = λ₁ + λ₂ and **determinant** det(A) = λ₁λ₂. Plotting regions in the (tr, det) plane reveals the full taxonomy: det < 0 → saddle (unstable); det > 0 and tr < 0 → stable node or spiral; det > 0 and tr > 0 → unstable node or spiral; det > 0 and tr = 0 → center (marginally stable). The boundary curves separate these regions, and this single diagram unifies every phase portrait type you studied geometrically into one algebraic picture.
