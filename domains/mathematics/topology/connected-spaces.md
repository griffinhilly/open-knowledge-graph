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
stage: abstract-reasoning
status: draft
---

# Connected Spaces

## Core Idea
A space is connected if it is not the disjoint union of two nonempty open sets. Connected spaces have no gaps. Continuous images of connected spaces are connected.

## Explainer

Your study of open sets gave you a language for describing topology in terms of neighborhoods and openness rather than distance. **Connectedness** is one of the first global properties that language can express — it answers the question: is this space "in one piece"? The formal definition is a negation: a topological space X is **connected** if it cannot be written as X = U ∪ V where U and V are both open, both nonempty, and disjoint. If such a partition exists, X is **disconnected** — it has been split into two completely separate open pieces with no overlap and nothing between them.

The real line ℝ with its standard topology is connected. Any open interval (a, b) is connected. But consider ℝ minus a single point: ℝ \ {0} = (−∞, 0) ∪ (0, ∞). These two pieces are both open in ℝ, nonempty, and disjoint — a valid disconnection. The intuition is that removing a single point "cuts" the line into two disconnected halves. The integers ℤ with the discrete topology (where every subset is open) are also disconnected: {0} and ℤ \ {0} form a valid disconnection. In the discrete topology every single-point set is both open and closed, and any space with more than one point is immediately disconnected.

One of the most powerful facts about connectedness is its **preservation under continuous maps**. If f: X → Y is continuous and X is connected, then f(X) — the image — is connected. This theorem has a celebrated corollary you might recognize from calculus: the **intermediate value theorem**. The argument runs as follows. The real line segment [0, 1] is connected. A continuous function f: [0, 1] → ℝ maps it to a connected subset of ℝ. Connected subsets of ℝ are intervals (a theorem in its own right). So f([0, 1]) is an interval — meaning f takes all intermediate values between f(0) and f(1). The IVT is just connectedness in disguise.

Understanding what makes a space disconnected often matters as much as knowing when it is connected. A space is disconnected precisely when it has a **clopen** subset — a set that is simultaneously open and closed, other than the empty set and the whole space. In a connected space, the only clopen sets are ∅ and X itself. This characterization is useful for proofs: to show X is connected, assume U is clopen and show it must be ∅ or X. The connected components — the maximal connected subsets of a space — partition every topological space and generalize this idea to spaces that have multiple pieces.
