---
id: separation-axioms-t3-regular
title: Regularity (T₃) and Normal Spaces (T₄)
domain: mathematics
course: topology
prerequisites:
- id: hausdorff-spaces
  type: hard
builds-toward:
- urysohn-lemma
- tietze-extension-theorem
tags:
- regularity
- t3
- normal
- t4
- separation
stage: advanced
status: draft
---

# Regularity (T₃) and Normal Spaces (T₄)

## Core Idea
Regular spaces (T₃) allow separation of points from disjoint closed sets by open neighborhoods, while normal spaces (T₄) extend this to separating disjoint closed sets. These axioms enable the existence of continuous functions with prescribed values on closed sets (Tietze extension) and provide flexibility in constructing continuous real-valued functions (Urysohn's lemma).

## Explainer

From your study of Hausdorff spaces (T₂), you know that a space satisfies the T₂ axiom if any two distinct points can be separated by disjoint open sets: given x ≠ y, find open U ∋ x and V ∋ y with U ∩ V = ∅. **Regularity** (T₃) strengthens this: instead of separating two points, you separate a point from a closed set. A space is **regular** if for every point x and every closed set C not containing x, there exist disjoint open sets U and V with x ∈ U and C ⊆ V. A **T₃ space** is both regular and T₁ (singletons are closed). The hierarchy so far: T₃ implies T₂ implies T₁. Regularity is strictly stronger because you are now matching an entire closed set with a single open set V, which demands more of the topology than separating two individual points.

**Normality** (T₄) pushes one step further: X is normal if any two disjoint closed sets A and B can be separated by disjoint open sets. A **T₄ space** is both normal and T₁. Every metric space is normal: given disjoint closed sets A and B, the open sets U = {x : d(x,A) < d(x,B)} and V = {x : d(x,B) < d(x,A)} are disjoint and cover A and B respectively (the triangle inequality ensures they work). So all the spaces of classical analysis are normal, which is why T₄ feels like the natural baseline for many theorems.

The payoff for T₄ is the pair of theorems it enables. **Urysohn's lemma** states: in a normal space, given disjoint closed sets A and B, there exists a continuous function f: X → [0,1] with f(A) = 0 and f(B) = 1. This is remarkable — it constructs a continuous function from purely topological data, with no metric or formula. The proof builds f by inductively finding open sets U_r for every dyadic rational r ∈ [0,1], arranged so that A ⊆ U_0 and X \ B ⊇ U_1 and U_r ⊆ closure(U_s) whenever r < s. Normality is invoked at every inductive step to find each new separating open set. The function f(x) = inf{r : x ∈ U_r} then turns out to be continuous.

The **Tietze extension theorem** follows from Urysohn and completes the picture: in a normal space, every continuous real-valued function defined on a closed subspace extends to a continuous function on the whole space. Together, Urysohn and Tietze show that T₄ is the threshold where topology becomes rich enough to guarantee the existence of continuous functions with prescribed behavior on closed sets. This matters practically: when you work in abstract settings like manifolds or function spaces, verifying normality (or the related condition of complete regularity, T₃.₅) is often the first step that legitimizes the use of partition-of-unity arguments, bump functions, and other tools that make analysis flexible.
