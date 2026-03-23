---
id: connected-spaces-definition
title: Connected Spaces and Connectedness
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
- id: connected-spaces
  type: soft
builds-toward:
- path-connected-spaces
- connected-components-decomposition
tags:
- connectedness
- fundamental
stage: formal-systems
status: validated
---

# Connected Spaces and Connectedness

## Core Idea
A space is connected if it is not the disjoint union of two non-empty open sets. Equivalently, the only clopen (both open and closed) sets are ∅ and X. Connected spaces are 'in one piece.' Intervals are exactly the connected subsets of ℝ. Continuous images of connected spaces are connected; products are connected iff factors are.

## Questions

```yaml
- question: "Which of the following subsets of ℝ, with the subspace topology inherited from ℝ, is disconnected?"
  type: multiple-choice
  options:
    - "[0, 1]"
    - "(0, 1)"
    - "[0, 1) ∪ (2, 3]"
    - "ℝ itself"
  answer: 2
  explanation: "[0, 1) ∪ (2, 3] is disconnected: take U = [0, 1) ∩ ([0,1) ∪ (2,3]) = [0, 1) and V = (2, 3] ∩ ([0,1) ∪ (2,3]) = (2, 3]. In the subspace topology, U = (−∞, 1) ∩ X and V = (2, ∞) ∩ X are both open in X, they are disjoint, and their union is all of X — a valid separation. The connected subsets of ℝ are exactly the intervals (including rays and ℝ itself), and [0,1) ∪ (2,3] is not an interval."

- question: "The Intermediate Value Theorem (a continuous function on [a,b] that takes values f(a) and f(b) must take every value in between) is a consequence of which topological property?"
  type: multiple-choice
  options:
    - "Compactness of [a, b]"
    - "Connectedness of [a, b] combined with the fact that continuous images of connected spaces are connected"
    - "Completeness of ℝ alone, with no topological input needed"
    - "The Hausdorff property of ℝ"
  answer: 1
  explanation: "If f: [a,b] → ℝ is continuous and [a,b] is connected, then f([a,b]) is connected in ℝ — hence an interval. An interval in ℝ contains all values between any two of its members. Since f(a) and f(b) are both in f([a,b]), all values between them must be too. The IVT is essentially this argument: connectedness is preserved by continuous maps, and intervals are the connected subsets of ℝ."

- question: "A topological space can be disconnected only if its two pieces are geometrically separated — for instance, if one component is entirely to the left of the other on a number line."
  type: true-false
  answer: false
  explanation: "Disconnection is a purely topological property defined in terms of open sets, not geometric distance. The space {0, 1} with the discrete topology (every subset open) is disconnected: {0} and {1} are both open, disjoint, and cover the whole space — a valid separation. No notion of distance is needed. In metric spaces, geometric separation often corresponds to topological disconnection, but the definition itself is purely set-theoretic."

- question: "In any topological space X, the empty set ∅ and X itself are always clopen (simultaneously open and closed)."
  type: true-false
  answer: true
  explanation: "By the axioms of a topology, ∅ and X are required to be open sets. Their complements — X and ∅ respectively — are also open, which makes ∅ and X each closed as well. So they are always clopen in any topological space. The key fact is that a connected space is one where these are the ONLY clopen sets — having any proper non-empty clopen subset is exactly what it means for a space to be disconnected."

- question: "State the clopen-set characterization of connectedness and explain why it is equivalent to the separation definition."
  type: short-answer
  answer: "A space X is connected if and only if the only clopen (simultaneously open and closed) subsets are ∅ and X. Equivalence: if U is a proper non-empty clopen subset, then V = X \\ U is non-empty and open (U is closed, so its complement is open), and U ∪ V = X with U ∩ V = ∅ — a separation. Conversely, if (U, V) is a separation, then U is open and its complement V is also open, making U closed too — so U is a proper non-empty clopen set."
  explanation: "Both definitions capture the same idea from different angles. The separation definition says 'you cannot split X into two open pieces.' The clopen definition says 'no piece of X is both open and closed except the trivial ones.' The clopen version is often more convenient for proofs because it frames connectedness as a statement about a single set rather than a pair of sets."
```

## Explainer

**Connectedness** captures the intuition that a space is "all in one piece." The formal definition is a separation condition: a topological space X is **connected** if there do not exist two non-empty disjoint open sets U and V with U ∪ V = X. Such a pair (U, V) is called a **separation** of X. A connected space is one where no separation exists — you cannot split X into two non-trivial open pieces.

There is a useful equivalent reformulation using **clopen** sets (sets that are simultaneously open and closed). In any space, ∅ and X are always clopen. A connected space is one where these are the only clopen sets. The equivalence is direct: if U is a proper non-empty clopen subset of X, then V = X \ U is non-empty and open (since U is closed), giving a separation. Conversely, given a separation (U, V), U is open and its complement V is also open, making U closed too — a proper non-empty clopen set. Both formulations are standard; the clopen version is often the easier one to use in proofs.

From your study of open sets, you can check specific cases. The interval [0,1] ⊂ ℝ is connected: any open set in the subspace topology is an intersection of an open set of ℝ with [0,1], and no two such non-empty open sets partition [0,1]. By contrast, the discrete space {0,1} is disconnected: {0} and {1} are both open and form a separation. More fundamentally, the connected subsets of ℝ are exactly the intervals (including rays and ℝ itself) — a theorem, not a definition, whose proof uses the completeness of ℝ via the least upper bound property. This connection to completeness is deep: the intermediate value theorem is essentially a consequence of connectedness, as you will see.

The two key theorems for working with connectedness are closure under continuous maps and under products. **Continuous images of connected spaces are connected**: if f: X → Y is continuous and X is connected, then f(X) is connected. This immediately implies the intermediate value theorem — if f: [0,1] → ℝ is continuous, f([0,1]) is connected in ℝ, hence an interval, hence it contains all values between f(0) and f(1). **Products are connected if and only if all factors are connected**: X × Y is connected iff both X and Y are. These two theorems, combined with the characterization of connected subsets of ℝ, give you nearly all the working tools of connectedness in analysis and topology.
