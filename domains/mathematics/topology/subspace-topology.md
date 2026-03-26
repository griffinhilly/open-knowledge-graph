---
id: subspace-topology
title: Subspace Topology
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
- id: subbasis-topology
  type: soft
builds-toward:
- product-topology
- quotient-topology
tags:
- subspace
- relative-topology
- induced-topology
stage: advanced
status: validated
---
# Subspace Topology

## Core Idea
The subspace topology on a subset A of a topological space X is defined by taking intersections of open sets in X with A. This makes A itself a topological space and ensures that the inclusion map is continuous. It provides a natural way to inherit topological structure from a larger space.

## Questions

```yaml
- question: "Let A = [0, 1] ⊆ ℝ with the standard topology. Is the set [0, 1/2) open in A with the subspace topology?"
  type: multiple-choice
  options:
    - "No — 0 is a boundary point of [0, 1/2) in ℝ, so it cannot be open in any topology"
    - "Yes — because [0, 1/2) = (−1, 1/2) ∩ [0, 1], and (−1, 1/2) is open in ℝ"
    - "No — open sets in A must also be open in ℝ"
    - "Yes, but only if A is given the discrete topology"
  answer: 1
  explanation: "The subspace topology on A consists of all sets of the form U ∩ A where U is open in ℝ. The set (−1, 1/2) is open in ℝ, and (−1, 1/2) ∩ [0, 1] = [0, 1/2). So [0, 1/2) is open in A. The key insight: openness is *relative to the space you are working in*. Within A's own topology, the point 0 has an open neighborhood [0, ε) in A — it is surrounded by open sets in A. Option A is the common confusion: it evaluates openness from ℝ's perspective rather than A's. The subspace topology explicitly allows A to have open sets that contain 'boundary' points of A as seen from ℝ."

- question: "The subspace topology on A ⊆ X is characterized by which universal property?"
  type: multiple-choice
  options:
    - "It is the largest topology on A making the inclusion map ι: A → X continuous"
    - "It is the smallest (coarsest) topology on A making the inclusion map ι: A → X continuous — and a map f: B → A is continuous if and only if the composition ι ∘ f: B → X is continuous"
    - "It ensures every subset of A is open, making any map into A continuous"
    - "It copies every open set of X onto A without modification"
  answer: 1
  explanation: "The subspace topology is the *initial topology* with respect to the inclusion map — the coarsest (fewest open sets) topology on A making ι continuous. It cannot be made coarser without breaking the continuity of ι. The universal property states that to check continuity of a map f: B → A, it is equivalent to check that ι ∘ f: B → X is continuous. This is why the subspace topology is 'right': it is the natural choice forced by requiring the inclusion to be continuous. Option A has the direction backwards — the largest topology on A would be discrete, which gives ι: A → X continuity trivially but imposes more open sets than necessary."

- question: "A subset C ⊆ A is closed in A (with the subspace topology) if and only if C = F ∩ A for some set F that is closed in X."
  type: true-false
  answer: true
  explanation: "This follows directly from the definition. A set is closed if its complement is open. C is closed in A iff A \\ C is open in A iff A \\ C = U ∩ A for some open U in X. Taking complements: C = A \\ (U ∩ A) = A ∩ (X \\ U). Let F = X \\ U, which is closed in X. Then C = F ∩ A. The same structure that defines open sets in A — intersecting open sets of X with A — gives an analogous description of closed sets."

- question: "If U is open in the subspace topology on A ⊆ X, then U is expected to also be open in X."
  type: true-false
  answer: false
  explanation: "This is the key subtlety of subspace topology: open in A does not imply open in X. A = [0, 1] with the subspace topology from ℝ: the set [0, 1/2) is open in A (it is (−1, 1/2) ∩ [0, 1]) but is not open in ℝ — it contains 0, which has no open interval around it lying entirely in [0, 1/2). Openness is always relative to a specific topology on a specific space. When we say U is open in A, we mean U belongs to the subspace topology τ_A, not that U belongs to the original topology τ on X."

- question: "Explain why, in the subspace topology on A = [0, 1] ⊆ ℝ, the endpoint 0 is an interior point of A even though it is a boundary point of [0, 1] when viewed from ℝ."
  type: short-answer
  answer: "Interior in the subspace topology means 0 has an open neighborhood *within A's topology* that contains only points of A. The set [0, ε) = (−ε, ε) ∩ [0, 1] is open in A for any ε > 0, and it is a neighborhood of 0 lying entirely within A. Since A only 'sees' its own topology — it does not look outside itself to ℝ — 0 is surrounded by open sets within A. The concept of interior is always relative: a point is interior if it has an open neighborhood in the topology of the space it belongs to. From ℝ's perspective, 0 is a boundary point of [0, 1] because any open interval around 0 in ℝ contains points outside [0, 1]. But once we restrict to A, those external points no longer exist in our space, and 0 gains interior status."
```

## Explainer

Given a topological space (X, τ) and a subset A ⊆ X, the **subspace topology** (also called the **induced** or **relative topology**) on A is the collection τ_A = {U ∩ A : U ∈ τ}. Each "open set" in A is the shadow that an open set of X casts onto A. This is the unique topology on A for which the inclusion map ι: A → X (sending each point to itself) is continuous and is in a precise sense the "smallest" such topology. The definition is forced by the requirement that pulling back open sets along ι must yield open sets in A.

The most instructive examples show that "open in A" does not mean "open in X." Consider A = [0, 1] inside X = ℝ with the standard topology. The set [0, 1/2) is **open in A** because it equals (−1, 1/2) ∩ [0, 1], and (−1, 1/2) is open in ℝ. But [0, 1/2) is not open in ℝ, since it contains the boundary point 0 with no interval around 0 lying entirely within [0, 1/2). This is essential: when you restrict your perspective to A, the endpoints of A behave like interior points of A, because you are only ever asking whether a set is open relative to A's own topology, not X's. Similarly, {0} is open in A if A has the discrete subspace topology (any single point is U ∩ A for a suitably narrow open U), but {0} is not open in ℝ.

The subspace topology also interacts cleanly with closures and continuous maps. A set C ⊆ A is **closed in A** if and only if C = F ∩ A for some closed set F in X. A function f: B → A (where B is some other space) is continuous when we give A the subspace topology if and only if the composition ι ∘ f: B → X is continuous — this is the **universal property** of the subspace topology. It says: to check continuity into A, you only need to check continuity into the larger space X. This universality is what makes the subspace topology the "right" choice: any other topology on A would either break the continuity of the inclusion or force more maps to be continuous than should be.

Understanding the subspace topology is a prerequisite for understanding product and quotient topologies, which also satisfy analogous universal properties (but for projections and quotient maps respectively). Together, they form the three fundamental ways to build new topological spaces from old ones. The pattern — define the topology to make a canonical map continuous, and prove it is the coarsest (or finest) topology with that property — recurs throughout topology and category theory as the notion of an **initial** or **final** topology, and recognizing it here is the first step toward that broader framework.


