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

