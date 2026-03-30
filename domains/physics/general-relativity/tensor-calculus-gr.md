---
id: tensor-calculus-gr
title: Tensor Calculus in General Relativity
domain: physics
course: general-relativity
prerequisites:
- id: curved-spacetime-metric-tensor
  type: hard
- id: linear-transformations
  type: hard
- id: partial-derivatives
  type: hard
- id: tangent-spaces
  type: hard
- id: four-vectors
  type: soft
tags:
- tensors
- covariance
- index-notation
- contravariant
- covariant
- tensor-transformation
stage: expert
status: validated
---

# Tensor Calculus in General Relativity

## Core Idea
Tensors are the mathematical objects that transform in a well-defined way under general coordinate transformations, making them the natural language for expressing physical laws in a form that is valid in all coordinate systems (general covariance). A tensor of type (p,q) has p contravariant (upper) indices and q covariant (lower) indices, and transforms with p factors of the Jacobian and q factors of the inverse Jacobian under coordinate changes. The metric tensor raises and lowers indices, connecting contravariant and covariant components. Einstein's summation convention, index manipulation, symmetrization, and antisymmetrization form the computational backbone of GR. The requirement that physical equations be tensor equations — valid in all coordinates — is the mathematical expression of the principle of general covariance.

## Questions

```yaml
- question: "Under a coordinate transformation x^μ → x'^μ, a rank-(1,1) tensor T^μ_ν transforms as:"
  type: multiple-choice
  options:
    - "T'^μ_ν = T^μ_ν (tensors are coordinate-invariant)"
    - "T'^μ_ν = (∂x'^μ/∂x^α)(∂x^β/∂x'^ν) T^α_β"
    - "T'^μ_ν = (∂x^α/∂x'^μ)(∂x'^ν/∂x^β) T^α_β"
    - "T'^μ_ν = (∂x'^μ/∂x^α)(∂x'^ν/∂x^β) T^α_β"
  answer: 1
  explanation: "Each upper (contravariant) index transforms with ∂x'^μ/∂x^α, and each lower (covariant) index transforms with ∂x^β/∂x'^ν. For a (1,1) tensor, this gives T'^μ_ν = (∂x'^μ/∂x^α)(∂x^β/∂x'^ν) T^α_β. Option A confuses invariance of tensor equations (which hold in all frames) with invariance of components (which change). Option C and D incorrectly assign the Jacobian factors."

- question: "The partial derivative of a vector field ∂_μ V^ν is itself a tensor."
  type: true-false
  answer: false
  explanation: "Under a general coordinate transformation, ∂_μ V^ν picks up an extra term involving the second derivative of the coordinate transformation, ∂²x'^ν/∂x^α∂x^β, which spoils the tensor transformation law. This is why the covariant derivative ∇_μ V^ν is needed — the Christoffel symbol connection term cancels the unwanted second-derivative piece, producing an object that transforms as a proper (1,1) tensor. In flat spacetime with Cartesian coordinates the Christoffel symbols vanish and partial derivatives coincide with covariant derivatives, but this is a special case."

- question: "Explain what it means to 'raise an index' on a covariant vector V_μ, and why the resulting object V^μ is physically the same vector expressed differently."
  type: short-answer
  answer: "Raising an index means contracting with the inverse metric: V^μ = g^{μν} V_ν. The covariant components V_μ and the contravariant components V^μ are two different representations of the same geometric object — the vector V living in the tangent space. The metric provides the isomorphism between the tangent space and its dual (cotangent space). In flat spacetime with Cartesian coordinates, g^{μν} = η^{μν} and raising/lowering only flips the sign of the time component, but in curved spacetime or non-Cartesian coordinates the relationship is nontrivial."
  explanation: "Index raising and lowering is fundamental to GR computation. The metric tensor serves as the bridge between vectors and one-forms, and this duality is built into every tensor equation. Physically, the distinction between V^μ and V_μ reflects the difference between a displacement direction and a gradient direction, which coincide only in orthonormal coordinates."

- question: "Why does general relativity require that all physical laws be expressed as tensor equations?"
  type: short-answer
  answer: "The principle of general covariance states that the laws of physics must take the same form in all coordinate systems, since coordinates are arbitrary labels with no physical content. Tensor equations automatically satisfy this requirement: if a tensor equation holds in one coordinate system, the transformation law guarantees it holds in every coordinate system. Non-tensorial equations, by contrast, can be true in one coordinate system and false in another, making them coordinate-dependent rather than physical. Expressing laws as tensor equations ensures that physics does not depend on the observer's choice of coordinates."
  explanation: "General covariance is the mathematical implementation of the equivalence principle's lesson: no coordinate system is preferred. This does not mean all coordinate systems are equally convenient — Schwarzschild coordinates may be more practical than Kruskal for some problems — but the physics must be the same regardless."
```

## Explainer

In special relativity, the natural coordinate systems are inertial frames related by Lorentz transformations — linear transformations that preserve the Minkowski metric. Vectors transform with a single Lorentz matrix, and the machinery is relatively simple. General relativity abandons any preferred class of coordinates: you may use spherical coordinates, co-moving coordinates, rotating coordinates, or any other smooth labeling of spacetime events. The price is that coordinate transformations are now arbitrary smooth functions x^μ → x'^μ(x), and the mathematical objects describing physics must transform consistently under these general transformations. These objects are tensors.

A tensor of type (p,q) at a point in spacetime is a multilinear map that takes p one-forms and q vectors as inputs and produces a real number. In coordinates, it is represented by components with p upper (contravariant) indices and q lower (covariant) indices: T^{μ₁...μ_p}_{ν₁...ν_q}. Under a coordinate change, each upper index transforms with the Jacobian ∂x'^μ/∂x^α (the same way vector components transform) and each lower index transforms with the inverse Jacobian ∂x^β/∂x'^ν (the same way one-form components transform). The metric tensor g_μν is a (0,2) tensor; a vector field V^μ is a (1,0) tensor; the Riemann curvature tensor R^α_{βγδ} is a (1,3) tensor. Scalars — quantities with no free indices — are (0,0) tensors, invariant under coordinate changes.

The Einstein summation convention is the notational engine of tensor calculus: any index that appears once as an upper index and once as a lower index in the same term is summed over all coordinate values (0,1,2,3 in four dimensions). This contraction reduces the rank of a tensor by two. For example, contracting the Riemann tensor R^α_{βαδ} produces the Ricci tensor R_{βδ}, a (0,2) tensor. The metric tensor g_μν and its inverse g^{μν} (defined by g^{μα}g_{αν} = δ^μ_ν) raise and lower indices: V^μ = g^{μν}V_ν. This operation does not change the geometric object — it converts between the tangent-space representation and the cotangent-space representation — but it changes the component values in general.

A critical subtlety is that ordinary partial derivatives of tensor fields are not tensors (except for scalars). The partial derivative ∂_μ V^ν acquires a non-tensorial term under general coordinate transformations because the basis vectors themselves change from point to point in curved spacetime. The fix is the covariant derivative ∇_μ, which adds a correction term involving the Christoffel symbols (connection coefficients) that exactly cancels the non-tensorial piece. The covariant derivative of a tensor is again a tensor, which is why all derivative operations in GR are expressed using ∇_μ rather than ∂_μ. This machinery — index manipulation, metric raising/lowering, covariant differentiation — is the computational language in which all of general relativity is written.
