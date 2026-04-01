---
id: motion-planning-algorithms
title: Motion Planning Algorithms and Path Finding
domain: engineering
course: robotics-and-autonomous-systems
prerequisites: []
builds-toward:
- rrt-prm-sampling-planners
- potential-field-methods
- trajectory-optimization
tags:
- motion-planning
- pathfinding
- configuration-space
- collision-avoidance
- autonomous-systems
stage: advanced
status: validated
---

# Motion Planning Algorithms and Path Finding

## Core Idea
Motion planning is the problem of computing a collision-free trajectory from a robot's current configuration to a goal configuration. The core algorithmic approach is to represent the robot's position and orientation as a point in configuration space (C-space), where each dimension is a degree of freedom. Obstacles become forbidden regions in this space. The problem becomes: find a path from the start point to the goal point in C-space that avoids forbidden regions. Classic algorithms include Dijkstra's shortest path (for discretized grids), A* (informed search with heuristics), and Breadth-First Search (for unweighted graphs). The choice of planning algorithm depends on whether the workspace is discretized into a grid, whether the robot has constraints (like bounded curvature), and whether optimal or merely feasible paths are needed.

## Questions

```yaml
- question: "A wheeled mobile robot must navigate from one room to another through a doorway. The robot's configuration space includes position (x, y) and orientation θ, making it 3D. The door is 1 meter wide. Which statement about C-space obstacles is correct?"
  type: multiple-choice
  options:
    - "The doorway in C-space is also 1 meter wide, because only position matters"
    - "The doorway in C-space is narrower than 1 meter because the robot's radius must be subtracted, and wider for some orientations if the robot is wider than it is long"
    - "The doorway is not visible in 3D C-space; it can only be analyzed in 2D by fixing θ to a particular value"
    - "The doorway in C-space expands to multiple meters wide because rotation freedom adds more configurations"
  answer: 1
  explanation: "When planning in full C-space (x, y, θ), obstacles are inflated by the robot's geometry. A point-robot reaching through a 1-meter doorway can pass at any orientation. But a rectangular robot of width w cannot pass if perpendicular to the doorway (regardless of y offset), yet can pass easily if parallel. The C-space obstacle is not a simple line; it's a 3D surface that depends on the robot's extent. Inflating by the robot's radius produces a minimum passage width that accounts for orientation. This is why computing C-space obstacles requires explicit geometry — it's not a simple subtraction."

- question: "Dijkstra's algorithm and A* both find shortest paths on graphs, but A* is faster in most robotics applications. Why?"
  type: multiple-choice
  options:
    - "A* evaluates fewer nodes because it uses a heuristic to prioritize exploration toward the goal, whereas Dijkstra explores equally in all directions"
    - "A* has a better time complexity — O(n) versus O(n log n) for Dijkstra"
    - "A* works with weighted graphs while Dijkstra requires unweighted graphs"
    - "A* is faster because it stops as soon as it finds any path, even if not optimal"
  answer: 0
  explanation: "A* uses a heuristic cost-to-goal estimate h(node) to guide the search. Nodes are prioritized by f(node) = g(node) + h(node), where g is actual cost from start and h is estimated cost to goal. This focuses exploration toward the goal rather than exploring uniformly outward like Dijkstra. In robotics, a spatial heuristic like Euclidean distance in the C-space is admissible (never overestimates) and consistent, ensuring A* finds optimal paths while evaluating far fewer nodes. If h is perfect (true distance to goal), A* becomes optimal greedy search; if h is zero, A* degenerates to Dijkstra."

- question: "A robot planning in a continuous 2D space must find the shortest path from start to goal with circular obstacles. Discretizing the space into a 1000 × 1000 grid and applying A* guarantees finding the optimal path in the original continuous space."
  type: true-false
  answer: false
  explanation: "Discretization introduces approximation error. The path found on the grid is optimal with respect to the grid, but the grid resolution is finite. If the optimal continuous path squeezes through a narrow gap at a boundary between grid cells, the discretized path may not find it or may take a longer grid-based detour. To guarantee optimality in continuous space, resolution must go to infinity or advanced techniques like configuration space decomposition or sampling-based planners must be used. Grid-based planning is very practical and often sufficient — the solution is nearly optimal if the grid is fine enough — but it trades exact optimality for computational tractability."

- question: "In configuration space, the path planning problem for a 6-degree-of-freedom robot arm is identical to planning for a point robot in 6D space, so standard graph search algorithms apply directly without modification."
  type: true-false
  answer: true
  explanation: "Correct. Configuration space is the key abstraction that reduces planning to point-robot pathfinding in a higher-dimensional space. A 6-DOF arm's configuration is a 6D point. Obstacles in workspace become forbidden regions in C-space. Once obstacles are represented in C-space, the planning problem is dimensionality-agnostic — graph search, sampling-based methods, or other algorithms apply the same way. The challenge is computing C-space obstacles from workspace geometry, which can be expensive for complex shapes, but conceptually the reduction is exact."

- question: "Describe why A* is generally preferred over Dijkstra's algorithm for robot motion planning, and explain what property a heuristic function must have to guarantee that A* finds an optimal path."
  type: short-answer
  answer: "A* uses a heuristic function h(node) estimating the cost from that node to the goal to guide the search, prioritizing exploration toward the goal. Dijkstra explores equally in all directions. For large spaces, A* evaluates far fewer nodes (especially with good heuristics), making it much faster. To guarantee optimality, the heuristic must be admissible: it never overestimates the true cost to goal. Euclidean distance in a 2D grid is admissible because straight-line distance cannot exceed actual path length. With an admissible heuristic, A* will find the optimal path and no other algorithm (with the same information) can expand fewer nodes while maintaining optimality."
  explanation: "A* elegantly balances exploration and exploitation. Exploring too much (Dijkstra) is wasteful; exploiting the heuristic too greedily (greedy best-first) can miss optimal paths. A* combines g(node) (proven cost from start) with h(node) (estimated cost to goal) so that the first path found is guaranteed optimal if h is admissible. In robotics, spatial heuristics from the C-space metric (Euclidean distance, Manhattan distance) are easy to compute and admissible, making A* the dominant choice for discrete planning."
```

## Explainer

Motion planning is central to autonomous robotics: given a goal configuration, compute a sequence of actions or waypoints to reach it while avoiding obstacles. The problem is deceptively simple to state but algorithmically rich. A naive approach — directly steer the robot toward the goal — fails in cluttered environments: the straight-line path is blocked, so the robot must navigate around obstacles. How do you find that path automatically?

The key insight is **configuration space** (C-space): instead of thinking about the robot as a complex 2D or 3D shape in the workspace, represent the robot's state as a point in an abstract space where each dimension is a degree of freedom (DOF). A planar robot has 3 DOF (x, y, θ). A 6-DOF robot arm has 6 DOF (joint angles). A point in C-space completely specifies the robot's configuration. Crucially, when the robot geometry is accounted for, obstacles in the workspace become forbidden regions in C-space. A collision-free path in C-space directly corresponds to a collision-free trajectory in the workspace.

With this abstraction, motion planning becomes a graph search problem: find a path in C-space from the start configuration to the goal configuration while avoiding C-space obstacles. This is algorithmically familiar — graph search, shortest path, tree exploration.

**Discretization and Grid Search**: The simplest approach discretizes C-space into a grid. Each cell is either free (robot doesn't collide) or occupied (robot collides with an obstacle). The grid is a graph where adjacent cells are connected. Standard shortest-path algorithms apply. Dijkstra's algorithm or Breadth-First Search will find paths, though they explore uniformly in all directions — inefficient if the goal is far away. The computation time grows with grid resolution and C-space dimensionality.

**A* and Heuristic Search**: A* improves on Dijkstra by using a heuristic function h(node) that estimates the cost from a node to the goal. The priority of a node becomes f(node) = g(node) + h(node), where g(node) is the actual cost from the start. By prioritizing nodes that are heuristically close to the goal, A* focuses exploration in promising directions rather than spreading equally. If the heuristic is **admissible** (never overestimates true cost), A* is guaranteed to find the optimal path while expanding fewer nodes than Dijkstra. In 2D, Euclidean distance is a natural admissible heuristic. In higher dimensions or with complex robot geometry, more sophisticated heuristics (e.g., pre-computed distance transform, multi-heuristic abstractions) are used.

**Limitations of Grid-Based Planning**: Discretization has drawbacks. (1) Coarse grids miss narrow passages; fine grids explode in memory and computation, especially in high dimensions. (2) Dimensionality curse: a 6D arm with 100 cells per dimension needs 10^12 cells. (3) The optimal path on a grid may not be the optimal path in continuous C-space, only the optimal path respecting the grid resolution.

**Informed Planning**: To handle higher dimensions and continuous spaces, more advanced methods become necessary. These include visibility graphs (connecting via straight lines between obstacles), rapid-exploring random trees (RRT, sample-based), and probabilistic roadmaps (PRM). Grid-based A* remains the workhorse for 2D navigation and low-dimensional problems, but for high-DOF systems like robot arms, sampling-based methods dominate because they scale better with dimensionality.

Understanding motion planning requires appreciating the configuration space abstraction, recognizing the core graph search structure, and knowing when discretization is adequate versus when continuous or sampling-based methods are needed. The choice determines tractability: a 3D mobile robot planning on a 500 × 500 grid is fast; a 7D arm on a 100^7-cell grid is hopeless.

