---
id: level-sets-surfaces
title: Level Sets and Surfaces in 3D
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: 3d-coordinate-systems
  type: hard
- id: functions-of-several-variables
  type: hard
builds-toward:
- contour-maps
- tangent-planes-linear-approximation
- gradient-vector-properties
tags:
- level-sets
- surfaces
- implicit-functions
stage: formal-systems
status: draft
---

# Level Sets and Surfaces in 3D

## Core Idea
A level set is the set of all points where f(x, y, z) = k for a fixed constant k. For a function f: ℝ² → ℝ, level sets are curves; for f: ℝ³ → ℝ, level sets are surfaces. These visualize how a scalar field varies through space.

## Explainer

You've already worked with functions of several variables, which assign a number to each point in 2D or 3D space — temperature at a location, altitude above sea level, pressure in an atmosphere. A **level set** visualizes such a function by asking: where does f take the same value k? For f: ℝ² → ℝ, the set {(x, y) : f(x, y) = k} is typically a curve in the plane — a **level curve** (or contour line). The collection of level curves for many values of k is the **contour map** you see on topographic charts: each closed loop marks a fixed elevation, and closely spaced contours indicate a steep slope.

For functions of three variables, fixing f(x, y, z) = k produces a **level surface** — a 2D surface embedded in 3D space. The classic example: f(x, y, z) = x² + y² + z² has level surfaces that are spheres of radius √k. Another: f(x, y, z) = x + 2y − z = k gives a family of parallel planes. The equation f = k defines the surface **implicitly**, without solving for any one variable as a function of the others. This implicit representation is more flexible than the explicit form z = g(x, y): it handles surfaces like spheres, tori, and saddle surfaces that fail the vertical-line test and cannot be globally written as a graph.

Level sets are the right conceptual tool whenever you want to describe a surface as the boundary between regions where a function is above or below a threshold. Isotherms in meteorology, equipotential surfaces in electrostatics, and decision boundaries in machine learning are all level sets of scalar fields. Thinking in level sets trains the habit of asking not "what is the value of f?" but "where does f equal this value?" — a shift that unlocks many geometric arguments.

One key geometric fact that connects level sets to the rest of multivariable calculus: the **gradient ∇f at a point P on a level surface is perpendicular to the surface at P**. Moving along the surface keeps f constant — the directional derivative along any tangent direction is zero — while the gradient points in the direction of maximum change. These two directions are orthogonal. This observation will become the foundation for tangent planes: the tangent plane to the level surface f(x, y, z) = k at a point P is exactly the plane through P perpendicular to ∇f(P).
