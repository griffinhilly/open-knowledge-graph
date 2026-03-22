---
id: topological-spaces-definition
title: 'Topological Spaces: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: set-theory-basics
  type: hard
- id: proof-by-contradiction
  type: hard
builds-toward:
- open-sets-topology
- closed-sets-topology
- basis-for-topology
tags:
- definition
- foundations
stage: formal-systems
status: draft
---

# Topological Spaces: Definition and Examples

## Core Idea
A topological space (X, τ) is a set X together with a collection τ of subsets (open sets) satisfying three axioms: ∅ and X are in τ; arbitrary unions of sets in τ remain in τ; finite intersections of sets in τ remain in τ. This axiomatizes 'openness' from real analysis, providing a framework for continuity and convergence without requiring distance metrics.

## Explainer

A **topological space** is a pair (X, τ) where X is a set and τ is a collection of subsets of X — called the **open sets** — satisfying three axioms: (1) the empty set ∅ and the whole set X belong to τ, (2) the union of any collection of sets in τ belongs to τ, and (3) the intersection of any finite collection of sets in τ belongs to τ. These axioms distill the essential properties of "openness" from real analysis and metric spaces into a minimal framework that requires no notion of distance. Everything in topology — continuity, convergence, compactness, connectedness — is built on this foundation.

The axioms are modeled on the behavior of open sets in ℝ. In the standard topology on ℝ, unions of open intervals are open, and finite intersections of open intervals are open. The topology axioms abstract exactly these closure properties. The asymmetry between arbitrary unions and finite intersections is not accidental: in ℝ, the infinite intersection ∩ₙ(−1/n, 1/n) = {0} is not open, so requiring closure under arbitrary intersections would exclude the standard topology. The finite-intersection restriction is precisely what allows the standard topology on ℝ to qualify while preventing a collapse to the discrete topology.

Any set X admits multiple topologies. The **discrete topology** τ = P(X) declares every subset open; the **indiscrete topology** τ = {∅, X} declares only ∅ and X open. These are the finest and coarsest possible topologies on X. Between them, many intermediate topologies exist. On ℝ, beyond the standard topology, one can define the cofinite topology (open sets are those with finite complement, plus ∅), the lower-limit topology (basis of half-open intervals [a, b)), and others. Each choice of τ yields a different topological space with different notions of convergence, continuity, and compactness — even though the underlying set X is the same.

The power of the axiomatic approach is its generality. Once the three axioms are in place, you can define continuity (a function f : X → Y is continuous if f⁻¹(U) is open in X whenever U is open in Y), convergence (a sequence converges to x if it is eventually in every open set containing x), compactness (every open cover has a finite subcover), and connectedness (no nontrivial partition into disjoint open sets) — all without mentioning distance. Metric spaces become a special case: every metric induces a topology via open balls, and all metric-space theorems about continuity and convergence are instances of the general topological definitions. The passage from metric spaces to topological spaces is the passage from quantitative distance to the qualitative structure of "which sets are open," and the three axioms are all that structure requires.

## Questions

```yaml
- question: "Let X = {1, 2, 3}. Which of the following collections τ fails to be a topology on X?"
  type: multiple-choice
  options:
    - "τ = {∅, X}"
    - "τ = {∅, {1}, X}"
    - "τ = {∅, {1}, {2}, X}"
    - "τ = {∅, {1}, {2}, {1,2}, X}"
  answer: 2
  explanation: "Option C fails because it violates the closure under arbitrary unions axiom: {1} and {2} are both in τ, but their union {1,2} is not. A topology must be closed under all unions of its members. Option A (the indiscrete topology) and option B are valid topologies — check that ∅ and X are present, unions stay in τ, and finite intersections stay in τ. Option D includes {1,2} = {1} ∪ {2}, so it is closed under unions and is a valid topology."

- question: "Topology requires closure under arbitrary unions but only finite intersections. Why is this asymmetry necessary?"
  type: multiple-choice
  options:
    - "It is a historical convention that has no mathematical justification"
    - "Infinite intersections are not valid set-theoretic operations"
    - "In the standard topology on ℝ, the intersection of all intervals (−1/n, 1/n) is {0}, which is not open — so allowing arbitrary intersections would exclude this standard example"
    - "Finite intersections are computationally tractable, while infinite ones are not"
  answer: 2
  explanation: "The axioms are designed to capture the behavior of open sets in metric spaces like ℝ. In the standard topology on ℝ, arbitrary unions of open intervals are open, but the intersection of all open intervals (−1/n, 1/n) for n = 1, 2, 3, ... equals the single point {0}, which is not open. If we required closure under arbitrary intersections, this standard topology would not qualify. The asymmetry is not a convention — it is forced by the intended model."

- question: "Every set X has exactly one possible topology."
  type: true-false
  answer: false
  explanation: "Any set X carries at least two topologies: the indiscrete topology τ = {∅, X} (only the empty set and X itself are open) and the discrete topology τ = 𝒫(X) (every subset is open). Between these extremes, most sets admit many more topologies. The same set X can be equipped with different topologies, yielding different topological spaces with different notions of openness, continuity, and convergence. The topology is not determined by the set — it is an additional structure you impose."

- question: "In any topological space (X, τ), both the empty set ∅ and the whole set X must be declared open."
  type: true-false
  answer: true
  explanation: "This is the first axiom of a topology: ∅ ∈ τ and X ∈ τ. Both inclusions serve important technical roles. ∅ being open is required for consistency with the union and intersection axioms (the empty union is ∅, which must be in τ). X being open ensures the whole space is 'open,' which is needed for many topological arguments. These are not optional — any collection of subsets that fails to include both ∅ and X is not a topology by definition."

- question: "Why does defining 'openness' through axioms rather than through distance allow topology to generalize beyond metric spaces?"
  type: short-answer
  answer: "Distance imposes a rigid quantitative structure: two points are 'close' if a number (their distance) is small. The topological axioms abstract only the qualitative behavior of open sets — which sets can be unioned and intersected — without requiring any measurement. This means the framework applies to any collection of subsets satisfying the axioms, including spaces with no natural notion of distance: function spaces, abstract sets with only combinatorial structure, spaces of convergent sequences, and more. Topology studies what is preserved by continuous deformation, not by rigid motion, and distance is too strong a requirement for that."
  explanation: "The key move is identifying which properties of open sets in ℝ are actually used in proofs about continuity and convergence — and it turns out to be only the three axioms, not the full distance structure. Once the axioms are in place, you can define continuity (preimages of open sets are open), convergence, compactness, and connectedness purely in terms of the topology τ, with no reference to distance. Metric spaces become a special case of topological spaces, and all theorems proved topologically apply to them automatically."
```
