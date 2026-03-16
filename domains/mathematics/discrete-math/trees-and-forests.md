---
id: trees-and-forests
title: Trees, Forests, and Spanning Trees
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: hard
- id: graph-connectivity-components
  type: soft
builds-toward:
- minimum-spanning-trees
tags:
- graph-theory
- trees
stage: formal-systems
status: draft
---

# Trees, Forests, and Spanning Trees

## Core Idea
A tree is a connected acyclic graph with n vertices and n-1 edges. A forest is a disjoint union of trees. A spanning tree of a graph is a subgraph that includes all vertices and is itself a tree. Trees are fundamental in computer science and have unique shortest paths between any two vertices.

## Explainer

From your graph theory prerequisite, you know a graph is a set of vertices connected by edges, and you can ask about paths, cycles, and connectivity. A **tree** is defined by two simple conditions held simultaneously: the graph is connected (you can reach any vertex from any other) and it contains no cycles (there is no closed loop). The remarkable thing is that these two conditions together force the edge count: any tree on n vertices has exactly n − 1 edges. Intuitively, you need at least n − 1 edges to connect n vertices (less and the graph disconnects), and adding one more creates a cycle. Trees are the "just barely connected" structures.

The no-cycle condition has a powerful consequence: there is exactly one path between any two vertices in a tree. If there were two distinct paths from u to v, following one forward and the other backward would form a cycle — contradicting the acyclic requirement. This uniqueness is what makes trees so useful in computer science: directory structures, parse trees, and search algorithms all exploit the fact that there is one canonical route between any two nodes.

A **forest** is simply a graph whose connected components are each trees — a disjoint union of trees. If a forest has n vertices and k connected components, it has exactly n − k edges. A forest with k = 1 component is a tree. This generalizes the tree edge count neatly.

A **spanning tree** of a connected graph G is a subgraph that (1) contains all vertices of G and (2) is itself a tree. You build a spanning tree by discarding edges while keeping the graph connected — strip away edges one at a time, but never disconnect anything. Equivalently, a spanning tree is a minimal connected spanning subgraph. Most graphs have many spanning trees. The question of how many — counting spanning trees — leads directly to the Matrix Tree Theorem. The question of which spanning tree minimizes total edge weight leads to the minimum spanning tree algorithms (Kruskal's, Prim's) that you will study next.
