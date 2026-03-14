---
id: graph-connectivity
title: Graph Paths, Cycles, and Connectivity
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: mathematical-induction
  type: soft
- id: graph-representation
  type: soft
builds-toward:
- bipartite-graphs
- trees-in-graph-theory
- euler-circuits-and-paths
- hamiltonian-circuits
- planar-graphs
- graph-coloring
tags:
- paths
- cycles
- connectivity
- connected-components
- graph-theory
stage: formal-systems
status: validated
---
# Graph Paths, Cycles, and Connectivity

## Core Idea
A path is a sequence of distinct vertices where consecutive vertices are connected by edges. A cycle is a closed path where the first and last vertices are the same. A graph is connected if there is a path between every pair of vertices; otherwise it consists of multiple disconnected components. The distinction between walks (vertices may repeat), trails (edges do not repeat), and paths (vertices do not repeat) is essential. Connectivity is the foundational structural property for almost all graph-theoretic results.

## How It's Best Learned
Practice finding paths and cycles in small graphs by hand, writing out vertex sequences explicitly. Test connectivity by trying to reach every vertex from a fixed start. Deliberately construct examples that distinguish walks from trails from paths.

## Common Misconceptions
- Confusing walks, trails, and paths — these are distinct notions and the differences matter for theorems.
- Assuming a connected graph has a unique path between any two vertices — only trees have this property.
- Thinking 'no isolated vertices' implies connectivity.
