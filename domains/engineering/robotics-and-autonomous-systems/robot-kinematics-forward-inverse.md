---
id: robot-kinematics-forward-inverse
title: Forward and Inverse Kinematics
domain: engineering
course: robotics-and-autonomous-systems
prerequisites: []
builds-toward:
- denavit-hartenberg-convention
- jacobian-robot-control
- trajectory-planning
tags:
- kinematics
- forward-kinematics
- inverse-kinematics
- robot-arm
- position-orientation
stage: advanced
status: validated
---

# Forward and Inverse Kinematics

## Core Idea
Forward kinematics solves the computational problem: given the joint angles of a robot arm, what is the position and orientation of the end-effector (tool, gripper, or sensor) in Cartesian space? Inverse kinematics solves the inverse problem: given a desired end-effector pose (position and orientation), what joint angles achieve it? Forward kinematics has a unique solution; inverse kinematics often has multiple, no, or infinitely many solutions depending on robot geometry. Both are essential for motion planning and control.

## How It's Best Learned
Build a simple 2-link planar arm and solve forward kinematics by hand: given angle θ₁ and θ₂, compute end-effector (x, y). Then solve inverse kinematics for that arm and discover multiple solutions geometrically. Progress to a 3-link arm to see how complexity grows. Use a robot simulator (CoppeliaSim, Gazebo) to visualize configurations in real time.

## Common Misconceptions
- Inverse kinematics always has a solution; in reality, the desired pose may be outside the robot's reachable workspace.
- There is always exactly one inverse kinematics solution; real robots often have multiple solutions (elbow-up vs. elbow-down) or none.
- Forward kinematics is trivial just because it's "forward"; for complex multi-link arms it requires careful composition of transformation matrices.
- Inverse kinematics can be solved by simply inverting the forward kinematics matrix; matrices aren't invertible in this context and the relationship is nonlinear.

## Questions

```yaml
- question: "A 2-link planar robot arm has link lengths L₁ = 1m and L₂ = 0.8m, with joint angles θ₁ = 45° and θ₂ = 30°. The forward kinematics equations are: x = L₁·cos(θ₁) + L₂·cos(θ₁ + θ₂), y = L₁·sin(θ₁) + L₂·sin(θ₁ + θ₂). The end-effector position is approximately:"
  type: multiple-choice
  options:
    - "x ≈ 1.41m, y ≈ 1.41m"
    - "x ≈ 1.56m, y ≈ 1.27m"
    - "x ≈ 0.71m, y ≈ 0.71m"
    - "x ≈ 1.80m, y ≈ 0.95m"
  answer: 1
  explanation: "Forward kinematics is computed by summing the contributions of each link's position. The first link extends L₁ in direction θ₁; the second extends L₂ in direction θ₁ + θ₂ (absolute frame). Substituting the values into the equations and computing the cosines and sines at the given angles yields the position."

- question: "A 3-DOF robot arm has a reachable workspace that forms a sphere of radius 1.5m (sum of all link lengths). A task requires the end-effector to reach a point 2.0m from the base. What is true about inverse kinematics for this task?"
  type: multiple-choice
  options:
    - "Inverse kinematics has exactly one solution in the reachable configuration space"
    - "Inverse kinematics has no solution; the point is outside the robot's workspace"
    - "Inverse kinematics has infinitely many solutions because the robot is redundant"
    - "Inverse kinematics has two solutions: one with elbow-up and one with elbow-down orientation"
  answer: 1
  explanation: "This geometric picture generalizes to higher dimensions: the number of inverse kinematics solutions depends on how many times the solution manifold intersects the constraint surface. For a 6-DOF arm with a 6-DOF pose specification (3 position + 3 orientation), solutions typically range from zero (outside workspace) to a discrete set of isolated configurations, often including multiple self-consistent solutions reflecting different 'elbow' configurations or arm bends."

- question: "A SCARA robot (selective compliance arm for robotic assembly) is a 4-DOF arm with four revolute joints: two horizontal planar joints, a vertical lift joint, and a wrist rotation. How many solutions does inverse kinematics typically have for a given target position and orientation?"
  type: short-answer
  answer: "A SCARA arm typically has two solutions: elbow-up and elbow-down configurations for the planar motion, while the vertical and rotation DOFs are determined uniquely by the target height and orientation. The redundancy in the planar 2-DOF arm reaching a 2-DOF target (x, y) creates the two-solution family."
  explanation: "The SCARA's structure makes inverse kinematics partially decoupled: the planar 2-DOF subsystem solves for (x, y) position (two solutions), the vertical joint directly sets z position, and the wrist orientation joint directly sets rotation. This design choice makes the arm easier to control than a fully general 6-DOF arm."
```

## Explainer

Imagine you are building a robotic arm to pick objects from a table. The arm has several joints (shoulder, elbow, wrist) that you can rotate through specific angles. **Forward kinematics** answers the practical question: if I command the shoulder to angle θ₁, elbow to θ₂, and wrist to θ₃, where does the gripper end up? You solve this by following the kinematic chain: the first link rotates the second link, which rotates the third link. The final position is the vector sum of all link contributions in the global frame of reference.

For a 2-link arm, the computation is straightforward. If link 1 has length L₁ and rotates to angle θ₁, its tip is at (L₁ cos θ₁, L₁ sin θ₁). Link 2, with length L₂, attaches to that point and rotates an additional θ₂ (relative angle) or θ₁ + θ₂ (absolute angle). The gripper position is the sum: x = L₁ cos θ₁ + L₂ cos(θ₁ + θ₂), y = L₁ sin θ₁ + L₂ sin(θ₁ + θ₂). This direct calculation yields a unique answer for any joint configuration. Forward kinematics is a function (and typically a well-defined one) from joint space to Cartesian space.

**Inverse kinematics** is the reverse problem: you want the gripper at a specific position (x_d, y_d). What joint angles achieve this? This is much harder. Unlike forward kinematics, inverse kinematics is not a simple arithmetic calculation. The equations x = L₁ cos θ₁ + L₂ cos(θ₁ + θ₂) and y = L₁ sin θ₁ + L₂ sin(θ₁ + θ₂) are nonlinear in θ₁ and θ₂, with coupled trigonometric terms. Moreover, solutions may not be unique. For the 2-link arm, the gripper can reach most positions in two configurations: elbow-up (where the arm bends one way) and elbow-down (where it bends the opposite way). If the target is at the boundary of the reachable workspace (distance = L₁ + L₂ or distance = |L₁ - L₂|), there is exactly one solution. If the target is unreachable, there is no solution.

As robots become more complex — a 6-DOF arm with six revolute joints — the forward kinematics computation becomes a chain of matrix multiplications (using the Denavit-Hartenberg convention), but the computation is still straightforward and yields a unique answer. Inverse kinematics, however, becomes dramatically harder. With six joints and six position/orientation constraints (3 Cartesian coordinates plus 3 orientation angles), the system is "non-redundant" in principle, but the equations are transcendental (products of sines and cosines) and may have zero, one, multiple discrete solutions, or even continuous families of solutions depending on the arm geometry and target pose. Singularities — special configurations where the arm loses degrees of freedom — create regions where inverse kinematics is ill-posed.

Practical robotics solves inverse kinematics through a mix of analytical and numerical methods. For simple arm geometries (2-DOF planar, 3-DOF SCARA), analytical solutions exist and can be hard-coded. For complex arms, iterative numerical methods (Newton-Raphson, trust region methods) adjust joint angles to minimize the error between the current gripper position and the desired position. These methods require a good initial guess and can get stuck in local minima. This is why trajectory planning (the next topic) is crucial: instead of commanding a large jump to an arbitrary target, the planner constructs a smooth path through joint space that respects the arm's constraints and avoids singularities.
