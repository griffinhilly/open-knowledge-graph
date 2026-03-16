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
status: draft
---

# Graphs: Basic Concepts and Terminology

## Core Idea
A graph G = (V, E) consists of vertices (nodes) and edges (connections). Edges can be directed or undirected, weighted or unweighted. Degree counts a vertex's incident edges; a path connects vertices via edges; a cycle closes back on itself.

## How It's Best Learned
Draw graphs and label vertices, edges, degrees. Practice building graphs from problem descriptions (networks, social links, puzzle states). Identify graph types: complete, bipartite, regular.

## Common Misconceptions
A simple graph has no loops (self-edges) or multi-edges; some definitions allow them. Directed graphs have in-degree and out-degree; undirected graphs have just degree.

## Explainer

A **graph** G = (V, E) is the mathematical abstraction of a network. V is the set of **vertices** (the objects — cities, people, web pages, tasks) and E is the set of **edges** (the connections between them). What makes graphs so powerful is that they separate structure from content: the same mathematical object — a graph — can describe a road network, a social network, or a circuit, and any theorem about graphs applies to all of them.

**Degree** is the most basic measure of a vertex's connectivity. In an undirected graph, the degree of a vertex v is the number of edges incident to it — how many neighbors it has. In a directed graph, you need two numbers: **in-degree** (edges pointing into v) and **out-degree** (edges pointing out of v). A vertex's degree tells you something about its local role: high-degree vertices are hubs; degree-0 vertices (isolated vertices) are completely disconnected from the rest of the graph.

A **path** from vertex u to vertex v is a sequence of vertices where consecutive vertices are connected by edges, and no vertex repeats. A **cycle** is a path that starts and ends at the same vertex. The distinction matters throughout graph theory: trees are connected graphs with no cycles; acyclic graphs are fundamental to scheduling and dependency analysis. The **length** of a path is the number of edges it traverses, which becomes a natural distance metric between vertices.

Graph types refine the basic model to fit different situations. A **simple graph** has at most one edge between any two vertices and no self-loops — the "default" graph in most contexts. A **multigraph** allows multiple edges between the same pair of vertices (think multiple flight routes between two cities). A **directed graph** (digraph) replaces undirected edges with arrows, modeling asymmetric relationships like web links or one-way streets. A **weighted graph** assigns a numerical value to each edge, modeling costs, distances, or capacities. Identifying which type fits your problem is always the first step before applying any graph algorithm.

The handshaking lemma captures one of graph theory's elegant constraints: the sum of all vertex degrees equals twice the number of edges, because every edge contributes 1 to exactly two vertices' degrees. This simple fact rules out many seemingly-possible graphs before you even try to construct them. As you move toward connectivity, components, and matrix representations, these foundational definitions will become the shared vocabulary for every theorem and algorithm you encounter.
