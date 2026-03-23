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
status: validated
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

## Questions

```yaml
- question: "You run DFS from vertex A in an undirected graph and visit vertices A, B, C, and D before the traversal terminates. You then discover vertex E exists but was not visited. What can you conclude?"
  type: multiple-choice
  options:
    - "The graph is disconnected — E belongs to a different connected component than A, B, C, D"
    - "There is a bug in the DFS implementation — a correct DFS always visits every vertex"
    - "E must be an isolated vertex with no edges"
    - "E is in the same component but the DFS chose a different path and missed it"
  answer: 0
  explanation: "DFS from a vertex visits every vertex reachable from it — by definition. If E was not visited, it is not reachable from A, which means there is no path from A to E. In an undirected graph, this means they belong to different connected components. Option C is wrong because E could have edges to vertices in its own separate component. Option D is impossible: DFS exhaustively explores all reachable vertices, so a reachable vertex cannot be missed."

- question: "What is the time complexity of finding all connected components in an undirected graph with V vertices and E edges using DFS?"
  type: multiple-choice
  options:
    - "O(V²) — each vertex may trigger a DFS that examines all other vertices"
    - "O(V · E) — each DFS pass examines all edges"
    - "O(V + E) — each vertex is visited exactly once and each edge is examined exactly once across all DFS calls"
    - "O(E log V) — sorting or priority structure is needed to track components"
  answer: 2
  explanation: "The algorithm iterates through all vertices and starts a DFS only from unvisited ones. Each vertex is visited exactly once total (the visited array prevents re-entry), and each edge is examined exactly once (or twice in undirected graphs, counted as O(E)). The total work across all DFS calls is therefore O(V + E), not the product of the number of calls times their individual costs. This is the same asymptotic cost as a single DFS traversal."

- question: "In a directed graph, the connected components found by repeatedly running DFS from unvisited vertices are equivalent to the strongly connected components of the graph."
  type: true-false
  answer: false
  explanation: "This confuses undirected connected components with directed strongly connected components (SCCs). In an undirected graph, reachability is symmetric: if you can reach B from A, you can reach A from B. In a directed graph, edges have directions — you might reach B from A without any path from B back to A. SCCs require a different algorithm (Tarjan's or Kosaraju's). Running naïve DFS on a directed graph and labeling everything visited from each start vertex gives weakly connected components, not SCCs."

- question: "After running the connected components algorithm, determining whether two specific vertices share a component can be answered in O(1) time."
  type: true-false
  answer: true
  explanation: "During the algorithm, each vertex is labeled with its component number (an integer). After the O(V + E) preprocessing pass, checking whether vertices u and v are in the same component reduces to comparing component[u] == component[v] — a constant-time array lookup. This is a key advantage of the labeling approach: amortize the O(V + E) cost once, then answer path-existence queries in O(1) each."

- question: "Explain why the connected components algorithm has O(V + E) time complexity even though it calls DFS multiple times — once for each component."
  type: short-answer
  answer: "The key is that the visited array is shared across all DFS calls and never reset. Each vertex is initialized as unvisited and marked visited exactly once — when it is first encountered in any DFS call. After that, it is never touched again. So the total work processing vertices across all calls sums to O(V). Similarly, each edge is examined a constant number of times total across all calls (at most twice for undirected graphs — once from each endpoint). The multiple DFS calls do not multiply the cost; they partition the work. The O(V + E) bound is the same as running a single full DFS traversal."
  explanation: "This is a general principle: an algorithm's complexity depends on total work done, not on the number of function calls. Because visited vertices are never re-processed, the calls cover disjoint subsets of the graph, and their costs add rather than multiply."
```

## Explainer

You know DFS as a graph traversal that starts at a vertex, goes as deep as possible along each branch before backtracking, and marks vertices as visited along the way. You also know how to represent graphs using adjacency lists or matrices. **Connected components** are what emerges when you ask a simple question: if I start DFS from a vertex, which vertices can I reach? The set of all vertices reachable from a given starting point (including the starting point itself) forms a connected component. Two vertices are in the same component if and only if there is a path between them.

The algorithm for finding all connected components in an undirected graph is remarkably simple. Maintain a "visited" array. Iterate through all vertices: when you encounter one that hasn't been visited, start a DFS (or BFS) from it. Every vertex that gets visited during that traversal belongs to the same component — label them all with the current component number. When the traversal finishes, move to the next unvisited vertex and start a new traversal with a new component label. When every vertex has been visited, you've identified every component. The total work is O(V + E) — each vertex is visited exactly once, and each edge is examined exactly once — because this is just DFS run to completion across the entire graph.

Think of it like exploring islands in an archipelago. You pick an unvisited island, explore every piece of land reachable by walking (following edges), and mark it all as "island 1." Then you jump to an unvisited island and do the same, calling it "island 2." The water between islands represents the absence of edges. When you're done, you know exactly how many islands there are and which landmasses belong to each. A graph with one component is called **connected** — every vertex can reach every other vertex. A graph with multiple components is **disconnected**, and no edge exists between vertices in different components.

Connected components have immediate practical applications. In a social network, components identify isolated communities with no connections between them. In image processing, component labeling identifies distinct objects in a binary image (each pixel is a vertex; edges connect adjacent pixels of the same color). In network reliability, checking whether removing a vertex or edge breaks a single component into two tells you whether that element is critical infrastructure — a concept formalized as **articulation points** and **bridges**, which build directly on component-finding. Understanding components also simplifies many graph problems: if a problem asks whether a path exists between two vertices, you only need to check whether they share a component, which is an O(1) lookup after a single O(V + E) preprocessing pass.
