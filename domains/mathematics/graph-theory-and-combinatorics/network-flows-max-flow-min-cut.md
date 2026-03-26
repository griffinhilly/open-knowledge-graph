---
id: network-flows-max-flow-min-cut
title: Network Flows and the Max-Flow Min-Cut Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
builds-toward:
- menger-theorem
tags:
- network-flows
- max-flow-min-cut
- optimization
stage: formal-systems
status: validated
---

# Network Flows and the Max-Flow Min-Cut Theorem

## Core Idea
A flow on a directed graph assigns values to edges respecting capacity constraints and flow conservation. The max-flow min-cut theorem proves that the maximum flow value equals the minimum cut capacity, a fundamental min-max result with applications to matching, connectivity, and scheduling.

## How It's Best Learned
Implement the Ford–Fulkerson method or Edmonds–Karp algorithm, watching augmenting paths progressively increase the flow. Verify that the final flow equals the minimum cut capacity.

## Common Misconceptions
- Thinking flow conservation applies at the source and sink (it does not; they are special).
- Assuming every augmenting path yields the same final flow value (the max-flow value is unique, but augmenting paths are not).

## Questions

```yaml
- question: "Ford-Fulkerson finds an augmenting path and pushes maximum flow along it. A student says: 'Since we push greedily along each path, the first augmenting path we find largely determines the final flow value.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing — the first augmenting path always determines the maximum flow"
    - "The algorithm only pushes one unit of flow per path, so the first path is irrelevant"
    - "The final max-flow value is unique, but backward edges in the residual graph let later augmenting paths reroute flow from suboptimal early choices"
    - "Ford-Fulkerson does not use augmenting paths — it finds minimum cuts directly"
  answer: 2
  explanation: "The maximum flow value is unique, but the set of augmenting paths used to reach it is not. Backward edges in the residual graph allow the algorithm to 'undo' flow committed along an earlier suboptimal path by routing flow backward along a previous edge. This rerouting capacity is what guarantees correctness regardless of path-selection order — without backward edges, greedy path selection could get stuck."

- question: "The capacity of a cut (S, T) in a flow network is defined as:"
  type: multiple-choice
  options:
    - "The sum of capacities of all edges with both endpoints in S or both in T"
    - "The sum of capacities of all edges crossing between S and T in either direction"
    - "The sum of capacities of edges directed from S to T only — backward edges from T to S are excluded"
    - "The minimum capacity among all edges incident to the source s"
  answer: 2
  explanation: "Cut capacity counts only forward edges (S → T), not backward edges (T → S). This asymmetry is essential: flow can only travel from s to t by crossing the cut in the forward direction. Edges going T → S don't constrain the flow — in fact, flow on such edges reduces the net flow across the cut, so they're irrelevant to the upper bound. Forgetting this asymmetry is a common error when computing cut capacities by hand."

- question: "When Ford-Fulkerson terminates with no remaining augmenting paths, the flow value achieved exactly equals the minimum cut capacity — this is a tight equality, not merely an upper bound."
  type: true-false
  answer: true
  explanation: "True. This is the Max-Flow Min-Cut Theorem. Any cut gives an upper bound on the flow; the minimum cut gives the tightest such bound; and when Ford-Fulkerson terminates, it achieves exactly that value. The vertices reachable from s in the final residual graph form one side of a minimum cut, and the flow through the corresponding forward edges equals their full capacity. The equality is tight — there is no gap between the maximum flow and the minimum cut."

- question: "Flow conservation requires that total flow in equals total flow out at most vertex in the network, including the source and the sink."
  type: true-false
  answer: false
  explanation: "False. Flow conservation applies at every vertex EXCEPT the source (s) and sink (t). The source has net outflow — flow originates there without arriving — and the sink has net inflow — flow terminates there without leaving. These net amounts are equal and define the value of the flow. Applying conservation to s and t would make any non-zero flow impossible, which is exactly the opposite of the point."

- question: "Explain why backward edges in the residual graph are necessary, and what would go wrong if Ford-Fulkerson only allowed augmenting paths along forward edges."
  type: short-answer
  answer: "Backward edges allow the algorithm to reroute previously committed flow. If only forward edges were used, an early suboptimal path choice — for example, routing through an edge that blocks a higher-capacity alternative path — could not be corrected. The algorithm would terminate with a suboptimal flow, unable to reach the true maximum. Backward edges represent residual capacity to 'cancel' flow on an edge, effectively allowing flow to be rerouted through alternative paths, which guarantees the algorithm always converges to the true maximum regardless of path selection order."
  explanation: "The key insight is that backward edges encode the freedom to change your mind. A backward edge of capacity f on edge (u,v) means you can reduce the flow on (u,v) by up to f units — the algorithmic equivalent of rerouting. Without this, Ford-Fulkerson would be a greedy algorithm with no backtracking, and greedy algorithms on network flow problems are provably suboptimal in general. The backward edges are what elevate it from a heuristic to an exact algorithm."
```

## Explainer

From your work with directed graphs, you know that edges have direction. A **flow network** adds two more pieces of structure: every edge has a **capacity** (an upper limit on how much can flow through it), and there are two special vertices — a **source** s where flow originates and a **sink** t where flow terminates. A **flow** is an assignment of a nonneg value to each edge satisfying two rules: (1) **capacity constraint** — the flow on each edge cannot exceed its capacity; and (2) **flow conservation** — for every vertex except s and t, the total flow in equals the total flow out. The **value** of the flow is the net flow leaving s (equivalently, arriving at t).

The central question is: what is the maximum flow you can push from s to t? The **Ford-Fulkerson method** answers this iteratively. Build a **residual graph**: for each edge with capacity c carrying flow f, add a forward edge with residual capacity c − f (room to add more flow) and a backward edge with capacity f (flow that can be "undone"). Find any **augmenting path** from s to t in the residual graph — a path with positive residual capacity on every edge. Push as much flow as possible along that path (the bottleneck capacity). Repeat until no augmenting path exists. The backward edges are the clever part: they allow the algorithm to "reroute" previously committed flow, correcting suboptimal early choices.

A **cut** is a partition of vertices into two sets S (containing s) and T (containing t). The **capacity** of a cut is the total capacity of edges going from S to T (forward edges only; backward edges don't count). Any cut capacity gives an upper bound on the flow: you cannot push more flow from s to t than can cross any dividing line. The **Max-Flow Min-Cut Theorem** is the deep result: the maximum flow value exactly equals the minimum cut capacity. When Ford-Fulkerson terminates — no augmenting path remains — the vertices reachable from s in the residual graph form one side of a minimum cut. The equality is not just a bound; it is tight.

The theorem is a celebrated example of a **min-max duality**: a maximization problem (max flow) equals a minimization problem (min cut). This pattern appears throughout combinatorics and optimization. Immediate applications include maximum bipartite matching (via a flow construction), the maximum number of edge-disjoint paths between two vertices (equal to the min cut, by Menger's theorem), and resource scheduling problems where bottlenecks are cuts. Whenever you have a system where something flows through a network with capacity limits, the max-flow min-cut theorem tells you exactly where the bottleneck is.
