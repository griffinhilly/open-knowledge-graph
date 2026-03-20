---
id: topological-sorting
title: Topological Sorting and Ordering
domain: mathematics
course: discrete-math
prerequisites:
- id: directed-graphs-and-digraphs
  type: hard
- id: directed-acyclic-graphs
  type: hard
builds-toward: []
tags:
- directed-graphs
- ordering
- algorithms
stage: advanced
status: draft
---
# Topological Sorting and Ordering

## Core Idea
Topological sorting arranges vertices of a directed acyclic graph (DAG) in a linear order such that for every directed edge from u to v, u comes before v. This ordering is useful for scheduling tasks with dependencies, resolving symbol dependencies in compilers, and determining precedence.

## Explainer

You already know that a **directed acyclic graph** (DAG) models dependencies: an edge from u to v means "u must come before v." A **topological sort** turns that partial ordering into a total ordering — a single linear sequence where all the "must come before" constraints are respected. The everyday analogy is a college degree plan: courses have prerequisites, and a valid course schedule is a topological sort of the prerequisite DAG.

The key reason topological sorts only exist for DAGs is intuitive: if the graph contained a directed cycle (A → B → C → A), then A would need to come before itself, which is impossible in any linear order. This makes cycle detection a natural companion to topological sorting — if you try to sort a graph and fail, you've found a cycle.

There are two standard algorithms. **Kahn's algorithm** works by repeatedly identifying vertices with no incoming edges (no remaining prerequisites) and removing them one at a time, adding each to the output sequence. Any vertex with in-degree 0 is "safe to go first" given what remains. When you remove a vertex, you decrement the in-degrees of its neighbors, potentially freeing them up next. If the graph is a DAG, this process empties it; if a cycle exists, some vertices will never reach in-degree 0.

The second approach uses **depth-first search**: run DFS on the graph, and each time you *finish* exploring a vertex (all its descendants are done), prepend it to the output list. The result is a valid topological order because finishing u after all of u's successors means u naturally lands before all of them when the list is reversed. This DFS-based approach is the foundation of the next topic in this sequence and appears in many advanced graph algorithms. Both methods run in O(V + E) time, making topological sort efficient even on large dependency graphs.
