---
id: kernel-and-image
title: Kernel and Image of Linear Transformations
domain: mathematics
course: linear-algebra
prerequisites:
- id: linear-transformation-matrix-representation
  type: hard
- id: rank-nullity-theorem
  type: hard
builds-toward:
- linear-transformations-advanced
- least-squares-approximation
tags:
- kernel
- image
- null-space
- column-space
stage: formal-systems
status: draft
---

# Kernel and Image of Linear Transformations

## Core Idea
The kernel ker(T) = {v : T(v) = 0} is the null space of the matrix A. The image im(T) = {T(v) : v ∈ V} is the column space of A. These subspaces determine when T is injective (ker(T) = {0}) or surjective (im(T) = W). The rank-nullity theorem: dim(ker(T)) + dim(im(T)) = dim(domain).

## How It's Best Learned
Compute kernel by solving Ax = 0 (null space). Find image by identifying pivot columns and their span. Relate geometric intuition: kernel is directions that collapse to zero; image is reachable outputs.

## Explainer

Every linear transformation T: V → W partitions its input space V into two fundamental subspaces. The **kernel** (also called the null space) is the collection of all vectors that T sends to the zero vector: ker(T) = {v ∈ V : T(v) = 0}. Think of the kernel as the "invisible" part of the domain — everything in it collapses to a single point (the zero vector in W) and leaves no trace in the output. The **image** (also called the column space or range) is the collection of all vectors that T can actually produce: im(T) = {T(v) : v ∈ V}. It answers the question "what outputs are reachable?"

From your prerequisite on matrix representations, you know T corresponds to a matrix A. Computing the kernel means solving the homogeneous system Ax = 0 — exactly the null space computation you've seen before. The image is the span of A's columns: any output T(v) = Av is a linear combination of the columns of A, weighted by the entries of v. So "which outputs are reachable?" is the same as "which vectors lie in the column space of A?"

The kernel determines **injectivity** (one-to-one-ness) of T. If ker(T) = {0} — the only vector sent to zero is zero itself — then T is injective: distinct inputs always produce distinct outputs. If the kernel contains nonzero vectors, then T collapses information: two different inputs (v and v + k, where k is in the kernel) map to the same output. The image determines **surjectivity** (onto-ness): T is surjective if and only if im(T) = W, meaning every vector in the target space is reachable.

The **rank-nullity theorem**, which you've already studied, ties these together with a single equation: dim(ker(T)) + dim(im(T)) = dim(V). The dimension of the kernel is called the **nullity**; the dimension of the image is called the **rank**. This is a conservation law: if T collapses a lot of information (large kernel, high nullity), it can only reach a small subspace of W (low rank). There is a precise trade-off between how much T "forgets" and how much it "covers." For a 3×3 matrix with rank 2, the nullity is 1 — the kernel is a line through the origin, and the image is a plane in ℝ³.
