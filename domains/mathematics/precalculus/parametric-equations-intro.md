---
id: parametric-equations-intro
title: Introduction to Parametric Equations
domain: mathematics
course: precalculus
prerequisites:
- id: function-notation-review
  type: hard
- id: trigonometric-ratios-review
  type: soft
- id: conic-sections-overview
  type: soft
builds-toward:
- parametric-curves-calculus
- arc-length-parametric
tags:
- parametric
- curves
- coordinate-geometry
stage: formal-systems
status: validated
---
# Introduction to Parametric Equations

## Core Idea
Parametric equations define x and y as separate functions of a third variable t (the parameter), typically representing time: x = f(t), y = g(t). This lets you describe curves that fail the vertical line test, model motion with direction and speed, and separate horizontal and vertical components. Eliminating the parameter converts back to a rectangular equation when possible.

## How It's Best Learned
Start with linear motion (x = t, y = 2t + 1), then circles (x = cos(t), y = sin(t)), then more exotic curves. Plot by making a table of t, x, y values and connecting points in order. Practice eliminating the parameter algebraically. Emphasize that the parameter adds information (direction, speed) that a rectangular equation lacks.

## Common Misconceptions
- Forgetting that the parameter t is not necessarily time and can range over any interval.
- Losing information about direction of traversal when eliminating the parameter.
- Assuming parametric equations always trace a curve exactly once (they may retrace or only cover part of a curve).

## Explainer

In everything you have studied so far, curves have been described by equations relating x and y directly: y = x², x² + y² = 1, and so on. **Parametric equations** take a fundamentally different approach: instead of relating x and y to each other, they define both as separate functions of a third variable t, called the **parameter**. You write x = f(t), y = g(t), and as t varies over some interval, the point (x, y) traces out a curve in the plane. The parameter often represents time — at time t, the object is at position (f(t), g(t)) — but it can represent any quantity that drives the motion.

The simplest example is a circle: x = cos(t), y = sin(t) for 0 ≤ t ≤ 2π. As t increases from 0 to 2π, the point starts at (1, 0) and sweeps counterclockwise around the unit circle. Eliminating the parameter — using the identity cos²(t) + sin²(t) = 1 — gives x² + y² = 1, the familiar rectangular equation. But the rectangular equation loses critical information: it tells you the shape is a circle, but not where the tracing starts, which direction it goes, or how fast. The parametric form encodes all of this. If you changed the parametrization to x = cos(2t), y = sin(2t) for 0 ≤ t ≤ π, the shape would be the same circle, but traversed twice as fast.

One of the primary advantages of parametric equations is that they can describe curves that fail the vertical line test — curves that cannot be written as y = f(x). A circle, a figure eight, a spiral — none of these are functions of x, yet all have clean parametric descriptions. The parametric framework separates horizontal and vertical motion into independent components, which is exactly how physics models projectile motion: x(t) = v₀ cos(θ) · t handles horizontal displacement while y(t) = v₀ sin(θ) · t − ½gt² handles vertical displacement, and together they trace the parabolic path.

To **eliminate the parameter**, you solve one equation for t and substitute into the other, or use an identity. From x = t + 1 and y = t², solving the first gives t = x − 1, so y = (x − 1)². But be careful: the parameter range restricts which portion of the rectangular curve is actually traced. If t ∈ [0, 3], then x ranges from 1 to 4 and y from 0 to 9 — only part of the parabola. The rectangular equation y = (x − 1)² describes the entire parabola, so elimination can introduce points that the parametric curve never visits. This is why parametric equations carry strictly more information than their rectangular counterparts: they encode not just the shape, but the extent, direction, and speed of traversal.

## Questions

```yaml
- question: "A circle is described by x = cos(t), y = sin(t) for 0 ≤ t ≤ 2π. A student eliminates t to get x² + y² = 1 and says the two representations are equivalent. What information does the rectangular form lose?"
  type: multiple-choice
  options:
    - "The equation is only valid for positive x and y values"
    - "The circle's center and radius"
    - "The direction and starting point of traversal around the circle"
    - "The fact that the curve is closed"
  answer: 2
  explanation: "The rectangular form x² + y² = 1 describes the shape but nothing about how it is traversed. The parametric form tells you traversal starts at (1, 0) when t = 0 and proceeds counterclockwise. Direction of motion, starting point, and speed are all lost when you eliminate the parameter — which is why parametric form carries strictly more information than the rectangular equation for a curve."

- question: "Consider two parametric curves: C1: x = t², y = t for all real t; and C2: x = t², y = t for 0 ≤ t ≤ 1. Both eliminate to y² = x. Which statement is true?"
  type: multiple-choice
  options:
    - "Both curves are identical because they have the same rectangular equation"
    - "C1 traces the full parabola y² = x; C2 traces only the arc from (0, 0) to (1, 1)"
    - "The rectangular equation y² = x fails the vertical line test, so neither parametric form is valid"
    - "C1 traces the parabola twice because t can be negative"
  answer: 1
  explanation: "The parameter interval restricts which portion of the curve is traced. C1 (all real t) covers y ∈ (−∞, ∞) → the full right-side parabola. C2 (t ∈ [0, 1]) covers only y ∈ [0, 1], the upper arc from origin to (1, 1). Eliminating the parameter destroys this interval information, making two geometrically different curves look algebraically identical. Note: C1 does not retrace — each t gives a unique point because y = t uniquely determines t."

- question: "When you eliminate the parameter from a set of parametric equations to obtain a rectangular equation, the two representations always describe exactly the same set of points."
  type: true-false
  answer: false
  explanation: "The rectangular equation may describe more points than the parametric curve. The parameter's range restricts which portion of the implicit curve is actually traced. For example, x = t², y = t for t ≥ 0 gives only the upper half of y² = x, but the rectangular equation includes the lower half too. Elimination reveals the shape; the parameter range reveals the extent and direction of traversal."

- question: "A parametric curve x = f(t), y = g(t) can represent shapes that would fail the vertical line test as a function y = h(x)."
  type: true-false
  answer: true
  explanation: "Because x and y are defined independently as functions of t, multiple y-values can correspond to the same x-value. A circle (x = cos t, y = sin t) fails the vertical line test — x = 0 corresponds to both y = 1 and y = −1 — yet it is perfectly described parametrically. This is one of the primary advantages of parametric form: it handles multi-valued curves, loops, and spirals that rectangular equations cannot represent as functions."

- question: "Explain what additional information parametric equations provide, compared to a rectangular equation y = f(x), when describing the path of a moving object."
  type: short-answer
  answer: "Parametric equations encode not just the geometric path (which points are visited) but also direction of travel, speed at each moment (via dx/dt and dy/dt), the specific portion of a curve that is traced, and whether any part is retraced. A rectangular equation describes only the shape of the curve."
  explanation: "The parameter t acts as a timeline. Knowing x(t) and y(t) separately lets you compute velocity components, detect reversals (when dx/dt or dy/dt changes sign), find where speed is zero, and determine which branch of a multi-valued curve is being traced at each moment. For motion problems in physics and engineering, these properties are essential and are completely inaccessible from y = f(x) alone."
```
