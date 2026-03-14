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
