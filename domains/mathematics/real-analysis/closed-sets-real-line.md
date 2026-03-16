---
id: closed-sets-real-line
title: Closed Sets on the Real Line
domain: mathematics
course: real-analysis
prerequisites:
- id: open-sets-real-line
  type: hard
builds-toward:
- compact-sets
- connected-sets
tags:
- closed-sets
- topology
- complements
stage: advanced
status: draft
---

# Closed Sets on the Real Line

## Core Idea
A set F ⊆ ℝ is closed if its complement ℝ ∖ F is open, equivalently, if it contains all its limit points (a ∈ F whenever some sequence from F converges to a). Closed sets are dual to open sets: finite unions of closed sets are closed, and arbitrary intersections of closed sets are closed.

## Explainer

From your study of open sets, you know that open sets are "inward-looking" — every point in an open set has a neighborhood that stays inside the set, so no point of an open set is on its boundary. Closed sets are defined as the complements of open sets, which immediately gives them a dual structure. Every theorem about open sets has a mirror image for closed sets, with unions and intersections swapped, and finite and arbitrary swapped.

The most important characterization of closed sets is the **limit point criterion**: a set F is closed if and only if it contains all of its limit points. A **limit point** of F is any point x (possibly in F, possibly not) such that every open interval around x contains a point of F other than x itself — in other words, points of F can get arbitrarily close to x. The closed interval [a, b] contains all its limit points because sequences from [a, b] converge to values in [a, b]; the open interval (a, b) fails this because sequences approaching a or b from the inside converge to points not in the set. The set {1/n : n ∈ ℕ} is not closed: the sequence 1, 1/2, 1/3, … converges to 0, but 0 is not in the set. Adding 0 to form {0} ∪ {1/n : n ≥ 1} makes it closed.

The intersection/union rules are the exact dual of what you know for open sets. Arbitrary intersections of closed sets are closed (the intersection of any collection of closed sets, even infinitely many, is closed), but only finite unions of closed sets are guaranteed to be closed. The classic counterexample for infinite unions: each singleton {1/n} is closed (any finite set is closed), but their union {1/n : n ≥ 1} is not closed, as shown above. This asymmetry mirrors the fact that open sets are closed under arbitrary unions but only finite intersections.

These duality rules have real consequences for analysis. When you need a set that is automatically closed — for instance, to take a limit of a sequence and know the limit stays inside — closed sets are the right setting. The interplay between open and closed sets is the foundation for compactness (every open cover has a finite subcover), which you will study next. A crucial distinction: despite the names, "not open" does not mean "closed," and "not closed" does not mean "open." The interval [0, 1) is neither open nor closed, and ℝ itself is both open and closed in the standard topology.
