---
id: boundary-value-problem-types
title: Classification of Boundary Value Problems
domain: physics
course: electrodynamics
prerequisites:
- id: laplace-poisson-equations-electrostatics
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- green-function-method-electrostatics
- spherical-harmonics-electrostatics
tags:
- boundary-conditions
- dirichlet
- neumann
- mixed-boundary-conditions
stage: expert
status: validated
---

# Classification of Boundary Value Problems

## Core Idea
Boundary value problems are classified by the type of boundary condition: Dirichlet (potential specified), Neumann (normal field specified), or mixed. The uniqueness theorem establishes that each type has a unique solution under appropriate regularity conditions.

## Questions

```yaml
- question: "A physicist is solving Laplace's equation inside a spherical cavity and knows only the surface charge density (not the potential) on every part of the boundary. Which type of boundary condition is this, and what does the uniqueness theorem say about the solution?"
  type: multiple-choice
  options:
    - "Dirichlet; the solution is unique"
    - "Neumann; the solution is unique up to an additive constant"
    - "Mixed; no unique solution exists without additional constraints"
    - "Dirichlet; the solution is unique up to an additive constant"
  answer: 1
  explanation: "Knowing the surface charge density is equivalent to knowing σ = ε₀E_n, the normal component of the electric field, which equals −ε₀(∂V/∂n). This is a Neumann boundary condition — the normal derivative of V is specified. The uniqueness theorem for Neumann problems states that the solution is unique up to an additive constant: you can always add a global constant to V without changing E (since E = −∇V). This ambiguity is physical — the absolute potential is arbitrary; only differences matter."

- question: "The method of images replaces a physical configuration (a point charge near a grounded conducting plane) with a simpler equivalent (a point charge and its mirror image, no plane). Why is this substitution valid?"
  type: multiple-choice
  options:
    - "Because the image charge produces the same total charge as the original problem"
    - "Because the method of images only works when the boundary is an equipotential surface"
    - "Because the uniqueness theorem guarantees that any solution satisfying the boundary conditions is the unique physical solution — finding it by any method is sufficient"
    - "Because both configurations satisfy Gauss's law globally"
  answer: 2
  explanation: "The uniqueness theorem is exactly what justifies the method of images. The grounded plane requires V = 0 on the plane (Dirichlet condition). The image charge configuration produces V = 0 everywhere on the plane and satisfies Laplace's equation in the region above the plane. Since those are exactly the boundary conditions of the original problem, and since the uniqueness theorem says only one solution can satisfy those conditions, the image configuration must be the right answer. It doesn't matter how you found the solution — any valid solution is the solution."

- question: "Specifying the normal derivative ∂V/∂n on a closed boundary is equivalent to specifying the potential V itself on that boundary."
  type: true-false
  answer: false
  explanation: "These are two fundamentally different types of boundary conditions with different physical content. A Dirichlet condition specifies V directly — as on a conductor held at a fixed voltage. A Neumann condition specifies ∂V/∂n, which corresponds to the normal electric field and thus to surface charge density. They are not interchangeable: Dirichlet problems have a unique solution, while Neumann problems are unique only up to an additive constant. Knowing the surface charge density tells you about E, not V."

- question: "The uniqueness theorem justifies solving electrostatic boundary value problems by any means necessary — including clever tricks, symmetry arguments, or images — because once you find a solution satisfying the boundary conditions, you know no other solution exists."
  type: true-false
  answer: true
  explanation: "This is the practical power of the uniqueness theorem. It is proved by assuming two solutions exist, taking their difference (which satisfies Laplace's equation with zero boundary conditions), and showing by energy arguments that this difference must be zero. The conclusion is that any valid solution is the unique physical solution. This is what licenses the method of images, Fourier series methods, and other non-obvious approaches: you don't need to derive the solution from first principles — you just need to find it."

- question: "A Neumann boundary value problem has a solution that is 'unique up to an additive constant.' What does this mean physically, and why doesn't it affect the ability to compute the electric field?"
  type: short-answer
  answer: "It means any two solutions to a Neumann problem can differ only by a global constant: if V(r) is one solution, then V(r) + C is another for any constant C. Physically, only potential differences matter — the absolute value of the potential at a single point is arbitrary and has no physical meaning. The electric field E = −∇V is unaffected by adding a constant because the gradient of a constant is zero. So the non-uniqueness is physically trivial: both solutions give the same electric field, the same forces, and the same energy differences."
  explanation: "This is why in problems where you only know the surface charge (Neumann), you can still uniquely determine the electric field even though the potential is only determined up to a constant. The ambiguity is absorbed by the freedom to choose a reference point for the zero of potential — a choice that has no physical consequence."
```

## Explainer

From Laplace's and Poisson's equations you know that the electrostatic potential V satisfies ∇²V = 0 in free space (or ∇²V = −ρ/ε₀ with sources). These are partial differential equations with infinitely many solutions taken alone. A **boundary value problem** (BVP) pins down the unique physical solution by specifying conditions on V at the boundaries of the region. The classification of BVPs by boundary condition type tells you what physical information you need to specify and whether a unique solution is guaranteed.

A **Dirichlet boundary condition** specifies the value of the potential V itself on the boundary. This corresponds physically to grounded or held-at-fixed-voltage conductors: you know V = 0 on a grounded surface or V = V₀ on a conductor held at potential V₀. This is the most common type in electrostatics. The Dirichlet problem always has a unique solution when V is specified on a closed surface enclosing the region of interest — a consequence of the maximum principle for harmonic functions.

A **Neumann boundary condition** specifies the normal derivative ∂V/∂n on the boundary, which equals −E_n, the normal component of the electric field. This arises when you know the surface charge density (since σ = ε₀E_n from the boundary condition on E) but not the potential itself. For example, if charge is deposited on an insulating surface where you know the charge density but not the resulting potential, you have a Neumann problem. Neumann problems have a unique solution up to an additive constant — you can always add a constant to V without changing E.

**Mixed boundary conditions** specify V on part of the boundary and ∂V/∂n on the rest. Real problems often combine grounded conductors (Dirichlet) with insulating surfaces carrying known charge (Neumann) in the same geometry. The **uniqueness theorem** — proved by supposing two solutions exist, subtracting them, and showing the difference must be zero — is the key theoretical result: it tells you that finding any solution satisfying the boundary conditions is sufficient, because that solution is the only one. This justifies powerful shortcut methods like the method of images, where you replace a complex physical setup with a simpler equivalent that happens to satisfy the same boundary conditions.
