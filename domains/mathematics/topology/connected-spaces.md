---
id: connected-spaces
title: Connected Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
- path-connectedness
- connected-components
tags:
- connected
- connectivity
stage: formal-systems
status: validated
---

# Connected Spaces

## Core Idea
A space is connected if it is not the disjoint union of two nonempty open sets. Connected spaces have no gaps. Continuous images of connected spaces are connected.

## Questions

```yaml
- question: "Consider X = ℝ² \ S¹, the plane with the unit circle removed (all points except those with x² + y² = 1). Is X connected?"
  type: multiple-choice
  options:
    - "Yes — removing a curve of zero width cannot disconnect the plane"
    - "Yes — you can still travel between any two points by going around the removed circle"
    - "No — the open disk {x² + y² < 1} and the exterior {x² + y² > 1} form a separation into two disjoint open sets"
    - "It depends on whether we use the standard or discrete topology on ℝ²"
  answer: 2
  explanation: "The unit circle disconnects the plane: {x² + y² < 1} and {x² + y² > 1} are both open in ℝ², both nonempty, disjoint, and their union is exactly X. This is a valid separation — so X is disconnected. Option A is the classic geometric misconception: intuitively, a curve 'has no width,' but topologically, removing it creates two pieces with no path between them that stays in X."

- question: "The Intermediate Value Theorem — that a continuous f: [0,1] → ℝ with f(0) < c < f(1) attains the value c — is a consequence of which topological fact?"
  type: multiple-choice
  options:
    - "The completeness of ℝ and the fact that bounded sequences have convergent subsequences"
    - "Continuous images of connected spaces are connected, and connected subsets of ℝ are intervals"
    - "Continuous functions on compact sets are uniformly continuous"
    - "The ε-δ definition of continuity prevents functions from skipping values"
  answer: 1
  explanation: "The topological proof: [0,1] is connected. f is continuous, so f([0,1]) is a connected subset of ℝ. Connected subsets of ℝ are exactly the intervals. Since f(0) and f(1) are in f([0,1]) and f([0,1]) is an interval, every value between them must also be in f([0,1]). The IVT is not a special theorem — it is connectedness applied to the real line."

- question: "In a connected topological space, the only subsets that are simultaneously open and closed (clopen) are the empty set and the entire space."
  type: true-false
  answer: true
  explanation: "This is one of the key characterizations of connectedness. If U is a nonempty proper clopen subset, then U and its complement V = X \\ U are both open, both nonempty, and disjoint with U ∪ V = X — a separation. So if X is connected, no such U can exist; the only clopens are ∅ and X. Conversely, if the only clopens are ∅ and X, any open partition would require one part to also be closed, forcing it to be ∅ or X."

- question: "A topological space is connected if and only if every two points in it can be joined by a continuous path."
  type: true-false
  answer: false
  explanation: "This describes path-connectedness, which is a strictly stronger condition. Every path-connected space is connected, but not every connected space is path-connected. The classic counterexample is the topologist's sine curve: the closure of {(x, sin(1/x)) : x > 0} in ℝ². This set is connected (the two pieces cannot be separated by open sets) yet there is no continuous path from a point on the oscillating part to the point (0, 0) on the y-axis segment."

- question: "Explain why ℝ with the standard topology is connected, while ℝ \\ {0} is not."
  type: short-answer
  answer: "ℝ is connected because any attempt to split it into two disjoint nonempty open sets must leave a point uncovered: between any two open intervals, there is always a point in neither. More formally, suppose ℝ = U ∪ V with U, V open, disjoint, nonempty. Pick a ∈ U and b ∈ V; the supremum of [a, b] ∩ U must belong to both the closure of U and the closure of V, but disjoint open sets have disjoint closures — contradiction. For ℝ \\ {0}: write it as (−∞, 0) ∪ (0, ∞). Both pieces are open in ℝ \\ {0}, nonempty, and disjoint — a valid separation."
  explanation: "Removing a single point from ℝ creates a gap that cannot be bridged by any path remaining in ℝ \\ {0}. Topologically, the removed point was the only 'link' between the two halves, and its absence makes the separation exact."
```

## Explainer

Your study of open sets gave you a language for describing topology in terms of neighborhoods and openness rather than distance. **Connectedness** is one of the first global properties that language can express — it answers the question: is this space "in one piece"? The formal definition is a negation: a topological space X is **connected** if it cannot be written as X = U ∪ V where U and V are both open, both nonempty, and disjoint. If such a partition exists, X is **disconnected** — it has been split into two completely separate open pieces with no overlap and nothing between them.

The real line ℝ with its standard topology is connected. Any open interval (a, b) is connected. But consider ℝ minus a single point: ℝ \ {0} = (−∞, 0) ∪ (0, ∞). These two pieces are both open in ℝ, nonempty, and disjoint — a valid disconnection. The intuition is that removing a single point "cuts" the line into two disconnected halves. The integers ℤ with the discrete topology (where every subset is open) are also disconnected: {0} and ℤ \ {0} form a valid disconnection. In the discrete topology every single-point set is both open and closed, and any space with more than one point is immediately disconnected.

One of the most powerful facts about connectedness is its **preservation under continuous maps**. If f: X → Y is continuous and X is connected, then f(X) — the image — is connected. This theorem has a celebrated corollary you might recognize from calculus: the **intermediate value theorem**. The argument runs as follows. The real line segment [0, 1] is connected. A continuous function f: [0, 1] → ℝ maps it to a connected subset of ℝ. Connected subsets of ℝ are intervals (a theorem in its own right). So f([0, 1]) is an interval — meaning f takes all intermediate values between f(0) and f(1). The IVT is just connectedness in disguise.

Understanding what makes a space disconnected often matters as much as knowing when it is connected. A space is disconnected precisely when it has a **clopen** subset — a set that is simultaneously open and closed, other than the empty set and the whole space. In a connected space, the only clopen sets are ∅ and X itself. This characterization is useful for proofs: to show X is connected, assume U is clopen and show it must be ∅ or X. The connected components — the maximal connected subsets of a space — partition every topological space and generalize this idea to spaces that have multiple pieces.
