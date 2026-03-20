---
id: closure-interior-boundary
title: Closure, Interior, and Boundary of Sets
domain: mathematics
course: topology
prerequisites:
- id: closed-sets-topology
  type: hard
- id: open-sets-topology
  type: hard
builds-toward:
- limit-points-and-accumulation
- continuous-functions-topology
tags:
- closure
- interior
- boundary
stage: formal-systems
status: draft
---

# Closure, Interior, and Boundary of Sets

## Core Idea
For a set A: the closure Ā is the smallest closed set containing A; the interior A° is the largest open set contained in A; the boundary ∂A = Ā \ A°. These are fundamental closure operators in topology.

## Explainer

From your work with open and closed sets, you know that a set can be open, closed, both, or neither — and that open and closed are not opposites in topology. The trio of **closure**, **interior**, and **boundary** gives you a precise vocabulary for describing how any set sits inside its ambient space, regardless of whether the set itself is open or closed.

Start with the **interior** A°. A point x is in A° if there exists an open set U with x ∈ U ⊆ A — in other words, x is "surrounded" by A, with a whole open neighborhood fitting inside A. The interior is the largest open set contained in A. Think of A = [0,1] in ℝ: the interior is (0,1), because every point strictly between 0 and 1 has a small open interval around it still inside [0,1], but 0 and 1 do not. The interior captures the "purely inside" part of A.

The **closure** Ā adds to A all points that are "limit points" — every open neighborhood of x intersects A. Equivalently, Ā is the smallest closed set containing A. For A = (0,1), the closure is [0,1]: the endpoints 0 and 1 are limit points because every open interval around them overlaps with (0,1). The closure captures A together with everything it is "trying to approach." A set is closed if and only if it equals its own closure.

The **boundary** ∂A = Ā \ A° consists of points that are in the closure but not the interior — points where every open neighborhood intersects both A and its complement. For A = (0,1), the boundary is {0, 1}. Boundary points are "on the edge": you cannot put an open ball around them that stays entirely inside A or entirely outside A. Notice that ∂A is always a closed set (as the difference of two closed sets), and that X is partitioned into three disjoint pieces: A°, ∂A (intersected with A and its complement), and the exterior (interior of the complement). These three operators together give a complete topological decomposition of how A relates to the ambient space, and they arise constantly in continuity proofs and limit point arguments that build on this foundation.
