---
id: matchings-bipartite-graphs
title: Matchings in Bipartite Graphs
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
builds-toward:
- halls-marriage-theorem
- konig-theorem
tags:
- matchings
- bipartite-graphs
- optimization
stage: advanced
status: validated
---

# Matchings in Bipartite Graphs

## Core Idea
A matching is a set of edges with no shared vertices; a maximum matching is one of largest cardinality. In bipartite graphs, matchings have rich structure and admit efficient algorithms. The problem of finding maximum matchings is equivalent to maximum flow, a cornerstone of combinatorial optimization.

## How It's Best Learned
Visualize small bipartite graphs and manually find maximum matchings using augmenting path intuition. Code a simple augmenting path algorithm to see how it progressively improves the matching.

## Common Misconceptions
- Confusing a matching with any subset of edges; the no-shared-vertices condition is essential.
- Thinking maximum matchings are always unique; many graphs have multiple maximum matchings with the same cardinality.

## Questions

```yaml
- question: "In a graph with edges {(A,1), (A,2), (B,2), (C,3)}, a student claims {(A,1), (A,2)} is a valid matching because both edges exist in the graph. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — any subset of edges in a graph forms a valid matching"
    - "No — edges (A,1) and (A,2) share vertex A, violating the no-shared-endpoint condition"
    - "No — a matching must include at least half the edges in the graph"
    - "Yes — both edges connect to different right-side vertices (1 and 2), so they are compatible"
  answer: 1
  explanation: "A matching requires that no two edges share an endpoint — the edges must be vertex-disjoint. Edges (A,1) and (A,2) both involve vertex A, so A would be 'double-booked,' violating the definition. The student's mistake is the most common one: confusing a matching with any subset of edges. Option D describes why the right-side vertices are fine, but the problem is on the left side — vertex A is shared."

- question: "An algorithm has found a matching of size 5 in a bipartite graph, and an exhaustive search confirms that no augmenting path exists. What can you conclude?"
  type: multiple-choice
  options:
    - "The matching is maximum — by Berge's theorem, no augmenting path means no improvement is possible"
    - "The matching may not be maximum; Berge's theorem only applies to perfect matchings"
    - "The graph must have at least 10 vertices, one for each matched endpoint"
    - "The matching is maximum only if the graph is connected"
  answer: 0
  explanation: "Berge's theorem states: a matching M is maximum if and only if there is no augmenting path with respect to M. An augmenting path is a path alternating between unmatched and matched edges, starting and ending at unmatched vertices. If no such path exists, the matching cannot be improved by any strategy — it is definitively maximum. Berge's theorem applies to all matchings, not just perfect ones. Connectivity of the graph is irrelevant."

- question: "In a bipartite graph, the maximum matching problem can be solved exactly by formulating it as a maximum flow problem on a network with unit edge capacities."
  type: true-false
  answer: true
  explanation: "This equivalence is a cornerstone result. Construct a flow network: add a source s with unit-capacity edges to every left vertex, direct the bipartite edges from left to right with unit capacity, and add unit-capacity edges from every right vertex to a sink t. A maximum integer flow in this network corresponds exactly to a maximum matching — each unit of flow through the network corresponds to one matched edge. This connection means all max-flow algorithms and the max-flow min-cut theorem apply directly to bipartite matching."

- question: "If two matchings in a graph have the same cardinality, then both is expected to be maximum matchings."
  type: true-false
  answer: false
  explanation: "Two matchings can share the same size without either being maximum. For example, in a path graph A–1–B–2–C–3, the matching {(A,1), (C,3)} and the matching {(1,B)} both have different sizes, but consider a graph with multiple components: each component might support non-maximum matchings of equal size without either reaching the global maximum. Matching cardinality equality says nothing about optimality — you must verify the absence of augmenting paths to confirm maximality."

- question: "What is an augmenting path in the context of bipartite matching, and why does finding one always allow you to increase the size of the current matching?"
  type: short-answer
  answer: "An augmenting path is a path in the graph that alternates between edges not in the current matching and edges in the current matching, starting and ending at vertices that are currently unmatched. Because it starts and ends at unmatched vertices and alternates, the path has one more unmatched edge than matched edges. By flipping the matched/unmatched status of every edge along the path — taking in the unmatched edges and removing the matched ones — the matching gains exactly one edge. Berge's theorem guarantees the converse: if no augmenting path exists, the matching is already maximum."
  explanation: "The alternating structure is the key. An augmenting path of length 2k+1 contains k+1 unmatched edges and k matched edges. Flipping produces a new matching of size (original size) + 1. This transforms the combinatorial optimization problem (find the largest matching) into a search problem (find an augmenting path), which is solvable efficiently. Repeated augmentation terminates when no augmenting path remains, guaranteeing maximality by Berge's theorem."
```

## Explainer

From the formal definitions of graph theory, you know that a graph consists of vertices and edges. A **matching** is a subset of edges such that no two edges share an endpoint — it is a selection of vertex-disjoint pairs. Think of it as a pairing: if vertices represent people and edges represent compatible pairs, a matching assigns each selected person exactly one partner, with no one double-booked. A **maximum matching** is simply a matching with as many edges as possible.

Bipartite graphs — graphs whose vertices split into two sets L and R with edges only between the two sides — are the natural setting for matching problems. Classic applications make this structure explicit: L is a set of workers, R is a set of jobs, and an edge means "this worker can do this job." Finding a maximum matching answers "what is the most work we can complete simultaneously?" The bipartite structure allows efficient algorithms that exploit the two-sided partition.

The key algorithmic idea is the **augmenting path**. Given a current matching M, an augmenting path is a path that alternates between unmatched and matched edges, starting and ending at unmatched vertices. If such a path exists, you can improve the matching by flipping the matched/unmatched status of every edge along the path — the matching grows by one edge. Berge's theorem guarantees the converse: a matching is maximum if and only if no augmenting path exists. This transforms the optimization problem into a search problem: repeatedly find and apply augmenting paths until none remain.

The equivalence to **maximum flow** connects matchings to a powerful general framework. Construct a flow network: add a source s with edges to every vertex in L, add a sink t with edges from every vertex in R, and direct each original edge from L to R. Every edge gets capacity 1. A maximum integer flow in this network corresponds exactly to a maximum matching. This connection means all of max-flow theory — including the max-flow min-cut theorem and efficient algorithms like Ford-Fulkerson — applies directly to bipartite matching. The two most important consequences are Hall's marriage theorem (a necessary and sufficient condition for a perfect matching to exist) and König's theorem (in bipartite graphs, the maximum matching size equals the minimum vertex cover size), which you will encounter as the natural successors to this topic.
