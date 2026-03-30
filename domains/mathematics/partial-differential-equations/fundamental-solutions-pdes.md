---
id: fundamental-solutions-pdes
title: Fundamental Solutions
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: greens-functions-pdes
  type: hard
- id: pde-classification
  type: hard
tags: [pde, fundamental-solution, singularity, potential-theory]
stage: advanced
status: validated
---
# Fundamental Solutions

## Core Idea
A fundamental solution of a linear PDE operator L is a distribution Φ satisfying LΦ = δ (the Dirac delta) in all of ℝⁿ, without boundary conditions. It represents the response to a point source in free space and is the building block from which Green's functions and general solutions are constructed. The fundamental solution for the Laplacian is the Newton potential (1/|x| in 3D), for the heat operator it is the Gaussian heat kernel, and for the wave operator it is a distribution supported on the light cone. These explicit formulas encode the essential character of each PDE type.

## Questions
```yaml
- question: "What is the fundamental solution of the Laplacian -Δ in two dimensions?"
  type: multiple-choice
  options:
    - "Φ(x) = -(1/2π)ln|x|"
    - "Φ(x) = 1/(4π|x|)"
    - "Φ(x) = e^(-|x|²)"
    - "Φ(x) = 1/|x|²"
  answer: 0
  explanation: "In 2D, the fundamental solution of -Δ is -(1/2π)ln|x|, which is the logarithmic potential. In 3D it would be 1/(4π|x|). The dimension dependence reflects the different rates at which flux spreads through space."
- question: "The fundamental solution of the heat operator (∂_t - kΔ) is supported for all times t."
  type: true-false
  answer: false
  explanation: "The heat kernel K(x,t) = (4πkt)^(-n/2)exp(-|x|²/(4kt)) is defined only for t > 0 and is zero for t < 0 (by causality). The heat equation is an evolution equation with a preferred time direction, so the fundamental solution respects this by being supported only in the forward time direction."
- question: "How is a Green's function for a bounded domain related to the fundamental solution?"
  type: short-answer
  answer: "G(x,y) = Φ(x-y) + corrector, where the corrector is a smooth solution chosen so G satisfies the boundary conditions"
  explanation: "The fundamental solution captures the singularity at x = y but does not satisfy boundary conditions. The corrector term is a regular solution of the homogeneous PDE chosen so that the sum G vanishes (or has zero normal derivative) on the boundary."
- question: "The fundamental solution of the wave operator in three dimensions exhibits Huygens' principle."
  type: true-false
  answer: true
  explanation: "In 3D, the fundamental solution of the wave operator is a distribution supported on the forward light cone |x| = ct (rather than inside it). This means a sharp initial pulse produces a sharp wavefront with no residual signal—Huygens' principle. In 2D and 1D, this fails: signals leave 'tails.'"
```

## Explainer
Fundamental solutions are the atoms of linear PDE theory. A fundamental solution Φ for an operator L satisfies LΦ = δ in the distributional sense, meaning it is the response to an idealized point source in all of space without boundaries. Unlike Green's functions, fundamental solutions are intrinsic to the operator itself and independent of any domain or boundary conditions. They exist for all constant-coefficient linear operators with nonzero principal symbol, as guaranteed by the Malgrange-Ehrenpreis theorem.

The fundamental solution of the Laplacian reflects the geometry of diffusion in different dimensions. In ℝ³, Φ(x) = 1/(4π|x|) is the Newtonian potential—the electrostatic potential of a point charge. In ℝ², Φ(x) = -(1/2π)ln|x| is the logarithmic potential, which grows without bound at infinity, reflecting the recurrence of two-dimensional random walks. In ℝⁿ for n ≥ 3, Φ(x) = c_n/|x|^(n-2). These formulas encode how influence from a point source decays with distance, and they underpin all of classical potential theory.

The heat kernel K(x,t) = (4πkt)^(-n/2)exp(-|x|²/(4kt)) for t > 0 is the fundamental solution of the heat operator ∂_t - kΔ. It is a Gaussian whose width grows as √(kt), describing how a point source of heat spreads diffusively. Two crucial properties are immediate from the formula: the infinite speed of propagation (K > 0 for all x when t > 0) and the smoothing effect (K is infinitely differentiable for t > 0 despite the singular initial data). The heat kernel appears throughout mathematics—in probability (transition density of Brownian motion), geometry (local index theorem), and number theory (Jacobi theta function).

For the wave operator ∂²_t - c²Δ, the fundamental solution depends critically on the spatial dimension. In one dimension, it is the Heaviside function H(ct - |x|)/(2c), which is supported inside the full light cone—a pulse rings forever. In three dimensions, it is a distribution supported exactly on the light cone |x| = ct, giving sharp wave fronts (Huygens' principle). In two dimensions, it is supported inside the light cone, producing the familiar trailing waves seen when a stone is dropped in water. These dimension-dependent behaviors are among the most striking results in PDE theory and have profound physical consequences.
