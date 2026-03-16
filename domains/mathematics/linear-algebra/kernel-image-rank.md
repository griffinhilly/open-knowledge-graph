---
id: kernel-image-rank
title: Kernel, Image, and Rank of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-definition
  type: hard
- id: vector-subspaces
  type: hard
builds-toward:
- rank-nullity-theorem
tags:
- transformations
- kernel
- image
- rank
stage: formal-systems
status: draft
---

# Kernel, Image, and Rank of Linear Transformations

## Core Idea
For a linear transformation T: V → W, the kernel ker(T) = {x : T(x) = 0} and image im(T) = {T(x) : x ∈ V} are subspaces. Rank is dim(im(T)); nullity is dim(ker(T)). These are the column space and null space for matrix representations.

## Explainer

Think of a linear transformation T: V → W as a machine that takes vectors from one space and sends them to another. The **kernel** of T is the set of all inputs that the machine "crushes" to zero — the vectors that T cannot distinguish from the zero vector. Every linear transformation sends zero to zero, so the kernel always contains at least the zero vector. But if other vectors land on zero too, those vectors are genuinely lost by T: T has no way to tell them apart from 0.

The **image** of T is what the machine can actually produce — all possible outputs. You already know from your study of vector subspaces that both ker(T) and im(T) are subspaces (closed under addition and scalar multiplication). The image tells you how much of W that T can reach. If T: ℝ³ → ℝ³ is a projection onto a plane, the image is a 2-dimensional plane inside ℝ³, and the kernel is the 1-dimensional line perpendicular to that plane.

**Rank** is the dimension of the image — it measures how much of the output space T actually covers. **Nullity** is the dimension of the kernel — it measures how much information T destroys. For a matrix, rank counts the number of linearly independent columns (the column space), while nullity counts the degrees of freedom in the solution set of Ax = 0 (the null space). These two quantities are not independent: the rank-nullity theorem (your next topic) establishes that rank + nullity = dim(V), meaning that every dimension of the input space is accounted for — it either contributes to the image or is swallowed by the kernel.

The practical payoff is understanding solvability. The equation T(x) = w has a solution if and only if w ∈ im(T). If T has full rank — im(T) = W — then T hits every target and every equation is solvable. If the kernel is non-trivial, solutions are not unique: whenever T(x₀) = w, then T(x₀ + k) = w for any k ∈ ker(T). The kernel parameterizes the ambiguity in solutions, the image determines which equations can be solved at all.
