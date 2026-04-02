---
id: denavit-hartenberg-convention
title: Denavit-Hartenberg Notation and Transformation Matrices
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: robot-kinematics-forward-inverse
  type: hard
builds-toward:
- jacobian-robot-control
- dynamics-robot-manipulators
tags:
- denavit-hartenberg
- dh-convention
- transformation-matrices
- homogeneous-coordinates
- kinematic-chain
stage: advanced
status: validated
---

# Denavit-Hartenberg Notation and Transformation Matrices

## Core Idea
The Denavit-Hartenberg (DH) convention is a systematic method for assigning coordinate frames to each joint and link of a robot arm. Using DH parameters (link length a, twist α, link offset d, joint angle θ), you construct a sequence of 4×4 homogeneous transformation matrices—one for each joint—whose product gives the total transformation from the base frame to the end-effector frame. This makes forward kinematics a deterministic matrix multiplication chain and greatly simplifies implementation and derivation of the robot's Jacobian.

## How It's Best Learned
Work through a 2-link planar arm first: assign DH frames by hand, compute all four DH parameters, construct the individual transformation matrices, multiply them to recover the forward kinematics equations you already know. Verify that the result matches. Move to a 3-DOF SCARA arm, then to a 6-DOF industrial robot like the PUMA or UR. Use a textbook table of DH parameters for a real robot and practice reconstructing the forward kinematics.

## Common Misconceptions
- DH frames are arbitrary; actually they follow strict rules (z-axis along the joint axis, x-axis along the common normal).
- All four DH parameters are nonzero for every link; typically one or two are zero for each link due to standard geometries.
- DH convention is unique; there are actually multiple valid DH parameter sets for the same robot depending on frame assignment choices.
- DH parameters directly give the physical dimensions; they must be measured or calibrated from the actual robot.

## Questions

```yaml
- question: "For a revolute joint in a robot arm, the Denavit-Hartenberg parameters are: link length a = 0.3m, twist α = 90°, link offset d = 0.2m, joint angle θ (variable). Which of these is determined by the robot's physical construction, and which changes as the joint rotates?"
  type: multiple-choice
  options:
    - "All four parameters are constant; θ varies as a separate quantity during motion"
    - "a, α, and d are constant (physical), and θ is the joint variable that changes"
    - "Only θ is constant; a, α, d all vary as the joint rotates to maintain kinematic consistency"
    - "θ is constant for a fixed joint configuration, and a, α, d are control inputs that change"
  answer: 1
  explanation: "The power of DH is standardization and reusability. Any robot can be described by its DH parameters. Any forward kinematics code that accepts a DH parameter table works for any arm. This has made DH the industry standard for robot kinematics."
```

## Explainer

When you first computed forward kinematics for a simple robot arm, you probably added the position contributions of each link by hand, tracking angles carefully. This approach works for small arms but becomes tedious and error-prone for robots with six or more joints. The Denavit-Hartenberg convention provides a systematic framework for this accounting.

The key insight is to assign a coordinate frame to each link—frame i attached to link i. The robot is then a chain of frames: base frame (frame 0) → frame 1 (attached to link 1) → frame 2 → ... → frame n (end-effector). The forward kinematics computation becomes: what is the cumulative transformation from frame 0 to frame n? This is expressed as a product of homogeneous transformation matrices, each of which describes how one frame relates to the previous one.

The DH convention provides rules for assigning these frames consistently. For each joint i:
1. The z-axis of frame i-1 points along the axis of rotation of joint i (for revolute joints) or along the direction of translation (for prismatic joints).
2. The x-axis points along the common normal between the z-axes of frames i-1 and i (or along the line from joint i-1 to i if the axes are parallel).
3. The y-axis completes the right-handed system.

With frames assigned, each link is described by four parameters:
- **a (link length)**: distance from the z-axis of frame i-1 to the z-axis of frame i along the x-axis of frame i-1.
- **α (twist)**: angle between the z-axes, measured about the x-axis of frame i-1.
- **d (link offset)**: distance from the x-axis of frame i-1 to the x-axis of frame i along the z-axis of frame i-1.
- **θ (joint angle)**: for a revolute joint, the rotation about the z-axis of frame i-1; for a prismatic joint, d is variable and θ is constant.

The transformation from frame i-1 to frame i is then the product of four basic matrices:

T_{i-1}^{i} = Rot_z(θ_i) · Trans_z(d_i) · Trans_x(a_i) · Rot_x(α_i)

The forward kinematics is the product chain:

T_0^{n} = T_0^{1} · T_1^{2} · ... · T_{n-1}^{n}

This matrix encodes both position and orientation of the end-effector relative to the base.

Why use DH instead of just multiplying arbitrary transformation matrices? Because DH enforces a standard, which makes forward kinematics systematic and automatable. You write a general function that takes a DH parameter table, builds the matrices in order, and returns the product—no robot-specific code needed. This also makes comparing different robots straightforward: their geometries are captured in different DH tables, but the algorithm is identical. Moreover, the Jacobian (the derivative of forward kinematics with respect to joint angles) also follows a standard formula in the DH framework, enabling systematic design of controllers, singularity avoidance, and velocity control.

DH parameters must be measured or calibrated from the actual robot. In practice, calibration involves measuring reference points on the end-effector and fitting DH parameters to minimize the error between predicted and measured positions. Once you have accurate DH parameters, forward kinematics becomes a reliable computational tool.
