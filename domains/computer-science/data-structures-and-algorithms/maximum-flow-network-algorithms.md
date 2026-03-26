---
id: maximum-flow-network-algorithms
title: 'Maximum Flow: Network Flow Problems and Algorithms'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-adjacency-list-matrix-representations
  type: hard
- id: selection-algorithm-quickselect
  type: soft
- id: articulation-points-cut-vertices
  type: soft
- id: bipartite-graph-detection-coloring
  type: soft
- id: boyer-moore-algorithm-details
  type: soft
- id: cycle-detection-directed-undirected
  type: soft
tags:
- graphs
- flow
- algorithms
stage: advanced
status: validated
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

## Questions

```yaml
- question: "In the Ford-Fulkerson method, why is the residual graph's reverse edge essential?"
  type: multiple-choice
  options:
    - "It prevents the algorithm from visiting the same node twice"
    - "It allows the algorithm to undo a previous flow decision and reroute flow more efficiently"
    - "It records edges that have been fully saturated so they are skipped"
    - "It doubles the capacity of each edge to handle bidirectional traffic"
  answer: 1
  explanation: "The residual graph's reverse edge is the key mechanism that makes Ford-Fulkerson correct. A greedy augmenting path choice might push flow along a suboptimal route. The reverse edge — with capacity equal to the current flow on that edge — lets a later augmenting path effectively 'cancel' earlier flow by routing through the reverse edge, redirecting that flow elsewhere. Without reverse edges, the algorithm could get permanently stuck at a suboptimal solution."

- question: "After running Ford-Fulkerson to completion, which of the following is guaranteed to be true?"
  type: multiple-choice
  options:
    - "The maximum flow equals the total capacity of all edges leaving the source"
    - "The maximum flow equals the minimum capacity cut separating source from sink"
    - "Every edge in the network carries flow equal to its capacity"
    - "The number of augmenting paths found equals the maximum flow value"
  answer: 1
  explanation: "The max-flow min-cut theorem states that the maximum flow from source to sink equals the minimum capacity of any cut that separates source from sink. This is not just a convenient fact — it means solving max-flow simultaneously solves min-cut. Option A is wrong because not all source edges need to be fully used; option C is wrong because many edges may carry less than capacity; option D conflates the count of paths with the flow value."

- question: "Edmonds-Karp guarantees polynomial time termination even when Ford-Fulkerson with DFS might not terminate."
  type: true-false
  answer: true
  explanation: "Edmonds-Karp uses BFS to always choose the shortest augmenting path (fewest edges), which guarantees at most O(VE) augmentations and O(VE²) total time — regardless of capacity values. Basic Ford-Fulkerson with DFS can fail to terminate when edge capacities are irrational numbers, because augmenting paths can approach the maximum flow asymptotically without ever reaching it."

- question: "Many combinatorial problems like bipartite matching require their own specialized algorithms and can seldom be reduced to max-flow."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Bipartite matching, edge-disjoint paths, circulation with lower bounds, and many scheduling problems all reduce to max-flow. For bipartite matching, you add a super-source connected to one partition and a super-sink connected to the other, set all capacities to 1, and run max-flow. The maximum flow value gives the maximum matching size. Recognizing problems as disguised max-flow instances is one of the most valuable skills in algorithm design."

- question: "Why is the residual graph the central data structure in maximum flow algorithms, and what role do its reverse edges play?"
  type: short-answer
  answer: "The residual graph tracks how much additional flow can be pushed along each edge. For a forward edge with capacity c carrying flow f, the residual capacity is c−f (remaining room). The reverse edge carries capacity f, representing the ability to 'undo' up to f units of flow. This is essential because greedy path choices may be locally good but globally suboptimal. By routing flow through a reverse edge, a later augmenting path effectively cancels and reroutes earlier flow, correcting those mistakes without explicit backtracking."
  explanation: "Without the residual graph and its reverse edges, the algorithm would be a simple greedy path-packer with no correction mechanism. The reverse edge is what transforms Ford-Fulkerson from a heuristic into an exact algorithm. Every correct max-flow algorithm implicitly or explicitly maintains this structure."
```

## Explainer

A **flow network** is a directed graph where each edge has a capacity — a maximum amount of "stuff" that can pass through it per unit time. There is a designated **source** node (where flow originates) and a **sink** node (where flow is consumed). Think of it as a system of pipes: each pipe has a maximum throughput, and you want to push as much water as possible from a pump (source) to a reservoir (sink). The **maximum flow problem** asks: what is the greatest total flow you can route from source to sink without exceeding any edge's capacity?

The foundational insight is the **Ford-Fulkerson method**, which works by repeatedly finding **augmenting paths** — routes from source to sink along which additional flow can be pushed. You start with zero flow everywhere, find a path with available capacity, and push as much flow as possible along it. The trick is the **residual graph**: after pushing flow along an edge, you create a "reverse edge" that allows you to undo that decision later. This reverse edge is essential because greedy path choices can lead to suboptimal solutions. The residual graph lets the algorithm effectively reroute flow, correcting earlier mistakes without backtracking explicitly. When no more augmenting paths exist in the residual graph, you have found the maximum flow.

The basic Ford-Fulkerson approach using DFS to find augmenting paths runs in O(E × max_flow) time, which can be slow if the maximum flow value is large. The **Edmonds-Karp algorithm** improves this by always choosing the shortest augmenting path (using BFS), which guarantees termination in O(V × E²) time regardless of capacity values. More advanced algorithms like Dinic's achieve O(V² × E) by exploiting the layered structure of the residual graph more aggressively.

The **max-flow min-cut theorem** ties everything together: the maximum flow from source to sink equals the minimum capacity of any cut separating source from sink. A **cut** is a partition of vertices into two sets (one containing the source, the other containing the sink), and its capacity is the sum of capacities of edges crossing from the source side to the sink side. This duality is not just theoretically elegant — it means that solving max-flow automatically solves min-cut, which has its own applications in network reliability, image segmentation, and resource allocation.

What makes maximum flow especially powerful is its versatility as a modeling tool. **Bipartite matching** — assigning workers to jobs, students to projects, or applicants to positions — reduces directly to max-flow by connecting a super-source to one side, a super-sink to the other, and giving every edge capacity one. If the maximum flow equals k, you can match k pairs. Problems in scheduling, circulation, edge-disjoint paths, and even baseball elimination can all be encoded as flow networks. Recognizing when a problem is secretly a max-flow problem is one of the most valuable pattern-matching skills in algorithm design.
