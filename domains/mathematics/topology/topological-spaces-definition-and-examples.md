---
id: topological-spaces-definition-and-examples
title: 'Topological Spaces: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: set-theory-basics
  type: hard
- id: open-and-closed-sets-real-line
  type: hard
builds-toward:
- open-sets-in-topological-spaces
- closed-sets-in-topological-spaces
tags:
- topological-spaces
- definitions
- foundations
stage: advanced
status: draft
---

# Topological Spaces: Definition and Examples

## Core Idea
A topological space is a set X with a collection of 'open sets' satisfying three axioms: the empty set and X are open, arbitrary unions of open sets are open, and finite intersections are open. This generalizes the concept of open sets from the real line to arbitrary sets, allowing us to study continuity and convergence without a metric.

## How It's Best Learned
Verify the axioms for three canonical examples: the discrete topology (all subsets open), the indiscrete topology (only ∅ and X open), and the standard topology on ℝ. Then construct a topology on a finite set by hand and check which properties (Hausdorff, connected, compact) it satisfies.

## Common Misconceptions
- Assuming every topology comes from a metric; the indiscrete topology on two or more points has no compatible metric.
- Thinking open sets must look like intervals; in the discrete topology, every singleton is open.
- Forgetting that "open" is not an intrinsic property of a set — it depends on the topology, which is a choice.

## Explainer

You already know about open sets on the real line from your prerequisite. The open intervals and their unions form a collection of sets with three key properties: ∅ and ℝ are in the collection, arbitrary unions of members are in the collection, and finite intersections of members are in the collection. A **topological space** takes exactly these three properties as axioms and uses them to define "open sets" on *any* set, without requiring a metric or a notion of distance.

Formally, a topology on a set X is a collection τ of subsets of X (called the **open sets** of the topology) satisfying: (1) ∅ ∈ τ and X ∈ τ, (2) if {Uα} is any collection of sets in τ, then their union ⋃Uα ∈ τ, and (3) if U₁, …, Uₙ ∈ τ, then their finite intersection U₁ ∩ … ∩ Uₙ ∈ τ. The pair (X, τ) is a **topological space**. The same set X can carry many different topologies — "open" is not an intrinsic property of a set or its points, but a *declared* structure that you impose.

The extreme cases illustrate the flexibility. The **discrete topology** on any set X declares every subset open: τ = 𝒫(X), the power set. Every singleton {x} is open, so the space is maximally "spread out" — every point is isolated from every other. The **indiscrete topology** (also called the trivial topology) declares only ∅ and X open. Here, no proper nonempty subset is open, so there is no way to separate points topologically — this topology carries almost no information. Between these extremes lie all interesting topologies, including the standard topology on ℝ (open intervals and their unions), the subspace topology (inherited by a subset of a topological space), and the product topology (defined on Cartesian products).

The reason to go through this abstraction is that continuity, convergence, and connectedness can all be defined purely in terms of open sets — without any reference to distance. A function f : X → Y is **continuous** if preimages of open sets are open: for every V ∈ τ_Y, f⁻¹(V) ∈ τ_X. This definition works identically whether X and Y are the real line, a function space, a finite graph with the discrete topology, or any other topological space. By stripping away metric structure and keeping only the open-set axioms, topology identifies the minimal assumptions needed for continuity to make sense — and reveals that the same theorems hold in a much broader universe of spaces than just ℝⁿ.

