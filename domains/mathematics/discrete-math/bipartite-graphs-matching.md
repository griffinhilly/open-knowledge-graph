---
id: bipartite-graphs-matching
title: Bipartite Graphs and Matching Problems
domain: mathematics
course: discrete-math
prerequisites:
- id: bipartite-graphs
  type: hard
- id: graph-coloring-discrete
  type: soft
builds-toward:
- hamiltonian-cycles-discrete
tags:
- bipartite
- matching
- Hall's-theorem
- perfect-matching
stage: formal-systems
status: draft
---

# Bipartite Graphs and Matching Problems

## Core Idea
A bipartite graph has vertex partition into two sets with edges only between sets (not within). A matching is a set of disjoint edges. Hall's marriage theorem characterizes when a perfect matching (every vertex matched) exists in a bipartite graph.

## How It's Best Learned
Recognize bipartite graphs: they have no odd cycles. Use BFS/DFS to 2-color them. Apply Hall's theorem to prove existence of matchings. Model problems as bipartite matching: job assignments, system administrators, Latin rectangles.

## Common Misconceptions
A bipartite graph need not be complete bipartite. Hall's condition is necessary and sufficient: every subset S of one part must have at least |S| neighbors on the other side.

## Explainer

A bipartite graph divides its vertices into two distinct groups — call them "left" and "right" — where edges only connect a left vertex to a right vertex, never two vertices within the same group. From your prior work on bipartite graphs, you know this two-colorability is equivalent to having no odd cycles. The classic real-world picture: left vertices are job applicants, right vertices are open positions, and edges connect each applicant to the jobs they qualify for. The question "can we assign everyone to a job?" is exactly a **matching** problem.

A matching is a set of edges with no shared endpoints — each vertex appears in at most one matched pair. A **perfect matching** matches every vertex on one side (or both sides if they're equal in size). The central theorem is **Hall's Marriage Theorem**: a bipartite graph has a perfect matching from the left side if and only if for every subset S of left vertices, the set of their neighbors N(S) satisfies |N(S)| ≥ |S|. This is called **Hall's condition**. Intuitively, it says no subset of applicants is "too picky" — every group of k applicants must collectively be interested in at least k distinct jobs.

The necessity of Hall's condition is immediate: if some subset S of left vertices has fewer than |S| neighbors on the right, there simply aren't enough distinct right vertices to match all of S, so a perfect matching is impossible. The sufficiency — that Hall's condition guarantees a perfect matching exists — requires a proof, typically by induction on the size of the graph. You build a matching greedily where the condition is tight (|N(S)| = |S| for some S), then handle the slack cases where you have room to maneuver.

In practice, **augmenting path algorithms** find the actual maximum matching efficiently. An augmenting path is a path that starts and ends at unmatched vertices and alternates between unmatched and matched edges. Following this path toggles the matching status of each edge on the path, increasing the matching size by one. The algorithm terminates when no augmenting path exists — at that point, the matching is maximum. Hall's theorem converts an existential question ("does a perfect matching exist?") into a combinatorial condition you can verify, while augmenting paths give you the constructive algorithm to find it.
