---
id: cycle-detection-directed-undirected
title: Cycle Detection in Directed and Undirected Graphs
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: bipartite-graph-detection-coloring
  type: soft
- id: articulation-points-cut-vertices
  type: soft
builds-toward:
- topological-sort
tags:
- graphs
- cycles
- dfs
stage: formal-systems
status: validated
---
# Cycle Detection in Directed and Undirected Graphs

## Core Idea
In undirected graphs, a back edge (to a visited neighbor other than the parent) signals a cycle. In directed graphs, back edges are those to ancestors in the DFS tree. Both detections run in O(V+E) during DFS. Cycle detection is essential for dependency resolution and deadlock detection.

## How It's Best Learned
Implement DFS with three vertex states (white, gray, black). Use gray edges as back edges. Trace on examples with and without cycles. Apply to topological sorting and deadlock detection.

## Common Misconceptions
- Treating directed and undirected cycle detection identically; the algorithms differ significantly.
- Not handling self-loops and parallel edges correctly.
- Assuming cycle detection requires storing all edges; DFS detects them during traversal.

## Questions

```yaml
- question: "During DFS on a directed graph, you are exploring node A (currently gray) and discover an edge to node B, which is black (fully explored). What does this tell you?"
  type: multiple-choice
  options:
    - "There is a cycle involving A and B"
    - "B is a forward or cross edge destination — no cycle is indicated"
    - "The algorithm must backtrack and try a different path"
    - "This situation cannot occur in a directed graph"
  answer: 1
  explanation: "A back edge — the only kind that indicates a cycle in a directed graph — is an edge from a gray node to another gray node (both on the current DFS stack). An edge to a black node means B was fully explored in a prior DFS subtree with no path back to the current traversal. This is why directed cycle detection requires three colors: an edge to a visited-but-black node is NOT evidence of a cycle, unlike in undirected graphs."

- question: "In an undirected graph, DFS visits A, then B (from A), then C (from B). From C, DFS finds that A is already visited. Is there a cycle?"
  type: multiple-choice
  options:
    - "No — A is C's grandparent in the DFS tree, which is normal"
    - "Yes — A is visited and is not C's direct parent, so the edge C→A is a back edge revealing a cycle"
    - "Only if A is also connected to D"
    - "No — in undirected graphs, revisiting any node during DFS is expected and harmless"
  answer: 1
  explanation: "In undirected DFS, you track the parent of each node to distinguish tree edges from back edges. B is C's parent (the node DFS came from), so an edge back to B would not indicate a cycle. But A is C's grandparent — a visited node that is NOT C's parent — so the edge C–A is a back edge proving a cycle (A→B→C→A)."

- question: "In a directed graph, any edge leading from a gray node to a previously visited node is evidence of a cycle."
  type: true-false
  answer: false
  explanation: "Only an edge from a gray node to another gray node indicates a cycle. Gray means 'currently on the DFS recursion stack.' An edge from gray to black means the destination was fully explored in a previous DFS subtree — it is a forward or cross edge, not a back edge. Treating black nodes the same as gray nodes is a classic bug in directed cycle detection."

- question: "The two-state (visited/unvisited) DFS approach sufficient for undirected cycle detection works equally well for directed graphs."
  type: true-false
  answer: false
  explanation: "In a directed graph, a node can be visited (fully explored) without being on the current recursion stack. If you only track visited/unvisited, you will incorrectly flag cross edges (to finished nodes in other subtrees) as cycles. The three-color scheme — white/gray/black — distinguishes 'on the current path' (gray) from 'already finished' (black), which is essential for correctness in directed graphs."

- question: "Why does directed cycle detection require three vertex states (white, gray, black) rather than the two states (visited/unvisited) that suffice for undirected graphs?"
  type: short-answer
  answer: "In a directed graph, a 'visited' node might have been fully explored in a separate DFS subtree with no connection to the current path — reaching it does not indicate a cycle. The gray state specifically marks nodes currently on the recursion stack (the active DFS path). A cycle exists only when DFS finds an edge back to a gray node — meaning the current path loops back on itself. Without the gray/black distinction, you cannot tell whether a visited node is on the current path (a back edge, cycle) or was processed earlier (a cross/forward edge, no cycle)."
  explanation: "The three-color insight is that 'visited' conflates two different situations: currently being explored (on the stack) vs. already finished. Only the former is evidence of a cycle in a directed graph."
```

## Explainer

From your study of depth-first search, you know that DFS explores a graph by going as deep as possible before backtracking, and that the edges it encounters can be classified based on the DFS tree it builds. **Cycle detection** exploits this classification. The core insight is that a cycle exists if and only if DFS encounters an edge that points back to a node already on the current exploration path — a **back edge**. But the precise definition of "back edge" differs between undirected and directed graphs, and conflating the two is a common source of bugs.

In an **undirected graph**, every edge is traversed in both directions during DFS. When you visit node A and see neighbor B, you will later visit B and see A as a neighbor too. This means you must distinguish between "B is my parent in the DFS tree" (not a cycle) and "B is a visited node that is not my parent" (a cycle). The algorithm is straightforward: during DFS, if you encounter a neighbor that has already been visited and is not the node you came from, you have found a cycle. For example, in a triangle A-B-C-A, when DFS reaches C (having come from B) and sees A is already visited, that back edge reveals the cycle. No special node coloring is needed — a simple visited/unvisited flag plus parent tracking suffices.

**Directed graphs** are more subtle. Here, a visited node is not necessarily evidence of a cycle — it might have been fully explored in a previous DFS subtree that has no connection back to the current path. The solution is to track three states for each node: **white** (undiscovered), **gray** (discovered, currently being explored — on the recursion stack), and **black** (fully explored, all descendants processed). A back edge in a directed graph is specifically an edge from a gray node to another gray node — both are on the current DFS path, forming a cycle. An edge from a gray node to a black node is a **cross edge** or **forward edge**, not a cycle. This three-color scheme is what makes directed cycle detection work correctly.

These algorithms run in **O(V + E)** time, matching the cost of DFS itself, because cycle detection adds only constant work per edge. The applications are pervasive in computing. Package managers use cycle detection to verify that dependency graphs are acyclic (a cycle means "A requires B which requires A" — an unresolvable deadlock). Compilers check for circular dependencies between modules. Operating systems detect deadlocks by looking for cycles in resource allocation graphs. And **topological sorting** — which you will study next — is only possible on directed acyclic graphs (DAGs), so verifying the absence of cycles is a prerequisite for topological ordering.
