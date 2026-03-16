---
id: list-coloring
title: List Coloring and Choosability
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
tags:
- graph-theory
- coloring
stage: formal-systems
status: draft
---

# List Coloring and Choosability

## Core Idea
List coloring (choosability) is a generalization where each vertex has a list of available colors, and the goal is to color vertices from their lists with no adjacent vertices sharing a color. The list chromatic number is always at least chromatic number and often larger, revealing finer structural properties.

## How It's Best Learned
Construct list-assignments and try to find valid colorings; observe how the structure of lists and graph connectivity interact.

## Common Misconceptions
List chromatic number can be much larger than standard chromatic number; having more total colors available doesn't guarantee good list colorability.

## Explainer

Standard graph coloring asks: given k colors for the whole graph, can every vertex be assigned one of those k colors so no two adjacent vertices share a color? **List coloring** relaxes the uniformity: each vertex v gets its own private list L(v) of allowed colors, and you must color v from L(v) while still avoiding color conflicts with neighbors. The graph is **k-choosable** (or k-list-colorable) if it can be properly list-colored from *any* assignment of lists of size k — no matter what specific k colors each vertex gets on its list.

The **list chromatic number** χ_ℓ(G) is the smallest k for which G is k-choosable. Because the uniform case (all lists identical) is a special case of list coloring, we always have χ(G) ≤ χ_ℓ(G). But list chromatic number can be strictly larger — and sometimes dramatically so. The canonical example is the complete bipartite graph K_{n,n}: it has chromatic number 2 (it's bipartite, so 2-colorable), but its list chromatic number is Θ(log n). To see why, imagine a cleverly adversarial list assignment where the top and bottom vertices each get n different colors arranged to conflict pairwise — no consistent coloring survives.

The distinction matters because list coloring models scenarios where different vertices have incompatible constraints. In scheduling, employees might each be available only on certain days; the question is whether a valid schedule exists given those individual constraints, not whether a fixed set of days works universally. Brooks' Theorem gives χ(G) ≤ Δ for most graphs, but the analogous result for list coloring (the **Galvin-Vizing theorem** for bipartite graphs, the **Erdős–Rubin–Taylor theorem** generally) requires higher k. A bipartite graph is always Δ-edge-choosable (Galvin's theorem), which is a stronger statement than the equivalent for vertex coloring.

The deep subtlety is that the adversary choosing lists is working *against* you. Even if the total number of colors across all lists is vast, a carefully constructed list assignment can make coloring impossible at any smaller-than-χ_ℓ list size. This is why checking whether a graph is 2-choosable is already nontrivial — you must verify that no adversarial list assignment of size 2 defeats you. The **kernel method**, a key proof technique, converts list coloring problems into questions about orientations of the graph, connecting this topic to directed graph theory you've seen in your prerequisites on graph coloring.
