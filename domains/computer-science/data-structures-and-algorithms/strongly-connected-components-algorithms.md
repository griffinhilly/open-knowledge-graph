---
id: strongly-connected-components-algorithms
title: 'Strongly Connected Components: Kosaraju and Tarjan Algorithms'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: graph-depth-first-search-applications
  type: hard
- id: topological-sort
  type: soft
tags:
- scc
- kosaraju
- tarjan
- graph-algorithm
stage: formal-systems
status: draft
---

# Strongly Connected Components: Kosaraju and Tarjan Algorithms

## Core Idea
A strongly connected component (SCC) is a maximal subgraph where every vertex reaches every other vertex. Kosaraju's algorithm: DFS forward, DFS backward on transpose in reverse finish order. Tarjan's: single DFS with a stack, outputs SCCs on the fly. Both run in O(V + E).

## Explainer

From your work with DFS applications, you know that depth-first search reveals structural properties of directed graphs — back edges indicate cycles, finish times encode reachability information, and the transpose graph reverses all edges. **Strongly connected components** (SCCs) decompose a directed graph into its most tightly connected pieces: within each SCC, every vertex can reach every other vertex via directed paths. Between SCCs, the connections are one-directional — forming a DAG (directed acyclic graph) of components. This decomposition is fundamental because it reduces a complex cyclic graph to a simpler DAG structure that you can analyze with topological sort.

**Kosaraju's algorithm** uses two passes of DFS. In the first pass, run DFS on the original graph and record each vertex's finish time. Vertices that finish later in DFS tend to be in SCCs that can reach more of the graph. In the second pass, construct the **transpose graph** (reverse every edge) and run DFS again, but process vertices in decreasing order of their first-pass finish times. Each DFS tree in this second pass corresponds to exactly one SCC. The intuition: the vertex with the latest finish time belongs to a "source" SCC in the component DAG. In the transpose graph, that source becomes a sink, so DFS from it only reaches vertices within the same SCC. Once that component is removed, the next highest-finish-time vertex identifies the next SCC, and so on.

**Tarjan's algorithm** accomplishes the same decomposition in a single DFS pass using a cleverly maintained stack. Each vertex is assigned a **discovery index** (when it was first visited) and a **low-link value** (the smallest discovery index reachable from it through the DFS subtree and back edges). As DFS explores, vertices are pushed onto a stack. When DFS finishes a vertex and its low-link value equals its own discovery index, that vertex is the **root** of an SCC — pop everything from the stack down to and including that vertex, and you have the complete SCC. The low-link value propagates upward through the DFS: if a descendant can reach back to an ancestor, the ancestor's low-link is updated, and the SCC won't be popped until the true root is finished.

Both algorithms run in O(V + E) — linear in the size of the graph. Kosaraju's is often easier to understand and implement (two standard DFS passes), while Tarjan's is more elegant (single pass, no transpose construction) and can be preferred when memory or implementation simplicity matters. The SCC decomposition itself has wide applications: in a dependency graph, SCCs represent circular dependencies; in a web graph, they identify clusters of mutually linked pages; and condensing the graph to its **DAG of SCCs** enables efficient reachability queries using topological ordering.
