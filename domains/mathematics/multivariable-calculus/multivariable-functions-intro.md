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

## Questions

```yaml
- question: "On a topographic map, contour lines (level sets of elevation) are packed closely together on one side of a mountain and spread widely apart on the other. What does this tell you about the terrain?"
  type: multiple-choice
  options:
    - "The packed side has lower elevation and the spread side has higher elevation"
    - "The packed side is steeper and the spread side has a gentler slope"
    - "The map is inaccurate — contour spacing should be uniform"
    - "The packed side has more surface area than the spread side"
  answer: 1
  explanation: "Contour lines are level sets of elevation — each line connects points at the same height. Closely packed contours mean many level sets in a small horizontal distance: elevation changes rapidly, indicating a steep slope. Widely spaced contours mean elevation changes slowly — a gentle grade. This is exactly why topographic maps are useful: contour spacing encodes steepness in a 2D diagram without requiring a 3D drawing."

- question: "Why can't we draw the graph of f(x, y, z) the way we draw the graph of f(x, y)?"
  type: multiple-choice
  options:
    - "Three-variable functions are not well-defined mathematically without additional constraints"
    - "The graph of f(x, y, z) would require four dimensions — three inputs plus one output — which cannot be visualized"
    - "Three-variable functions only have level sets, not graphs"
    - "The computational complexity makes it impractical"
  answer: 1
  explanation: "The graph of f(x, y) is the set of points (x, y, f(x,y)) in 3D space — one dimension beyond the 2D domain. For f(x, y, z), the graph would be points (x, y, z, f(x,y,z)) in 4D space, which cannot be embedded in our 3D world. This is why level sets become essential: the level set f(x, y, z) = c is a surface in 3D space, which can be visualized — giving us useful 3D snapshots of an inherently 4D object."

- question: "The level set of f(x, y) = x² + y² at the value c = 9 is a circle of radius 3 centered at the origin."
  type: true-false
  answer: true
  explanation: "The level set at c = 9 is all (x, y) satisfying x² + y² = 9, which is by definition a circle of radius √9 = 3. This illustrates how level sets reduce a surface to curves: instead of the full paraboloid z = x² + y², each level set gives one ring at a specific height. Circular level sets tell you the function is radially symmetric — its value depends only on the distance from the origin."

- question: "To verify that a multivariable function has a limit at a point, it is sufficient to check that the limit is the same along every straight-line path through that point."
  type: true-false
  answer: false
  explanation: "This is a dangerous misconception. A multivariable limit requires the function to approach the same value along ALL paths — not just straight lines. Functions exist where every straight-line limit yields the same value, yet curved paths give a different value, so the true limit fails to exist. The classic example: f(x, y) = x²y/(x⁴ + y²) has limit 0 along every line through the origin, but limit 1/2 along the parabolic path y = x². Checking only straight lines is insufficient."

- question: "Why are level sets a more useful visualization tool for f(x, y) than attempting to describe the graph of f directly?"
  type: short-answer
  answer: "The graph of f(x, y) is a surface in 3D space, which is hard to read precisely from a static 2D drawing. Level sets project information onto the 2D domain: each curve shows all points where f takes a specific value, and the spacing between curves encodes the rate of change. This produces a complete, readable picture — like a topographic map — without the distortion of a 3D projection. Level sets also generalize to three-variable functions, where the graph is 4-dimensional but level sets are 3D surfaces."
  explanation: "The level-set representation packs full information about a function's behavior into a 2D diagram. Engineers and scientists use contour plots routinely for this reason. The technique generalizes: for f(x, y, z), the graph lives in 4D and is impossible to visualize, but level surfaces f(x, y, z) = c are 3D objects that can be rendered and analyzed."
```

## Explainer

A single-variable function f: ℝ → ℝ takes one number and returns one number. Extending this to f: ℝⁿ → ℝ means accepting n numbers as input — a point (x₁, x₂, ..., xₙ) — and returning a single output value. The inputs form a point in n-dimensional space, and the output is a real number. Everything you know about functions of one variable (domain, range, limits, continuity, the idea of a function as a rule) carries over directly; only the domain gets larger. For two inputs, f(x, y) might represent temperature at point (x, y) on a flat plate, elevation at geographic coordinates, or pressure as a function of volume and temperature.

The **graph** of a two-variable function f(x, y) is the set of all points (x, y, f(x, y)) in three-dimensional space — a surface floating above (or passing through) the xy-plane. The height of the surface above each point (x, y) is the function's value there. For f(x, y) = x² + y², the graph is a paraboloid, bowl-shaped with its minimum at the origin. For f(x, y) = sin(x) cos(y), the graph is a wavy surface. You can think of it as drawing every (x, y, z) triple that satisfies z = f(x, y). For functions of three or more variables, the graph lives in four or more dimensions and can't be drawn, but the idea is the same.

**Level sets** — also called contour curves for two-variable functions — are the practical tool for visualizing functions you can't draw completely. A level set at value c is the set of all inputs where f equals c: {(x, y) : f(x, y) = c}. For elevation, level sets are exactly the contour lines on a topographic map — each contour line traces a path of constant altitude. For f(x, y) = x² + y², the level sets are circles centered at the origin (since x² + y² = c defines a circle of radius √c). Closely spaced level sets indicate a steep region; widely spaced ones indicate a gentle slope. This encoding is why engineers and scientists use contour plots routinely — they pack the information of a 3D surface into a 2D diagram.

From your study of multivariable limits, you already know that continuity in multiple variables is more subtle than in one variable: a function can approach a point along every straight-line path and still fail to have a limit (because different curved paths may give different values). This subtlety is why the formal definition of limit — requiring the function to approach the same value regardless of the path — is essential here. Multivariable functions are the setting for partial derivatives, gradients, and integration over regions, all of which you will build next. The intuition to develop now: a multivariable function is a machine that assigns a number to every point in a space, and level sets are the best way to see its overall shape.
