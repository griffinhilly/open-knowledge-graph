---
id: convergence-in-topology
title: Convergence in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: limit-points-and-accumulation
  type: hard
builds-toward:
- sequential-compactness
- continuous-functions-topology
tags:
- convergence
- sequences
stage: advanced
status: draft
---

# Convergence in Topological Spaces

## Core Idea
A sequence (xₙ) converges to x if every neighborhood of x contains all but finitely many terms. Unlike metric spaces, limits need not be unique in general topological spaces, and sequences alone cannot always describe the topology—nets or filters are sometimes necessary.

## Explainer

In a metric space, you said xₙ → x when the distances d(xₙ, x) → 0 — a numerical condition that uniquely pins down the limit. In a general topological space, there are no distances, only open sets. The topological definition replaces "distance less than ε" with "inside some open neighborhood": the sequence **(xₙ) converges to x** if for every open set U containing x, all but finitely many terms of the sequence lie in U. This is a direct translation: instead of "eventually within distance ε," you say "eventually inside every open neighborhood." When the topology comes from a metric, the two definitions agree exactly, since open balls form a neighborhood basis.

The loss of a metric introduces a phenomenon that never occurs in metric spaces: **non-uniqueness of limits**. In the **indiscrete topology** (only ∅ and the whole space X are open), every sequence converges to every point — because the only open set containing any point is all of X, which automatically contains all sequence terms. This seems pathological, but it is not a defect of the definition; it is a consequence of the topology being too coarse to separate points. In a **Hausdorff space** (also called T₂), any two distinct points have disjoint open neighborhoods, which forces limits to be unique: if xₙ → x and xₙ → y with x ≠ y, you can separate them by disjoint opens, which cannot both contain all but finitely many terms simultaneously. Uniqueness of limits is thus a property of the topology, not of convergence itself.

A deeper surprise is that **sequences are sometimes insufficient** to describe the topology. In a metric space, every topological property — continuity, closure, compactness — can be characterized in terms of sequences. In a general topological space, this fails. A point x may be a limit point of a set A (every open set around x meets A) without any sequence of points in A converging to x. This phenomenon occurs in spaces that are not first-countable (no countable neighborhood basis exists at x). The fix is to generalize sequences to **nets** (directed systems) or **filters**, which are indexed by more general ordered sets instead of the natural numbers. In a general topological space, x is in the closure of A if and only if some net from A converges to x — the sequence version requires first countability.

Understanding this progression — metric convergence → topological neighborhood convergence → nets and filters — reflects a broader theme in topology: the goal is to find the minimal structure needed for each concept. Sequences capture convergence perfectly in metric spaces because the countable naturals are rich enough to probe all open sets around a limit point. When open sets are structured differently, you need a more powerful indexing apparatus. This is why convergence in topology is not just a definition to memorize but a window into the difference between what "nearness" means in different mathematical contexts.


