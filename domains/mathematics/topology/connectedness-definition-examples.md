---
id: connectedness-definition-examples
title: 'Connectedness: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
- id: closed-sets-in-topological-spaces
  type: hard
builds-toward:
- path-connectedness
- connected-components
tags:
- connectedness
- connected-spaces
- disconnected
stage: advanced
status: draft
---

# Connectedness: Definition and Examples

## Core Idea
A topological space is connected if it cannot be written as a union of two disjoint nonempty open sets. Equivalently, the only subsets that are both open and closed (clopen) are the empty set and the whole space. Connectedness captures the intuitive idea that a space is "in one piece." The real line ℝ is connected, but ℝ minus a point is not—removing any point splits it into two open rays. The continuous image of a connected space is connected, which is why the intermediate value theorem holds: a continuous function on a connected domain cannot skip values. Connectedness is a topological invariant preserved under homeomorphisms.

## How It's Best Learned
Prove that ℝ is connected using the least upper bound property, then show ℚ is disconnected by exhibiting a clopen set. Working through these two cases builds a concrete understanding of the definition before moving to more exotic spaces.

## Common Misconceptions
Connected does not mean path-connected. The topologist's sine curve is connected but not path-connected. Students also sometimes think removing a point always disconnects a space—this is true for ℝ but false for ℝ² (which remains connected after removing any single point).

## Questions

```yaml
- question: "ℚ (the rationals with the subspace topology from ℝ) is disconnected. Which partition demonstrates this most directly?"
  type: multiple-choice
  options:
    - "The partition into negative rationals and positive rationals, since both are open and cover ℚ minus 0"
    - "The partition U = {q ∈ ℚ : q < √2} and V = {q ∈ ℚ : q > √2}, which are disjoint nonempty open sets covering ℚ"
    - "The partition into integers and non-integers, since the integers form a closed discrete subspace"
    - "There is no such partition because ℚ is dense in ℝ, and ℝ is connected"
  answer: 1
  explanation: "Since √2 is irrational, every rational is either less than √2 or greater — so U and V partition ℚ with no element left out. Both are open in ℚ (each is ℚ intersected with an open interval of ℝ), they are disjoint and nonempty. This is exactly the definition of disconnectedness. Option A fails because it omits 0. Option D is a common confusion: a dense subspace of a connected space need not itself be connected — ℚ is dense in ℝ but disconnected."

- question: "A student argues: 'Removing a point from ℝ disconnects it into two open rays, so removing a point from ℝ² must also disconnect it.' Evaluate this argument."
  type: multiple-choice
  options:
    - "Correct — removing any point from any connected space always disconnects it"
    - "Incorrect — ℝ² minus a point remains connected because any two remaining points can be path-connected by a curve that detours around the missing point"
    - "Correct — both ℝ and ℝ² minus a point have exactly two connected components"
    - "Incorrect — ℝ² minus a point is disconnected but for a different reason than ℝ minus a point"
  answer: 1
  explanation: "ℝ² minus a point is connected (and path-connected). In two dimensions, any path between two points can detour around the missing point — there is room to maneuver. In ℝ, every path from one side of the missing point to the other must pass through it, so its removal separates the line into two components. The argument fails by applying ℝ intuition to ℝ²; the dimension makes a fundamental difference to connectivity properties."

- question: "A topological space X is connected if and only if the only subsets of X that are simultaneously open and closed (clopen) are ∅ and X itself."
  type: true-false
  answer: true
  explanation: "This is equivalent to the standard definition. If X = U ∪ V with U, V disjoint nonempty open sets, then U is also closed (its complement V is open), giving a nontrivial clopen set. Conversely, any nontrivial clopen set A gives a partition X = A ∪ (X − A) into two disjoint nonempty open sets. The equivalence makes the clopen characterization a useful diagnostic: to prove connectedness, show no nontrivial clopen sets exist; to prove disconnectedness, exhibit one."

- question: "The topologist's sine curve — the closure of {(x, sin(1/x)) : x > 0} in ℝ² — is path-connected."
  type: true-false
  answer: false
  explanation: "The topologist's sine curve is connected but not path-connected — it is the canonical counterexample separating these concepts. The closure adds the segment {0} × [−1, 1]. No continuous path can connect a point on the oscillating sine portion to a point on the y-axis segment, because any such path would have to traverse the wildly oscillating tail, which oscillates infinitely without converging to any single limit on the y-axis. This shows that connected does not imply path-connected."

- question: "State the definition of a connected topological space and explain why the intermediate value theorem can be seen as a consequence of the connectedness of intervals in ℝ."
  type: short-answer
  answer: "A space X is connected if it cannot be written as a union of two disjoint nonempty open sets. The key theorem is that the continuous image of a connected space is connected. Closed intervals [a, b] ⊂ ℝ are connected (provable from the least upper bound property). Suppose f : [a, b] → ℝ is continuous with f(a) < c < f(b) and suppose f never equals c. Then [a, b] = f⁻¹((−∞, c)) ∪ f⁻¹((c, +∞)), a partition into two disjoint nonempty sets that are open by continuity of f. This contradicts the connectedness of [a, b], so f must attain the value c."
  explanation: "The IVT is really a statement about topology: continuous maps preserve connectedness, and connected subsets of ℝ cannot 'skip' values without being partitioned into two open pieces."
```

