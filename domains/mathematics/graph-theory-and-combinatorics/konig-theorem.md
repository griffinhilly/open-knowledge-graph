---
id: konig-theorem
title: König's Theorem and Min-Max Relations
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: halls-marriage-theorem
  type: hard
builds-toward:
- network-flows-max-flow-min-cut
tags:
- konig-theorem
- min-max
- vertex-cover
stage: formal-systems
status: draft
---

# König's Theorem and Min-Max Relations

## Core Idea
König's theorem states that in a bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover. This min-max equality is a central result in combinatorial optimization and does not hold for general graphs.

## How It's Best Learned
Compute both the maximum matching and minimum vertex cover for several small bipartite graphs to verify equality. Use the duality to understand why König's theorem fails on odd cycles.

## Common Misconceptions
- Thinking the matching-vertex-cover duality holds for all graphs (it fails on non-bipartite graphs like K₃).
- Confusing minimum vertex cover with minimum edge cover; these are different problems.

## Explainer

From Hall's theorem, you know when a perfect matching exists in a bipartite graph. König's theorem goes further: it pins down the *size* of the largest matching by connecting it to an entirely different concept — the **vertex cover**. A vertex cover is a set of vertices such that every edge in the graph has at least one endpoint in the set. To "cover" all edges, you need to station a guard at enough vertices that no edge goes unwatched. The minimum vertex cover is the smallest such set. König's theorem says: in any bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover.

This equality is not obvious. It is a minimax result — the maximum of one quantity equals the minimum of another — which is a powerful pattern in combinatorial optimization. One direction is easy: any vertex cover must have at least as many vertices as a maximum matching has edges, because each edge in the matching needs its own vertex to cover it (the edges are disjoint, so no single vertex can cover two of them). This gives maximum matching ≤ minimum vertex cover. The hard direction — that a matching and a cover of the same size always exist — requires construction, and the proof uses augmenting paths, a technique from the study of matchings you have seen before.

A concrete example clarifies both sides. Consider a bipartite graph with Left vertices {1, 2, 3} and Right vertices {a, b, c} with edges 1-a, 1-b, 2-b, 3-c. A maximum matching might be {1-a, 2-b, 3-c}, size 3. A minimum vertex cover is {1, 2, 3} (or equivalently {a, b, c}, but also check {1, b, 3} — does it cover all edges? 1-a ✓, 1-b ✓, 2-b ✓, 3-c ✓ — yes, size 3). So maximum matching = minimum vertex cover = 3, confirming König.

The theorem fails for non-bipartite graphs: in a triangle K₃, the maximum matching has size 1 (only one disjoint edge fits), but the minimum vertex cover has size 2 (you need two vertices to cover all three edges). The odd cycle creates an asymmetry that bipartite structure prevents. König's theorem is a special case of the broader **LP duality** in linear programming: matching and vertex cover are dual optimization problems, and integrality of bipartite graphs guarantees the duality gap is zero. This connection foreshadows the max-flow min-cut theorem you will encounter next, which generalizes the same min-max principle to network flows.
