---
id: neighborhoods-and-open-sets
title: Neighborhoods and Open Sets
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
- limit-points-and-accumulation
- convergence-in-topology
tags:
- local
- neighborhoods
stage: advanced
status: draft
---

# Neighborhoods and Open Sets

## Core Idea
A neighborhood of point x is an open set containing x. Neighborhoods capture the intuition of 'regions around x.' Every topological space is determined by the neighborhood structure: two topologies are equal iff they assign the same neighborhoods to every point. Neighborhoods enable local analysis of topological spaces.

## Explainer

From your study of open sets in topology, you know that a topology on a space X is defined by specifying which subsets are "open," subject to the axioms (X and ∅ are open; arbitrary unions of open sets are open; finite intersections of open sets are open). A **neighborhood** of a point x is simply any open set that contains x. This seemingly minor repackaging — going from "open sets of the space" to "open sets around a point" — is a conceptual shift from global to local analysis.

Why is the local perspective useful? Because most of the properties we care about in analysis and topology are local: continuity, convergence, and limit points all depend on what happens near a point, not on the entire space at once. A function f: X → Y is continuous at x if and only if the preimage of every neighborhood of f(x) is a neighborhood of x. A sequence (xₙ) converges to x if and only if every neighborhood of x contains all but finitely many terms of the sequence. In both cases, the question reduces to: what sets contain x? The neighborhood concept focuses your attention precisely there.

The collection of all neighborhoods of x is called the **neighborhood filter** at x. Filters are closed under supersets (if U is a neighborhood of x and U ⊆ V, then V is a neighborhood of x) and finite intersections (the intersection of two neighborhoods of x is a neighborhood of x). These closure properties make the neighborhood filter a clean algebraic object. More importantly, the topology is completely determined by its neighborhood structure: a set U is open if and only if it is a neighborhood of every point it contains. You can verify this directly — if every point x in U has a neighborhood Nₓ ⊆ U, then U = ⋃ₓ Nₓ, a union of open sets, hence open.

The practical payoff is that local analysis decomposes complex global questions into manageable point-by-point questions. Rather than asking "is this map continuous everywhere?" you ask "does the preimage of each neighborhood at f(x) contain a neighborhood of x?" at each x. This decomposition is why neighborhoods are the natural language for the concepts you'll encounter next: limit points (which ask whether every neighborhood of x meets a set A) and convergence in topology (which asks whether sequences eventually land in every neighborhood). The neighborhood perspective is not just convenient notation — it is the right level of abstraction for doing local topology.
