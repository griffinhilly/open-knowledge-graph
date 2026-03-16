---
id: heine-borel-compact-sets
title: Heine-Borel Theorem
domain: mathematics
course: topology
prerequisites:
- id: compact-sets-definition
  type: hard
- id: compact-sets-heine-borel
  type: soft
builds-toward:
- compactness-hausdorff-spaces
tags:
- compactness
- characterization
stage: advanced
status: draft
---

# Heine-Borel Theorem

## Core Idea
In ℝⁿ with standard topology, a set is compact iff it is closed and bounded. This theorem does not generalize to all metric spaces (e.g., [0,∞) is closed but not compact), showing that compactness is truly a topological concept, not merely about boundedness.

## Explainer

You already know the abstract definition of compactness: a space is compact if every open cover has a finite subcover. That definition is powerful but opaque — given an arbitrary set in ℝⁿ, checking every possible open cover is infeasible. The **Heine-Borel Theorem** replaces this with a concrete geometric test: in ℝⁿ with its standard topology, a set K is compact if and only if it is **closed** and **bounded**. Closed means K contains all its limit points. Bounded means K fits inside some ball of finite radius. Both conditions are straightforward to verify.

Why do both conditions matter? Bounded alone is insufficient: the open interval (0, 1) is bounded, but the open cover {(1/n, 1) : n ≥ 2} has no finite subcover — the left endpoint 0 is the problem, and it's a limit point missing from the set. Closed alone is also insufficient: the entire real line ℝ is closed, but cover it with open intervals (−n, n) for n = 1, 2, 3, …; no finite subcollection covers all of ℝ. The combination — closed and bounded — is what traps sequences and covers simultaneously: boundedness prevents escape to infinity, and closedness ensures limit points are included.

The proof strategy illustrates the deep connection to Bolzano-Weierstrass. One direction (compact → closed and bounded) is relatively easy: compactness implies sequential compactness, which forces the set to contain its limit points (hence closed) and prohibits sequences escaping to infinity (hence bounded). The other direction (closed and bounded → compact) proceeds by enclosing K in a large closed box, showing the box is compact via iterated bisection, and noting that K as a closed subset of a compact set is itself compact.

The theorem's scope is limited to ℝⁿ, and this is no accident. In the space C([0,1]) of continuous functions with the sup norm, the closed unit ball {f : ‖f‖∞ ≤ 1} is closed and bounded but not compact — you can construct sequences of continuous functions with no convergent subsequence. Compactness is a topological property, not a geometric one, and "closed and bounded" is a special feature of finite-dimensional Euclidean space. In higher-dimensional and infinite-dimensional settings, you must work directly from the cover definition or use sequential compactness, which is why the abstract definition was necessary to learn first.
