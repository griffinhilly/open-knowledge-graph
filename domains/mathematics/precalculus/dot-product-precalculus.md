---
id: dot-product-precalculus
title: Dot Product
domain: mathematics
course: precalculus
prerequisites:
  - id: vector-operations
    type: hard
  - id: law-of-cosines
    type: soft
builds-toward:
  - work-as-integral
tags: [vectors, dot-product, orthogonality]
stage: formal-systems
status: validated
---

# Dot Product

## Core Idea
The dot product of two vectors u = (u1, u2) and v = (v1, v2) is u * v = u1*v1 + u2*v2, a scalar (not a vector). Geometrically, u * v = |u| |v| cos(theta), where theta is the angle between them. The dot product measures how much two vectors point in the same direction. It is zero when vectors are perpendicular (orthogonal), positive when they point similarly, and negative when they point oppositely.

## How It's Best Learned
Compute dot products algebraically, then verify with the geometric formula. Use the dot product to find angles between vectors, check orthogonality, and compute projections. Connect to work in physics (W = F * d) and to the Law of Cosines.

## Common Misconceptions
- Expecting the dot product to produce a vector (it produces a scalar).
- Forgetting that the geometric formula requires the angle between the vectors, not a reference angle.
- Confusing dot product with cross product (which exists in 3D and produces a vector).

## Explainer

From vector operations, you know how to add vectors and scale them, but those operations always return another vector. The **dot product** does something different: it takes two vectors and returns a single number. That number encodes something geometrically meaningful — how much the two vectors "agree" in direction.

The algebraic definition is straightforward: for u = (u₁, u₂) and v = (v₁, v₂), the dot product is u · v = u₁v₁ + u₂v₂. Multiply corresponding components, then add. For example, (3, 4) · (1, 2) = 3·1 + 4·2 = 3 + 8 = 11. This formula extends naturally to any number of dimensions: just multiply matching components and sum. The result is always a scalar — a plain number with no direction.

The geometric formula u · v = |u| |v| cos θ reveals what that scalar measures. Here θ is the angle between the vectors. When the vectors point in the same direction, θ = 0 and cos θ = 1, giving the maximum possible dot product. When they are **perpendicular** (θ = 90°), cos θ = 0 and the dot product is exactly zero — this is the test for **orthogonality**. When they point in opposite directions, θ = 180° and the dot product is negative. The dot product's sign alone tells you whether two vectors point toward the same half-space (positive), are perpendicular (zero), or oppose each other (negative).

You can connect this to the Law of Cosines you may have seen. The law of cosines says c² = a² + b² − 2ab cos θ for a triangle with sides a, b, c. If you set up the triangle with two sides as vectors u and v, then c = u − v, and expanding |u − v|² = |u|² − 2(u · v) + |v|² recovers the law of cosines exactly — with u · v playing the role of ab cos θ. This is more than a coincidence; it shows that the dot product is the algebraic encoding of angle, connecting the abstract component formula to the familiar geometry of triangles. This connection becomes the foundation for projection — decomposing one vector along the direction of another — which you will use extensively in calculus and linear algebra.
