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
builds-toward:
  - parametric-curves-calculus
  - arc-length-parametric
tags: [parametric, curves, coordinate-geometry]
stage: formal-systems
status: draft
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
