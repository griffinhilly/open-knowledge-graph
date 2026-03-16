---
id: subspace-topology
title: Subspace Topology
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
builds-toward:
- product-topology
- quotient-topology
tags:
- subspace
- relative-topology
- induced-topology
stage: advanced
status: draft
---

# Subspace Topology

## Core Idea
The subspace topology on a subset A of a topological space X is defined by taking intersections of open sets in X with A. This makes A itself a topological space and ensures that the inclusion map is continuous. It provides a natural way to inherit topological structure from a larger space.

## Explainer

Given a topological space (X, τ) and a subset A ⊆ X, the **subspace topology** (also called the **induced** or **relative topology**) on A is the collection τ_A = {U ∩ A : U ∈ τ}. Each "open set" in A is the shadow that an open set of X casts onto A. This is the unique topology on A for which the inclusion map ι: A → X (sending each point to itself) is continuous and is in a precise sense the "smallest" such topology. The definition is forced by the requirement that pulling back open sets along ι must yield open sets in A.

The most instructive examples show that "open in A" does not mean "open in X." Consider A = [0, 1] inside X = ℝ with the standard topology. The set [0, 1/2) is **open in A** because it equals (−1, 1/2) ∩ [0, 1], and (−1, 1/2) is open in ℝ. But [0, 1/2) is not open in ℝ, since it contains the boundary point 0 with no interval around 0 lying entirely within [0, 1/2). This is essential: when you restrict your perspective to A, the endpoints of A behave like interior points of A, because you are only ever asking whether a set is open relative to A's own topology, not X's. Similarly, {0} is open in A if A has the discrete subspace topology (any single point is U ∩ A for a suitably narrow open U), but {0} is not open in ℝ.

The subspace topology also interacts cleanly with closures and continuous maps. A set C ⊆ A is **closed in A** if and only if C = F ∩ A for some closed set F in X. A function f: B → A (where B is some other space) is continuous when we give A the subspace topology if and only if the composition ι ∘ f: B → X is continuous — this is the **universal property** of the subspace topology. It says: to check continuity into A, you only need to check continuity into the larger space X. This universality is what makes the subspace topology the "right" choice: any other topology on A would either break the continuity of the inclusion or force more maps to be continuous than should be.

Understanding the subspace topology is a prerequisite for understanding product and quotient topologies, which also satisfy analogous universal properties (but for projections and quotient maps respectively). Together, they form the three fundamental ways to build new topological spaces from old ones. The pattern — define the topology to make a canonical map continuous, and prove it is the coarsest (or finest) topology with that property — recurs throughout topology and category theory as the notion of an **initial** or **final** topology, and recognizing it here is the first step toward that broader framework.


