---
id: path-connectedness
title: Path Connectedness
domain: mathematics
course: topology
prerequisites:
- id: connectedness-definition-examples
  type: hard
- id: continuous-functions-topology
  type: soft
- id: homotopy-paths
  type: soft
builds-toward:
- homotopy-of-paths
- fundamental-group-definition
tags:
- path-connectedness
- paths
- arcs
stage: advanced
status: validated
---
# Path Connectedness

## Core Idea
A space is path-connected if any two points can be joined by a continuous path (image of a continuous map from [0,1]). Path-connectedness implies connectedness but not conversely. It provides a more intuitive and constructive notion of connectedness amenable to algebraic topology.

## Questions

```yaml
- question: "The topologist's sine curve — the closure of the graph of sin(1/x) for x > 0 in ℝ² — is connected but not path-connected. What prevents a continuous path from reaching the segment {0} × [−1, 1]?"
  type: multiple-choice
  options:
    - "The set is not compact, so paths in it need not have closed images"
    - "sin(1/x) oscillates infinitely rapidly as x → 0, so no continuous function can approach the y-axis without 'jumping'"
    - "The segment {0} × [−1, 1] is open in the subspace topology, making it unreachable"
    - "Paths in ℝ² cannot cross the y-axis because it divides the plane into two components"
  answer: 1
  explanation: "As x → 0⁺, sin(1/x) oscillates between −1 and 1 with increasing frequency and no limit. A continuous path γ: [0,1] → X approaching the y-axis segment would require traversing arbitrarily large oscillations in a finite parameter interval — impossible for a continuous function. By the intermediate value theorem, the path would need to hit every value between −1 and 1 infinitely often in any neighborhood of its endpoint. The space is connected because you cannot separate it with disjoint open sets, but the path-connectedness construction fails due to this geometric obstruction."

- question: "You want to study the fundamental group of a space X by analyzing loops based at a point x₀. Why is path-connectedness a prerequisite rather than a convenience?"
  type: multiple-choice
  options:
    - "Path-connectedness is equivalent to simply-connectedness, which is the actual hypothesis needed"
    - "Without path-connectedness, there may be points between which no path exists, making the fundamental group depend on basepoint in a way that cannot be compared across the space"
    - "The fundamental group is only defined for metric spaces, which must be path-connected"
    - "Path-connectedness ensures the space has no holes, guaranteeing a trivial fundamental group"
  answer: 1
  explanation: "The fundamental group π₁(X, x₀) is defined as homotopy classes of loops at x₀. For this to reflect the global topology of X, groups at different basepoints must be comparable — which requires a path between any two points (the isomorphism is constructed by conjugating loops with a connecting path). If X is not path-connected, π₁(X, x₀) only sees the path-component of x₀, and basepoints in different components give unrelated groups. Path-connectedness ensures the fundamental group is a property of the whole space, not an accident of basepoint choice."

- question: "Every path-connected topological space is connected."
  type: true-false
  answer: true
  explanation: "Proof sketch: Suppose X is path-connected but not connected. Then X = U ∪ V with U, V disjoint, nonempty, and open. Take p ∈ U and q ∈ V. By path-connectedness, there is a continuous path γ: [0,1] → X with γ(0) = p and γ(1) = q. Then [0,1] = γ⁻¹(U) ∪ γ⁻¹(V) is a partition into disjoint open sets, with 0 ∈ γ⁻¹(U) and 1 ∈ γ⁻¹(V). But [0,1] is connected — contradiction. Therefore path-connectedness implies connectedness."

- question: "Every connected topological space is path-connected."
  type: true-false
  answer: false
  explanation: "The topologist's sine curve (closure of {(x, sin(1/x)) : x > 0}) is the standard counterexample. It is connected — it cannot be split into two disjoint nonempty open sets — but it is not path-connected because no continuous path can reach the limit segment {0} × [−1, 1] from the oscillating part. Connectedness is a strictly weaker condition: it rules out global separations, but does not guarantee that any two points can be joined by a continuous arc."

- question: "What is the difference between connectedness and path-connectedness, and why does algebraic topology require the stronger condition rather than just connectedness?"
  type: short-answer
  answer: "Connectedness says only that the space cannot be split into two disjoint nonempty open sets — it is a global separation condition. Path-connectedness says any two points can be joined by a continuous path γ: [0,1] → X — it is a constructive condition. Algebraic topology requires path-connectedness because homotopy theory is built from paths: the fundamental group consists of homotopy classes of loops, and comparing fundamental groups at different basepoints requires a path between them. A merely connected space may have pairs of points with no path between them, making loop-based constructions undefined or incoherent. Path-connectedness guarantees the algebraic structure actually reflects the topology of the whole space."
  explanation: "The topologist's sine curve illustrates the gap: it is connected but the limit segment is completely unreachable by paths, so any homotopy theory based at a point on the oscillating part would be blind to the y-axis segment. Path-connectedness eliminates this kind of pathological disconnection between the geometry and the algebra."
```

## Explainer

You already know that a topological space is **connected** if it cannot be split into two disjoint nonempty open sets. That is a "global" condition — it says the space has no partition of a certain kind. **Path-connectedness** gives a "local-to-global" version that is often easier to work with and closer to geometric intuition: a space X is path-connected if for every pair of points p, q ∈ X, there exists a continuous function γ : [0, 1] → X with γ(0) = p and γ(1) = q. The function γ is called a **path** from p to q. The image γ([0, 1]) is a continuous arc connecting the two points within X.

The interval [0, 1] is the standard parameter space for paths because it is compact, connected, and conveniently normalizes endpoints to 0 and 1. A path is not a route — it is a function, so it can double back on itself, slow down, or even be constant. What matters is continuity: no teleportation allowed. Any two points in ℝⁿ can be joined by a straight-line path γ(t) = (1−t)p + tq, so ℝⁿ is path-connected. Any convex set is path-connected for the same reason. Most spaces you have intuition for — spheres, tori, circles — are path-connected.

Path-connectedness implies connectedness, but the converse fails. The classic counterexample is the **topologist's sine curve**: the closure of the graph of sin(1/x) for x > 0. This set is connected — you cannot separate it into two open pieces — but it is not path-connected because no continuous path can cross from the oscillating part to the limit segment on the y-axis. The oscillation becomes infinitely rapid as x → 0, preventing any path from reaching the y-axis without "jumping." This example shows that connectedness is a weaker condition, and path-connectedness is the right hypothesis when you need to actually construct a path between points.

Path-connectedness is the entry point to **algebraic topology** because paths compose. If γ₁ goes from p to q and γ₂ goes from q to r, then concatenating them gives a path from p to r (reparametrize so γ₁ runs over [0, 1/2] and γ₂ over [1/2, 1]). The set of paths in a space, up to continuous deformation, organizes into algebraic structures — the **fundamental group** being the first. This is why path-connectedness is a prerequisite to homotopy theory: before asking how paths deform, you need to know paths exist between any two points.
