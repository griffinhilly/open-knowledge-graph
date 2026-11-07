---
id: vectors-in-3d
title: 'Vectors in 3D Space: Operations and Magnitude'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: 3d-coordinate-systems
  type: hard
- id: distance-and-distance-formula-3d
  type: hard
builds-toward:
- dot-cross-products-geometry
- vector-fields
- equations-lines-planes
tags:
- vectors
- 3d-geometry
- magnitude
stage: formal-systems
status: validated
---

# Vectors in 3D Space: Operations and Magnitude

## Core Idea
A 3D vector ⟨a, b, c⟩ has magnitude √(a² + b² + c²) and can be added, subtracted, and scalar-multiplied component-wise. Vectors represent displacement, force, velocity, and other directional quantities in 3D space.

## How It's Best Learned
Start from two points, P = (1, 2, 3) and Q = (3, −1, 9). Form the vector from P to Q as Q − P = ⟨2, −3, 6⟩. Find its length in two Pythagorean steps: √(4 + 9) = √13 across the floor, then √(13 + 36) = 7. Divide by 7 to get a unit vector, then sketch tip-to-tail sums in a box drawing.

## Common Misconceptions
- A vector has to start at the origin, so ⟨a, b, c⟩ and the point (a, b, c) are the same thing. (A vector is a displacement that can be drawn from any starting point. Drawn from the origin, ⟨a, b, c⟩ ends at the point (a, b, c).)
- The vector from P to Q is P − Q. (It is Q − P, the end point minus the starting point. P − Q has the same length but points the opposite way.)
- The length of a sum is the sum of the lengths, |u + v| = |u| + |v|. (That holds only when u and v point the same way or one is zero. For ⟨1, 0, 0⟩ + ⟨0, 1, 0⟩ the length is √2, not 2.)

## Questions

```yaml
- question: "What is the magnitude of the vector ⟨-3, 0, 4⟩?"
  type: multiple-choice
  options: ["7", "5", "-5", "1"]
  answer: 1
  explanation: "Magnitude = √((-3)² + 0² + 4²) = √(9 + 0 + 16) = √25 = 5. The negative sign on the component is eliminated by squaring — magnitude is always non-negative. A common error is adding the components directly (−3 + 0 + 4 = 1) instead of squaring them."

- question: "Multiplying a vector by a negative scalar reverses its direction while keeping its magnitude unchanged."
  type: true-false
  answer: false
  explanation: "Only multiplication by −1 preserves magnitude while reversing direction. Multiplying by any other negative scalar −k both reverses the direction and scales the magnitude by |k|. For example, −3 × ⟨1, 0, 0⟩ = ⟨−3, 0, 0⟩, which has magnitude 3, not 1."

- question: "Why is 3D vector addition computed component-wise rather than some other way?"
  type: short-answer
  answer: "Because the three coordinate axes are mutually perpendicular (orthogonal), displacement along each axis is independent. Adding component-wise accumulates displacement along each independent direction separately, which corresponds geometrically to the tip-to-tail rule."
  explanation: "When two axes are orthogonal, motion along one does not affect position along the other. So total x-displacement, y-displacement, and z-displacement each add independently — exactly what component-wise addition computes. Geometrically, this is equivalent to placing vectors end-to-end and measuring the resultant displacement."
```

## Explainer

When you learned 3D coordinate systems, you located points in space as ordered triples (x, y, z). Vectors in 3D extend this to describe *displacement* — how far and in which direction to move. Writing ⟨a, b, c⟩ means "move a units along x, b units along y, c units along z." The distinction between a point and a vector is subtle but important: a point is a location; a vector is a displacement that can originate anywhere.

The magnitude of a vector is its length — the actual distance of the displacement. Because the three axes are mutually perpendicular, you apply the Pythagorean theorem twice: first combine the x and y components into a horizontal distance √(a² + b²), then combine that with the z component to get the full 3D magnitude √(a² + b² + c²). This is a direct extension of the 2D distance formula, and the squaring step ensures the result is always non-negative regardless of the signs of the components.

Vector addition is computed component-wise because the axes are independent — what happens along x has no effect on y or z. If you walk 3 meters east and your friend walks 4 meters east, together you have covered 7 meters east; the east-direction displacements simply add. The same logic applies to each axis separately. Geometrically, this corresponds to the tip-to-tail rule: place the tail of the second vector at the tip of the first, and the vector from the original tail to the final tip is the sum.

Scalar multiplication stretches or shrinks a vector: k × ⟨a, b, c⟩ = ⟨ka, kb, kc⟩. For positive k, the direction is unchanged and the magnitude scales by k. For negative k, the direction reverses and the magnitude scales by |k|. These two operations — vector addition and scalar multiplication — are the building blocks for the entire space of linear algebra and multivariable calculus: dot products, cross products, projections, and gradient vectors all rest on this foundation.
