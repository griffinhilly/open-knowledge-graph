---
id: graph-traversal-algorithms
title: 'Graph Traversal: Depth-First and Breadth-First Search'
domain: mathematics
course: discrete-math
prerequisites:
- id: depth-first-search-graphs
  type: hard
- id: breadth-first-search-graphs
  type: hard
builds-toward:
- graph-coloring-discrete
tags:
- DFS
- BFS
- traversal
- tree-edges
- back-edges
stage: formal-systems
status: validated
---

# Graph Traversal: Depth-First and Breadth-First Search

## Core Idea
Depth-first search (DFS) explores as far as possible along each branch (recursively), while breadth-first search (BFS) explores level-by-level using a queue. Both visit all reachable vertices, producing a spanning tree. DFS finds back-edges (identifying cycles); BFS finds shortest paths in unweighted graphs.

## How It's Best Learned
Trace DFS and BFS by hand on small graphs, noting discovery and finish times for DFS. Implement both iteratively. Recognize DFS orderings and topological sorting applications.

## Common Misconceptions
DFS can visit vertices in many different orders depending on starting vertex and edge order; BFS finds the shortest path in unweighted graphs, not weighted ones.

## Questions

```yaml
- question: "You need to find whether a directed graph contains a cycle. Which traversal algorithm is most naturally suited, and what does it detect?"
  type: multiple-choice
  options:
    - "BFS, because it explores level by level and can detect cross-edges that indicate cycles"
    - "DFS, because it detects back-edges — edges pointing to a vertex still on the current recursion stack"
    - "Either algorithm works equally well, since both visit all vertices"
    - "BFS, because its queue ensures vertices are visited in the order they were discovered, revealing repetitions"
  answer: 1
  explanation: "DFS is the natural choice for cycle detection. When DFS encounters a vertex already on the current recursion stack (marked 'in progress'), it has found a back-edge — a backward link that closes a loop. BFS can detect cross-edges to already-visited vertices, but this does not as cleanly expose cycle structure. The back-edge criterion from DFS is the basis for topological sort and DAG detection."

- question: "In an unweighted graph, you want the shortest path from vertex S to every other reachable vertex. Which algorithm gives correct results, and why does the other one fail?"
  type: multiple-choice
  options:
    - "DFS gives correct results; BFS may miss some vertices by terminating early"
    - "BFS gives correct results; DFS may find a path but not the shortest one"
    - "Both give correct shortest paths because both visit all reachable vertices"
    - "DFS gives correct results because its stack structure naturally prioritizes direct paths"
  answer: 1
  explanation: "BFS discovers each vertex for the first time via the shortest path from the source, because it explores all vertices at distance k before any at distance k+1. DFS follows chains as deep as possible before backtracking, so it may reach a vertex via a long path when a shorter one exists. BFS's queue is the mechanism that enforces level-by-level exploration and thus shortest-path correctness — but only in unweighted graphs. In weighted graphs, Dijkstra's algorithm is required."

- question: "In an unweighted graph, BFS guarantees that each vertex is first discovered via the shortest path (fewest edges) from the source."
  type: true-false
  answer: true
  explanation: "This is BFS's defining property. Because BFS uses a queue and processes vertices in FIFO order, it finishes all vertices at distance d before reaching any at distance d+1. The first time a vertex is discovered, it is reached via the shortest possible route. DFS makes no such guarantee — it may find a vertex after following a long chain when a two-hop path existed."

- question: "DFS is faster than BFS in the worst case because it finds the target vertex sooner without exploring all levels."
  type: true-false
  answer: false
  explanation: "Both DFS and BFS run in O(V + E) time — they visit every vertex and edge exactly once. DFS may happen to find a target quickly in a specific case, but in the worst case (e.g., the target is at the opposite end of the graph), it explores just as much as BFS. The difference between the algorithms is not efficiency but the *structure* they expose: DFS reveals back-edges and cycle structure; BFS reveals shortest paths."

- question: "Why does using a queue (rather than a stack) cause BFS to find shortest paths in unweighted graphs?"
  type: short-answer
  answer: "A queue is FIFO: vertices discovered first are explored first. This means BFS processes all vertices at distance 1 before any at distance 2, all at distance 2 before any at distance 3, and so on. The first time a vertex is dequeued and explored, it was reached via the smallest number of hops possible. A stack (used by DFS) is LIFO, which causes deep-first exploration and gives no such level-ordering guarantee."
  explanation: "The data structure is the entire explanation. Queue → FIFO → level-by-level → shortest paths. Stack → LIFO → depth-first → no shortest-path guarantee. Understanding this makes both algorithms' properties follow directly from one underlying principle rather than two separate rules to memorize."
```

## Explainer

You already know the mechanics of **depth-first search** and **breadth-first search** individually. This topic is about understanding them together — their structural differences, what each one reveals about a graph, and when to reach for one versus the other.

The key distinction is the data structure each algorithm uses to decide which vertex to explore next. DFS uses a stack (or the call stack via recursion): push neighbors, pop the most recent, explore it, repeat. This sends the search diving deep before it backtracks. BFS uses a queue: push neighbors, dequeue the oldest, explore it, repeat. This sends the search spreading outward one layer at a time, like ripples from a stone dropped in water. The same logic, two different data structures, two completely different exploration patterns.

Both algorithms produce a **spanning tree** of the reachable portion of the graph. But the shape of that tree differs. A DFS spanning tree tends to be tall and thin — the algorithm follows long chains before backtracking. A BFS spanning tree tends to be short and wide — all vertices at distance 1 are found before any at distance 2. This is why BFS gives you **shortest paths** in unweighted graphs: every vertex is first discovered via the shortest possible route from the source. DFS makes no such guarantee.

DFS reveals something BFS cannot: **back-edges**. When DFS revisits a vertex that is still on the current recursion stack (marked "in progress"), it has found a back-edge — an edge that points backward in the DFS tree, closing a loop. Back-edges are exactly how you detect cycles in a graph using DFS. BFS, exploring layer by layer, can detect cross-edges between already-visited vertices, but it does not naturally expose cycle structure the same way. This connects directly to topological sorting and DAG detection: run DFS, check for back-edges. If none exist, the graph is acyclic and the reverse finish-time order is a valid topological ordering.

A practical summary: use **BFS** when you need shortest paths (in unweighted graphs) or want to explore a graph level by level. Use **DFS** when you need to detect cycles, produce a topological sort, find strongly connected components, or exhaustively enumerate paths. Both are linear-time O(V + E) — the difference is not efficiency but what structure each exposes.
