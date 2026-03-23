---
id: topological-invariants
title: Topological Invariants
domain: mathematics
course: topology
prerequisites:
- id: homeomorphisms-topological-equivalence
  type: hard
builds-toward:
- fundamental-group-definition
- classification-compact-surfaces
tags:
- invariants
- properties-preserved
- homeomorphisms
stage: advanced
status: validated
---

# Topological Invariants

## Core Idea
Topological invariants are properties preserved under homeomorphisms—if two spaces are homeomorphic, they must share the same invariants. Examples include compactness, connectedness, dimension, and the fundamental group. Invariants provide tools to prove that two spaces are not homeomorphic.

## Questions

```yaml
- question: "You compute that spaces X and Y are both compact, path-connected, and have trivial fundamental group. What can you conclude?"
  type: multiple-choice
  options:
    - "X and Y are homeomorphic — they share all the key invariants"
    - "X and Y are not homeomorphic — identical invariants on distinct spaces imply a contradiction"
    - "Sharing these invariants is insufficient to establish homeomorphism; they may still differ on finer invariants"
    - "X and Y are homotopy equivalent but not necessarily homeomorphic, and homotopy equivalence implies homeomorphism"
  answer: 2
  explanation: "Topological invariants work asymmetrically: a single differing invariant proves non-homeomorphism, but no finite collection of shared invariants proves homeomorphism. The disk D² and the sphere S² are both compact, path-connected, and simply connected (trivial fundamental group), yet they are not homeomorphic. Proving homeomorphism requires constructing an explicit homeomorphism, not just accumulating invariant evidence."

- question: "To prove that the real line ℝ is not homeomorphic to the plane ℝ², the most direct argument is:"
  type: multiple-choice
  options:
    - "Show that ℝ is simply connected while ℝ² is not"
    - "Remove a single point from each: the punctured ℝ is disconnected, but the punctured ℝ² remains path-connected"
    - "Compute the fundamental groups: π₁(ℝ) = ℤ while π₁(ℝ²) = 0"
    - "Show that ℝ has Euler characteristic 1 while ℝ² has Euler characteristic 2"
  answer: 1
  explanation: "Removing a single point from ℝ leaves two disjoint open rays — the space is disconnected. Removing a single point from ℝ² leaves a punctured plane, which is still path-connected (you can route any path around the missing point). Since connectedness after point removal is a topological invariant (it depends only on the homeomorphism type), ℝ and ℝ² cannot be homeomorphic. This elegant argument requires no algebraic invariants. Note: both ℝ and ℝ² are simply connected with trivial fundamental group, so option C is actually wrong."

- question: "If two topological spaces share the same fundamental group, they must be homeomorphic."
  type: true-false
  answer: false
  explanation: "Invariants establish necessary conditions for homeomorphism, not sufficient ones. Two spaces can share their fundamental group — and even all their homotopy groups — while still failing to be homeomorphic. A single differing invariant rules out homeomorphism; shared invariants only tell you the spaces might be homeomorphic. Proving homeomorphism requires constructing an explicit bijective continuous map with continuous inverse."

- question: "The open interval (0,1) and the closed interval [0,1] are not homeomorphic because (0,1) is unbounded while [0,1] is bounded."
  type: true-false
  answer: false
  explanation: "Boundedness is not a topological invariant — it depends on how the space is embedded in ℝ, which is not preserved by homeomorphisms. The correct reason is that [0,1] is compact (every open cover has a finite subcover) and (0,1) is not compact. Compactness IS a topological invariant because homeomorphisms preserve open sets in both directions and hence preserve the finite subcover property."

- question: "Explain the asymmetry in using topological invariants: why can a single differing invariant immediately prove non-homeomorphism, yet no finite list of shared invariants proves homeomorphism?"
  type: short-answer
  answer: "A homeomorphism must preserve every topological property without exception. If spaces differ on even one invariant, no homeomorphism can exist. But homeomorphism is stronger than sharing invariants: two spaces might agree on every invariant we have checked and still differ on one we haven't computed. Proving homeomorphism requires constructing the map itself."
  explanation: "This asymmetry is why topological classification is hard in the positive direction but often easy in the negative direction. Counterexample: the closed disk and the sphere S² agree on compactness, path-connectedness, and simple connectedness, yet are not homeomorphic (the disk has a boundary, the sphere does not). 'Boundary' is another topological invariant that distinguishes them. The lesson: every non-homeomorphism proof needs only one witness; every homeomorphism proof needs a complete construction."
```

## Explainer

Homeomorphisms, which you've studied, are the topology-preserving isomorphisms: bijections f: X → Y such that both f and f⁻¹ are continuous. Because homeomorphisms preserve open sets in both directions, any property defined purely in terms of open sets must be preserved under homeomorphism. A **topological invariant** is exactly such a property — one that every homeomorphic copy of a space shares. Invariants are the tools that let you answer the fundamental classification question: are these two spaces topologically the same or different?

The simplest invariants are qualitative properties. **Compactness** (every open cover has a finite subcover), **connectedness** (the space cannot be split into two disjoint nonempty open sets), and **path-connectedness** (any two points can be joined by a continuous path) are all preserved under homeomorphism, because homeomorphisms pull open covers back and push connected decompositions forward. These immediately yield non-homeomorphism proofs: the closed interval [0,1] is compact, the open interval (0,1) is not, so they are not homeomorphic. The real line ℝ is connected; two disjoint copies of ℝ are not; so these are not homeomorphic.

Finer invariants distinguish spaces that share the simple ones. Consider the circle S¹ and the figure-eight: both are compact and path-connected. They differ in their **fundamental group** π₁, which you will encounter next. The fundamental group of S¹ is ℤ: loops around the circle are classified by how many times they wind, and winding number is an integer. The fundamental group of the figure-eight is a free group on two generators — much richer, because loops can traverse either lobe. Since the fundamental groups are different, S¹ and the figure-eight are not homeomorphic. The fundamental group is also why the circle and the disk differ: every loop in the disk can be contracted to a point (trivial fundamental group), but loops winding around the circle cannot (fundamental group ℤ).

The strategy for proving non-homeomorphism is always the same: find an invariant that the two spaces don't share. A particularly powerful technique is to examine what happens when you remove a point. Removing a single point from ℝ gives two disconnected components; removing a single point from ℝ² leaves a path-connected space. This proves ℝ ≇ ℝ² — the real line and the plane are not homeomorphic — without needing to compute any algebraic invariant. More generally, **dimension** is a topological invariant (ℝⁿ ≇ ℝᵐ for n ≠ m), though proving this rigorously requires substantial machinery. The practical takeaway is asymmetric: shared invariants cannot prove homeomorphism (you might lack fine enough tools), but a single differing invariant proves non-homeomorphism immediately.
