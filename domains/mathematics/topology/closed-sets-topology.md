---
id: closed-sets-topology
title: Closed Sets in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: topological-spaces-definition
  type: hard
builds-toward:
- closure-interior-boundary
- limit-points-and-accumulation
tags:
- closed-sets
- complements
stage: abstract-reasoning
status: draft
---

# Closed Sets in Topological Spaces

## Core Idea
A set F in a topological space is closed if its complement X \ F is open. Closed sets satisfy the dual property to open sets: they are closed under arbitrary intersections and finite unions.

## Explainer

From your study of topological spaces, you know that a topology on a set X is a collection of **open sets** satisfying three axioms: ∅ and X are open, arbitrary unions of open sets are open, and finite intersections of open sets are open. **Closed sets** are defined purely in terms of open sets — a set F is closed when its complement X \ F is open. This is not a separate structure layered on top of the topology; it is the same topology viewed through complementation.

The relationship between open and closed becomes intuitive with examples. In ℝ with the standard topology, the open interval (0, 1) is open — every point has a small open neighborhood contained in the interval. Its complement (−∞, 0] ∪ [1, ∞) is closed. The closed interval [0, 1] is closed — its complement (−∞, 0) ∪ (1, ∞) is open. A single point {0.5} is closed — its complement is the union of two open rays. Notice that "closed" does not mean "not open": the empty set ∅ and the whole space X are both open and closed simultaneously (called **clopen** sets), and in general a set can be open, closed, both, or neither.

The closure properties of closed sets follow immediately from De Morgan's laws applied to the open set axioms. Arbitrary intersections of closed sets are closed: if each Fα is closed, then its complement is open, and ⋃(X \ Fα) = X \ (⋂Fα) is an arbitrary union of open sets — hence open — so ⋂Fα is closed. Finite unions of closed sets are closed by the dual argument. This is the exact mirror image of open sets, with the quantifiers swapped: open sets support arbitrary unions but only finite intersections; closed sets support arbitrary intersections but only finite unions. The asymmetry between "arbitrary" and "finite" is fundamental to topology and recurs throughout the subject.

Understanding closed sets well is essential for what comes next. The **closure** of a set A is the smallest closed set containing A — equivalently, the intersection of all closed sets containing A. The **interior** of A is the largest open set contained in A. The **boundary** of A sits between them. These notions give you the vocabulary to talk about limits, accumulation points, and continuity in purely topological terms, without any reference to distance or ε-δ arguments — a level of generality that becomes powerful when you move to spaces with no natural metric.
