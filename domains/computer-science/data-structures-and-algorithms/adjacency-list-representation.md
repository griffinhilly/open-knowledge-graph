---
id: adjacency-list-representation
title: Adjacency List Graph Representation
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: linked-lists
  type: soft
- id: graph-theory-intro
  type: soft
builds-toward:
- breadth-first-search
- depth-first-search
- graph-bfs-unweighted-shortest-path
tags:
- graphs
- adjacency-list
- representation
- sparse
- memory-efficient
stage: formal-systems
status: validated
---
# Adjacency List Graph Representation

## Core Idea
An adjacency list represents a graph as an array of lists, where each vertex has a list of adjacent vertices. This representation is space-efficient for sparse graphs (E ≪ V²), using O(V + E) space. It is ideal for DFS, BFS, and most graph algorithms, as neighbor iteration is naturally efficient.

## How It's Best Learned
Build adjacency lists by hand for directed and undirected graphs. Implement neighbor iteration. Compare space usage to adjacency matrix for sparse vs. dense graphs. Trace BFS and DFS using adjacency list representation.

## Common Misconceptions
- Adjacency list is always better than adjacency matrix (adjacency matrix is faster for dense graphs and edge-existence queries). - Adjacency lists require linked lists (vectors of vectors work better in practice for cache locality).

## Questions

```yaml
- question: "You are implementing an algorithm on a dense graph (E ≈ V²) that frequently checks whether a specific edge (u, v) exists. Which representation is more appropriate?"
  type: multiple-choice
  options:
    - "Adjacency list — it always uses less memory than a matrix"
    - "Adjacency matrix — it provides O(1) edge-existence queries and is efficient when E ≈ V²"
    - "Adjacency list — neighbor iteration is O(degree(v)), which is fast for dense graphs"
    - "Adjacency matrix — it requires less preprocessing before running graph algorithms"
  answer: 1
  explanation: "For dense graphs (E ≈ V²), the adjacency matrix's O(V²) space is not wasteful because nearly all entries are occupied. The decisive advantage is O(1) edge-existence queries: to check if edge (u, v) exists, look up matrix[u][v] in constant time. With an adjacency list, you must scan through u's neighbor list — O(degree(u)) time. When edge queries are frequent and the graph is dense, the matrix wins. Option A is incorrect: for dense graphs, both representations use comparable space."

- question: "A graph has V = 1,000 vertices and E = 3,000 edges. How does the space usage of an adjacency list compare to an adjacency matrix?"
  type: multiple-choice
  options:
    - "Adjacency list: O(V²) ≈ 1,000,000 entries; Adjacency matrix: O(V + E) ≈ 4,000 entries"
    - "Both use O(V + E) ≈ 4,000 entries, since the matrix stores only existing edges"
    - "Adjacency list: O(V + E) ≈ 4,000 entries; Adjacency matrix: O(V²) = 1,000,000 entries"
    - "Adjacency list: O(E) = 3,000 entries; Adjacency matrix: O(V) = 1,000 entries"
  answer: 2
  explanation: "The adjacency list uses O(V + E) space: V list headers plus E total neighbor entries — roughly 4,000 entries here. The adjacency matrix always allocates V² cells regardless of actual edges — one million entries for a 1,000-vertex graph. With only 3,000 edges (E ≪ V²), the graph is very sparse and the matrix wastes ~997,000 entries. This gap is the central efficiency argument for adjacency lists on sparse graphs."

- question: "An adjacency list is more space-efficient than an adjacency matrix when the graph is sparse (E ≪ V²)."
  type: true-false
  answer: true
  explanation: "The adjacency list uses O(V + E) space, storing only edges that actually exist. The adjacency matrix always uses O(V²) space. When E is much smaller than V², the list can be orders of magnitude more compact. For a graph with 10,000 vertices and 20,000 edges: the list uses ~20,000 entries while the matrix requires 100,000,000 — a 5,000× difference."

- question: "Checking whether edge (u, v) exists takes O(1) time with an adjacency list, just as it does with an adjacency matrix."
  type: true-false
  answer: false
  explanation: "With an adjacency matrix, edge (u, v) is a single array lookup: matrix[u][v] — O(1). With a basic adjacency list, you must scan through u's neighbor list to find v — O(degree(u)) in the worst case. For a high-degree vertex in a dense graph, this approaches O(V). This is the primary disadvantage of adjacency lists, and why adjacency matrices are preferred for algorithms requiring frequent individual edge-existence queries."

- question: "Why is an adjacency list the preferred representation for BFS and DFS rather than an adjacency matrix?"
  type: short-answer
  answer: "BFS and DFS both iterate over all neighbors of each vertex. With an adjacency list, iterating vertex v's neighbors takes O(degree(v)) — proportional to actual edges. With a matrix, it requires scanning an entire row of V entries, most of which may be zero — O(V) per vertex. Total traversal cost: O(V + E) with a list vs. O(V²) with a matrix. For sparse graphs, this gap makes the difference between a practical and an impractical algorithm."
  explanation: "The total work across a full BFS/DFS adds up each vertex's neighbor iteration: Σ degree(v) = 2E (each edge counted twice for undirected graphs) plus V for the vertex list headers = O(V + E). With a matrix, each vertex requires O(V) work regardless of its degree, giving O(V²) total. For sparse graphs where E ≪ V², the adjacency list wins decisively."
```

## Explainer

You already know that a graph consists of vertices and edges, and that arrays let you store collections with indexed access. An **adjacency list** combines these ideas: for each vertex in the graph, you maintain a list of the vertices it connects to. If vertex 0 has edges to vertices 1, 3, and 4, then the entry at index 0 holds the list [1, 3, 4]. The entire graph is stored as an array of these per-vertex lists — conceptually, an array of arrays.

Consider a social network with 1,000 users where each person has about 150 friends. An adjacency matrix would allocate a 1,000 × 1,000 grid — one million entries — even though only about 150,000 of them (counting both directions) represent actual friendships. The adjacency list stores only the edges that exist: 1,000 lists averaging 150 entries each, totaling roughly 150,000 entries. This is the O(V + E) space guarantee — you pay for the number of vertices (the array of lists) plus the number of edges (the entries within those lists). For **sparse graphs** where E is much less than V², this is dramatically more efficient than the O(V²) matrix.

The adjacency list's real strength shows up when you need to iterate over a vertex's neighbors — the most common operation in graph algorithms. In BFS, you visit every neighbor of the current vertex. In DFS, you explore neighbors recursively. With an adjacency list, iterating over the neighbors of vertex v takes O(degree(v)) time — you simply walk through v's list. With an adjacency matrix, the same operation requires scanning an entire row of V entries, most of which may be zero. For sparse graphs, this difference is the gap between a practical algorithm and an impractical one.

The tradeoff appears when you need to answer "does edge (u, v) exist?" With an adjacency matrix, this is a single O(1) array lookup. With a basic adjacency list, you must search through u's neighbor list, which takes O(degree(u)) time. For algorithms that frequently check edge existence (like certain dense-graph optimizations), the matrix wins. In practice, most graph algorithms — shortest paths, connected components, topological sort — spend their time iterating over neighbors rather than checking individual edges, which is why adjacency lists are the default choice. Implementation-wise, despite the name "list," using a dynamic array (vector) for each vertex's neighbors gives better cache performance than linked list nodes scattered across memory.
