---
id: graph-connectivity
title: Graph Paths, Cycles, and Connectivity
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: mathematical-induction
  type: soft
- id: graph-representation
  type: soft
builds-toward:
- bipartite-graphs
- trees-in-graph-theory
- euler-circuits-and-paths
- hamiltonian-circuits
- planar-graphs
- graph-coloring
tags:
- paths
- cycles
- connectivity
- connected-components
- graph-theory
stage: formal-systems
status: validated
---
# Graph Paths, Cycles, and Connectivity

## Core Idea
A path is a sequence of distinct vertices where consecutive vertices are connected by edges. A cycle is a closed path where the first and last vertices are the same. A graph is connected if there is a path between every pair of vertices; otherwise it consists of multiple disconnected components. The distinction between walks (vertices may repeat), trails (edges do not repeat), and paths (vertices do not repeat) is essential. Connectivity is the foundational structural property for almost all graph-theoretic results.

## How It's Best Learned
Practice finding paths and cycles in small graphs by hand, writing out vertex sequences explicitly. Test connectivity by trying to reach every vertex from a fixed start. Deliberately construct examples that distinguish walks from trails from paths.

## Common Misconceptions
- Confusing walks, trails, and paths — these are distinct notions and the differences matter for theorems.
- Assuming a connected graph has a unique path between any two vertices — only trees have this property.
- Thinking 'no isolated vertices' implies connectivity.

## Questions

```yaml
- question: "Which of the following vertex sequences is a valid path (not just a walk or trail)?"
  type: multiple-choice
  options:
    - "A → B → A → C → D"
    - "A → B → C → B → D"
    - "A → C → B → D"
    - "A → B → B → D"
  answer: 2
  explanation: "A path requires all vertices to be distinct. 'A → C → B → D' visits four distinct vertices in sequence — it is a valid path if those edges exist. Option 0 repeats A; option 1 repeats B; option 3 repeats B immediately (an edge from a vertex to itself would be a loop, not a simple edge). Sequences that repeat vertices are walks or trails, not paths."

- question: "If every vertex in a graph has at least one edge (no isolated vertices), then the graph must be connected."
  type: true-false
  answer: false
  explanation: "Having no isolated vertices means every vertex has degree ≥ 1, but that does not guarantee a path between every pair of vertices. For example, the graph {A,B,C,D} with only edges A-B and C-D has no isolated vertices, yet A cannot reach C or D. The graph has two disconnected components. Connectivity is a global property requiring reachability between all vertex pairs, not just local degree conditions."

- question: "Explain the difference between a walk, a trail, and a path. Why do these distinctions matter for graph theory theorems?"
  type: short-answer
  answer: "A walk allows repeated vertices and edges. A trail forbids repeated edges but allows repeated vertices. A path forbids repeated vertices (which also prevents repeated edges). The distinctions matter because theorems are stated in terms of specific types: Euler circuits concern trails (traverse every edge exactly once), Hamiltonian cycles concern paths (visit every vertex exactly once). Using the wrong term leads to applying the wrong theorem."
  explanation: "These are not just terminological nitpicking. An Euler circuit exists iff every vertex has even degree — this is a statement about trails (edge-repetition forbidden), not arbitrary walks. A Hamiltonian cycle is NP-hard to detect in general — this is about paths (vertex-repetition forbidden). The level of restriction changes both the mathematical content and the computational difficulty."
```

## Explainer

From your introduction to graphs, you know that a graph is a set of vertices and a set of edges connecting pairs of vertices. Now the natural question is: given two vertices, is there a way to travel from one to the other along edges? And if so, what kind of route is it? These questions lead to the core vocabulary of paths, cycles, and connectivity.

The vocabulary for routes through a graph comes in three levels of precision, and keeping them distinct is essential. A **walk** is completely permissive: you follow edges in sequence, and you may revisit any vertex or edge as many times as you like. A **trail** adds one restriction: you may not reuse any edge, though you may revisit vertices. A **path** is the most restrictive: you may not revisit any vertex, which automatically prevents reusing any edge. In formal notation, a path from u to v is a sequence u = v₀, v₁, ..., vₖ = v where all the vᵢ are distinct and each consecutive pair is connected by an edge.

A graph is **connected** if a path exists between every pair of vertices. If the graph is not connected, it decomposes into **connected components** — maximal subgraphs that are internally connected but have no edges between them. Checking connectivity from a given vertex can be done by a depth-first or breadth-first search: start at the vertex, follow edges to unvisited neighbors, repeat. If you reach every vertex, the graph is connected; if some vertices remain unreachable, they form separate components.

A very common misconception is that "no isolated vertices" implies connectivity. It does not. Isolated vertices have degree 0; removing them from the hypothesis still leaves graphs that are disconnected into multiple components, each of which has all its vertices connected to at least one other vertex within the component. Connectivity is a global property of the whole graph, not a local property of each vertex's neighborhood.

**Cycles** — closed paths where the first and last vertex coincide and all intermediate vertices are distinct — capture the idea of a loop in a graph. Cycles are central to almost every advanced graph theorem you will study next: trees are characterized as connected acyclic graphs, Euler circuits require every vertex to have even degree, and planarity is tied to the structure of cycles through Kuratowski's theorem. Keeping walks, trails, and paths precisely defined now will prevent errors when these theorems state exactly which type of route they are about.
