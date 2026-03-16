---
id: adjacency-matrix-graphs
title: Adjacency Matrix and Spectral Graph Theory
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- graph-laplacian-spectrum
- matrix-tree-theorem
tags:
- adjacency-matrix
- spectral-methods
- eigenvalues
stage: advanced
status: draft
---

# Adjacency Matrix and Spectral Graph Theory

## Core Idea
The adjacency matrix A of a graph encodes its structure; its eigenvalues (spectrum) reveal deep information about the graph. The largest eigenvalue λ₁ relates to edge density, expansion properties, and diameter. Spectral methods connect linear algebra to graph combinatorics.

## Explainer

The **adjacency matrix** A of a graph with n vertices is an n × n matrix where entry Aᵢⱼ = 1 if there is an edge between vertex i and vertex j, and 0 otherwise. For an undirected graph, A is symmetric — Aᵢⱼ = Aⱼᵢ. This encoding is not just a bookkeeping device; multiplying A by itself reveals structure invisible to the eye. The entry (A²)ᵢⱼ counts the number of walks of length 2 from vertex i to vertex j, because you sum over all possible intermediate vertices k the product Aᵢₖ · Aₖⱼ. More generally, (Aᵏ)ᵢⱼ counts walks of length k between i and j. Graph connectivity questions become matrix power questions.

Because A is a real symmetric matrix, your prerequisite on eigenvalues guarantees it has n real eigenvalues and n orthogonal eigenvectors. The eigenvalues of A, sorted as λ₁ ≥ λ₂ ≥ … ≥ λₙ, are called the **spectrum** of the graph. The largest eigenvalue λ₁ (the **spectral radius**) is tightly connected to the graph's edge density: for a d-regular graph (every vertex has degree d), λ₁ = d exactly, and the eigenvector corresponding to λ₁ is the all-ones vector. The remaining eigenvalues measure how much the graph deviates from this uniform structure.

The **spectral gap** — the difference λ₁ − λ₂ — is one of the most important quantities in spectral graph theory. A large spectral gap means the graph is a good **expander**: information, random walks, or network traffic spreads quickly and does not get trapped in clusters. Expander graphs are used in error-correcting codes, derandomization, and network design precisely because their spectral gap guarantees rapid mixing. Conversely, a small spectral gap indicates that the graph is nearly disconnected — it can be cut into large pieces with few crossing edges. The **Cheeger inequality** makes this intuition precise by bounding the edge expansion ratio above and below by functions of the spectral gap.

Spectral methods also detect clustering and community structure. The eigenvectors corresponding to the smallest eigenvalues tend to assign similar values to vertices in the same community and different values to vertices in different communities — this is the mathematical basis for **spectral clustering**, a technique widely used in data science and machine learning. The adjacency matrix bridge between graph combinatorics and linear algebra is one of the most productive in all of mathematics: discrete, combinatorial structure becomes continuous geometry in eigenspace, and techniques from one world illuminate the other.
