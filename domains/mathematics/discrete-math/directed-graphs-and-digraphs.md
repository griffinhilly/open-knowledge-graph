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

## Questions

```yaml
- question: "In a directed graph modeling web hyperlinks, page A links to page B, and page B links to page C. Can page C reach page A by following links?"
  type: multiple-choice
  options:
    - "Yes — since A, B, and C are all connected, the graph is connected and any page can reach any other"
    - "Not necessarily — directed edges are one-way, and reachability from C to A depends on whether a directed path back to A exists"
    - "Yes — in any connected graph, every vertex can reach every other vertex"
    - "No — once you reach a page with no outgoing links you cannot continue, so backward traversal is impossible"
  answer: 1
  explanation: "Direction creates asymmetric reachability — the existence of a directed path from A to C does not guarantee any path from C back to A. The web link graph is a classic example: following hyperlinks is strictly one-directional. This is the fundamental departure from undirected graphs, where connectivity is symmetric. A digraph can be 'weakly connected' (undirected version is connected) without being 'strongly connected' (every vertex reachable from every other)."

- question: "A vertex in a digraph has in-degree 0 and positive out-degree. This vertex is called a source. Which best describes its role?"
  type: multiple-choice
  options:
    - "It receives information from all other vertices but produces none"
    - "It produces information or flow that others receive, but nothing points into it from other vertices"
    - "It is an isolated vertex with no connections in either direction"
    - "It has equal in-degree and out-degree, making it balanced"
  answer: 1
  explanation: "A source has no incoming arcs (in-degree 0) and at least one outgoing arc. Nothing feeds into it — it originates flow. In a software dependency graph, a source package has no dependencies of its own. In a web graph, a source page is never linked to by other pages. This is the directed analogue of an isolated node only in one direction — it participates in the graph actively as an originator, not passively as a receiver."

- question: "A directed graph can be weakly connected without being strongly connected — treating all edges as undirected yields a connected graph, but directed paths between some pairs of vertices may not exist in both directions."
  type: true-false
  answer: true
  explanation: "Weak connectivity only requires that the underlying undirected graph (ignoring arrows) is connected. Strong connectivity requires that every vertex can reach every other vertex by following directed paths. A simple counterexample: A → B → C is weakly connected (A, B, C are all linked) but not strongly connected (C cannot reach A or B following directed paths). Most real directed graphs — web links, citation networks, dependency graphs — are weakly but not strongly connected."

- question: "In a directed graph, if vertex B is reachable from vertex A via a directed path, then vertex A is necessarily reachable from vertex B via a directed path."
  type: true-false
  answer: false
  explanation: "This is the key conceptual error when transitioning from undirected to directed graphs. In undirected graphs, connectivity is symmetric. In directed graphs, reachability is asymmetric — following arrows forward may take you somewhere you cannot return from. B reachable from A means there exists a sequence of arcs pointing in the forward direction from A to B; there may be no path back. This asymmetry is exactly why one-way streets, hyperlinks, and dependency graphs require digraphs to model accurately."

- question: "What is the difference between weak connectivity and strong connectivity in a directed graph, and why does the distinction matter in practice?"
  type: short-answer
  answer: "A digraph is weakly connected if ignoring edge directions leaves a connected undirected graph — all vertices are linked, but directional reachability may be one-way. It is strongly connected if every vertex can reach every other vertex by following directed paths. The distinction matters because many algorithms and real-world properties depend on which type applies. Topological sorting, for example, is only possible in directed acyclic graphs (which are not strongly connected). Strongly connected components partition a digraph into the maximal subsets within which every vertex is mutually reachable, which is essential for analyzing dependency cycles, finding feedback loops in systems, and determining which nodes in a web graph can be reached from each other."
  explanation: "The directed analogue of the handshaking lemma — sum of in-degrees equals sum of out-degrees equals number of arcs — also reflects this structure. Identifying strongly connected components is a fundamental algorithmic problem solved by Kosaraju's or Tarjan's algorithm, both of which build on depth-first search."
```

## Explainer

In an undirected graph, an edge between vertices A and B means you can travel freely in either direction. A **directed graph** (or **digraph**) breaks this symmetry: each edge is an **arc** with a specific tail (where it starts) and a **head** (where it points). The arc from A to B is a completely different object from the arc from B to A — and the graph may have one, both, or neither. This small change — adding arrows — dramatically changes the questions you can ask and the answers you get.

The most important new concept is **reachability**. In a digraph, vertex B is reachable from A if there exists a directed path following arcs in their forward direction. Even if A and B are connected by arcs, B might be reachable from A while A is not reachable from B. Think of a one-way street network: you can reach the highway from your house via certain routes, but returning home may require a completely different sequence of streets. This asymmetric reachability is the heart of why digraphs model so many real systems — web hyperlinks, program control flow, dependency trees, and tournament rankings all have this one-way character.

From your prerequisite knowledge of undirected graphs, you know that **connectivity** tells you whether any two vertices can communicate. Digraphs split this into two levels. A digraph is **weakly connected** if the underlying undirected graph (ignoring arrow directions) is connected — the vertices are linked, but not necessarily reachable from each other. It is **strongly connected** if every vertex is reachable from every other vertex following directed paths. A directed cycle — a path that returns to its starting vertex following arrows — is only possible in a strongly connected component. Detecting these components is a major algorithmic task that builds directly on your graph traversal skills.

**In-degree** and **out-degree** replace the single degree concept you know from undirected graphs. A vertex's in-degree counts arrows pointing into it; its out-degree counts arrows leaving it. A vertex with out-degree zero is a **sink** — information or flow ends there. A vertex with in-degree zero is a **source** — it produces but never receives. These roles are critical in applications: in a dependency graph, sources are packages with no dependencies; sinks are packages nothing depends on. In a web crawl, a page with no outgoing links is a sink. The sum of all in-degrees equals the sum of all out-degrees (both equal the number of arcs), which is the directed analogue of the handshaking lemma you know from undirected graphs.
