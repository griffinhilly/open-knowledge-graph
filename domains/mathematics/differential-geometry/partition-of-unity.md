---
id: partition-of-unity
title: Partition of Unity
domain: mathematics
course: differential-geometry
prerequisites:
  - id: smooth-manifolds
    type: hard
  - id: compactness-hausdorff-spaces
    type: soft
  - id: metric-spaces-definition
    type: soft
tags:
  - partition-of-unity
  - bump-functions
  - paracompactness
  - localization
stage: advanced
status: validated
---

# Partition of Unity

## Core Idea
A partition of unity is a collection of smooth non-negative functions {ρα} on a manifold that sum to 1 everywhere, each supported in a single coordinate chart. Partitions of unity allow you to patch together local constructions — metrics, forms, connections — into global objects. Their existence on smooth manifolds (guaranteed by paracompactness and the existence of smooth bump functions) is what makes the passage from local to global possible throughout differential geometry.

## Questions

```yaml
- question: "A partition of unity subordinate to an open cover {Uα} of a manifold M is a collection {ρα} of smooth functions satisfying three conditions. Which of the following is NOT one of them?"
  type: multiple-choice
  options:
    - "Each ρα ≥ 0 everywhere on M"
    - "The support of each ρα is contained in the corresponding Uα"
    - "Σα ρα(p) = 1 for every p ∈ M"
    - "Each ρα is strictly positive on all of Uα"
  answer: 3
  explanation: "Option D is not required and is generally false. Each ρα must be non-negative and supported inside Uα, but it can be zero on much of Uα — it just needs to be nonzero somewhere inside Uα. The three actual conditions are: (1) ρα ≥ 0, (2) supp(ρα) ⊂ Uα, and (3) Σα ρα = 1 everywhere. The sum is locally finite (only finitely many ρα are nonzero near any point), which makes the sum well-defined. The functions need not cover each Uα uniformly."

- question: "Partitions of unity exist on every smooth manifold."
  type: true-false
  answer: true
  explanation: "This is a theorem, not obvious. The proof requires two ingredients: (1) smooth manifolds are paracompact (every open cover has a locally finite refinement), which follows from second-countability; and (2) smooth bump functions exist — compactly supported smooth functions that are identically 1 on a given compact set. Paracompactness provides a locally finite cover, and bump functions provide the raw material. The bump functions are then normalized (divided by their sum) to produce the partition. This fails for analytic manifolds — analytic bump functions do not exist."

- question: "How are partitions of unity used to construct a Riemannian metric on any smooth manifold?"
  type: short-answer
  answer: "In each coordinate chart (Uα, φα), the standard Euclidean inner product on ℝⁿ pulls back to a Riemannian metric gα on Uα. Using a partition of unity {ρα} subordinate to {Uα}, define g = Σα ρα · gα. This sum is well-defined (locally finite), smooth, and at each point is a convex combination of inner products — hence positive definite. The result is a globally defined Riemannian metric. This construction shows that every smooth manifold admits a Riemannian metric."
  explanation: "The key insight is that the set of inner products on a vector space is convex — a positive combination of inner products is again an inner product. Since partition-of-unity functions are non-negative and sum to 1, the combination g = Σ ρα gα is a convex combination at each point, hence positive definite. This convexity argument works for metrics but fails for other structures (like symplectic forms) where the 'space of structures' is not convex."

- question: "Partitions of unity do not exist in the analytic (Cω) category because analytic bump functions do not exist."
  type: true-false
  answer: true
  explanation: "A real-analytic function that vanishes on an open set is identically zero (by the identity theorem). Therefore, a compactly supported analytic function that is not identically zero cannot exist — it would need to vanish outside a compact set but be nonzero inside. Since bump functions are the building blocks of partitions of unity, the partition-of-unity technique is fundamentally a smooth (C∞) phenomenon. This is one reason smooth manifolds are more flexible than analytic manifolds, and why many constructions in differential geometry require C∞ smoothness."
```

## Explainer

Many constructions in differential geometry start locally — in a single coordinate chart, it is easy to define a metric, a connection, or a volume form using the coordinate structure of ℝⁿ. The challenge is patching these local constructions into a coherent global object. **Partitions of unity** are the glue that makes this possible. They are collections of smooth functions that decompose the manifold into weighted pieces, each living inside a single chart.

A **smooth bump function** is the fundamental building block: a smooth non-negative function that equals 1 on a compact set K and vanishes outside a slightly larger open set. Such functions exist in the smooth category because C∞ functions can be "flat" (all derivatives zero) at a point without being identically zero. The standard construction uses the function e^{-1/x} for x > 0 and 0 for x ≤ 0, which is smooth but not analytic. Starting from bump functions, you construct a partition of unity subordinate to any open cover by taking bump functions for each chart and normalizing by dividing by their sum.

The construction of a **Riemannian metric** on any smooth manifold illustrates the power of the technique. Each chart provides a local metric (the pullback of the Euclidean metric on ℝⁿ). These local metrics may disagree on overlaps, but the partition-of-unity average g = Σ ρα gα produces a globally defined metric. This works because the set of positive-definite inner products is **convex**: any positive combination of inner products is again an inner product. The same technique constructs connections, embeddings into Euclidean space (the Nash embedding theorem uses partitions of unity), and many other global geometric objects.

Not every structure can be patched with partitions of unity. The technique works for structures defined by **convex** conditions (metrics, connections) but fails for structures defined by **non-convex** conditions. Symplectic forms, for instance, cannot be averaged — a convex combination of symplectic forms need not be symplectic. Complex structures similarly resist partition-of-unity arguments. This is why some geometric structures (Riemannian metrics) always exist on smooth manifolds while others (symplectic forms, complex structures) impose genuine topological constraints. Understanding which constructions survive the local-to-global passage — and which do not — is one of the organizing themes of differential geometry.
