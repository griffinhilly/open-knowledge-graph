---
id: rrt-prm-sampling-planners
title: RRT and PRM Sampling-Based Planners
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: motion-planning-algorithms
  type: hard
tags:
- rrt
- prm
- sampling-based-planning
- high-dimensional
- asymptotic-optimality
stage: expert
status: validated
---

# RRT and PRM Sampling-Based Planners

## Core Idea
Rapidly-exploring Random Trees (RRT) and Probabilistic Roadmaps (PRM) are sampling-based motion planning algorithms that handle high-dimensional configuration spaces by randomly sampling in C-space and building a graph of collision-free configurations. RRT grows a tree from the start toward the goal, greedily expanding toward random samples; it is single-query (good for one specific start-goal pair) and naturally anytime (returns feasible solutions quickly). PRM pre-builds a roadmap by sampling random collision-free configurations and connecting nearby ones; it is multi-query (answers many start-goal pairs with one roadmap) and asymptotically optimal (path length approaches optimal as sample count grows). Both methods avoid explicit C-space discretization and scale better to high dimensions than grid-based planners, though they provide probabilistic rather than guaranteed completeness.

## Questions

```yaml
- question: "An RRT planner is given 5 seconds to plan a path for a 6-DOF robot arm. After 1 second, it has found a feasible path from start to goal. What should the planner do with the remaining 4 seconds?"
  type: multiple-choice
  options:
    - "Stop and return the path immediately, because a feasible solution has been found"
    - "Continue sampling and tree expansion to find shorter and smoother paths, with anytime optimization"
    - "Restart with a different random seed to explore alternative paths"
    - "Switch to a deterministic planner like A* to refine the RRT solution"
  answer: 1
  explanation: "This distinction drives algorithmic choice in practice. Mobile robots in static environments favor PRM (build roadmap once per environment, then answer rapid goal queries). Robotic manipulators in semi-dynamic environments favor RRT (environment changes, rebuild on each plan request). Hybrid approaches use PRM for the mobile base and RRT for the arm, leveraging each algorithm's strength. The choice trades off single-query planning time against multi-query amortized cost."
```

## Explainer

As robot configuration spaces grow in dimensionality — a 7-DOF manipulator, a robot with redundant degrees of freedom for grasping — grid-based motion planning becomes intractable. A 7D grid with 100 cells per dimension requires 10^14 cells. Sampling-based methods circumvent this dimensionality curse by abandoning exhaustive discretization: instead of dividing space into cells, they randomly sample in C-space and connect samples that are collision-free and sufficiently close.

**Probabilistic Roadmaps (PRM)** work in two phases. Phase 1 (Learning): Sample N random configurations uniformly from C-space. For each sample, check collision-free. Discard collisions. Among the free samples, compute pairwise distances and connect each sample to its k-nearest neighbors (usually k=10-20) with straight-line paths, checking each connection for collision. The result is a graph (roadmap) whose nodes are free configurations and edges are collision-free paths. Phase 2 (Query): For a new (start, goal) pair, connect the start and goal to the roadmap, then use A* or Dijkstra to find a path in the graph.

The key insight is amortization. Building the roadmap is expensive (thousands of samples, collision checks for each sample and each potential edge connection). But once built, answering queries is cheap — just graph search. If you have 100 goal requests in the same environment, PRM pays the roadmap cost once and then answers all queries quickly. This makes PRM ideal for static environments where multiple goals are queried sequentially.

**RRT (Rapidly-Exploring Random Trees)** takes a different approach, more suited to single-query problems. RRT grows a tree from the start configuration toward the goal. At each iteration: (1) sample a random configuration in C-space; (2) find the nearest node in the existing tree; (3) extend from that node toward the sample by a fixed distance (step size); (4) if the extension is collision-free, add the new node to the tree. Repeat until a node reaches the goal or time expires. RRT is called "rapidly exploring" because random sampling efficiently fills high-dimensional space — better than grid-based methods which have dead zones. The algorithm is anytime: it quickly returns a feasible (not optimal) path, then continues improving if time permits.

**Why High Dimensions Matter**: In high dimensions, the volume of C-space explodes exponentially. But most of it is obstacle-free (in typical robotic workspaces). Random sampling uniformly samples this vast free space, with collision checks quickly filtering out the few bad samples. Grid-based planning tries to partition the space exhaustively, hitting exponential blowup. Sampling avoids this by exploiting the fact that we don't need to partition — we just need a representative set of free configurations.

**Asymptotic Optimality**: Basic RRT and PRM find any feasible path. Variants like RRT* and PRM* improve paths over time, with theoretical guarantees that path length approaches optimal as sample count increases. RRT* does this by rewiring the tree — after adding a new node, checking if the new node can provide shortcuts to existing nodes and updating parent pointers. This is more expensive per iteration but converges to optimal paths given sufficient time.

**Practical Trade-offs**: RRT and PRM are probabilistically complete — they find paths with probability approaching 1 as sample count increases, but for any finite sample count, they may miss a feasible path. In contrast, grid-based planning is resolution-complete (guaranteed to find paths of sufficient resolution). RRT and PRM excel when the grid would be too fine (high dimension, narrow passages); grid-based planning excels when feasibility or optimality guarantees are mandatory and dimensions are low (2D-4D).

**Hybrid Approaches**: Modern systems often combine methods. A mobile base plans using grid-based A* on a 2D occupancy map (fast, deterministic). A manipulator planning in high-dimensional joint space uses RRT or PRM. As dimensionality increases, sampling-based methods dominate — this is why high-dimensional robotic systems almost universally use RRT, PRM, or similar variants.

