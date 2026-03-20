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

## Explainer

You already know what open sets are and how they define a topology on a set X. Now suppose you have a subset A ⊆ X. You want to do topology *within* A — to talk about what's open, what converges, what's continuous, all "relative to A." The **subspace topology** (or **relative topology**) is the natural way to do this: declare a subset V ⊆ A to be open in A if and only if V = A ∩ U for some set U open in the ambient space X. You are inheriting topological structure from X, restricted to what's visible from inside A.

A simple example makes this concrete. Take X = ℝ with the usual topology, and A = [0, 1]. What sets are open in A? The interval (0.2, 0.7) is open in both ℝ and A. But what about [0, 0.5)? In ℝ, this is not open — it contains its left endpoint and there's no open ball around 0 that stays in [0, 0.5). But in A it *is* open: [0, 0.5) = [0,1] ∩ (−1, 0.5), an intersection of A with the open set (−1, 0.5). The endpoint 0 is a "boundary" point of ℝ but an "interior" point of [0,1] when we look only at [0,1]. This is the essence of relative topology: openness is a *local* notion, and local means relative to the space you're living in.

The subspace topology is characterized by a universal property: it is the **coarsest topology on A that makes the inclusion map ι: A → X continuous** (equivalently, the finest that is natural from X). Any function f: Y → A is continuous with respect to the subspace topology if and only if the composition ι ∘ f: Y → X is continuous. This means continuity relative to A is equivalent to continuity relative to X, which is exactly the right behavior — you don't want the meaning of continuity to change just because you're restricting attention to a subset.

Closed sets in the subspace topology follow symmetrically: V is closed in A if V = A ∩ C for some closed set C in X. Note that a set can be both open and closed in the subspace (called **clopen**), even if no non-trivial clopen sets exist in X — this is how disconnected subspaces arise. For instance, A = (0,1) ∪ (2,3) in ℝ is disconnected: each piece is both open and closed in the subspace topology, even though ℝ itself is connected. Understanding the subspace topology is foundational because almost every construction in topology — compact subsets, connected components, manifold charts — is defined as a statement about the subspace topology on a subset of a larger ambient space.


