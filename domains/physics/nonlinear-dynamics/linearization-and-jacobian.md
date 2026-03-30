---
id: linearization-and-jacobian
title: Linearization and the Jacobian Matrix
domain: physics
course: nonlinear-dynamics
prerequisites:
- id: fixed-points-and-stability
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- hopf-bifurcation
- chaos-definition-and-properties
tags:
- linearization
- jacobian
- hartman-grobman
- local-analysis
stage: advanced
status: validated
---

# Linearization and the Jacobian Matrix

## Core Idea
Near a fixed point x*, a nonlinear system ẋ = f(x) can be approximated by its linearization ẋ ≈ Df(x*) · (x - x*), where Df(x*) is the Jacobian matrix of partial derivatives evaluated at the fixed point. The Hartman-Grobman theorem guarantees that this linear approximation captures the correct qualitative behavior — the nonlinear flow is topologically equivalent to the linearized flow — provided all eigenvalues have nonzero real parts (the fixed point is hyperbolic).

## Questions

```yaml
- question: "For the system ẋ = x² + y, ẏ = x - y, what is the Jacobian matrix at the fixed point (0, 0)?"
  type: multiple-choice
  options:
    - "[[0, 1], [1, -1]]"
    - "[[1, 1], [1, -1]]"
    - "[[0, 0], [1, -1]]"
    - "[[2x, 1], [1, -1]] evaluated at (0,0), which is [[0, 1], [1, -1]]"
  answer: 3
  explanation: "The Jacobian is [[∂f₁/∂x, ∂f₁/∂y], [∂f₂/∂x, ∂f₂/∂y]] = [[2x, 1], [1, -1]]. At (0,0), this gives [[0, 1], [1, -1]]. Options A and D describe the same correct matrix. The eigenvalues of this matrix ((-1 ± √5)/2) determine local stability: one positive and one negative eigenvalue means (0,0) is a saddle point."

- question: "The Hartman-Grobman theorem guarantees that linearization gives the correct qualitative picture near a fixed point. Under what condition does this guarantee fail?"
  type: multiple-choice
  options:
    - "When the fixed point is a saddle — saddles are too sensitive to nonlinear perturbation"
    - "When any eigenvalue of the Jacobian has zero real part — the fixed point is non-hyperbolic"
    - "When the system has more than two dimensions"
    - "When the nonlinear terms are not polynomial"
  answer: 1
  explanation: "Hartman-Grobman requires the fixed point to be hyperbolic: all eigenvalues must have nonzero real parts. When an eigenvalue has zero real part (Re(λ) = 0), the linear and nonlinear systems can have qualitatively different phase portraits. A linear center might become a nonlinear spiral; a zero eigenvalue might correspond to a bifurcation. Dimensionality and the form of nonlinear terms don't affect the theorem's applicability — only the eigenvalue condition matters."

- question: "Linearization around a fixed point tells you the exact quantitative behavior of the nonlinear system in a neighborhood of that point."
  type: true-false
  answer: false
  explanation: "Linearization gives qualitative (topological) equivalence, not quantitative agreement. The Hartman-Grobman theorem says there exists a homeomorphism (continuous but not necessarily smooth map) between the nonlinear and linear phase portraits near a hyperbolic fixed point. This means the topology of trajectories is the same — same number of attracting/repelling directions, same type of fixed point — but distances, speeds, and angles may differ. For quantitative predictions, you need higher-order terms or numerical methods."

- question: "A three-dimensional system has a fixed point whose Jacobian has eigenvalues -2, -1 + 3i, and -1 - 3i. Describe the local behavior near this fixed point."
  type: short-answer
  answer: "All three eigenvalues have negative real parts, so the fixed point is asymptotically stable. The real eigenvalue -2 gives exponential decay along one direction. The complex conjugate pair -1 ± 3i produces oscillatory decay (spiraling) in the plane spanned by the corresponding eigenvectors. Locally, trajectories spiral inward while also decaying along the third direction, creating a stable spiral node — trajectories approach the fixed point along helical paths."
  explanation: "In three dimensions, you can have richer combinations than in 2D. Here, one eigendirection is a pure exponential decay (the real eigenvalue) and a two-dimensional eigenplane has spiraling decay (the complex pair). The spiral frequency is 3 (from the imaginary part) and the decay rate is 1 (from the real part). Because all real parts are negative, the fixed point is a global attractor in its neighborhood."
```

## Explainer

Nonlinear systems are, in general, impossible to solve exactly. But near a fixed point, the nonlinear terms are small compared to the linear ones (because the state variables are close to zero after shifting coordinates to place the fixed point at the origin). This is the fundamental insight behind linearization: replace the hard problem with an easy one that's accurate where it matters most — in the neighborhood of equilibrium.

The tool is the Jacobian matrix Df(x*), the matrix of all first partial derivatives of f evaluated at the fixed point. If ẋ = f(x) and x* is a fixed point with f(x*) = 0, then Taylor-expanding around x* gives ẋ = Df(x*)(x - x*) + higher-order terms. Dropping the higher-order terms yields the linearized system, which is just a linear ODE whose solution you know from your work on eigenvalues: the eigenvalues and eigenvectors of Df(x*) completely determine the local dynamics. Negative real parts mean attraction, positive mean repulsion, imaginary parts mean oscillation.

The **Hartman-Grobman theorem** makes this precise. It says that if x* is a hyperbolic fixed point (all eigenvalues of Df(x*) have nonzero real parts), then there exists a continuous change of coordinates that maps the nonlinear flow onto the linear flow near x*. The phase portraits are topologically equivalent — they have the same qualitative structure. A stable node stays a stable node. A saddle stays a saddle. An unstable spiral stays an unstable spiral. The nonlinear terms can warp trajectories, change speeds, and distort shapes, but they cannot change the topology of the local flow.

The theorem's restriction to hyperbolic fixed points is not a technicality — it's where all the interesting dynamics hide. When an eigenvalue has zero real part, the linearization is on a knife's edge: the nonlinear terms determine whether the system tips toward stability or instability. A linear center (purely imaginary eigenvalues) might become a stable spiral, an unstable spiral, or remain a center in the nonlinear system. A zero eigenvalue often signals a bifurcation — a qualitative change in the number or stability of fixed points as a parameter varies. The Hartman-Grobman theorem tells you exactly where linearization succeeds and, equally importantly, where you need more sophisticated tools.
