---
id: functions-of-several-variables
title: 'Functions of Several Variables: Definition and Domain'
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: 3d-coordinate-systems
  type: hard
- id: function-notation-review
  type: hard
builds-toward:
- limits-continuity-multivariable
- partial-derivatives
- contour-maps
tags:
- multivariate-functions
- domain
- range
stage: formal-systems
status: validated
---

# Functions of Several Variables: Definition and Domain

## Core Idea
A function of n variables is a rule f: D ⊆ ℝⁿ → ℝ mapping n-tuples (x₁, ..., xₙ) to real numbers. The domain D is the set of valid inputs; understanding domain restrictions (division by zero, logarithms, square roots) is essential in multivariable calculus.

## Questions

```yaml
- question: "What is the domain of f(x, y) = √(9 − x² − y²)?"
  type: multiple-choice
  options:
    - "All (x, y) such that x² + y² ≤ 9 — the closed disk of radius 3"
    - "All (x, y) such that x² + y² < 9 — the open disk of radius 3"
    - "All (x, y) such that x² + y² > 9 — the exterior of the circle"
    - "All (x, y) with x ≥ 0 and y ≥ 0 — the first quadrant only"
  answer: 0
  explanation: "The square root requires its argument to be non-negative: 9 − x² − y² ≥ 0, which rearranges to x² + y² ≤ 9. This is the closed disk of radius 3 centered at the origin, including the boundary circle x² + y² = 9 (where the function equals 0). The domain is now a 2D region, not an interval — the key shift from single-variable to multivariable calculus."

- question: "A student claims that f(x, y, z) = x² + y² + z² can be visualized as a surface in 3D space, just like f(x, y) = x² + y² is visualized as a paraboloid surface. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Visualizing f(x, y, z) as a surface would require a 4th dimension for the output value, which cannot be drawn"
    - "f(x, y, z) is not a valid function because functions cannot accept more than two inputs"
    - "3D functions produce vector outputs, not scalar values, so surface visualization does not apply"
    - "The function f(x, y, z) = x² + y² + z² is not continuous and therefore cannot be graphed"
  answer: 0
  explanation: "f(x, y) can be visualized as a surface because the two inputs provide the horizontal position (x, y) and the output f provides the height z — three dimensions total. For f(x, y, z), the three inputs already fill 3D space, and the output value would require a 4th axis. The graph would live in ℝ⁴, which cannot be drawn. Functions of three variables instead appear as scalar fields — temperature, pressure, or potential — where the output value is associated with each point in space rather than graphed above it."

- question: "The domain of g(x, y) = ln(x + y) includes the point (−3, 5)."
  type: true-false
  answer: true
  explanation: "The natural logarithm requires a positive argument: x + y > 0. At (−3, 5), we have x + y = −3 + 5 = 2 > 0, so the point is in the domain. The domain of g is the half-plane above the line y = −x, i.e., all points where x + y > 0. Notice that the domain condition defines a region in the plane, not an interval on the number line — the key geometric shift when moving to functions of two variables."

- question: "A function of two variables f(x, y) maps points in ℝ² to points in ℝ², producing a two-component output."
  type: true-false
  answer: false
  explanation: "A function of several variables, as defined in multivariable calculus, maps n-tuples to a single real number: f: D ⊆ ℝⁿ → ℝ. So f(x, y) takes a point in ℝ² and produces one real number — not a pair of numbers. The function's value can be visualized as a 'height' at each point in the plane. A function that maps ℝ² → ℝ² would be a vector-valued function (or vector field), which is a different object entirely."

- question: "How does finding the domain of a two-variable function f(x, y) differ from finding the domain of a single-variable function f(x)? What geometric form do the domain restrictions typically take?"
  type: short-answer
  answer: "For a single-variable function, domain restrictions (such as no division by zero, no negative square roots) exclude isolated points or intervals from the real line, producing a domain that is a subset of ℝ¹. For f(x, y), the same types of algebraic restrictions — but applied to expressions involving both x and y — exclude entire curves or regions from the plane ℝ². For example, 'x − y ≠ 0' excludes the line y = x; 'x² + y² ≤ 1' defines a disk. The domain is now a 2D region, and describing it requires specifying curves and inequalities rather than isolated points."
  explanation: "This geometric shift is why multivariable calculus requires visualizing domains as regions in the plane rather than intervals on the number line. The boundary of the domain often plays a crucial role in optimization: a function may achieve its maximum or minimum on the boundary of its domain, not in the interior — which is why understanding domain geometry is foundational for partial derivatives and constrained optimization."
```

## Explainer

From your single-variable background, a function f(x) takes one number and produces one number, and its domain is typically a subset of the real line — an interval or a union of intervals. A **function of several variables** generalizes this: f(x, y) takes a pair of numbers (a point in the plane ℝ²) and produces one number; f(x, y, z) takes a triple (a point in space ℝ³). The output is always a single real number. From your 3D coordinate systems prerequisite, you already work in ℝ³; now the function's output value becomes a "height" associated with each point, creating a surface above the xy-plane.

The **domain** of f is the set of all input tuples for which the formula makes sense. The same restrictions you know from single-variable calculus apply here — you cannot divide by zero, take even roots of negative numbers, or take logarithms of non-positive numbers — but now the restrictions define regions or curves in the plane rather than isolated points or intervals on the line. For instance, f(x, y) = √(1 − x² − y²) requires 1 − x² − y² ≥ 0, i.e., x² + y² ≤ 1: the domain is the closed unit disk. The formula g(x, y) = ln(x + y) requires x + y > 0: the domain is the half-plane above the line y = −x.

Visualizing f(x, y) as a surface is the key mental model. Imagine every point (x, y) in the domain as a location on a flat table, and the value f(x, y) as the height of the surface at that location. The surface z = f(x, y) lives in three-dimensional space: the inputs specify the horizontal position, and the output specifies the elevation. Functions of three variables f(x, y, z) cannot be graphed this way (it would require four dimensions), but they appear throughout physics as scalar fields — temperature, pressure, or electric potential at each point in space.

The **range** is the set of all output values f actually achieves over its domain. Identifying the range requires thinking about what output values the function can produce and which are impossible. This extends the single-variable skill of finding the range of f(x), but the geometry of the domain now matters more: a function may achieve its maximum and minimum only on the boundary, or not at all if the domain is open. Mastering domain and range for multivariable functions builds the foundation for limits, continuity, and partial derivatives — all of which require careful attention to which regions of the input plane are in play.
