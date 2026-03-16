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
status: draft
---

# Topological Invariants

## Core Idea
Topological invariants are properties preserved under homeomorphisms—if two spaces are homeomorphic, they must share the same invariants. Examples include compactness, connectedness, dimension, and the fundamental group. Invariants provide tools to prove that two spaces are not homeomorphic.

## Explainer

Homeomorphisms, which you've studied, are the topology-preserving isomorphisms: bijections f: X → Y such that both f and f⁻¹ are continuous. Because homeomorphisms preserve open sets in both directions, any property defined purely in terms of open sets must be preserved under homeomorphism. A **topological invariant** is exactly such a property — one that every homeomorphic copy of a space shares. Invariants are the tools that let you answer the fundamental classification question: are these two spaces topologically the same or different?

The simplest invariants are qualitative properties. **Compactness** (every open cover has a finite subcover), **connectedness** (the space cannot be split into two disjoint nonempty open sets), and **path-connectedness** (any two points can be joined by a continuous path) are all preserved under homeomorphism, because homeomorphisms pull open covers back and push connected decompositions forward. These immediately yield non-homeomorphism proofs: the closed interval [0,1] is compact, the open interval (0,1) is not, so they are not homeomorphic. The real line ℝ is connected; two disjoint copies of ℝ are not; so these are not homeomorphic.

Finer invariants distinguish spaces that share the simple ones. Consider the circle S¹ and the figure-eight: both are compact and path-connected. They differ in their **fundamental group** π₁, which you will encounter next. The fundamental group of S¹ is ℤ: loops around the circle are classified by how many times they wind, and winding number is an integer. The fundamental group of the figure-eight is a free group on two generators — much richer, because loops can traverse either lobe. Since the fundamental groups are different, S¹ and the figure-eight are not homeomorphic. The fundamental group is also why the circle and the disk differ: every loop in the disk can be contracted to a point (trivial fundamental group), but loops winding around the circle cannot (fundamental group ℤ).

The strategy for proving non-homeomorphism is always the same: find an invariant that the two spaces don't share. A particularly powerful technique is to examine what happens when you remove a point. Removing a single point from ℝ gives two disconnected components; removing a single point from ℝ² leaves a path-connected space. This proves ℝ ≇ ℝ² — the real line and the plane are not homeomorphic — without needing to compute any algebraic invariant. More generally, **dimension** is a topological invariant (ℝⁿ ≇ ℝᵐ for n ≠ m), though proving this rigorously requires substantial machinery. The practical takeaway is asymmetric: shared invariants cannot prove homeomorphism (you might lack fine enough tools), but a single differing invariant proves non-homeomorphism immediately.
