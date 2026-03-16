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
status: draft
---

# Contour Maps and Level Curves

## Core Idea
A contour map shows level curves of f(x, y) at equally spaced values on the xy-plane. Spacing between contours indicates steepness: close contours mean the function changes rapidly, while distant contours indicate gentle slopes. Contour maps are the primary tool for visualizing scalar fields.

## Explainer

From your work on functions of several variables, you know that f(x, y) produces a surface in three dimensions — a landscape over the xy-plane. From level sets, you know that setting f(x, y) = c defines a curve in the xy-plane: the set of all input points that produce the same output value c. A **contour map** (or topographic map) is simply a collection of these level curves drawn at regularly spaced output values — say f = 0, f = 10, f = 20, f = 30, and so on — all projected onto the same flat picture.

The fundamental reading rule is: **the spacing between contour lines encodes steepness**. Because the output values are equally spaced (say, increments of 10), curves that are close together in the xy-plane represent places where the function changes by 10 units over a short horizontal distance — a steep slope. Curves far apart represent places where the function traverses the same 10-unit output change over a much larger horizontal distance — a gentle slope. This is exactly how hikers read topographic maps: closely packed brown lines mean a steep climb; widely spaced lines mean easy walking.

Two geometric facts follow immediately. First, **contour lines never cross**. If they did, a single point (x, y) would have two output values simultaneously, which contradicts the definition of a function. Second, contour lines either form **closed loops** (if the function has a peak or bowl) or extend to the boundary of the domain. A series of nested closed loops converging inward signals a local maximum or minimum at the center; a pattern of curves crossing without closing signals a saddle point. Even before you know calculus, you can identify the rough locations of critical points just from the topology of the contour map.

Contour maps are indispensable because they compress three-dimensional information into a two-dimensional diagram. You will use them throughout multivariable calculus: the gradient vector (coming soon) always points in the direction perpendicular to contour lines, in the direction of steepest ascent. Optimization amounts to finding peaks and valleys in the contour map. Constrained optimization (Lagrange multipliers, later) asks where a constraint curve is tangent to a contour. Learning to read and sketch contour maps fluently is one of the most transferable visualization skills in all of applied mathematics.
