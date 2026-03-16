---
id: vectors-in-rn
title: Vectors in R^n
domain: mathematics
course: linear-algebra
prerequisites: []
builds-toward:
- vector-addition-subtraction
- scalar-multiplication-vectors
- linear-transformations
tags:
- vectors
- fundamentals
- rn-spaces
stage: formal-systems
status: draft
---

# Vectors in R^n

## Core Idea
A vector in R^n is an ordered n-tuple of real numbers, representing both magnitude and direction in n-dimensional space. Vectors can be represented as columns or rows and form the foundational objects of linear algebra. They generalize familiar 2D and 3D vectors to arbitrary dimensions, enabling abstract algebraic treatment.

## Explainer

A vector in ℝⁿ is an ordered list of n real numbers, written as a column (or sometimes a row). If you've worked with points in the coordinate plane, you already have the right intuition: a 2D point (3, −1) and the vector ⟨3, −1⟩ contain identical data — the vector just emphasizes movement and direction rather than location. The leap to ℝⁿ is notational: a vector in ℝ⁵ is ⟨x₁, x₂, x₃, x₄, x₅⟩, and the same geometric intuitions about arrows, lengths, and angles extend into dimensions you cannot visualize.

What makes vectors powerful is that they carry two types of information simultaneously: **magnitude** (how long the arrow is) and **direction** (which way it points). These can be separated: the zero vector has magnitude zero and no direction; any nonzero vector can be scaled to a unit vector that preserves only direction. The magnitude of v = ⟨v₁, ..., vₙ⟩ is ‖v‖ = √(v₁² + ... + vₙ²), a direct generalization of the Pythagorean theorem to n dimensions.

The convention of writing vectors as columns (rather than rows) will pay off when you encounter matrix-vector multiplication. A matrix A acting on a column vector v reads naturally as a linear combination of A's columns, weighted by the entries of v. For now, just know that column vectors and row vectors are transposes of each other, and linear algebra defaults to columns.

Beyond ℝ³, the n-dimensional setting arises naturally in practice. A data point with 100 measured features is a vector in ℝ¹⁰⁰. A 28×28 grayscale image is a vector in ℝ⁷⁸⁴. The algebraic rules — addition, scalar multiplication, dot product — work identically regardless of dimension. This is the power of abstraction: theorems proved for arbitrary ℝⁿ apply immediately to any of these concrete cases, without re-deriving anything.
