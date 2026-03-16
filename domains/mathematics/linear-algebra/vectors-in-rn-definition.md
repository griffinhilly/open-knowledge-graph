---
id: vectors-in-rn-definition
title: Vectors in R^n and Vector Notation
domain: mathematics
course: linear-algebra
prerequisites: []
builds-toward:
- vector-addition-subtraction
- dot-product-definition
- vector-magnitude-norm
tags:
- vectors
- foundations
- rn
stage: formal-systems
status: draft
---

# Vectors in R^n and Vector Notation

## Core Idea
A vector in R^n is an ordered list of n real numbers, representing magnitude and direction in n-dimensional space. Vectors can be written as column vectors, row vectors, or using component notation v = (v₁, v₂, ..., vₙ). Vectors form the building blocks of linear algebra, used to represent points, directions, and transformations.

## Explainer

Start in R^2, which you can picture as the ordinary coordinate plane. A vector like (3, 4) names a specific point — but more usefully, it names a direction and distance: go 3 units right and 4 units up. The **ordered pair** is essential: (3, 4) and (4, 3) are different vectors because order encodes meaning. The same idea extends to R^3 (three coordinates for three-dimensional space) and then to R^n for any n. In R^n you can no longer picture the space visually, but the algebraic structure is identical: an **n-tuple** (v₁, v₂, ..., vₙ) of real numbers listed in a fixed order.

Notation matters because linear algebra uses vectors in two distinct roles. As a **column vector**, the numbers are stacked vertically and the vector is treated as an n×1 matrix — this is the default convention in most linear algebra contexts and the one that makes matrix-vector multiplication work cleanly. As a **row vector**, the numbers are arranged horizontally (a 1×n matrix). The component notation v = (v₁, ..., vₙ) is informal shorthand that works well for description but must be converted to column form for most calculations. Getting comfortable switching between these three representations is a basic fluency skill for everything that follows.

Vectors serve two overlapping roles: they can represent **points** (locations in space) or **directions** (displacements). The vector (3, 4) could mean "the point at coordinates (3, 4)" or "move 3 units in the x-direction and 4 in the y-direction." In linear algebra, the displacement interpretation is usually dominant: vectors are arrows you can add, scale, and combine. When you add two vectors, you chain their displacements; when you multiply by a scalar, you stretch or flip the arrow. These operations — addition and scalar multiplication — are exactly the operations that define a vector space, which is the framework underlying all of linear algebra.

The specific choice of R^n (real numbers) matters: the components are ordinary numbers you can do arithmetic with, which makes it possible to define geometric concepts like length and angle algebraically. The **magnitude** of v = (v₁, ..., vₙ) is √(v₁² + ... + vₙ²), a direct generalization of the Pythagorean theorem. Even in R^1000, "length" and "angle" have precise meanings through this formula. This algebraic generalization of geometry — extending familiar two- and three-dimensional intuitions to arbitrary dimensions — is the central payoff of the vector framework.
