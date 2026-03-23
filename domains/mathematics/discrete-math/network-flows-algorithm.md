---
id: network-flows-algorithm
title: 'Network Flows: Maximum Flow and Minimum Cut'
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-matching-halls-theorem
  type: soft
tags:
- graph-theory
- flows
stage: formal-systems
status: validated
---

# Network Flows: Maximum Flow and Minimum Cut

## Core Idea
In a flow network, edges have capacity constraints and carry flow values. A maximum flow is the largest total flow from source to sink. The max-flow min-cut theorem states that the maximum flow equals the minimum capacity of any cut separating source from sink.

## Questions

```yaml
- question: "You find a flow in a network with value 12. You also identify a cut of capacity 12. What can you conclude?"
  type: multiple-choice
  options:
    - "The flow might be improvable; you need to keep running Ford-Fulkerson"
    - "The flow is maximum and the cut is minimum — each is a certificate proving the other"
    - "The cut capacity gives a lower bound, so the maximum flow could be higher than 12"
    - "You have confirmed the flow is feasible, but optimality requires checking all cuts"
  answer: 1
  explanation: "By the max-flow min-cut theorem, maximum flow = minimum cut capacity. Finding a flow of value 12 and a cut of capacity 12 simultaneously certifies both: the flow cannot be improved (every cut gives an upper bound, and this cut equals 12), and no cut smaller than 12 exists (a flow of 12 was achieved, so every cut must be at least 12). The two together constitute a proof of optimality requiring no further computation."

- question: "What is the purpose of backward edges in the residual graph during Ford-Fulkerson?"
  type: multiple-choice
  options:
    - "They represent unused capacity in the original forward direction"
    - "They allow the algorithm to undo and reroute earlier flow assignments that turned out to be suboptimal"
    - "They indicate edges where the original graph allows bidirectional flow"
    - "They are only generated when the source and sink are disconnected"
  answer: 1
  explanation: "A backward edge with capacity f(e) on an edge where f(e) units of flow have been sent allows the algorithm to 'cancel' up to f(e) units of that earlier flow — effectively rerouting it along a different path. Without backward edges, Ford-Fulkerson could get stuck with suboptimal local routing and fail to reach the true maximum. Backward edges are what allow the algorithm to correct greedy decisions made in earlier iterations."

- question: "In a flow network, a cut of small capacity provides a lower bound on the maximum possible flow."
  type: true-false
  answer: false
  explanation: "Cuts provide upper bounds, not lower bounds. Every cut separates source from sink, so every unit of flow must cross the cut — meaning the flow value cannot exceed the cut capacity. A minimum cut gives the tightest upper bound, which by the max-flow min-cut theorem equals the maximum flow. A valid flow of known value provides a lower bound."

- question: "When Ford-Fulkerson terminates — finding no augmenting path in the residual graph — the current flow value is guaranteed to equal the capacity of some cut in the network."
  type: true-false
  answer: true
  explanation: "When no augmenting path exists, the set of nodes reachable from the source in the residual graph forms set S of a cut (S, T). The edges from S to T in the original graph are all fully saturated (no residual capacity forward), and this cut's capacity equals the current flow value. This is the constructive proof of the max-flow min-cut theorem: termination of Ford-Fulkerson and the min-cut condition are the same event."

- question: "Why is the max-flow min-cut theorem described as providing a 'certificate of optimality'? What two things does it simultaneously produce, and why does that matter?"
  type: short-answer
  answer: "It simultaneously produces (1) a flow achieving the maximum value and (2) a cut proving that no larger flow is possible. The flow is the constructive witness; the cut is the impossibility proof. Together they certify optimality without requiring exhaustive search — you don't need to check all possible flows, because the cut proves that the achieved value is an upper bound, and the flow proves that upper bound is attained."
  explanation: "This duality is computationally valuable: you can verify a maximum flow in polynomial time just by exhibiting a cut of equal capacity. It also unifies matching and flow problems — a maximum bipartite matching and its certificate of optimality (Hall's condition violation) correspond exactly to a max flow and its min cut."
```

## Explainer

Imagine water flowing through a network of pipes from a **source** (where water enters) to a **sink** (where it exits). Each pipe has a **capacity** — a maximum amount it can carry. You want to push as much total flow as possible from source to sink while respecting every capacity constraint. This is the maximum flow problem, and it sits at the intersection of graph theory, linear programming, and combinatorial optimization.

A **flow** assigns a non-negative value f(e) to each edge e, subject to two rules: (1) capacity constraints — f(e) ≤ cap(e) for every edge, and (2) flow conservation — for every internal node (not source or sink), the total flow in equals the total flow out. The **value** of a flow is the total amount leaving the source. The problem is to find a flow of maximum value. The algorithmic workhorse is **Ford-Fulkerson**: repeatedly find an **augmenting path** — a path from source to sink with remaining capacity on every edge — and push more flow along it. The process terminates when no augmenting path exists, at which point the flow is maximum. The **residual graph** tracks remaining capacity on forward edges and the possibility of "un-sending" flow on backward edges, which is what allows the algorithm to correct earlier suboptimal routing decisions.

The deep structural result is the **max-flow min-cut theorem**: the maximum value of any flow equals the minimum capacity of any **cut**. A cut is a partition of the vertices into two sets S (containing the source) and T (containing the sink); its capacity is the total capacity of edges going from S to T. Every cut imposes an upper bound on all flows (you can only send as much as crosses the cut), and the theorem says the tightest of these bounds is actually achievable. Ford-Fulkerson terminates precisely when it has found a flow equal to the minimum cut, providing a simultaneous certificate of optimality: here is the flow achieving the maximum, and here is the cut proving no larger flow is possible.

Network flow has immediate practical applications. If you've studied Hall's theorem for bipartite matching (your prerequisite), you can see bipartite matching as a special flow problem: add a source connected to all left vertices, connect all right vertices to a sink, and assign all edges capacity 1. A maximum matching corresponds exactly to a maximum flow, and Hall's condition corresponds to the min-cut condition. This unification is one of the most elegant aspects of combinatorial optimization — many seemingly different problems (matching, assignment, transportation, scheduling) are all instances of the same flow framework, and fast flow algorithms solve them all.
