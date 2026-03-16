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

## Explainer

Think of dropping a stone into a pond and watching ripples spread outward. The first ripple ring contains all points one step from the center; the second ring contains all points two steps away; and so on. Breadth-first search works exactly like this. Starting from a **source vertex**, BFS visits every neighbor at distance 1 before visiting any vertex at distance 2. This "wave" property is not an accident — it is enforced by the data structure BFS uses.

The key data structure is a **queue** (first-in, first-out). You enqueue the source vertex and mark it as visited. Then you repeatedly dequeue the front vertex, examine all its unvisited neighbors, mark them visited, and enqueue them. Because you always process vertices in the order they were discovered, vertices at distance 1 are always fully processed before any vertex at distance 2 is dequeued. This is why BFS finds **shortest paths** in unweighted graphs: the first time you reach a vertex is guaranteed to be via the fewest edges possible.

The runtime is O(V+E). You visit each vertex once (O(V)) and, for each vertex, you inspect each of its edges once (O(E) total across all vertices). This efficiency depends on the visited-marking step — without it, you could revisit vertices indefinitely in a graph with cycles. Your prerequisite knowledge of graph theory (vertices, edges, adjacency) gives you the vocabulary; Big-O notation lets you reason about why O(V+E) is nearly as fast as reading the graph itself.

A useful concrete example: in a social network graph where edges represent friendships, BFS from your profile finds all your friends first, then friends-of-friends, then third-degree connections. The **BFS tree** — the spanning tree formed by the edges used to first discover each vertex — records the shortest-path structure. Every vertex's depth in the BFS tree equals its shortest-path distance from the source. This tree is the foundation for the next topic: shortest-path algorithms on unweighted graphs.
