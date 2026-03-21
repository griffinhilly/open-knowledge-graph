---
id: kuratowskis-theorem
title: Kuratowski's Theorem and Forbidden Minors
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: planar-graphs
  type: hard
builds-toward:
- wagners-theorem
- graph-minors
tags:
- graph-theory
- planar-graphs
stage: formal-systems
status: draft
---

# Kuratowski's Theorem and Forbidden Minors

## Core Idea
Kuratowski's Theorem characterizes planar graphs by forbidden minors: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃. This shows that planarity is completely determined by the absence of two specific topological structures, providing a constructive understanding of why certain graphs cannot be drawn planar.

## Questions

```yaml
- question: "A student examines graph G and finds a subgraph that is a subdivision of K₅. What can the student immediately conclude?"
  type: multiple-choice
  options:
    - "G might or might not be planar — a K₅ subdivision is necessary but not sufficient for non-planarity"
    - "G is non-planar, by Kuratowski's theorem"
    - "G is planar, since the K₅ subdivision has been identified and can be isolated from the rest of the graph"
    - "G is non-planar only if it also contains a K₃,₃ subdivision"
  answer: 1
  explanation: "Kuratowski's theorem says a graph is planar if and only if it contains NO subdivision of K₅ or K₃,₃. Finding a K₅ subdivision in G confirms G is non-planar — you only need one forbidden subdivision. Options A and D misread the theorem: you don't need both, and the condition is 'if and only if,' so a subdivision is both necessary and sufficient (in the negative direction). Option C is incorrect because the crossing structure of the subdivision cannot be isolated away from the rest of the graph."

- question: "Why are K₅ and K₃,₃ specifically the two forbidden subgraphs in Kuratowski's theorem, rather than some other pair of graphs?"
  type: multiple-choice
  options:
    - "They are the minimal non-planar graphs: removing any single edge or vertex from either one yields a planar graph"
    - "They were chosen arbitrarily to provide a simple two-element characterization"
    - "They are the two densest graphs that can be drawn in the plane with crossings"
    - "They are the only graphs whose vertex count exceeds the planar Euler bound E ≤ 3V − 6"
  answer: 0
  explanation: "K₅ and K₃,₃ are the unique minimal non-planar graphs. Every proper subgraph of each is planar (remove any vertex or edge and the result can be drawn without crossings). This minimality is what makes them the correct 'obstructions': any non-planar graph must contain a subdivision of one of them, but no smaller non-planar structure exists. Option D is partially true but incomplete — K₃,₃ is bipartite (no triangles), so the relevant bound is E ≤ 2V − 4, and many other graphs also violate Euler bounds without being minimal."

- question: "According to Kuratowski's theorem, a graph is planar if and only if it contains no subgraph that is a subdivision of K₅ or K₃,₃."
  type: true-false
  answer: true
  explanation: "This is the exact statement of Kuratowski's theorem (1930). It is a biconditional: planar graphs have no such subdivision (⇒ direction), and any graph without such a subdivision is planar (⇐ direction, the harder direction proved by Kuratowski). The 'if and only if' is crucial — it means the two forbidden subdivisions completely characterize the boundary between planar and non-planar graphs."

- question: "Inserting a new degree-2 vertex into the middle of an edge of a non-planar graph can make the graph planar."
  type: true-false
  answer: false
  explanation: "A subdivision of a graph — obtained by inserting degree-2 vertices along edges — preserves planarity status in both directions. If G is non-planar and contains a K₅ (or K₃,₃) subdivision, subdividing more edges of G still leaves that forbidden subdivision present as a subgraph. Conversely, if G is planar, any subdivision of G is also planar. Topology only cares about which vertices are connected and how paths route between them, not about intermediate degree-2 vertices on edges."

- question: "What is a 'subdivision' of K₅, and why is the concept of subdivision (rather than subgraph isomorphism to K₅ itself) the right tool for characterizing planarity obstructions?"
  type: short-answer
  answer: "A subdivision of K₅ is obtained by replacing each edge of K₅ with a path of one or more edges (inserting any number of degree-2 vertices along edges). The result has the same 5 'branch' vertices of degree 4, but the edges between them may pass through additional intermediate vertices. Subdivision is the right concept because planarity depends on the crossing structure of connections between high-degree vertices, not on the exact length of paths between them. A degree-2 vertex in the middle of a path cannot resolve a crossing, so the obstruction is preserved regardless of how many intermediate vertices are added."
  explanation: "This is why the theorem uses 'subdivision' rather than 'K₅ as a subgraph' — a graph can contain K₅-like crossing structure without having 5 vertices of degree 4 adjacent to each other. Any graph with a topological copy of K₅ (the connectivity is there, paths may be stretched) inherits K₅'s non-planarity. The related Wagner's theorem restates this using 'minors' (edge contractions instead of subdivisions), giving an equivalent but differently expressed characterization."
```

## Explainer

From your study of planar graphs, you know that a graph is **planar** if it can be drawn in the plane with no edge crossings. You also know that K₅ (the complete graph on 5 vertices) and K₃,₃ (the complete bipartite graph with three vertices on each side) are the two canonical non-planar graphs — both fail Euler's formula and cannot be drawn without crossings. Kuratowski's theorem tells you that these two graphs are not just examples of non-planarity — they are its complete explanation.

The precise statement involves **subdivisions**. A subdivision of a graph G is obtained by inserting additional vertices of degree 2 into edges, effectively replacing each edge with a path. This doesn't change the essential crossing structure — if K₅ can't be drawn planar, then a graph with a subdivided K₅ embedded inside it (as a subgraph after those edge-subdivision vertices are added) also can't be drawn planar. The theorem says: a graph is planar if and only if it contains no subgraph that is a subdivision of K₅ or K₃,₃. In other words, **K₅ and K₃,₃ are the only obstruction families for planarity**.

Why these two and not others? The intuition comes from counting. K₅ has 5 vertices and 10 edges; for a planar graph, Euler's formula gives E ≤ 3V − 6, so we need 10 ≤ 9 — a contradiction. K₃,₃ has 6 vertices and 9 edges; it's bipartite, so it has no triangles, meaning every face has at least 4 edges, which gives E ≤ 2V − 4 = 8 — another contradiction. These are the minimal graphs that violate planarity: remove any vertex or edge from either one and the result is planar. This minimality is exactly what makes them the right "forbidden" structures.

The proof that K₅ and K₃,₃ subdivisions are *sufficient* to obstruct planarity is the hard direction — it was proved by Kazimierz Kuratowski in 1930 and requires showing that any non-planar graph must contain one of them. The related **Wagner's theorem** (your next topic) gives an equivalent characterization using graph minors instead of subdivisions — contracting edges rather than inserting vertices. Together, these theorems opened the field of **graph minor theory**, culminating in the Robertson–Seymour theorem, which shows that every graph property closed under minors can be characterized by a finite list of forbidden minors. Planarity, with just two forbidden minors, was the first and simplest example of this deep pattern.
