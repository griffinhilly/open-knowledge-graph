---
id: vector-norms-magnitude
title: Vector Norms and Magnitude
domain: mathematics
course: linear-algebra
prerequisites:
- id: dot-product
  type: hard
builds-toward:
- orthogonal-projections
- gram-schmidt-process
- inner-product-spaces
tags:
- norm
- magnitude
- length
- distance
stage: formal-systems
status: draft
---

# Vector Norms and Magnitude

## Core Idea
The Euclidean norm (or length) of a vector v in R^n is ‖v‖ = √(v · v) = √(v₁² + v₂² + ... + vₙ²), extending the Pythagorean theorem to n dimensions. Unit vectors have norm 1. The norm defines a notion of distance and is used to measure vector sizes, convergence, and error in computations.

## How It's Best Learned
Start with concrete 2D and 3D examples, computing norms and verifying the Pythagorean relationship. Then verify that the formula extends naturally to higher dimensions through abstract notation.

## Common Misconceptions
Confusing the dot product with the norm—the norm is a single number (length), while the dot product requires two vectors. Forgetting the square root when computing norm from the dot product.

## Explainer

You already know the dot product: given v = (v₁, v₂, ..., vₙ), the dot product v · v = v₁² + v₂² + ... + vₙ². Now ask: what does this number measure? In two dimensions, v · v = v₁² + v₂², and by the Pythagorean theorem this is exactly the square of the distance from the origin to the point (v₁, v₂). The **Euclidean norm** ‖v‖ = √(v · v) is simply that distance — the length of the arrow from the origin to the tip of v. The square root extracts the actual length from the squared-length that the dot product gives you.

This extends cleanly to n dimensions even though you can no longer draw a picture. In R³, ‖v‖ = √(v₁² + v₂² + v₃²) is the 3D distance formula from the origin, itself just a double application of the Pythagorean theorem (first in the xy-plane, then vertically). In Rⁿ, you apply the same formula with n terms. The geometry is harder to visualize, but the algebra is identical. A **unit vector** has norm exactly 1 — it points in a direction but carries no length information. Any nonzero vector can be normalized by dividing by its norm: u = v/‖v‖ gives a unit vector in the same direction as v.

The norm is the foundation for measuring distance between vectors: dist(u, v) = ‖u - v‖. If u = (3, 0) and v = (0, 4), then u - v = (3, -4) and ‖u - v‖ = √(9 + 16) = 5 — exactly the hypotenuse of the 3-4-5 right triangle. This distance function lets you ask "how far apart are two vectors?" which in turn underpins convergence (a sequence vₙ converges if ‖vₙ - L‖ → 0), error measurement in computation, and the geometry of orthogonal projections you will study next.

One critical distinction: the norm takes one vector and returns a scalar; the dot product takes two vectors and returns a scalar. They are related by ‖v‖² = v · v, but the norm is not the dot product of v with itself — it is the *square root* of that dot product. This is the most common computational error, so build the habit of writing ‖v‖ = √(v · v), not ‖v‖ = v · v.
