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
status: draft
---

# Connected Spaces and Connectedness

## Core Idea
A space is connected if it is not the disjoint union of two non-empty open sets. Equivalently, the only clopen (both open and closed) sets are ∅ and X. Connected spaces are 'in one piece.' Intervals are exactly the connected subsets of ℝ. Continuous images of connected spaces are connected; products are connected iff factors are.

## Explainer

**Connectedness** captures the intuition that a space is "all in one piece." The formal definition is a separation condition: a topological space X is **connected** if there do not exist two non-empty disjoint open sets U and V with U ∪ V = X. Such a pair (U, V) is called a **separation** of X. A connected space is one where no separation exists — you cannot split X into two non-trivial open pieces.

There is a useful equivalent reformulation using **clopen** sets (sets that are simultaneously open and closed). In any space, ∅ and X are always clopen. A connected space is one where these are the only clopen sets. The equivalence is direct: if U is a proper non-empty clopen subset of X, then V = X \ U is non-empty and open (since U is closed), giving a separation. Conversely, given a separation (U, V), U is open and its complement V is also open, making U closed too — a proper non-empty clopen set. Both formulations are standard; the clopen version is often the easier one to use in proofs.

From your study of open sets, you can check specific cases. The interval [0,1] ⊂ ℝ is connected: any open set in the subspace topology is an intersection of an open set of ℝ with [0,1], and no two such non-empty open sets partition [0,1]. By contrast, the discrete space {0,1} is disconnected: {0} and {1} are both open and form a separation. More fundamentally, the connected subsets of ℝ are exactly the intervals (including rays and ℝ itself) — a theorem, not a definition, whose proof uses the completeness of ℝ via the least upper bound property. This connection to completeness is deep: the intermediate value theorem is essentially a consequence of connectedness, as you will see.

The two key theorems for working with connectedness are closure under continuous maps and under products. **Continuous images of connected spaces are connected**: if f: X → Y is continuous and X is connected, then f(X) is connected. This immediately implies the intermediate value theorem — if f: [0,1] → ℝ is continuous, f([0,1]) is connected in ℝ, hence an interval, hence it contains all values between f(0) and f(1). **Products are connected if and only if all factors are connected**: X × Y is connected iff both X and Y are. These two theorems, combined with the characterization of connected subsets of ℝ, give you nearly all the working tools of connectedness in analysis and topology.
