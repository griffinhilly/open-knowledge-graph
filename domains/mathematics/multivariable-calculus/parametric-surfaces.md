---
id: parametric-surfaces
title: Parametric Surfaces
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions
  type: hard
- id: partial-derivatives
  type: hard
- id: cross-product
  type: hard
- id: tangent-planes-surfaces
  type: soft
- id: space-curves
  type: soft
builds-toward:
- surface-integrals-scalar
- flux-integrals
tags:
- parametric-surface
- normal-vector
- surface
- tangent-plane
stage: formal-systems
status: validated
---
# Parametric Surfaces

## Core Idea
A parametric surface is described by a vector function r(u, v) = ⟨x(u,v), y(u,v), z(u,v)⟩ mapping a 2D parameter domain to a surface in ℝ³. The partial derivatives r_u and r_v are tangent vectors to the surface, and their cross product r_u × r_v gives a normal vector to the surface. The magnitude |r_u × r_v| is the surface area element dS for surface integrals. Parametric surfaces generalize from explicit surfaces z = f(x,y) to surfaces that may loop back or cannot be expressed as functions.

## How It's Best Learned
Practice parametrizing familiar surfaces: sphere (using spherical angles), cylinder (using angle and height), and the graph z = f(x,y) (using x and y directly). For each, compute r_u × r_v and verify that it points outward (or inward). Emphasize that the parametrization is not unique — the same surface has infinitely many valid parametrizations.

## Common Misconceptions
- The normal vector r_u × r_v is not generally a unit vector; its magnitude |r_u × r_v| is the area scaling factor.
- If r_u × r_v = 0 at a point, the surface has a singularity at that parameter value (e.g., the north pole of a sphere in standard parametrization).
- The orientation of the normal (inward vs outward) depends on the order of r_u × r_v vs r_v × r_u.

## Questions

```yaml
- question: "You compute r_u × r_v for a parametric surface and get a nonzero vector. You want to use it as the surface normal in a flux integral. What is wrong with using this vector directly without modification?"
  type: multiple-choice
  options:
    - "Nothing — r_u × r_v is already a unit normal vector suitable for any calculation"
    - "It points inward; you must always reverse it to point outward"
    - "Its magnitude is not 1; it encodes area scaling and must not be normalized before multiplying by dA"
    - "It only gives the normal at the origin, not at arbitrary surface points"
  answer: 2
  explanation: "r_u × r_v is not generally a unit vector — its magnitude |r_u × r_v| is the area scaling factor that converts parameter-space area du dv into actual surface area. In a surface integral, dS = |r_u × r_v| du dv: you keep the full vector (or its magnitude) precisely because it carries this geometric information. Normalizing it to a unit vector and then multiplying by du dv would give the wrong element of surface area."

- question: "A surface is parametrized with r(u, v). You accidentally compute r_v × r_u instead of r_u × r_v. What is the effect on the resulting normal vector?"
  type: multiple-choice
  options:
    - "The normal vector is unchanged — cross product is commutative for perpendicular vectors"
    - "The magnitude changes but the direction stays the same"
    - "The direction reverses (inward vs outward flip) but the magnitude is the same"
    - "The result is no longer perpendicular to the surface"
  answer: 2
  explanation: "The cross product is anti-commutative: r_v × r_u = −(r_u × r_v). The magnitude |r_v × r_u| = |r_u × r_v| is unchanged (so the area element dS is unaffected), but the direction flips. This means swapping the order reverses the orientation of the surface — what was the outward normal becomes the inward normal. For flux integrals, orientation matters: reversing the normal negates the integral."

- question: "For the parametrization r(x, y) = ⟨x, y, f(x,y)⟩ of a graph surface, the surface area element dS equals √(f_x² + f_y² + 1) dx dy."
  type: true-false
  answer: true
  explanation: "For this parametrization, r_x = ⟨1, 0, f_x⟩ and r_y = ⟨0, 1, f_y⟩. Their cross product is r_x × r_y = ⟨−f_x, −f_y, 1⟩, and its magnitude is √(f_x² + f_y² + 1). So dS = |r_x × r_y| dx dy = √(f_x² + f_y² + 1) dx dy. This is exactly the graph surface area formula, confirming that the parametric framework recovers it as a special case."

- question: "At a point where r_u × r_v = 0, the parametric surface has a well-defined tangent plane with a degenerate (zero-length) normal."
  type: true-false
  answer: false
  explanation: "When r_u × r_v = 0, the two tangent vectors r_u and r_v are parallel (or one is zero), meaning they do not span a plane. The surface has a singularity at that parameter value — a point where the geometry breaks down and a tangent plane is not defined. A common example is the north pole of a sphere in standard spherical coordinates, where the parameter lines all collapse to a single point. The cross product being zero signals a failure of the parametrization, not just a degenerate normal."

- question: "Explain why the magnitude |r_u × r_v| must appear in a surface integral, rather than simply integrating over the parameter domain with area element du dv."
  type: short-answer
  answer: "A small rectangle in the parameter domain with sides du and dv maps to a small parallelogram on the surface with sides r_u du and r_v dv. The area of a parallelogram equals the magnitude of the cross product of its edge vectors, so the actual surface area element is |r_u × r_v| du dv, not du dv. Without this factor, you would be integrating over parameter area, not surface area — the two differ whenever the surface stretches or compresses the parameter domain, which is almost always."
  explanation: "This is the surface-integral analogue of the Jacobian in change-of-variables for double integrals (where r dr dθ replaces dx dy in polar coordinates). The parameter domain and the surface are different geometric objects; |r_u × r_v| is the local distortion factor that converts between them. Omitting it produces integrals that depend on the choice of parametrization rather than on the intrinsic geometry of the surface."
```

## Explainer

You already know how a **vector-valued function** r(t) traces a curve by mapping a one-dimensional parameter t to points in ℝ³. A **parametric surface** extends this idea to two parameters: r(u, v) = ⟨x(u,v), y(u,v), z(u,v)⟩ maps a region in the (u, v) parameter plane to a surface in ℝ³. As u and v range over their domain, r sweeps out a two-dimensional sheet in space. This lets you describe surfaces — spheres, cylinders, tori, graphs — in a uniform framework, even when no single formula z = f(x, y) can describe them.

The derivatives from your prerequisite on **partial derivatives** now describe the surface's local geometry. The partial derivative r_u = ∂r/∂u is the tangent vector you get by moving along the surface in the u-direction (holding v fixed). Similarly, r_v is the tangent vector in the v-direction. At any smooth point of the surface, these two vectors span the **tangent plane** — the plane that best approximates the surface at that point. From your knowledge of the **cross product**, you know that r_u × r_v is perpendicular to both tangent vectors. This cross product is therefore a **normal vector** to the surface.

The magnitude |r_u × r_v| is the most important quantity for integration. Imagine a small rectangle in the parameter domain with dimensions du × dv. Its image on the surface is a small parallelogram with sides r_u du and r_v dv. The area of a parallelogram spanned by two vectors equals the magnitude of their cross product, so the area element on the surface is dS = |r_u × r_v| du dv. This is the surface analogue of the Jacobian factor r that appeared in polar coordinates: it converts parameter-space area into actual surface area. Every surface integral you will compute — for scalar quantities and for flux — uses this formula.

To use parametric surfaces in practice, you need to parametrize familiar shapes. A sphere of radius R uses spherical angles: r(φ, θ) = ⟨R sin φ cos θ, R sin φ sin θ, R cos φ⟩ for φ ∈ [0, π], θ ∈ [0, 2π). A cylinder of radius R and height h uses r(θ, z) = ⟨R cos θ, R sin θ, z⟩. A graph z = f(x, y) parametrizes trivially: r(x, y) = ⟨x, y, f(x, y)⟩, which gives r_x × r_y = ⟨−f_x, −f_y, 1⟩ and |r_x × r_y| = √(f_x² + f_y² + 1), recovering the surface area formula you may have seen earlier. The power of the parametric framework is that all three cases use the same r_u × r_v calculation, regardless of how different the surfaces look.
