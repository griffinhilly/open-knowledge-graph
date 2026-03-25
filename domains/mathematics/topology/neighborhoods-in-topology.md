---
id: neighborhoods-in-topology
title: Neighborhoods and Local Properties
domain: mathematics
course: topology
prerequisites:
- id: basis-for-a-topology
  type: hard
- id: neighborhoods-and-open-sets
  type: soft
builds-toward:
- limit-points-convergence-topology
- continuity-topological-spaces
tags:
- neighborhoods
- local-properties
- topology
stage: advanced
status: validated
---
# Neighborhoods and Local Properties

## Core Idea
A neighborhood of a point x is any set containing an open set that contains x. Neighborhoods allow us to study local behavior in a topological space—properties that depend only on what happens near a particular point, not on the space globally. Convergence and continuity are fundamentally local concepts expressed via neighborhoods.

## Questions

```yaml
- question: "Is the closed interval [0, 2] a neighborhood of the point 1 in ℝ with the standard topology?"
  type: multiple-choice
  options:
    - "No — neighborhoods must be open sets, and [0, 2] is closed"
    - "Yes — [0, 2] contains an open set (e.g., (0.5, 1.5)) that contains 1"
    - "No — a neighborhood must be an open ball centered at the point"
    - "Only if we restrict to the subspace topology on [0, 2]"
  answer: 1
  explanation: "A neighborhood of x is any set containing an open set that contains x — the neighborhood itself need not be open. [0, 2] contains the open interval (0.5, 1.5) which contains 1, so it qualifies as a neighborhood of 1. Option A is the most common misconception: students assume 'neighborhood' means 'open set,' but the definition is deliberately more general. Open balls centered at x are the canonical examples of neighborhoods but are not required."

- question: "A sequence (xₙ) in a topological space X converges to x under the neighborhood definition when:"
  type: multiple-choice
  options:
    - "Every open set in X eventually contains all terms of the sequence"
    - "For every neighborhood N of x, there exists M such that xₙ ∈ N for all n > M"
    - "The sequence enters every open ball around x and never leaves"
    - "For some neighborhood N of x, almost all terms of the sequence lie in N"
  answer: 1
  explanation: "Convergence to x requires that every neighborhood of x eventually contains all terms — for any N containing an open set around x, there exists M with xₙ ∈ N for all n > M. Option A is too strong: requiring every open set (not just those containing x) makes no sense. Option C adds a 'never leaves' condition not in the definition, and 'open ball' is metric-specific. Option D uses 'some neighborhood,' but convergence requires all neighborhoods of x."

- question: "Every open set containing x is a neighborhood of x."
  type: true-false
  answer: true
  explanation: "By definition, a neighborhood N of x is any set containing an open set U with x ∈ U ⊆ N. If N is itself open and contains x, take U = N: N contains the open set N which contains x. So every open set containing x satisfies the neighborhood definition. The class of neighborhoods is a superset of 'open sets containing x' — it includes non-open sets too, as long as they contain an open cushion around x."

- question: "A neighborhood of a point must itself be an open set."
  type: true-false
  answer: false
  explanation: "This is the central misconception. The definition requires only that a neighborhood N of x contain some open set U with x ∈ U ⊆ N — N itself need not be open. For example, [0, 1] is a neighborhood of 0.5 in ℝ (it contains (0.25, 0.75) which contains 0.5), even though [0, 1] is closed. Insisting that neighborhoods be open would collapse the concept to 'open sets containing x,' losing the flexibility that makes neighborhoods useful."

- question: "Why do topologists define neighborhoods as sets that *contain* an open set around x, rather than simply requiring neighborhoods to be open sets containing x? What flexibility does this gain?"
  type: short-answer
  answer: "Requiring neighborhoods to be open would make them identical to 'open sets containing x,' adding no new concept. Allowing any set that contains an open cushion around x separates 'local' from 'open': a neighborhood captures what happens near x without requiring the global property of openness. This allows closed intervals, half-open intervals, and other non-open sets to serve as neighborhoods, making arguments more flexible. It also connects naturally to the basis: a neighborhood of x just needs to contain some basis element containing x, letting local arguments reduce to checking finitely describable sets."
  explanation: "The deeper payoff is in continuity and convergence: f is continuous at x iff preimages of neighborhoods of f(x) are neighborhoods of x — this formulation works identically whether sets are open or not. The generalization also opens the door to filter theory, where the collection of all neighborhoods of x forms the prototypical example of a filter."
```

## Explainer

The concept of a **neighborhood** formalizes the intuitive idea of "near a point." You already know that a topology on a set X is a collection of open sets satisfying certain axioms, and that a basis generates all open sets. A neighborhood of a point x is simply any set N that contains some open set U with x ∈ U ⊆ N. The neighborhood need not itself be open — what matters is that there is an open "cushion" around x sitting inside N. In metric spaces, the familiar open balls B(x, ε) are the prototypical neighborhoods, and every metric topology can be understood entirely in terms of them.

Why introduce neighborhoods at all, rather than working directly with open sets? Because many key concepts in topology are fundamentally **local** — they describe behavior near a single point, not behavior across the whole space. Convergence is the clearest example. A sequence (x₁, x₂, …) converges to x if every neighborhood of x eventually contains all terms of the sequence: for every N containing an open set around x, there exists some index M such that xₙ ∈ N for all n > M. This is exactly the topological generalization of the familiar ε-N definition from metric spaces, where ε-balls play the role of neighborhoods.

Continuity at a point has an equally clean neighborhood formulation. A function f: X → Y is continuous at x if for every neighborhood V of f(x) in Y, there exists a neighborhood U of x in X such that f(U) ⊆ V — the image of a small region around x lands inside any prescribed region around f(x). This phrasing makes the local character of continuity explicit: whether f is continuous at x depends only on what f does near x, not on the global structure of X or Y.

Because a basis generates all opens, it suffices to check neighborhoods against **basis elements**. If B is a basis for the topology on X, then N is a neighborhood of x if and only if some basis element B ∈ B with x ∈ B is contained in N. This means neighborhood arguments can often be reduced to checking finitely describable basic sets — a practical simplification that carries through to all the local concepts built on neighborhoods.
