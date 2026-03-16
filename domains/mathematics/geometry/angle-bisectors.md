---
id: angle-bisectors
title: Angle Bisectors
domain: mathematics
course: geometry
prerequisites:
  - id: angle-basics-and-classification
    type: hard
  - id: segment-and-distance
    type: hard
builds-toward:
  - coordinate-geometry-proofs
tags: [bisectors, angles, incenter, equidistance]
stage: abstract-reasoning
status: validated
---

# Angle Bisectors

## Core Idea
An angle bisector is a ray that divides an angle into two congruent angles. The Angle Bisector Theorem states that any point on the bisector of an angle is equidistant from the two sides of the angle. The three angle bisectors of a triangle are concurrent at the incenter, which is equidistant from all three sides and is the center of the inscribed circle (incircle).

## How It's Best Learned
Construct angle bisectors with compass and straightedge. Verify equidistance from the sides using perpendicular distances. Prove the theorem with congruent triangles. Explore the incenter by bisecting all three angles of a triangle and observing they meet at one point. Connect to the inscribed circle.

## Common Misconceptions
- Confusing angle bisectors with perpendicular bisectors.
- Measuring distance from a point to a side incorrectly (distance must be perpendicular).
- Thinking the incenter can be outside the triangle (it is always inside for any triangle).

## Explainer

You already know how to classify and measure angles, and how to measure the distance between two points. An **angle bisector** adds a new construction: a ray that slices an angle exactly in half, creating two congruent angles. If angle ABC measures 80°, the bisector of angle ABC is a ray from B that makes two 40° angles with BA and BC. Constructing one with a compass and straightedge — the classical method — involves drawing arcs that locate the points equidistant from both sides, then connecting them to the vertex.

The core theorem is that any point lying on the angle bisector is **equidistant from the two sides** of the angle, where distance is measured perpendicularly. Think of it this way: imagine standing at the corner of a room where two walls meet. If you walk along the exact center line — the angle bisector — you stay equally far from both walls at every step. Move off that line toward one wall, and you get closer to it and farther from the other. This equidistance property is proved using congruent right triangles: drop perpendiculars from a point on the bisector to each side, and the resulting triangles are congruent by AAS.

In a triangle, you have three angles, so you can draw three angle bisectors — one from each vertex. A remarkable fact is that all three meet at a single point, called the **incenter**. This is one of the four classical triangle centers. Because the incenter lies on all three bisectors simultaneously, it is equidistant from all three sides of the triangle. That common distance is the **inradius**, and the circle centered at the incenter with that radius is the **inscribed circle** (or incircle) — the largest circle that fits entirely inside the triangle, touching each side at exactly one point.

The incenter always lies inside the triangle, regardless of whether the triangle is acute, right, or obtuse. This distinguishes it from the circumcenter (which can fall outside for obtuse triangles). A useful mnemonic: the incenter is the center of the *in*scribed circle; you find it by bisecting the *in*terior angles. When you encounter problems involving circles tangent to all three sides of a triangle, or distances from an interior point to the sides, the incenter and angle bisectors are the right tools.
