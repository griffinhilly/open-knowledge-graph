---
id: laplace-poisson-equations-electrostatics
title: Laplace's and Poisson's Equations
domain: physics
course: electrodynamics
prerequisites:
- id: maxwell-equations-differential-form
  type: hard
- id: divergence-theorem
  type: hard
builds-toward:
- boundary-value-problems-electrostatics
- separation-variables-elliptic-equations
tags:
- laplace-equation
- poisson-equation
- potential
stage: advanced
status: draft
---

# Laplace's and Poisson's Equations

## Core Idea
Laplace's equation ∇²φ = 0 governs the electrostatic potential in charge-free regions, while Poisson's equation ∇²φ = -ρ/ε₀ includes charge sources. Solutions to these equations determine all electrostatic fields and represent one of the most important PDEs in physics and mathematics. Their rich mathematical theory (harmonic functions, Green's functions, conformal mappings) provides powerful techniques for solving electrostatics problems.

## Explainer

You already know from Maxwell's equations in differential form that ∇·E = ρ/ε₀ (Gauss's law) and ∇×E = 0 in electrostatics (no time-varying magnetic fields). Since the curl of E vanishes, you can write E = −∇φ, where φ is the electric potential. Substituting into Gauss's law gives ∇·(−∇φ) = ρ/ε₀, or **Poisson's equation**: ∇²φ = −ρ/ε₀. This single PDE encodes all of electrostatics — every static electric field problem reduces to solving it. In a region free of charge (ρ = 0), it simplifies to **Laplace's equation**: ∇²φ = 0. The strategy shift is profound: instead of summing up the contributions of every charge directly, you find a potential function satisfying a partial differential equation and then recover E by differentiation.

Solutions to Laplace's equation are called **harmonic functions**, and they have a remarkable property: the value of φ at any point equals the average of φ over any sphere centered on that point. This **mean value theorem** immediately implies that harmonic functions cannot have local maxima or minima in a charge-free region — the potential must take its extreme values on the boundary. This is not just a mathematical curiosity; it is the foundation of **uniqueness theorems**. If you specify φ (Dirichlet) or ∂φ/∂n (Neumann) on all boundaries of a charge-free region, then the solution inside is unique. This means you can solve a problem in any convenient way — by symmetry, by guessing a form, by conformal mapping — and if you find a solution satisfying the boundary conditions, it is the only one.

The practical approach to solving Laplace's equation in many geometries is **separation of variables**. In Cartesian coordinates, you assume φ(x,y,z) = X(x)Y(y)Z(z) and find that each factor satisfies an ordinary differential equation with a separation constant. In spherical coordinates — natural for problems with a center of symmetry — the radial and angular parts separate into polynomial (Legendre) and exponential solutions, building toward the spherical harmonic decompositions that reappear in quantum mechanics. The key is choosing coordinates that match the symmetry of the boundary conditions.

For Poisson's equation with known source distributions, **Green's functions** provide the general framework. The Green's function G(r, r′) is the potential at r due to a unit point charge at r′, accounting for boundary conditions. Once you know G, the potential for any charge distribution is an integral: φ(r) = ∫ G(r,r′) ρ(r′)/ε₀ dV′. For an unbounded region, G = 1/(4πε₀|r − r′|), which is just the Coulomb potential — recovering the familiar superposition principle as a special case of the Green's function method. The general Green's function machinery handles conductors, cavities, and grounded surfaces by adding image charges or boundary correction terms, revealing the deep unity between seemingly different solution techniques.
