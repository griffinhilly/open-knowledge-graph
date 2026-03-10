---
id: topological-sort
title: Topological Sort
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: graph-theory-intro
  type: soft
- id: graph-connectivity
  type: soft
builds-toward:
- dynamic-programming-intro
tags:
- topological-sort
- DAG
- ordering
- dependencies
stage: formal-systems
status: draft
---

# Topological Sort

## Core Idea
Topological sort produces a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u → v, u appears before v. It is only possible for DAGs — any graph with a cycle has no valid topological ordering. Two standard algorithms are DFS-based (append each node to a result stack on DFS finish, then reverse) and Kahn's algorithm (iteratively remove nodes with in-degree zero using a queue). Topological sort is essential for scheduling problems, build systems, and resolving dependency chains.

## How It's Best Learned
Implement both the DFS-based approach and Kahn's algorithm. Apply both to a concrete dependency problem such as course prerequisite ordering. Verify that Kahn's algorithm detects cyclic graphs by checking whether all nodes appear in the output.

## Common Misconceptions
- Topological sort is not unique; a DAG can have many valid orderings.
- A graph with cycles has no topological ordering; Kahn's algorithm detects this naturally, while the DFS-based approach requires explicit cycle detection.
