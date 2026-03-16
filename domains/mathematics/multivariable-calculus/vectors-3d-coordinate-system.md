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

## Explainer

You already know that every point in 3D space is located by three coordinates (x, y, z), measuring displacement along three mutually perpendicular axes. A **vector** in R³ takes this idea one step further: instead of labeling a location, a vector encodes a *displacement* — a directed movement through space. The vector ⟨a, b, c⟩ means "move a units in the x-direction, b units in the y-direction, c units in the z-direction." It has a direction and a magnitude, but no fixed starting position.

The distinction between a point and a vector is fundamental. The point (3, 4, 0) is a specific location. The vector ⟨3, 4, 0⟩ is an instruction: move 3 right and 4 forward. Starting at (1, 1, 0) and applying that vector brings you to (4, 5, 0); starting at the origin brings you to (3, 4, 0). Same vector, different results depending on where you begin. Vectors are arrows that can be picked up and placed anywhere; what defines a vector is its components, not where its tail sits. The one exception is the **position vector** ⟨x, y, z⟩, which conventionally has its tail at the origin — it bridges points and vectors by identifying each point with the displacement from the origin to that point.

The **magnitude** of a vector v = ⟨a, b, c⟩ is its length: ‖v‖ = √(a² + b² + c²). This is the Pythagorean theorem extended to three dimensions: in 2D you had √(a² + b²) for the hypotenuse; the third dimension simply adds c² under the radical. A vector with ‖v‖ = 1 is called a **unit vector**; dividing any nonzero vector by its magnitude gives the unit vector in the same direction: v̂ = v/‖v‖.

Vectors support two operations that form the foundation for all of multivariable calculus. **Scalar multiplication** c⟨a, b, c⟩ = ⟨ca, cb, cc⟩ stretches or shrinks the vector — and reverses its direction when c < 0. **Vector addition** ⟨a₁, b₁, c₁⟩ + ⟨a₂, b₂, c₂⟩ = ⟨a₁ + a₂, b₁ + b₂, c₁ + c₂⟩ combines two displacements: first travel by the first vector, then by the second. Together these operations obey the same algebraic rules as ordinary numbers, making R³ a **vector space**. The dot product, cross product, gradient, and every integral theorem in multivariable calculus are built directly on top of these two basic vector operations.
