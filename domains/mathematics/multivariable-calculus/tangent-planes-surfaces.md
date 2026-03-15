---
id: tangent-planes-surfaces
title: Tangent Planes to Surfaces
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector-definition
  type: hard
- id: tangent-planes-linear-approximation
  type: hard
builds-toward:
- surface-parametrization
tags:
- tangent-planes
- surfaces
- normal-vector
stage: formal-systems
status: draft
---

# Tangent Planes to Surfaces

## Core Idea
For a surface z = f(x, y), the tangent plane at (x₀, y₀, z₀) has equation z − z₀ = f_x(x₀, y₀)(x − x₀) + f_y(x₀, y₀)(y − y₀). The normal vector is n = ⟨f_x, f_y, −1⟩, and ∇f lies in the plane.
