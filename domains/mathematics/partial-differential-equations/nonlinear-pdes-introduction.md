---
id: nonlinear-pdes-introduction
title: Nonlinear PDEs Introduction
domain: mathematics
course: partial-differential-equations
prerequisites:
- id: weak-solutions-rigorous
  type: hard
- id: conservation-laws-weak-solutions-intro
  type: hard
- id: maximum-principles-pdes
  type: soft
tags: [pde, nonlinear, semilinear, quasilinear, blow-up]
stage: expert
status: validated
---
# Nonlinear PDEs Introduction

## Core Idea
Nonlinear PDEs arise when the equation depends nonlinearly on the unknown function or its derivatives, breaking the superposition principle that makes linear theory tractable. They are classified by degree of nonlinearity: semilinear (nonlinear in u but linear in highest derivatives, like -Δu = u³), quasilinear (coefficients of highest derivatives depend on u, like div(|∇u|^{p-2}∇u) = 0), and fully nonlinear (arbitrary dependence on highest derivatives, like det(D²u) = f). Each class requires different techniques, and fundamentally new phenomena emerge: blow-up in finite time, multiple solutions, pattern formation, and solitons.

## Questions
```yaml
- question: "Which of the following is a semilinear PDE?"
  type: multiple-choice
  options:
    - "-Δu + u³ = 0"
    - "div(|∇u|^{p-2}∇u) = 0 (p-Laplacian)"
    - "det(D²u) = f (Monge-Ampere)"
    - "u_t + uu_x = 0 (Burgers)"
  answer: 0
  explanation: "Semilinear means the highest-order derivatives appear linearly (here, -Δu is linear in second derivatives) while lower-order terms are nonlinear (u³). The p-Laplacian is quasilinear, Monge-Ampere is fully nonlinear, and Burgers is quasilinear (first-order)."
- question: "The superposition principle holds for nonlinear PDEs."
  type: true-false
  answer: false
  explanation: "If u₁ and u₂ are solutions of a nonlinear PDE, their sum u₁ + u₂ is generally NOT a solution. This is the fundamental difference from linear theory: we cannot build general solutions from particular ones. Each nonlinear problem must be attacked individually."
- question: "What is finite-time blow-up in nonlinear PDEs?"
  type: short-answer
  answer: "The solution becomes unbounded (||u(·,t)|| → ∞) at some finite time T* < ∞, so no global solution exists"
  explanation: "Blow-up is a genuinely nonlinear phenomenon absent from linear PDEs. For example, the ODE u_t = u² has solutions that blow up at t = 1/u₀. Similarly, the semilinear heat equation u_t = Δu + u^p can have solutions that become infinite in finite time when p > 1, depending on the initial data."
- question: "The p-Laplacian equation div(|∇u|^{p-2}∇u) = 0 for p ≠ 2 is:"
  type: multiple-choice
  options:
    - "Quasilinear"
    - "Semilinear"
    - "Fully nonlinear"
    - "Linear"
  answer: 0
  explanation: "The highest-order term involves second derivatives of u, but its coefficients depend on the first derivatives of u (through |∇u|^{p-2}). This makes it quasilinear. For p = 2 it reduces to Laplace's equation."
```

## Explainer
Nonlinear PDEs are ubiquitous in science and mathematics: fluid mechanics (Navier-Stokes, Euler), general relativity (Einstein), quantum mechanics (nonlinear Schrodinger), materials science (Ginzburg-Landau), and geometry (Ricci flow, minimal surfaces) all involve nonlinear PDEs. The loss of the superposition principle means that the powerful linear machinery—Green's functions, Fourier transforms, spectral decompositions—cannot be applied directly. Instead, nonlinear PDE theory relies on a combination of a priori estimates, fixed-point theorems, variational methods, and comparison principles.

Semilinear equations, where the nonlinearity affects only the lower-order terms, are the most tractable. For -Δu = f(u) on a bounded domain, the linear theory for -Δ provides a framework (Green's functions, Sobolev regularity), and the nonlinearity f(u) is handled as a perturbation. The Leray-Schauder fixed-point theorem and the mountain pass theorem are key existence tools. The critical issue is the growth rate of f: subcritical nonlinearities (growing slower than u^{(n+2)/(n-2)} in the Sobolev-critical sense) allow compact embedding arguments, while supercritical nonlinearities can produce non-existence or blow-up.

Quasilinear equations, where the highest derivatives have coefficients depending on u or ∇u, present deeper challenges because the equation itself changes character as the solution evolves. The p-Laplacian div(|∇u|^{p-2}∇u) = 0 is degenerate elliptic (the coefficient |∇u|^{p-2} vanishes where ∇u = 0), and its solutions are C^{1,α} but generally not C^2. The regularity theory of De Giorgi-Nash-Moser provides Holder continuity for divergence-form quasilinear equations under very general structural conditions, using an iterative argument that bootstraps L^∞ bounds into Holder estimates.

Fully nonlinear equations like the Monge-Ampere equation det(D²u) = f and Hamilton-Jacobi equations H(x, Du) = 0 require entirely different frameworks—viscosity solutions for first-order equations, and the Evans-Krylov theory for second-order convex equations. The interplay between existence, uniqueness, regularity, and blow-up makes nonlinear PDE theory one of the richest and most active areas of modern mathematics. Many fundamental questions remain open: global regularity for Navier-Stokes (a Millennium Prize problem), singularity formation in the Euler equations, and the full regularity theory for the Monge-Ampere equation in non-convex settings.
