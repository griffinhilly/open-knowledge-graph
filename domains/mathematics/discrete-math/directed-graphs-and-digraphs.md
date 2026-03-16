---
id: directed-graphs-and-digraphs
title: Directed Graphs and Digraphs
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
builds-toward:
- strongly-connected-components
- topological-sorting
- cycle-detection-directed-graphs
tags:
- graph-theory
- directed-graphs
- digraphs
stage: formal-systems
status: draft
---

# Directed Graphs and Digraphs

## Core Idea
Directed graphs (digraphs) extend graph theory by adding direction to edges. Each edge points from one vertex to another, creating paths and cycles with directionality. They model relationships where direction matters: web links, tournament results, and state transitions.

## How It's Best Learned
Draw digraphs with arrows showing direction. Trace paths following arrow directions. Compare directed vs. undirected versions of the same graph to see how direction changes properties like connectivity.

## Common Misconceptions
- Assuming an undirected edge is bidirectional in a digraph. - Overlooking that cycles are harder to define in directed graphs due to the direction constraint.

## Explainer

In an undirected graph, an edge between vertices A and B means you can travel freely in either direction. A **directed graph** (or **digraph**) breaks this symmetry: each edge is an **arc** with a specific tail (where it starts) and a **head** (where it points). The arc from A to B is a completely different object from the arc from B to A — and the graph may have one, both, or neither. This small change — adding arrows — dramatically changes the questions you can ask and the answers you get.

The most important new concept is **reachability**. In a digraph, vertex B is reachable from A if there exists a directed path following arcs in their forward direction. Even if A and B are connected by arcs, B might be reachable from A while A is not reachable from B. Think of a one-way street network: you can reach the highway from your house via certain routes, but returning home may require a completely different sequence of streets. This asymmetric reachability is the heart of why digraphs model so many real systems — web hyperlinks, program control flow, dependency trees, and tournament rankings all have this one-way character.

From your prerequisite knowledge of undirected graphs, you know that **connectivity** tells you whether any two vertices can communicate. Digraphs split this into two levels. A digraph is **weakly connected** if the underlying undirected graph (ignoring arrow directions) is connected — the vertices are linked, but not necessarily reachable from each other. It is **strongly connected** if every vertex is reachable from every other vertex following directed paths. A directed cycle — a path that returns to its starting vertex following arrows — is only possible in a strongly connected component. Detecting these components is a major algorithmic task that builds directly on your graph traversal skills.

**In-degree** and **out-degree** replace the single degree concept you know from undirected graphs. A vertex's in-degree counts arrows pointing into it; its out-degree counts arrows leaving it. A vertex with out-degree zero is a **sink** — information or flow ends there. A vertex with in-degree zero is a **source** — it produces but never receives. These roles are critical in applications: in a dependency graph, sources are packages with no dependencies; sinks are packages nothing depends on. In a web crawl, a page with no outgoing links is a sink. The sum of all in-degrees equals the sum of all out-degrees (both equal the number of arcs), which is the directed analogue of the handshaking lemma you know from undirected graphs.
