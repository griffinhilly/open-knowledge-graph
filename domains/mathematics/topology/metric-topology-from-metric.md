---
id: metric-topology-from-metric
title: The Topology Induced by a Metric
domain: mathematics
course: topology
prerequisites:
- id: metric-spaces-definition-examples
  type: hard
- id: open-sets-definition-examples
  type: soft
builds-toward:
- compact-metric-spaces
- completeness-metric-spaces-definition
tags:
- metric-topology
- induced-topology
stage: formal-systems
status: draft
---

# The Topology Induced by a Metric

## Core Idea
Given a metric d on X, the metric topology consists of all unions of open balls B(x,ε) = {y : d(x,y) < ε}. Open balls form a basis for this topology. Not every topology comes from a metric (metrization theorems characterize which do). Metrics provide explicit, computable topologies on ℝⁿ and function spaces.

## Explainer

A **metric** gives you a way to measure distance: d(x, y) satisfies non-negativity, symmetry, and the triangle inequality. From your prerequisites you know what a metric space is and what open sets look like. The goal here is to see precisely how a metric *generates* a topology — how the distance function produces a family of open sets that satisfies all the topological axioms.

The construction begins with **open balls**: B(x, ε) = {y ∈ X : d(x, y) < ε}. Think of this as all points strictly within distance ε of x — the interior of a ball of radius ε centered at x. On the real line, B(x, ε) = (x−ε, x+ε), an open interval. In ℝ², it is an open disk. In a discrete metric space (where d(x,y) = 1 for all x ≠ y), B(x, 1/2) = {x}, a single point. The **metric topology** is then defined as the collection of all sets that can be written as unions of open balls. A set U is open in the metric topology if for every point x ∈ U, some open ball B(x, ε) is contained in U — equivalently, every point of U has a little breathing room inside U. Verifying that this collection satisfies the topological axioms (closed under arbitrary unions, finite intersections, contains ∅ and X) is a standard exercise using the triangle inequality.

The open balls form a **basis** for this topology, meaning every open set is a union of open balls — but the open balls themselves need not form a topology, because finite intersections of open balls are not generally open balls. The concept of a basis is important: you rarely specify a topology by listing all open sets (there can be uncountably many). Instead, you specify a basis and declare a set open if it's a union of basis elements. The metric provides such a basis for free.

A central point is that **different metrics can generate the same topology**. On ℝⁿ, the Euclidean metric, the taxicab metric (sum of coordinate differences), and the maximum metric all generate the same topology — the standard one — even though the shapes of their open "balls" differ. Two metrics that generate the same topology are called **topologically equivalent**. This shows that topology abstracts away the specific geometry (exact distances) and retains only the qualitative structure (which sets are open). The converse question — which topologies arise from some metric — is answered by **metrization theorems**: not every topology is metrizable, and conditions like second-countability and regularity characterize which ones are. The metric topology sits at a middle level of generality: richer than abstract topology (because you have explicit distances), but not as rigid as Euclidean geometry (because distances can be exotic). Most spaces you encounter in analysis — function spaces like C([0,1]) with the sup-norm, sequence spaces like ℓ², manifolds — are metric spaces, making this the dominant setting for applied topology.
