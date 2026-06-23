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
tags:
- lines
- planes
- vector-equations
stage: formal-systems
status: validated
---

# Equations of Lines and Planes in 3D

## Core Idea
A line in 3D can be written parametrically as r(t) = r₀ + tv, where r₀ is a point on the line and v is the direction vector. A plane through point (x₀, y₀, z₀) with normal vector n = ⟨a, b, c⟩ has equation a(x−x₀) + b(y−y₀) + c(z−z₀) = 0.

## Questions

```yaml
- question: "You know a plane contains the point (3, 0, -1) and has normal vector n = ⟨2, -1, 4⟩. Which is the correct plane equation?"
  type: multiple-choice
  options:
    - "2x − y + 4z = 0"
    - "2(x − 3) − (y − 0) + 4(z + 1) = 0"
    - "3x + 0y − z = 2"
    - "⟨2, -1, 4⟩ · ⟨x, y, z⟩ = ⟨3, 0, -1⟩"
  answer: 1
  explanation: "The plane equation comes from requiring that any vector from the base point to (x,y,z) be perpendicular to the normal n. That vector is ⟨x−3, y−0, z−(−1)⟩ = ⟨x−3, y, z+1⟩. Taking the dot product with n = ⟨2,−1,4⟩ and setting it to zero gives 2(x−3) − y + 4(z+1) = 0. The key insight: the normal vector's components ⟨2,−1,4⟩ are exactly the coefficients in the plane equation. Option A omits the base point entirely; option C treats the point's coordinates as the normal; option D mixes vectors and scalars incorrectly."

- question: "A line passes through the point (2, 5, 1) with direction vector ⟨1, 0, 0⟩. What is geometrically true about this line?"
  type: multiple-choice
  options:
    - "It lies in the plane z = 1 and is parallel to the x-axis, with y fixed at 5"
    - "It passes through the origin because the direction vector starts at (0,0,0)"
    - "It requires two equations to describe because it lives in three-dimensional space"
    - "It has slope 1 in the x-direction and slope 0 in the y and z directions"
  answer: 0
  explanation: "The parametric equations are x = 2 + t, y = 5 + 0·t = 5, z = 1 + 0·t = 1. Because y and z are constant, the line is parallel to the x-axis (only x changes), lies in the horizontal plane z = 1, and passes through y = 5 throughout. Option B is wrong: the direction vector gives the direction of travel, not a starting point at the origin. Option C is technically true (you could use two plane intersections) but misleads — parametric equations are the natural description. Option D misapplies the 2D concept of slope to 3D."

- question: "In 3D, a line can be fully described by a single linear equation in x, y, and z, analogous to y = mx + b in 2D."
  type: true-false
  answer: false
  explanation: "A single linear equation in x, y, z defines a plane in 3D — a two-dimensional surface — not a line. A line is a one-dimensional object in three-dimensional space; it requires more constraints. It can be described either by parametric equations (three scalar equations in a parameter t) or as the intersection of two planes (two simultaneous linear equations). The slope-intercept form y = mx + b has no direct 3D analogue because the concept of 'slope' is undefined for a 3D line."

- question: "The direction vector of the line where two planes intersect is parallel to the cross product of their normal vectors."
  type: true-false
  answer: true
  explanation: "If the two planes have normals n₁ and n₂, then the line of intersection must be perpendicular to both normals (since it lies in both planes). The cross product n₁ × n₂ produces exactly a vector perpendicular to both n₁ and n₂, which therefore lies along the intersection line. This makes computing the direction of a line of intersection straightforward: no need to solve the full system of equations just to get the direction."

- question: "Why can't the familiar equation y = mx + b be used to describe a line in 3D, and what two pieces of information are required instead?"
  type: short-answer
  answer: "In 3D, there is no single 'slope' — a line can travel in any combination of x, y, and z directions simultaneously, which cannot be captured by a single rate of change. The equation y = mx + b also implicitly fixes z, describing a line only in a 2D plane. Instead, a 3D line needs: (1) a point it passes through, given as a position vector r₀, and (2) a direction vector v indicating the direction of travel. These combine in the parametric form r(t) = r₀ + tv, which traces every point on the line as t varies over all reals."
  explanation: "The conceptual shift from 2D to 3D is from scalar slope to direction vector. In 2D, slope captures 'rise over run' because there is only one possible direction of variation. In 3D, a line travels in a direction that has x, y, and z components simultaneously — requiring a vector. The parametric form also makes it explicit that a line is a one-parameter family of points (indexed by t), which matches the geometric intuition of one-dimensionality inside three-dimensional space."
```

## Explainer

In 2D, a line is captured by y = mx + b — one equation relating x and y, encoding slope and intercept. In 3D, this approach breaks down: there is no single slope, and a line is a one-dimensional object inside three-dimensional space. The right framework uses vectors, which you already know as ordered triples encoding direction and magnitude.

A line in 3D is determined by two things: a **point it passes through** and a **direction it travels**. The **parametric equation** r(t) = r₀ + tv encodes both. Here r₀ = ⟨x₀, y₀, z₀⟩ is a position vector to a known point on the line, v = ⟨a, b, c⟩ is the **direction vector**, and t is a real-valued parameter. As t ranges over all reals, r(t) traces every point on the line. At t = 0 you're at r₀; at t = 1 you've moved one full step of v; at t = −1 you've moved backward. Reading off scalar equations: x = x₀ + at, y = y₀ + bt, z = z₀ + ct. These are the parametric equations of the line, each coordinate evolving linearly in t.

A **plane** is determined by a point and a **normal vector** n = ⟨a, b, c⟩ — a vector perpendicular to every vector lying in the plane. Any vector from the base point (x₀, y₀, z₀) to a general point (x, y, z) in the plane is ⟨x − x₀, y − y₀, z − z₀⟩, and it must be perpendicular to n. Perpendicularity means zero dot product: n · ⟨x − x₀, y − y₀, z − z₀⟩ = 0. Expanding gives the plane equation a(x − x₀) + b(y − y₀) + c(z − z₀) = 0. The coefficients ⟨a, b, c⟩ in the plane equation are exactly the components of the normal vector — the plane's orientation is encoded in n.

Lines and planes interact in structured ways. Two planes with normal vectors n₁ and n₂ intersect in a line whose **direction vector is n₁ × n₂** — the cross product, which you'll meet soon. To find where a parametric line r(t) = r₀ + tv pierces a plane, substitute the parametric equations into the plane equation and solve for t; that value of t gives the intersection point. These relationships form the geometric foundation for tangent planes and surface geometry later in multivariable calculus, where a surface near a point is approximated by a plane — and the normal to that plane determines the geometry of the surface.
