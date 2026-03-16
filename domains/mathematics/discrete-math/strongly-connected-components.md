---
id: strongly-connected-components
title: Strongly Connected Components
domain: mathematics
course: discrete-math
prerequisites:
- id: directed-graphs-and-digraphs
  type: hard
- id: graph-connectivity
  type: hard
builds-toward:
- topological-sorting
- condensation-digraph
tags:
- directed-graphs
- connectivity
- components
stage: formal-systems
status: draft
---

# Strongly Connected Components

## Core Idea
A strongly connected component (SCC) is a maximal subset of vertices where every vertex is reachable from every other vertex following directed edges. Partitioning a digraph into SCCs reveals its underlying structure and identifies cycles.

## Explainer

From your prerequisite on directed graphs, you know that a digraph's edges have direction — getting from A to B doesn't mean you can get from B to A. This asymmetry creates a richer notion of connectivity than in undirected graphs. A **strongly connected component** (SCC) is a maximal group of vertices where mutual reachability holds: from any vertex in the group, you can follow directed edges to reach every other vertex in the group. "Maximal" means you can't add any more vertices to the group while preserving this mutual reachability.

Think of a social network where edges represent "can directly contact." An SCC is a clique of mutual accessibility — a set of people who can all communicate with each other along the directed links. Vertices outside each other's SCCs have one-way or no reachability. A digraph always decomposes into SCCs, and this decomposition is unique: every vertex belongs to exactly one SCC (even if it's a trivial SCC of size 1, a vertex that can't reach itself).

The two classic algorithms — **Kosaraju's** and **Tarjan's** — both run in O(V+E) time using depth-first search from your graph connectivity background. Kosaraju's is conceptually clean: run DFS on the original graph, recording finish times; then run DFS on the *reversed* graph in decreasing finish-time order. Each DFS tree in the second pass is exactly one SCC. The key insight is that reversing all edges swaps "reachable from" with "can reach" — so the two passes together identify exactly the mutual-reachability clusters.

Once you've found all SCCs, you can build the **condensation digraph**: collapse each SCC to a single super-vertex and keep the inter-SCC edges. The condensation is always a DAG (directed acyclic graph) — if it had a cycle, those SCCs would merge into one larger SCC, contradicting maximality. This DAG view is powerful: it reveals the large-scale flow structure of the original graph, which is the first step toward topological sorting and understanding which parts of a system can influence other parts without possibility of feedback.
