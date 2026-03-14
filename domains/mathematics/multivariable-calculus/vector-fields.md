---
id: vector-fields
title: Vector Fields
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vectors-in-3d
  type: hard
- id: functions-of-several-variables
  type: hard
- id: gradient-vector
  type: soft
builds-toward:
- line-integrals-scalar
- line-integrals-vector-fields
- curl-and-divergence
- conservative-fields
tags:
- vector-field
- flow
- gradient-field
- visualization
stage: formal-systems
status: validated
---

# Vector Fields

## Core Idea
A vector field F(x, y) = ⟨P(x,y), Q(x,y)⟩ assigns a vector to each point in a region of ℝ² (or ℝ³). Vector fields model physical phenomena where both magnitude and direction vary continuously in space: velocity fields of fluids, gravitational and electric force fields, and magnetic fields. The gradient ∇f of a scalar function is a special type of vector field called a gradient field or conservative field. Visualizing vector fields requires drawing representative arrows proportional to F at sample points.

## How It's Best Learned
Use software tools to visualize vector fields — the qualitative behavior (sources, sinks, rotational patterns) is essential context for the theorems that follow. Students should be able to identify, at least roughly, whether a field is conservative (no rotation), has sources/sinks (nonzero divergence), or rotates (nonzero curl) before those terms are formally defined.

## Common Misconceptions
- A vector field is not a function from ℝ² to ℝ² in the sense of composition — each input point gets an attached vector, not a mapped-to point.
- The notation F = ⟨P, Q⟩ means F = P i + Q j; P and Q are scalar functions, not vectors.
- Not every vector field is the gradient of some scalar function; this special property characterizes conservative fields.
