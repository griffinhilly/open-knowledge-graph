---
id: open-sets-in-topological-spaces
title: Open Sets in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: topological-spaces-definition-and-examples
  type: hard
- id: neighborhoods-and-open-sets
  type: soft
builds-toward:
- basis-for-a-topology
- neighborhoods-in-topology
tags:
- open-sets
- topology
- definitions
stage: advanced
status: validated
---
# Open Sets in Topological Spaces

## Core Idea
Open sets form the fundamental building blocks of a topology. They satisfy axioms that generalize the intuitive properties of open intervals on the real line: any union of open sets is open, and finite intersections of open sets are open. Understanding open sets is essential for defining continuity and other topological properties without relying on distance.

## Explainer

**Open sets** are the primitive objects of a topological space. A topological space (X, τ) is defined by specifying a set X together with a collection τ of subsets — the open sets — satisfying three axioms: (1) ∅ ∈ τ and X ∈ τ, (2) any union of members of τ is in τ, and (3) any finite intersection of members of τ is in τ. From your study of topological spaces, you know that these axioms abstract the behavior of open sets in metric spaces. Open sets in a general topology need not be defined by distances or ε-balls; they are simply the sets that belong to τ.

The distinction between arbitrary unions and finite intersections is essential. Unions of open sets are always open, no matter how many sets are involved — even uncountably many. But only finite intersections of open sets are guaranteed to be open. The intersection of infinitely many open sets can fail to be open: in ℝ with the standard topology, each interval (−1/n, 1/n) is open, but ∩ₙ(−1/n, 1/n) = {0} is not. If the axioms required arbitrary intersections to be open, every point would be open (as the intersection of smaller and smaller intervals), collapsing the topology to the discrete one. The finite-intersection restriction is precisely calibrated to exclude this collapse while preserving a meaningful notion of "openness."

Openness is not an intrinsic property of a set — it depends entirely on the topology. On a set X = {1, 2, 3}, the collection τ₁ = {∅, {1}, {1, 2}, X} and τ₂ = {∅, {2}, {2, 3}, X} are both valid topologies, but the set {1} is open in τ₁ and not open in τ₂. The same underlying set supports many different topologies, each declaring different sets to be open. This flexibility is the point of the axiomatic approach: rather than deriving openness from a distance formula, you declare which sets are open and derive everything else — continuity, convergence, compactness — from that declaration.

Open sets determine all other topological concepts. A function f : X → Y is continuous if and only if the preimage of every open set in Y is open in X. A set is closed if its complement is open. The interior of a set is the largest open set it contains. Compactness, connectedness, and separation axioms are all defined in terms of open sets. Understanding open sets thoroughly is therefore not just the first step in topology — it is the foundation on which the entire theory is built.

## Questions

```yaml
- question: "Consider the set X = {1, 2, 3} with topology τ = {∅, {1}, {1,2}, X}. Is {2} an open set in this topology?"
  type: multiple-choice
  options:
    - "Yes — every singleton set is open in any topology"
    - "No — {2} is not in τ, and open sets are exactly the members of τ"
    - "Yes — {2} is a subset of {1,2}, which is open, so {2} must be open"
    - "No — {2} is not open because it doesn't contain 1, the smallest element"
  answer: 1
  explanation: "In a topological space (X, τ), a set is open if and only if it belongs to the topology τ. Here τ = {∅, {1}, {1,2}, X}, and {2} is not listed — so {2} is not open. Option A is wrong: singletons are not guaranteed to be open in a general topology (they are open in the discrete topology but not in others). Option C confuses 'subset of an open set' with 'open' — this would make every subset of X open, which is only true for the discrete topology."

- question: "Which of the following is guaranteed to be open in every possible topology on a set X?"
  type: multiple-choice
  options:
    - "Every singleton set {x} for each x in X"
    - "Only ∅ and X itself"
    - "Every finite subset of X"
    - "Every subset of X — all subsets are open by default"
  answer: 1
  explanation: "The topology axioms require that both ∅ and X itself belong to any topology — these are the only sets that must be open in every topology. Everything else depends on the choice of topology. The discrete topology makes every subset open; the indiscrete topology makes only ∅ and X open. Singletons are not always open (they fail in the indiscrete topology). Finite subsets are not always open (they may be absent from a topology). 'Openness' is a property conferred by the topology, not intrinsic to the set."

- question: "In a topological space, an arbitrary (possibly infinite) intersection of open sets is generally open."
  type: true-false
  answer: false
  explanation: "The open-set axioms only guarantee that finite intersections of open sets are open. Infinite intersections can fail to be open. A classic example in ℝ with the standard topology: the open intervals (−1/n, 1/n) are open for every positive integer n, but their intersection ⋂ₙ (−1/n, 1/n) = {0}, a single point, which is not open in ℝ. The restriction to finite intersections is not an oversight — it is carefully designed to exclude this failure while preserving enough structure for the theory to work."

- question: "The same set of points S can be an open set in one topology on X but fail to be open in a different topology on the same set X."
  type: true-false
  answer: true
  explanation: "Openness is relative to a topology, not intrinsic to the set. For example, take X = {1, 2, 3}. In the discrete topology (where every subset is open), {1} is open. In the indiscrete topology τ = {∅, X}, only ∅ and X are open — so {1} is not open. The 'same' set {1} is open in one topology and not open in another. This is a key conceptual shift from metric spaces, where openness is determined by distances and is less flexible."

- question: "Why does the topology axiom require only finite intersections of open sets to be open, rather than allowing arbitrary intersections? What goes wrong if you permit infinite intersections?"
  type: short-answer
  answer: "Infinite intersections of open sets can be closed sets — or more precisely, sets that are not open. In the standard topology on ℝ, the intersection of all open intervals (−1/n, 1/n) for n = 1, 2, 3, … is the single point {0}, which is a closed set (not open). If infinite intersections were required to be open, then {0} would be open, but then every set would be open (by taking intersections of intervals centered at any point), collapsing the topology to the discrete topology. The finite-intersection axiom is precisely calibrated to preserve a non-trivial distinction between open and non-open sets."
  explanation: "This is why topology textbooks are careful to state 'finite intersection' explicitly. The restriction is load-bearing: it separates the useful structure of topological spaces from the too-rigid discrete topology where everything is open and all maps are automatically continuous."
```
