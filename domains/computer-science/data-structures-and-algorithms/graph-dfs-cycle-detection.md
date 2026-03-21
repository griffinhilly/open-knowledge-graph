---
id: graph-dfs-cycle-detection
title: Depth-First Search and Cycle Detection
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: stacks-data-structure
  type: soft
- id: adjacency-list-representation
  type: soft
tags:
- dfs
- cycle-detection
- graph-traversal
- recursive
- back-edges
stage: formal-systems
status: draft
---

# Depth-First Search and Cycle Detection

## Core Idea
DFS explores a graph by going as deep as possible before backtracking, typically implemented recursively. It detects cycles via back edges: an edge to an ancestor in the DFS tree indicates a cycle. DFS also computes connected components, topological order, and strongly connected components in O(V + E) time.

## How It's Best Learned
Trace DFS by hand, noting pre- and post-visit times. Implement both recursively and iteratively (stack-based). Understand the three edge types (tree, forward, back, cross) and which indicate cycles. Use DFS for cycle detection and topological sorting.

## Common Misconceptions
- DFS must be recursive (iterative with a stack works equally well). - Back edges always exist if a cycle exists (yes in undirected graphs; in directed graphs, back edges specifically indicate cycles).

## Questions

```yaml
- question: "You implement directed-graph cycle detection using only two colors: 'unvisited' and 'visited'. When DFS finds an edge to a visited vertex, you report a cycle. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "It will miss cycles because back edges look the same as tree edges in a two-color scheme"
    - "It produces false positives — an edge to a fully-processed vertex is a cross or forward edge, not a cycle"
    - "It works correctly for directed graphs but fails for undirected graphs"
    - "The approach is correct; two colors are sufficient for any graph"
  answer: 1
  explanation: "A two-color scheme cannot distinguish between a gray vertex (currently on the recursion stack — an ancestor) and a black vertex (fully processed and off the stack). An edge to a black vertex is a cross or forward edge and does not indicate a cycle. Only an edge to a gray vertex (a white→gray back edge) indicates a cycle. Without the gray/black distinction, you incorrectly flag those harmless edges as cycles. This is why directed cycle detection requires the three-color white/gray/black scheme."

- question: "In undirected graph DFS, when traversing from vertex v to neighbor u, you find that u is already visited. Before declaring a cycle, what must you check?"
  type: multiple-choice
  options:
    - "Whether u has a higher discovery time than v"
    - "Whether u is the parent of v in the DFS tree"
    - "Whether u is in the same connected component as v"
    - "Whether the edge (v, u) is a tree edge or a back edge"
  answer: 1
  explanation: "In an undirected graph, the edge you just traversed to reach v from its parent also exists in the reverse direction. When you examine v's neighbors and see the parent, that is not a back edge — it is just the undirected edge you arrived on. Without checking 'is u my parent?', you would falsely report a cycle on every single edge. A genuine back edge in an undirected graph is an edge to a visited vertex that is NOT the parent, forming an actual cycle. Undirected graphs do not need the three-color scheme precisely because there are only tree edges and back edges (no forward or cross edges), so the parent check is sufficient."

- question: "In directed graph DFS, an edge from vertex v to a fully-processed (black) vertex indicates a cycle."
  type: true-false
  answer: false
  explanation: "An edge to a black vertex is either a forward edge (to a descendant that was already fully processed in a prior subtree) or a cross edge (to a vertex in a different DFS subtree). Neither creates a cycle. A cycle requires a path back to an ancestor — which means an edge to a gray vertex (one currently on the active recursion stack). The white/gray/black scheme exists precisely to distinguish ancestors (gray) from merely-visited-but-finished vertices (black)."

- question: "If DFS on a directed graph completes without ever encountering an edge to a gray vertex, the graph is a DAG and the reverse of DFS finish times gives a valid topological ordering."
  type: true-false
  answer: true
  explanation: "The absence of any edge to a gray vertex means no back edges exist, which is equivalent to the graph being a directed acyclic graph (DAG). DFS finish times encode a topological relationship: if there is a directed path from u to v, u finishes after v. Reversing the finish order therefore yields a valid topological sort. This is the standard linear-time topological sort algorithm — DFS with no back edges detected, reversed finish order output."

- question: "Why does directed-graph cycle detection require a three-color (white/gray/black) scheme while undirected-graph cycle detection only needs a visited/unvisited flag plus a parent check?"
  type: short-answer
  answer: "In directed graphs, edges come in four types: tree, back, forward, and cross. Only back edges (to a gray, in-progress ancestor) indicate cycles; forward and cross edges do not. Without distinguishing gray (on the stack) from black (finished), you cannot tell cycles from harmless cross or forward edges. In undirected graphs, forward and cross edges cannot exist — every non-tree edge is a back edge — so simply checking 'visited and not my parent' is sufficient to detect a cycle. The parent check handles the false-positive case where the undirected edge back to the parent looks like a back edge."
```

## Explainer

You already understand depth-first search as a traversal strategy: pick a starting vertex, explore as far as possible along one branch, then backtrack and try the next. During this traversal, DFS implicitly classifies every edge in the graph. **Tree edges** are the edges DFS follows to discover new vertices — they form the DFS tree (or forest). The remaining edges connect vertices that are already discovered, and their classification reveals the graph's structure. The most important category for cycle detection is the **back edge**: an edge from a vertex to one of its ancestors in the DFS tree.

Why do back edges indicate cycles? A back edge from vertex `v` to ancestor `u` means there is a path from `u` down through the DFS tree to `v` (the tree edges), and also a direct edge from `v` back to `u` (the back edge). Together, these form a cycle: `u → ... → v → u`. Conversely, if a cycle exists, DFS must encounter a back edge — when it first reaches the cycle, it will traverse tree edges around most of the cycle until it finds an edge leading back to an already-visited ancestor. So the rule is simple: **a graph contains a cycle if and only if DFS encounters a back edge**.

For **undirected graphs**, implementation is straightforward. Maintain a visited set and track each vertex's parent in the DFS tree. When you examine a neighbor of the current vertex, if it is already visited and it is not the parent, you have found a back edge — and therefore a cycle. The parent check is necessary because in an undirected graph, the edge you just traversed from parent to child also exists from child to parent; without the check, you would falsely detect a "cycle" on every edge.

For **directed graphs**, the situation is more subtle because edges are classified into four types: tree, back, forward (to a descendant), and cross (to a vertex in a different subtree). Only back edges indicate cycles — a forward or cross edge does not create one. To detect back edges in a directed graph, you need to distinguish between vertices that are **currently on the recursion stack** (ancestors of the current vertex) and vertices that are merely visited (fully processed and off the stack). Use a three-color scheme: white (unvisited), gray (in progress — on the stack), and black (finished). If DFS encounters an edge to a gray vertex, that is a back edge and a cycle exists. An edge to a black vertex is a cross or forward edge and is harmless. This gray/black distinction is also the foundation for **topological sorting**: if DFS completes without finding any back edges, the graph is a DAG (directed acyclic graph), and the reverse of the finish order gives a valid topological ordering.
