---
id: graph-representation
title: 'Graph Representation: Matrices and Lists'
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
- id: matrices-intro
  type: soft
builds-toward:
- graph-connectivity
- graph-isomorphism
tags:
- adjacency-matrix
- adjacency-list
- graph-representation
- incidence-matrix
stage: formal-systems
status: draft
---

# Graph Representation: Matrices and Lists

## Core Idea
Graphs can be represented computationally in multiple ways. An adjacency matrix is an n×n matrix where entry (i,j) is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. An adjacency list stores, for each vertex, the list of its neighbors. Adjacency matrices support O(1) edge lookup but use O(n²) space; adjacency lists use space proportional to vertices plus edges and are preferred for sparse graphs. Powers of the adjacency matrix count the number of walks of a given length between vertices.

## How It's Best Learned
Practice converting between graph drawings and both matrix and list representations for the same graph. Compare storage trade-offs for dense versus sparse graphs with concrete examples. Compute A² for a small graph and verify it counts 2-step walks.

## Common Misconceptions
- Assuming adjacency matrices are always symmetric — this is only true for undirected graphs.
- Ignoring space-versus-time trade-offs when choosing a representation for a given application.
