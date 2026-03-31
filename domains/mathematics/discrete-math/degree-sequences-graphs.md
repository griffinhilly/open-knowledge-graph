---
id: degree-sequences-graphs
title: Degree Sequences and the Handshaking Lemma
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
builds-toward:
- bipartite-graphs-characterization
tags:
- graph-theory
- degree
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "Someone proposes a graph with 6 vertices having degree sequence [4, 3, 3, 2, 2, 2]. Can such a graph exist?"
  type: multiple-choice
  options:
    - "No — the maximum degree in any graph equals the number of vertices minus one, and degree 4 requires at least 5 vertices, so 6 is acceptable, but the sequence still fails another test"
    - "No — the sum of degrees is 16, which is even, but it would require 8 edges, which exceeds what is possible"
    - "Yes — the sum of degrees is 16 (even), so 16/2 = 8 edges would be required, and the two odd-degree vertices (both degree 3) number exactly 2, which is even"
    - "No — the number of odd-degree vertices is 2, but the handshaking lemma requires zero odd-degree vertices"
  answer: 2
  explanation: "The Handshaking Lemma requires the sum of all degrees to be even (it must equal 2|E|). Sum here: 4+3+3+2+2+2 = 16 — even. So 8 edges would be needed. Additionally, the number of odd-degree vertices must be even: there are exactly 2 vertices of odd degree (both degree-3 vertices), which satisfies this requirement. The sequence passes both necessary conditions. (Passing these checks doesn't guarantee a graph exists — the Erdős–Gallai theorem gives the full characterization — but it doesn't immediately rule it out.)"

- question: "Why must every graph have an even number of vertices with odd degree?"
  type: multiple-choice
  options:
    - "Because every vertex must connect to an even number of other vertices by graph construction rules"
    - "Because the Handshaking Lemma guarantees the sum of all degrees is even, and a sum can be even only if the number of odd terms is even"
    - "Because graphs with an odd number of odd-degree vertices would require a fractional number of edges"
    - "Because the degree sequence must sum to a multiple of 4 for a valid graph"
  answer: 1
  explanation: "From the Handshaking Lemma: Σ deg(v) = 2|E|, which is always even. Now split the sum: degrees of odd-degree vertices contribute an odd amount each; degrees of even-degree vertices contribute an even amount each. The even-degree vertices' contributions sum to an even number. For the total sum to be even, the odd-degree vertices' contributions must also sum to an even number — and a sum of odd numbers is even only if there are an even count of them. Hence: number of odd-degree vertices is always even."

- question: "It is possible to draw a graph in which exactly three vertices have odd degree."
  type: true-false
  answer: false
  explanation: "The Handshaking Lemma guarantees the sum of all degrees equals 2|E|, which is even. If exactly three vertices had odd degree, those three odd numbers would sum to an odd number. Adding the even contributions from the remaining vertices still gives an odd total — contradicting Σ deg(v) = 2|E|. Therefore, no graph can have exactly 3 (or any odd number of) odd-degree vertices. This is a hard mathematical constraint, not just a convention."

- question: "The Handshaking Lemma can be used to immediately rule out an impossible degree sequence: if the proposed degrees sum to an odd number, no graph with that degree sequence can exist."
  type: true-false
  answer: true
  explanation: "Since Σ deg(v) = 2|E| must hold for any graph, the sum of degrees is always even. If someone proposes the degree sequence [3, 2, 2], the sum is 7 — odd — so no such graph exists. This is a necessary condition (failing it rules a sequence out), though not sufficient (a sequence with an even sum may still be unrealizable for other reasons, e.g., requiring more edges between two vertices than the graph allows). The Handshaking Lemma gives the quickest sanity check."

- question: "Explain intuitively why the sum of all vertex degrees must equal twice the number of edges, using the idea of how each edge is 'counted' in the sum."
  type: short-answer
  answer: "Each edge connects exactly two vertices. When you sum up every vertex's degree, each edge gets counted once for the vertex at each of its two endpoints — so every edge contributes exactly 2 to the total sum. If there are |E| edges, the total is 2|E|. The handshake metaphor makes this vivid: each handshake (edge) involves two people (vertices), so the total number of 'hands shaken' (sum of degrees) is twice the number of handshakes (edges)."
  explanation: "This double-counting argument is the simplest proof in graph theory. It works because the degree of a vertex counts incident edges from that vertex's perspective. When you aggregate across all vertices, each edge is seen from both its endpoints, so it contributes 2 to the total. This same double-counting technique appears throughout combinatorics: summing a quantity from different perspectives and equating the two counts is a recurring proof strategy."
```

## Explainer

You already know from graph fundamentals that a graph is a collection of vertices (nodes) connected by edges. The **degree** of a vertex is simply how many edges attach to it — think of it as the number of neighbors a person has in a social network. A vertex with degree 3 has exactly 3 edges coming out of it, regardless of what those edges connect to.

The **Handshaking Lemma** says something elegant: if you add up the degrees of every vertex in a graph, you always get exactly twice the number of edges. The name comes from the handshake metaphor — if 5 people each shake hands once, 5 handshakes occur, but the total number of "hands shaken" is 10, because each handshake involves two hands. Every edge, similarly, contributes 1 to exactly two vertices' degree counts. So when you sum all degrees, every edge gets counted twice, giving Σ deg(v) = 2|E|.

The most useful corollary follows immediately: since 2|E| is always even, the sum of all degrees is always even. The only way a sum can be even is if there are an even number of odd terms — so the number of odd-degree vertices must be even. You can never draw a graph with, say, exactly 3 vertices of odd degree. This constraint is a powerful sanity check when constructing or reasoning about graphs.

The **degree sequence** of a graph lists all vertex degrees in non-increasing order (e.g., [4, 3, 3, 2, 2, 2]). It encodes structural information about the graph — a dense, hub-and-spoke network looks different in its degree sequence than a sparse chain. The Handshaking Lemma lets you immediately rule out impossible degree sequences: if the sum of the proposed degrees is odd, no such graph can exist. This makes degree sequences one of the simplest graph invariants — properties you can compute quickly to test whether two graphs might or might not be structurally the same.
