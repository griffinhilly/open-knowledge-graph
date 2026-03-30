---
id: hyperbolic-pde-theory
title: Hyperbolic PDE Theory (Wave Propagation and Characteristics)
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: method-of-characteristics
  type: hard
- id: energy-methods-pdes
  type: hard
- id: distribution-theory-pdes
  type: soft
tags: [pde, hyperbolic, wave, propagation, finite-speed, domain-of-dependence]
stage: expert
status: validated
---
# Hyperbolic PDE Theory (Wave Propagation and Characteristics)

## Core Idea
Hyperbolic PDEs describe wave propagation phenomena with finite speed of information travel. The wave equation u_tt = c²Δu is the prototype, with solutions determined by initial data through D'Alembert's formula (1D) and Kirchhoff's formula (3D). Key features include: finite domain of dependence (the solution at a point depends only on data within the backward characteristic cone), preservation of singularities (unlike parabolic equations, waves carry discontinuities), and energy conservation. The theory of symmetric hyperbolic systems extends these results to Maxwell's equations, elasticity, and general relativity.

## Questions
```yaml
- question: "The domain of dependence for the wave equation u_tt = c²Δu at a point (x₀, t₀) is:"
  type: multiple-choice
  options:
    - "The intersection of the backward characteristic cone with the initial surface"
    - "The entire initial surface t = 0"
    - "A single point on the initial surface"
    - "The forward characteristic cone"
  answer: 0
  explanation: "The solution u(x₀, t₀) depends only on initial data within the ball |x - x₀| ≤ ct₀ on the initial surface. This is the intersection of the backward light cone with t = 0. Data outside this region has no influence—information cannot travel faster than speed c."
- question: "Huygens' principle holds in all spatial dimensions."
  type: true-false
  answer: false
  explanation: "The strong form of Huygens' principle—that a sharp initial pulse produces a sharp signal—holds only in odd dimensions ≥ 3. In even dimensions and in 1D, signals leave 'tails': the wave equation in 2D produces a residual signal after the main wavefront passes (this is why a splash in a pond creates spreading ripples rather than a single sharp ring)."
- question: "What does energy conservation for the wave equation imply about solution regularity?"
  type: short-answer
  answer: "Solutions are exactly as regular as the initial data — they neither smooth out nor develop new singularities"
  explanation: "Since E(t) = ½∫[u_t² + c²|∇u|²]dx is conserved, the H¹ norm of the solution is preserved in time. This means initial data in H^k produces a solution in H^k for all time — no smoothing (unlike parabolic) and no loss of regularity."
- question: "A symmetric hyperbolic system is a first-order system of the form A₀u_t + Σ Aⱼu_{xⱼ} = f where:"
  type: multiple-choice
  options:
    - "A₀ is symmetric positive definite and all Aⱼ are symmetric"
    - "All matrices are diagonal"
    - "The system is scalar"
    - "A₀ = I (identity)"
  answer: 0
  explanation: "Symmetric hyperbolicity is a structural condition guaranteeing well-posedness via energy estimates. The symmetry of Aⱼ enables energy methods: multiplying by u^T A₀ and integrating gives a conserved energy. Maxwell's equations, linearized Euler equations, and Einstein's equations can all be written as symmetric hyperbolic systems."
```

## Explainer
Hyperbolic PDEs are the mathematical description of wave phenomena—sound, light, elastic vibrations, gravitational waves. Their defining characteristic is finite propagation speed: information travels along characteristic surfaces at a definite speed, creating domains of dependence and influence. This is physically natural (nothing travels faster than light) but mathematically distinctive: it means hyperbolic equations behave very differently from elliptic and parabolic ones.

For the wave equation u_tt = c²Δu in ℝⁿ, the solution with initial data u(x,0) = f(x), u_t(x,0) = g(x) is given by explicit formulas that depend on the dimension. In 1D, D'Alembert's formula u = ½[f(x-ct) + f(x+ct)] + (1/2c)∫g(s)ds shows the solution is a superposition of left- and right-traveling waves. In 3D, Kirchhoff's formula involves an average of the data over a sphere of radius ct—this is Huygens' principle, and it implies a sharp wavefront with no residual signal. In 2D, Hadamard's method of descent from 3D gives a formula involving an integral over a disk, producing wave tails.

The energy method is the primary tool for establishing well-posedness of hyperbolic problems. For the wave equation, E(t) = ½∫[u_t² + c²|∇u|²]dx is conserved, which gives uniqueness (if initial data is zero, energy is zero, so u ≡ 0) and continuous dependence. For general symmetric hyperbolic systems, the energy E = ½∫u^T A₀ u dx satisfies dE/dt ≤ CE for a constant depending on the coefficients, and Gronwall's inequality gives exponential bounds. These estimates are sharp: hyperbolic equations conserve regularity, neither smoothing initial data nor creating new singularities.

The theory of singularities for hyperbolic equations is much richer than for elliptic or parabolic equations. Singularities in the initial data propagate along characteristics: a discontinuity in the initial data traces out a characteristic surface in space-time, creating a wavefront. Diffraction, reflection, and focusing of singularities at boundaries and caustics produce complex patterns described by microlocal analysis and geometric optics. For nonlinear hyperbolic equations, new singularities can form spontaneously—shock waves in gas dynamics, caustics in nonlinear optics—even from smooth initial data. The global existence theory for nonlinear hyperbolic equations remains one of the great open challenges in PDE theory.
