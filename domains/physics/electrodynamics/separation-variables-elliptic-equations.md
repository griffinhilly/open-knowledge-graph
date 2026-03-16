---
id: separation-variables-elliptic-equations
title: Separation of Variables for Elliptic PDEs
domain: physics
course: electrodynamics
prerequisites:
- id: boundary-value-problems-electrostatics
  type: hard
- id: separation-variables-pde
  type: soft
builds-toward:
- laplace-poisson-equations-electrostatics
tags:
- separation-of-variables
- pde-solution
stage: advanced
status: draft
---

# Separation of Variables for Elliptic PDEs

## Core Idea
Separation of variables reduces partial differential equations (Laplace, Poisson, wave equations) into ordinary differential equations by assuming separable solutions. In Cartesian coordinates, this yields sines and cosines; in cylindrical coordinates, Bessel functions; in spherical coordinates, Legendre polynomials. This technique is fundamental for solving structured BVPs and understanding the spectrum of modes in confined geometries.

## Explainer

You know that boundary value problems in electrostatics require solving Laplace's equation ∇²V = 0 (or Poisson's equation where charge is present) with V or ∂V/∂n prescribed on boundaries. This partial differential equation couples all three spatial variables simultaneously, which seems forbidding. Separation of variables is a powerful trick that breaks the problem into three independent ordinary differential equations — each involving only one variable — that you already know how to solve.

The strategy is to guess a **product-form solution**: V(x,y,z) = X(x)Y(y)Z(z). Substituting into Laplace's equation and dividing through by XYZ gives X''/X + Y''/Y + Z''/Z = 0. Since each term depends only on one variable, and they must sum to zero for all x, y, z, each term must individually equal a constant: X''/X = k_x², Y''/Y = k_y², Z''/Z = k_z², with k_x² + k_y² + k_z² = 0. Each coordinate now obeys its own ODE. In Cartesian coordinates the solutions are sines, cosines, or exponentials; which combination applies depends on the sign of each separation constant and the geometry of the boundary.

The real power emerges from **superposition**. Because Laplace's equation is linear, any sum of solutions is also a solution. The general solution is an infinite series of these product solutions, with coefficients determined by matching the boundary conditions. This matching step uses the **orthogonality** of the basis functions: just as Fourier series coefficients are extracted by integrating against sin(nπx/L), the coefficients in your series are extracted by integrating the boundary condition against each basis function in turn. The difficult-looking boundary condition decomposes cleanly into independent mode amplitudes.

In curvilinear coordinates the same idea applies but the ODEs change character. In **cylindrical coordinates**, the radial equation produces **Bessel functions** J_n(kr) — oscillatory functions that replace the sines and cosines of Cartesian coordinates near the axis, decaying differently from them far from it. In **spherical coordinates**, the radial equation yields power laws r^ℓ and r^(−ℓ−1), while the angular equations yield **Legendre polynomials** P_ℓ^m(cosθ) and complex exponentials in φ. The products of these angular solutions are the **spherical harmonics** Y_ℓ^m(θ,φ) that appear identically in atomic orbital shapes, multipole expansions of charge distributions, and gravitational potential theory — because physical systems with spherical symmetry always decompose into the same angular eigenfunctions regardless of the physics being modeled.
