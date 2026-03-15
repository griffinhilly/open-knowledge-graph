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
