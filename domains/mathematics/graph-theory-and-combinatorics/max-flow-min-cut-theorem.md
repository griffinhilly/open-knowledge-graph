---
id: max-flow-min-cut-theorem
title: Max-Flow Min-Cut Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: network-flows
  type: hard
builds-toward:
- mengers-theorem
tags:
- graph-theory
- flows
- optimization
stage: advanced
status: validated
---

# Max-Flow Min-Cut Theorem

## Core Idea
The Max-Flow Min-Cut Theorem states that the maximum flow from source to sink equals the minimum capacity of any cut separating them. This powerful result provides both a theoretical characterization and a practical algorithm for solving flow problems.

## How It's Best Learned
Work through small networks by hand, computing flows and cuts to see the equality in action. Use the Ford-Fulkerson method to incrementally build flows.

## Common Misconceptions
A cut's capacity is the sum of edge capacities crossing it, not the number of edges. Minimum cut is not the cut with fewest edges, but minimum total capacity.

## Questions

```yaml
- question: "In a network, the S-side of a cut sends three forward edges to the T-side with capacities 5, 3, and 7. Two backward edges run from T-side to S-side with capacities 4 and 2. What is the capacity of this cut?"
  type: multiple-choice
  options:
    - "21 — the sum of all crossing edges in both directions"
    - "15 — the sum of forward edges only (5 + 3 + 7)"
    - "9 — the sum of backward edges, since they limit how much can return"
    - "6 — the minimum capacity among the forward edges"
  answer: 1
  explanation: "The capacity of a cut is the total capacity of edges directed from S to T — forward edges only. Backward edges (T to S) do not count toward the cut capacity; they can carry flow back from T to S, which would reduce the net flow but does not add to the bottleneck. This is one of the most common errors: including backward edges makes cuts appear larger than they are and breaks the max-flow min-cut equality."

- question: "The Max-Flow Min-Cut Theorem guarantees that for any network with a source and sink:"
  type: multiple-choice
  options:
    - "The maximum flow is at most the minimum cut capacity (a one-sided bound)"
    - "The maximum flow value equals the minimum cut capacity exactly — these two quantities are always the same"
    - "Every cut has the same capacity as the maximum flow"
    - "The minimum cut always contains the fewest edges of any cut separating source from sink"
  answer: 1
  explanation: "The theorem proves exact equality — not just that max flow ≤ min cut (which is easy, the 'weak duality'), but that max flow = min cut. This is the strong result. Option A (one-sided bound) is true but weaker. Option C confuses minimum cut with all cuts. Option D is the classic misconception: minimum cut means minimum total capacity, not fewest edges — a cut with two edges of capacity 100 each has more capacity than one with ten edges of capacity 1 each."

- question: "When the Ford-Fulkerson algorithm terminates with no augmenting path remaining, every forward edge from the source-reachable vertex set S to the non-reachable set T in the residual graph must be fully saturated."
  type: true-false
  answer: true
  explanation: "This is the key step in the proof. If any forward edge from S to T were not fully saturated, its residual capacity would be positive, meaning the endpoint in T would be reachable from the source — contradicting the definition of T as the non-reachable set. Full saturation of all S-to-T forward edges (and zero flow on all T-to-S backward edges) is precisely what makes the current flow equal to the capacity of this cut, proving max flow = min cut."

- question: "The minimum cut in a network is the cut that separates source from sink using the fewest edges."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about min-cut. The minimum cut minimizes total capacity — the sum of capacities of forward edges crossing the cut — not the number of edges. A single edge with capacity 1000 has more cut capacity than a thousand edges of capacity 1 each. Confusing 'minimum capacity' with 'fewest edges' leads to incorrect identification of bottlenecks and wrong max-flow values."

- question: "Explain why the Max-Flow Min-Cut Theorem proves that augmenting-path algorithms like Ford-Fulkerson find the true maximum flow when they terminate."
  type: short-answer
  answer: "When no augmenting path remains, define S as all vertices reachable from the source in the residual graph. The sink must be in T = V\\S. Every forward edge from S to T is fully saturated (otherwise its endpoint would be reachable), and every backward edge from T to S carries zero flow (otherwise its tail would be reachable). The current flow therefore equals the capacity of this S-T cut exactly. Since any flow ≤ any cut capacity (weak duality), and this flow equals a specific cut capacity, the flow is maximum and this cut is minimum."
  explanation: "The proof is constructive: when Ford-Fulkerson stops, it simultaneously certifies optimality and exhibits a minimum cut. You don't need to check all cuts — the algorithm's termination state defines the min cut for you. This is the power of the theorem: it converts a 'no more augmenting paths' stopping condition into a proof of global optimality."
```

## Explainer

From your study of network flows, you know that a **flow** assigns a value to each edge — respecting capacity constraints and conservation (flow in = flow out at every internal vertex). The value of a flow is the total amount leaving the source. You also know that you can push flow along augmenting paths to increase the total flow. The Max-Flow Min-Cut Theorem provides the theoretical foundation for why augmenting path algorithms actually find the maximum: they stop precisely when the flow equals the minimum cut.

A **cut** is a partition of all vertices into two sets: S, containing the source, and T, containing the sink. Every path from source to sink must cross from S to T at least once. The **capacity of the cut** is the total capacity of edges going from S to T (forward edges only — backward edges from T to S do not count). This immediately implies that any flow ≤ any cut capacity: the flow must pass through the cut's forward edges, and can never exceed their combined capacity. This "weak duality" is easy to see — any cut gives an upper bound on the maximum flow.

The remarkable result is that these two quantities are not just bounded together — they are **equal**: max flow = min cut. The proof uses the idea of residual capacity. When Ford-Fulkerson terminates (no augmenting paths remain), define S as all vertices reachable from the source in the residual graph. Then T = V \ S contains the sink (otherwise there would be an augmenting path). Every forward edge from S to T must be fully saturated (otherwise the endpoint in T would be reachable), and every backward edge from T to S must carry zero flow (otherwise the tail in S would be reachable). Therefore the current flow value exactly equals the capacity of the S-T cut — proving equality.

The theorem is one of the great duality results in combinatorics and optimization. It connects two seemingly different questions — "how much can flow from source to sink?" and "what is the bottleneck in the network?" — and shows they have the same answer. Applications are wide-ranging: maximum matching in bipartite graphs reduces to max-flow (finding the minimum vertex cover equals the maximum matching, by König's theorem, which is itself a consequence of max-flow min-cut). Network reliability, airline scheduling, image segmentation, and supply chain optimization all use this theorem. Whenever you want to maximize throughput through a constrained network, or find the minimum set of resources to disrupt a network, the Max-Flow Min-Cut Theorem is the underlying guarantee that your algorithm will find the exact answer.
