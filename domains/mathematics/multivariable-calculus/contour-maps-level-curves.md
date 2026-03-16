---
id: contour-maps-level-curves
title: Contour Maps and Level Curves
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-functions-intro-domain
  type: hard
builds-toward:
- gradient-vector
- directional-derivatives
tags:
- contour-maps
- level-sets
- visualization
stage: formal-systems
status: draft
---

# Contour Maps and Level Curves

## Core Idea
A level curve of f(x, y) is a curve where f(x, y) = c for constant c. Contour maps show families of level curves, like topographic maps where each contour represents constant elevation. Level curves are perpendicular to the gradient.

## Explainer

A multivariable function f(x, y) takes pairs of inputs to a single output — a surface hovering over the xy-plane when you graph it in 3D. But a 3D graph is hard to work with directly. A **contour map** (also called a level curve diagram) solves this by slicing the surface horizontally at different heights c and projecting the slices down to the xy-plane. Each slice gives you a curve in the plane along which the function is constantly equal to c — a **level curve** f(x, y) = c.

The topographic map is the perfect everyday analogy. Each contour line on a hiking map represents constant elevation: if you walk along one of those lines, you stay at the same altitude the whole time. The shape of the contours tells you about the terrain. Closely spaced contours mean the elevation is changing rapidly — a steep slope. Widely spaced contours mean gradual change — a gentle slope or a flat plain. Concentric closed curves (like the rings on a bull's-eye) indicate a peak or a valley depending on whether the labeled values increase or decrease toward the center.

Reading a contour map fluently is a key skill. To estimate f at a point (x, y), find which two labeled level curves the point falls between and interpolate. To understand the direction of steepest ascent, look for where the contours are most densely packed — the function changes fastest perpendicular to the level curves, in the direction of the **gradient vector** ∇f. This perpendicularity is not a coincidence: if you move along a level curve, f does not change, so the rate of change in that direction is zero. The gradient, which points in the direction of maximum increase, must therefore be perpendicular to every direction of zero change — it is orthogonal to the level curve at every point.

Level curves generalize immediately. A **level surface** of a function g(x, y, z) = c is a surface in 3D space where the function is constant — think of equipotential surfaces in electrostatics or isotherms in meteorology. The gradient ∇g is perpendicular to the level surface at each point, a fact that becomes essential when you need to find the tangent plane to an implicitly defined surface: the normal vector to f(x, y, z) = c at a point is simply ∇f evaluated at that point.

When you move from contour maps to directional derivatives and the gradient vector, you will find that every quantitative statement about rates of change in multivariable calculus connects back to the geometry of level curves. The gradient's direction is "across" the level curves (steepest ascent), its magnitude is how fast f changes per unit distance in that direction, and the level curves themselves are the geometric record of where f is constant. Building a clear mental image of contour diagrams now pays dividends throughout multivariable calculus and beyond.
