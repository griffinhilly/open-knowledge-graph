---
id: vectors-in-rn-operations
title: 'Vectors in R^n: Addition and Scalar Multiplication'
domain: mathematics
course: linear-algebra
prerequisites:
- id: coordinate-plane-all-four-quadrants
  type: soft
builds-toward:
- dot-product
- vector-norms
- vector-spaces
tags:
- vectors
- operations
- foundational
stage: formal-systems
status: draft
---

# Vectors in R^n: Addition and Scalar Multiplication

## Core Idea
Vectors in R^n are ordered n-tuples of real numbers that can be added component-wise and scaled by real numbers. These operations follow algebraic rules (commutativity, associativity, distributivity) that define R^n as a vector space. Understanding vector operations is foundational for linear algebra, enabling the study of higher-dimensional systems.

## How It's Best Learned
Use 2D and 3D geometric intuition first (arrows in the plane), then verify operations algebraically. Practice visualizing multiple vector operations combined (e.g., 2u + 3v).

## Common Misconceptions
Vectors are not points, though they can be represented with a starting point. Component-wise operations are not element-wise matrix operations—they're the same thing only for column/row vectors.

## Explainer

You already know how to plot points in the coordinate plane using (x, y) coordinates. A vector in ℝ² is written the same way — as an ordered pair — but the interpretation shifts: instead of a location, a vector represents a **displacement**, an arrow with a direction and a length. The vector **v** = (3, 2) means "move 3 units right and 2 units up," not "the point at position 3, 2." This distinction matters because vectors can be placed anywhere — what defines them is their direction and magnitude, not their starting point.

**Vector addition** combines two displacements. To add **u** = (1, 4) and **v** = (3, 2), you add component-wise: **u** + **v** = (4, 6). Geometrically, this is the tip-to-tail rule: place the tail of **v** at the tip of **u**, and the sum is the arrow from your starting point to where you end up. The commutativity and associativity you know from numbers carry over because the components are just numbers — the rules are inherited coordinate by coordinate.

**Scalar multiplication** stretches or flips a vector. Multiplying **v** = (3, 2) by 2 gives (6, 4) — the arrow doubles in length, pointing the same direction. Multiplying by −1 gives (−3, −2) — same length, reversed direction. Multiplying by 0 gives (0, 0), the **zero vector**, which has no direction and acts as the additive identity. The combination of scalar multiplication and addition is called a **linear combination**: expressions like 2**u** + 3**v** are the building blocks of all of linear algebra.

In ℝⁿ for higher n, everything works the same way component-wise, just with more slots. You can't draw ℝ⁷, but you can manipulate it algebraically with complete confidence — each operation acts independently on each coordinate. The eight vector space axioms (commutativity, associativity, distributivity, etc.) you verify for ℝ² all hold for ℝⁿ by the same argument, applied to each component. This is what makes ℝⁿ a **vector space**: a setting where these two operations satisfy the axioms. Later topics like dot products, norms, and linear transformations all build on this foundation.
