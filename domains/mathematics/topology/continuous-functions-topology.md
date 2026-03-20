---
id: continuous-functions-topology
title: Continuous Functions in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
- homeomorphisms-topological-equivalence
- quotient-topology
tags:
- continuity
- fundamental
stage: formal-systems
status: draft
---

# Continuous Functions in Topological Spaces

## Core Idea
A function f: X → Y is continuous if for every open set V in Y, the preimage f⁻¹(V) is open in X. This generalizes ε-δ continuity and works in any topological context.

## Explainer

Your prerequisite, open sets in topology, defined what it means for a collection of subsets to constitute a topology: the whole space and the empty set are open, arbitrary unions of open sets are open, and finite intersections of open sets are open. Now, with two topological spaces X and Y, you need a notion of "continuous function" that captures the same idea as ε-δ continuity but without distances. The topological definition does this elegantly: **f: X → Y is continuous if for every open set V ⊆ Y, the preimage f⁻¹(V) = {x ∈ X : f(x) ∈ V} is open in X**.

To see why this generalizes ε-δ, consider X = Y = ℝ with the standard (metric) topology. An open set in ℝ is a union of open intervals. The ε-δ condition says: for every ε > 0 and every x, there exists δ > 0 such that |x − y| < δ implies |f(x) − f(y)| < ε. In other words, every open ball around f(x) (the set (f(x)−ε, f(x)+ε)) has an open ball around x mapping into it — which is exactly saying that the preimage of any open interval around f(x) contains an open interval around x, which is exactly saying that preimages of open sets are open. The two definitions coincide on ℝ.

The preimage definition is asymmetric in a way that demands explanation: why preimages, not images? The answer is that **continuous functions need not send open sets to open sets**. The constant function f(x) = 0 sends every open set to the single point {0}, which is not open in ℝ. Functions that do map open sets to open sets — called **open maps** — are a separate, strictly stronger condition. The topological definition of continuity is correctly one-directional: open sets pull back to open sets.

Thinking in terms of preimages reframes what continuity means: a function is continuous when the topology on the *domain* is at least as fine as the topology induced by the *codomain* via f. If V is "declared open" in Y, then f⁻¹(V) must be "declared open" in X — the topology on X must respect what f sees as open structure in Y. This perspective makes it easy to compare topologies (the coarser the topology on Y, the easier continuity is to achieve) and to define new topologies from functions (the **initial topology** and **quotient topology** are both defined via this preimage condition). The definition you have here is not just a generalization of ε-δ; it is the right structural concept that makes the rest of topology work.
