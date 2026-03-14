---
id: directed-graphs-and-digraphs
title: Directed Graphs and Digraphs
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: hard
builds-toward:
- strongly-connected-components
- topological-sorting
- cycle-detection-directed-graphs
tags:
- graph-theory
- directed-graphs
- digraphs
stage: formal-systems
status: draft
---

# Directed Graphs and Digraphs

## Core Idea
Directed graphs (digraphs) extend graph theory by adding direction to edges. Each edge points from one vertex to another, creating paths and cycles with directionality. They model relationships where direction matters: web links, tournament results, and state transitions.

## How It's Best Learned
Draw digraphs with arrows showing direction. Trace paths following arrow directions. Compare directed vs. undirected versions of the same graph to see how direction changes properties like connectivity.

## Common Misconceptions
- Assuming an undirected edge is bidirectional in a digraph. - Overlooking that cycles are harder to define in directed graphs due to the direction constraint.
