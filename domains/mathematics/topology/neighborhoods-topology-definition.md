---
id: neighborhoods-topology-definition
title: Neighborhoods and Neighborhood Bases
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
builds-toward:
- continuity-topological-definition
- limit-points-topology-definition
tags:
- neighborhoods
- local-structure
stage: abstract-reasoning
status: draft
---

# Neighborhoods and Neighborhood Bases

## Core Idea
A neighborhood of a point x is any set N containing an open set U with x ∈ U. A neighborhood base at x is a collection {Bᵢ} of neighborhoods such that every neighborhood of x contains some Bᵢ. Neighborhoods encode local topological structure; a set is open iff it is a neighborhood of each of its points.

## Explainer

Open sets, from your prerequisite, are defined globally: a set is either in the topology or it isn't. **Neighborhoods** reframe the same information locally — they let you talk about "what the space looks like near this particular point" without specifying the whole topology at once. A neighborhood of x is any set N that contains an open set U with x ∈ U ⊆ N. The key flexibility is that N itself need not be open: the closed interval [0.9, 1.1] is a neighborhood of 1 in ℝ, because the open interval (0.95, 1.05) sits inside it and contains 1. Neighborhoods are "open sets with wiggle room" — they absorb boundaries without losing the local information.

The equivalence "U is open iff U is a neighborhood of each of its points" is not a definition but a theorem, and it repackages the definition of open sets in local terms. If U is open and x ∈ U, then U itself witnesses that U is a neighborhood of x. Conversely, if every point of U has some open set around it inside U, you can take the union of all these open sets to reconstruct U itself — so U is open. This local characterization is useful because it lets you prove openness point by point, which is often easier than verifying the global condition directly.

A **neighborhood base** (local base) at x is a collection {Bᵢ} of neighborhoods of x such that every neighborhood of x contains some Bᵢ. In a metric space, the open balls {B(x, 1/n) : n ∈ ℕ} form a countable neighborhood base at every point: any neighborhood of x must contain some ball, and you only need to check ball-sized neighborhoods to understand the local structure completely. Spaces where every point has a *countable* neighborhood base are called **first-countable**; all metric spaces are first-countable. This property is important because first-countability is exactly what allows sequences to detect topological structure — a point x is in the closure of A if and only if some sequence in A converges to x. In spaces that fail first-countability, sequences are insufficient and the more general tools of nets or filters are required.

Neighborhoods provide the sharpest formulation of **continuity at a point**. A function f: X → Y is continuous at x if and only if for every neighborhood V of f(x), there is a neighborhood U of x with f(U) ⊆ V. Compare this to the ε-δ definition from calculus: ε defines a neighborhood (x − ε, x + ε) of the output, and δ defines a neighborhood (x − δ, x + δ) of the input. The neighborhood version is identical in structure but works in any topological space with no distance function needed. This is how the intuition from calculus carries over wholesale into the abstract setting.
