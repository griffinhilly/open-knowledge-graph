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
