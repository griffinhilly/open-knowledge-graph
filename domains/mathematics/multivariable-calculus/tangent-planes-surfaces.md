---
id: tangent-planes-surfaces
title: Tangent Planes to Surfaces
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector-definition
  type: hard
- id: tangent-planes-linear-approximation
  type: hard
builds-toward:
- surface-parametrization
tags:
- tangent-planes
- surfaces
- normal-vector
stage: formal-systems
status: draft
---

# Tangent Planes to Surfaces

## Core Idea
For a surface z = f(x, y), the tangent plane at (x₀, y₀, z₀) has equation z − z₀ = f_x(x₀, y₀)(x − x₀) + f_y(x₀, y₀)(y − y₀). The normal vector is n = ⟨f_x, f_y, −1⟩, and ∇f lies in the plane.

## Explainer

In single-variable calculus, the tangent line at a point (x₀, y₀) on the curve y = f(x) has equation y − y₀ = f'(x₀)(x − x₀). It is the best linear approximation to f near x₀. The **tangent plane** for a surface z = f(x, y) is the direct 3D extension: a flat plane that best approximates the surface near the point (x₀, y₀, z₀). Instead of one derivative, there are two — f_x and f_y, the partial derivatives you know from the gradient — and the plane accounts for the slope in each independent direction.

The tangent plane equation z − z₀ = f_x(x₀, y₀)(x − x₀) + f_y(x₀, y₀)(y − y₀) can be read as: "the change in z is approximately the x-slope times the change in x, plus the y-slope times the change in y." Hold y fixed (set y = y₀) and the equation becomes z − z₀ = f_x(x − x₀), which is exactly the tangent line in the xz-plane. Hold x fixed and you recover the tangent line in the yz-plane. The tangent plane combines both tangent lines simultaneously — it is the unique plane containing both.

The **gradient** ∇f = ⟨f_x, f_y⟩ encodes both partial derivatives but lives in the xy-plane, not in 3D. The **normal vector** to the tangent plane is n = ⟨f_x, f_y, −1⟩. To see why: rewrite the tangent plane as f_x(x − x₀) + f_y(y − y₀) − (z − z₀) = 0, which is the equation n · ⟨x − x₀, y − y₀, z − z₀⟩ = 0 — the standard form of a plane with normal n. The third component is −1 because z appears with coefficient −1 when you move it to the left side. This is why the statement "∇f lies in the plane" is true: the 2D gradient vector is not the 3D normal; the normal has an additional z-component.

For a surface given **implicitly** as F(x, y, z) = c (rather than explicitly as z = f(x,y)), the 3D gradient ∇F = ⟨F_x, F_y, F_z⟩ is the normal vector to the surface. This is the more general form: since F is constant on the surface, any tangent direction v must satisfy ∇F · v = 0, making ∇F normal to every tangent direction. The explicit case z = f(x,y) is a special case: define F(x,y,z) = f(x,y) − z, so ∇F = ⟨f_x, f_y, −1⟩, recovering the normal vector from the Core Idea. This unification — the gradient of an implicit equation is always the normal to the corresponding surface — is one of the most reusable ideas in multivariable calculus.
