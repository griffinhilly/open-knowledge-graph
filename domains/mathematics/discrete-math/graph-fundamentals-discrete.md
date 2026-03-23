---
id: graph-fundamentals-discrete
title: 'Graphs: Basic Concepts and Terminology'
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
builds-toward:
- connectivity-components-discrete
- graph-matrices-representations
tags:
- graphs
- vertices
- edges
- degree
- terminology
stage: formal-systems
status: validated
---

# Graphs: Basic Concepts and Terminology

## Core Idea
A graph G = (V, E) consists of vertices (nodes) and edges (connections). Edges can be directed or undirected, weighted or unweighted. Degree counts a vertex's incident edges; a path connects vertices via edges; a cycle closes back on itself.

## How It's Best Learned
Draw graphs and label vertices, edges, degrees. Practice building graphs from problem descriptions (networks, social links, puzzle states). Identify graph types: complete, bipartite, regular.

## Common Misconceptions
A simple graph has no loops (self-edges) or multi-edges; some definitions allow them. Directed graphs have in-degree and out-degree; undirected graphs have just degree.

## Questions

```yaml
- question: "An undirected graph has 5 vertices with degrees 2, 3, 3, 4, 4. How many edges does the graph have?"
  type: multiple-choice
  options:
    - "16 edges"
    - "8 edges"
    - "5 edges"
    - "14 edges"
  answer: 1
  explanation: "The handshaking lemma states that the sum of all vertex degrees equals 2|E|. Sum of degrees = 2 + 3 + 3 + 4 + 4 = 16. Therefore 2|E| = 16, so |E| = 8. Every edge contributes exactly 1 to each of its two endpoints' degree counts, so every edge is counted exactly twice in the total degree sum. The lemma also implies that the number of odd-degree vertices is always even — a useful constraint for checking whether a proposed degree sequence is realizable."

- question: "In a directed graph, vertex v has in-degree 3 and out-degree 2. How many edges are incident to v in total?"
  type: multiple-choice
  options:
    - "2 edges — only outgoing edges are 'incident' to a vertex in a directed graph"
    - "3 edges — only incoming edges count because v is a destination"
    - "5 edges — both incoming and outgoing edges are incident to v"
    - "6 edges — in-degree and out-degree are multiplied"
  answer: 2
  explanation: "In a directed graph, a vertex's total edge count is in-degree + out-degree. Vertex v has 3 incoming edges and 2 outgoing edges, for 5 total incident edges. This is different from an undirected graph, where 'degree' is a single number; directed graphs require two separate counts. Common mistakes include counting only one direction (options A and B) or confusing degree with some product."

- question: "In any undirected graph, the sum of all vertex degrees is always an even number."
  type: true-false
  answer: true
  explanation: "This is the handshaking lemma: the sum of all vertex degrees = 2|E|, which is always even. The reason is that each edge {u, v} contributes exactly 1 to u's degree and exactly 1 to v's degree — contributing exactly 2 to the total degree sum. Summing over all edges gives 2|E|. A useful corollary follows: every undirected graph has an even number of odd-degree vertices (since odd terms must pair up to give an even total). This rules out many seemingly-possible degree sequences before attempting to construct a graph."

- question: "A path in a graph is a sequence of vertices where consecutive vertices are connected by edges; a vertex may appear more than once as long as no edge is repeated."
  type: true-false
  answer: false
  explanation: "By standard definition, a path requires that no vertex repeats (which also prevents edge repetition). A sequence allowing vertex repetition but no edge repetition is called a *trail*; a sequence allowing both is a *walk*. The distinction matters: Eulerian path theorems concern trails (traverse every edge exactly once); Hamiltonian path problems concern paths (visit every vertex exactly once). Using 'path' loosely to mean 'walk' causes errors in applying graph theorems."

- question: "State the handshaking lemma and explain why it holds. What is one useful consequence of the lemma?"
  type: short-answer
  answer: "Handshaking lemma: in any undirected graph G = (V, E), the sum of all vertex degrees equals 2|E|. It holds because each edge {u, v} contributes exactly 1 to deg(u) and exactly 1 to deg(v), so it contributes exactly 2 to the total degree sum. Summing over all |E| edges gives 2|E|. One useful consequence: every graph has an even number of odd-degree vertices. Since the total degree sum is even (= 2|E|), and the contribution of even-degree vertices is already even, the odd-degree vertices must contribute an even sum — requiring an even count of them."
  explanation: "The 'even number of odd-degree vertices' consequence is frequently used to prove impossibility: if a proposed graph requires an odd number of vertices with odd degree, it cannot exist. It also underlies the Euler path/circuit theorem: an Euler circuit exists iff all vertices have even degree, and an Euler path (not circuit) exists iff exactly two vertices have odd degree — both conclusions flow directly from degree counting."
```

## Explainer

A **graph** G = (V, E) is the mathematical abstraction of a network. V is the set of **vertices** (the objects — cities, people, web pages, tasks) and E is the set of **edges** (the connections between them). What makes graphs so powerful is that they separate structure from content: the same mathematical object — a graph — can describe a road network, a social network, or a circuit, and any theorem about graphs applies to all of them.

**Degree** is the most basic measure of a vertex's connectivity. In an undirected graph, the degree of a vertex v is the number of edges incident to it — how many neighbors it has. In a directed graph, you need two numbers: **in-degree** (edges pointing into v) and **out-degree** (edges pointing out of v). A vertex's degree tells you something about its local role: high-degree vertices are hubs; degree-0 vertices (isolated vertices) are completely disconnected from the rest of the graph.

A **path** from vertex u to vertex v is a sequence of vertices where consecutive vertices are connected by edges, and no vertex repeats. A **cycle** is a path that starts and ends at the same vertex. The distinction matters throughout graph theory: trees are connected graphs with no cycles; acyclic graphs are fundamental to scheduling and dependency analysis. The **length** of a path is the number of edges it traverses, which becomes a natural distance metric between vertices.

Graph types refine the basic model to fit different situations. A **simple graph** has at most one edge between any two vertices and no self-loops — the "default" graph in most contexts. A **multigraph** allows multiple edges between the same pair of vertices (think multiple flight routes between two cities). A **directed graph** (digraph) replaces undirected edges with arrows, modeling asymmetric relationships like web links or one-way streets. A **weighted graph** assigns a numerical value to each edge, modeling costs, distances, or capacities. Identifying which type fits your problem is always the first step before applying any graph algorithm.

The handshaking lemma captures one of graph theory's elegant constraints: the sum of all vertex degrees equals twice the number of edges, because every edge contributes 1 to exactly two vertices' degrees. This simple fact rules out many seemingly-possible graphs before you even try to construct them. As you move toward connectivity, components, and matrix representations, these foundational definitions will become the shared vocabulary for every theorem and algorithm you encounter.
