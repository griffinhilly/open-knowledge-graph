---
id: graph-theory-fundamentals
title: 'Graph Theory: Vertices, Edges, and Basic Definitions'
domain: mathematics
course: discrete-math
prerequisites: []
builds-toward:
- graph-representation
- degree-sequences-graphs
tags:
- graph-theory
- fundamentals
stage: formal-systems
status: validated
---

# Graph Theory: Vertices, Edges, and Basic Definitions

## Core Idea
A graph G = (V, E) consists of a set of vertices V and a set of edges E. Edges can be directed (arcs) or undirected, and weighted or unweighted. Graphs model relationships, networks, and dependencies across many domains. Complete graphs Kₙ, empty graphs, and special structures like cycles and paths are fundamental examples.

## Questions

```yaml
- question: "A complete graph Kₙ has an edge between every pair of distinct vertices. How many edges does K₅ have?"
  type: multiple-choice
  options: ["5", "10", "15", "20"]
  answer: 1
  explanation: "Kₙ has n(n−1)/2 edges — one for each pair of distinct vertices. For n = 5: 5×4/2 = 10. This equals C(5,2), the number of ways to choose 2 items from 5, which makes sense since each edge corresponds to a unique 2-vertex subset."

- question: "A graph must have at least one edge — a graph with vertices but no edges is not a valid graph."
  type: true-false
  answer: false
  explanation: "An empty (edgeless) graph, with any number of vertices and E = ∅, is perfectly valid. G = (V, E) only requires V to be nonempty; the edge set can be empty. Empty graphs appear regularly as boundary cases in proofs and as base cases in inductive arguments."

- question: "What is the difference between a directed graph and an undirected graph, and give an example of a real-world relationship that each models more accurately?"
  type: short-answer
  answer: "In a directed graph, each edge (arc) has a specific direction, representing an asymmetric relationship. In an undirected graph, edges are bidirectional, representing symmetric relationships. Example: 'follows' on social media is directed (A follows B does not imply B follows A); 'is friends with' is undirected (friendship is mutual)."
  explanation: "Choosing directed vs. undirected is a modeling decision based on whether the relationship is inherently symmetric. Using an undirected graph to model a one-way relationship loses information; using a directed graph for a symmetric one adds unnecessary complexity."
```

## Explainer

Graph theory provides a language for modeling relationships. Wherever you have objects and connections between them — cities and roads, websites and hyperlinks, people and friendships, tasks and dependencies — a graph is the natural mathematical structure. The same abstraction applies across computer science, biology, social science, logistics, and linguistics, which is why graph theory is worth learning as its own subject rather than just a tool within any one domain.

A graph G = (V, E) is formally a set of vertices V (also called nodes or points) and a set of edges E connecting pairs of vertices. The notation is deliberately abstract. An undirected graph has edges without direction: if u and v are connected, you can traverse the edge either way. A directed graph (digraph) has arcs with a specified direction: an arc u→v permits travel from u to v, but not necessarily the reverse. A weighted graph assigns numerical values to edges — a road network might weight edges by distance or travel time. These choices are modeling decisions: you pick the variant that captures what matters in your domain.

Some graph families appear so often they have standard names. A complete graph Kₙ connects every pair of distinct vertices — the densest possible simple graph, with n(n−1)/2 edges. A path is a sequence of distinct vertices where each is connected to the next. A cycle is a closed path — it starts and ends at the same vertex. A tree is a connected graph with no cycles; a tree on n vertices has exactly n−1 edges. An empty graph has vertices but no edges at all. Getting fluent at recognizing these structures is the first step in graph-theoretic reasoning, because most theorems and algorithms are stated in terms of them.

The power of graph theory is that once you express a problem as a graph, the entire toolkit of graph algorithms becomes applicable. Is there a route between any two points in a network? That is a connectivity question, answered by depth-first or breadth-first search. Can you traverse every edge exactly once? That is an Euler path question. What is the fastest route from A to B? That is a shortest-path question, answered by Dijkstra's algorithm. Can you color regions of a map so no two adjacent regions share a color? That is a graph coloring question. The definitions in this topic — vertices, edges, directed vs. undirected, complete, cycle, path, empty — are the vocabulary that makes all of those questions precisely statable and solvable.
