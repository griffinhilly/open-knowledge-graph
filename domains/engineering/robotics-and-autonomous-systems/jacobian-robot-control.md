---
id: jacobian-robot-control
title: The Robot Jacobian and Velocity Control
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: robot-kinematics-forward-inverse
  type: hard
- id: denavit-hartenberg-convention
  type: hard
builds-toward:
- trajectory-planning
- actuators-and-sensors-robotics
tags:
- jacobian
- velocity-control
- cartesian-velocity
- joint-space
- singularities
- differential-kinematics
stage: advanced
status: validated
---

# The Robot Jacobian and Velocity Control

## Core Idea
The Jacobian matrix J relates joint velocities (how fast each joint rotates or extends) to the end-effector velocity (how fast the gripper moves and rotates in 3D space). Mathematically, J is the matrix of partial derivatives of the forward kinematics function: each column contains the partial derivative of end-effector position/orientation with respect to one joint variable. Given desired end-effector velocity, you solve J · θ_dot = v_ee for joint velocities θ_dot. When J becomes singular (determinant = 0), velocity control breaks down—the robot loses degrees of freedom and cannot move in certain directions.

## How It's Best Learned
Compute the Jacobian by hand for a 2-DOF planar arm: differentiate the forward kinematics equations with respect to θ₁ and θ₂. Verify that multiplying J by [θ₁_dot, θ₂_dot] gives the end-effector velocity [ẋ, ẏ]. Visualize singularities: where does det(J) = 0? What configurations make the arm "lock"? Experiment with velocity control in simulation to see what happens near singularities.

## Common Misconceptions
- The Jacobian is computed by inverting the forward kinematics matrix; actually J is computed by differentiation, not matrix inversion.
- If the robot is non-redundant (6 joints, 6-DOF pose), the Jacobian is always invertible; actually singularities occur at specific poses regardless of redundancy level.
- Singularities are rare edge cases; they occur frequently and must be accounted for in motion planning and control.
- The condition number of the Jacobian is irrelevant; a nearly singular Jacobian (high condition number) amplifies joint motion requirements and leads to large actuator demands for small end-effector velocities.

## Questions

```yaml
- question: "For a 2-link planar robot arm with forward kinematics x = L₁·cos(θ₁) + L₂·cos(θ₁ + θ₂), y = L₁·sin(θ₁) + L₂·sin(θ₁ + θ₂), the Jacobian J relates joint velocities [θ̇₁, θ̇₂]ᵀ to end-effector velocity [ẋ, ẏ]ᵀ. Which is the correct expression for J?"
  type: multiple-choice
  options:
    - "J = [[-L₁·sin(θ₁) - L₂·sin(θ₁ + θ₂), -L₂·sin(θ₁ + θ₂)], [L₁·cos(θ₁) + L₂·cos(θ₁ + θ₂), L₂·cos(θ₁ + θ₂)]]"
    - "J = [[L₁·cos(θ₁), L₂·cos(θ₁ + θ₂)], [L₁·sin(θ₁), L₂·sin(θ₁ + θ₂)]]"
    - "J = [∂x/∂θ₁, ∂x/∂θ₂; ∂y/∂θ₁, ∂y/∂θ₂] = [[-L₁·sin(θ₁) - L₂·sin(θ₁ + θ₂), -L₂·sin(θ₁ + θ₂)], [L₁·cos(θ₁) + L₂·cos(θ₁ + θ₂), L₂·cos(θ₁ + θ₂)]]"
    - "Options (a) and (c) are equivalent"
  answer: 3
  explanation: "Near-singular configurations are almost as problematic as true singularities from a practical control perspective. This is why motion planners include singularity-avoidance heuristics: they maintain the Jacobian well-conditioned by modifying reference trajectories to avoid configurations with high condition numbers."

- question: "A 6-DOF robot arm is commanded with a desired end-effector velocity [v_x, v_y, v_z, ω_x, ω_y, ω_z]ᵀ (3 linear + 3 angular velocity components). The Jacobian is 6×6. If this Jacobian is singular, which of the following must be true?"
  type: true-false
  answer: true
  explanation: "At least one of the six velocity components cannot be achieved, or at least one joint would require infinite velocity. The rank of J must be less than 6, meaning the null space is non-empty and there exist desired velocities that lie outside the range of J."
```

## Explainer

You now know how to compute the position and orientation of a robot's end-effector given its joint angles (forward kinematics). The next question is: how do you move the end-effector along a desired path or at a desired velocity? You need to solve the inverse problem at every instant: given a desired end-effector velocity, what joint velocities achieve it?

The Jacobian is the bridge between these two spaces. Mathematically, it is the matrix of first partial derivatives of the forward kinematics function. If forward kinematics is expressed as:

p = f(θ),

where p is the end-effector position/orientation and θ is the vector of joint angles, then the Jacobian is:

J = ∂f/∂θ

Each column of J corresponds to one joint, and each row corresponds to one output dimension. For a planar 2-DOF arm with position output [x, y], the Jacobian is 2×2. For a 6-DOF robot with 6-DOF pose output (3 position + 3 orientation), it is 6×6.

By the chain rule of calculus, the end-effector velocity is related to joint velocities by:

v_ee = J · θ_dot

This is the **velocity kinematics equation**. To control the end-effector velocity, you invert it:

θ_dot = J⁻¹ · v_ee

In principle, this tells you what joint velocities to command. But there's a catch: J is invertible only when its determinant is nonzero. At configurations where det(J) = 0, the matrix is singular, and inversion fails. What does this mean physically? At a singularity, the robot has lost a degree of freedom. The configuration is usually one where multiple links have aligned in a way that constrains motion. For example, a 2-DOF planar arm becomes singular when fully extended (θ₂ = 0) or fully folded (θ₂ = 180°) — at these configurations, the end-effector can only move along a line, not in all directions, because the second link is aligned with the first and cannot contribute perpendicular motion.

The practical implication is severe: at a singularity, certain end-effector velocities are unachievable no matter how fast the joints move. If you command an end-effector velocity toward a singular direction, the required joint velocities become infinite. Real actuators have finite speed limits, so this is impossible to achieve. Motion planning must therefore avoid singularities or approach them carefully.

Even when J is invertible, it may be nearly singular—the condition number is high. The condition number, defined as cond(J) = σ_max / σ_min (ratio of largest to smallest singular value), measures how much the Jacobian amplifies errors. A high condition number means the Jacobian is ill-conditioned: small errors in the desired velocity get amplified into large joint velocity errors. This causes jerky, jerky motion requiring large actuator efforts for small end-effector motions.

In practice, velocity control using the Jacobian is robust when the Jacobian is well-conditioned and away from singularities. For redundant robots (more than 6 joints controlling a 6-DOF end-effector), you use the **pseudo-inverse** J⁺ = Jᵀ(JJᵀ)⁻¹, which provides the least-squares solution and allows null-space motion for secondary objectives (e.g., avoiding obstacles or self-collision). Understanding the Jacobian and its singularities is central to robot control and motion planning.
