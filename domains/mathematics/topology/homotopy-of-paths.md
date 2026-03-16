---
id: homotopy-of-paths
title: Homotopy of Paths
domain: mathematics
course: topology
prerequisites:
- id: path-connectedness
  type: hard
- id: continuity-topological-spaces
  type: hard
builds-toward:
- fundamental-group-definition
tags:
- homotopy
- homotopic-paths
- path-deformation
stage: advanced
status: draft
---

# Homotopy of Paths

## Core Idea
Two paths are homotopic if one can be continuously deformed into the other while keeping endpoints fixed. This is an equivalence relation on paths, and the set of equivalence classes can be given a group structure (under concatenation) when the basepoint is fixed. Homotopy captures the intuition that topologically equivalent deformations preserve path structure.

## Explainer

From path-connectedness, you know that a space X is path-connected when any two points can be joined by a continuous path — a continuous map γ: [0, 1] → X with γ(0) = p and γ(1) = q. But path-connectedness only tells you that paths exist; it says nothing about how many "essentially different" paths there are. Homotopy is the tool for measuring that difference. Two paths α, β from p to q are **homotopic** (rel endpoints) if there exists a continuous map H: [0, 1] × [0, 1] → X such that H(t, 0) = α(t), H(t, 1) = β(t), H(0, s) = p, and H(1, s) = q for all t and s. Think of the second coordinate s as a "deformation parameter": at s = 0 you have the path α; at s = 1 you have the path β; in between, H(−, s) is a continuously varying family of paths, all sharing the same endpoints.

The geometric picture is immediate: imagine drawing two paths between the same two points on a piece of paper. You can always continuously deform one into the other by sliding it across the paper — the plane has no obstacles. Now imagine the same two paths on a surface with a hole (like an annulus, or the punctured plane ℝ² \ {0}). A path that loops around the hole and a path that does not loop around the hole cannot be deformed into each other without passing through the hole. Homotopy detects this topological obstruction. The paths live in the same space but belong to different **homotopy classes** — equivalence classes under the "can be continuously deformed" relation.

That homotopy is an equivalence relation (reflexive, symmetric, transitive) is a standard verification using the continuity you know from your second prerequisite: identity homotopies, reversals, and compositions of homotopies are all continuous. The deeper payoff is that homotopy classes of loops (paths with γ(0) = γ(1) = basepoint) can be composed by concatenation — traverse α then traverse β — and this composition is well-defined on equivalence classes. The resulting structure is the **fundamental group** π₁(X, p), the key invariant built in the next topic. The word "group" is justified because the concatenation operation has an identity (the constant loop at p) and inverses (the reverse path), with associativity holding up to homotopy.

The constraint that endpoints stay fixed throughout the deformation is essential and not merely technical. Without fixing endpoints, two paths between different pairs of points could be "homotoped" into each other in a connected space, losing all information. Fixing endpoints ensures homotopy measures how paths differ in their traversal of the space between two fixed points. This is the distinction between a free homotopy (endpoints can wander) and a homotopy rel endpoints, and in the context of the fundamental group, it is always the latter that matters. Every path has a homotopy class; those classes compose; and the resulting group carries deep information about the shape of the space — whether it has holes, handles, or other features that no amount of continuous deformation can remove.
