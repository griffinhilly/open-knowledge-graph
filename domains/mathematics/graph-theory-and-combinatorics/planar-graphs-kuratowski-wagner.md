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
