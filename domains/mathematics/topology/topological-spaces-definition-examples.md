---
id: topological-spaces-definition-examples
title: 'Topological Spaces: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: set-theory-basics
  type: hard
- id: equivalence-relations
  type: soft
builds-toward:
- open-sets-definition-examples
- neighborhoods-topology-definition
tags:
- foundations
- definition
stage: formal-systems
status: draft
---

# Topological Spaces: Definition and Examples

## Core Idea
A topological space (X, τ) consists of a set X and a collection τ of subsets called open sets satisfying: ∅ and X are open, any union of open sets is open, and finite intersections of open sets are open. This structure generalizes the notion of 'open' from real analysis to arbitrary sets and forms the foundation of topology.

## Explainer

In real analysis, an open set in ℝ is one where every point has an open interval around it entirely contained in the set. This definition works beautifully — but it depends on the notion of distance. What if you want to study continuity and connectedness on a set where there is no natural notion of distance? Topology answers this by isolating the minimum structure needed: instead of defining "open" in terms of distance, you simply declare which sets are open, subject to three axioms that capture how open sets in ℝ actually behave.

The three axioms for a **topology** τ on a set X are: (1) the empty set ∅ and the whole set X are in τ; (2) any union of sets in τ is in τ — even infinite unions; (3) any **finite** intersection of sets in τ is in τ. The asymmetry between (2) and (3) is deliberate and important. In ℝ, the intersection of the open sets (−1/n, 1/n) for all n = 1, 2, 3, … is the single point {0}, which is not open. Allowing infinite intersections would let you generate closed sets from open sets through the back door, collapsing the structure. The axioms are carefully calibrated to permit enough structure for interesting topology while avoiding this collapse.

To build intuition, consider three extreme examples on the same set X = {a, b, c}. The **discrete topology** τ = 𝒫(X) (all subsets are open) is the finest possible topology — every set is open. The **indiscrete topology** τ = {∅, X} is the coarsest — only the two required sets are open. Between these extremes lie all other topologies, such as τ = {∅, {a}, X}, which is finer than the indiscrete but coarser than the discrete. Each topology encodes a different notion of which points are "close together": in the indiscrete topology, you cannot separate any two points with open sets at all, so in a sense every point is adjacent to every other.

The payoff is generality with preservation of key theorems. Continuous functions, convergence, connectedness, and compactness can all be defined purely in terms of open sets — no distances required. This means every theorem you prove in the topological setting applies automatically to metric spaces, function spaces, and far stranger settings. The set X you bring to topology can be almost anything: the real line, a finite set, a space of functions, a manifold. The topology τ specifies what "nearby" means in that context, and the three axioms ensure the structure is rich enough to do geometry with.
