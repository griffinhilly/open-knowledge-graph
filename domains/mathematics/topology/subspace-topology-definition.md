---
id: subspace-topology-definition
title: Subspace Topology and Relative Topology
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
- id: subspace-topology
  type: soft
tags:
- subspace
- induced-topology
stage: advanced
status: draft
---

# Subspace Topology and Relative Topology

## Core Idea
Given a subspace A ⊆ X, the subspace topology on A consists of sets of the form A ∩ U where U is open in X. Open sets in A are exactly the intersections of A with open sets in X; closed sets in A are intersections with closed sets in X. Subspace topology preserves 'relative' topological properties; it is the finest topology making the inclusion continuous.

## Questions

```yaml
- question: "Let A = [0, 1] ⊆ ℝ with the standard topology. Which of the following sets is open in the subspace topology on A but NOT open in ℝ?"
  type: multiple-choice
  options:
    - "(0.2, 0.7), an open interval in the interior of A"
    - "[0, 0.5), the half-open interval starting at the left endpoint of A"
    - "(0, 1), the open interval missing both endpoints"
    - "(0.3, 0.8), another open interval in the interior of A"
  answer: 1
  explanation: "[0, 0.5) is open in A because [0, 0.5) = [0,1] ∩ (−1, 0.5), and (−1, 0.5) is open in ℝ. But [0, 0.5) is not open in ℝ — the point 0 has no open ball in ℝ contained within [0, 0.5). This is the essence of subspace topology: the 'boundary' of [0,1] in ℝ (the endpoint 0) becomes an 'interior' point when we restrict attention to [0,1]. Openness is relative to the ambient space."

- question: "A function f: Y → A is continuous with respect to the subspace topology on A ⊆ X if and only if:"
  type: multiple-choice
  options:
    - "f maps open sets of Y to open sets of X"
    - "The composition ι ∘ f: Y → X is continuous, where ι: A → X is the inclusion map"
    - "f is uniformly continuous on every compact subset of A"
    - "f maps closed sets of Y to closed sets of A"
  answer: 1
  explanation: "The subspace topology is the coarsest topology making the inclusion ι: A → X continuous. As a consequence, f: Y → A is continuous iff ι ∘ f: Y → X is continuous. This is the 'right' behavior — continuity relative to A should be equivalent to continuity relative to X when composed with inclusion. It means you don't need to check membership in A separately."

- question: "A subset V of a subspace A ⊆ X can be both open and closed in the subspace topology even if the only clopen sets in the ambient space X are ∅ and X itself."
  type: true-false
  answer: true
  explanation: "This is how disconnected subspaces arise. Consider A = (0,1) ∪ (2,3) ⊆ ℝ. Each piece is open in A (as an intersection of A with an open set of ℝ) and also closed (its complement in A is the other piece, which is open). Yet ℝ itself is connected — no proper nonempty subset is clopen. The subspace can have richer clopen structure than the ambient space because 'inside A' is a different vantage point."

- question: "If V ⊆ A is open in the subspace topology on A ⊆ X, then V must also be open in X."
  type: true-false
  answer: false
  explanation: "The set [0, 0.5) is open in [0,1] (as a subspace of ℝ) but not open in ℝ. The subspace topology declares V open in A if V = A ∩ U for *some* open U in X — but V itself need not be open in X. The intersection with A can clip off boundary points of U that prevent V from being open in the ambient space."

- question: "Why does the subspace topology define open sets in A as intersections A ∩ U (with U open in X), rather than simply taking the open sets of X that happen to be contained in A?"
  type: short-answer
  answer: "Taking only open subsets of X that are contained in A would miss natural 'interior' structure of A. For example, [0, 0.5) is naturally open relative to [0,1] — the point 0 has neighborhoods entirely within A — but no open set of ℝ contained in [0,1] can include 0. The intersection definition captures the correct notion of 'open relative to A': it is the minimal definition that makes the inclusion map ι: A → X continuous."
  explanation: "The universal property confirms this: the subspace topology is the coarsest topology on A making ι continuous. For ι to be continuous, the preimage of every open U in X under ι must be open in A — and that preimage is A ∩ U. Using only open sets of X that are subsets of A would be too coarse to satisfy this. The intersection definition is not arbitrary; it is forced by the requirement that continuity relative to A be equivalent to continuity relative to X."
```

## Explainer

You already know what open sets are and how they define a topology on a set X. Now suppose you have a subset A ⊆ X. You want to do topology *within* A — to talk about what's open, what converges, what's continuous, all "relative to A." The **subspace topology** (or **relative topology**) is the natural way to do this: declare a subset V ⊆ A to be open in A if and only if V = A ∩ U for some set U open in the ambient space X. You are inheriting topological structure from X, restricted to what's visible from inside A.

A simple example makes this concrete. Take X = ℝ with the usual topology, and A = [0, 1]. What sets are open in A? The interval (0.2, 0.7) is open in both ℝ and A. But what about [0, 0.5)? In ℝ, this is not open — it contains its left endpoint and there's no open ball around 0 that stays in [0, 0.5). But in A it *is* open: [0, 0.5) = [0,1] ∩ (−1, 0.5), an intersection of A with the open set (−1, 0.5). The endpoint 0 is a "boundary" point of ℝ but an "interior" point of [0,1] when we look only at [0,1]. This is the essence of relative topology: openness is a *local* notion, and local means relative to the space you're living in.

The subspace topology is characterized by a universal property: it is the **coarsest topology on A that makes the inclusion map ι: A → X continuous** (equivalently, the finest that is natural from X). Any function f: Y → A is continuous with respect to the subspace topology if and only if the composition ι ∘ f: Y → X is continuous. This means continuity relative to A is equivalent to continuity relative to X, which is exactly the right behavior — you don't want the meaning of continuity to change just because you're restricting attention to a subset.

Closed sets in the subspace topology follow symmetrically: V is closed in A if V = A ∩ C for some closed set C in X. Note that a set can be both open and closed in the subspace (called **clopen**), even if no non-trivial clopen sets exist in X — this is how disconnected subspaces arise. For instance, A = (0,1) ∪ (2,3) in ℝ is disconnected: each piece is both open and closed in the subspace topology, even though ℝ itself is connected. Understanding the subspace topology is foundational because almost every construction in topology — compact subsets, connected components, manifold charts — is defined as a statement about the subspace topology on a subset of a larger ambient space.


