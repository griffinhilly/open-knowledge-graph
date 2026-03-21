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

## Questions

```yaml
- question: "A graph has three vertices forming a triangle (K₃). A student claims: 'The maximum matching has size 1. By König's theorem, the minimum vertex cover should also have size 1.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The maximum matching of K₃ is actually size 2, not size 1"
    - "König's theorem only applies to bipartite graphs; K₃ is an odd cycle and is not bipartite, so the theorem does not apply"
    - "The minimum vertex cover of K₃ is size 1, confirming the student's claim"
    - "König's theorem requires that the graph have a perfect matching"
  answer: 1
  explanation: "König's theorem is specific to bipartite graphs. In K₃, the maximum matching has size 1 (only one edge can be selected without sharing a vertex), but the minimum vertex cover has size 2 (any single vertex leaves one edge uncovered). The theorem fails here precisely because K₃ is an odd cycle, which cannot be bipartite. The bipartite structure is essential to the result."

- question: "In a bipartite graph, why does maximum matching ≤ minimum vertex cover follow immediately from the definitions?"
  type: multiple-choice
  options:
    - "Bipartite graphs always have more vertices than edges, guaranteeing the inequality"
    - "Each edge in the matching is vertex-disjoint from every other matching edge, so each matching edge requires its own dedicated covering vertex"
    - "The matching algorithm terminates before the vertex cover is fully constructed"
    - "Vertex covers in bipartite graphs must include one entire partition"
  answer: 1
  explanation: "Matching edges are vertex-disjoint by definition — no two selected edges share an endpoint. This means a single vertex cannot cover two different matching edges. Therefore, to cover all k matching edges, the vertex cover needs at least k vertices. This gives the easy direction: maximum matching ≤ minimum vertex cover. The hard direction — that equality is always achievable in bipartite graphs — requires the constructive proof using augmenting paths."

- question: "König's theorem states that in any graph, the size of a maximum matching equals the size of a minimum vertex cover."
  type: true-false
  answer: false
  explanation: "König's theorem holds only for bipartite graphs. In non-bipartite graphs, the maximum matching can be strictly smaller than the minimum vertex cover. The triangle K₃ is the canonical counterexample: maximum matching = 1, minimum vertex cover = 2. The bipartite condition is not a technicality — it is the exact structural property that prevents odd cycles from breaking the min-max equality."

- question: "In a bipartite graph, no single vertex can cover two edges from a maximum matching simultaneously, because matching edges share no endpoints by definition."
  type: true-false
  answer: true
  explanation: "This is the key geometric fact behind the inequality max matching ≤ min vertex cover. Matching edges share no endpoints by the definition of a matching. Therefore each matching edge must be covered by a distinct vertex, and no vertex in the cover does double duty across two matching edges. This forces the cover to be at least as large as the matching."

- question: "Explain why König's theorem fails on odd cycles like K₃ but holds for bipartite graphs. What property of bipartite graphs is essential?"
  type: short-answer
  answer: "Bipartite graphs have no odd cycles — every cycle has even length. This two-colorability is what allows matchings and vertex covers to achieve equality in size. In an odd cycle like K₃, the three edges form a cycle that cannot be split into two independent sets with all edges crossing between them; this asymmetry means you need more vertices to cover all edges than you have edges in a maximum matching. Bipartite graphs avoid this: their LP relaxation is always integral (by total unimodularity), meaning the duality gap between the matching and cover problems is zero."
  explanation: "The connection to LP duality is the deeper explanation: matching and vertex cover are dual linear programs, and integrality of the LP solution is guaranteed for bipartite graphs but not for general graphs. For non-bipartite graphs, the LP optimal can be fractional, and the integer solutions diverge. Bipartiteness is not a convenience restriction — it is the exact condition under which combinatorial duality is tight."
```

## Explainer

From Hall's theorem, you know when a perfect matching exists in a bipartite graph. König's theorem goes further: it pins down the *size* of the largest matching by connecting it to an entirely different concept — the **vertex cover**. A vertex cover is a set of vertices such that every edge in the graph has at least one endpoint in the set. To "cover" all edges, you need to station a guard at enough vertices that no edge goes unwatched. The minimum vertex cover is the smallest such set. König's theorem says: in any bipartite graph, the size of a maximum matching equals the size of a minimum vertex cover.

This equality is not obvious. It is a minimax result — the maximum of one quantity equals the minimum of another — which is a powerful pattern in combinatorial optimization. One direction is easy: any vertex cover must have at least as many vertices as a maximum matching has edges, because each edge in the matching needs its own vertex to cover it (the edges are disjoint, so no single vertex can cover two of them). This gives maximum matching ≤ minimum vertex cover. The hard direction — that a matching and a cover of the same size always exist — requires construction, and the proof uses augmenting paths, a technique from the study of matchings you have seen before.

A concrete example clarifies both sides. Consider a bipartite graph with Left vertices {1, 2, 3} and Right vertices {a, b, c} with edges 1-a, 1-b, 2-b, 3-c. A maximum matching might be {1-a, 2-b, 3-c}, size 3. A minimum vertex cover is {1, 2, 3} (or equivalently {a, b, c}, but also check {1, b, 3} — does it cover all edges? 1-a ✓, 1-b ✓, 2-b ✓, 3-c ✓ — yes, size 3). So maximum matching = minimum vertex cover = 3, confirming König.

The theorem fails for non-bipartite graphs: in a triangle K₃, the maximum matching has size 1 (only one disjoint edge fits), but the minimum vertex cover has size 2 (you need two vertices to cover all three edges). The odd cycle creates an asymmetry that bipartite structure prevents. König's theorem is a special case of the broader **LP duality** in linear programming: matching and vertex cover are dual optimization problems, and integrality of bipartite graphs guarantees the duality gap is zero. This connection foreshadows the max-flow min-cut theorem you will encounter next, which generalizes the same min-max principle to network flows.
