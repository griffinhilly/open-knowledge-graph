---
id: dot-product-definition
title: Dot Product and Inner Product
domain: mathematics
course: linear-algebra
prerequisites:
- id: vectors-in-rn-definition
  type: hard
- id: vector-magnitude-norm
  type: hard
builds-toward:
- orthogonal-vectors-orthonormal-bases
- inner-product-spaces
tags:
- vectors
- dot product
- inner product
stage: formal-systems
status: draft
---

# Dot Product and Inner Product

## Core Idea
The dot product of vectors u and v is u·v = u₁v₁ + ... + uₙvₙ, a scalar equal to ||u|| ||v|| cos(θ) where θ is the angle between them. The dot product measures alignment: it's zero for perpendicular vectors and positive/negative based on acute/obtuse angles. It underpins geometric reasoning in linear algebra.

## Explainer

You already know that vectors in ℝⁿ are lists of coordinates representing direction and magnitude, and that the **norm** (length) of a vector is computed by summing squared components and taking the square root. The dot product is the next operation — and while it looks like a simple coordinate calculation (multiply matching components, add the products), its geometric meaning is what makes it so useful.

The dot product u·v = u₁v₁ + u₂v₂ + ... + uₙvₙ produces a single number, a **scalar**. Think of two vectors in ℝ² pointing in different directions. If they point in exactly the same direction, their dot product equals the product of their lengths (||u|| × ||v||), its maximum possible value. If they are perpendicular — pointing at a right angle — the dot product is exactly zero. If they point in roughly opposite directions, the dot product is negative. This is the geometric meaning: u·v = ||u|| ||v|| cos(θ), where θ is the angle between them. The dot product measures how much the two vectors "agree" in direction.

The most immediate use is testing for **orthogonality**: two nonzero vectors are perpendicular if and only if their dot product is zero. This is one of the most important computations in linear algebra — orthogonal vectors are independent in the strongest geometric sense, and building orthogonal sets of vectors is a central technique. The dot product also gives you the angle between any two vectors directly: θ = arccos(u·v / (||u|| ||v||)). You could never compute angles between high-dimensional vectors any other way.

A concrete application builds intuition: **projecting** one vector onto another. If you want to know how much of vector u lies in the direction of v, you compute the scalar projection: (u·v) / ||v||. Physically, this is like asking "how far does u's shadow extend along v?" If you then multiply by the unit vector in v's direction, you get the **vector projection** of u onto v. This operation is the geometric heart of least-squares fitting, Gram-Schmidt orthogonalization, and nearly every algorithm that decomposes vectors into components. The dot product is not just an arithmetic rule — it is the core tool for thinking about angles, projections, and geometric relationships in any number of dimensions.
