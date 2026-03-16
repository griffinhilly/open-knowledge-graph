---
id: neighborhood-basis-topology
title: Neighborhood Basis and Local Bases
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
- sequences-convergence-topology
- first-countable-spaces
tags:
- neighborhoods
- local-bases
stage: abstract-reasoning
status: draft
---

# Neighborhood Basis and Local Bases

## Core Idea
A neighborhood basis at point x is a collection of open sets containing x such that every open neighborhood of x contains some basis set. This characterizes local topology around points.

## Explainer

You have already seen that a topological basis for a whole space allows you to reconstruct every open set as a union of basis elements. A **neighborhood basis** (or **local base**) at a point x is a more focused version: a collection ℬ(x) of open sets containing x such that for every open set U with x ∈ U, some B ∈ ℬ(x) satisfies x ∈ B ⊆ U. In other words, the local base "approximates" the local topology around x from inside — any open neighborhood of x contains at least one basis element. The neighborhood basis tells you everything about what it means to "approach" x within the topology.

In a metric space, the open balls B(x, 1/n) for n = 1, 2, 3, ... form a countable neighborhood basis at x. This is the key structure behind the ε–δ definition of continuity: to verify that a function is continuous at x, you only need to check preimages of sets in the local base, not all open sets. The countability of this local base is not a coincidence — it is the defining property of **first-countable spaces**. In such spaces, sequences suffice to detect limits, closure, and continuity, which is why metric-space intuition transfers so cleanly to first-countable topological spaces.

In more exotic spaces, the local base may be uncountable. Consider the **long line** or **ordinal spaces**: at certain points, every neighborhood basis must be uncountable because the topology is too rich to be probed by sequences alone. In such spaces, the absence of a countable local base means that sequences are no longer sufficient — a point x can be a limit point of a set A without any sequence in A converging to x. This failure of sequences is precisely what motivated the development of nets and filters as the natural convergence tools for general topology.

The neighborhood basis concept also clarifies what **homeomorphism** really means at the local level. Two spaces are homeomorphic if there is a bijection that sends open sets to open sets in both directions. At each point, this bijection must map a neighborhood basis at x to a neighborhood basis at the image f(x). So a homeomorphism preserves the entire local structure — not just closeness in a metric sense but the pattern of which sets nest inside which near each point. This is why topologists say homeomorphic spaces are "the same," even when they look geometrically different: their local bases are in bijective correspondence, and local bases encode everything about how the topology behaves near each point.


