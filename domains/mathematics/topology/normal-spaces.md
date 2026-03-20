---
id: normal-spaces
title: Normal Spaces (T4 Spaces)
domain: mathematics
course: topology
prerequisites:
- id: separation-axioms
  type: hard
builds-toward:
- urysohns-lemma
- tietze-extension-theorem
tags:
- normal
- t4
stage: formal-systems
status: draft
---

# Normal Spaces (T4 Spaces)

## Core Idea
A space is normal if disjoint closed sets F, G have disjoint open neighborhoods. Every compact Hausdorff space and every metric space is normal.

## Explainer

You've studied the **separation axioms** — a hierarchy of conditions that capture how well a topological space can separate points and sets using open sets. Recall the key levels: T₁ (points are closed), T₂ or Hausdorff (disjoint points have disjoint open neighborhoods), and T₃ or regular (a point and a disjoint closed set have disjoint open neighborhoods). **Normal spaces** (T₄) push this one step further: *two disjoint closed sets* can always be separated by disjoint open neighborhoods.

To feel why this is a meaningful strengthening, compare T₃ and T₄. In a regular space, you can separate a *point* from a closed set it doesn't belong to. But a single point is a very special kind of closed set. Normality demands the same separation for *arbitrary* disjoint closed sets — even large, complicated ones. In some pathological spaces (certain infinite products, the long line), disjoint closed sets cannot always be separated this way, showing that normality is a genuine restriction.

The two major classes of normal spaces are metric spaces and compact Hausdorff spaces. For metric spaces, the proof is constructive: given disjoint closed sets F and G in a metric space, let U = {x : d(x,F) < d(x,G)} and V = {x : d(x,G) < d(x,F)}. These are open (they're defined by strict inequalities of continuous functions), disjoint, and contain F and G respectively. The metric provides enough structure to build the separating neighborhoods explicitly. For compact Hausdorff spaces, the argument is topological: compactness lets you build finite open covers, and Hausdorff-ness provides local separability that can be pieced together globally.

Why does normality matter? It is the exact condition needed for **Urysohn's Lemma**, which you'll study next: in a normal space, any two disjoint closed sets can be separated not just by open sets, but by a *continuous real-valued function* — one that equals 0 on one closed set and 1 on the other. This is a striking upgrade from separation by open sets alone, and it's the key to constructing continuous functions in topology. Urysohn's Lemma is then the engine behind the **Tietze Extension Theorem**, which says that every continuous real-valued function defined on a closed subset of a normal space extends to the whole space. Together, these results make normality the foundation of the theory of continuous functions on topological spaces.
