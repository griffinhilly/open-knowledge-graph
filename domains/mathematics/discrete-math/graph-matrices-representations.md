---
id: graph-matrices-representations
title: 'Graph Representation: Adjacency and Incidence Matrices'
domain: mathematics
course: discrete-math
prerequisites:
- id: adjacency-matrix
  type: hard
- id: graph-fundamentals-discrete
  type: hard
builds-toward:
- connectivity-components-discrete
tags:
- adjacency-matrix
- incidence-matrix
- representation
- computation
stage: formal-systems
status: draft
---

# Graph Representation: Adjacency and Incidence Matrices

## Core Idea
An adjacency matrix A represents a graph where A[i,j] is the number of edges from vertex i to vertex j (0 or 1 for simple graphs). An incidence matrix shows vertex-edge relationships. These representations enable algorithmic computation on graphs.

## How It's Best Learned
Construct adjacency matrices for small graphs by hand. Observe that A² counts paths of length 2. See how matrix properties (symmetry, sparsity) reflect graph structure.

## Common Misconceptions
The adjacency matrix for an undirected graph is symmetric; for directed graphs it need not be. Diagonal entries are 0 in simple graphs (no self-loops).
