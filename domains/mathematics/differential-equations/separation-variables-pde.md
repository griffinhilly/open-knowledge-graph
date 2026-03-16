---
id: separation-variables-pde
title: Separation of Variables for Partial Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: heat-equation-pde
  type: hard
- id: systems-first-order-linear-odes
  type: soft
builds-toward:
- wave-equation-pde
tags:
- separation-variables
- pde
- method
stage: advanced
status: draft
---

# Separation of Variables for Partial Differential Equations

## Core Idea
Separation of variables assumes u(x,t) = X(x)T(t) as a product. Substituting into a PDE yields an equation where one side depends only on x and the other only on t; both must equal a constant. This reduces the PDE into ODEs for X and T solvable separately. Superposing solutions for multiple separation constants yields the general solution.

## Explainer

A partial differential equation involves a function u of two or more variables and its partial derivatives. Unlike an ODE, you cannot just integrate both sides — the solution is a function of multiple variables, and any arbitrary function of the "other" variable could appear. The **separation of variables** method cuts through this complexity with a single bold assumption: suppose the solution happens to be a product, u(x, t) = X(x) · T(t), where X depends only on x and T depends only on t. This assumption is almost certainly not true for the general solution, but it is a productive lie — solutions of this product form are easy to find, and superposing many of them reconstructs the general solution.

To see the mechanism, apply the method to the heat equation u_t = κ u_{xx}. Substituting u = XT gives X T' = κ X'' T. Dividing both sides by κXT yields T'/(κT) = X''/X. The left side depends only on t; the right side depends only on x. Since x and t are independent variables, the only way a function of t alone can equal a function of x alone for all x and t is if both sides equal the same constant, say −λ. This produces two ODEs: T' = −κλT and X'' = −λX. Both are ODEs you already know how to solve — the first is exponential decay (T = e^{−κλt}), the second depends on the sign of λ. For λ > 0, X is sinusoidal; for λ < 0, X is exponential; for λ = 0, X is linear.

Boundary conditions on the spatial variable x determine which values of λ are allowed — these are the **eigenvalues** of the problem. For example, on a rod with endpoints held at zero temperature (X(0) = 0, X(L) = 0), the condition X(0) = 0 forces the solution to be X = sin(nπx/L), and X(L) = 0 then requires λ = (nπ/L)² for positive integers n. Each eigenvalue λₙ gives one separated solution uₙ(x, t) = sin(nπx/L) · e^{−κ(nπ/L)²t}. This is where your ODE systems background connects: the structure is analogous to finding the eigenvalues and eigenvectors of a matrix, but in function space.

The full solution is assembled by **superposition**: u(x, t) = Σ bₙ sin(nπx/L) e^{−κ(nπ/L)²t}. The coefficients bₙ are determined by the initial condition u(x, 0) = f(x), which requires expanding f(x) as a sum of sin functions — a Fourier sine series. This is why separation of variables and Fourier analysis are inseparable: the method generates the basis functions (the sin(nπx/L) terms), and Fourier theory tells you how to represent an arbitrary initial condition in that basis. The time dependence then comes along for free — each Fourier mode decays at its own rate, with higher spatial frequencies dying out faster.
