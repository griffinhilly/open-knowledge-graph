---
id: breadth-first-search-graphs
title: Breadth-First Search (BFS)
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: big-o-notation
  type: soft
builds-toward:
- shortest-paths-unweighted-graphs
tags:
- graph-algorithms
- traversal
- bfs
stage: formal-systems
status: draft
---

# Breadth-First Search (BFS)

## Core Idea
Breadth-first search systematically explores a graph level by level, visiting all neighbors of a vertex before moving deeper. BFS uses a queue to process vertices, runs in O(V+E) time, and finds shortest paths in unweighted graphs.

## Questions

```yaml
- question: "You run BFS on an unweighted graph from source vertex A. Vertex B is discovered when it is first dequeued at level 4. Can BFS later find a shorter path from A to B?"
  type: multiple-choice
  options:
    - "Yes — BFS might find a shorter path later if it hasn't explored all vertices yet"
    - "No — BFS guarantees that the first time a vertex is discovered, it is via the shortest path"
    - "Yes — BFS only guarantees shortest paths in trees, not graphs with cycles"
    - "It depends on whether the graph is directed or undirected"
  answer: 1
  explanation: "BFS explores vertices level by level: all vertices at distance 1 before distance 2, and so on. This is enforced by the FIFO queue — vertices are processed in the order they were first discovered. The first time vertex B is reached, it must have been discovered from a level-3 vertex, meaning B is at distance 4 from A. Any shorter path would have reached B at an earlier level, but BFS would have discovered B then instead. Therefore, first discovery is always via the shortest path in unweighted graphs. This guarantee holds regardless of whether the graph has cycles."

- question: "You modify BFS to use a stack instead of a queue. What algorithm does this produce, and does it still find shortest paths?"
  type: multiple-choice
  options:
    - "Dijkstra's algorithm — it finds shortest paths in weighted graphs"
    - "Topological sort — it still finds shortest paths but in topological order"
    - "Depth-first search (DFS) — it does not guarantee shortest paths"
    - "A faster variant of BFS that still guarantees shortest paths"
  answer: 2
  explanation: "Replacing the FIFO queue with a LIFO stack transforms BFS into depth-first search (DFS). A stack causes the algorithm to always continue from the most recently discovered vertex, diving deep along one path before backtracking — the opposite of BFS's level-by-level expansion. DFS does NOT guarantee shortest paths; it finds *some* path to each vertex, not necessarily the shortest. The data structure is not an implementation detail — it is what determines whether the algorithm finds shortest paths at all."

- question: "BFS visits all vertices at distance k from the source before visiting any vertex at distance k+1."
  type: true-false
  answer: true
  explanation: "This is the defining 'wavefront' property of BFS, enforced by the FIFO queue. When a distance-k vertex is processed, its unvisited neighbors (at distance k+1) are enqueued *after* any distance-k vertices already in the queue. Therefore, all distance-k vertices are fully dequeued and processed before any distance-(k+1) vertex is reached. This level-by-level expansion is exactly why BFS finds shortest paths: each wave of exploration travels exactly one step further than the previous wave."

- question: "Without the visited-marking step, BFS on a graph with cycles would eventually terminate because vertices would stop being enqueued once all paths are explored."
  type: true-false
  answer: false
  explanation: "Without visited marking, BFS on a cyclic graph loops indefinitely. In a cycle A−B−C−A: processing A enqueues B and C; processing B re-enqueues A (not yet marked visited from B's view); processing the re-enqueued A enqueues B and C again — and the queue never empties. Visited marking prevents a vertex from being enqueued more than once, ensuring each vertex is processed exactly once. Without it, BFS neither terminates nor finds shortest paths correctly. The visited flag is what gives BFS its O(V+E) runtime guarantee."

- question: "Why does BFS guarantee finding the shortest path in an unweighted graph, while depth-first search (DFS) does not?"
  type: short-answer
  answer: "BFS uses a FIFO queue, which enforces processing vertices in non-decreasing order of their distance from the source. The first time BFS reaches a vertex, it has traveled the minimum possible number of edges. DFS uses a stack (or recursion) that dives as deep as possible along one path before backtracking — it may traverse 5 edges to reach a vertex that is only 2 edges from the source via a different path. DFS finds *a* path to each vertex, not the *shortest* path. The data structure controls the exploration order, and exploration order is what determines whether shortest paths are guaranteed."
  explanation: "The intuition is the ripple analogy: BFS expands uniformly in all directions, so it reaches each vertex at its true minimum distance before any longer path could arrive. DFS is like following one hallway to its dead end before checking adjacent ones — the first path found may be far longer than the shortest. For unweighted graphs, BFS's level-by-level expansion is both necessary and sufficient for shortest paths. For weighted graphs, Dijkstra's algorithm generalizes this using a priority queue to always process the cheapest unvisited vertex first."
```

## Explainer

Think of dropping a stone into a pond and watching ripples spread outward. The first ripple ring contains all points one step from the center; the second ring contains all points two steps away; and so on. Breadth-first search works exactly like this. Starting from a **source vertex**, BFS visits every neighbor at distance 1 before visiting any vertex at distance 2. This "wave" property is not an accident — it is enforced by the data structure BFS uses.

The key data structure is a **queue** (first-in, first-out). You enqueue the source vertex and mark it as visited. Then you repeatedly dequeue the front vertex, examine all its unvisited neighbors, mark them visited, and enqueue them. Because you always process vertices in the order they were discovered, vertices at distance 1 are always fully processed before any vertex at distance 2 is dequeued. This is why BFS finds **shortest paths** in unweighted graphs: the first time you reach a vertex is guaranteed to be via the fewest edges possible.

The runtime is O(V+E). You visit each vertex once (O(V)) and, for each vertex, you inspect each of its edges once (O(E) total across all vertices). This efficiency depends on the visited-marking step — without it, you could revisit vertices indefinitely in a graph with cycles. Your prerequisite knowledge of graph theory (vertices, edges, adjacency) gives you the vocabulary; Big-O notation lets you reason about why O(V+E) is nearly as fast as reading the graph itself.

A useful concrete example: in a social network graph where edges represent friendships, BFS from your profile finds all your friends first, then friends-of-friends, then third-degree connections. The **BFS tree** — the spanning tree formed by the edges used to first discover each vertex — records the shortest-path structure. Every vertex's depth in the BFS tree equals its shortest-path distance from the source. This tree is the foundation for the next topic: shortest-path algorithms on unweighted graphs.
