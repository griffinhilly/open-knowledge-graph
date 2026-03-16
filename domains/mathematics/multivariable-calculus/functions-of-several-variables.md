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
status: draft
---

# Functions of Several Variables: Definition and Domain

## Core Idea
A function of n variables is a rule f: D ⊆ ℝⁿ → ℝ mapping n-tuples (x₁, ..., xₙ) to real numbers. The domain D is the set of valid inputs; understanding domain restrictions (division by zero, logarithms, square roots) is essential in multivariable calculus.

## Explainer

From your single-variable background, a function f(x) takes one number and produces one number, and its domain is typically a subset of the real line — an interval or a union of intervals. A **function of several variables** generalizes this: f(x, y) takes a pair of numbers (a point in the plane ℝ²) and produces one number; f(x, y, z) takes a triple (a point in space ℝ³). The output is always a single real number. From your 3D coordinate systems prerequisite, you already work in ℝ³; now the function's output value becomes a "height" associated with each point, creating a surface above the xy-plane.

The **domain** of f is the set of all input tuples for which the formula makes sense. The same restrictions you know from single-variable calculus apply here — you cannot divide by zero, take even roots of negative numbers, or take logarithms of non-positive numbers — but now the restrictions define regions or curves in the plane rather than isolated points or intervals on the line. For instance, f(x, y) = √(1 − x² − y²) requires 1 − x² − y² ≥ 0, i.e., x² + y² ≤ 1: the domain is the closed unit disk. The formula g(x, y) = ln(x + y) requires x + y > 0: the domain is the half-plane above the line y = −x.

Visualizing f(x, y) as a surface is the key mental model. Imagine every point (x, y) in the domain as a location on a flat table, and the value f(x, y) as the height of the surface at that location. The surface z = f(x, y) lives in three-dimensional space: the inputs specify the horizontal position, and the output specifies the elevation. Functions of three variables f(x, y, z) cannot be graphed this way (it would require four dimensions), but they appear throughout physics as scalar fields — temperature, pressure, or electric potential at each point in space.

The **range** is the set of all output values f actually achieves over its domain. Identifying the range requires thinking about what output values the function can produce and which are impossible. This extends the single-variable skill of finding the range of f(x), but the geometry of the domain now matters more: a function may achieve its maximum and minimum only on the boundary, or not at all if the domain is open. Mastering domain and range for multivariable functions builds the foundation for limits, continuity, and partial derivatives — all of which require careful attention to which regions of the input plane are in play.
