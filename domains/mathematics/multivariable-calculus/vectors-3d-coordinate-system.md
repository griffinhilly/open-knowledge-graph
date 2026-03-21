---
id: vectors-3d-coordinate-system
title: 3D Coordinate Systems and Vectors
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: 3d-coordinate-systems
  type: hard
builds-toward:
- vector-magnitude-norm
- dot-product
- cross-product-3d
tags:
- vectors
- 3d
- coordinate-geometry
stage: formal-systems
status: draft
---

# 3D Coordinate Systems and Vectors

## Core Idea
A vector in R³ is an ordered triple ⟨a, b, c⟩ representing displacement from the origin. Vectors in 3D space have magnitude (length) and direction, forming the foundation for multivariable calculus. The position vector from origin to point (x, y, z) is r = ⟨x, y, z⟩.

## How It's Best Learned
Start with 2D vectors, then extend to 3D by adding the z-component. Visualize vectors as arrows in 3D space using coordinate axes.

## Common Misconceptions
Confusing vectors with points; forgetting that vectors represent displacement, not position (though position vectors reference the origin).

## Questions

```yaml
- question: "Two arrows are drawn in 3D space with identical components ⟨3, 0, −2⟩ — one with its tail at (1, 1, 0) and one with its tail at (5, −2, 3). Which statement is correct?"
  type: multiple-choice
  options:
    - "They are different vectors because they start at different locations in space"
    - "They are the same vector because vectors are defined by their components, not their starting position"
    - "They are different vectors because their heads point to different terminal points"
    - "They are equal only if one of them is a position vector from the origin"
  answer: 1
  explanation: "A vector is defined entirely by its components — its direction and magnitude. Two vectors with identical components are the same mathematical object regardless of where their tails are placed. This is what distinguishes vectors from points: vectors are free to be translated anywhere without changing their identity. Option A is the classic misconception of treating a vector like a fixed, located arrow. Option C describes points (locations), not vectors."

- question: "A particle is at point P = (2, −1, 4). You apply displacement vector v = ⟨−2, 3, −4⟩. What is the particle's new position?"
  type: multiple-choice
  options:
    - "(−2, 3, −4) — the displacement vector itself"
    - "(−4, −3, −16) — multiplying corresponding coordinates"
    - "(0, 2, 0) — adding v's components to P's coordinates"
    - "(4, −4, 8) — subtracting the wrong way"
  answer: 2
  explanation: "Applying a displacement vector means adding its components to the current coordinates: (2 + (−2), −1 + 3, 4 + (−4)) = (0, 2, 0). Option A is the most common error — confusing the vector (a displacement instruction) with the resulting position. The vector tells you how far to move; the new position is where you end up after starting at P."

- question: "The magnitude of vector ⟨3, 0, 4⟩ is 5."
  type: true-false
  answer: true
  explanation: "The magnitude is computed using the 3D Pythagorean theorem: ‖v‖ = √(3² + 0² + 4²) = √(9 + 0 + 16) = √25 = 5. The zero y-component simply contributes nothing under the radical — this vector lies in the xz-plane and is the familiar 3-4-5 right triangle extended into 3D."

- question: "The position vector of point (a, b, c) is a fundamentally different type of mathematical object from the vector ⟨a, b, c⟩."
  type: true-false
  answer: false
  explanation: "A position vector IS the vector ⟨a, b, c⟩, conventionally drawn with its tail at the origin. It is not a new type of object — it is the same displacement vector, just given a specific starting point. The term 'position vector' describes a role or convention (tail at origin), not a different mathematical entity. This bridge between points and vectors is exactly what makes the notation r = ⟨x, y, z⟩ useful for tying geometry to algebra."

- question: "What is the key conceptual difference between a point (x, y, z) and a vector ⟨x, y, z⟩, and how does the notion of a position vector bridge the two?"
  type: short-answer
  answer: "A point (x, y, z) is a fixed location in space. A vector ⟨x, y, z⟩ is a displacement — an instruction to move x units along the x-axis, y along y, z along z — with no fixed starting position. The position vector bridges them by anchoring the vector's tail at the origin, so it points from (0,0,0) to the point (x,y,z). This lets every point be identified with the displacement needed to reach it from the origin."
  explanation: "This distinction is foundational. Vectors can be freely translated (same vector, different starting point); points cannot. The confusion arises because they share numerical coordinates — both a point and a vector can be described by three numbers — but they answer different questions: 'where is it?' vs. 'how far and in what direction?' The position vector is useful precisely because it gives each point a canonical vector representative, linking the geometry of locations to the algebra of displacements."
```

## Explainer

You already know that every point in 3D space is located by three coordinates (x, y, z), measuring displacement along three mutually perpendicular axes. A **vector** in R³ takes this idea one step further: instead of labeling a location, a vector encodes a *displacement* — a directed movement through space. The vector ⟨a, b, c⟩ means "move a units in the x-direction, b units in the y-direction, c units in the z-direction." It has a direction and a magnitude, but no fixed starting position.

The distinction between a point and a vector is fundamental. The point (3, 4, 0) is a specific location. The vector ⟨3, 4, 0⟩ is an instruction: move 3 right and 4 forward. Starting at (1, 1, 0) and applying that vector brings you to (4, 5, 0); starting at the origin brings you to (3, 4, 0). Same vector, different results depending on where you begin. Vectors are arrows that can be picked up and placed anywhere; what defines a vector is its components, not where its tail sits. The one exception is the **position vector** ⟨x, y, z⟩, which conventionally has its tail at the origin — it bridges points and vectors by identifying each point with the displacement from the origin to that point.

The **magnitude** of a vector v = ⟨a, b, c⟩ is its length: ‖v‖ = √(a² + b² + c²). This is the Pythagorean theorem extended to three dimensions: in 2D you had √(a² + b²) for the hypotenuse; the third dimension simply adds c² under the radical. A vector with ‖v‖ = 1 is called a **unit vector**; dividing any nonzero vector by its magnitude gives the unit vector in the same direction: v̂ = v/‖v‖.

Vectors support two operations that form the foundation for all of multivariable calculus. **Scalar multiplication** c⟨a, b, c⟩ = ⟨ca, cb, cc⟩ stretches or shrinks the vector — and reverses its direction when c < 0. **Vector addition** ⟨a₁, b₁, c₁⟩ + ⟨a₂, b₂, c₂⟩ = ⟨a₁ + a₂, b₁ + b₂, c₁ + c₂⟩ combines two displacements: first travel by the first vector, then by the second. Together these operations obey the same algebraic rules as ordinary numbers, making R³ a **vector space**. The dot product, cross product, gradient, and every integral theorem in multivariable calculus are built directly on top of these two basic vector operations.
