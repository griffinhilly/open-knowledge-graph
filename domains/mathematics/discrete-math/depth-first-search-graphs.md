---
id: depth-first-search-graphs
title: Depth-First Search (DFS)
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: big-o-notation
  type: soft
builds-toward:
- topological-sorting
- strongly-connected-components
- cycle-detection-directed-graphs
tags:
- graph-algorithms
- traversal
- dfs
stage: formal-systems
status: validated
---

# Depth-First Search (DFS)

## Core Idea
Depth-first search systematically explores a graph by going as deep as possible before backtracking. Starting from a source vertex, DFS visits adjacent unvisited vertices recursively, generating a DFS tree. It runs in O(V+E) time and is fundamental to many graph algorithms.

## How It's Best Learned
Trace DFS by hand on small graphs, maintaining a stack of vertices to visit. Observe how DFS discovers edges as tree edges, back edges, and cross edges in directed graphs.

## Common Misconceptions
- Confusing the DFS tree with the original graph structure. - Assuming DFS always finds the shortest path, which is true only for unweighted graphs in BFS.

## Questions

```yaml
- question: "During a DFS of a directed graph, you encounter an edge (u, v) where v is already discovered and is an ancestor of u in the DFS tree. What does this edge indicate?"
  type: multiple-choice
  options:
    - "A cross edge — v was discovered in a different DFS subtree"
    - "A forward edge — v is a descendant of u"
    - "A back edge — and this means there is a cycle in the graph"
    - "A tree edge — v has not been fully processed yet"
  answer: 2
  explanation: "An edge (u, v) where v is an ancestor of u in the DFS tree is a back edge. Back edges are the signature of cycles: you can traverse from v down to u (via the tree path) and then jump back to v (via the back edge), forming a cycle. This is why DFS-based cycle detection is straightforward: a back edge exists if and only if a cycle exists. Cross edges go between different subtrees; forward edges go to already-finished descendants; tree edges are the edges DFS actually traversed."

- question: "You run DFS on a graph with V = 1,000 vertices and E = 50,000 edges. Which best describes the time complexity, and why?"
  type: multiple-choice
  options:
    - "O(V²) — because DFS must compare every pair of vertices to decide if they're connected"
    - "O(V + E) — because each vertex is processed once and each edge is examined once"
    - "O(E log V) — because the DFS tree requires sorting edges by discovery order"
    - "O(V × E) — because each vertex may trigger exploration of all edges"
  answer: 1
  explanation: "DFS runs in O(V + E): each vertex is discovered and finished exactly once (O(V) total), and each edge is examined exactly once when DFS processes its source vertex (O(E) total). There is no sorting, no repeated work, and no nested iteration over all vertices per edge. O(V + E) is optimal for graph traversal — you cannot process a graph without visiting every vertex and edge at least once."

- question: "In a DFS tree, if vertex v is a descendant of vertex u, then u's discovery time is less than v's discovery time, which is less than v's finish time, which is less than u's finish time."
  type: true-false
  answer: true
  explanation: "This is the parenthesis theorem for DFS timestamps. Because DFS recurses into v's subtree while u is still on the stack, u's interval [disc(u), fin(u)] completely contains v's interval [disc(v), fin(v)]. This nesting property is the key structural insight behind topological sorting (vertices finish in reverse topological order) and strongly connected component algorithms (Kosaraju's and Tarjan's both exploit finish-time ordering)."

- question: "DFS is preferred over BFS when you need to find the shortest path between two vertices in an unweighted graph."
  type: true-false
  answer: false
  explanation: "BFS, not DFS, finds shortest paths in unweighted graphs. BFS explores vertices level by level (by hop count), so the first time it reaches a vertex is via the shortest path. DFS dives deep immediately and may reach a vertex via a long, indirect path long before it would try a shorter one. The file mentions this directly as a common misconception. DFS's strength lies in cycle detection, topological sort, and SCC — not shortest paths."

- question: "Why do DFS discovery and finish timestamps enable topological sorting of a directed acyclic graph?"
  type: short-answer
  answer: "In a DAG, if there is a directed edge from u to v (u must come before v), DFS will always finish u after it finishes v — because DFS fully explores v's subtree before returning to finish u. So processing vertices in reverse finish-time order gives a valid topological ordering: every vertex appears before the vertices it has edges to."
  explanation: "The finish-time ordering works because the DFS parenthesis structure captures 'comes before' relationships: if u depends on nothing that v depends on, u finishes later. Reversing this gives the topological order. This is why a single DFS pass suffices for topological sort — the timestamps implicitly encode the dependency ordering without any additional work."
```

## Explainer

Think of DFS as exploring a maze using the rule "always go as deep as you can before turning back." You enter a corridor, keep walking forward into new corridors, and only backtrack when you hit a dead end — then you return to the last junction you hadn't fully explored. This explore-deep-first strategy is exactly what DFS implements on a graph. Starting from a source vertex, DFS visits an unvisited neighbor, then immediately recurses into *that* vertex's neighbors before returning. The call stack (or an explicit stack data structure) remembers where to backtrack.

From your prerequisite knowledge of graph theory, you know that a graph G = (V, E) consists of vertices and edges. DFS systematically marks each vertex as **discovered** when first visited and **finished** when all its neighbors have been explored. The edges DFS traverses form a **DFS tree** — a spanning substructure rooted at the source. Not all edges of the original graph end up in this tree, and classifying the non-tree edges is one of DFS's most powerful features. In a directed graph, an edge (u, v) is a **back edge** if v is an ancestor of u in the DFS tree (meaning there's a cycle), a **forward edge** if v is a descendant but not a child, or a **cross edge** otherwise.

The runtime of O(V + E) follows naturally from the structure: each vertex is discovered and finished exactly once (contributing O(V)), and each edge is examined exactly once when DFS processes the vertex it leaves from (contributing O(E)). If you've seen Big-O notation, this is as good as it gets for graph traversal — you can't process a graph without at least touching every vertex and edge.

The real power of DFS lies in what the discovery and finish times reveal. If you record a **timestamp** when each vertex is discovered and when it's finished, these intervals nest cleanly: if v is a descendant of u in the DFS tree, then u's discovery time < v's discovery time < v's finish time < u's finish time. This **parenthesis structure** is the engine behind topological sorting (process vertices in reverse finish order), cycle detection (a back edge exists if and only if a cycle exists), and finding strongly connected components. DFS is not just a traversal — it is a framework that, with small instrumentation changes, solves an entire family of graph problems.
