---
id: path-connectedness
title: Path Connectedness
domain: mathematics
course: topology
prerequisites:
- id: connectedness-definition-examples
  type: hard
- id: continuous-functions-topology
  type: soft
builds-toward:
- homotopy-of-paths
- fundamental-group-definition
tags:
- path-connectedness
- paths
- arcs
stage: advanced
status: draft
---

# Path Connectedness

## Core Idea
A space is path-connected if any two points can be joined by a continuous path (image of a continuous map from [0,1]). Path-connectedness implies connectedness but not conversely. It provides a more intuitive and constructive notion of connectedness amenable to algebraic topology.

## Explainer

You already know that a topological space is **connected** if it cannot be split into two disjoint nonempty open sets. That is a "global" condition — it says the space has no partition of a certain kind. **Path-connectedness** gives a "local-to-global" version that is often easier to work with and closer to geometric intuition: a space X is path-connected if for every pair of points p, q ∈ X, there exists a continuous function γ : [0, 1] → X with γ(0) = p and γ(1) = q. The function γ is called a **path** from p to q. The image γ([0, 1]) is a continuous arc connecting the two points within X.

The interval [0, 1] is the standard parameter space for paths because it is compact, connected, and conveniently normalizes endpoints to 0 and 1. A path is not a route — it is a function, so it can double back on itself, slow down, or even be constant. What matters is continuity: no teleportation allowed. Any two points in ℝⁿ can be joined by a straight-line path γ(t) = (1−t)p + tq, so ℝⁿ is path-connected. Any convex set is path-connected for the same reason. Most spaces you have intuition for — spheres, tori, circles — are path-connected.

Path-connectedness implies connectedness, but the converse fails. The classic counterexample is the **topologist's sine curve**: the closure of the graph of sin(1/x) for x > 0. This set is connected — you cannot separate it into two open pieces — but it is not path-connected because no continuous path can cross from the oscillating part to the limit segment on the y-axis. The oscillation becomes infinitely rapid as x → 0, preventing any path from reaching the y-axis without "jumping." This example shows that connectedness is a weaker condition, and path-connectedness is the right hypothesis when you need to actually construct a path between points.

Path-connectedness is the entry point to **algebraic topology** because paths compose. If γ₁ goes from p to q and γ₂ goes from q to r, then concatenating them gives a path from p to r (reparametrize so γ₁ runs over [0, 1/2] and γ₂ over [1/2, 1]). The set of paths in a space, up to continuous deformation, organizes into algebraic structures — the **fundamental group** being the first. This is why path-connectedness is a prerequisite to homotopy theory: before asking how paths deform, you need to know paths exist between any two points.
