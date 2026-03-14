---
id: adjacency-matrix
title: Adjacency Matrix and Spectral Basics
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-representation
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- graph-laplacian
- matrix-tree-theorem
tags:
- algebraic-graph-theory
- matrices
- spectrum
stage: abstract-reasoning
status: draft
---

# Adjacency Matrix and Spectral Basics

## Core Idea
The adjacency matrix A of a graph has A[i,j] = 1 if vertices i,j are adjacent, 0 otherwise. Its eigenvalues (spectrum) encode structural information: largest eigenvalue relates to max degree, closed walks of length k appear in tr(A^k), and spectral properties reveal connectivity, regularity, and expansion. Spectral graph theory bridges linear algebra and graph combinatorics.
