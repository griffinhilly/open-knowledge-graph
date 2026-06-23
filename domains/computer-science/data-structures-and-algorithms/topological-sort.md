---
id: topological-sort
title: Topological Sort
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: depth-first-search
  type: hard
- id: graph-adjacency-list-matrix-representations
  type: soft
- id: graph-connectivity
  type: soft
- id: breadth-first-search
  type: soft
- id: graph-depth-first-search-applications
  type: hard
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

## Questions

```yaml
- question: "You run a topological sort algorithm on a directed graph and observe that Kahn's algorithm terminates with only 4 of the 6 nodes placed in the output. What can you conclude?"
  type: multiple-choice
  options:
    - "The graph has a valid topological ordering, but the algorithm made an error"
    - "The graph contains a cycle involving the 2 nodes not in the output"
    - "The graph is disconnected and the 2 missing nodes are in a separate component"
    - "The algorithm needs to be restarted from a different source node"
  answer: 1
  explanation: "In Kahn's algorithm, nodes are placed in the output only when their in-degree drops to zero — meaning all their prerequisites have been processed. If the algorithm terminates early, it means the remaining nodes each have at least one unprocessed prerequisite, which can only happen if they form a cycle (each node waiting for another in the cycle). Kahn's algorithm is a cycle detector precisely because of this: if output size < total nodes, a cycle exists."

- question: "For the dependency graph A → C, B → C, B → D, A → D, which of the following is a valid topological ordering?"
  type: multiple-choice
  options:
    - "C, D, A, B"
    - "A, C, B, D"
    - "A, B, C, D"
    - "B, D, A, C"
  answer: 2
  explanation: "A valid topological ordering requires every node to appear before all nodes it points to. A → C means A must precede C; B → C means B must precede C; A → D means A must precede D; B → D means B must precede D. Option C (A, B, C, D) works: A before C ✓, A before D ✓, B before C ✓, B before D ✓. Option A fails because C appears before A and B, which are its prerequisites. Note that option C is not the only valid ordering — B, A, C, D and B, A, D, C also work, illustrating that topological sort is not unique."

- question: "A DAG with 5 nodes can have more than one valid topological ordering."
  type: true-false
  answer: true
  explanation: "Topological sort is not unique unless the graph is a single chain (each node has exactly one prerequisite). Whenever two nodes have no dependency relationship between them, either can appear first in a valid ordering. The number of valid orderings can be exponentially large for sparse graphs. Both the DFS-based algorithm and Kahn's algorithm produce one valid ordering, but the choice depends on traversal order — different orderings of the input can yield different valid topological sorts."

- question: "A graph with a directed cycle has multiple valid topological orderings, since you can start the cycle at different points."
  type: true-false
  answer: false
  explanation: "A graph with any directed cycle has no valid topological ordering at all — not multiple orderings, zero orderings. A topological ordering requires every edge u → v to have u before v. In a cycle A → B → C → A, we need A before B, B before C, and C before A simultaneously — a contradiction. No linear ordering can satisfy all three constraints. Topological sort is defined only for DAGs (directed acyclic graphs)."

- question: "How does Kahn's algorithm naturally detect that a graph contains a cycle, without any explicit cycle-checking code?"
  type: short-answer
  answer: "Kahn's algorithm only enqueues nodes when their in-degree reaches zero — meaning all their predecessors have been processed. In a cycle, every node in the cycle has at least one predecessor that is also in the cycle, so no node in the cycle ever reaches in-degree zero. The algorithm empties its queue while these nodes remain unprocessed. After the algorithm finishes, if the output contains fewer nodes than the graph, the missing nodes must be in a cycle."
  explanation: "This is one of Kahn's algorithm's most elegant properties: cycle detection emerges automatically from the queue logic, with no additional bookkeeping. In contrast, the DFS-based algorithm requires explicit tracking of nodes currently on the recursion stack (gray nodes) to detect back edges, which indicate cycles. For applications where cycle detection matters — build systems, package managers, dependency validators — Kahn's approach can be more straightforward to implement correctly."
```

## Explainer

You already understand directed graphs and depth-first search. Now consider a practical problem: you have a list of tasks, and some tasks must be completed before others. Course prerequisites are a perfect example — you cannot take Data Structures before Introduction to Programming. **Topological sort** takes a directed acyclic graph (DAG) of such dependencies and produces a linear ordering where every task appears after all of its prerequisites. It answers the question: "in what order can I do everything, respecting all the constraints?"

The **DFS-based algorithm** leverages a property you know from depth-first search: when DFS finishes processing a node (all its descendants have been fully explored), that node has no unvisited dependencies remaining in its subtree. By recording each node's **finish time** — the moment DFS completes it — and then reversing the order, you get a valid topological sort. Intuitively, nodes that other nodes depend on will finish later in DFS (because DFS must first finish all their descendants), so reversing finish order places prerequisites first. In practice, you push each node onto a stack when DFS finishes it, then pop the stack to get the sorted order.

**Kahn's algorithm** takes the opposite approach: instead of going deep, it works from the "outside in." Start by finding all nodes with **in-degree zero** — nodes that have no prerequisites. These can safely go first. Add them to a queue, and for each one you process, remove its outgoing edges (decrement the in-degree of its neighbors). Any neighbor whose in-degree drops to zero gets added to the queue. Repeat until the queue is empty. The order in which nodes are dequeued is a valid topological sort. A powerful bonus: if the queue empties before all nodes are processed, the remaining nodes are part of a cycle, so Kahn's algorithm doubles as a cycle detector.

Both algorithms run in **O(V + E)** time — linear in the size of the graph — because each vertex and edge is processed exactly once. The choice between them is mostly stylistic: DFS-based is natural when you already have DFS infrastructure, while Kahn's is often easier to reason about and naturally yields cycle detection. Topological sort is foundational beyond course scheduling. Build systems like Make use it to determine compilation order. Package managers use it to resolve installation dependencies. Spreadsheet engines use it to determine cell recalculation order. And in algorithm design, topological sort enables efficient dynamic programming on DAGs — once you have a valid ordering, you can process nodes left to right, and every node's dependencies are guaranteed to have been computed already.
