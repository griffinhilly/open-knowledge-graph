---
id: trajectory-planning
title: Trajectory Planning and Motion Planning
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: jacobian-robot-control
  type: hard
- id: robot-kinematics-forward-inverse
  type: soft
builds-toward:
- pid-control-robotics
tags:
- trajectory-planning
- motion-planning
- path-planning
- joint-space-trajectory
- cartesian-space
- collision-avoidance
stage: advanced
status: validated
---

# Trajectory Planning and Motion Planning

## Core Idea
Trajectory planning computes a time-parameterized path through configuration space (joint space) that moves the robot from an initial configuration to a goal configuration while respecting joint limits, velocity limits, and acceleration limits. Path planning ignores time and finds a collision-free path geometrically; trajectory planning adds timing and ensures the path is dynamically feasible. Common approaches: sampling-based (RRT, PRM), search-based (A*), or analytical (polynomial splines). The trajectory must be smooth (continuous velocity) to avoid controller chattering and joint stress.

## How It's Best Learned
Start with simple joint-space trajectories: connect two configurations with a cubic polynomial in joint space, verify joint limits are not violated, compute the trajectory in Cartesian space using forward kinematics to visualize it. Implement simple collision checking: discretize the path and test if any configuration intersects obstacles. Graduate to Cartesian-space trajectories: specify a start and goal pose, inverse kinematics at each point, then interpolate in joint space. Try a simple RRT planner in simulation.

## Common Misconceptions
- Trajectory planning in joint space is simpler but produces unnatural end-effector paths; Cartesian planning is always better. In reality, joint-space planning is often more efficient and avoids multiple inverse kinematics solutions.
- Straight-line paths in Cartesian space are optimal and should always be used; joint-space straight lines are simpler and just as good if they avoid singularities.
- Smooth trajectories are only an aesthetic choice; actually smoothness (continuous acceleration) is essential to avoid jerky control that damages the mechanism and fatigues materials.
- Collision avoidance can be added as a post-processing step after planning; actually, checking for obstacles during planning is far more efficient.

## Questions

```yaml
- question: "A robot must move from configuration A to configuration B. Joint-space trajectory planning connects A and B with a cubic polynomial: θ(t) = θ₀ + (3/t_f²)·(t_f - t)·(θ_f - θ₀)·t - (2/t_f³)·(t_f - t)·t²·(θ_f - θ₀). At the start (t=0) and end (t=t_f), the velocity is zero. Why is this constraint important?"
  type: multiple-choice
  options:
    - "To ensure the robot doesn't move too fast, which would damage it"
    - "To ensure the trajectory starts and ends with zero velocity (smooth starts and stops), preventing jerk and mechanical stress"
    - "To ensure the trajectory passes through the intermediate configuration θ_mid at t = t_f/2"
    - "To ensure the robot doesn't hit obstacles at the beginning and end of the motion"
  answer: 1
  explanation: "This is why cubic polynomials are popular: they have continuous acceleration. Piecewise-linear trajectories (connecting configurations with straight lines in joint space) have discontinuous acceleration at the connection points, requiring infinite torque. Splines with higher-order continuity (quintic, B-splines) smooth acceleration changes further."

- question: "A path-planning algorithm finds a collision-free path from start to goal, but doesn't account for dynamics. In the context of real robot execution, what additional check is needed?"
  type: true-false
  answer: true
  explanation: "A collision-free path in configuration space guarantees the path exists, but not that the robot can follow it given its speed and acceleration limits. When the trajectory is parameterized with time and accelerations, the trajectory itself (not just the path) might collide with obstacles if the robot moves too fast through tight spaces. More subtly, accelerations can shift the robot's center of mass or configuration slightly, potentially causing self-collision. Therefore, the full trajectory in space-time should be checked for collision, especially for fast or highly dynamic motions."
```

## Explainer

Imagine your robot must move a part from a cluttered workbench to an assembly station. Simply specifying the starting and goal joint angles is not enough. The robot must physically move through the environment without hitting obstacles, and the motion must be smooth and efficient. This is the problem of trajectory planning.

Trajectory planning has two components: **path planning** (finding a collision-free route geometrically) and **trajectory design** (adding timing and smoothness). A path is a sequence of configurations with no concern for time. A trajectory is the same path with timing: θ(t), fully parameterized over time.

In **joint-space planning**, you find a path directly in configuration space (the space of all possible joint angles). A simple approach is to connect the start and goal configurations with a straight line in this space, then check whether any configuration along this line causes the robot to collide with obstacles. If there are obstacles, you need a more sophisticated approach.

**Sampling-based motion planning** (like RRT—Rapidly-exploring Random Trees) works by repeatedly sampling random configurations and trying to connect them to nearby configurations using simple local paths (straight lines in joint space). Over time, this builds a tree of connected configurations that explores the space. Once the tree connects the start to the goal, a path is found. The beauty of RRT is that it scales reasonably to high-dimensional spaces (6+ DOF) and handles arbitrary obstacle geometries without explicit computation of the free space. The downside is that it doesn't optimize the path quality, though variants like RRT* gradually improve the path as computation continues.

In **Cartesian-space planning**, you instead specify the desired end-effector path (e.g., a straight line from start to goal pose). You then solve inverse kinematics at many points along this path to get a sequence of joint configurations, and connect them smoothly in joint space. This approach is more intuitive (the robot moves in a straight line in 3D space) but is computationally more expensive because inverse kinematics must be solved repeatedly and may fail at some points.

Once you have a path, **trajectory design** adds timing. A naive approach would be to simply move at constant velocity along the path. However, this produces infinite accelerations at path transitions (kinks), which is mechanically infeasible and requires infinite actuator torque. Instead, you smooth the path with **interpolating polynomials**. A cubic polynomial in joint space—starting at θ₀, ending at θ_f, with zero velocity at both ends—automatically produces smooth motion with finite accelerations. More complex trajectories (multiple waypoints, time-optimal motions) use quintic polynomials or spline bases to ensure continuous acceleration.

The trajectory must satisfy **joint limits**: each joint has a maximum velocity (θ̇_max) and acceleration (θ̈_max). The trajectory design process checks these limits and scales the motion time accordingly if needed. If the trajectory would violate limits, you either extend the motion time or (for advanced planners) replan to a different path.

**Collision checking** is applied both to the path and the trajectory. Path checking tests whether intermediate configurations collide. Trajectory checking considers the continuous motion: as the robot moves from one configuration to another, does any link enter an obstacle? This is more conservative but necessary for fast motions where the detailed trajectory shape matters.

The field of motion planning is vast—there are dozens of algorithms for specific robot types, environments, and constraints. But the core idea is always the same: find a feasible, smooth path that respects the robot's kinematic and dynamic limits and avoids obstacles.
