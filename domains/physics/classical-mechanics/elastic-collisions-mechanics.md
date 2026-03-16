---
id: elastic-collisions-mechanics
title: Elastic Collisions
domain: physics
course: classical-mechanics
prerequisites:
- id: conservation-of-momentum
  type: hard
- id: kinetic-energy
  type: hard
builds-toward:
- inelastic-collisions
- collision-analysis-applications
- two-body-collision-center-of-mass
tags:
- collisions
- conservation
- energy
stage: formal-systems
status: draft
---

# Elastic Collisions

## Core Idea
In an elastic collision, both kinetic energy and momentum are conserved. The objects may exchange velocity components, but the total kinetic energy before and after collision is identical, meaning no energy is lost to deformation or heat.

## How It's Best Learned
Solve 1D collisions using both momentum and energy conservation simultaneously. Graph velocity before and after for different mass ratios. Extend to 2D glancing collisions.

## Common Misconceptions
Objects do not have to stick together after a collision for it to be inelastic. Elastic collisions are an idealization; real collisions always lose some energy. Equal mass elastic collisions result in complete velocity exchange only in 1D.

## Explainer

You know two conservation laws from your prerequisites: **conservation of momentum** (the total momentum of an isolated system is constant) and **conservation of kinetic energy** (in an elastic collision, the total kinetic energy before and after is identical). By themselves, each law constrains what can happen in a collision. The power of elastic collision analysis comes from applying both simultaneously: two equations, two unknowns (the final velocities of the two objects), fully determined by initial conditions.

To see the method clearly, consider two objects colliding head-on in one dimension. Let masses m₁ and m₂ have initial velocities v₁ and v₂. Conservation of momentum gives: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'. Conservation of kinetic energy gives: ½m₁v₁² + ½m₂v₂² = ½m₁v₁'² + ½m₂v₂'². Solving this system yields exact final velocities. The algebra simplifies beautifully when you rearrange using both equations together, revealing an elegant result: the **relative velocity of approach equals the relative velocity of separation**, (v₁ − v₂) = −(v₁' − v₂'). This shortcut converts the quadratic energy equation into a linear one and is often faster in practice than solving the full system directly.

The most instructive special cases are worth internalizing as physical intuition anchors. When m₁ = m₂ (equal masses), the two objects exchange velocities completely: the moving ball stops and the stationary ball moves off at the original speed. This is what you observe in billiards (approximately) and Newton's cradle (strikingly). When m₁ >> m₂ (a bowling ball hits a ping-pong ball), the heavy object barely slows and the light object bounces off at roughly twice the heavy object's incoming speed. When m₁ << m₂ (ping-pong ball hits a wall), the light object reverses velocity while the heavy object barely moves. These limiting cases give you physical intuition that persists long after the formulas are forgotten.

It's important to remember that **elastic collisions are idealizations**. Real collisions — billiard balls, cars, even molecular impacts — lose some energy to deformation, heat, or sound. The elastic case is the theoretical limit where none is lost. Nevertheless, the idealization is enormously productive: nuclear and particle physicists regularly use elastic scattering to probe the structure of matter, because the conservation constraints are tight enough that measuring final momenta reveals information about the nature of the interaction. The same algebraic tools you apply here — extended into relativistic mechanics — remain central to frontier physics.
