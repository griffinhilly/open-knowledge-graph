---
id: formal-definitions-graph-theory
title: Formal Definitions in Graph Theory
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
builds-toward:
- degree-sequences-erdos-gallai
- graph-operations-and-products
tags:
- graph-theory
- foundations
- definitions
stage: formal-systems
status: validated
---

# Formal Definitions in Graph Theory

## Core Idea
Graph theory formalizes the study of objects (vertices) and their pairwise relationships (edges). Directed and undirected graphs, simple graphs, multigraphs, and weighted graphs each have precise definitions capturing different relationship structures. Understanding these foundational distinctions is essential for all further work in graph theory.

## How It's Best Learned
Study simple examples (friendship networks, web links, transportation systems) and verify which definition each satisfies. Draw both small examples and counterexamples to reinforce why each definition excludes certain structures.

## Common Misconceptions
- Thinking all graphs must be simple graphs; multigraphs and directed graphs are equally fundamental.
- Confusing the direction of edges in directed graphs with temporal order.
- Believing that edge weights must always represent distance or cost.

## Questions

```yaml
- question: "An airline network has three direct flights between Chicago and New York operated by different carriers. Which graph model best captures this situation?"
  type: multiple-choice
  options:
    - "A simple graph, since Chicago and New York are distinct vertices"
    - "A directed graph, since flights operate in both directions"
    - "A multigraph, since multiple distinct edges between the same pair of vertices are needed"
    - "A weighted simple graph with the weight set to 3"
  answer: 2
  explanation: "A simple graph allows at most one edge between any pair of vertices, so it cannot represent three separate routes between the same two cities. A weighted graph with weight 3 captures total capacity but loses the identity of the individual routes. A multigraph is the right choice because it explicitly allows multiple edges between the same pair of vertices — each edge is a distinct connection with potentially different properties. The choice of definition directly determines which questions you can answer about the network."

- question: "In the formal definition of a simple graph G = (V, E), edges are unordered pairs of *distinct* vertices. Why does 'distinct' appear in the definition?"
  type: multiple-choice
  options:
    - "To prevent the graph from containing any cycles"
    - "To ensure every vertex has a unique label"
    - "To prohibit loops — edges from a vertex to itself"
    - "To guarantee the graph remains connected"
  answer: 2
  explanation: "The word 'distinct' excludes the case {v, v} — a vertex connected to itself (a loop). Simple graphs have no loops by definition. This matters because loop-free graphs have different properties: for example, every vertex's degree counts only edges to other vertices, not self-connections. Multigraphs can relax this constraint. The definition is precise because every excluded structure is excluded for a reason."

- question: "A theorem proven for simple graphs may not hold for multigraphs, because multigraphs permit structures that simple graphs explicitly exclude."
  type: true-false
  answer: true
  explanation: "This is precisely why formal definitions matter in mathematics. Theorems are proven for all objects satisfying a given definition. A result about simple graphs — which have no loops and at most one edge between any pair — may rely on these restrictions in its proof. Multigraphs relax those constraints, so the proof no longer applies. For example, theorems about Eulerian circuits behave differently in multigraphs than in simple graphs. Knowing which definition you're working with determines which results you can use."

- question: "In a directed graph, the edge (u, v) and the edge (v, u) represent the same connection viewed from opposite directions."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about directed graphs. Edges in a directed graph are ordered pairs, so (u, v) and (v, u) are entirely distinct edges — one goes from u to v, the other from v to u. A directed graph can contain both, one, or neither. This matters enormously: a web page can link to another without the other linking back; a road can be one-way; a dependency can be one-directional. Confusing directed edges with undirected ones would make it impossible to model asymmetric relationships."

- question: "Why does choosing between a simple graph, directed graph, multigraph, or weighted graph matter before solving a graph problem?"
  type: short-answer
  answer: "The definition specifies the model — it determines exactly which relationships can be represented and which questions can be asked. A shortest-path algorithm designed for weighted graphs has no meaning on an unweighted graph. A theorem about simple graphs may fail for multigraphs. A directed-graph reachability question ('Is there a path from u to v?') has a different answer than its undirected counterpart. Choosing the wrong model means your results don't apply to the actual problem you're solving."
  explanation: "Formal definitions in graph theory are not bureaucratic overhead — they are the specification of the object you're reasoning about. When you prove something about 'a graph,' you prove it about every graph satisfying the definition. Using the wrong definition means your conclusions may not transfer. In applied settings, the model choice shapes whether your answers are valid: modeling a one-way road network as an undirected graph would give incorrect routing results."
```

## Explainer

Graph theory's power comes from the precision of its definitions. An informal idea like "a network of connected things" is intuitive but imprecise — it doesn't tell you whether connections can be one-directional, whether two objects can have multiple distinct connections, or whether connections have strengths. The formal definitions fix all of these choices explicitly, and knowing which choice fits your problem is the first skill of applied graph theory.

The most fundamental object is a **simple graph**: a pair G = (V, E) where V is a finite set of vertices and E is a set of unordered pairs of distinct vertices. "Unordered" means edges are symmetric — if {u, v} ∈ E, then {v, u} is the same edge, not a separate one. "Distinct" means no vertex is connected to itself (no **loops**). "Set of pairs" means at most one edge between any two vertices. A simple graph captures symmetric, binary relationships between distinct objects — friendship, adjacency on a map, or reachability in a maze.

Relaxing the constraints yields richer models. A **multigraph** allows multiple edges between the same pair of vertices — useful when two cities have multiple direct flight routes, or two circuits have multiple parallel wires. A **directed graph** (or **digraph**) replaces unordered pairs with ordered pairs: edge (u, v) goes from u to v, but (v, u) is a separate edge in the other direction. Directed graphs model asymmetric relationships — web links (a page links to another, not necessarily vice versa), dependencies (A requires B, but B does not require A), or one-way streets. A **weighted graph** assigns a real number to each edge; this weight can represent distance, cost, capacity, probability, or any other quantity that characterizes the connection.

Each definition is a deliberate choice that shapes what questions you can ask. In a simple graph, you can ask "Is there a path from u to v?" In a weighted graph, you can ask "What is the shortest-weight path?" In a directed graph, you can ask "Is there a directed path from u to v?" — a question with a different answer than "from v to u?" The formal definition is not bureaucracy; it is the specification of the model. A theorem proven for simple graphs may fail for multigraphs, and a shortest-path algorithm designed for weighted graphs has no meaning on unweighted ones.

Getting comfortable with formal definitions in graph theory is preparation for rigorous mathematical argument. When you prove a theorem about graphs, you prove it about every graph satisfying the definition — not just the specific example you drew. That universality is what makes the definitions valuable. As you move to degree sequences, graph products, and structural theorems, these definitions will be the shared foundation that lets you apply general results to specific cases confidently.
