---
id: dynamics-robot-manipulators
title: Dynamics of Robot Manipulators
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: denavit-hartenberg-convention
  type: hard
builds-toward:
- actuators-and-sensors-robotics
tags:
- robot-dynamics
- lagrangian
- inertia-matrix
- centrifugal-coriolis
- computed-torque-control
stage: advanced
status: validated
---

# Dynamics of Robot Manipulators

## Core Idea
Robot dynamics describes how joint torques produce joint accelerations, accounting for inertia, gravity, and coupling forces (centrifugal and Coriolis effects). The equation of motion is M(θ)·θ̈ + C(θ,θ̇)·θ̇ + G(θ) = τ, where M is the inertia matrix, C couples joint velocities to accelerations, G is the gravity vector, and τ is the applied torque. Knowing the dynamics enables model-based control (computed torque control), which can achieve precise trajectory tracking despite coupling between joints. The Lagrangian formulation is the standard tool: L = KE - PE; then apply Euler-Lagrange equations to derive the dynamics.

## How It's Best Learned
Derive the dynamics of a 2-DOF planar arm by hand using the Lagrangian method: compute kinetic energy (as a function of θ̇₁ and θ̇₂), potential energy, form the Lagrangian, apply the Euler-Lagrange equation for each DOF. Observe how inertia terms couple the two equations: acceleration of joint 2 appears in the equation for joint 1, and vice versa. Verify that the result has the form M(θ)·θ̈ + C(θ,θ̇)·θ̇ + G(θ) = τ. Graduate to a 3-link arm and observe that the inertia matrix becomes more complex but the procedure is the same.

## Common Misconceptions
- Robot dynamics can be ignored if the control loop is fast enough; ignoring dynamics leads to poor tracking performance and instability at high speeds.
- The gravity vector G(θ) is constant; actually G(θ) depends on joint configuration because link positions change with θ.
- The inertia matrix M(θ) is diagonal; in general, M is dense and fully coupled, meaning joint accelerations affect all other joints.
- Computed torque control requires perfect knowledge of the robot's parameters (masses, inertias); practical implementations use adaptive or robust control to handle modeling errors.

## Questions

```yaml
- question: "For a single rigid link of mass m, length L, rotating about a fixed axis, the moment of inertia is I = (1/3)·m·L². What is the torque required to produce an angular acceleration α?"
  type: multiple-choice
  options:
    - "τ = m·L·α"
    - "τ = I·α = (1/3)·m·L²·α"
    - "τ = m·g·L (gravity only)"
    - "Insufficient information; the moment of inertia depends on the shape, not just mass and length"
  answer: 1
  explanation: "Gravity compensation is configuration-dependent. Sophisticated robot controllers measure the gravity torque at each configuration and actively compensate for it. Without compensation, the robot would sag under gravity when held stationary. With compensation, the robot feels 'weightless' to the operator during manual manipulation (teach pendant programming)."
```

## Explainer

You now understand how to command a robot to reach specific poses (forward kinematics) and move along planned trajectories (trajectory planning). To actually execute these commands, you need to know how joint torques produce joint accelerations—the dynamics of the robot.

The equation of motion for a robot arm is most conveniently derived using **Lagrangian mechanics**. The Lagrangian is L = KE - PE, where KE is the total kinetic energy and PE is the total potential energy. The kinetic energy includes rotation of each link about its center of mass and translation of its center of mass. The potential energy includes gravitational PE for each link. For a link attached to a joint at position r_i, the translational velocity is v_i = J_p,i(θ) · θ̇, where J_p,i is the Jacobian relating joint velocities to the Cartesian velocity of the link. This is why KE depends on θ as well as θ̇: the Jacobian itself depends on configuration.

Applying the Euler-Lagrange equation for each joint:

d/dt(∂L/∂θ̇_i) - ∂L/∂θ_i = τ_i

yields the dynamics equation:

M(θ)·θ̈ + C(θ,θ̇)·θ̇ + G(θ) = τ

This is the fundamental equation of robot dynamics. Let's parse each term:

- **M(θ)** is the inertia matrix (n × n for an n-DOF robot). M(θ) is symmetric and positive-definite. Diagonal terms M_ii represent the effective inertia of joint i; off-diagonal terms M_ij represent coupling: how acceleration of joint j influences the torque required at joint i. The inertia matrix depends on configuration because as links move, the distribution of mass relative to each joint axis changes.

- **C(θ,θ̇)·θ̇** is the Coriolis and centrifugal term. Centrifugal forces arise when a rotating link has mass at a distance from the rotation axis; as angular velocity increases, the centrifugal force increases. Coriolis forces arise from the interaction of two joints: when one joint rotates, it creates reaction forces on the other. These terms are nonlinear in velocity and are particularly significant at high speeds.

- **G(θ)** is the gravity vector. G_i is the torque required to hold joint i stationary against gravity. For a horizontal joint, G_i = 0. For a vertical joint holding mass, G_i = m·g·h, where h is the height. G(θ) is configuration-dependent: as the arm moves, the distribution of mass above each joint changes, so the gravity torque changes.

The control problem is: given a desired trajectory θ_d(t), compute the joint torques τ(t) to track this trajectory. The simplest approach is independent joint control: PID control at each joint, ignoring the coupling terms. This works well when dynamics are weak (slow motions, lightweight arms) but fails at high speeds or with heavy loads because the coupling terms become significant.

**Computed torque control** accounts for the full dynamics. The control law is:

τ = M(θ)·θ̈_d + C(θ,θ̇)·θ̇ + G(θ) + K_p·e(t) + K_i·∫e dt

The first three terms are the computed nominal torques needed to execute the desired acceleration and overcome Coriolis, centrifugal, and gravity forces. The last two terms are PID feedback on the tracking error e = θ_d - θ. If the model (M, C, G) is accurate and the actuators are fast, the feedback terms are small and the system tracks accurately. If the model has errors, the feedback terms compensate and maintain stability.

The challenge is that computing M(θ), C(θ,θ̇), and G(θ) requires knowing the robot's mass distribution, inertias, and center-of-mass locations—parameters that are difficult to measure precisely. In practice, robots are calibrated to identify these parameters, or adaptive control is used to update estimates online. Despite these challenges, model-based control is far more powerful than independent joint control and is standard in advanced robot applications like manipulation, manufacturing, and humanoid robots.
