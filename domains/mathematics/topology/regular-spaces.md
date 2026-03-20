---
id: regular-spaces
title: Regular Spaces (T3 Spaces)
domain: mathematics
course: topology
prerequisites:
- id: separation-axioms
  type: hard
- id: closed-sets-topology
  type: hard
builds-toward:
- urysohns-lemma
- metrization-theorems
tags:
- regular
- t3
stage: formal-systems
status: draft
---

# Regular Spaces (T3 Spaces)

## Core Idea
A space is regular if for closed F and x ∉ F, there exist disjoint open sets separating them. Regularity separates points from closed sets. Every metric space is regular.

## Explainer

You've already worked through the separation hierarchy: T0 spaces separate points by distinguishing their neighborhoods, T1 spaces ensure single points are closed, and T2 (**Hausdorff**) spaces separate any two distinct points with disjoint open sets. **Regularity** (T3) extends this further: it separates not just points from each other but **points from closed sets**. The axiom is: for any closed set F and any point x ∉ F, there exist disjoint open sets U and V with x ∈ U and F ⊆ V. The point gets its own neighborhood; the entire closed set gets its own neighborhood; they don't overlap.

Why upgrade from T2 to T3? In a Hausdorff space, you can separate any two distinct *points*. But closed sets are typically much larger than single points, and separating a point from an entire closed set is a stronger demand. Every metric space is regular — the construction uses balls: if d(x, F) = r > 0, take open balls of radius r/2 around x and around each point of F. Regularity is the topological abstraction of this key feature of metric spaces that makes analysis behave well.

A common source of confusion is naming. "**Regular**" in most modern usage means the separation condition described above. "**T3**" sometimes means regular *plus* T1 (which requires single points to be closed). The distinction matters because regularity without T1 can produce strange behavior — separation axioms are only meaningful when the topology distinguishes points at all. In practice, most spaces in analysis are T1, so "regular" usually implies the full T3 condition.

Regularity sits between T2 (Hausdorff) and **normality** (T4), where the axiom is upgraded to separate any two *disjoint closed sets* with disjoint open sets. The step from T2 to T3 already gives considerable power — it is part of the hypothesis for several metrization results — but T4 (normality) is what Urysohn's lemma requires, characterizing normal spaces as those where disjoint closed sets can be separated by a continuous real-valued function. Understanding T3 as an intermediate step shows what each additional separation axiom purchases and why metrization theorems require progressively stronger conditions.
