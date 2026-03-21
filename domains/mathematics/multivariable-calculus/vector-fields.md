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

## Questions

```yaml
- question: "What is the output of the vector field F(x, y) = ⟨−y, x⟩ at the point (3, 2)?"
  type: multiple-choice
  options:
    - "A scalar value of −6"
    - "The vector ⟨−2, 3⟩"
    - "The vector ⟨3, 2⟩"
    - "The vector ⟨−3, −2⟩"
  answer: 1
  explanation: "A vector field evaluates to a vector at each point, not a scalar. Substituting (x, y) = (3, 2) into F(x, y) = ⟨−y, x⟩ gives ⟨−2, 3⟩. The P-component is −y = −2, and the Q-component is x = 3. This illustrates that the output is a vector (two numbers), not a single number, and that the components of a vector field are functions of position."

- question: "A fluid velocity field has arrows at every sampled point directed toward a single center point, with the arrows growing longer as they approach the center. What does this pattern most directly represent?"
  type: multiple-choice
  options:
    - "A rotating flow circling the center point"
    - "A uniform flow in the direction of the center"
    - "A converging (sink) flow where fluid flows inward and accelerates toward the center"
    - "A field with constant magnitude but varying direction"
  answer: 2
  explanation: "Arrows pointing toward a central point with increasing length indicate a sink: fluid is converging inward, and the flow speed increases as it approaches the center. This is the visual pattern of a draining vortex or gravitational attraction. Rotation would show arrows circling the center (tangent to circles), not pointing toward it. This example illustrates why arrow patterns in vector field visualizations carry geometric information about the field's behavior."

- question: "In a vector field, two points that are very close together in space can have vectors pointing in completely different directions."
  type: true-false
  answer: true
  explanation: "A vector field assigns an independent vector to each point in space based on the field's component functions P and Q (or P, Q, R in 3D). There is no requirement that nearby points have similar vectors — the field could change direction rapidly. In practice, smooth physical fields (like velocity or gravity) tend to vary continuously, so nearby points often have similar vectors, but this is a property of the specific field, not a definitional requirement. The field F(x, y) = ⟨sin(100x), cos(100y)⟩ would have rapidly oscillating directions at nearby points."

- question: "The vector field F(x, y) = ⟨1, 0⟩ produces longer arrows at points farther from the origin, reflecting increasing field strength with distance."
  type: true-false
  answer: false
  explanation: "F(x, y) = ⟨1, 0⟩ is a uniform field — every point in the plane gets the exact same vector ⟨1, 0⟩, regardless of location. The magnitude is 1 everywhere, and all arrows point in the positive x-direction with equal length. This is analogous to a uniform horizontal wind: same speed and direction throughout the region. Arrow length in a vector field diagram reflects the magnitude of F at that point, not distance from the origin."

- question: "Why are vector fields more appropriate than individual vectors for modeling physical phenomena like gravity or fluid flow, and what does the function F: ℝⁿ → ℝⁿ structure capture?"
  type: short-answer
  answer: "Gravity and fluid flow don't act at a single point — they assign a force or velocity to every point in space simultaneously. A single vector captures what happens at one location; a vector field captures the complete spatial structure by specifying a vector at every point. The function structure F: ℝⁿ → ℝⁿ formalizes this: you input a position and get the corresponding vector, making the whole spatial pattern computable and analyzable."
  explanation: "The power of the vector field concept is that it lifts the idea of a directed quantity from individual points to an entire region of space. This is what makes it possible to compute quantities like total work done by a force along a path (line integrals) or whether a fluid is spreading out or rotating at a given location (divergence and curl). Physical laws like Maxwell's equations and the Navier-Stokes equations are naturally expressed as relationships between vector fields, not individual vectors."
```

## Explainer

From your study of vectors in 3D, you know how to represent individual vectors as arrows with magnitude and direction. A **vector field** takes this one step further: instead of a single arrow, you attach an arrow to every point in a region of space. Formally, a vector field F on ℝ² assigns to each point (x, y) a vector ⟨P(x,y), Q(x,y)⟩, where P and Q are real-valued functions. In ℝ³ you get a third component: F(x, y, z) = ⟨P, Q, R⟩. The result is not a single geometric object but an entire landscape of arrows.

The physical examples are the clearest way to build intuition. A **velocity field** assigns to each point in a fluid the velocity vector of the fluid particle at that point — the arrows show which way the water (or air) is flowing and how fast. A **gravitational field** assigns to each point in space the acceleration that a unit mass would experience if placed there — pointing toward Earth's center, growing stronger as you descend. An **electric field** assigns to each point the force per unit charge experienced by a positive test charge. In every case, the vector field is a function of position that produces a vector output, and the arrows drawn at sampled points give a qualitative picture of the whole field.

To visualize a vector field, you sample a grid of points and draw an arrow at each one, with the arrow's direction and length determined by F at that point. In practice, arrows are often normalized to a fixed length (or scaled down) to avoid clutter, showing direction more clearly than magnitude. Recognizable patterns emerge: a field like F(x, y) = ⟨−y, x⟩ produces counterclockwise rotation around the origin; F(x, y) = ⟨x, y⟩ produces outward-pointing arrows that grow with distance; F(x, y) = ⟨1, 0⟩ is a uniform horizontal flow.

Vector fields are the natural input for the two central operations of multivariable calculus that come next: **line integrals** and the differential operators **curl** and **divergence**. The line integral of F along a curve measures the total "work done" by the field along that path. The divergence of F measures how much the field is spreading out (or converging) at each point; the curl measures how much it is rotating. These operations extract scalar information from the vector field and are the language of Maxwell's equations, fluid mechanics, and gravitational theory — all of which you'll be equipped to read once you understand what a vector field is.
