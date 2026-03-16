---
id: boundary-value-problems-em
title: Separation of Variables for Boundary Value Problems
domain: physics
course: electrodynamics
prerequisites:
- id: method-of-images
  type: soft
- id: differential-equations
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- cavity-resonators
tags:
- boundary-value-problems
- pde
- separation
stage: abstract-reasoning
status: draft
---

# Separation of Variables for Boundary Value Problems

## Core Idea
Separation of variables systematically solves Laplace's and Poisson's equations in bounded regions with specified boundary conditions. Assuming solutions of the form f(x,y,z) = X(x)Y(y)Z(z) reduces the PDE to ODEs. Boundary conditions determine which eigenfunction combinations satisfy the full problem.

## Explainer

You know from multivariable calculus that Laplace's equation ∇²V = 0 governs the electric potential in charge-free regions. In principle, any function satisfying this PDE is a valid solution — the challenge is finding the *particular* solution that also matches the boundary conditions (specified potential or field values on the surfaces bounding the region). **Separation of variables** is the systematic strategy for doing this when the geometry aligns with a coordinate system.

The key assumption is that the potential can be written as a product of single-variable functions: V(x,y,z) = X(x)Y(y)Z(z). Substituting into ∇²V = 0 and dividing by XYZ gives (X''/X) + (Y''/Y) + (Z''/Z) = 0. Because each term depends on a different variable, each must independently equal a constant. This turns one PDE into three ODEs: X'' = k²ₓX, Y'' = k²ᵧY, Z'' = k²ᵤZ with k²ₓ + k²ᵧ + k²ᵤ = 0. The separation constants must satisfy this constraint, coupling the three equations. The solutions are exponentials, sines/cosines, or hyperbolic functions depending on the sign of each constant.

The boundary conditions do two jobs: they select which **eigenfunctions** are allowed (by forcing solutions to vanish at walls or match specified values), and they determine the coefficients of each allowed mode. For example, if V = 0 on two parallel walls at x = 0 and x = a, only X(x) = sin(nπx/a) for integer n satisfies both conditions. The allowed values of n are the eigenvalues, and the corresponding sin(nπx/a) are the eigenfunctions. A general solution is then a superposition: V = ΣAₙ sin(nπx/a)·f(y,z), and the remaining boundary conditions determine the Aₙ coefficients via Fourier analysis.

The method of images, which you may know as a soft prerequisite, solves a different class of boundary problems by replacing conductors with image charges. Separation of variables is complementary: it works in bounded geometries where the method of images doesn't directly apply. Together, they cover most analytically tractable electrostatic configurations — parallel plates, rectangular boxes, cylindrical cavities, spherical shells. The solutions you find here also form the template for solving waveguide and resonator problems, where the same mathematical structure (eigenvalue equations from boundary conditions) governs which modes can propagate at which frequencies.
