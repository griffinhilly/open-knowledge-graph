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
status: validated
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

## Questions

```yaml
- question: "Let X = {a, b, c} and τ = {∅, {a}, {a, b}, X}. Is the set {b} open in the topology τ?"
  type: multiple-choice
  options:
    - "Yes — {b} is a subset of X, and all subsets of X are open in any topology"
    - "No — {b} is not in τ, and openness means being a member of the topology"
    - "Yes — {b} is a subset of the open set {a, b}, so it must be open"
    - "The question cannot be answered without knowing the metric on X"
  answer: 1
  explanation: "In a topological space, 'open' means precisely 'is a member of τ.' The set {b} is not listed in τ = {∅, {a}, {a,b}, X}, so it is not open. Option A describes the discrete topology, which τ is not. Option C confuses 'subset of an open set' with 'open' — subsets of open sets are not automatically open. Option D reflects the misconception that topologies must come from metrics; τ is a topology by definition, and no metric is needed or referenced."

- question: "The indiscrete topology on X = {a, b} has τ = {∅, X}. A student claims that {a} is open because 'a is a point in X and points should be open.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — points are always open in any topology"
    - "The student conflates 'open' with 'nonempty' — open is a topological designation, not a property of single elements"
    - "'Open' is not intrinsic — it depends entirely on which sets belong to τ, and {a} ∉ τ in the indiscrete topology"
    - "The student should check whether {a} is also closed before deciding"
  answer: 2
  explanation: "The student is importing an intuition from the discrete topology (where every singleton is open) and incorrectly treating it as universal. 'Open' is entirely determined by membership in τ — it is a declaration about the topological structure, not a property a set possesses independently. In the indiscrete topology, only ∅ and X are open. {a} is neither. This is the most important conceptual shift from calculus to topology: 'open' is not intrinsic to a set; it is relative to a chosen topology on the containing space."

- question: "A set that is open in the discrete topology on X may not be open if a different topology is placed on the same set X."
  type: true-false
  answer: true
  explanation: "This is the central conceptual point: 'open' is relative to the topology, not intrinsic to the set. In the discrete topology on X = {a, b, c}, every subset — including {a}, {b}, {a,c}, etc. — is open. But in the indiscrete topology on the same X, only ∅ and X are open, and {a} is not open. Same set X, same subset {a}, different topologies — different answers to 'is {a} open?' This dependence is what makes topology a study of structure rather than just a study of sets."

- question: "Most topology on a set X is expected to come from a metric (a distance function) on X — a topology is essentially the same thing as a metric space."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about topology. A topological space is strictly more general than a metric space. The indiscrete topology on a set with two or more points is not metrizable — no metric can generate it, because metric spaces always produce the T₁ property (singletons are closed), but the indiscrete topology is not T₁. One of topology's founding motivations was precisely to identify which properties of analysis require a metric and which require only the open-set axioms — many deep theorems hold in all topological spaces, not just metric ones."

- question: "The axiom for topological spaces allows arbitrary unions but only finite intersections of open sets. Give an example on ℝ (with the standard topology) showing why infinite intersections of open sets can fail to be open."
  type: short-answer
  answer: "For each n ≥ 1, the interval (−1/n, 1/n) is open in ℝ. But the intersection ⋂_{n=1}^∞ (−1/n, 1/n) = {0}, the singleton containing only 0. In the standard topology on ℝ, no singleton is open. So infinitely many open sets can intersect to produce a non-open set. This is why the topology axiom requires only finite intersections to be open — finite intersections of open neighborhoods remain open (needed for continuity), but infinite intersections can collapse to a point."
  explanation: "The asymmetry between arbitrary unions and only finite intersections is deliberate. Taking bigger and bigger unions of open sets keeps you within open sets (you're only widening). But intersecting open intervals can progressively shrink them to a single point, which should not be forced to be open — that would make the standard topology on ℝ collapse to the discrete topology. The axioms are calibrated to capture exactly the structure needed for continuity while remaining general enough to allow interesting non-metric examples."
```

## Explainer

You already know about open sets on the real line from your prerequisite. The open intervals and their unions form a collection of sets with three key properties: ∅ and ℝ are in the collection, arbitrary unions of members are in the collection, and finite intersections of members are in the collection. A **topological space** takes exactly these three properties as axioms and uses them to define "open sets" on *any* set, without requiring a metric or a notion of distance.

Formally, a topology on a set X is a collection τ of subsets of X (called the **open sets** of the topology) satisfying: (1) ∅ ∈ τ and X ∈ τ, (2) if {Uα} is any collection of sets in τ, then their union ⋃Uα ∈ τ, and (3) if U₁, …, Uₙ ∈ τ, then their finite intersection U₁ ∩ … ∩ Uₙ ∈ τ. The pair (X, τ) is a **topological space**. The same set X can carry many different topologies — "open" is not an intrinsic property of a set or its points, but a *declared* structure that you impose.

The extreme cases illustrate the flexibility. The **discrete topology** on any set X declares every subset open: τ = 𝒫(X), the power set. Every singleton {x} is open, so the space is maximally "spread out" — every point is isolated from every other. The **indiscrete topology** (also called the trivial topology) declares only ∅ and X open. Here, no proper nonempty subset is open, so there is no way to separate points topologically — this topology carries almost no information. Between these extremes lie all interesting topologies, including the standard topology on ℝ (open intervals and their unions), the subspace topology (inherited by a subset of a topological space), and the product topology (defined on Cartesian products).

The reason to go through this abstraction is that continuity, convergence, and connectedness can all be defined purely in terms of open sets — without any reference to distance. A function f : X → Y is **continuous** if preimages of open sets are open: for every V ∈ τ_Y, f⁻¹(V) ∈ τ_X. This definition works identically whether X and Y are the real line, a function space, a finite graph with the discrete topology, or any other topological space. By stripping away metric structure and keeping only the open-set axioms, topology identifies the minimal assumptions needed for continuity to make sense — and reveals that the same theorems hold in a much broader universe of spaces than just ℝⁿ.

