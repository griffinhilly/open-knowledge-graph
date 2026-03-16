---
id: degree-sequences-graphs
title: Degree Sequences and the Handshaking Lemma
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: hard
builds-toward:
- bipartite-graphs-characterization
tags:
- graph-theory
- degree
stage: formal-systems
status: draft
---

# Degree Sequences and the Handshaking Lemma

## Core Idea
The degree deg(v) of a vertex v is the number of edges incident to it. The handshaking lemma states Σ deg(v) = 2|E| (sum of degrees equals twice the number of edges). This implies the number of vertices with odd degree is always even.

## How It's Best Learned
Draw small graphs and compute degrees for each vertex. Verify the handshaking lemma.

## Common Misconceptions
- Forgetting to count each edge twice in the sum.
- Confusing in-degree and out-degree in directed graphs.
- Not recognizing that the sum of degrees is always even.

## Explainer

You already know from graph fundamentals that a graph is a collection of vertices (nodes) connected by edges. The **degree** of a vertex is simply how many edges attach to it — think of it as the number of neighbors a person has in a social network. A vertex with degree 3 has exactly 3 edges coming out of it, regardless of what those edges connect to.

The **Handshaking Lemma** says something elegant: if you add up the degrees of every vertex in a graph, you always get exactly twice the number of edges. The name comes from the handshake metaphor — if 5 people each shake hands once, 5 handshakes occur, but the total number of "hands shaken" is 10, because each handshake involves two hands. Every edge, similarly, contributes 1 to exactly two vertices' degree counts. So when you sum all degrees, every edge gets counted twice, giving Σ deg(v) = 2|E|.

The most useful corollary follows immediately: since 2|E| is always even, the sum of all degrees is always even. The only way a sum can be even is if there are an even number of odd terms — so the number of odd-degree vertices must be even. You can never draw a graph with, say, exactly 3 vertices of odd degree. This constraint is a powerful sanity check when constructing or reasoning about graphs.

The **degree sequence** of a graph lists all vertex degrees in non-increasing order (e.g., [4, 3, 3, 2, 2, 2]). It encodes structural information about the graph — a dense, hub-and-spoke network looks different in its degree sequence than a sparse chain. The Handshaking Lemma lets you immediately rule out impossible degree sequences: if the sum of the proposed degrees is odd, no such graph can exist. This makes degree sequences one of the simplest graph invariants — properties you can compute quickly to test whether two graphs might or might not be structurally the same.
