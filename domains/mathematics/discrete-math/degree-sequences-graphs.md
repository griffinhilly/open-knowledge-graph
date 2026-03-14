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
