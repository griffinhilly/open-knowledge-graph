---
id: path-connected-spaces
title: Path Connected Spaces
domain: mathematics
course: topology
prerequisites:
- id: connected-spaces-definition
  type: hard
builds-toward:
- connected-components-decomposition
- homotopy-definition
tags:
- path-connected
- connectedness
stage: formal-systems
status: draft
---

# Path Connected Spaces

## Core Idea
A space is path-connected if for every two points x,y, there exists a continuous path γ: [0,1] → X with γ(0) = x and γ(1) = y. Path-connected implies connected, but not conversely (topologist's sine curve). Most natural 'nice' spaces that are connected are path-connected; path-connectivity is more intuitive and stronger.

## Explainer

From your study of connected spaces, you know that a topological space X is **connected** if it cannot be written as a disjoint union of two nonempty open sets. Connectedness captures a kind of "oneness" — the space cannot be split apart. But connectedness is defined in purely set-theoretic and topological terms, and it admits some counterintuitive examples. **Path-connectedness** offers a more geometric, hands-on version of the same intuition: a space is path-connected if you can draw a continuous curve between any two of its points without leaving the space.

Formally, a **path** from x to y is a continuous function γ: [0, 1] → X with γ(0) = x and γ(1) = y. The interval [0, 1] serves as the parameter domain — think of it as "time." At time 0 you are at x; at time 1 you are at y; at each intermediate time t you are at γ(t), continuously varying. The space X is **path-connected** if such a path exists for every pair of points. All of ℝⁿ is path-connected: the straight-line path γ(t) = (1−t)x + ty works. Open balls, spheres, and all manifolds you encounter in calculus are path-connected.

The relationship to connectedness is one-directional: **path-connected implies connected**, but not vice versa. The proof of the implication uses the intermediate value theorem in disguise — a continuous image of the connected space [0, 1] is connected, and if you can path-connect every pair of points, you can show X cannot be split. The classic counterexample to the converse is the **topologist's sine curve**: the closure of the graph of sin(1/x) for x > 0. This set is connected — it cannot be split into two separated open pieces — but there is no path from a point on the oscillating part to any point on the segment {0} × [−1, 1], because no continuous function can "cross" the accumulation behavior at x = 0.

For the spaces that arise naturally in analysis and geometry — open subsets of ℝⁿ, smooth manifolds, convex sets — path-connectedness and connectedness agree. The distinction matters most in algebraic topology, where path-connectedness is the right notion for defining the **fundamental group** and **homotopy theory**: the next topic you will study. Two paths from x to y that can be continuously deformed into each other represent the same "shape of connection," and comparing these shapes is how homotopy captures the topological holes and loops in a space.
