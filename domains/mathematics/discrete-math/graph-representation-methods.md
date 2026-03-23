---
id: graph-representation-methods
title: 'Graph Representation: Adjacency Lists, Matrices, and Edge Lists'
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: hard
builds-toward:
- graph-isomorphism-equivalence
tags:
- graph-theory
- representation
stage: formal-systems
status: validated
---

# Graph Representation: Adjacency Lists, Matrices, and Edge Lists

## Core Idea
Graphs can be represented as adjacency matrices (n×n where entry (i,j) is the edge weight), adjacency lists (list of neighbors for each vertex), or edge lists (list of all edges). Each representation has different time and space tradeoffs depending on graph density and algorithm requirements.

## Questions

```yaml
- question: "A social network graph has 100,000 users (vertices) but each user follows an average of only 50 others (edges). Which representation is most space-efficient?"
  type: multiple-choice
  options:
    - "Adjacency matrix — O(1) edge lookup is essential for a network this large"
    - "Adjacency list — it uses O(n + m) space proportional to what actually exists"
    - "Edge list — it uses O(m) space and is always smallest"
    - "Adjacency matrix — it handles weighted edges better than lists"
  answer: 1
  explanation: "With n = 100,000 vertices and m ≈ 5,000,000 edges (100,000 × 50 / 2), an adjacency matrix needs O(n²) = 10¹⁰ cells — enormously wasteful for a sparse graph. The adjacency list uses O(n + m) ≈ 5,100,000 entries, proportional only to what exists. An edge list uses O(m) but doesn't support fast neighbor lookup. The common misconception is to prefer the matrix for its O(1) lookup without accounting for its space cost in sparse graphs."

- question: "You are implementing Kruskal's minimum spanning tree algorithm, which sorts all edges by weight and processes them in order without needing to look up a specific vertex's neighbors. Which representation is most natural?"
  type: multiple-choice
  options:
    - "Adjacency matrix — it allows O(1) weight lookup for any edge"
    - "Adjacency list — it handles degree queries efficiently"
    - "Edge list — it stores edges directly and is easy to sort and iterate"
    - "Adjacency matrix — it naturally supports sparse and dense graphs equally"
  answer: 2
  explanation: "Kruskal's algorithm processes edges in sorted order without ever asking 'what are vertex u's neighbors?' — it asks 'give me all edges sorted by weight.' An edge list stores exactly this: a collection of (u, v, weight) triples that is trivially sorted and iterated. The adjacency list is designed for neighbor traversal (BFS, DFS, Dijkstra's), and the matrix is designed for O(1) edge existence checks — neither fits Kruskal's access pattern as naturally."

- question: "An adjacency matrix always uses more memory than an adjacency list for the same graph."
  type: true-false
  answer: false
  explanation: "For dense graphs where nearly every pair of vertices is connected (m ≈ n²), the adjacency list uses O(n + m) ≈ O(n²) space — comparable to the matrix's O(n²), and potentially more due to pointer overhead. The matrix is generally more space-efficient for dense graphs. The statement is only true for sparse graphs where m << n². Representation choice depends on graph density, not a universal rule."

- question: "Checking whether a specific edge (u, v) exists takes O(1) time with an adjacency list."
  type: true-false
  answer: false
  explanation: "With an adjacency list, checking whether (u, v) exists requires scanning vertex u's neighbor list, taking O(degree(u)) time — potentially O(n) in a dense graph. The O(1) edge existence check is the defining advantage of the adjacency matrix, where you simply look up entry (u, v) in constant time. This is the key tradeoff: matrix wins for edge queries; list wins for space in sparse graphs and for iterating all neighbors."

- question: "Why might a developer use different graph representations for different algorithms operating on the same underlying graph?"
  type: short-answer
  answer: "Because each representation optimizes for different operations: adjacency matrices give O(1) edge existence checks but O(n²) space; adjacency lists give efficient neighbor iteration in O(degree) time with O(n + m) space; edge lists support simple edge iteration in O(m) time. Dijkstra's repeatedly asks 'what are this vertex's neighbors?', making adjacency lists natural. Floyd-Warshall processes every vertex pair, making a matrix natural. Kruskal's needs sorted edges, making an edge list natural. Converting between representations is sometimes worth the cost."
  explanation: "The key insight is that no representation is universally optimal — optimality depends on which operations an algorithm performs most frequently. A good programmer builds the representation that matches the algorithm's access pattern, even if that means converting a stored graph from one form to another at algorithm boundaries. Understanding all three representations and their tradeoffs is therefore as important as knowing any single one."
```

## Explainer

From graph theory fundamentals, you know a graph is an abstract object: a set of vertices and a set of edges between them. But to actually *compute* with a graph — run an algorithm, store it in memory, search it — you need to encode that abstract structure in concrete form. The choice of representation shapes what operations are fast, how much memory you use, and which algorithms become natural to implement.

The **adjacency matrix** represents a graph as an n×n grid where row i, column j holds the weight of the edge from vertex i to vertex j (or 1 if unweighted, 0 if no edge). This makes one question instant: "Is there an edge between vertex i and vertex j?" — just look up the cell in O(1). But it costs O(n²) space regardless of how many edges actually exist. For a sparse graph with only a handful of edges per vertex, this wastes enormous space storing zeros. For a dense graph where nearly every pair of vertices is connected, the matrix is a natural fit.

The **adjacency list** stores, for each vertex, a list of its neighbors (and optionally edge weights). A graph with n vertices and m edges uses O(n + m) space — proportional only to what actually exists. Iterating over all edges from a given vertex is fast (just walk its list), which makes adjacency lists ideal for algorithms like BFS, DFS, and Dijkstra's that repeatedly ask "what are this vertex's neighbors?" The tradeoff is that checking whether a specific edge (u, v) exists requires scanning u's neighbor list, taking O(degree(u)) time in the worst case rather than O(1).

The **edge list** is the simplest representation: just an unordered collection of (u, v, weight) triples. It uses O(m) space and is easy to iterate over all edges, making it natural for algorithms that process every edge once — like Kruskal's minimum spanning tree algorithm. However, it is slow for neighbor lookups or checking edge existence. The right choice depends on the algorithm: Dijkstra's wants adjacency lists; Floyd-Warshall wants a matrix; Kruskal's wants an edge list. In practice, understanding all three and knowing when to convert between them is as important as knowing the representations themselves.
