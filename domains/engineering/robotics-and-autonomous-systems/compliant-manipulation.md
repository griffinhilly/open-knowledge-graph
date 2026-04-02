---
id: compliant-manipulation
title: Compliant Manipulation and Force Control
domain: engineering
course: robotics-and-autonomous-systems
prerequisites:
- id: dynamics-robot-manipulators
  type: hard
- id: pid-control-robotics
  type: hard
builds-toward:
- surgical-robotics
- soft-robotics
tags:
- manipulation
- control
- force-control
- compliance
- haptic
stage: expert
status: validated
---

# Compliant Manipulation and Force Control

## Core Idea
Most robotic manipulation assumes position control: command the robot's end-effector to move to a specific location, and it gets there. This works well when the environment is perfectly known and rigid (pick up a block, place it elsewhere). In reality, the environment is partially unknown or compliant (soft), and the robot must interact gently with it (insertion tasks, assembly, surgery). In these cases, position-only control fails: if you command the robot to move 100 mm but encounter a surface at 50 mm, a rigid position controller drives hard against the surface, potentially damaging it. **Compliant manipulation** addresses this by controlling both position and force. Instead of rigidly commanding "move to X," the robot modulates compliance (stiffness/damping in different directions) and can interact with the environment with controlled force rather than uncontrolled displacement. **Hybrid position/force control** is a foundational technique: in constrained directions (touching a surface), control force; in unconstrained directions, control position. **Impedance control** is a generalization: the robot behaves like a spring-damper system with commanded stiffness, so it naturally yields to external forces while maintaining desired behavior. This is how surgeons work (pushing gently, feeling tissue resistance) and how assembly robots succeed despite imperfect part alignment.

## Questions

```yaml
- question: "A robot is assembling a part that must be inserted into a hole (peg-in-hole insertion). Without force feedback, the robot often fails (peg hits the side of the hole, gets stuck). With force control, the robot can succeed despite misalignment. Why does force control solve this problem?"
  type: multiple-choice
  options:
    - "Force control makes the robot stronger so it can force the peg through"
    - "With force control, the robot feels sideways force when the peg contacts the hole's edge. Rather than pushing harder, it modulates motion to reduce the sideways force, essentially 'feeling' its way into the hole. The robot can also comply in the lateral direction, allowing slight misalignment to be corrected by deformation rather than jamming"
    - "Force control is irrelevant; the issue is just imprecise positioning"
    - "Force control only works for soft materials, not hard parts"
  answer: 1
  explanation: "This conceptual unification is why impedance control is taught as a foundational abstraction. Rather than learning separate position-control and force-control algorithms, a student learns impedance control and understands that both position and force control are special cases. This abstraction has power: it simplifies algorithm design and enables robots to switch between behaviors by just changing stiffness parameters."
```

## Explainer

Compliant manipulation addresses a fundamental challenge in robotics: the interaction with partially known and deformable environments. Early industrial robots used pure position control — move the end-effector to a commanded pose, hold it stiffly against external disturbances. This works when the environment is perfectly known and rigid (moving blocks in a factory) but fails in any application involving interaction with soft or unknown structure.

**The Peg-in-Hole Problem**: Consider a classic assembly task: inserting a peg into a hole. With perfect knowledge, position control is sufficient: move the peg to the hole's center and push straight down. In reality, positioning is never perfect. If the peg's position is off by a few millimeters, it hits the hole's edge. A pure position controller pushes hard against the edge, and the peg gets stuck or jams. With force feedback, the robot detects the lateral force (peg hitting the edge), recognizes the misalignment, and adjusts: it might shift sideways slightly to align better, reduce downward force to allow sliding, or tilt to ease entry. This is what human assemblers do automatically — they use tactile feedback to handle imperfect alignment. Force control enables robots to replicate this capability.

**Hybrid Position/Force Control**: The foundational approach to compliant manipulation divides the robot's workspace into constrained and unconstrained directions. In directions where the robot is in contact with the environment (touching a surface or assembly surface), it controls force. In free directions, it controls position. For peg-in-hole, downward direction is constrained (peg in hole), so control force downward to avoid jamming. Lateral directions are unconstrained initially (peg moving toward hole), so control position to move toward the hole. When the peg touches the hole's edge, lateral directions become constrained, and the controller switches to force control in those directions. This requires detecting contact and switching control modes dynamically.

**Impedance Control**: A more general approach treats the robot as a mechanical system with commanded impedance: the relationship between applied force and resulting motion. Specifically, the robot generates motion according to a virtual spring-damper model: when the robot tries to move to position x_desired but encounters an external force, it yields according to F = K*(x - x_desired) + B*(v), where K is stiffness, B is damping, x is actual position, and v is actual velocity. High stiffness means the robot resists disturbances and maintains position (appropriate for holding an object). Low stiffness means the robot yields easily to external forces (appropriate for gentle manipulation). This single control law unifies position and force control: set K very high and you get position control; set K = 0 and you get force control. Intermediate values produce hybrid behavior. Impedance control also naturally handles unexpected disturbances — the robot yields rather than fighting, reducing impact forces and improving safety.

**Force Sensing and Feedback**: Implementing force control requires measuring force at the robot's end-effector using a force/torque sensor (6-axis load cell measuring three-axis force and three-axis torque). The sensor output feeds the control algorithm, which adjusts motion to achieve the desired force. Force sensing adds cost and complexity but is essential for safe, compliant manipulation. In surgical robotics, high-fidelity force sensing enables the surgeon to feel tissue resistance through haptic feedback (force feedback to the surgeon's hands).

**Challenges**: Real force control is harder in practice than theory suggests. Friction and stiction (static friction) cause sticking at zero force, making smooth force control difficult. Sensor noise in force measurement can cause high-frequency oscillations. Contact detection (knowing when the robot touches the environment) is non-trivial — the robot might be near the surface but not in contact. These practical challenges mean force-controlled systems require careful tuning and often use adaptive or learning-based approaches to handle variability.

