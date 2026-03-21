---
id: equations-lines-planes
title: Equations of Lines and Planes in 3D
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-in-3d
  type: hard
- id: dot-cross-products-geometry
  type: hard
builds-toward:
- tangent-planes-linear-approximation
- level-sets-surfaces
tags:
- lines
- planes
- parametric-equations
- normal-vectors
stage: formal-systems
status: draft
---

# Equations of Lines and Planes in 3D

## Core Idea
A line in 3D is parametrized as r(t) = r₀ + td (position plus scalar multiple of direction vector). A plane with normal vector n = ⟨a, b, c⟩ passing through (x₀, y₀, z₀) has equation a(x−x₀) + b(y−y₀) + c(z−z₀) = 0.

## Questions

```yaml
- question: "Consider two planes: 2x + 3y − z = 5 and 4x + 6y − 2z = 11. What is their geometric relationship?"
  type: multiple-choice
  options:
    - "They intersect in a line, since two planes generically intersect"
    - "They are the same plane"
    - "They are parallel but distinct"
    - "They are perpendicular, since one equation is a multiple of the other"
  answer: 2
  explanation: "The normal vector of the first plane is ⟨2, 3, −1⟩; the normal of the second is ⟨4, 6, −2⟩ = 2⟨2, 3, −1⟩ — they are proportional, so the planes are parallel. But 5 ≠ 2·(11/2) when checked: the second equation 4x + 6y − 2z = 11 is not simply twice the first (which would give 2·5 = 10 ≠ 11), so the planes are distinct. Parallel normals mean parallel planes; the different constants confirm they don't coincide. The tempting wrong answer is 'they intersect' — two generic planes do intersect, but only when their normals are not proportional."

- question: "What is the direction vector of the line of intersection of planes x + 2y + 3z = 4 and 2x − y + z = 5?"
  type: multiple-choice
  options:
    - "⟨1, 2, 3⟩ + ⟨2, −1, 1⟩ = ⟨3, 1, 4⟩ (sum of normal vectors)"
    - "⟨1, 2, 3⟩ · ⟨2, −1, 1⟩ (dot product of normal vectors)"
    - "⟨1, 2, 3⟩ × ⟨2, −1, 1⟩ = ⟨5, 5, −5⟩ (cross product of normal vectors)"
    - "Any vector parallel to both planes, found by inspection"
  answer: 2
  explanation: "The line of intersection lies in both planes simultaneously, so it must be perpendicular to both normal vectors. The cross product of two vectors produces a vector perpendicular to both — so **n₁** × **n₂** gives the direction of the intersection line. In this case: ⟨1, 2, 3⟩ × ⟨2, −1, 1⟩ = ⟨(2)(1)−(3)(−1), (3)(2)−(1)(1), (1)(−1)−(2)(2)⟩ = ⟨5, 5, −5⟩. The dot product gives a scalar, not a vector; the sum of normals has no geometric meaning for this purpose."

- question: "In the plane equation ax + by + cz = d, the coefficients a, b, c are the components of a normal vector to the plane."
  type: true-false
  answer: true
  explanation: "This follows directly from how the equation is derived. Given normal **n** = ⟨a, b, c⟩ and a point (x₀, y₀, z₀), any other point (x, y, z) in the plane satisfies **n** · ((x, y, z) − (x₀, y₀, z₀)) = 0, which expands to ax + by + cz = ax₀ + by₀ + cz₀ = d. The normal vector components appear directly as the coefficients — reading off the normal from a plane equation is immediate."

- question: "In 3D, a line can be fully described by specifying a slope and a point on the line, just as in 2D."
  type: true-false
  answer: false
  explanation: "Slope is a single number describing steepness relative to a reference direction, and it only works in 2D where there is one relevant reference axis. In 3D, a line can tilt in two independent directions (toward x and toward y), so a single scalar slope cannot capture the full direction. Instead, a 3D line requires a direction vector ⟨a, b, c⟩ — three components — and a point. The parametric form r(t) = r₀ + t**d** replaces the slope-intercept form entirely in 3D."

- question: "Why does describing a plane in 3D require a normal vector rather than a direction vector, and how do you find the normal vector when you know two vectors lying in the plane?"
  type: short-answer
  answer: "A plane has infinitely many directions within it, so no single direction vector characterizes it uniquely. What uniquely specifies a plane's orientation is a vector perpendicular to all directions in it — the normal vector. If two vectors **u** and **v** lie in the plane, their cross product **n** = **u** × **v** is perpendicular to both and therefore to the entire plane. The normal vector then determines the plane equation directly: its components become the coefficients a, b, c."
  explanation: "The contrast with lines is instructive: a line has a unique direction (up to scaling), so a direction vector captures it. A plane has a unique *orientation* but not a unique direction — the perpendicular to that orientation is what captures it. The cross product is the natural tool because it is defined as 'perpendicular to both inputs,' which is exactly what finding a normal requires."
```

## Explainer

In 2D, a line is fully described by a slope and a point — but in 3D, there is no single "slope." Instead, the natural description of a line uses the idea from your study of vectors: start at a known point and walk in a fixed direction. The **parametric equation** of a line is r(t) = r₀ + t**d**, where r₀ is the position vector of a point on the line and **d** is the direction vector. As t ranges over all real numbers, r(t) traces out the entire line. The parameter t plays the role of a signed distance along the line. In component form: x = x₀ + at, y = y₀ + bt, z = z₀ + ct, where ⟨a, b, c⟩ = **d**. Two parallel lines have proportional direction vectors; two intersecting lines share a point for some pair of t values.

A plane in 3D is characterized not by a direction of travel but by a **normal vector** — a vector perpendicular to every vector lying in the plane. This is where the cross product becomes essential: if you know two vectors **u** and **v** that lie in the plane, then **n** = **u** × **v** is normal to both and hence to the plane. Given a normal vector **n** = ⟨a, b, c⟩ and a point (x₀, y₀, z₀) in the plane, any other point (x, y, z) in the plane satisfies: the vector from (x₀, y₀, z₀) to (x, y, z) must be perpendicular to **n**. Writing this dot product condition gives the **point-normal form**: a(x−x₀) + b(y−y₀) + c(z−z₀) = 0, which expands to ax + by + cz = d for some constant d. The coefficients of x, y, z in the plane equation are precisely the components of the normal vector.

The dot product plays a structural role throughout. The **distance from a point P to a plane** is computed by projecting the vector from any plane point to P onto the unit normal — it's |(P − P₀) · **n̂**|. Two planes are parallel if their normals are parallel (proportional), perpendicular if their normals are orthogonal (dot product zero), and intersect in a line otherwise. The line of intersection of two planes is found by solving the two plane equations simultaneously, and its direction vector is the cross product of the two normals — perpendicular to both.

These representations feed directly into the tangent plane problems ahead. When you compute the tangent plane to a surface z = f(x, y) at a point, you are finding the plane that best approximates the surface — and its normal vector will come from the partial derivatives. The parametric line equation appears in optimization (moving along a line to find minima) and in computing intersections needed for integration. Mastering the point-normal form and the parametric line form, and the geometric role of dot and cross products in deriving them, provides the foundation for nearly every 3D calculation in multivariable calculus.
