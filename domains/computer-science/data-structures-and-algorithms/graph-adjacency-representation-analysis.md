---
id: graph-adjacency-representation-analysis
title: 'Graph Representations: Adjacency List and Matrix'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-theory-intro
  type: soft
- id: graph-theory-fundamentals
  type: soft
builds-toward:
- breadth-first-search
- depth-first-search
tags:
- graphs
- representation
- implementation
stage: formal-systems
status: validated
---

# Graph Representations: Adjacency List and Matrix

## Core Idea
Graphs are represented as adjacency lists (O(V+E) space, O(degree) to traverse neighbors) or adjacency matrices (O(V²) space, O(1) edge lookup). Choice depends on graph density: sparse graphs favor lists, dense graphs favor matrices. Weighted edges naturally extend both.

## How It's Best Learned
Implement both representations for the same graph. Measure space and time for edge lookup, neighbor traversal, and insertion. Run BFS/DFS on both and observe differences in memory and cache behavior.

## Common Misconceptions
- Assuming one representation is universally better; the choice depends on V, E, and query patterns.
- Thinking adjacency lists are always efficient; with poor hash functions or linked lists, traversal can be slow.
- Not accounting for the cost of dynamic graph modifications (edge insertion/deletion).

## Questions

```yaml
- question: "A social network has 1 million users (V = 10⁶) and each user averages 200 connections (E ≈ 10⁸). A developer argues that an adjacency matrix is preferable because O(1) edge lookup will speed up friend-of-friend queries. What is the critical problem with this choice?"
  type: multiple-choice
  options:
    - "Adjacency matrices do not support weighted edges, which are needed for social networks"
    - "An adjacency matrix would require V² = 10¹² entries — roughly a terabyte of memory — to represent what fits in a few gigabytes with an adjacency list"
    - "O(1) edge lookup is actually slower in practice because of cache misses"
    - "Adjacency matrices cannot represent directed graphs, which social networks require"
  answer: 1
  explanation: "This is a sparse graph (E << V²). An adjacency matrix always allocates V² space regardless of edge count — here, 10¹² cells for a graph with only 10⁸ edges. The adjacency list uses O(V + E) ≈ O(10⁸) space. The O(1) lookup advantage is real but irrelevant when the representation is physically impractical."

- question: "You are implementing Dijkstra's algorithm on a sparse road network (10,000 cities, ~30,000 roads). The algorithm must repeatedly visit all neighbors of a given vertex. Which representation minimizes time for this operation?"
  type: multiple-choice
  options:
    - "Adjacency matrix, because O(1) cell access makes neighbor lookup instantaneous"
    - "Adjacency list, because iterating neighbors takes O(degree) time rather than O(V) time"
    - "Adjacency matrix, because its regular memory layout improves cache performance for row scans"
    - "Both representations take the same time, since each neighbor is eventually visited either way"
  answer: 1
  explanation: "With an adjacency list, visiting all neighbors takes O(degree) — proportional to how many neighbors actually exist. With an adjacency matrix, you must scan the entire row of V = 10,000 entries for each vertex, even if the vertex has only 3 neighbors. For a sparse graph, this O(V) per vertex is dramatically slower than O(degree)."

- question: "An adjacency list is always the better choice for graph representation because it uses less memory than an adjacency matrix."
  type: true-false
  answer: false
  explanation: "For dense graphs where E approaches V², an adjacency list uses roughly 2E ≈ V² space — comparable to an adjacency matrix — while also lacking its O(1) edge lookup. The adjacency matrix wins or ties on both memory and lookup speed in the dense case. The right choice depends on graph density and the query patterns of the algorithm you're running."

- question: "Checking whether edge (u, v) exists takes O(1) time with an adjacency matrix regardless of graph density."
  type: true-false
  answer: true
  explanation: "The adjacency matrix stores all edges in a 2D array; matrix[u][v] is a single array access — always O(1). This is the matrix's primary advantage. With a basic adjacency list, you must search u's neighbor list, which takes O(degree(u)) time (though a hash-set-backed list can also achieve O(1) expected time)."

- question: "Why does the choice between adjacency list and adjacency matrix matter for algorithms like BFS and DFS? What property of those algorithms makes one representation clearly preferable for sparse graphs?"
  type: short-answer
  answer: "BFS and DFS repeatedly iterate over all neighbors of each vertex. An adjacency list makes this O(degree) per vertex; an adjacency matrix requires scanning the full row of V entries per vertex, most of which are zeros in a sparse graph. Across the entire traversal, the list gives O(V + E) total work; the matrix gives O(V²) — a massive difference when E << V²."
  explanation: "The 'visit all neighbors' pattern is the heart of graph traversal. Adjacency lists are purpose-built for this — each list stores exactly the neighbors that exist, no more. Matrices store all possible edges (most absent), so every neighbor scan wastes time on empty cells."
```

## Explainer

From graph theory fundamentals, you know what graphs are — vertices connected by edges, directed or undirected, possibly weighted. But to actually compute anything with a graph, you need to store it in memory, and the choice of representation profoundly affects the performance of every algorithm you run on it. The two standard representations are the **adjacency matrix** and the **adjacency list**, and choosing between them is one of the first decisions in any graph algorithm implementation.

An **adjacency matrix** is a V×V two-dimensional array where entry [i][j] is 1 (or the edge weight) if there is an edge from vertex i to vertex j, and 0 otherwise. Its great strength is constant-time edge lookup: to check whether vertices u and v are connected, you simply read matrix[u][v] — one array access, O(1). Its weakness is space. The matrix always uses O(V²) memory regardless of how many edges actually exist. For a social network with a million users (V = 10⁶) but where each user has only a few hundred friends (E ≈ 10⁸), the matrix would allocate 10¹² entries — a terabyte — to store what could fit in a few gigabytes. Furthermore, iterating over all neighbors of a vertex requires scanning an entire row of V entries, even if the vertex has only 3 neighbors.

An **adjacency list** stores, for each vertex, a list of its neighbors (and edge weights if applicable). The total space is O(V + E): one list per vertex, and each edge appears once (directed) or twice (undirected) across all lists. Finding all neighbors of a vertex takes O(degree) time — you simply iterate the list — which makes adjacency lists ideal for algorithms like BFS and DFS that need to visit all neighbors of each vertex. The tradeoff is that checking whether a specific edge (u, v) exists requires searching u's neighbor list, which takes O(degree(u)) time with a simple list or O(1) expected time if you use a hash set instead.

The decision comes down to **graph density**. A graph is **dense** when E approaches V² (most possible edges exist) and **sparse** when E is much smaller than V². Most real-world graphs — social networks, road maps, web links, dependency graphs — are sparse. For sparse graphs, adjacency lists are almost always the right choice: they use far less memory and make neighbor iteration fast, which is exactly what BFS, DFS, Dijkstra's algorithm, and most other graph algorithms need. Adjacency matrices shine for dense graphs or when you need frequent O(1) edge existence checks, such as in certain matrix-based algorithms for transitive closure or graph powers. When you implement BFS and DFS next, you will see firsthand how naturally the adjacency list representation supports the "visit all neighbors" pattern that drives those traversals.
