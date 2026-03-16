---
id: vector-fields
title: Vector Fields and Their Representations
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: applications-triple-integrals
  type: soft
- id: vectors-in-3d
  type: hard
builds-toward:
- line-integrals
- curl-and-divergence
tags:
- vector-fields
- representation
- examples
stage: formal-systems
status: draft
---

# Vector Fields and Their Representations

## Core Idea
A vector field F: ℝⁿ → ℝⁿ assigns a vector to each point in space, such as F(x, y) = ⟨P(x,y), Q(x,y)⟩. Vector fields model physical phenomena: velocity (fluid flow), force (electric or gravitational), and heat flux. Visualization uses arrows indicating magnitude and direction.

## Explainer

From your study of vectors in 3D, you know how to represent individual vectors as arrows with magnitude and direction. A **vector field** takes this one step further: instead of a single arrow, you attach an arrow to every point in a region of space. Formally, a vector field F on ℝ² assigns to each point (x, y) a vector ⟨P(x,y), Q(x,y)⟩, where P and Q are real-valued functions. In ℝ³ you get a third component: F(x, y, z) = ⟨P, Q, R⟩. The result is not a single geometric object but an entire landscape of arrows.

The physical examples are the clearest way to build intuition. A **velocity field** assigns to each point in a fluid the velocity vector of the fluid particle at that point — the arrows show which way the water (or air) is flowing and how fast. A **gravitational field** assigns to each point in space the acceleration that a unit mass would experience if placed there — pointing toward Earth's center, growing stronger as you descend. An **electric field** assigns to each point the force per unit charge experienced by a positive test charge. In every case, the vector field is a function of position that produces a vector output, and the arrows drawn at sampled points give a qualitative picture of the whole field.

To visualize a vector field, you sample a grid of points and draw an arrow at each one, with the arrow's direction and length determined by F at that point. In practice, arrows are often normalized to a fixed length (or scaled down) to avoid clutter, showing direction more clearly than magnitude. Recognizable patterns emerge: a field like F(x, y) = ⟨−y, x⟩ produces counterclockwise rotation around the origin; F(x, y) = ⟨x, y⟩ produces outward-pointing arrows that grow with distance; F(x, y) = ⟨1, 0⟩ is a uniform horizontal flow.

Vector fields are the natural input for the two central operations of multivariable calculus that come next: **line integrals** and the differential operators **curl** and **divergence**. The line integral of F along a curve measures the total "work done" by the field along that path. The divergence of F measures how much the field is spreading out (or converging) at each point; the curl measures how much it is rotating. These operations extract scalar information from the vector field and are the language of Maxwell's equations, fluid mechanics, and gravitational theory — all of which you'll be equipped to read once you understand what a vector field is.
