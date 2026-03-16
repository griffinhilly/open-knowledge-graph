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
stage: abstract-reasoning
status: draft
---

# Network Flow Models and Feasibility

## Core Idea
A flow network is a directed graph where each edge has a capacity, and a flow assigns values respecting capacity and flow conservation (inflow equals outflow at internal vertices). Network flows model routing, transportation, and resource distribution. Understanding feasibility and optimality is central to applied graph theory and combinatorial optimization.

## Explainer

You know from graph theory that a directed graph assigns a direction to each edge. A **flow network** adds two more ingredients: a **capacity** c(u,v) ≥ 0 on each directed edge (the maximum amount that can pass through), and a designated **source** s (where flow originates) and **sink** t (where flow terminates). A **flow** assigns a value f(u,v) to each edge satisfying two constraints: the flow on each edge cannot exceed its capacity (capacity constraint), and at every vertex except s and t, total inflow equals total outflow (conservation constraint). The network is like a system of pipes — each pipe has a maximum throughput, and what flows into any junction must equal what flows out.

Think of a city's road network during rush hour, with a highway on-ramp as the source and a downtown parking garage as the sink. Each road segment has a capacity measured in cars per hour. The conservation law models the physical reality that cars don't teleport or multiply — every car that enters an intersection must leave it. A valid flow describes one feasible traffic assignment; different valid flows route the traffic differently but all respect the road capacities.

The **value** of a flow is the total amount leaving the source (equivalently, the total arriving at the sink — conservation ensures these are equal). A feasible flow with value 0 always exists (send nothing). The interesting questions are about maximizing flow value and about the structure of maximum flows. The **max-flow min-cut theorem** (which you'll encounter next) says the maximum flow value equals the minimum capacity of any **cut** — a partition of vertices into S (containing s) and T (containing t) where the cut capacity is the sum of capacities of edges crossing from S to T. This duality between flows and cuts is one of the deepest results in combinatorial optimization.

Network flows appear throughout computing and operations research: routing packets in a communication network, assigning workers to jobs (bipartite matching is a special case), scheduling project tasks with resource constraints, and supply chain logistics. The framework unifies these seemingly different problems under one set of mathematical tools, making flow networks one of the most practically useful structures in all of graph theory.
