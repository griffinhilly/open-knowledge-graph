---
id: dot-product-geometry
title: Dot Product and Projections
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-3d-coordinate-system
  type: hard
- id: dot-product
  type: hard
builds-toward:
- directional-derivatives
- gradient-vector-properties
tags:
- dot-product
- projections
- orthogonality
stage: formal-systems
status: draft
---

# Dot Product and Projections

## Core Idea
The dot product a·b = |a||b|cos(θ) measures how aligned two vectors are. Geometrically, it computes the projection of one vector onto another: proj_a(b) = (a·b/|a|²)a. When a·b = 0, vectors are orthogonal.

## Explainer

You already know the algebraic definition of the dot product: **a** · **b** = a₁b₁ + a₂b₂ + a₃b₃ for vectors in R³. What the formula **a** · **b** = |**a**||**b**|cos(θ) adds is a geometric interpretation: the dot product is the product of the two magnitudes, scaled by the cosine of the angle between them. Cosine is 1 when the vectors point the same way, 0 when perpendicular, and −1 when antiparallel. So the dot product is a measure of **alignment** — how much the two vectors point in the same direction, weighted by their lengths.

This is why **orthogonality** (perpendicularity) has the clean test **a** · **b** = 0. At 90°, cos(θ) = 0, so the product vanishes regardless of the magnitudes. Two nonzero vectors with zero dot product are perpendicular. This test generalizes to any dimension, even when you have no direct geometric picture of "perpendicular" — in Rⁿ, we *define* orthogonality by the dot product being zero. The algebraic formula extends the geometric notion.

The **scalar projection** of **b** onto **a** is the signed length of **b**'s shadow cast along the direction of **a**: comp_**a**(**b**) = (**a** · **b**)/|**a**| = |**b**|cos(θ). The **vector projection** rescales the unit vector in **a**'s direction by this amount: proj_**a**(**b**) = ((**a** · **b**)/|**a**|²)**a**. Intuitively, you are decomposing **b** into two components: one along **a** and one perpendicular to **a**. The vector projection gives the parallel component; subtracting it from **b** gives the perpendicular component **b** − proj_**a**(**b**), which is orthogonal to **a** by construction. This decomposition — parallel plus perpendicular — is one of the most repeatedly useful tools in vector calculus.

The dot product's role will grow significantly as you move to directional derivatives and gradients. The directional derivative of f in direction **u** is ∇f · **u** — the dot product of the gradient with a unit vector. This dot product is maximized when **u** aligns with ∇f, which is why the gradient points in the direction of steepest ascent. Every statement about "how fast f changes in direction **u**" is a dot product statement. Learning to see alignment and projection as the fundamental interpretations of the dot product now sets you up to read gradient geometry fluently.
