---
id: depth-first-search
title: Depth-First Search (DFS)
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: recursion-basics
  type: hard
- id: graph-representation
  type: hard
- id: stacks-data-structure
  type: soft
- id: graph-theory-intro
  type: soft
- id: tree-traversals
  type: soft
builds-toward:
- topological-sort
- union-find
tags:
- DFS
- graph-traversal
- recursion
- cycle-detection
- connected-components
stage: formal-systems
status: validated
---
# Depth-First Search (DFS)

## Core Idea
Depth-first search (DFS) explores a graph by going as deep as possible along each branch before backtracking. It can be implemented recursively or iteratively with an explicit stack, and runs in O(V + E) time. DFS is the foundation for cycle detection, topological sorting, strongly connected components (Tarjan's and Kosaraju's algorithms), and solving maze-like problems. Tracking discovery and finish times during DFS produces edge classifications: tree edges, back edges (cycles), forward edges, and cross edges.

## How It's Best Learned
Implement recursive DFS tracking discovery and finish timestamps. Then implement the iterative stack version and verify equivalent results. Use DFS to detect cycles in both directed and undirected graphs as a practical exercise.

## Common Misconceptions
- DFS does not find shortest paths; BFS does.
- In an undirected graph, encountering an already-visited node that is not your direct parent indicates a cycle. In directed graphs, only a back edge (reaching an ancestor in the current DFS path) indicates a cycle.

## Questions

```yaml
- question: "During DFS on a directed graph, you visit node A, then B, then C — and from C you find an edge back to A, which is still on the current recursion stack. What type of edge is this, and what does it indicate?"
  type: multiple-choice
  options: ["A tree edge — it is part of the DFS spanning tree", "A back edge — it indicates a cycle in the directed graph", "A cross edge — it connects two unrelated branches", "A forward edge — it points to a descendant already fully processed"]
  answer: 1
  explanation: "A back edge points from a node to one of its ancestors in the current DFS recursion stack. Finding a back edge proves the graph has a directed cycle (A → B → C → A). Cross edges and forward edges point to already-visited nodes that are not current ancestors, so they do not indicate cycles in directed graphs."

- question: "DFS is a good algorithm for finding the shortest path between two nodes in an unweighted graph."
  type: true-false
  answer: false
  explanation: "DFS follows a single path as deep as possible before backtracking. It will find *a* path, but not necessarily the shortest one. BFS (breadth-first search) finds shortest paths in unweighted graphs because it explores all nodes at distance 1 before any at distance 2, guaranteeing the first time it reaches the target is via the shortest route."

- question: "What is the time complexity of DFS on a graph with V vertices and E edges, and why?"
  type: short-answer
  answer: "O(V + E). Each vertex is visited exactly once (O(V)), and each edge is examined exactly once when processing the vertex it originates from (O(E))."
  explanation: "DFS marks each vertex visited on first encounter and never revisits it. When processing a vertex, it checks all outgoing edges to find unvisited neighbors. Across all vertices, the total number of edge checks equals the total number of edges E. So the combined work is proportional to V + E, regardless of graph structure."
```

## Explainer

If you have written recursive tree traversals (like inorder or postorder), you have already implemented a special case of depth-first search — trees are acyclic graphs, and DFS on a tree is exactly what those traversals do. Generalizing to arbitrary graphs requires only one addition: a visited set to avoid processing the same node twice (and to prevent infinite loops in cyclic graphs).

The DFS algorithm works like this: start at a source node, mark it visited, then recursively visit each unvisited neighbor before returning. The "depth-first" name captures the behavior — you commit fully to one branch, following it to its dead end, before backtracking and trying another. The call stack (or an explicit stack data structure if implemented iteratively) holds the current path from the source to wherever you are. This is fundamentally different from BFS, which explores level by level. Neither is universally better — they answer different questions.

DFS has a remarkable side effect: the order in which nodes are *entered* (discovery time) and *exited* (finish time) produces a classification of every edge in the graph. A tree edge is one you traverse to an unvisited node. A back edge points from a node to an ancestor currently on the stack — finding one proves a cycle exists in the directed graph. Forward and cross edges cover other cases. This edge classification is the foundation for algorithms like topological sort (process nodes in reverse finish-time order) and strongly connected components (Tarjan's algorithm uses discovery and finish times directly).

Cycle detection deserves special care. In an undirected graph, any edge to an already-visited node that isn't your direct parent means a cycle exists (you reached the same node via two different paths). In a directed graph, the rule is stricter: only a back edge — one that points to a node still on the active recursion stack — proves a cycle. A directed edge to a node that was visited in a previous DFS branch (a cross edge) doesn't create a cycle, because that edge goes from one branch to another, not backward along the current path.

The O(V + E) time complexity follows naturally from the algorithm's structure: each vertex is visited exactly once, and each edge is examined exactly once when its source vertex is being processed. This makes DFS efficient even on large sparse graphs, and it's why DFS is the go-to building block for so many graph algorithms.
