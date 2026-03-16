---
id: mengers-theorem
title: Menger's Theorem and Network Connectivity
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: max-flow-min-cut-theorem
  type: hard
- id: graph-connectivity
  type: soft
tags:
- graph-theory
- connectivity
- paths
stage: formal-systems
status: draft
---

# Menger's Theorem and Network Connectivity

## Core Idea
Menger's Theorem states that the maximum number of edge-disjoint paths between two vertices equals the minimum number of edges whose removal disconnects them. This theorem reveals that connectivity is dual to separability; it follows as a consequence of max-flow min-cut by translating path-disjointness into flow problems.
