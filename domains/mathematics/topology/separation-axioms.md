---
id: separation-axioms
title: Separation Axioms (T0 through T4)
domain: mathematics
course: topology
prerequisites:
- id: open-sets-topology
  type: hard
builds-toward:
- hausdorff-spaces
- regular-spaces
- normal-spaces
tags:
- separation
- axioms
stage: formal-systems
status: draft
---

# Separation Axioms (T0 through T4)

## Core Idea
Separation axioms measure how well a topology distinguishes points and sets. T₀ through T₄ range from weak separation (different neighborhoods) to strong separation (disjoint closed sets).

## Questions

```yaml
- question: "In a topological space, you want to guarantee that every convergent sequence has at most one limit. Which separation axiom is sufficient (and necessary) for this?"
  type: multiple-choice
  options:
    - "T₀ (Kolmogorov) — there exists an open set distinguishing any two points"
    - "T₁ (Fréchet) — for any two points, each has an open set not containing the other"
    - "T₂ (Hausdorff) — any two distinct points have disjoint open neighborhoods"
    - "T₄ (Normal) — any two disjoint closed sets can be separated by open sets"
  answer: 2
  explanation: "T₂ (Hausdorff) is exactly what guarantees unique limits. If xₙ → x and xₙ → y with x ≠ y, the disjoint open sets U ∋ x and V ∋ y (guaranteed by T₂) eventually exclude all terms of the sequence simultaneously — a contradiction. In T₁ spaces, the open sets separating two points may overlap, allowing a sequence to satisfy both neighborhoods. Disjointness is the critical word."

- question: "In a T₁ space, every singleton set {x} is closed. Which argument correctly establishes this?"
  type: multiple-choice
  options:
    - "T₁ implies T₂, and in Hausdorff spaces all singletons are closed by a separate theorem"
    - "Every singleton is open in T₁ spaces, so its complement is closed by definition"
    - "For every y ≠ x, the T₁ condition provides an open set containing y but not x; the complement of {x} is a union of such open sets, hence open — making {x} closed"
    - "In T₁ spaces the topology is discrete, so every set including {x} is both open and closed"
  answer: 2
  explanation: "The complement of {x} is X\\{x} = ∪_{y≠x} U_y, where each U_y is an open set given by T₁ that contains y but not x. A union of open sets is open, so X\\{x} is open, meaning {x} is closed. T₁ does not imply T₂, and T₁ spaces need not be discrete — in the cofinite topology on an infinite set, singletons are closed (complements are cofinite = open) but the space is T₁ and not T₂."

- question: "Every metric space is a Hausdorff (T₂) topological space."
  type: true-false
  answer: true
  explanation: "Given two distinct points x and y in a metric space with d(x,y) = r > 0, the open balls B(x, r/2) and B(y, r/2) are disjoint open neighborhoods. If some point z were in both, the triangle inequality gives r = d(x,y) ≤ d(x,z) + d(z,y) < r/2 + r/2 = r, a contradiction. This construction works in any metric space, so all metric spaces — including ℝⁿ, normed vector spaces, and function spaces with a metric — are Hausdorff."

- question: "Every Hausdorff (T₂) space is also a normal (T₄) space."
  type: true-false
  answer: false
  explanation: "This is false. T₄ requires separating any two disjoint *closed sets* by disjoint open sets; T₂ only requires separating *points*. There exist Hausdorff spaces that are not normal — a classic example is the Sorgenfrey plane (ℝ² with the lower-limit topology on each coordinate). The two axes are disjoint closed sets that cannot be separated by disjoint open sets in that topology. The implications run T₄ → T₃ → T₂ → T₁ → T₀, but none of these arrows reverses."

- question: "Explain why Urysohn's lemma makes the normal (T₄) separation axiom especially significant for analysis, beyond the purely topological separation of closed sets."
  type: short-answer
  answer: "Urysohn's lemma states that a space is T₄ if and only if any two disjoint closed sets A and B can be separated by a continuous real-valued function f with f(A)=0 and f(B)=1. This bridges the gap between purely topological separation (open sets) and the existence of continuous functions. Normality is the minimum condition needed to construct real-valued continuous functions with prescribed values on closed sets, which underlies results like the Tietze extension theorem (extending continuous functions from closed subsets) and partitions of unity used throughout differential geometry and functional analysis."
  explanation: "The key insight is that separation axioms are not just about keeping points or sets topologically distinct — the stronger axioms actually determine what continuous functions exist. T₂ ensures uniqueness of limits but says little about continuous functions from the space to ℝ. T₄ is the threshold at which the topological structure is rich enough to support continuous real-valued functions with precise controlled behavior on closed sets, making it the natural setting for many analytic constructions."
```

## Explainer

When you first encountered open sets, the examples were mostly familiar spaces — ℝ, intervals, metric spaces — where distinct points have plenty of room between them. But a topology can in principle put any collection of sets on a space and call them open, including pathological ones where distinct points are topologically indistinguishable. The **separation axioms** are a hierarchy of conditions that progressively rule out these pathologies by requiring that the topology can separate points or sets from one another using open sets.

**T₀ (Kolmogorov)** is the weakest: for any two distinct points x and y, there exists an open set containing one but not the other. This rules out the trivial topology where the only open sets are ∅ and X — in that topology, every point looks identical. **T₁ (Fréchet)** strengthens this: for any two distinct points x and y, there exist open sets separating *each* from the other — one containing x but not y, and one containing y but not x. In T₁ spaces, every singleton {x} is a closed set, because its complement is the intersection of all open sets containing each other point, which is open. Finite spaces with discrete topology are T₁; in fact T₁ is often described as "points are closed."

**T₂ (Hausdorff)** is the most commonly invoked axiom in analysis and geometry: for any two distinct points x and y, there exist *disjoint* open sets U containing x and V containing y. Hausdorff means points can be *simultaneously* separated — they each have their own private open neighborhood with no overlap. Every metric space is Hausdorff (just take balls of radius half the distance between the points). Most spaces mathematicians work with day-to-day are Hausdorff, which is why limits of sequences are unique in these spaces: if xₙ → x and xₙ → y with x ≠ y in a Hausdorff space, the disjoint open sets around x and y eventually exclude the sequence, giving a contradiction.

**T₃ (Regular)** and **T₄ (Normal)** push the separation from points to closed sets. T₃ (usually required in combination with T₁, giving "regular Hausdorff" spaces, also called T₃ spaces) separates a point from a closed set not containing it by disjoint open sets. T₄ (normal, combined with T₁) separates any two disjoint closed sets by disjoint open sets. The landmark theorem here is **Urysohn's lemma**: a space is T₄ if and only if any two disjoint closed sets can be separated by a continuous real-valued function — a function that equals 0 on one closed set and 1 on the other. This connects the purely topological separation axiom to the existence of continuous functions, which is why normality (T₄) is essential for results like Tietze's extension theorem and the construction of partitions of unity in differential geometry.
