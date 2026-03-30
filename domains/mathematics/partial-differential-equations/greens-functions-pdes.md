---
id: greens-functions-pdes
title: Green's Functions for PDEs
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: laplaces-equation
  type: hard
- id: divergence-theorem
  type: hard
- id: dirac-delta-function
  type: soft
tags: [pde, greens-function, fundamental-solution, integral-representation]
stage: advanced
status: validated
---
# Green's Functions for PDEs

## Core Idea
A Green's function G(x, y) for a linear PDE operator L on a domain Ω is the response at point x to a point source at y—the solution to LG = δ(x - y) satisfying appropriate boundary conditions. Once known, the Green's function allows any solution to be written as an integral: if Lu = f, then u(x) = ∫G(x,y)f(y)dy. This converts the PDE into an integral equation and provides a powerful representation formula that encodes both the differential operator and the boundary geometry.

## Questions
```yaml
- question: "What is the Green's function for the Laplacian in three dimensions (free space)?"
  type: multiple-choice
  options:
    - "G(x,y) = -1/(4π|x-y|)"
    - "G(x,y) = -1/(2π) ln|x-y|"
    - "G(x,y) = |x-y|²"
    - "G(x,y) = e^(-|x-y|)"
  answer: 0
  explanation: "The free-space Green's function for -Δ in 3D is G(x,y) = 1/(4π|x-y|). This is the electrostatic potential due to a unit point charge, reflecting the inverse-square law in three dimensions."
- question: "The Green's function for the Laplacian on a bounded domain depends on the shape of the domain."
  type: true-false
  answer: true
  explanation: "The Green's function must satisfy boundary conditions (typically G = 0 on ∂Ω for Dirichlet problems), so it depends on the domain geometry. The free-space fundamental solution is domain-independent, but the Green's function adds a correction term to enforce the boundary condition."
- question: "How does the Green's function relate to the superposition principle?"
  type: short-answer
  answer: "It decomposes any source f into point sources and sums their individual responses via integration"
  explanation: "For a linear operator, the response to an arbitrary source f is the integral (superposition) of responses to point sources δ(x-y) weighted by f(y). This is the essence of the representation u(x) = ∫G(x,y)f(y)dy."
- question: "The Green's function G(x,y) for a self-adjoint operator satisfies G(x,y) = G(y,x)."
  type: true-false
  answer: true
  explanation: "This reciprocity property means the response at x due to a source at y equals the response at y due to a source at x. It follows from the self-adjointness of the operator and is physically meaningful: it expresses Maxwell's reciprocity principle in electrostatics."
```

## Explainer
Green's functions are one of the most powerful tools in the theory of linear PDEs, connecting the abstract operator theory to concrete integral representations. The idea is simple but profound: if you know how a system responds to a single point impulse (the Green's function), you can determine its response to any forcing by superposition. For a linear operator L with Lu = f, the Green's function G satisfies LG(x,y) = δ(x-y) with homogeneous boundary conditions, and the solution is u(x) = ∫_Ω G(x,y)f(y)dy.

For Laplace's equation in free space, the Green's function is the fundamental solution: G(x,y) = -1/(2π)ln|x-y| in 2D and G(x,y) = 1/(4π|x-y|) in 3D. These are the electrostatic potentials due to point charges and underlie all of classical potential theory. On a bounded domain with Dirichlet boundary conditions, the Green's function is G = Φ + corrector, where Φ is the fundamental solution and the corrector is a harmonic function chosen so that G vanishes on the boundary. Finding this corrector for a specific domain is the central challenge.

The method of images provides Green's functions for simple geometries. For the half-space, one places an image charge at the reflected point across the boundary, and the Green's function is the difference of two fundamental solutions. For the ball in ℝⁿ, Kelvin inversion gives the image point, yielding an explicit formula. For general domains, the Green's function typically cannot be found in closed form and must be approximated numerically or studied qualitatively.

Green's functions extend naturally to time-dependent problems. The heat kernel K(x,y,t) = (4πkt)^(-n/2) exp(-|x-y|²/(4kt)) is the Green's function for the heat equation, representing the temperature distribution from an initial point source. The retarded Green's function for the wave equation encodes the Huygens principle and finite propagation speed. These time-dependent Green's functions are fundamental in physics, appearing as propagators in quantum mechanics and field theory.

Beyond explicit computation, Green's functions have deep theoretical significance. Their existence is equivalent to the solvability of the PDE for arbitrary data. Their regularity properties reflect the regularity theory of the operator. The spectral decomposition of the Green's function in terms of eigenfunctions connects PDE theory to spectral theory. In modern analysis, the study of Green's function estimates is central to understanding the behavior of solutions on manifolds and in rough domains.
