---
id: degree-sequences
title: Degree Sequences and Graph Realization
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
- id: graph-representation
  type: hard
builds-toward:
- erdos-gallai-theorem
tags:
- graph-theory
- sequences
- degrees
stage: abstract-reasoning
status: draft
---

# Degree Sequences and Graph Realization

## Core Idea
A degree sequence is the list of degrees of all vertices in a graph, typically written in non-increasing order. The realization problem asks: given a sequence of non-negative integers, does there exist a simple graph having exactly that degree sequence? Understanding which sequences are graphical is fundamental to analyzing graph structure.

## Explainer

You know from graph theory basics that the **degree** of a vertex is the number of edges incident to it. The **degree sequence** of a graph is simply the list of all vertex degrees, written in non-increasing order. For a triangle (3 vertices, 3 edges), every vertex has degree 2, so the degree sequence is (2, 2, 2). For a path of 4 vertices, the two endpoints have degree 1 and the two interior vertices have degree 2, giving (2, 2, 1, 1). The degree sequence is a coarse summary of a graph's structure — it tells you how "connected" the graph is without specifying which vertices connect to which.

The first essential fact is the **handshaking lemma**: the sum of all vertex degrees equals twice the number of edges. Each edge contributes 1 to the degree of each of its two endpoints, so it contributes 2 to the total degree count. Two immediate consequences: the sum of any degree sequence must be even, and an odd number of vertices with odd degree is impossible. These are necessary conditions for a sequence to be **graphical** — that is, realizable as the degree sequence of some simple graph. But they are not sufficient. The sequence (3, 1, 1, 1) sums to 6 (even) and describes a star graph K₁,₃. The sequence (3, 3, 2, 2, 2) sums to 12 (even) — is it realizable?

The **Erdős–Gallai theorem** gives a complete characterization of graphical sequences. A sequence d₁ ≥ d₂ ≥ ⋯ ≥ dₙ is graphical if and only if (1) the sum is even, and (2) for each k from 1 to n, the sum of the k largest degrees is at most k(k−1) plus the sum of min(dᵢ, k) for all remaining vertices. This looks complicated, but the idea is intuitive: the k highest-degree vertices can connect to at most k(k−1) other vertices among themselves (since it's a simple graph, no self-loops or multi-edges), and can only absorb min(dᵢ, k) connections from each remaining vertex. The theorem checks that no subset of high-degree vertices demands more connections than the rest of the graph can provide.

The realization problem also connects to graph representation: given a graphical sequence, you can construct a concrete graph using the **Hakimi algorithm** — repeatedly attach the highest-degree vertex to the next highest-degree vertices, reduce degrees accordingly, and repeat. This greedy construction always works if the sequence is graphical. Understanding degree sequences becomes foundational when you study random graphs (where you ask "what graph properties are typical for a random degree sequence?") and network analysis (where degree sequences characterize the connectivity structure of social networks, the internet, or biological systems).
