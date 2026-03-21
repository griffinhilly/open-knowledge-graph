---
id: network-flows
title: Network Flow Models and Feasibility
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
builds-toward:
- max-flow-min-cut-theorem
- mengers-theorem
tags:
- graph-theory
- flows
- networks
stage: formal-systems
status: draft
---

# Network Flow Models and Feasibility

## Core Idea
A flow network is a directed graph where each edge has a capacity, and a flow assigns values respecting capacity and flow conservation (inflow equals outflow at internal vertices). Network flows model routing, transportation, and resource distribution. Understanding feasibility and optimality is central to applied graph theory and combinatorial optimization.

## Questions

```yaml
- question: "Which pair of constraints must every valid flow in a network satisfy?"
  type: multiple-choice
  options:
    - "Flow on each edge equals its capacity AND total flow into source equals total flow out of sink"
    - "Flow on each edge does not exceed its capacity AND inflow equals outflow at every internal vertex"
    - "Flow on each edge is positive AND at least one path from source to sink is fully saturated"
    - "Inflow equals outflow at every vertex including source and sink AND no cycles carry flow"
  answer: 1
  explanation: "A valid flow satisfies exactly two constraints: the capacity constraint (flow on each directed edge ≤ capacity of that edge) and the conservation constraint (inflow = outflow at every vertex except the source and sink). Option D is wrong because conservation does NOT apply at the source and sink — the source has net outflow and the sink has net inflow, which is the whole point. Option A incorrectly requires flow to equal capacity (that would be a saturating flow, not any valid flow)."

- question: "A flow network has a minimum cut with capacity 7. What is the maximum possible flow value from source to sink?"
  type: multiple-choice
  options:
    - "It cannot be determined without knowing the individual edge capacities"
    - "It must be exactly 7, by the max-flow min-cut theorem"
    - "It must be at least 7, since the cut is a lower bound"
    - "It is at most 7 but may be less depending on the network structure"
  answer: 1
  explanation: "The max-flow min-cut theorem is an exact equality: the maximum flow value equals the minimum cut capacity. If the min-cut is 7, then the max flow is exactly 7 — not 'at most' and not 'cannot be determined.' The minimum cut represents the tightest bottleneck separating source from sink; no flow can exceed it (any flow must cross every cut), and algorithms like Ford-Fulkerson show the maximum can always be achieved."

- question: "The maximum flow through a network can exceed the minimum cut capacity if the network has enough parallel paths from source to sink."
  type: true-false
  answer: false
  explanation: "No. Every flow must cross every cut — any path from source to sink crosses a cut at least once. The total flow across a cut cannot exceed the sum of capacities of edges crossing from the source side to the sink side. The minimum cut is the tightest such bottleneck, so it is an absolute upper bound on flow. The max-flow min-cut theorem says the maximum flow achieves this bound exactly, not that it merely approaches it."

- question: "A flow that sends zero units along every edge is always a valid feasible flow in any network."
  type: true-false
  answer: true
  explanation: "The zero flow trivially satisfies both constraints: every edge carries 0, which is ≤ any non-negative capacity, and inflow = outflow = 0 at every vertex. This makes it a valid feasible flow with value 0. It is not interesting or useful, but its existence guarantees that the feasibility problem always has a trivial solution. The non-trivial question is how to find a feasible flow with maximum value."

- question: "What does flow conservation mean in a network flow model, and why is it a necessary constraint for the model to represent real-world routing problems?"
  type: short-answer
  answer: "Flow conservation means that at every internal vertex (every node except source and sink), the total flow on incoming edges equals the total flow on outgoing edges. It is necessary because in any physical routing problem — traffic, data packets, water pipes, goods in supply chains — material doesn't spontaneously appear or disappear at intermediate nodes. What flows into a junction must flow out. Without conservation, the model could 'create' flow at intermediate nodes, making the computed flow meaningless for describing real systems."
  explanation: "Conservation is what gives network flows their power as models. It abstracts away the specifics of what is flowing and captures the universal constraint that resources are neither created nor destroyed in transit. The single exception — the source produces flow and the sink absorbs it — corresponds directly to the origin and destination in the real problem. This also means the value of a flow (total leaving source) must equal total entering sink, a consequence of conservation applied globally."
```

## Explainer

You know from graph theory that a directed graph assigns a direction to each edge. A **flow network** adds two more ingredients: a **capacity** c(u,v) ≥ 0 on each directed edge (the maximum amount that can pass through), and a designated **source** s (where flow originates) and **sink** t (where flow terminates). A **flow** assigns a value f(u,v) to each edge satisfying two constraints: the flow on each edge cannot exceed its capacity (capacity constraint), and at every vertex except s and t, total inflow equals total outflow (conservation constraint). The network is like a system of pipes — each pipe has a maximum throughput, and what flows into any junction must equal what flows out.

Think of a city's road network during rush hour, with a highway on-ramp as the source and a downtown parking garage as the sink. Each road segment has a capacity measured in cars per hour. The conservation law models the physical reality that cars don't teleport or multiply — every car that enters an intersection must leave it. A valid flow describes one feasible traffic assignment; different valid flows route the traffic differently but all respect the road capacities.

The **value** of a flow is the total amount leaving the source (equivalently, the total arriving at the sink — conservation ensures these are equal). A feasible flow with value 0 always exists (send nothing). The interesting questions are about maximizing flow value and about the structure of maximum flows. The **max-flow min-cut theorem** (which you'll encounter next) says the maximum flow value equals the minimum capacity of any **cut** — a partition of vertices into S (containing s) and T (containing t) where the cut capacity is the sum of capacities of edges crossing from S to T. This duality between flows and cuts is one of the deepest results in combinatorial optimization.

Network flows appear throughout computing and operations research: routing packets in a communication network, assigning workers to jobs (bipartite matching is a special case), scheduling project tasks with resource constraints, and supply chain logistics. The framework unifies these seemingly different problems under one set of mathematical tools, making flow networks one of the most practically useful structures in all of graph theory.
