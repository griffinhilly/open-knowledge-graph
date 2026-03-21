---
id: surface-parametrization-tangent
title: Parametric Surfaces and Tangent Vectors
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: change-of-variables-jacobian
  type: hard
builds-toward:
- surface-area-integrals
- surface-integrals-flux
tags:
- parametric-surfaces
- tangent-vectors
- normal-vectors
stage: formal-systems
status: draft
---

# Parametric Surfaces and Tangent Vectors

## Core Idea
A surface can be parametrized as r(u, v) = ⟨x(u, v), y(u, v), z(u, v)⟩. The tangent vectors r_u and r_v span the tangent plane. The normal vector n = r_u × r_v is perpendicular to the surface and has magnitude equal to the local area scaling factor.

## Questions

```yaml
- question: "For the cylinder r(u, v) = ⟨cos u, sin u, v⟩, the tangent vectors are r_u = ⟨−sin u, cos u, 0⟩ and r_v = ⟨0, 0, 1⟩, giving r_u × r_v = ⟨cos u, sin u, 0⟩ with magnitude 1. What does this magnitude of 1 represent geometrically?"
  type: multiple-choice
  options:
    - "The curvature of the cylinder surface at that point is 1"
    - "The local area scaling factor — a small rectangle of area du·dv in the parameter domain maps to a surface patch with the same area 1·du·dv"
    - "The angle between r_u and r_v is 1 radian"
    - "The speed at which the parametrization traces the surface as u and v increase simultaneously"
  answer: 1
  explanation: "The surface area element is dS = |r_u × r_v| du dv. When |r_u × r_v| = 1, a unit square in parameter space maps to a unit-area patch on the surface — the standard cylindrical parametrization is an isometry (area-preserving). For more complex surfaces such as a sphere, the magnitude varies with position: near the poles of a spherical parametrization |r_φ × r_θ| = sin φ, which shrinks to zero at the poles, correctly reflecting that the parameter grid compresses to a point there."

- question: "Why are r_u and r_v called 'tangent vectors' to the surface at a point r(u₀, v₀)?"
  type: multiple-choice
  options:
    - "They point in the direction of steepest ascent along the surface at that point"
    - "They are velocity vectors along the coordinate curves on the surface: holding v = v₀ and varying u traces a curve whose tangent vector is r_u = ∂r/∂u"
    - "They are always perpendicular to each other, forming a natural orthonormal frame"
    - "They equal the gradient of the height function at each point when the surface is expressed as z = g(x, y)"
  answer: 1
  explanation: "Holding v = v₀ fixed in r(u, v) traces a curve on the surface as u varies; the velocity of this curve is dr/du = r_u. Similarly, r_v is the velocity along the u = u₀ coordinate curves. These two vectors lie in the tangent plane and serve as its natural basis vectors — they are tangent to the two families of coordinate curves on the surface, just as the columns of a Jacobian span the tangent space for a coordinate change. They are generally not perpendicular unless the parametrization is orthogonal."

- question: "The cross product n = r_u × r_v is always perpendicular to the tangent plane of the surface at the corresponding point."
  type: true-false
  answer: true
  explanation: "The cross product of two vectors is perpendicular to both by definition. Since r_u and r_v lie in the tangent plane, their cross product is automatically perpendicular to the tangent plane — it is the surface normal. This is not a formula to memorize but a consequence of the cross product's geometric meaning. The normal's direction encodes orientation (which side of the surface faces outward), and its magnitude encodes local area scaling, making it the key quantity for all surface integral calculations."

- question: "For a surface parametrized as r(u, v), the surface area element is simply dS = du dv — the same as an area element in the flat parameter plane."
  type: true-false
  answer: false
  explanation: "The surface area element is dS = |r_u × r_v| du dv. The magnitude |r_u × r_v| accounts for how the parametrization stretches or compresses area as it maps from the flat parameter domain into 3D space. For a flat surface r(u, v) = ⟨u, v, 0⟩, we get |r_u × r_v| = 1, recovering dS = du dv as a special case. But for a curved surface this factor varies with position, and omitting it gives an incorrect answer for surface area — just as omitting the Jacobian gives incorrect answers in a change of variables for double integrals."

- question: "Explain why |r_u × r_v| — rather than, say, |r_u|·|r_v| — is the correct surface area scaling factor when setting up surface integrals."
  type: short-answer
  answer: "A small parameter rectangle [u, u+du] × [v, v+dv] maps to a parallelogram on the surface with edge vectors r_u·du and r_v·dv. The area of a parallelogram with edges **a** and **b** is |**a** × **b**|, which equals |**a**||**b**| sin θ where θ is the angle between them. Using |r_u|·|r_v| would assume θ = 90°, which is only correct when r_u and r_v are perpendicular (an orthogonal parametrization). The cross product magnitude correctly accounts for the angle between the tangent vectors and gives the true area of the surface patch regardless of parametrization."
  explanation: "This is the direct 3D generalization of the 2D Jacobian story. In 2D, a change of variables (u,v) → (x,y) scales area by |det J| = area of the parallelogram formed by the Jacobian columns. Here, the Jacobian is a 3×2 matrix with columns r_u and r_v, and the generalized 'determinant' is |r_u × r_v|, the magnitude of the cross product. It equals √(det(JᵀJ)), the Gram determinant, and captures the area distortion of the map from the parameter plane into 3D space."
```

## Explainer

From your work with the Jacobian, you know that changing variables in an integral introduces a scaling factor that accounts for how the coordinate transformation stretches or compresses area. **Parametric surfaces** use the same idea to describe curved surfaces in R³: you have a flat parameter domain (a region in the uv-plane) and a function r(u, v) = ⟨x(u, v), y(u, v), z(u, v)⟩ that maps it to a surface in R³. Just as parametric curves trace paths in space as a single parameter moves, parametric surfaces fill out two-dimensional sheets as two parameters move simultaneously. For example, a sphere of radius 1 is parametrized by r(φ, θ) = ⟨sin φ cos θ, sin φ sin θ, cos φ⟩ for φ ∈ [0, π] and θ ∈ [0, 2π].

The **tangent vectors** r_u and r_v arise as partial derivatives of r with respect to each parameter. Holding v constant and varying u traces a curve on the surface; its velocity vector at any point is r_u = ⟨∂x/∂u, ∂y/∂u, ∂z/∂u⟩. Similarly, r_v is tangent to the u = constant curves. These two vectors lie in the **tangent plane** of the surface at the corresponding point — they are the tangent plane's natural basis vectors at that point, playing the same role that the columns of the Jacobian play for planar coordinate changes. Together they span the tangent plane, provided they are not parallel (i.e., they are linearly independent, which is the condition that r is a regular parametrization).

The **normal vector** n = r_u × r_v is constructed via the cross product, which automatically produces a vector perpendicular to both r_u and r_v — hence perpendicular to the tangent plane and therefore normal to the surface. Its direction points "outward" (or "inward," depending on orientation), and its magnitude |r_u × r_v| measures the local area scaling factor: a small rectangle du × dv in the parameter domain maps to a parallelogram on the surface with area |r_u × r_v| du dv. This is exactly the surface-area element dS = |r_u × r_v| du dv, the key piece in computing surface area integrals.

The connection to the Jacobian is direct. For a surface z = g(x, y) over a region in the xy-plane, you can parametrize with r(x, y) = ⟨x, y, g(x, y)⟩. Then r_x = ⟨1, 0, gₓ⟩ and r_y = ⟨0, 1, g_y⟩, and their cross product has magnitude √(gₓ² + g_y² + 1), recovering the classical surface area formula. For a general parametrization, the Jacobian of the map (u, v) ↦ (x, y, z) is the 3 × 2 matrix with columns r_u and r_v, and |r_u × r_v| is the "generalized Jacobian determinant" (the magnitude of the unique vector whose square equals the Gram determinant det(JᵀJ)). Everything downstream — surface area integrals, flux integrals, Stokes' theorem — builds on this local geometry of r_u, r_v, and their cross product.
