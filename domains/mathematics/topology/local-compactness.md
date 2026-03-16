---
id: local-compactness
title: Local Compactness
domain: mathematics
course: topology
prerequisites:
- id: compact-spaces-open-covers
  type: hard
builds-toward:
- topological-manifolds-introduction
tags:
- local-compactness
- compact-neighborhoods
stage: advanced
status: draft
---

# Local Compactness

## Core Idea
A space is locally compact if every point has a compact neighborhood. Local compactness allows one-point compactification and enables many results from classical analysis to extend. Manifolds are locally compact, and the concept bridges finite-dimensional compactness with infinite-dimensional topology.

## Explainer

From your study of compact spaces and open covers, you know that compactness is a global condition: every open cover of the entire space has a finite subcover. **Local compactness** replaces this global demand with a pointwise one. A space X is **locally compact at a point x** if there exists a compact neighborhood of x — a compact set K containing an open set containing x. The space is **locally compact** if it is locally compact at every point.

The canonical example is ℝⁿ. The real line ℝ is not compact (the cover {(−n, n) : n ∈ ℕ} has no finite subcover), but every point x ∈ ℝ has a compact neighborhood: [x−1, x+1] is compact by the Heine-Borel theorem. So ℝ is locally compact but not compact. More generally, any open subset of ℝⁿ is locally compact, and any compact space is trivially locally compact (the whole space is a compact neighborhood of each point). An example that is neither: ℚ with the subspace topology from ℝ — it is not locally compact because no compact neighborhood of a rational number exists (compact subsets of ℚ have empty interior).

The most powerful consequence of local compactness in a Hausdorff space is the **one-point compactification** (Alexandroff compactification). Given a locally compact Hausdorff space X, adjoin a single extra point ∞ to form X* = X ∪ {∞}. Declare the topology on X* by keeping all the original open sets of X, and declaring a neighborhood of ∞ to be any set whose complement in X is compact. The result is compact: every open cover of X* either omits ∞ (covered by X's topology) or includes a neighborhood of ∞ whose complement is compact, reducing to a finite subcover. This construction turns ℝ into the circle S¹ and ℝ² into the 2-sphere S². Local compactness is exactly the hypothesis that ensures there are enough compact sets to build the topology around ∞ coherently — without it, the construction fails to produce a Hausdorff space.

Local compactness is also a cornerstone of integration theory beyond ℝⁿ. **Haar measure** — the canonical translation-invariant measure on locally compact groups — requires local compactness as an essential hypothesis; without compact neighborhoods, the averaging procedure used to construct the measure breaks down. For topological manifolds, local compactness is part of the definition: it ensures every point has a neighborhood homeomorphic to an open ball in ℝⁿ, connecting abstract topology to the finite-dimensional geometry you understand from calculus. Local compactness is the minimal condition under which the intuitions of classical analysis — that you can work locally in a small, controlled, "finite-feeling" region — remain valid in a general topological setting.
