---
id: equations-lines-planes-3d
title: Equations of Lines and Planes in 3D
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-3d-coordinate-system
  type: hard
builds-toward:
- tangent-planes
- surface-parametrization
tags:
- lines
- planes
- vector-equations
stage: formal-systems
status: draft
---

# Equations of Lines and Planes in 3D

## Core Idea
A line in 3D can be written parametrically as r(t) = r₀ + tv, where r₀ is a point on the line and v is the direction vector. A plane through point (x₀, y₀, z₀) with normal vector n = ⟨a, b, c⟩ has equation a(x−x₀) + b(y−y₀) + c(z−z₀) = 0.

## Explainer

In 2D, a line is captured by y = mx + b — one equation relating x and y, encoding slope and intercept. In 3D, this approach breaks down: there is no single slope, and a line is a one-dimensional object inside three-dimensional space. The right framework uses vectors, which you already know as ordered triples encoding direction and magnitude.

A line in 3D is determined by two things: a **point it passes through** and a **direction it travels**. The **parametric equation** r(t) = r₀ + tv encodes both. Here r₀ = ⟨x₀, y₀, z₀⟩ is a position vector to a known point on the line, v = ⟨a, b, c⟩ is the **direction vector**, and t is a real-valued parameter. As t ranges over all reals, r(t) traces every point on the line. At t = 0 you're at r₀; at t = 1 you've moved one full step of v; at t = −1 you've moved backward. Reading off scalar equations: x = x₀ + at, y = y₀ + bt, z = z₀ + ct. These are the parametric equations of the line, each coordinate evolving linearly in t.

A **plane** is determined by a point and a **normal vector** n = ⟨a, b, c⟩ — a vector perpendicular to every vector lying in the plane. Any vector from the base point (x₀, y₀, z₀) to a general point (x, y, z) in the plane is ⟨x − x₀, y − y₀, z − z₀⟩, and it must be perpendicular to n. Perpendicularity means zero dot product: n · ⟨x − x₀, y − y₀, z − z₀⟩ = 0. Expanding gives the plane equation a(x − x₀) + b(y − y₀) + c(z − z₀) = 0. The coefficients ⟨a, b, c⟩ in the plane equation are exactly the components of the normal vector — the plane's orientation is encoded in n.

Lines and planes interact in structured ways. Two planes with normal vectors n₁ and n₂ intersect in a line whose **direction vector is n₁ × n₂** — the cross product, which you'll meet soon. To find where a parametric line r(t) = r₀ + tv pierces a plane, substitute the parametric equations into the plane equation and solve for t; that value of t gives the intersection point. These relationships form the geometric foundation for tangent planes and surface geometry later in multivariable calculus, where a surface near a point is approximated by a plane — and the normal to that plane determines the geometry of the surface.
