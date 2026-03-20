---
id: connectivity-components-discrete
title: Connectivity and Connected Components
domain: mathematics
course: discrete-math
prerequisites:
- id: connected-components
  type: hard
- id: graph-fundamentals-discrete
  type: hard
builds-toward:
- trees-and-tree-properties
tags:
- connectivity
- components
- bridges
- articulation-points
stage: advanced
status: draft
---

# Connectivity and Connected Components

## Core Idea
A graph is connected if a path exists between any two vertices. Connected components partition vertices into maximal connected subgraphs. Bridges are edges whose removal increases the number of components; articulation points are vertices with this property.

## How It's Best Learned
Use depth-first search (DFS) or breadth-first search (BFS) to find connected components. Identify bridges and articulation points algorithmically. Recognize that a connected graph on n vertices has at least n−1 edges (a tree).

## Common Misconceptions
Being connected is not the same as being complete. A tree is minimally connected (n vertices, n−1 edges). A single isolated vertex is its own component.

## Explainer

From your work with graph fundamentals, you know that a graph is a collection of vertices and edges. Not every graph is "all in one piece." A graph is **connected** if you can travel between any two vertices by following edges — there is always a path. If some vertices are unreachable from others, the graph is disconnected, and it breaks into **connected components**: the maximal subsets of vertices that are mutually reachable. Every graph has at least one component; a single isolated vertex with no edges counts as its own component.

You already know how to traverse a graph using depth-first search (DFS) or breadth-first search (BFS). Finding connected components is a direct application: start DFS or BFS from any unvisited vertex, mark everything reachable as one component, then restart from the next unvisited vertex to find the next component. Repeat until all vertices are visited. The number of restarts plus one equals the number of components.

Within a connected graph, some structural elements are especially important. A **bridge** is an edge whose removal would disconnect the graph — it is a single point of failure for connectivity. Similarly, an **articulation point** (or **cut vertex**) is a vertex whose removal would increase the number of components. You can think of bridges and articulation points as the fragile connections in a network: they keep the graph together, but only barely. Identifying them is essential for network reliability analysis.

A key threshold to remember: a connected graph on n vertices has at least n−1 edges. Exactly n−1 edges with no cycles means the graph is a **tree** — the most minimal form of connectivity. Add any edge to a tree and you create a cycle; remove any edge and you disconnect it. Connectivity is therefore not about having many edges, but about whether the edges you have form a path between every pair of vertices.
