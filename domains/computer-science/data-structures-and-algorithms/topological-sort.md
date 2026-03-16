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
- id: breadth-first-search
  type: soft
builds-toward:
- dynamic-programming-intro
tags:
- topological-sort
- DAG
- ordering
- dependencies
stage: formal-systems
status: validated
---
# Topological Sort

## Core Idea
Topological sort produces a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge u → v, u appears before v. It is only possible for DAGs — any graph with a cycle has no valid topological ordering. Two standard algorithms are DFS-based (append each node to a result stack on DFS finish, then reverse) and Kahn's algorithm (iteratively remove nodes with in-degree zero using a queue). Topological sort is essential for scheduling problems, build systems, and resolving dependency chains.

## How It's Best Learned
Implement both the DFS-based approach and Kahn's algorithm. Apply both to a concrete dependency problem such as course prerequisite ordering. Verify that Kahn's algorithm detects cyclic graphs by checking whether all nodes appear in the output.

## Common Misconceptions
- Topological sort is not unique; a DAG can have many valid orderings.
- A graph with cycles has no topological ordering; Kahn's algorithm detects this naturally, while the DFS-based approach requires explicit cycle detection.

## Explainer

You already understand directed graphs and depth-first search. Now consider a practical problem: you have a list of tasks, and some tasks must be completed before others. Course prerequisites are a perfect example — you cannot take Data Structures before Introduction to Programming. **Topological sort** takes a directed acyclic graph (DAG) of such dependencies and produces a linear ordering where every task appears after all of its prerequisites. It answers the question: "in what order can I do everything, respecting all the constraints?"

The **DFS-based algorithm** leverages a property you know from depth-first search: when DFS finishes processing a node (all its descendants have been fully explored), that node has no unvisited dependencies remaining in its subtree. By recording each node's **finish time** — the moment DFS completes it — and then reversing the order, you get a valid topological sort. Intuitively, nodes that other nodes depend on will finish later in DFS (because DFS must first finish all their descendants), so reversing finish order places prerequisites first. In practice, you push each node onto a stack when DFS finishes it, then pop the stack to get the sorted order.

**Kahn's algorithm** takes the opposite approach: instead of going deep, it works from the "outside in." Start by finding all nodes with **in-degree zero** — nodes that have no prerequisites. These can safely go first. Add them to a queue, and for each one you process, remove its outgoing edges (decrement the in-degree of its neighbors). Any neighbor whose in-degree drops to zero gets added to the queue. Repeat until the queue is empty. The order in which nodes are dequeued is a valid topological sort. A powerful bonus: if the queue empties before all nodes are processed, the remaining nodes are part of a cycle, so Kahn's algorithm doubles as a cycle detector.

Both algorithms run in **O(V + E)** time — linear in the size of the graph — because each vertex and edge is processed exactly once. The choice between them is mostly stylistic: DFS-based is natural when you already have DFS infrastructure, while Kahn's is often easier to reason about and naturally yields cycle detection. Topological sort is foundational beyond course scheduling. Build systems like Make use it to determine compilation order. Package managers use it to resolve installation dependencies. Spreadsheet engines use it to determine cell recalculation order. And in algorithm design, topological sort enables efficient dynamic programming on DAGs — once you have a valid ordering, you can process nodes left to right, and every node's dependencies are guaranteed to have been computed already.
