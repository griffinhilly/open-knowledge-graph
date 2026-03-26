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

## Questions

```yaml
- question: "A simple undirected graph has 6 vertices with degrees 4, 3, 3, 2, 2, 2. How many edges does it have?"
  type: multiple-choice
  options: ["8", "16", "6", "Cannot be determined without the edge list"]
  answer: 0
  explanation: "By the handshaking lemma, the sum of all degrees equals twice the number of edges. Sum of degrees = 4+3+3+2+2+2 = 16, so the number of edges = 16/2 = 8. This works for any simple undirected graph — no edge list needed."

- question: "Two drawings of a graph that look geometrically different (e.g., one has crossing edges, the other doesn't) should be different graphs."
  type: true-false
  answer: false
  explanation: "A graph is defined by its vertex and edge sets G = (V, E), not by how it is drawn on paper. The same graph can be drawn in infinitely many ways. Two graphs that look different in a drawing may be isomorphic — structurally identical. Only the combinatorial relationships matter, not the geometric positions of vertices."

- question: "What does the degree of a vertex represent, and why does the handshaking lemma follow from this definition?"
  type: short-answer
  answer: "The degree of a vertex is the number of edges incident to it. The handshaking lemma (sum of degrees = 2|E|) follows because each edge contributes exactly 1 to the degree of each of its two endpoints, so every edge is counted exactly twice when you sum all degrees."
  explanation: "This question tests whether students understand degree as counting edge-endpoint incidences. The factor of 2 is not arbitrary — it reflects the fact that every edge has two endpoints. This is a clean example of a combinatorial identity that follows directly from the definition."
```

## Explainer

Graph theory begins with a deceptively simple idea: take a set of objects (vertices) and a set of pairwise relationships between them (edges). Formally, a graph G = (V, E) is just these two sets. Despite this minimalism, graph theory captures the structure of an enormous range of real-world systems — social networks, road maps, the internet, molecular bonds, and prerequisite relationships like those in this knowledge graph.

A key concept to internalize early is that a graph is a *combinatorial* object, not a geometric one. When you draw a graph on paper, the positions of the vertices and the curves of the edges are irrelevant. What matters is which vertices are connected by edges. Two drawings that look completely different can represent the exact same graph. This means your intuitions about geometry (distance, area, crossing) do not directly apply — you have to reason purely from the adjacency relationships.

The *degree* of a vertex is the number of edges incident to it. In a social network, degree is how many friends someone has. The *handshaking lemma* says that the sum of all vertex degrees equals twice the number of edges: Σ deg(v) = 2|E|. The proof is a one-liner: each edge contributes exactly 1 to the degree of each of its two endpoints, so summing over all vertices counts each edge exactly twice. This lemma has an immediate corollary: the number of odd-degree vertices in any graph must be even.

Graphs come in several important variants. A *simple graph* has no loops (edges from a vertex to itself) and no multiple edges between the same pair of vertices. A *multigraph* allows multiple edges. A *directed graph* (or digraph) has edges with direction — each edge goes from one vertex *to* another, not just *between* them. The choice of which variant to use depends on what you are modeling: flight routes between cities are naturally a directed graph (routes may be one-way), while friendship networks are typically undirected.

Because you already know set theory, you can use that framework fluently here. The vertex set V and edge set E are just sets; their cardinalities |V| and |E| are the number of vertices and edges. An edge between vertices u and v is an unordered pair {u, v} in the undirected case, or an ordered pair (u, v) in the directed case. This set-theoretic foundation is what lets graph theory scale up to rigorous proofs — you start from definitions and derive everything from there.
