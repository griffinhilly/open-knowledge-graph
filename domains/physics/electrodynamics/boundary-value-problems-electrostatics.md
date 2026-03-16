---
id: boundary-value-problems-electrostatics
title: Boundary Value Problems in Electrostatics
domain: physics
course: electrodynamics
prerequisites:
- id: laplace-poisson-equations-electrostatics
  type: hard
- id: dirichlet-neumann-boundary-conditions
  type: soft
builds-toward:
- method-of-images
- separation-variables-elliptic-equations
tags:
- boundary-value-problems
- electrostatics
stage: advanced
status: draft
---

# Boundary Value Problems in Electrostatics

## Core Idea
Boundary value problems (BVPs) in electrostatics involve finding the potential satisfying Poisson's equation in a region, subject to boundary conditions on its surface. The boundary conditions (Dirichlet, Neumann, or mixed) specify either the potential or its normal derivative, and uniqueness theorems guarantee a unique solution. BVPs are ubiquitous in engineering and physics, describing fields near conductors, dielectrics, and complex electrode configurations.

## Explainer

From your study of Laplace's and Poisson's equations, you know that the electrostatic potential Φ satisfies ∇²Φ = −ρ/ε₀ throughout space, reducing to ∇²Φ = 0 in charge-free regions. But a differential equation alone has infinitely many solutions — any harmonic function satisfies Laplace's equation. What singles out the physically correct one is the **boundary conditions**: information about the potential or its derivatives on the boundary surfaces that enclose the region of interest.

There are two fundamental types of boundary conditions. **Dirichlet conditions** specify the value of the potential on a surface — for instance, a grounded conductor enforces Φ = 0 everywhere on its surface. **Neumann conditions** specify the normal derivative ∂Φ/∂n on a surface — since E = −∇Φ and E_n = σ/ε₀ at a conductor surface, knowing the surface charge density gives you the normal derivative of Φ. The **uniqueness theorem** is the cornerstone of this subject: given a region, its bounding surfaces, and appropriate boundary conditions (Dirichlet, Neumann, or mixed), the solution for Φ is unique. This means that if you can *guess* a solution by any means and verify it satisfies both Poisson's equation and the boundary conditions, it must be the right answer — a license to be clever.

The methods of solution exploit this uniqueness in different ways. **Separation of variables** assumes Φ(x,y,z) = X(x)Y(y)Z(z) and decomposes the PDE into three ordinary differential equations coupled by separation constants. Applied to a rectangular box with specified potentials on its faces, this yields Fourier series solutions. The boundary conditions determine which terms survive and what the coefficients are. **The method of images** — a topic you will encounter next — uses uniqueness even more boldly: replace a conductor with a fictitious "image charge" that reproduces the correct boundary condition, then solve for the field of the original plus image charges in free space. The uniqueness theorem guarantees this trick gives the correct answer inside the original region.

The practical power of BVPs is that they describe every real electrostatics problem: designing electrode geometries, finding fields inside capacitors of arbitrary shape, calculating shielding effectiveness. The physics is encoded entirely in Poisson's equation plus boundary conditions — a complete, self-contained mathematical problem whose unique solution is the physical reality.
