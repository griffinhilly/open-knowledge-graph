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
status: draft
---

# Planar Graphs: Kuratowski's and Wagner's Theorems

## Core Idea
Kuratowski's theorem characterizes planar graphs: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃. Wagner's theorem gives an equivalent condition using graph minors instead of subdivisions. These theorems are foundational for understanding planar graph structure.

## How It's Best Learned
Attempt to draw K₅ and K₃,₃ in the plane, recognizing why both are non-planar. Then verify Kuratowski's criterion on graphs you suspect are non-planar by finding a subdivision.

## Explainer

You already know that a graph is **planar** if it can be drawn in the plane without edge crossings, and that Euler's formula (V − E + F = 2) constrains how many edges a planar graph can have. But Euler's formula only gives a *necessary* condition — it can rule out planarity but can't confirm it. Kuratowski's and Wagner's theorems give a complete **if and only if** characterization, turning planarity into a structural question about forbidden patterns.

The two fundamental non-planar graphs are **K₅** (complete graph on 5 vertices, where every vertex connects to every other) and **K₃,₃** (complete bipartite graph with two sets of 3 vertices, where every vertex in one set connects to every vertex in the other). Try to draw either in the plane — you'll always end up with a crossing you can't eliminate. Kuratowski's theorem says these two are the *only* obstructions, in the following sense: a graph is planar if and only if it contains no **subdivision** of K₅ or K₃,₃. A subdivision is obtained by replacing each edge with a path (inserting new "degree-2" vertices along edges). So a graph that has a K₃,₃ hiding inside it — even with extra vertices subdividing its edges — is non-planar.

Wagner's theorem reframes the same idea using **graph minors** instead of subdivisions. A minor is obtained by contracting edges (merging the two endpoints into one vertex) and deleting edges or vertices. Wagner proved: a graph is planar if and only if it has no minor isomorphic to K₅ or K₃,₃. Minors are a strictly coarser equivalence than subdivisions — every subdivision is a minor, but not vice versa — so the two theorems are equivalent but their proofs use different machinery.

The significance of these theorems extends far beyond planarity. They inspired the **Robertson-Seymour theorem**, one of the deepest results in graph theory, which proved that for *any* graph property closed under minors, there is a finite list of forbidden minors characterizing it — a vast generalization of Wagner's theorem. The algorithmic implications are also profound: planarity testing can be done in linear time by searching for K₅ or K₃,₃ subdivisions, and the structure of planar graphs underpins efficient algorithms for the four-color theorem, network routing, and VLSI circuit layout.
