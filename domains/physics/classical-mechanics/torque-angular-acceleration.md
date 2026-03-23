---
id: torque-angular-acceleration
title: Torque and Angular Acceleration Relations
domain: physics
course: classical-mechanics
prerequisites:
- id: torque
  type: hard
- id: rotational-motion-fixed-axis
  type: hard
- id: cross-product-3d
  type: soft
builds-toward:
- work-power-rotation
- rigid-body-planar-motion
tags:
- torque
- angular-dynamics
- mechanics
stage: formal-systems
status: validated
---

# Torque and Angular Acceleration Relations

## Core Idea
The net torque equals the moment of inertia times angular acceleration: τ_net = Iα. This is the rotational analog of Newton's second law and applies to both rigid bodies and systems of particles.

## Questions

```yaml
- question: "Two identical masses hang on either side of a pulley. In which scenario does the system have lower linear acceleration?"
  type: multiple-choice
  options:
    - "When the pulley is very light (negligible moment of inertia)"
    - "When the pulley is massive (large moment of inertia)"
    - "The pulley's mass doesn't affect linear acceleration — only the hanging masses matter"
    - "When the rope connecting the masses is longer"
  answer: 1
  explanation: "A massive pulley has a large moment of inertia I, so applying τ_net = Iα, more of the net driving force goes into angularly accelerating the pulley rather than linearly accelerating the hanging masses. This is directly analogous to adding mass to a linear system: more inertia means less acceleration for the same net force. The massless-pulley approximation always overestimates linear acceleration."

- question: "Two solid cylinders have identical total mass but different radii. Which has the greater moment of inertia about its central axis?"
  type: multiple-choice
  options:
    - "The smaller cylinder — less volume means mass is more concentrated near the axis"
    - "The larger cylinder — more of its mass sits at greater distances from the axis, and I scales with r²"
    - "They are equal — same mass means same rotational inertia"
    - "The larger cylinder — because it has greater surface area"
  answer: 1
  explanation: "Moment of inertia is I = ∫r² dm — mass at distance r from the axis contributes r² dm. A larger cylinder (same total mass spread over a larger radius) has more mass at greater r values, yielding a higher I. Equal total mass does NOT mean equal rotational inertia — distribution matters quadratically."

- question: "The moment of inertia of a rigid body depends only on its total mass, not on how that mass is distributed around the rotation axis."
  type: true-false
  answer: false
  explanation: "Moment of inertia explicitly depends on mass distribution: I = ∫r² dm. A hollow cylinder (all mass at the rim) has a greater moment of inertia than a solid cylinder of the same mass and radius, because all the mass sits at maximum r. The r² weighting means even modest redistributions of mass — like a figure skater extending their arms — have large effects on I."

- question: "In a pulley-and-mass system where the pulley has a nonzero moment of inertia, the rope tension must be different on the two sides of the pulley."
  type: true-false
  answer: true
  explanation: "For the pulley to angularly accelerate, there must be a net torque: τ_net = (T₁ − T₂)R = Iα. This requires T₁ ≠ T₂. If the tensions were equal, the net torque on the pulley would be zero, meaning no angular acceleration — inconsistent with the hanging masses accelerating. Unequal tension is the defining feature of a massive pulley problem and is what distinguishes it from the massless-pulley case."

- question: "How is τ_net = Iα analogous to F_net = ma, and what does moment of inertia represent in this analogy?"
  type: short-answer
  answer: "Just as F = ma says net force produces linear acceleration inversely proportional to mass, τ = Iα says net torque produces angular acceleration inversely proportional to moment of inertia. Moment of inertia is the rotational analog of mass — it quantifies resistance to changes in angular velocity. Unlike mass (a fixed scalar), I depends on mass distribution relative to the rotation axis: the r² weighting means mass farther from the axis contributes quadratically more to rotational inertia."
  explanation: "The analogy is exact: every linear quantity has a rotational counterpart. Force ↔ torque, mass ↔ moment of inertia, linear acceleration ↔ angular acceleration, and F = ma ↔ τ = Iα. Exploiting this structural parallel makes rotational dynamics much easier to set up and solve."
```

## Explainer

You already know that **torque** is the rotational effectiveness of a force — τ = r × F — and that **rotational motion about a fixed axis** is described by angular displacement θ, angular velocity ω, and angular acceleration α, with the same kinematic relationships as linear motion. The equation τ_net = Iα ties these together exactly as F_net = ma ties force to linear acceleration, and the parallel structure is worth exploiting fully.

In linear dynamics, **mass** measures resistance to changes in translational motion — a large mass requires a large force to accelerate. In rotational dynamics, the **moment of inertia** I plays the same role for angular acceleration. But I is not just a number intrinsic to the object; it depends on how the mass is *distributed relative to the axis of rotation*. A mass element dm at distance r from the axis contributes r² dm to the moment of inertia, so mass far from the axis counts for much more than mass near it. This is why a figure skater pulls in their arms to spin faster — reducing r reduces I, and since angular momentum Iω is conserved, ω must increase. The r² dependence means even modest redistributions of mass have large rotational effects.

To apply τ_net = Iα, the procedure mirrors F = ma: identify all forces acting on the body, compute the torque each exerts about the rotation axis (τ = r F sin θ, where θ is the angle between r and F), sum them with signs (choose a positive direction for rotation), look up or calculate I for the body and axis, then solve for α. The force-torque analogy runs deep: a force tangential to the rotation path produces torque most efficiently (sin θ = 1); a force directed through the axis produces zero torque (r = 0 or sin θ = 0). This is the rotational equivalent of recognizing that only the component of force along the direction of motion does work.

The most common application is a **pulley or wheel with mass**. In an introductory problem, a massless pulley simply changes the direction of a string tension. Once the pulley has mass, the tension on the two sides of the rope need not be equal — the net torque from the tension difference is what causes the pulley to accelerate angularly. Writing τ_net = Iα for the pulley alongside F = ma for each hanging mass yields a system of equations. The coupling condition is the kinematic constraint: the rope's linear acceleration a equals the pulley rim's tangential acceleration, a = αR. This constraint links the linear and rotational dynamics and allows you to solve for all accelerations and the true tensions. Notice that a massive pulley always results in a *smaller* linear acceleration than the massless case — some of the driving force goes into spinning up the pulley rather than accelerating the masses.
