---
id: connected-sets
title: Connected Sets
domain: mathematics
course: real-analysis
prerequisites:
- id: open-sets-real-line
  type: hard
- id: closed-sets-real-line
  type: hard
builds-toward:
- intermediate-value-theorem-rigorous
tags:
- connected
- topology
- path-connected
stage: advanced
status: draft
---

# Connected Sets

## Core Idea
A set S is connected if it cannot be written as S = U ∪ V where U and V are non-empty, disjoint, open sets (in the subspace topology). In ℝ, intervals and rays are exactly the connected sets. Continuous images of connected sets are connected, leading directly to the Intermediate Value Theorem.

## Explainer

From your study of open and closed sets on the real line, you know how to classify subsets of ℝ by their topological properties. **Connectedness** captures a different property: whether a set is "all in one piece" or can be separated into two disjoint parts with no points of contact. Formally, a set S ⊆ ℝ is **disconnected** if it can be written as S = U ∪ V where U and V are non-empty, disjoint, and both open in the subspace topology on S. If no such separation exists, S is **connected**. The definition is topological — it depends on the subspace topology, not on any metric or algebraic structure.

The complete characterization of connected subsets of ℝ is elegant: **a subset of ℝ is connected if and only if it is an interval** (where single points, rays, and the empty set count as degenerate intervals). The forward direction is intuitive: if S is not an interval, there exist points a, b ∈ S with some c between them satisfying c ∉ S. Then U = S ∩ (−∞, c) and V = S ∩ (c, ∞) provide a separation. The reverse direction — showing that every interval is connected — requires a proof by contradiction using the completeness of ℝ. The key step uses the least upper bound property to show that any supposed separation of an interval must fail.

The most important theorem involving connectedness is that **continuous images of connected sets are connected**. If f : S → ℝ is continuous and S is connected, then f(S) is connected — hence an interval. This immediately yields the **Intermediate Value Theorem**: if f is continuous on [a, b] and y lies between f(a) and f(b), then y ∈ f([a, b]) because f([a, b]) is an interval (a connected subset of ℝ contains every value between any two of its elements). This is arguably the cleanest proof of the IVT — it reduces the theorem to two facts: intervals are connected, and continuous functions preserve connectedness.

The subspace topology is essential to the definition and a source of common confusion. The set {0, 1} is disconnected because {0} = {0, 1} ∩ (−1/2, 1/2) and {1} = {0, 1} ∩ (1/2, 3/2) are both open in the subspace topology, even though neither is open in ℝ. Similarly, ℝ \ {0} = (−∞, 0) ∪ (0, ∞) is disconnected — removing a single point from ℝ creates a gap that separates the line into two open pieces. In higher dimensions, removing a point from ℝ² does not disconnect it (you can go around the hole), which shows that connectedness is sensitive to the ambient space and dimension. In ℝ, however, the equivalence "connected ⟺ interval" gives a complete and concrete answer.

## Questions

```yaml
- question: "Consider S = ℝ \\ {0} = (-∞, 0) ∪ (0, ∞). Is S connected?"
  type: multiple-choice
  options:
    - "Yes — removing a single point cannot disconnect a set"
    - "No — S can be written as the union of two non-empty, disjoint sets that are open in the subspace topology on S"
    - "Yes — S is an open set, and open sets in ℝ are connected"
    - "No — S is disconnected because it is not closed"
  answer: 1
  explanation: "The key is the subspace topology. In the subspace topology on S, the sets (-∞, 0) and (0, ∞) are both open (each is the intersection of S with an open interval in ℝ), non-empty, disjoint, and their union is S. This is exactly the definition of disconnectedness. Option A mistakes removing a single point for a 'small' change — in topology, even one removed point can disconnect a set. Options C and D confuse connectedness with being open or closed, which are separate properties."

- question: "Why does the Intermediate Value Theorem follow directly from the fact that continuous images of connected sets are connected?"
  type: multiple-choice
  options:
    - "Because continuous functions map open sets to open sets, preserving the interval structure"
    - "Because if f is continuous on [a,b], then f([a,b]) is a connected subset of ℝ — which means it is an interval — so f must take every value between f(a) and f(b)"
    - "Because differentiable functions cannot skip values, and continuous functions are almost everywhere differentiable"
    - "Because [a,b] is both open and closed, forcing f([a,b]) to be an interval"
  answer: 1
  explanation: "The IVT proof via connectedness is elegant precisely because it reduces to two facts: (1) [a,b] is connected (it is an interval, and intervals are exactly the connected subsets of ℝ), and (2) continuous images of connected sets are connected. Together they force f([a,b]) to be a connected subset of ℝ — hence an interval. If f(a) and f(b) are both in f([a,b]), then every value between them must be too (since an interval contains all points between any two of its elements). This is the IVT, with no ε-δ case analysis required."

- question: "In ℝ, a set is connected if and only if it is an interval (where single points, rays, and the empty set count as degenerate intervals)."
  type: true-false
  answer: true
  explanation: "This is the complete characterization of connected subsets of ℝ. An interval cannot be split into two disjoint non-empty open parts because any gap would create such a split. Conversely, any non-interval subset of ℝ has a gap — a point not in the set between two points that are — and this gap immediately provides the separation required by the definition of disconnectedness. The equivalence 'connected ⟺ interval' is specific to ℝ; in higher dimensions, connected does not imply path-connected or convex."

- question: "A set S ⊆ ℝ is disconnected only if it can be written as a union of two disjoint non-empty closed sets (in the subspace topology)."
  type: true-false
  answer: false
  explanation: "The standard definition of disconnectedness uses open sets: S is disconnected if S = U ∪ V with U, V non-empty, disjoint, and open in the subspace topology. However, in the subspace topology, U and V would each also be closed (since each is the complement of the other within S). So for subsets of ℝ, the open-set and closed-set formulations are actually equivalent — but the statement as posed is misleading because it suggests closed sets are the fundamental requirement, when the definition is given in terms of open sets. More importantly, not all disconnected sets can be split by globally closed sets in ℝ; the subspace topology is what matters."

- question: "Using the definition precisely, explain why the set {0, 1} ⊂ ℝ (with the subspace topology inherited from ℝ) is disconnected."
  type: short-answer
  answer: "Let U = {0} and V = {1}. In the subspace topology on {0,1}, a set is open if it equals the intersection of {0,1} with some open set in ℝ. Since {0} = {0,1} ∩ (-1/2, 1/2) and {1} = {0,1} ∩ (1/2, 3/2), both {0} and {1} are open in the subspace topology. They are also non-empty, disjoint, and their union is {0,1}. This is exactly the definition of disconnectedness: a separation of {0,1} into two disjoint non-empty open sets."
  explanation: "The subtlety is that 'open in the subspace topology' is not the same as 'open in ℝ.' The set {0} is not open in ℝ, but it is open in the subspace topology on {0,1} because it is the restriction of an open interval to the subspace. This is why the definition specifies 'open in the subspace topology' — it makes disconnectedness a property of the set itself, independent of how it sits in a larger space."
```
