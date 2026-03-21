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

## Questions

```yaml
- question: "After substituting V(x,y,z) = X(x)Y(y)Z(z) into Laplace's equation and dividing by XYZ, you obtain (X''/X) + (Y''/Y) + (Z''/Z) = 0. Why must each term independently equal a constant?"
  type: multiple-choice
  options:
    - "Because the physical boundary conditions require constant separation"
    - "Because each term depends only on one variable, and a function of x alone cannot compensate for changes in a function of y and z alone — so both must be constant"
    - "Because Laplace's equation only has constant solutions in bounded regions"
    - "Because the eigenvalues of the system must be real"
  answer: 1
  explanation: "The argument is purely one of variable independence. If (X''/X) were not constant, varying x would change its value — but (Y''/Y) + (Z''/Z), depending only on y and z, cannot adjust to compensate. The only way a function of x alone can always sum with functions of y and z alone to give zero is if each term is individually constant. This reduction to constants is the mathematical core of the technique."

- question: "Boundary conditions require V = 0 at x = 0 and x = a. Which functions X(x) satisfy both conditions simultaneously?"
  type: multiple-choice
  options:
    - "X(x) = e^(kx) for any real k"
    - "X(x) = cos(nπx/a) for positive integer n"
    - "X(x) = sin(nπx/a) for positive integer n"
    - "Any linear combination of exponentials"
  answer: 2
  explanation: "To vanish at both x = 0 and x = a, X must be zero at both endpoints. sin(nπx/a) equals zero at x = 0 (since sin(0) = 0) and at x = a (since sin(nπ) = 0 for all integers n). Cosines fail because cos(0) = 1 ≠ 0. Real exponentials are positive definite and cannot vanish at two points. This selection of allowed eigenfunctions is exactly the job boundary conditions do in the method."

- question: "Boundary conditions in separation of variables serve only to constrain the coefficients (Aₙ) of the final superposition; the eigenfunctions themselves are determined by the PDE alone."
  type: true-false
  answer: false
  explanation: "False. Boundary conditions do two jobs: they first determine which eigenfunctions are allowed (selecting sin over cos, ruling out exponentials) and then — on remaining surfaces — determine the coefficients Aₙ via Fourier analysis. The PDE alone would admit infinitely many solutions; boundary conditions filter which ones are physically realized. This dual role is the key conceptual point of the method."

- question: "Once an eigenfunction X(x) = sin(nπx/a) is found for a particular n, the general solution to the boundary value problem is that single eigenfunction with an appropriate coefficient."
  type: true-false
  answer: false
  explanation: "False. There are infinitely many eigenfunctions — one for each allowed positive integer n — and the general solution is a superposition of all of them: V = ΣAₙ sin(nπx/a)·f(y,z). The coefficients Aₙ are then determined by matching the remaining boundary conditions via Fourier analysis. A single mode is generally not flexible enough to satisfy an arbitrary prescribed boundary value."

- question: "In separation of variables, why are only discrete values of the separation constant allowed (e.g., n = 1, 2, 3, ...) rather than a continuous range of values?"
  type: short-answer
  answer: "Boundary conditions impose simultaneous constraints that only certain spatial frequencies can satisfy. For example, the condition V = 0 at both x = 0 and x = a forces sin(nπx/a) to vanish at both walls — which only works when the argument equals a multiple of π at x = a, selecting integers n = 1, 2, 3, .... A non-integer value of n would produce a function that satisfies the ODE but fails at least one boundary condition. The allowed discrete values are the eigenvalues; the corresponding functions are eigenfunctions."
  explanation: "The analogy is to standing waves on a string fixed at both ends: only wavelengths that fit exactly between the endpoints are allowed. Continuous values of the separation constant correspond to 'modes' that don't fit the boundaries. The fact that boundary conditions quantize the solution spectrum is the mathematical connection between classical boundary value problems and quantum mechanics — eigenvalue equations arise in both contexts for the same reason."
```

## Explainer

You know from multivariable calculus that Laplace's equation ∇²V = 0 governs the electric potential in charge-free regions. In principle, any function satisfying this PDE is a valid solution — the challenge is finding the *particular* solution that also matches the boundary conditions (specified potential or field values on the surfaces bounding the region). **Separation of variables** is the systematic strategy for doing this when the geometry aligns with a coordinate system.

The key assumption is that the potential can be written as a product of single-variable functions: V(x,y,z) = X(x)Y(y)Z(z). Substituting into ∇²V = 0 and dividing by XYZ gives (X''/X) + (Y''/Y) + (Z''/Z) = 0. Because each term depends on a different variable, each must independently equal a constant. This turns one PDE into three ODEs: X'' = k²ₓX, Y'' = k²ᵧY, Z'' = k²ᵤZ with k²ₓ + k²ᵧ + k²ᵤ = 0. The separation constants must satisfy this constraint, coupling the three equations. The solutions are exponentials, sines/cosines, or hyperbolic functions depending on the sign of each constant.

The boundary conditions do two jobs: they select which **eigenfunctions** are allowed (by forcing solutions to vanish at walls or match specified values), and they determine the coefficients of each allowed mode. For example, if V = 0 on two parallel walls at x = 0 and x = a, only X(x) = sin(nπx/a) for integer n satisfies both conditions. The allowed values of n are the eigenvalues, and the corresponding sin(nπx/a) are the eigenfunctions. A general solution is then a superposition: V = ΣAₙ sin(nπx/a)·f(y,z), and the remaining boundary conditions determine the Aₙ coefficients via Fourier analysis.

The method of images, which you may know as a soft prerequisite, solves a different class of boundary problems by replacing conductors with image charges. Separation of variables is complementary: it works in bounded geometries where the method of images doesn't directly apply. Together, they cover most analytically tractable electrostatic configurations — parallel plates, rectangular boxes, cylindrical cavities, spherical shells. The solutions you find here also form the template for solving waveguide and resonator problems, where the same mathematical structure (eigenvalue equations from boundary conditions) governs which modes can propagate at which frequencies.
