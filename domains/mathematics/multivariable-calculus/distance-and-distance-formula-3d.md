---
id: distance-and-distance-formula-3d
title: Distance Formula and Metric in 3D Space
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: 3d-coordinate-systems
  type: hard
- id: pythagorean-theorem
  type: hard
builds-toward:
- vectors-in-3d
tags:
- distance
- metric
- 3d-space
stage: formal-systems
status: validated
---

# Distance Formula and Metric in 3D Space

## Core Idea
The distance between two points in 3D space (x₁, y₁, z₁) and (x₂, y₂, z₂) is √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²]. This formula extends the 2D distance formula by including the z-component and defines the Euclidean metric in ℝ³.

## Questions

```yaml
- question: "What is the distance between the points (1, 2, 3) and (4, 6, 3)?"
  type: multiple-choice
  options:
    - "5, since √[(4−1)² + (6−2)² + (3−3)²] = √25"
    - "√7, since √(3 + 4 + 0)"
    - "√34, since √(9 + 16 + 9)"
    - "7, since (4−1) + (6−2) + (3−3)"
  answer: 0
  explanation: "Distance = √[(4−1)² + (6−2)² + (3−3)²] = √[9 + 16 + 0] = √25 = 5. Since the z-coordinates are equal, the z-term contributes zero and this reduces to the 2D distance in the xy-plane. Option C incorrectly uses (3−3)² = 9 instead of 0; option B adds differences without squaring; option D omits the square root entirely."

- question: "Which equation describes all points (x, y, z) at distance 3 from the point (1, 2, 4)?"
  type: multiple-choice
  options:
    - "(x−1) + (y−2) + (z−4) = 3"
    - "(x−1)² + (y−2)² + (z−4)² = 9"
    - "√[(x−1)² + (y−2)² + (z−4)²] = 9"
    - "(x+1)² + (y+2)² + (z+4)² = 3"
  answer: 1
  explanation: "Set the distance formula equal to r = 3 and square both sides: (x−1)² + (y−2)² + (z−4)² = 9. This is the equation of a sphere of radius 3 centered at (1, 2, 4). Option C has 9 under the root instead of 3 (the formula would give distance = √9 = 3, but it's written inconsistently); option D has the wrong signs on the center coordinates and the wrong exponent on r; option A omits squaring the differences."

- question: "The 3D distance formula is derived from a single application of the Pythagorean theorem, extended to accommodate a third coordinate."
  type: true-false
  answer: false
  explanation: "Two applications are required. First, compute the horizontal distance in the xy-plane: d_xy = √[(x₂−x₁)² + (y₂−y₁)²]. Then treat d_xy and |z₂−z₁| as legs of a new right triangle and apply Pythagoras again: distance = √[d_xy² + (z₂−z₁)²] = √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²]. This two-step structure is why the formula works: the three axes are mutually perpendicular, so each coordinate difference contributes independently."

- question: "The Euclidean distance between two points gives the length of the shortest possible path between them through 3D space."
  type: true-false
  answer: true
  explanation: "In Euclidean space, the straight-line segment is always the shortest path between two points — this follows from the triangle inequality, which the Euclidean metric satisfies. The formula gives exactly this straight-line length. It is a geometric property of space itself, not a navigational calculation. This is why 'Euclidean metric' is the standard meaning of 'distance' in 3D space, and why it generalizes naturally to higher dimensions."

- question: "Explain why the 3D distance formula adds a (z₂−z₁)² term rather than simply using the 2D formula with an additive z-correction."
  type: short-answer
  answer: "Because the three coordinate axes are mutually perpendicular, displacements in each direction contribute independently and orthogonally to total distance. The 2D formula gives the horizontal distance d_xy in the xy-plane. The actual 3D path from one point to the other is the hypotenuse of a right triangle whose legs are d_xy and |z₂−z₁|. Applying the Pythagorean theorem to this triangle gives distance² = d_xy² + (z₂−z₁)² = (x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)². The squaring and square-rooting follow directly from this second Pythagorean application."
  explanation: "The key geometric insight is that the three Cartesian axes are orthogonal — they don't cross-couple. This is what allows the formula to be a simple sum of squared differences. In a non-Cartesian system where axes are not perpendicular, you would need cross-terms (as in the law of cosines). The elegant form of the Euclidean metric reflects the orthogonality of the coordinate system."
```

## Explainer

You already know the 2D distance formula from the Pythagorean theorem: the distance between (x₁, y₁) and (x₂, y₂) is √[(x₂−x₁)² + (y₂−y₁)²]. This is just the length of the hypotenuse of a right triangle whose legs have lengths |x₂−x₁| and |y₂−y₁|. Extending to 3D requires one more application of the same theorem. Think of it as a two-step process: first find the horizontal distance in the xy-plane (ignoring z), then treat that horizontal distance and the vertical displacement |z₂−z₁| as the legs of a new right triangle. Applying Pythagoras again gives the full 3D distance.

Explicitly: the horizontal distance in the xy-plane is √[(x₂−x₁)² + (y₂−y₁)²]. Call this d_xy. Now the 3D diagonal from the first point to the second is the hypotenuse of a right triangle with legs d_xy and |z₂−z₁|, giving distance = √[d_xy² + (z₂−z₁)²] = √[(x₂−x₁)² + (y₂−y₁)² + (z₂−z₁)²]. The 3D coordinate system you studied as a prerequisite provides exactly the framework for this decomposition: the three axes are mutually perpendicular, so the three coordinate differences contribute independently and orthogonally to the total displacement.

This formula defines the **Euclidean metric** on ℝ³ — the standard way to measure distance in three-dimensional space. The word "metric" means a function that measures distance and satisfies three axioms: d(A, A) = 0, d(A, B) = d(B, A), and the triangle inequality d(A, C) ≤ d(A, B) + d(B, C). The Euclidean metric satisfies all three, and it is the natural notion of "straight-line distance" in physical space.

The distance formula also provides the equation of a **sphere**: all points (x, y, z) at distance r from a center (a, b, c) satisfy (x−a)² + (y−b)² + (z−c)² = r². This is just the distance formula squared, set equal to r². From here, the same ideas generalize: replacing the equality with an inequality describes the interior or exterior of a sphere, and the notion of distance is the foundation for limits, continuity, and convergence in three-dimensional calculus — all of which build directly on this formula.
