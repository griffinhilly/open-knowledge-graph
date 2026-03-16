---
id: condensation-digraph
title: Graph Condensation and Metagraph
domain: mathematics
course: discrete-math
prerequisites:
- id: strongly-connected-components
  type: hard
tags:
- directed-graphs
- components
- structure
stage: formal-systems
status: draft
---

# Graph Condensation and Metagraph

## Core Idea
The condensation (or metagraph) of a digraph contracts each strongly connected component to a single vertex, creating a DAG. This transformation simplifies the structure of complex digraphs and reveals their layered organization. The condensation is unique and is itself a DAG.

## Explainer

You already know that a **strongly connected component (SCC)** is a maximal set of vertices where every vertex can reach every other. Now imagine zooming out: instead of seeing individual vertices, you see whole SCCs as single blobs. The graph you get by collapsing each blob to a point is the **condensation** (also called the metagraph or DAG of SCCs).

Why is the condensation always a DAG? Suppose it had a cycle — say SCC A could reach SCC B and SCC B could reach SCC A. Then every vertex in A could reach every vertex in B and vice versa, meaning A and B were actually one larger SCC, contradicting the assumption that they were separate. So no cycles can exist in the condensation. Every directed graph, no matter how tangled, has a unique condensation that is a DAG.

This is powerful because DAGs are much easier to work with than general digraphs. DAGs have topological orderings, no circular dependencies, and admit efficient dynamic programming. The condensation lets you "factor out" the cyclic complexity of a graph: first understand the structure among SCCs (which ones can reach which others), then separately analyze the internal structure within each SCC. This two-level view is especially useful in compiler design (dependency resolution), deadlock analysis, and anywhere you need to find a linear order in a system with loops.

Concretely, consider a digraph with six vertices where vertices {1,2,3} all reach each other, {4,5} all reach each other, and vertex 3 has an edge to 4, and vertex 5 has an edge to 6. The condensation has three nodes — call them A={1,2,3}, B={4,5}, C={6} — with edges A→B and B→C. This tiny DAG reveals that A is a "source" SCC, B is a "middle" layer, and C is a "sink" SCC. The topological order A,B,C tells you the flow of reachability through the whole system.
