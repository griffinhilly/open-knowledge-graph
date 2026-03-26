---
id: equations-of-motion-from-free-body-diagrams
title: Equations of Motion from Free Body Diagrams
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: free-body-diagrams
  type: hard
- id: derivative-as-slope-of-tangent
  type: soft
- id: vector-addition-subtraction
  type: hard
- id: vectors-in-3d
  type: soft
builds-toward:
- projectile-motion
- static-equilibrium
tags:
- kinematics
- dynamics
- forces
- methodology
stage: formal-systems
status: validated
---

# Equations of Motion from Free Body Diagrams

## Core Idea
Once you draw a free-body diagram identifying all forces, Newton's second law F_net = ma directly yields the equations governing motion. Each coordinate direction yields one differential equation; solving these systematically gives acceleration, which you integrate to find velocity and position. This bridges the gap between force diagrams and kinematic equations.

## How It's Best Learned
Start with single-force cases, then progressively add forces (gravity + normal, then friction). Repeatedly practice: sketch diagram → identify axes → write ΣF_x = ma_x and ΣF_y = ma_y separately → solve algebraically.

## Common Misconceptions
- Assuming the normal force always equals mg; it only does so when perpendicular acceleration is zero. - Forgetting static friction can be less than μ_s N; it adjusts to prevent motion up to its maximum value. - Confusing the direction of the net force with the direction of motion; net force determines acceleration, not velocity direction.

## Questions

```yaml
- question: "A block of mass m sits on a frictionless inclined plane at angle θ. Aligning the x-axis along the slope (positive pointing down the slope) and the y-axis perpendicular to it, what is the net force equation along the x-axis?"
  type: multiple-choice
  options:
    - "ΣFₓ = mg — the full weight acts along the slope"
    - "ΣFₓ = mg cos θ — the component of gravity perpendicular to the slope"
    - "ΣFₓ = mg sin θ — the component of gravity along the slope"
    - "ΣFₓ = N − mg — normal force minus total weight"
  answer: 2
  explanation: "When the x-axis is aligned along the slope, the gravitational force (pointing straight down) has two components: mg sin θ along the slope and mg cos θ perpendicular to the slope. Only mg sin θ appears in the x-equation: ΣFₓ = mg sin θ = maₓ, giving acceleration aₓ = g sin θ down the slope. The normal force N points perpendicular to the surface, so it appears only in the y-equation (where it balances mg cos θ). This is the payoff of smart axis choice: the y-equation immediately gives N = mg cos θ, and the x-equation gives the acceleration without solving a system."

- question: "A car of mass m is accelerating horizontally on a flat road. What is the normal force from the road on the car?"
  type: multiple-choice
  options:
    - "Greater than mg, because the engine exerts a downward force through the drivetrain"
    - "Less than mg, because the car is moving and kinetic effects reduce the apparent weight"
    - "Equal to mg, because vertical acceleration is zero: ΣFᵧ = N − mg = maᵧ = 0, so N = mg"
    - "Cannot be determined without knowing the car's speed or acceleration"
  answer: 2
  explanation: "The normal force is determined by the perpendicular force equation, independent of the horizontal motion. Since the car accelerates horizontally but not vertically, aᵧ = 0. Applying Newton's second law in the vertical direction: N − mg = 0, so N = mg. The horizontal acceleration is irrelevant to the vertical force balance. This shows why N = mg only holds when perpendicular acceleration is zero — on an incline, N = mg cos θ < mg; in an accelerating elevator, N ≠ mg. The formula N = mg is a consequence of zero vertical acceleration, not a general law."

- question: "The direction of the net force on an object typically matches the direction of the object's velocity."
  type: true-false
  answer: false
  explanation: "Net force determines the direction of acceleration, not velocity. A ball thrown upward has upward velocity but downward net force (gravity). A car braking while moving forward has forward velocity and backward net force. A planet in circular orbit has velocity tangent to the orbit but net force (gravity) pointing toward the center — perpendicular to velocity. Net force and velocity can point in the same direction, opposite directions, or at any angle. Confusing the direction of force with the direction of motion is one of the most common conceptual errors in introductory mechanics."

- question: "On an inclined plane at angle θ, the normal force equals mg cos θ rather than mg, because it only needs to balance the component of gravity perpendicular to the surface."
  type: true-false
  answer: true
  explanation: "Applying Newton's second law perpendicular to the incline: the block doesn't accelerate into or away from the surface, so ΣF_perp = N − mg cos θ = 0, giving N = mg cos θ. This is less than mg because gravity's full weight does not push directly into the surface — only its perpendicular component does. On flat ground θ = 0°, cos 0 = 1, and N = mg is recovered as a special case. This is why assuming N = mg on an incline leads to errors in friction calculations and in analyzing the block's motion."

- question: "Why is the choice of coordinate axes so important when applying Newton's second law to an inclined plane, and what advantage does aligning the x-axis along the slope provide?"
  type: short-answer
  answer: "Newton's second law must be applied component-by-component, so the axes determine how forces are decomposed. With horizontal/vertical axes, both the normal force and gravity have components in each direction, and the equations for x and y are coupled — you must solve them together as a system. Aligning the x-axis along the slope decouples the problem: the normal force lies entirely along the y-axis (perpendicular to slope), and the y-equation immediately gives N = mg cos θ. Gravity's component along the slope (mg sin θ) appears only in the x-equation, giving acceleration directly without simultaneous equations. The general principle is to align one axis with the direction of acceleration — this isolates the dynamics in one equation and the constraint forces in the other."
  explanation: "Smart axis choice doesn't change the physics, but it can eliminate an entire equation from the problem. This is why the methodology step 'choose axes' is not optional — a poor choice multiplies the algebra needed."
```

## Explainer

You already know two things that together make this topic powerful. From **free-body diagrams**, you know how to systematically identify and represent every force acting on an object: weight, normal force, friction, tension, applied forces — each a vector with a specific direction. From **Newton's second law**, you know that the net force on an object equals its mass times its acceleration: F_net = ma. This topic is about bridging the two — taking the forces you have drawn and turning them into equations you can solve.

The key procedural insight is that vectors must be analyzed **component by component**. If you orient your coordinate axes wisely, you can decompose every force into its x- and y-components, then write Newton's second law separately for each axis: ΣF_x = ma_x and ΣF_y = ma_y. These are two independent equations. On an inclined plane, for example, gravity acts downward — but if you orient the x-axis along the slope, gravity's component along the slope is mg sin θ (driving the block down the slope) and the component perpendicular to the slope is mg cos θ (balanced by the normal force, giving N = mg cos θ). This decomposition is what makes inclined-plane problems tractable, and it illustrates a general principle: the choice of axes is yours, and a smart choice eliminates algebra.

The connection to calculus — which you have seen in your study of **derivatives** — is what turns "equations of motion" into a real mathematical object. Acceleration is the second derivative of position with respect to time: a = d²x/dt². So ΣF_x = ma_x is really the differential equation m(d²x/dt²) = ΣF_x. In the simplest case of constant forces, you can solve this by integration: integrating once gives velocity v(t) = v₀ + at, and integrating again gives position x(t) = x₀ + v₀t + ½at². These are the kinematic equations you may have encountered before — now you understand where they come from. They are the solutions to Newton's second law under constant force, not independent postulates.

The most important practical skill is **setting up the problem correctly before solving anything**. The choice of coordinate axes matters enormously: aligning one axis with the direction of acceleration (or with the surface of contact) often eliminates one equation from the problem. A common failure is working in a rotated coordinate system but forgetting to rotate all force components — especially dangerous for friction (which acts tangent to the contact surface) and for normal forces (which act perpendicular to it). The methodology is always: draw the diagram → choose axes → decompose every force → apply ΣF = ma per axis → solve algebraically. Each step is simple; the failure mode is skipping one.
