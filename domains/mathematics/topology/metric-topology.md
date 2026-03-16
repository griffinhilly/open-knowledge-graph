---
id: metric-topology
title: Metric Topology
domain: mathematics
course: topology
prerequisites:
- id: metric-spaces-definition-and-examples
  type: hard
- id: basis-for-a-topology
  type: soft
builds-toward:
- metrization-theorems
- completeness-metric-spaces
tags:
- metric-topology
- open-balls
- induced-topology
stage: advanced
status: draft
---

# Metric Topology

## Core Idea
Every metric induces a topology by taking open balls as a basis: open sets are unions of balls. This metric topology makes the distance function continuous and provides the most familiar examples of topological spaces. The metric topology is Hausdorff, first-countable, and forms the bridge between metric analysis and general topology.

## Explainer

From your study of metric spaces, you know that a metric d gives a precise notion of distance: d(x, y) measures how far apart x and y are. From your study of topological bases, you know that a topology can be built from a collection of "basic" open sets whose unions generate all open sets. Metric topology brings these ideas together: every metric space carries a natural topology, defined by declaring open balls to be the basic open sets.

The **open ball** of radius r centered at x is the set B(x, r) = {y ∈ X : d(x, y) < r} — all points strictly closer than r from x. The collection of all open balls forms a **basis** for the metric topology: an arbitrary set U is open if and only if for every x ∈ U, there is some r > 0 with B(x, r) ⊆ U. This recovers exactly the ε-δ definition of open sets from real analysis — a set is open if every point has "wiggle room." The topology defined this way is called the **metric topology** (or the topology induced by d), and continuity in this topology is exactly ε-δ continuity. So metric topology is not introducing new ideas but giving a precise categorical framework for what you already know from analysis.

The metric topology has particularly nice separation and countability properties. It is **Hausdorff** (any two distinct points can be enclosed in disjoint open balls), which means limits of sequences are unique and many familiar arguments carry through. It is **first-countable** (each point has a countable neighborhood base — namely, the balls of radius 1/n), which means sequences are sufficient to detect limits and closures; you don't need the more general notion of nets. This is why analysis can use sequences everywhere, while general topology sometimes requires nets or filters.

The crucial conceptual move in metric topology is realizing that two different metrics can induce the same topology — they are then called **equivalent metrics**, or **topologically equivalent**. The Euclidean metric and the taxicab metric on ℝⁿ are different functions, but they generate the same open sets, so every continuous map in one sense is continuous in the other. This is why topology cares about open sets rather than distances: the topology captures which properties are preserved by continuous maps, while the specific metric values are extra structure that may or may not be preserved. Metric topology is thus the gateway from analysis, which works with specific distances, to general topology, which works with open set structure alone.
