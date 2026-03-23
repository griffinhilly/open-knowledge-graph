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
status: validated
---

# Contour Maps and Level Curves

## Core Idea
A level curve of f(x, y) is a curve where f(x, y) = c for constant c. Contour maps show families of level curves, like topographic maps where each contour represents constant elevation. Level curves are perpendicular to the gradient.

## Questions

```yaml
- question: "On a contour map of f(x, y), you are at a point between the level curves labeled f = 4 and f = 6. Contours to your east are closely spaced; contours to your north are widely spaced. In which direction does f increase most rapidly from your position?"
  type: multiple-choice
  options:
    - "North, because widely spaced contours indicate gradual change and the gradient favors that direction"
    - "East, because closely spaced contours indicate rapid change, and the gradient points perpendicular to them toward higher values"
    - "Along the level curve, because moving parallel to the contour preserves the maximum gradient"
    - "Upward out of the plane, because contour maps do not encode direction in the xy-plane"
  answer: 1
  explanation: "Closely spaced contours indicate that the function changes rapidly over a short distance — a steep slope. The gradient points perpendicular to the level curves toward higher values. Since contours are closely packed to the east, the function changes fastest in the east-west direction, and east is toward the higher values. Option C describes a direction of zero change (along the level curve), not maximum change."

- question: "Two hikers study a topographic map. Hiker A says the gradient points along the contour lines. Hiker B says the gradient points perpendicular to the contour lines, toward higher elevation. Who is correct?"
  type: multiple-choice
  options:
    - "Hiker A — the gradient indicates the direction of travel along constant elevation"
    - "Hiker B — the gradient is perpendicular to level curves and points in the direction of steepest ascent"
    - "Both — the gradient has components both along and perpendicular to the contours"
    - "Neither — the gradient is a scalar, not a direction"
  answer: 1
  explanation: "Hiker B is correct. The gradient ∇f at a point points in the direction of maximum increase of f and is perpendicular (orthogonal) to the level curve through that point. Moving along a level curve means f doesn't change, so the directional derivative in that direction is zero. The gradient, pointing in the direction of maximum increase, must be orthogonal to every direction of zero change — it cannot have any component along the level curve."

- question: "The gradient vector at a point on a contour map is parallel to the level curve passing through that point."
  type: true-false
  answer: false
  explanation: "The gradient is perpendicular to the level curve, not parallel to it. Moving along a level curve means the function value stays constant, so the directional derivative in that direction is zero. The gradient points in the direction of maximum increase, which must be orthogonal to all directions of zero change. A gradient parallel to a level curve would mean the function's maximum rate of change is in a direction where f doesn't change — a contradiction."

- question: "Walking along a level curve of f(x, y) keeps the value of f constant throughout the walk."
  type: true-false
  answer: true
  explanation: "By definition, a level curve is the set of all points (x, y) where f(x, y) = c for a fixed constant c. Any path that stays on this curve maintains the same function value. This is exactly why level curves are useful: they map out the 'terrain' of a function by showing where it is constant, analogous to contour lines on a topographic map showing constant elevation."

- question: "Why must the gradient vector ∇f be perpendicular to the level curve of f at every point?"
  type: short-answer
  answer: "The gradient points in the direction of maximum rate of increase of f. A level curve is the set of points where f is constant — moving along the level curve produces zero change in f, so the directional derivative in any direction tangent to the level curve is zero. Since the gradient is the direction of maximum increase, it cannot have any component in a direction of zero change — it must be entirely orthogonal to the level curve."
  explanation: "This perpendicularity is one of the most important geometric facts in multivariable calculus. It connects the algebraic gradient to the geometric level curve in a precise way, and it underlies the formula for finding normal vectors to implicitly defined surfaces: the gradient of F(x,y,z) at a point on the surface F=c gives a vector normal to that surface. Building this geometric intuition now makes directional derivatives, the gradient, and tangent planes all follow naturally."
```

## Explainer

A multivariable function f(x, y) takes pairs of inputs to a single output — a surface hovering over the xy-plane when you graph it in 3D. But a 3D graph is hard to work with directly. A **contour map** (also called a level curve diagram) solves this by slicing the surface horizontally at different heights c and projecting the slices down to the xy-plane. Each slice gives you a curve in the plane along which the function is constantly equal to c — a **level curve** f(x, y) = c.

The topographic map is the perfect everyday analogy. Each contour line on a hiking map represents constant elevation: if you walk along one of those lines, you stay at the same altitude the whole time. The shape of the contours tells you about the terrain. Closely spaced contours mean the elevation is changing rapidly — a steep slope. Widely spaced contours mean gradual change — a gentle slope or a flat plain. Concentric closed curves (like the rings on a bull's-eye) indicate a peak or a valley depending on whether the labeled values increase or decrease toward the center.

Reading a contour map fluently is a key skill. To estimate f at a point (x, y), find which two labeled level curves the point falls between and interpolate. To understand the direction of steepest ascent, look for where the contours are most densely packed — the function changes fastest perpendicular to the level curves, in the direction of the **gradient vector** ∇f. This perpendicularity is not a coincidence: if you move along a level curve, f does not change, so the rate of change in that direction is zero. The gradient, which points in the direction of maximum increase, must therefore be perpendicular to every direction of zero change — it is orthogonal to the level curve at every point.

Level curves generalize immediately. A **level surface** of a function g(x, y, z) = c is a surface in 3D space where the function is constant — think of equipotential surfaces in electrostatics or isotherms in meteorology. The gradient ∇g is perpendicular to the level surface at each point, a fact that becomes essential when you need to find the tangent plane to an implicitly defined surface: the normal vector to f(x, y, z) = c at a point is simply ∇f evaluated at that point.

When you move from contour maps to directional derivatives and the gradient vector, you will find that every quantitative statement about rates of change in multivariable calculus connects back to the geometry of level curves. The gradient's direction is "across" the level curves (steepest ascent), its magnitude is how fast f changes per unit distance in that direction, and the level curves themselves are the geometric record of where f is constant. Building a clear mental image of contour diagrams now pays dividends throughout multivariable calculus and beyond.
