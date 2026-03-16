---
id: graph-connectivity-components-dfs
title: 'Graph Connectivity: Finding Connected Components'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: graph-adjacency-representation-analysis
  type: hard
builds-toward:
- strongly-connected-components-algorithms
- articulation-points-cut-vertices
tags:
- graphs
- connectivity
- components
- dfs
stage: formal-systems
status: draft
---

# Graph Connectivity: Finding Connected Components

## Core Idea
A connected component is a maximal set of vertices reachable from each other. DFS or BFS starting from an unvisited vertex marks all vertices in its component. Running this repeatedly identifies all components in O(V+E) time.

## How It's Best Learned
Implement DFS-based component finding. Verify on graphs with known component structure. Use components to solve applications like detecting if a graph is connected or merging two graphs safely.

## Common Misconceptions
- Confusing connected components (undirected) with strongly connected components (directed).
- Thinking component finding requires special algorithms; it's a straightforward DFS/BFS application.
- Not recognizing components are useful for partitioning large graphs and understanding structure.

## Explainer

You know DFS as a graph traversal that starts at a vertex, goes as deep as possible along each branch before backtracking, and marks vertices as visited along the way. You also know how to represent graphs using adjacency lists or matrices. **Connected components** are what emerges when you ask a simple question: if I start DFS from a vertex, which vertices can I reach? The set of all vertices reachable from a given starting point (including the starting point itself) forms a connected component. Two vertices are in the same component if and only if there is a path between them.

The algorithm for finding all connected components in an undirected graph is remarkably simple. Maintain a "visited" array. Iterate through all vertices: when you encounter one that hasn't been visited, start a DFS (or BFS) from it. Every vertex that gets visited during that traversal belongs to the same component — label them all with the current component number. When the traversal finishes, move to the next unvisited vertex and start a new traversal with a new component label. When every vertex has been visited, you've identified every component. The total work is O(V + E) — each vertex is visited exactly once, and each edge is examined exactly once — because this is just DFS run to completion across the entire graph.

Think of it like exploring islands in an archipelago. You pick an unvisited island, explore every piece of land reachable by walking (following edges), and mark it all as "island 1." Then you jump to an unvisited island and do the same, calling it "island 2." The water between islands represents the absence of edges. When you're done, you know exactly how many islands there are and which landmasses belong to each. A graph with one component is called **connected** — every vertex can reach every other vertex. A graph with multiple components is **disconnected**, and no edge exists between vertices in different components.

Connected components have immediate practical applications. In a social network, components identify isolated communities with no connections between them. In image processing, component labeling identifies distinct objects in a binary image (each pixel is a vertex; edges connect adjacent pixels of the same color). In network reliability, checking whether removing a vertex or edge breaks a single component into two tells you whether that element is critical infrastructure — a concept formalized as **articulation points** and **bridges**, which build directly on component-finding. Understanding components also simplifies many graph problems: if a problem asks whether a path exists between two vertices, you only need to check whether they share a component, which is an O(1) lookup after a single O(V + E) preprocessing pass.
