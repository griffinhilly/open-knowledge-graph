---
id: vector-magnitude-norm
title: Vector Magnitude and Norms
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-definition
  type: hard
builds-toward:
- dot-product-definition
- orthogonal-vectors-orthonormal-bases
tags:
- vectors
- magnitude
- norms
- distance
stage: formal-systems
status: draft
---

# Vector Magnitude and Norms

## Core Idea
The magnitude (or Euclidean norm) of a vector v = (v₁, ..., vₙ) is ||v|| = √(v₁² + ... + vₙ²), representing its length. A norm is any function satisfying positivity, homogeneity, and the triangle inequality. The Euclidean norm is the standard in linear algebra and relates to dot products and distances.

## Explainer

You already know from studying vectors in ℝⁿ that a vector is an ordered list of numbers representing a direction and magnitude in space. The **magnitude** (also called the **Euclidean norm** or **2-norm**) answers the question: how long is this vector? In two dimensions the answer comes directly from the Pythagorean theorem: a vector (v₁, v₂) has length √(v₁² + v₂²). In three dimensions, two applications of Pythagoras give √(v₁² + v₂² + v₃²). The pattern extends to any number of dimensions: ||v|| = √(v₁² + ... + vₙ²). This is not a new formula — it is the same Pythagorean idea, applied n-dimensionally.

The magnitude satisfies three fundamental properties that together define what it means for a function to be a **norm**. First, **positivity**: ||v|| ≥ 0, and ||v|| = 0 only when v is the zero vector (a vector with zero length must be the zero vector). Second, **homogeneity**: ||cv|| = |c| · ||v|| — scaling a vector by a scalar scales its length by the absolute value of that scalar. Third, the **triangle inequality**: ||u + v|| ≤ ||u|| + ||v|| — the length of a sum is no greater than the sum of the lengths, exactly as in the geometric fact that any side of a triangle is shorter than the sum of the other two sides.

Why define an abstract norm rather than just using the Euclidean formula? Because different problems call for different notions of "size." The **1-norm** (Manhattan distance) ||v||₁ = |v₁| + ... + |vₙ| counts the total absolute displacement, useful in optimization and statistics. The **∞-norm** ||v||∞ = max|vᵢ| measures the largest single component, useful for bounding errors. Any of these qualifies as a norm because all three properties hold. The Euclidean norm is special because it arises from a dot product — ||v|| = √(v · v) — which connects magnitude to angle and orthogonality and makes it the foundation for geometry in ℝⁿ.

Understanding magnitude builds directly toward the dot product and orthogonality. Two vectors are orthogonal when their dot product is zero; the dot product itself is ||u|| ||v|| cos θ, so the angle between vectors is defined through their norms. When you later normalize a vector to unit length by computing v/||v||, you are dividing by the norm to produce a vector of magnitude 1 that preserves the direction. This operation — and the geometric intuitions it carries — depends entirely on having a reliable way to measure length, which is exactly what the norm provides.
