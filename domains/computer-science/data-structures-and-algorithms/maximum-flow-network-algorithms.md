---
id: maximum-flow-network-algorithms
title: 'Maximum Flow: Network Flow Problems and Algorithms'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-adjacency-representation-analysis
  type: hard
tags:
- graphs
- flow
- algorithms
stage: formal-systems
status: draft
---

# Maximum Flow: Network Flow Problems and Algorithms

## Core Idea
The maximum flow problem finds the maximum amount of flow from a source to a sink along weighted edges with capacity constraints. Algorithms like Ford-Fulkerson use augmenting paths in O(E·max_flow) time; Edmonds-Karp uses BFS for O(VE²) worst-case time. Applications include bipartite matching, airline scheduling, and network design.

## How It's Best Learned
Implement Ford-Fulkerson with DFS, then Edmonds-Karp with BFS. Trace augmenting paths and residual graph updates. Apply to bipartite matching by constructing a flow network.

## Common Misconceptions
- Thinking maximum flow is a niche problem; many problems reduce to it (matching, path packing, circulation).
- Not understanding augmenting paths; they're the key insight enabling efficient algorithms.
- Assuming integer flows always exist; with irrational capacities, exact solutions may not exist.

## Explainer

A **flow network** is a directed graph where each edge has a capacity — a maximum amount of "stuff" that can pass through it per unit time. There is a designated **source** node (where flow originates) and a **sink** node (where flow is consumed). Think of it as a system of pipes: each pipe has a maximum throughput, and you want to push as much water as possible from a pump (source) to a reservoir (sink). The **maximum flow problem** asks: what is the greatest total flow you can route from source to sink without exceeding any edge's capacity?

The foundational insight is the **Ford-Fulkerson method**, which works by repeatedly finding **augmenting paths** — routes from source to sink along which additional flow can be pushed. You start with zero flow everywhere, find a path with available capacity, and push as much flow as possible along it. The trick is the **residual graph**: after pushing flow along an edge, you create a "reverse edge" that allows you to undo that decision later. This reverse edge is essential because greedy path choices can lead to suboptimal solutions. The residual graph lets the algorithm effectively reroute flow, correcting earlier mistakes without backtracking explicitly. When no more augmenting paths exist in the residual graph, you have found the maximum flow.

The basic Ford-Fulkerson approach using DFS to find augmenting paths runs in O(E × max_flow) time, which can be slow if the maximum flow value is large. The **Edmonds-Karp algorithm** improves this by always choosing the shortest augmenting path (using BFS), which guarantees termination in O(V × E²) time regardless of capacity values. More advanced algorithms like Dinic's achieve O(V² × E) by exploiting the layered structure of the residual graph more aggressively.

The **max-flow min-cut theorem** ties everything together: the maximum flow from source to sink equals the minimum capacity of any cut separating source from sink. A **cut** is a partition of vertices into two sets (one containing the source, the other containing the sink), and its capacity is the sum of capacities of edges crossing from the source side to the sink side. This duality is not just theoretically elegant — it means that solving max-flow automatically solves min-cut, which has its own applications in network reliability, image segmentation, and resource allocation.

What makes maximum flow especially powerful is its versatility as a modeling tool. **Bipartite matching** — assigning workers to jobs, students to projects, or applicants to positions — reduces directly to max-flow by connecting a super-source to one side, a super-sink to the other, and giving every edge capacity one. If the maximum flow equals k, you can match k pairs. Problems in scheduling, circulation, edge-disjoint paths, and even baseball elimination can all be encoded as flow networks. Recognizing when a problem is secretly a max-flow problem is one of the most valuable pattern-matching skills in algorithm design.
