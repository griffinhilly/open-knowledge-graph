---
id: basis-for-a-topology
title: Basis for a Topology
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
builds-toward:
- product-topology
- metric-topology
tags:
- basis
- topology
- generation
stage: advanced
status: draft
---

# Basis for a Topology

## Core Idea
A basis for a topology is a collection of open sets such that every open set is a union of basis sets. Working with a basis is often easier than the entire topology since you only need to verify properties for basis elements. This is how metric topologies and product topologies are typically constructed.

## Explainer

A topology can contain enormously many open sets — in principle, uncountably many. Checking a property for every open set is impractical. A **basis** is a compact generating set: a smaller collection ℬ such that every open set in the topology is a union of elements of ℬ. This is analogous to a basis in linear algebra, where every vector is a linear combination of basis vectors — except here, "combination" means union rather than addition. The topology is completely determined by ℬ, yet ℬ is usually far simpler to describe.

A collection ℬ of subsets of X qualifies as a basis for a topology if two conditions hold: (1) every point of X belongs to some basis element (ℬ covers X), and (2) whenever a point x lies in B₁ ∩ B₂ for basis elements B₁, B₂ ∈ ℬ, there exists a basis element B₃ ∈ ℬ with x ∈ B₃ ⊆ B₁ ∩ B₂. The second condition ensures that intersections of basis elements, though not necessarily basis elements themselves, are still expressible as unions of basis elements — so the collection {unions of ℬ-elements} is closed under finite intersection, as a topology requires. When these two conditions hold, declaring the topology to be all unions of elements of ℬ is well-defined and produces a genuine topology.

The canonical example is ℝ with the standard topology. Open intervals (a, b) form a basis: every open subset of ℝ is a union of open intervals (this is actually a theorem, not a definition). The topology contains far more open sets — arbitrary unions of intervals, including things like (0,1) ∪ (3,5) ∪ (7,∞) — but the basis {(a,b)} is all you need to specify to pin down the topology completely. In a general metric space, **open balls** B(x, r) = {y : d(x, y) < r} form a basis for the **metric topology**, connecting the abstract basis definition back to the distance-based intuitions from calculus and analysis.

The basis framework makes product topologies tractable. The product topology on X × Y is defined by declaring the basis to be all sets of the form U × V where U is open in X and V is open in Y. Not every open set in X × Y looks like a "rectangle" U × V — most open sets are unions of many such rectangles — but the rectangle sets generate everything. Without the basis concept, specifying the product topology would require characterizing an enormously complex family of sets directly. With a basis, the recipe is two lines. This pattern — "define a simple basis, generate the full topology by taking unions" — recurs throughout topology whenever a new space is constructed from existing ones.
