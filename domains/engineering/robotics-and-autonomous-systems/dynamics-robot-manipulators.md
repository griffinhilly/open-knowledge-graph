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
  explanation: "By Newton's second law for rotation, τ = I·α. Substituting I = (1/3)·m·L² (the moment of inertia for a uniform rod about one end), the required torque is τ = (1/3)·m·L²·α. This is the fundamental rotational dynamics equation."

- question: "A 2-DOF robot arm has the equation of motion: [M₁₁·θ̈₁ + M₁₂·θ̈₂] + [C₁₁·θ̇₁² + C₁₂·θ̇₁·θ̇₂] + G₁ = τ₁. The term M₁₂·θ̈₂ in the equation for joint 1 represents:"
  type: multiple-choice
  options:
    - "The effect of gravity on joint 1"
    - "The coupling between joints: acceleration of joint 2 influences the motion of joint 1 due to the inertia of link 2"
    - "The friction force at joint 1"
    - "A measurement error in the torque sensor at joint 1"
  answer: 1
  explanation: "The inertia matrix M(θ) is dense and fully coupled. The term M₁₂ indicates that acceleration of joint 2 contributes to the torque equation of joint 1. Physically, joint 2 has inertia (mass of link 2 and everything beyond), and when joint 2 accelerates, it creates reaction forces on link 1. These reaction forces couple the dynamics: to accelerate link 1, you must not only overcome its own inertia but also account for the inertia of the downstream links. This is a key feature of multi-link arms and requires model-based control to handle properly."

- question: "The Lagrangian of a mechanical system is L = KE - PE, where KE is kinetic energy and PE is potential energy. For a robot arm, the kinetic energy is typically a function of θ̇ (joint velocities) and the potential energy is typically a function of θ (joint angles). Why does kinetic energy depend on θ as well, not just θ̇?"
  type: multiple-choice
  options:
    - "Kinetic energy doesn't depend on θ; you misunderstood the question"
    - "Because the orientation of the robot changes with θ, which affects how much kinetic energy is stored in each link's rotation"
    - "Because the velocity of each link's center of mass depends on θ as well as θ̇; links at different angles have different velocities for the same joint speeds"
    - "Because gravity changes with joint angle θ"
  answer: 2
  explanation: "The kinetic energy of a link is KE = (1/2)·m·v² + (1/2)·I·ω². The velocity v of the link's center of mass depends on θ (through the Jacobian relating joint velocities to Cartesian velocities) as well as θ̇. For a multi-link arm, link 2's absolute velocity depends on both θ₁ and θ̇₁ (it moves because link 1 rotates) and on θ₂ and θ̇₂ (its own rotation). Thus, KE is a function of both θ and θ̇. This is why the inertia matrix M(θ) depends on θ: the effective inertia seen by each joint changes with the robot's configuration."

- question: "The centrifugal and Coriolis terms in robot dynamics are grouped into C(θ,θ̇)·θ̇. These terms arise from:"
  type: multiple-choice
  options:
    - "The rotation of coordinate frames as the robot moves, creating fictitious forces in the rotating frame"
    - "Gravity acting on the links at different angles"
    - "Non-linear coupling in the inertia matrix, where the velocity-dependent part of kinetic energy generates additional forces"
    - "Friction in the joints"
  answer: 2
  explanation: "When you apply the Euler-Lagrange equation d/dt(∂L/∂θ̇) - ∂L/∂θ = τ and the kinetic energy KE(θ, θ̇) is nonlinear in θ̇ and depends on θ, the time derivative of ∂KE/∂θ̇ produces terms involving θ̈ (which form the inertia matrix) and terms involving θ̇² and θ̇₁·θ̇₂ (the centrifugal and Coriolis terms). These are not fictitious forces per se, but rather consequences of the nonlinear kinematics of multi-link systems. They are real forces that must be accounted for in control."

- question: "A robot arm is controlled using computed torque control: τ = M(θ)·θ̈_d + C(θ,θ̇)·θ̇ + G(θ), where θ̈_d is a desired acceleration computed from a trajectory. If the model is perfectly accurate and the actuators respond instantly, what is the resulting closed-loop system?"
  type: true-false
  answer: true
  explanation: "Correct. Substituting this control law into the dynamics equation M(θ)·θ̈ + C(θ,θ̇)·θ̇ + G(θ) = τ gives M(θ)·θ̈ + C(θ,θ̇)·θ̇ + G(θ) = M(θ)·θ̈_d + C(θ,θ̇)·θ̇ + G(θ), which simplifies to θ̈ = θ̈_d. The system follows the desired acceleration exactly. This is the power of computed torque: if you know the dynamics well, you can cancel the nonlinearities and make the robot behave like a simple linear system θ̈ = θ̈_d. In practice, modeling errors and actuator delays prevent perfect cancellation, so additional feedback control (e.g., PID) is layered on top."

- question: "In the gravity vector G(θ), the term for joint i is the partial derivative of potential energy: G_i = ∂PE/∂θ_i. For a vertical robot arm lifting against gravity, explain why G(θ) changes as the arm moves through different configurations."
  type: short-answer
  answer: "The potential energy of a link at height h is PE = m·g·h. As the robot's configuration θ changes, the height of each link's center of mass changes. For example, extending an arm vertically raises the center of mass and increases PE; folding it downward lowers the center of mass and decreases PE. The gravity torque is G_i = ∂PE/∂θ_i, which is the torque required to counteract gravity for a given joint. Different configurations require different gravity torques because the arms are at different heights. A horizontal arm requires zero gravity torque (height doesn't change with rotation). A vertical arm requires maximum gravity torque. Intermediate angles require intermediate compensation."
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
