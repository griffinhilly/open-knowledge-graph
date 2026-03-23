---
id: planar-graphs-kuratowski-wagner
title: 'Planar Graphs: Kuratowski''s and Wagner''s Theorems'
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: planar-graphs
  type: hard
- id: formal-definitions-graph-theory
  type: soft
builds-toward:
- four-color-theorem
- graph-minors-robertson-seymour
tags:
- planar-graphs
- kuratowski
- wagner
- forbidden-subgraphs
stage: formal-systems
status: validated
---

# Planar Graphs: Kuratowski's and Wagner's Theorems

## Core Idea
Kuratowski's theorem characterizes planar graphs: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃. Wagner's theorem gives an equivalent condition using graph minors instead of subdivisions. These theorems are foundational for understanding planar graph structure.

## How It's Best Learned
Attempt to draw K₅ and K₃,₃ in the plane, recognizing why both are non-planar. Then verify Kuratowski's criterion on graphs you suspect are non-planar by finding a subdivision.

## Questions

```yaml
- question: "A graph G has 10 vertices, 20 edges, and 12 faces. Since V − E + F = 10 − 20 + 12 = 2, Euler's formula is satisfied. Can you conclude that G is planar?"
  type: multiple-choice
  options:
    - "Yes — Euler's formula is satisfied, confirming G is planar"
    - "No — Euler's formula is a necessary condition for planarity but not sufficient; you would need to verify G contains no subdivision of K₅ or K₃,₃"
    - "Yes — if V − E + F = 2 holds, the graph must be embeddable in the plane"
    - "It depends on whether G is connected and simple"
  answer: 1
  explanation: "Euler's formula provides a necessary condition: any connected planar graph must satisfy V − E + F = 2. But satisfying the formula doesn't prove planarity — the formula can't even be evaluated without first assuming a planar embedding exists. Kuratowski's theorem gives the complete if-and-only-if characterization: G is planar exactly when it contains no subdivision of K₅ or K₃,₃."

- question: "Graph G contains K₃,₃ as a minor (obtained by contracting and deleting edges). What does Wagner's theorem tell you about G?"
  type: multiple-choice
  options:
    - "G is non-planar only if it also contains K₃,₃ as a subdivision"
    - "G is non-planar — having K₃,₃ as a minor is sufficient by Wagner's theorem"
    - "Wagner's theorem applies only to K₅, not K₃,₃"
    - "G might still be planar since K₃,₃ appears only as a minor, not as a subgraph"
  answer: 1
  explanation: "Wagner's theorem states: a graph is planar if and only if it contains no minor isomorphic to K₅ or K₃,₃. Having K₃,₃ as a minor is sufficient to conclude non-planarity — this is the full biconditional. Options A and D reflect a common confusion: minors are a coarser relation than subdivisions, but both are sufficient to certify non-planarity."

- question: "Kuratowski's theorem proves that every non-planar graph IS either K₅ or K₃,₃."
  type: true-false
  answer: false
  explanation: "Kuratowski's theorem says a graph is non-planar if and only if it CONTAINS a subdivision of K₅ or K₃,₃ — not that it equals one. Non-planar graphs can be arbitrarily large and complex; what's guaranteed is that somewhere inside them you can find a K₅ or K₃,₃ subdivision as a pattern. The theorem characterizes non-planarity by a forbidden pattern, not by identity with those two graphs."

- question: "If a graph G contains a subdivision of K₅, then G also contains K₅ as a minor."
  type: true-false
  answer: true
  explanation: "Every subdivision is a minor. A subdivision of K₅ inserts degree-2 vertices along edges; contracting those inserted vertices back down gives K₅ itself, which is therefore a minor of G. This is why minors are a coarser relation: every subdivision is a minor, but not every minor arises from subdivision. Wagner's theorem uses the coarser condition (minors) while Kuratowski's uses the finer one (subdivisions), yet both equivalently characterize planarity."

- question: "Explain the difference between a subdivision and a minor of a graph. Which operation is coarser, and why are both sufficient to detect non-planarity?"
  type: short-answer
  answer: "A subdivision inserts new degree-2 vertices along edges, replacing each edge with a path. A minor is obtained by contracting edges (merging their endpoints) and deleting edges or vertices — a strictly more permissive operation. Minors are coarser. Every subdivision is a minor (contract the inserted vertices back), but not every minor arises from subdivision. Both detect non-planarity because neither operation can make a non-planar graph planar: if G can be drawn without crossings, any graph obtained by subdividing or contracting its edges can also be drawn without crossings."
  explanation: "The equivalence of Kuratowski's and Wagner's characterizations shows that non-planarity is robust under both operations. This robustness is the seed of the Robertson-Seymour theorem, which generalizes Wagner's result to prove that any minor-closed graph property has a finite forbidden minor characterization — one of the deepest results in graph theory."
```

## Explainer

You already know that a graph is **planar** if it can be drawn in the plane without edge crossings, and that Euler's formula (V − E + F = 2) constrains how many edges a planar graph can have. But Euler's formula only gives a *necessary* condition — it can rule out planarity but can't confirm it. Kuratowski's and Wagner's theorems give a complete **if and only if** characterization, turning planarity into a structural question about forbidden patterns.

The two fundamental non-planar graphs are **K₅** (complete graph on 5 vertices, where every vertex connects to every other) and **K₃,₃** (complete bipartite graph with two sets of 3 vertices, where every vertex in one set connects to every vertex in the other). Try to draw either in the plane — you'll always end up with a crossing you can't eliminate. Kuratowski's theorem says these two are the *only* obstructions, in the following sense: a graph is planar if and only if it contains no **subdivision** of K₅ or K₃,₃. A subdivision is obtained by replacing each edge with a path (inserting new "degree-2" vertices along edges). So a graph that has a K₃,₃ hiding inside it — even with extra vertices subdividing its edges — is non-planar.

Wagner's theorem reframes the same idea using **graph minors** instead of subdivisions. A minor is obtained by contracting edges (merging the two endpoints into one vertex) and deleting edges or vertices. Wagner proved: a graph is planar if and only if it has no minor isomorphic to K₅ or K₃,₃. Minors are a strictly coarser equivalence than subdivisions — every subdivision is a minor, but not vice versa — so the two theorems are equivalent but their proofs use different machinery.

The significance of these theorems extends far beyond planarity. They inspired the **Robertson-Seymour theorem**, one of the deepest results in graph theory, which proved that for *any* graph property closed under minors, there is a finite list of forbidden minors characterizing it — a vast generalization of Wagner's theorem. The algorithmic implications are also profound: planarity testing can be done in linear time by searching for K₅ or K₃,₃ subdivisions, and the structure of planar graphs underpins efficient algorithms for the four-color theorem, network routing, and VLSI circuit layout.
