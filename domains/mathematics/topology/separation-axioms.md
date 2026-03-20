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

## Explainer

When you first encountered open sets, the examples were mostly familiar spaces — ℝ, intervals, metric spaces — where distinct points have plenty of room between them. But a topology can in principle put any collection of sets on a space and call them open, including pathological ones where distinct points are topologically indistinguishable. The **separation axioms** are a hierarchy of conditions that progressively rule out these pathologies by requiring that the topology can separate points or sets from one another using open sets.

**T₀ (Kolmogorov)** is the weakest: for any two distinct points x and y, there exists an open set containing one but not the other. This rules out the trivial topology where the only open sets are ∅ and X — in that topology, every point looks identical. **T₁ (Fréchet)** strengthens this: for any two distinct points x and y, there exist open sets separating *each* from the other — one containing x but not y, and one containing y but not x. In T₁ spaces, every singleton {x} is a closed set, because its complement is the intersection of all open sets containing each other point, which is open. Finite spaces with discrete topology are T₁; in fact T₁ is often described as "points are closed."

**T₂ (Hausdorff)** is the most commonly invoked axiom in analysis and geometry: for any two distinct points x and y, there exist *disjoint* open sets U containing x and V containing y. Hausdorff means points can be *simultaneously* separated — they each have their own private open neighborhood with no overlap. Every metric space is Hausdorff (just take balls of radius half the distance between the points). Most spaces mathematicians work with day-to-day are Hausdorff, which is why limits of sequences are unique in these spaces: if xₙ → x and xₙ → y with x ≠ y in a Hausdorff space, the disjoint open sets around x and y eventually exclude the sequence, giving a contradiction.

**T₃ (Regular)** and **T₄ (Normal)** push the separation from points to closed sets. T₃ (usually required in combination with T₁, giving "regular Hausdorff" spaces, also called T₃ spaces) separates a point from a closed set not containing it by disjoint open sets. T₄ (normal, combined with T₁) separates any two disjoint closed sets by disjoint open sets. The landmark theorem here is **Urysohn's lemma**: a space is T₄ if and only if any two disjoint closed sets can be separated by a continuous real-valued function — a function that equals 0 on one closed set and 1 on the other. This connects the purely topological separation axiom to the existence of continuous functions, which is why normality (T₄) is essential for results like Tietze's extension theorem and the construction of partitions of unity in differential geometry.
