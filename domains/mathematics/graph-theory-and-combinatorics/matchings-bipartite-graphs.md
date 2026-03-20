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
stage: formal-systems
status: draft
---

# Matchings in Bipartite Graphs

## Core Idea
A matching is a set of edges with no shared vertices; a maximum matching is one of largest cardinality. In bipartite graphs, matchings have rich structure and admit efficient algorithms. The problem of finding maximum matchings is equivalent to maximum flow, a cornerstone of combinatorial optimization.

## How It's Best Learned
Visualize small bipartite graphs and manually find maximum matchings using augmenting path intuition. Code a simple augmenting path algorithm to see how it progressively improves the matching.

## Common Misconceptions
- Confusing a matching with any subset of edges; the no-shared-vertices condition is essential.
- Thinking maximum matchings are always unique; many graphs have multiple maximum matchings with the same cardinality.

## Explainer

From the formal definitions of graph theory, you know that a graph consists of vertices and edges. A **matching** is a subset of edges such that no two edges share an endpoint — it is a selection of vertex-disjoint pairs. Think of it as a pairing: if vertices represent people and edges represent compatible pairs, a matching assigns each selected person exactly one partner, with no one double-booked. A **maximum matching** is simply a matching with as many edges as possible.

Bipartite graphs — graphs whose vertices split into two sets L and R with edges only between the two sides — are the natural setting for matching problems. Classic applications make this structure explicit: L is a set of workers, R is a set of jobs, and an edge means "this worker can do this job." Finding a maximum matching answers "what is the most work we can complete simultaneously?" The bipartite structure allows efficient algorithms that exploit the two-sided partition.

The key algorithmic idea is the **augmenting path**. Given a current matching M, an augmenting path is a path that alternates between unmatched and matched edges, starting and ending at unmatched vertices. If such a path exists, you can improve the matching by flipping the matched/unmatched status of every edge along the path — the matching grows by one edge. Berge's theorem guarantees the converse: a matching is maximum if and only if no augmenting path exists. This transforms the optimization problem into a search problem: repeatedly find and apply augmenting paths until none remain.

The equivalence to **maximum flow** connects matchings to a powerful general framework. Construct a flow network: add a source s with edges to every vertex in L, add a sink t with edges from every vertex in R, and direct each original edge from L to R. Every edge gets capacity 1. A maximum integer flow in this network corresponds exactly to a maximum matching. This connection means all of max-flow theory — including the max-flow min-cut theorem and efficient algorithms like Ford-Fulkerson — applies directly to bipartite matching. The two most important consequences are Hall's marriage theorem (a necessary and sufficient condition for a perfect matching to exist) and König's theorem (in bipartite graphs, the maximum matching size equals the minimum vertex cover size), which you will encounter as the natural successors to this topic.
