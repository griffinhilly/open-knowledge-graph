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
status: draft
---

# Equations of Motion from Free Body Diagrams

## Core Idea
Once you draw a free-body diagram identifying all forces, Newton's second law F_net = ma directly yields the equations governing motion. Each coordinate direction yields one differential equation; solving these systematically gives acceleration, which you integrate to find velocity and position. This bridges the gap between force diagrams and kinematic equations.

## How It's Best Learned
Start with single-force cases, then progressively add forces (gravity + normal, then friction). Repeatedly practice: sketch diagram → identify axes → write ΣF_x = ma_x and ΣF_y = ma_y separately → solve algebraically.

## Common Misconceptions
- Assuming the normal force always equals mg; it only does so when perpendicular acceleration is zero. - Forgetting static friction can be less than μ_s N; it adjusts to prevent motion up to its maximum value. - Confusing the direction of the net force with the direction of motion; net force determines acceleration, not velocity direction.

## Explainer

You already know two things that together make this topic powerful. From **free-body diagrams**, you know how to systematically identify and represent every force acting on an object: weight, normal force, friction, tension, applied forces — each a vector with a specific direction. From **Newton's second law**, you know that the net force on an object equals its mass times its acceleration: F_net = ma. This topic is about bridging the two — taking the forces you have drawn and turning them into equations you can solve.

The key procedural insight is that vectors must be analyzed **component by component**. If you orient your coordinate axes wisely, you can decompose every force into its x- and y-components, then write Newton's second law separately for each axis: ΣF_x = ma_x and ΣF_y = ma_y. These are two independent equations. On an inclined plane, for example, gravity acts downward — but if you orient the x-axis along the slope, gravity's component along the slope is mg sin θ (driving the block down the slope) and the component perpendicular to the slope is mg cos θ (balanced by the normal force, giving N = mg cos θ). This decomposition is what makes inclined-plane problems tractable, and it illustrates a general principle: the choice of axes is yours, and a smart choice eliminates algebra.

The connection to calculus — which you have seen in your study of **derivatives** — is what turns "equations of motion" into a real mathematical object. Acceleration is the second derivative of position with respect to time: a = d²x/dt². So ΣF_x = ma_x is really the differential equation m(d²x/dt²) = ΣF_x. In the simplest case of constant forces, you can solve this by integration: integrating once gives velocity v(t) = v₀ + at, and integrating again gives position x(t) = x₀ + v₀t + ½at². These are the kinematic equations you may have encountered before — now you understand where they come from. They are the solutions to Newton's second law under constant force, not independent postulates.

The most important practical skill is **setting up the problem correctly before solving anything**. The choice of coordinate axes matters enormously: aligning one axis with the direction of acceleration (or with the surface of contact) often eliminates one equation from the problem. A common failure is working in a rotated coordinate system but forgetting to rotate all force components — especially dangerous for friction (which acts tangent to the contact surface) and for normal forces (which act perpendicular to it). The methodology is always: draw the diagram → choose axes → decompose every force → apply ΣF = ma per axis → solve algebraically. Each step is simple; the failure mode is skipping one.
