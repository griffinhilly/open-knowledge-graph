---
id: closure-interior-and-boundary
title: Closure, Interior, and Boundary
domain: mathematics
course: topology
prerequisites:
- id: closed-sets-in-topological-spaces
  type: hard
builds-toward:
- limit-points-convergence-topology
- interior-closure-operators
tags:
- closure
- interior
- boundary
- derived-sets
stage: advanced
status: draft
---

# Closure, Interior, and Boundary

## Core Idea
For a set A in a topological space, the closure is the smallest closed set containing A, the interior is the largest open set contained in A, and the boundary consists of points in the closure but not the interior. These three operations decompose the space into three disjoint pieces relative to any subset and are fundamental to understanding local structure.

## Explainer

Work first with the concrete example of an open disk in the plane: A = {(x, y) : x² + y² < 1}, the open unit disk. You already know what it means for a set to be closed (it contains all its limit points). The **interior** of A is the largest open set contained within A — here, it's A itself, because A is already open. The **closure** of A is the smallest closed set containing A — here, it's the closed disk {(x, y) : x² + y² ≤ 1}, which adds the boundary circle. The **boundary** of A is what's left: the circle {(x, y) : x² + y² = 1}. Every point of the plane belongs to exactly one of these three zones relative to A: the interior (strictly inside), the boundary (on the edge), or the exterior (strictly outside). Together they partition the whole space.

Each operation has a clean characterization in terms of neighborhoods. A point p is in the **interior** of A if some open neighborhood of p fits entirely inside A — you can step in any direction a little bit and stay in A. A point p is in the **closure** of A if every open neighborhood of p intersects A — no matter how small a neighborhood you take, it touches A. A **boundary point** satisfies both: every neighborhood intersects A and intersects the complement of A. Boundary points are precisely the points where A and its complement touch.

These definitions extend uniformly to any topological space, not just ℝ² with its familiar geometry. This is the power of the topological framework you've been building: the same concepts apply to function spaces, discrete topologies, or anything else equipped with a notion of open sets. Notice also that the interior and closure are "dual" operations: the interior of A is the complement of the closure of the complement of A. This algebraic relationship means you rarely need to define both separately — one determines the other.

A crucial subtlety: the closure of an open set is not always obtained by simply "closing it up." Consider A = (0, 1) ∪ (2, 3) in ℝ. Its closure is [0, 1] ∪ [2, 3] — two disjoint closed intervals, not one connected set. The boundary consists of {0, 1, 2, 3}. None of the topology's global structure is assumed; everything follows from which sets are declared open. Mastering these three operators gives you the vocabulary to describe local structure — how a set sits in its ambient space — and is prerequisite to discussing continuity, limit points, and compactness in the full generality of topology.
