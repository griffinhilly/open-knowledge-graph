---
id: bipartite-graphs
title: Bipartite Graphs and Matchings
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: graph-theory-intro
  type: hard
tags:
- bipartite
- matching
- graph-theory
- two-colorable
- hall-theorem
stage: formal-systems
status: validated
---

# Bipartite Graphs and Matchings

## Core Idea
A bipartite graph has its vertices divided into two disjoint sets U and V such that every edge connects a vertex in U to one in V — no edges exist within either set. A graph is bipartite if and only if it contains no odd-length cycle. A matching is a set of edges with no shared vertices; a perfect matching saturates every vertex. Hall's marriage theorem gives a necessary and sufficient condition for a perfect matching to exist: for every subset S of U, the neighborhood N(S) satisfies |N(S)| ≥ |S|.

## How It's Best Learned
Check bipartiteness by 2-coloring: alternate colors while traversing the graph. If you must assign the same color to two adjacent vertices, the graph has an odd cycle and is not bipartite. Model Hall's theorem with practical assignment problems (students to internships) before examining its proof.

## Common Misconceptions
- Thinking any graph without an odd cycle must be a tree — bipartite graphs can have many even cycles.
- Confusing a matching with a path or Hamiltonian circuit — matchings are a set of disjoint edges, not a traversal.
