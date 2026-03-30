---
id: christoffel-symbols
title: Christoffel Symbols
domain: physics
course: general-relativity
prerequisites:
- id: tensor-calculus-gr
  type: hard
- id: curved-spacetime-metric-tensor
  type: hard
- id: connections-covariant-derivative
  type: hard
tags:
- christoffel-symbols
- connection
- covariant-derivative
- metric-compatibility
- levi-civita
stage: expert
status: validated
---

# Christoffel Symbols

## Core Idea
The Christoffel symbols Γ^λ_{μν} are the connection coefficients of the unique torsion-free, metric-compatible connection on a pseudo-Riemannian manifold (the Levi-Civita connection). They are computed entirely from the metric tensor and its first partial derivatives: Γ^λ_{μν} = (1/2) g^{λσ}(∂_μ g_νσ + ∂_ν g_μσ - ∂_σ g_μν). Although Christoffel symbols are not tensors — they can be made to vanish at any single point by choosing locally inertial coordinates — they are essential for constructing the covariant derivative, the geodesic equation, and ultimately the curvature tensors. They encode how the coordinate basis vectors change from point to point, serving as the gravitational analog of a force in the equations of motion.

## Questions

```yaml
- question: "The Christoffel symbols Γ^λ_{μν} transform as a tensor under general coordinate transformations."
  type: true-false
  answer: false
  explanation: "Christoffel symbols are not tensors. Under a coordinate transformation, they pick up an inhomogeneous term involving the second derivative of the coordinate transformation: Γ'^λ_{μν} = (∂x'^λ/∂x^σ)(∂x^α/∂x'^μ)(∂x^β/∂x'^ν) Γ^σ_{αβ} + (∂x'^λ/∂x^σ)(∂²x^σ/∂x'^μ ∂x'^ν). This extra term is precisely what allows the covariant derivative (which combines partial derivatives and Christoffel symbols) to transform as a tensor. At any single point, one can choose coordinates (Riemann normal coordinates) where all Christoffel symbols vanish, which is impossible for a genuine tensor that is nonzero."

- question: "In Riemann normal coordinates centered at a point P, all Christoffel symbols vanish at P. What does this imply physically?"
  type: multiple-choice
  options:
    - "Spacetime is flat at P"
    - "The gravitational field vanishes at P, confirming the equivalence principle — a freely falling observer experiences no gravitational acceleration locally"
    - "The curvature tensor vanishes at P"
    - "The metric equals the Minkowski metric everywhere in these coordinates"
  answer: 1
  explanation: "Riemann normal coordinates are the mathematical realization of a local freely falling frame. At the chosen point, Γ^λ_{μν} = 0 and g_μν = η_μν, so the equations of motion reduce to those of special relativity — the equivalence principle in action. However, the first derivatives of the Christoffel symbols (and hence the curvature tensor) generally do not vanish, so spacetime is not flat (option A is wrong). The metric equals η_μν only at P, not everywhere (option D is wrong). Curvature is a tensor and cannot be made to vanish by a coordinate choice (option C is wrong)."

- question: "Derive the number of independent Christoffel symbols Γ^λ_{μν} in four-dimensional spacetime, given their symmetry in the lower two indices."
  type: short-answer
  answer: "Christoffel symbols are symmetric in their lower two indices: Γ^λ_{μν} = Γ^λ_{νμ} (because the Levi-Civita connection is torsion-free). The upper index λ runs over 4 values. The symmetric pair (μ,ν) has 4×5/2 = 10 independent combinations. Therefore the total number of independent Christoffel symbols is 4 × 10 = 40."
  explanation: "The 40 independent Christoffel symbols encode how the 10 independent metric components vary across the 4 coordinate directions, minus the constraints imposed by metric compatibility and vanishing torsion. Despite this large number, they are all determined by the metric through the standard formula — there are no additional degrees of freedom in the connection."

- question: "Why are Christoffel symbols sometimes called 'gravitational force' terms in the geodesic equation, and in what sense is this description misleading?"
  type: short-answer
  answer: "In the geodesic equation d²x^λ/dτ² + Γ^λ_{μν}(dx^μ/dτ)(dx^ν/dτ) = 0, the Christoffel symbol term plays a role analogous to the force term in Newton's second law: it causes the coordinate acceleration d²x^λ/dτ² to be nonzero even for a freely falling particle. In the Newtonian limit, the Γ^0_{00} component reduces to the gradient of the gravitational potential. However, calling them 'forces' is misleading because Christoffel symbols are coordinate-dependent and can be made to vanish at any point — a genuine physical force (like an electromagnetic force) cannot be eliminated by a coordinate choice. The Christoffel terms represent the effect of using non-inertial coordinates, not a real force."
  explanation: "This is the mathematical expression of the equivalence principle: gravity as described by Christoffel symbols is locally eliminable, just as a gravitational field is locally equivalent to acceleration. The true, non-eliminable gravitational effects are encoded in the curvature tensor, which involves derivatives of the Christoffel symbols."
```

## Explainer

When you write the covariant derivative of a vector field V^λ, you need to account for the fact that the coordinate basis vectors e_μ = ∂/∂x^μ themselves change from point to point in curved spacetime (or even in curvilinear coordinates on flat spacetime). The Christoffel symbols Γ^λ_{μν} quantify exactly this change: ∇_μ e_ν = Γ^λ_{μν} e_λ. The covariant derivative of V^λ is then ∇_μ V^λ = ∂_μ V^λ + Γ^λ_{μσ} V^σ, where the first term captures how the components change and the second term corrects for the changing basis. For a covariant vector (one-form) W_λ, the correction has the opposite sign: ∇_μ W_λ = ∂_μ W_λ - Γ^σ_{μλ} W_σ. The pattern extends straightforwardly to arbitrary-rank tensors, with one Christoffel term for each index.

The specific form of the Christoffel symbols in GR is fixed by two requirements: the connection must be torsion-free (Γ^λ_{μν} = Γ^λ_{νμ}) and metric-compatible (∇_σ g_μν = 0). These two conditions together uniquely determine the Levi-Civita connection, whose components are given by the textbook formula Γ^λ_{μν} = (1/2) g^{λσ}(∂_μ g_νσ + ∂_ν g_μσ - ∂_σ g_μν). Metric compatibility means that the covariant derivative preserves inner products: if two vectors are parallel-transported along a curve, the angle and magnitudes measured by the metric remain constant. Vanishing torsion means that the antisymmetric part of the connection is zero, which ensures that coordinate-based constructions like the commutator of partial derivatives behave consistently.

Computing Christoffel symbols from a given metric is one of the core mechanical tasks in GR. For the Schwarzschild metric, for example, only a handful of the 40 potentially independent components are nonzero (thanks to the spherical symmetry and static nature of the solution), but each one is a specific function of the radial coordinate involving the mass parameter M. In the weak-field, slow-motion limit, the dominant Christoffel symbol Γ^i_{00} ≈ (1/2) ∂_i g_{00} reduces to ∂_i Φ/c², where Φ is the Newtonian gravitational potential — recovering Newton's gravitational acceleration from the geometry of spacetime.

The most important conceptual point about Christoffel symbols is their coordinate dependence. At any chosen point P, you can always find coordinates (Riemann normal coordinates) in which all 40 Christoffel symbols vanish and the metric equals the Minkowski metric. This is the mathematical statement of the equivalence principle: a freely falling observer at P sees no gravitational acceleration. But the first derivatives of the Christoffel symbols — which enter the Riemann curvature tensor — generally cannot be made to vanish. The Christoffel symbols themselves encode the "gravitational field" (which is coordinate-dependent and locally removable), while the curvature tensor encodes the tidal gravitational effects (which are coordinate-independent and physically real). This distinction between connection and curvature is one of the deepest insights in the mathematical structure of GR.
