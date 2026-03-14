---
id: critical-points-multivariable
title: Critical Points of Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: gradient-vector
  type: hard
- id: optimization-problems
  type: soft
builds-toward:
- second-partials-test
- lagrange-multipliers
tags:
- critical-points
- optimization
- saddle-points
- local-extrema
stage: formal-systems
status: validated
---

# Critical Points of Multivariable Functions

## Core Idea
A critical point of f(x, y) is a point where ∇f = 0 (both partial derivatives are zero) or where ∇f is undefined. Critical points are candidates for local maxima, local minima, and saddle points. Unlike single-variable calculus, critical points in ℝ² can be saddle points — points that are local minima in one direction and local maxima in another, with no extreme value. Finding critical points requires solving a system of equations f_x = 0 and f_y = 0 simultaneously.

## How It's Best Learned
The saddle point concept has no single-variable analogue and requires geometric visualization. Show the surface z = x² − y² (a classic saddle) and identify that its critical point at the origin is neither a max nor a min. Then contrast with z = x² + y² (paraboloid) whose critical point at the origin is a minimum.

## Common Misconceptions
- Not every critical point is a local extremum — saddle points are critical points that are neither maxima nor minima.
- Setting f_x = 0 alone is insufficient; both partial derivatives must be zero (or undefined) simultaneously.
- A function defined on a closed bounded domain can also attain its extrema on the boundary, not just at interior critical points.
