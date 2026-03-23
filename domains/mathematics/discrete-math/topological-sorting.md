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
stage: formal-systems
status: validated
---
# Topological Sorting and Ordering

## Core Idea
Topological sorting arranges vertices of a directed acyclic graph (DAG) in a linear order such that for every directed edge from u to v, u comes before v. This ordering is useful for scheduling tasks with dependencies, resolving symbol dependencies in compilers, and determining precedence.

## Questions

```yaml
- question: "A project scheduler models task dependencies as a directed graph: task A depends on B and C; B and C both depend on D; D has no dependencies. Which execution order is valid?"
  type: multiple-choice
  options:
    - "A, B, C, D"
    - "D, B, C, A"
    - "B, A, D, C"
    - "D, A, B, C"
  answer: 1
  explanation: "A valid topological order must place every dependency before the task that requires it. D must come first (no prerequisites), then B and C (both need D), then A (needs B and C). Options A and C put A or B before D, violating the dependency constraints. Option D places A before B and C, which also violates the constraints."

- question: "You run Kahn's algorithm on a directed graph. After the algorithm terminates, several vertices were never added to the output sequence. What does this imply?"
  type: multiple-choice
  options:
    - "The graph has multiple valid topological orderings"
    - "Some vertices have no outgoing edges"
    - "The graph contains a directed cycle"
    - "The graph is disconnected"
  answer: 2
  explanation: "In Kahn's algorithm, a vertex enters the queue only when its in-degree reaches 0 (all its prerequisites are satisfied). A vertex in a cycle can never reach in-degree 0, because other cycle members — which also never get processed — still point to it. If the algorithm exits with unprocessed vertices, those vertices are part of one or more cycles. This makes cycle detection a natural byproduct of topological sort: failure to produce a complete ordering proves a cycle exists."

- question: "A directed graph that contains a cycle cannot have a valid topological ordering."
  type: true-false
  answer: true
  explanation: "A topological ordering requires that for every edge u → v, u appears before v in the sequence. In a cycle A → B → C → A, A must come before B, B before C, and C before A — which means A must come before itself. No linear sequence can satisfy this. The existence of any cycle makes topological sorting impossible, which is why topological sort is defined only for DAGs (directed acyclic graphs)."

- question: "Every directed graph has at least one valid topological ordering."
  type: true-false
  answer: false
  explanation: "Only directed acyclic graphs (DAGs) admit a topological ordering. Any graph with a directed cycle has no valid topological ordering, because a cycle creates a requirement that some vertex appear before itself in the sequence — an impossibility. The existence of a topological ordering is equivalent to the graph being a DAG."

- question: "Why does Kahn's algorithm detect cycles as a side effect of performing topological sorting?"
  type: short-answer
  answer: "Kahn's algorithm processes vertices greedily by in-degree: any vertex with in-degree 0 is ready to be placed next, and removing it decrements the in-degrees of its neighbors. Vertices in a cycle can never reach in-degree 0 because they always have an unprocessed predecessor inside the cycle pointing to them. If the algorithm finishes with vertices remaining (output count < total vertices), those leftover vertices must be part of cycles — their prerequisites were never satisfied because some prereq was also waiting for them."
  explanation: "This is the key insight linking topological sort to cycle detection: a successful topological sort and the absence of directed cycles are logically equivalent properties of a directed graph. Both Kahn's algorithm and the DFS-based approach exploit this equivalence, making them useful not just for ordering but for validating that a dependency graph is well-formed."
```

## Explainer

You already know that a **directed acyclic graph** (DAG) models dependencies: an edge from u to v means "u must come before v." A **topological sort** turns that partial ordering into a total ordering — a single linear sequence where all the "must come before" constraints are respected. The everyday analogy is a college degree plan: courses have prerequisites, and a valid course schedule is a topological sort of the prerequisite DAG.

The key reason topological sorts only exist for DAGs is intuitive: if the graph contained a directed cycle (A → B → C → A), then A would need to come before itself, which is impossible in any linear order. This makes cycle detection a natural companion to topological sorting — if you try to sort a graph and fail, you've found a cycle.

There are two standard algorithms. **Kahn's algorithm** works by repeatedly identifying vertices with no incoming edges (no remaining prerequisites) and removing them one at a time, adding each to the output sequence. Any vertex with in-degree 0 is "safe to go first" given what remains. When you remove a vertex, you decrement the in-degrees of its neighbors, potentially freeing them up next. If the graph is a DAG, this process empties it; if a cycle exists, some vertices will never reach in-degree 0.

The second approach uses **depth-first search**: run DFS on the graph, and each time you *finish* exploring a vertex (all its descendants are done), prepend it to the output list. The result is a valid topological order because finishing u after all of u's successors means u naturally lands before all of them when the list is reversed. This DFS-based approach is the foundation of the next topic in this sequence and appears in many advanced graph algorithms. Both methods run in O(V + E) time, making topological sort efficient even on large dependency graphs.
