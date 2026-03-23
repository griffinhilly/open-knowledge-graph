---
id: contour-maps
title: Contour Maps and Level Curves
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: level-sets-surfaces
  type: hard
- id: functions-of-several-variables
  type: hard
builds-toward:
- directional-derivatives-gradient
- partial-derivatives
- gradient-vector-properties
tags:
- contours
- level-curves
- visualization
stage: formal-systems
status: validated
---

# Contour Maps and Level Curves

## Core Idea
A contour map shows level curves of f(x, y) at equally spaced values on the xy-plane. Spacing between contours indicates steepness: close contours mean the function changes rapidly, while distant contours indicate gentle slopes. Contour maps are the primary tool for visualizing scalar fields.

## Questions

```yaml
- question: "A contour map of f(x, y) shows contours at values 0, 10, 20, and 30. In region A the contour lines are widely spaced; in region B they are tightly packed. What can you conclude?"
  type: multiple-choice
  options:
    - "Region B has larger output values than region A"
    - "The function changes more rapidly (steeper slope) in region B than in region A"
    - "Region A contains a local maximum of the function"
    - "The map has been drawn incorrectly — contour spacing should be uniform across the domain"
  answer: 1
  explanation: "The fundamental reading rule: contour spacing encodes steepness. Because output values are equally spaced (increments of 10), closely packed lines mean the function traverses 10 units of output over a short horizontal distance — steep slope. Widely spaced lines mean the same 10-unit change occurs over a long horizontal distance — gentle slope. Region B is steeper. Output value magnitude is not related to contour spacing: you cannot tell from spacing alone whether values are large or small."

- question: "Two contour lines on a contour map appear to intersect at a point P. What does this imply?"
  type: multiple-choice
  options:
    - "The function f(x, y) has a saddle point at P"
    - "The function achieves a local maximum at P"
    - "This is impossible — a single point (x, y) cannot have two different output values, so contour lines for distinct values can never cross"
    - "The function is not differentiable at P"
  answer: 2
  explanation: "Contour lines are level curves: each line represents all points where f equals a specific constant. If two contour lines with different values crossed at P, then f(P) would simultaneously equal both constants — a contradiction, since f is a function (one output per input). This is a strict geometric constraint: crossing contours are logically impossible for any well-defined function, not just for 'nice' functions. The topology of contour lines therefore directly encodes function structure."

- question: "On a contour map where output values increase toward the center, a series of nested closed loops converging inward indicates a local extremum at the center."
  type: true-false
  answer: true
  explanation: "Nested closed loops converging inward are the signature of a peak or bowl in the function surface. Each loop represents a level curve at a higher output value (if a maximum) or lower value (if a minimum); as you move inward the values increase or decrease monotonically until the extreme point at the center. This is one of the most useful pattern-recognition skills on contour maps: before doing any calculus, you can identify the rough locations of local maxima and minima just from the topology of the contour lines."

- question: "The gradient vector at any point on f(x, y) points along the nearest contour line in the direction of increasing values."
  type: true-false
  answer: false
  explanation: "The gradient vector points PERPENDICULAR to contour lines, in the direction of steepest ascent. Contour lines are curves of constant output — moving along a contour produces no change in f. The direction of maximum rate of change must therefore be perpendicular to constant-f curves. This perpendicularity relationship is one of the most important facts about gradients and will be essential when you study directional derivatives and optimization in this course."

- question: "Why do closely spaced contour lines indicate a steep slope? Use the equal-spacing property of contour values in your explanation."
  type: short-answer
  answer: "On a contour map, adjacent lines represent equally spaced output values — for example, increments of 10. The horizontal distance between those lines in the xy-plane represents how far you must travel to achieve that fixed output change. If the lines are closely spaced, you achieve the same 10-unit output change over a short horizontal distance: that is a steep slope. If the lines are widely spaced, the same 10-unit output change happens over a large horizontal distance: that is a gentle slope. The equal-spacing convention is what makes the spacing geometrically meaningful — it is the denominator in the rise-over-run ratio."
  explanation: "The insight is that the contour map compresses 3D information (rise and run) into a 2D diagram by fixing the 'rise' (equal output increments) and letting the 'run' (horizontal distance between lines) vary. Close spacing means small run for fixed rise — steep. Wide spacing means large run for fixed rise — gentle. This is exactly how topographic maps encode terrain steepness, and it transfers directly to the mathematical analysis of scalar fields."
```

## Explainer

From your work on functions of several variables, you know that f(x, y) produces a surface in three dimensions — a landscape over the xy-plane. From level sets, you know that setting f(x, y) = c defines a curve in the xy-plane: the set of all input points that produce the same output value c. A **contour map** (or topographic map) is simply a collection of these level curves drawn at regularly spaced output values — say f = 0, f = 10, f = 20, f = 30, and so on — all projected onto the same flat picture.

The fundamental reading rule is: **the spacing between contour lines encodes steepness**. Because the output values are equally spaced (say, increments of 10), curves that are close together in the xy-plane represent places where the function changes by 10 units over a short horizontal distance — a steep slope. Curves far apart represent places where the function traverses the same 10-unit output change over a much larger horizontal distance — a gentle slope. This is exactly how hikers read topographic maps: closely packed brown lines mean a steep climb; widely spaced lines mean easy walking.

Two geometric facts follow immediately. First, **contour lines never cross**. If they did, a single point (x, y) would have two output values simultaneously, which contradicts the definition of a function. Second, contour lines either form **closed loops** (if the function has a peak or bowl) or extend to the boundary of the domain. A series of nested closed loops converging inward signals a local maximum or minimum at the center; a pattern of curves crossing without closing signals a saddle point. Even before you know calculus, you can identify the rough locations of critical points just from the topology of the contour map.

Contour maps are indispensable because they compress three-dimensional information into a two-dimensional diagram. You will use them throughout multivariable calculus: the gradient vector (coming soon) always points in the direction perpendicular to contour lines, in the direction of steepest ascent. Optimization amounts to finding peaks and valleys in the contour map. Constrained optimization (Lagrange multipliers, later) asks where a constraint curve is tangent to a contour. Learning to read and sketch contour maps fluently is one of the most transferable visualization skills in all of applied mathematics.
