---
id: graph-theory-intro
title: Introduction to Graph Theory
domain: mathematics
course: discrete-math
prerequisites:
- id: set-theory-basics
  type: hard
- id: counting-principles
  type: soft
builds-toward:
- graph-representation
- graph-connectivity
- graph-isomorphism
- bipartite-graphs
- trees-in-graph-theory
tags:
- graph-theory
- vertices
- edges
- degree
- handshaking-lemma
stage: formal-systems
status: validated
---

# Introduction to Graph Theory

## Core Idea
A graph G = (V, E) consists of a set of vertices V and a set of edges E, where each edge connects two vertices. Key concepts include vertex degree (the number of edges incident to a vertex), the handshaking lemma (the sum of all degrees equals twice the number of edges), and the distinction between simple graphs (no loops or multiple edges), multigraphs, and directed graphs (digraphs). Graphs model an enormous range of phenomena: social networks, road maps, circuit layouts, and dependency structures.

## How It's Best Learned
Draw graphs by hand constantly. Start with small examples (5-6 vertices), identify degrees, count edges, and verify the handshaking lemma numerically. Move between visual drawings and formal set notation to build fluency with both representations.

## Common Misconceptions
- Thinking of a graph as having a fixed geometric layout — graphs are purely combinatorial; different drawings of the same graph are equivalent.
- Confusing degree (edges at a vertex) with the number of vertices in the graph.
- Not distinguishing between directed and undirected edges when context matters.
