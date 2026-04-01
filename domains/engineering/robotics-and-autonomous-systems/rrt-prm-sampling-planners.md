---
id: rrt-prm-sampling-planners
title: RRT and PRM Sampling-Based Planners
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: motion-planning-algorithms
  type: hard
builds-toward:
- trajectory-optimization
- reactive-control-feedback
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
  explanation: "RRT is an anytime algorithm: it quickly finds feasible (not optimal) paths, then continuously improves as more time is available. Continuing to sample and expand explores shortcuts and smoother trajectories. RRT* variants track the best path found so far and improve it with asymptotic optimality guarantees. Stopping immediately wastes available computation time and leaves a potentially long, winding path. Restarting or switching algorithms discards the work done and loses the anytime benefit. In robotics, anytime behavior is valuable because it provides a solution if interrupted but continues to optimize if time permits."

- question: "A PRM planner samples 5,000 random collision-free configurations and connects each to its k-nearest neighbors, building a roadmap. Later, query pairs (start, goal) use this same roadmap to find paths via A* on the graph. Is the roadmap reusable for a completely different environment with different obstacles?"
  type: multiple-choice
  options:
    - "Yes, as long as the configuration space dimensionality is the same"
    - "No, the roadmap is specific to the obstacles sampled during construction; a new environment requires a new roadmap"
    - "Yes, if the obstacles in the new environment are similar in volume and spacing"
    - "It depends on the value of k; if k is large enough, the roadmap is reusable"
  answer: 1
  explanation: "Each roadmap encodes connectivity within that specific environment's free space. When obstacles change, the free space changes, and paths valid in the old environment may become infeasible (collide with new obstacles). Sampling a new environment will sample a different free-space region. Reusing the old roadmap in a new environment is like using a subway map from London to navigate Tokyo — the topology is completely different. PRM's multi-query advantage is amortized over many (start, goal) pairs within the same environment, not across environments."

- question: "RRT-Connect grows two trees simultaneously — one from start, one from goal — and tries to connect them. This approach reduces planning time because it explores two smaller spaces instead of one large space."
  type: true-false
  answer: true
  explanation: "Correct. Bidirectional search (RRT-Connect) reduces the problem complexity. Each tree needs to explore only a partial path; they meet in the middle. For a 6D space, the effective exploration volume per tree is roughly half the original, which (due to exponential dimensionality effects) can dramatically reduce samples needed. Bidirectional search is especially effective in narrow-passage problems where single-tree RRT spends many samples exploring dead ends."

- question: "PRM guarantees probabilistic completeness: as the number of samples increases to infinity, the probability of finding a path (if one exists) approaches 1. However, for any finite sample count, there is no guarantee of finding a feasible path even if one exists."
  type: true-false
  answer: true
  explanation: "Correct. This is the trade-off of sampling-based methods. They don't guarantee finding paths in finite time, only that with enough samples, they eventually will. In practice, finite sample counts (1,000 to 10,000) are sufficient for moderate-dimensional problems, and paths are found with high probability. This contrasts with grid-based methods which are (in theory) resolution-complete — guaranteed to find a path with sufficient resolution — but require exponential grid refinement in high dimensions where sampling methods excel."

- question: "Explain the key difference between RRT and PRM in terms of when planning occurs, and discuss the implications for robotics applications where multiple goal targets are given sequentially."
  type: short-answer
  answer: "RRT is a single-query planner: it builds the tree on-demand for a specific (start, goal) pair. When a new goal arrives, planning restarts from scratch. PRM is a multi-query planner: it pre-builds a roadmap once, then answers multiple (start, goal) queries using graph search on the pre-built roadmap. For sequential goals (e.g., a delivery robot with many targets), PRM is more efficient — one roadmap construction overhead is amortized over many queries. For one-shot planning or dynamic environments where obstacles change, RRT is more practical because it avoids wasting time on roadmap regions never queried."
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

