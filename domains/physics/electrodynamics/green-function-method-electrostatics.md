---
id: green-function-method-electrostatics
title: Green Function Method for Electrostatics
domain: physics
course: electrodynamics
prerequisites:
- id: boundary-value-problems-electrostatics
  type: hard
- id: laplace-poisson-equations-electrostatics
  type: hard
- id: spherical-harmonics-electrostatics
  type: soft
builds-toward:
- green-function-method-electrostatics
- method-of-images
tags:
- greens-functions
- boundary-value-problems
- poisson-equation
stage: advanced
status: draft
---

# Green Function Method for Electrostatics

## Core Idea
Green's functions are fundamental solutions to the Poisson equation that encode boundary conditions. The Green function method reduces electrostatic boundary value problems to integral equations over sources and boundaries.

## How It's Best Learned
Derive Green's function for simple geometries (infinite plane, sphere) and verify reciprocity. Apply to conductors and dielectrics to see how boundary conditions determine the Green function.

## Explainer

You have worked through boundary value problems by expanding in known eigenfunctions — spherical harmonics, Fourier series — and matching coefficients at boundaries. The Green function method offers a more general and powerful perspective: instead of choosing a basis, you find the potential due to a single point source at every possible source location, encoding all boundary effects, and then superpose. The key question becomes: what potential does the geometry produce in response to a unit charge placed at position r'? That response function is the **Green function** G(r, r').

The connection to what you already know is direct. The Poisson equation ∇²φ = −ρ/ε₀ is a linear differential equation, and linear equations obey superposition. If you know how to solve ∇²G(r,r') = −δ³(r − r') with the appropriate boundary conditions (G = 0 on conducting surfaces for Dirichlet problems), then the solution for any charge distribution ρ follows by integration: φ(r) = ∫ G(r,r') ρ(r')/ε₀ d³r'. The Green function is essentially the impulse response of the Poisson operator — the same idea that appears in signal processing and differential equations for linear systems. You already know that the free-space Poisson equation has the solution φ = kq/r for a point charge; the free-space Green function is just G₀(r,r') = 1/(4π|r − r'|), which encodes that Coulomb law.

The complication — and the power — comes from boundary conditions. In free space, G₀ is simple. But if you introduce a grounded conducting sphere, the Green function must satisfy G = 0 on the sphere's surface. The **method of images** can be seen as a technique for constructing the modified Green function: you place an image charge outside the domain so that the total potential (real charge + image) vanishes on the boundary surface. The Green function with boundary conditions thus contains all the physics of how the conductor responds to a source charge — the induced surface charge distribution is implicitly encoded in G.

**Reciprocity** is one of the most elegant properties: G(r,r') = G(r',r). The potential at r due to a unit source at r' equals the potential at r' due to a unit source at r. This symmetry reflects the self-adjoint nature of the Laplacian operator and has deep physical meaning: the mutual capacitance coefficient between two conductors is symmetric. In practice, reciprocity provides a consistency check on any computed Green function. Once you have G for a given geometry, computing the potential for any charge distribution is reduced to a single integral — the hard work of satisfying boundary conditions is done once and encoded in G, after which new source distributions require only integration, not a new boundary value calculation.
