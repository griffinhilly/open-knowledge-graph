---
id: limit-points-and-accumulation
title: Limit Points and Accumulation Points
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
- sequences-convergence-topology
- closed-sets-topology
tags:
- limit-points
- convergence
stage: abstract-reasoning
status: draft
---

# Limit Points and Accumulation Points

## Core Idea
A point x is a limit point of a set A if every open set containing x contains a point of A other than x itself. The closure of A equals A union its limit points. This characterizes closed sets.

## Explainer

You already know what **open sets** are in a topological space: sets that are "open" in the sense that every point has a neighborhood entirely contained within them. With that in hand, you can make precise what it means for a set to have "nearby" points accumulating around a given location. A point x is a **limit point** (also called an **accumulation point**) of a set A if every open set containing x also contains at least one point of A that is different from x itself.

Notice the phrasing carefully: *different from x itself*. This rules out the trivial case where x is isolated in A — a point that has some open neighborhood containing no other point of A. An isolated point is in A, but A doesn't "pile up" around it. A limit point may or may not belong to A; what matters is that A approaches x arbitrarily closely. In ℝ with the usual topology, every point of the interval (0, 1) is a limit point, and so are the endpoints 0 and 1 — even though 0 and 1 are not in the open interval itself. The sequence 1/n approaches 0, so every open set around 0 contains infinitely many points of the set {1, 1/2, 1/3, ...}, making 0 a limit point of that set.

The **closure** of a set A is defined as A together with all its limit points: A̅ = A ∪ A'. This is the smallest closed set containing A — adding the limit points fills in the "edges" that A is approaching. A set is **closed** if and only if it contains all its limit points, equivalently, if A = A̅. This is why [0, 1] is closed but (0, 1) is not: the open interval is missing its limit points 0 and 1. A closed set has "captured" everything that accumulates inside it.

Limit points let you connect the topology's open-set language to the analyst's intuition about limits of sequences. In a metric space, x is a limit point of A if and only if there exists a sequence of distinct points in A converging to x. In general topological spaces — where sequences may not capture all convergence behavior — the open-set definition of limit point is the correct generalization. This distinction matters when you move to spaces where first-countability fails and sequences must be replaced by nets or filters. But for the metric-space contexts you will encounter most often, the intuition is exactly right: a limit point is a point that A gets arbitrarily close to, a target that sequences in A can converge toward.
