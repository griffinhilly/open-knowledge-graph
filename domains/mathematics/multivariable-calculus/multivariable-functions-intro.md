---
id: multivariable-functions-intro
title: Functions of Several Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: functions-of-several-variables
  type: hard
- id: multivariable-limits
  type: hard
builds-toward:
- partial-derivatives
- continuity-multivariable
tags:
- functions
- multivariable
- level-sets
stage: formal-systems
status: draft
---

# Functions of Several Variables

## Core Idea
A multivariable function f: ℝⁿ → ℝ takes multiple inputs (x, y, z, …) and produces one output. The graph lives in ℝⁿ⁺¹. Level sets (contours) visualize f by showing where f takes constant values, like altitude on a map.

## Explainer

A single-variable function f: ℝ → ℝ takes one number and returns one number. Extending this to f: ℝⁿ → ℝ means accepting n numbers as input — a point (x₁, x₂, ..., xₙ) — and returning a single output value. The inputs form a point in n-dimensional space, and the output is a real number. Everything you know about functions of one variable (domain, range, limits, continuity, the idea of a function as a rule) carries over directly; only the domain gets larger. For two inputs, f(x, y) might represent temperature at point (x, y) on a flat plate, elevation at geographic coordinates, or pressure as a function of volume and temperature.

The **graph** of a two-variable function f(x, y) is the set of all points (x, y, f(x, y)) in three-dimensional space — a surface floating above (or passing through) the xy-plane. The height of the surface above each point (x, y) is the function's value there. For f(x, y) = x² + y², the graph is a paraboloid, bowl-shaped with its minimum at the origin. For f(x, y) = sin(x) cos(y), the graph is a wavy surface. You can think of it as drawing every (x, y, z) triple that satisfies z = f(x, y). For functions of three or more variables, the graph lives in four or more dimensions and can't be drawn, but the idea is the same.

**Level sets** — also called contour curves for two-variable functions — are the practical tool for visualizing functions you can't draw completely. A level set at value c is the set of all inputs where f equals c: {(x, y) : f(x, y) = c}. For elevation, level sets are exactly the contour lines on a topographic map — each contour line traces a path of constant altitude. For f(x, y) = x² + y², the level sets are circles centered at the origin (since x² + y² = c defines a circle of radius √c). Closely spaced level sets indicate a steep region; widely spaced ones indicate a gentle slope. This encoding is why engineers and scientists use contour plots routinely — they pack the information of a 3D surface into a 2D diagram.

From your study of multivariable limits, you already know that continuity in multiple variables is more subtle than in one variable: a function can approach a point along every straight-line path and still fail to have a limit (because different curved paths may give different values). This subtlety is why the formal definition of limit — requiring the function to approach the same value regardless of the path — is essential here. Multivariable functions are the setting for partial derivatives, gradients, and integration over regions, all of which you will build next. The intuition to develop now: a multivariable function is a machine that assigns a number to every point in a space, and level sets are the best way to see its overall shape.
