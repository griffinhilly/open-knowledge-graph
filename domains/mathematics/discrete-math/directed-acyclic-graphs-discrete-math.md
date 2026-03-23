---
id: directed-acyclic-graphs-discrete-math
title: Directed Acyclic Graphs (DAGs)
domain: mathematics
course: discrete-math
prerequisites:
- id: directed-graphs-and-digraphs
  type: hard
- id: cycle-detection-directed-graphs
  type: soft
builds-toward:
- topological-sorting
tags:
- directed-graphs
- acyclic
- dags
stage: formal-systems
status: validated
---

# Directed Acyclic Graphs (DAGs)

## Core Idea
A directed acyclic graph (DAG) is a digraph with no directed cycles. DAGs are fundamental in computer science for modeling dependencies, partial orders, and data flow. The absence of cycles guarantees that topological orderings exist.

## Questions

```yaml
- question: "A software build system needs to compile modules where some depend on others. A developer tries to add a dependency so that module A requires B, B requires C, and C requires A. Why does this break the build system?"
  type: multiple-choice
  options:
    - "The system can't handle more than two levels of dependencies"
    - "The cycle creates an impossible ordering — A must be compiled before B, B before C, and C before A, which cannot all be satisfied simultaneously"
    - "The graph would have too many edges to traverse efficiently"
    - "The system only supports undirected dependency graphs"
  answer: 1
  explanation: "A DAG models dependencies precisely because its acyclicity guarantees a valid ordering exists. The moment you introduce a directed cycle, no topological ordering is possible — there is no linear sequence that puts every prerequisite before its dependent. Real dependency systems (package managers, build tools, course sequences) enforce acyclicity for exactly this reason: a cycle represents an incoherent circular requirement."

- question: "Which property is guaranteed in every directed acyclic graph?"
  type: multiple-choice
  options:
    - "Every vertex has exactly one outgoing edge"
    - "Every vertex is reachable from every other vertex"
    - "There exists at least one vertex with no incoming edges (a source)"
    - "The graph has exactly one connected component"
  answer: 2
  explanation: "Every DAG must have at least one source (a vertex with no incoming edges). The proof is by contradiction: if every vertex had at least one incoming edge, you could always follow edges backward indefinitely, eventually revisiting a vertex — forming a cycle, which contradicts the DAG property. The symmetric argument proves every DAG also has at least one sink (vertex with no outgoing edges)."

- question: "A directed graph has a topological ordering if and only if it is a DAG."
  type: true-false
  answer: true
  explanation: "This is the fundamental equivalence: the existence of a topological ordering is exactly equivalent to acyclicity. If a directed graph contains a cycle, no linear ordering can place every vertex before those it points to — some edge will always go 'backward.' Conversely, if there are no cycles, a DFS-based algorithm can produce a topological ordering by reading finish times in reverse. A DFS cycle check and a topological sort are essentially the same computation."

- question: "A DAG can contain directed cycles, as long as those cycles don't include every vertex in the graph."
  type: true-false
  answer: false
  explanation: "By definition, a DAG contains NO directed cycles — not even partial ones. Even a single cycle involving just two or three vertices violates the acyclic property and destroys the guarantee of topological ordering. The name 'directed acyclic graph' means the entire graph is cycle-free, not just that cycles are limited in scope."

- question: "Why does every DAG have at least one source (a vertex with no incoming edges)? Explain using a proof by contradiction."
  type: short-answer
  answer: "Assume every vertex in the DAG has at least one incoming edge. Then starting at any vertex, you can always follow an edge backward to a predecessor. Since the graph is finite, you must eventually revisit a vertex — creating a directed cycle. But that contradicts the assumption that the graph is acyclic. Therefore, our assumption was false: at least one vertex must have no incoming edges."
  explanation: "This argument is important not just for DAGs but as a template for structural reasoning about directed graphs. The same logic shows every DAG has at least one sink: if every vertex had an outgoing edge, following edges forward would eventually create a cycle. Sources and sinks are the 'endpoints' that every DAG must have, and they are where topological orderings begin and end."
```

## Explainer

You already know that a **directed graph** (digraph) has edges with a direction — an arrow from A to B means something different from an arrow from B to A. Now add one constraint: no directed cycles. A **directed acyclic graph**, or **DAG**, is simply a digraph where you can never follow edges in their direction and return to where you started. That one restriction turns out to have profound consequences.

The easiest way to build intuition for DAGs is to think about prerequisites. In this knowledge graph, topics point to the topics that require them. You can't learn Gaussian elimination before you learn systems of equations. This dependency structure is a DAG — if topic A is a prerequisite for B, and B for C, then C cannot also be a prerequisite for A without creating circular reasoning. Real dependency systems (software packages, build steps, course sequences, task pipelines) are almost always DAGs for exactly this reason: cycles represent impossible orderings.

The absence of cycles has a direct structural payoff: every DAG has at least one **source** (a vertex with no incoming edges) and at least one **sink** (a vertex with no outgoing edges). This is easy to see — if every vertex had at least one incoming edge, you could always walk backwards along edges indefinitely, eventually revisiting a vertex and forming a cycle. Since that can't happen, sources must exist. The symmetric argument gives sinks.

This is why **topological sorting** is possible in DAGs but not in general digraphs. A topological ordering is a linear sequence of all vertices such that every directed edge goes from earlier to later in the sequence. It's the formal version of "do all prerequisites before the topic they unlock." Your prerequisite on cycle detection in directed graphs connects here: a digraph has a topological ordering if and only if it contains no directed cycle — i.e., if and only if it is a DAG. Any DFS-based cycle check on a directed graph is simultaneously a test for DAG-ness. If no back-edge is found, you have a DAG and can read off a topological order from the DFS finish times in reverse.
