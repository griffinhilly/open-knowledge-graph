---
id: graph-adjacency-list-matrix-representations
title: "Graph Representations: Adjacency List vs. Adjacency Matrix"
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-lists
  type: hard
- id: linked-lists
  type: hard
builds-toward:
- graph-depth-first-search-applications
- graph-breadth-first-search-applications
tags:
- graph
- representation
- adjacency
stage: formal-systems
status: validated
---
# Graph Representations: Adjacency List vs. Adjacency Matrix

## Core Idea
Adjacency lists use O(V + E) space, fast for sparse graphs; adjacency matrices use O(V²) space, fast for edge lookups. Dense graphs (E ≈ V²) favor matrices; sparse graphs (E ≪ V²) favor lists. Representation choice affects algorithm complexity.

## Questions

```yaml
- question: "You are implementing BFS on a social network graph with 1 million users (V = 10⁶) and 10 million friendships (E = 10⁷). Which representation gives better BFS performance, and why?"
  type: multiple-choice
  options:
    - "Adjacency matrix — O(1) edge lookup makes the traversal faster at each step"
    - "Adjacency list — O(V + E) traversal avoids scanning empty matrix rows for sparse graphs"
    - "Either is equivalent — BFS visits every edge once regardless of representation"
    - "Adjacency matrix — it uses less memory since it is stored as a fixed-size array"
  answer: 1
  explanation: "BFS examines every vertex and every edge once. With an adjacency list, this costs O(V + E) = O(10⁶ + 10⁷) ≈ O(10⁷). With an adjacency matrix, you must scan every row to find neighbors, even rows with few or no edges — that costs O(V²) = O(10¹²). The graph here is very sparse (E/V = 10, far below V = 10⁶), so the matrix wastes enormous work scanning empty entries. Option A is wrong because O(1) edge lookup is not the bottleneck in BFS — finding all neighbors is. Option D is wrong: the matrix would require storing 10¹² entries, vastly more than the list's O(V + E) = O(10⁷)."

- question: "What is the time complexity of checking whether a directed edge from vertex u to vertex v exists in an adjacency list representation?"
  type: multiple-choice
  options:
    - "O(1) — array indexing gives direct access to u's neighbor list"
    - "O(V) — you must scan all vertices to find v"
    - "O(degree(u)) — you must scan u's neighbor list to find v"
    - "O(E) — edge lookup requires scanning all edges in the worst case"
  answer: 2
  explanation: "In an adjacency list, you index directly into the list for vertex u in O(1), but then must scan that list to check whether v appears in it. In the worst case (v is last or absent), this scans all of u's neighbors, taking O(degree(u)). For a vertex with high degree, this can be slow. By contrast, an adjacency matrix answers the same question in O(1) by reading matrix[u][v] directly. This is the fundamental trade-off: adjacency lists are space-efficient but slow for edge queries; matrices are space-hungry but fast for edge queries."

- question: "In an undirected graph stored as an adjacency list, each edge (u, v) is represented twice — once in u's list and once in v's list — so the total storage for edges is 2E entries."
  type: true-false
  answer: true
  explanation: "An undirected edge (u, v) means both u connects to v and v connects to u. In an adjacency list, v appears in u's neighbor list and u appears in v's neighbor list. So each undirected edge contributes two list entries. The total space for all edges is 2E, and with the V-entry array of lists, total space is O(V + 2E) = O(V + E). In a directed graph, each edge (u → v) appears only in u's list, so total edge entries equal E exactly."

- question: "An adjacency matrix usually uses less memory than an adjacency list because it avoids the pointer overhead of linked lists."
  type: true-false
  answer: false
  explanation: "An adjacency matrix always uses O(V²) space regardless of how many edges exist. An adjacency list uses O(V + E) space. For sparse graphs (E ≪ V²), the adjacency list is far more compact. For example, a graph with V = 10,000 vertices and E = 50,000 edges uses a 100-million-entry matrix vs. roughly 60,000 list entries — a 1,600× difference. The matrix only uses less memory when the graph is dense enough that E is close to V², in which case O(V + E) ≈ O(V²) anyway. Pointer overhead in adjacency lists is real but small relative to the O(V²) vs. O(V + E) space difference for sparse graphs."

- question: "Why does the choice between adjacency list and adjacency matrix affect the time complexity of BFS and DFS, not just memory usage?"
  type: short-answer
  answer: "BFS and DFS must examine every edge at least once. The representation determines how efficiently that examination happens. With an adjacency list, finding all neighbors of a vertex takes time proportional to its degree — you only look at edges that actually exist. Across the whole traversal, this sums to O(V + E). With an adjacency matrix, finding all neighbors of vertex u requires scanning the entire u-th row of V entries, whether or not those edges exist. This costs O(V) per vertex, for O(V²) total. For sparse graphs, O(V + E) is much smaller than O(V²), so the representation choice changes the asymptotic complexity of the algorithm, not just the constant factor."
  explanation: "The key insight is that representation determines what work the algorithm must do, not just how much memory it uses. An algorithm running on an adjacency matrix 'pays' for edges that don't exist — it must check each matrix entry to determine it's 0. An adjacency list skips non-edges entirely because they simply aren't listed. This is why adjacency lists are the default: most real-world graphs are sparse, and the algorithm's work should scale with what's actually there."
```

## Explainer

A graph is an abstract concept — vertices connected by edges — but to write algorithms that operate on graphs, you need a concrete data structure in memory. The two foundational choices are the **adjacency matrix** and the **adjacency list**, and the right choice depends on the shape of your graph and the operations your algorithm needs. Both build directly on arrays and linked lists, the data structures you already know.

An **adjacency matrix** is a V × V two-dimensional array where entry matrix[i][j] is 1 (or the edge weight) if there is an edge from vertex i to vertex j, and 0 otherwise. The appeal is simplicity and speed for one specific operation: checking whether an edge exists between two vertices is a single O(1) array lookup. For an undirected graph, the matrix is symmetric (matrix[i][j] = matrix[j][i]), which means half the storage is redundant. The cost is space: regardless of how many edges exist, you always allocate V² entries. A graph with 10,000 vertices requires a 100-million-entry matrix even if it has only 20,000 edges.

An **adjacency list** takes the opposite approach. You maintain an array of V lists (or dynamic arrays), one per vertex. The list at index i contains only the vertices that i actually connects to. If vertex i has 3 neighbors, its list has 3 entries — not V entries. Total space is O(V + E): V for the array of lists, and E for all the neighbor entries combined (2E for undirected graphs, since each edge appears in two lists). For sparse graphs — and most real-world graphs are sparse — this savings is enormous. The tradeoff is that checking "does edge (u, v) exist?" requires scanning u's neighbor list, which takes O(degree(u)) instead of O(1).

The choice between representations cascades through algorithm performance. BFS and DFS visit every vertex and examine every edge once — with an adjacency list, this takes O(V + E), but with a matrix, examining all edges requires scanning every row completely for O(V²) regardless of sparsity. For sparse graphs, O(V + E) can be vastly smaller. Conversely, algorithms that need constant-time edge lookups or that operate on dense graphs (where E approaches V²) lose nothing with a matrix and gain simpler code. Weighted graphs work naturally with both: the matrix stores weights instead of 1s, and each list entry becomes a (neighbor, weight) pair. In practice, adjacency lists are the default starting point, and you switch to a matrix only when your graph is dense or your algorithm's bottleneck is edge-existence queries.
