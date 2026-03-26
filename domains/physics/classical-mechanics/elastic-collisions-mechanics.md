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
status: validated
---

# Elastic Collisions

## Core Idea
In an elastic collision, both kinetic energy and momentum are conserved. The objects may exchange velocity components, but the total kinetic energy before and after collision is identical, meaning no energy is lost to deformation or heat.

## How It's Best Learned
Solve 1D collisions using both momentum and energy conservation simultaneously. Graph velocity before and after for different mass ratios. Extend to 2D glancing collisions.

## Common Misconceptions
Objects do not have to stick together after a collision for it to be inelastic. Elastic collisions are an idealization; real collisions always lose some energy. Equal mass elastic collisions result in complete velocity exchange only in 1D.

## Questions

```yaml
- question: "In a 1D elastic collision, a 2 kg object moving at 6 m/s collides with a stationary 2 kg object. What happens after the collision?"
  type: multiple-choice
  options:
    - "Both objects move at 3 m/s — they share the initial momentum equally"
    - "The first object continues at 6 m/s; the second stays still"
    - "The first object stops; the second moves at 6 m/s"
    - "The first object bounces back at 6 m/s; the second stays still"
  answer: 2
  explanation: "Equal-mass elastic collisions result in complete velocity exchange: the incoming object stops and the stationary one moves off at the original speed. This conserves both momentum (m×6 = m×0 + m×6) and kinetic energy (½m×36 = ½m×0 + ½m×36). Option A conserves momentum but not kinetic energy (½m×9 + ½m×9 ≠ ½m×36). Options B and D both violate momentum conservation."

- question: "A bowling ball (very large mass) rolls elastically into a stationary ping-pong ball (very small mass). Which outcome best describes what happens?"
  type: multiple-choice
  options:
    - "The bowling ball stops; the ping-pong ball moves forward at the bowling ball's original speed"
    - "The bowling ball barely slows; the ping-pong ball moves forward at roughly twice the bowling ball's speed"
    - "Both balls rebound in opposite directions with equal speeds"
    - "The bowling ball slows to half its speed; the ping-pong ball moves at three times the original speed"
  answer: 1
  explanation: "When m₁ >> m₂, the heavy object barely slows (its momentum is so large the light ball's reaction barely affects it) and the light ball launches forward at approximately twice the heavy ball's original speed. Option A describes the equal-mass case; option C would require zero net momentum initially, which is not the case here; option D overstates both the slowdown and the launch speed. These mass-ratio limiting cases are the key physical intuition anchors for collision analysis."

- question: "The relative velocity of approach equals the relative velocity of separation in any elastic collision."
  type: true-false
  answer: true
  explanation: "This elegant result follows from combining the momentum conservation equation (linear) with the kinetic energy conservation equation (quadratic). Rearranging and factoring both together yields (v₁ − v₂) = −(v₁' − v₂'): the relative velocity reverses sign but not magnitude. This is a powerful shortcut — it replaces the quadratic energy equation with a linear one, making 1D elastic collision problems much faster to solve than working with the full system of equations directly."

- question: "In a 1D elastic collision, the heavier incoming object typically stops after impact, transferring most its kinetic energy to the lighter stationary object."
  type: true-false
  answer: false
  explanation: "Complete velocity transfer (the incoming object stopping) only occurs when the two objects have equal mass. When the incoming object is heavier, it continues forward — barely slowing — while pushing the lighter object ahead at roughly twice its own speed. When the incoming object is lighter, it bounces back. Only the equal-mass case produces a full stop of the first object. The mass ratio determines what fraction of momentum and energy transfers, and only equal masses transfer everything."

- question: "Why must both momentum conservation and kinetic energy conservation be applied simultaneously to solve an elastic collision? What goes wrong if only one law is used?"
  type: short-answer
  answer: "Each conservation law alone gives one equation with two unknowns (the two final velocities), leaving the system underdetermined — infinitely many final velocity combinations satisfy either law alone. Momentum conservation is satisfied by any outcome that preserves total momentum, including objects passing through each other or sticking together. Kinetic energy conservation alone also allows multiple solutions. Only by applying both simultaneously do we get two independent equations for two unknowns, fully determining the final velocities from initial conditions."
  explanation: "This is the algebraic heart of elastic collision analysis. The uniqueness of the solution (given specific initial conditions) is what makes the elastic case so powerful: two constraints, two unknowns, fully determined. In inelastic collisions, kinetic energy is not conserved — some is lost to heat or deformation — so we need additional information (like 'objects stick together') to replace the energy constraint."
```

## Explainer

You know two conservation laws from your prerequisites: **conservation of momentum** (the total momentum of an isolated system is constant) and **conservation of kinetic energy** (in an elastic collision, the total kinetic energy before and after is identical). By themselves, each law constrains what can happen in a collision. The power of elastic collision analysis comes from applying both simultaneously: two equations, two unknowns (the final velocities of the two objects), fully determined by initial conditions.

To see the method clearly, consider two objects colliding head-on in one dimension. Let masses m₁ and m₂ have initial velocities v₁ and v₂. Conservation of momentum gives: m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'. Conservation of kinetic energy gives: ½m₁v₁² + ½m₂v₂² = ½m₁v₁'² + ½m₂v₂'². Solving this system yields exact final velocities. The algebra simplifies beautifully when you rearrange using both equations together, revealing an elegant result: the **relative velocity of approach equals the relative velocity of separation**, (v₁ − v₂) = −(v₁' − v₂'). This shortcut converts the quadratic energy equation into a linear one and is often faster in practice than solving the full system directly.

The most instructive special cases are worth internalizing as physical intuition anchors. When m₁ = m₂ (equal masses), the two objects exchange velocities completely: the moving ball stops and the stationary ball moves off at the original speed. This is what you observe in billiards (approximately) and Newton's cradle (strikingly). When m₁ >> m₂ (a bowling ball hits a ping-pong ball), the heavy object barely slows and the light object bounces off at roughly twice the heavy object's incoming speed. When m₁ << m₂ (ping-pong ball hits a wall), the light object reverses velocity while the heavy object barely moves. These limiting cases give you physical intuition that persists long after the formulas are forgotten.

It's important to remember that **elastic collisions are idealizations**. Real collisions — billiard balls, cars, even molecular impacts — lose some energy to deformation, heat, or sound. The elastic case is the theoretical limit where none is lost. Nevertheless, the idealization is enormously productive: nuclear and particle physicists regularly use elastic scattering to probe the structure of matter, because the conservation constraints are tight enough that measuring final momenta reveals information about the nature of the interaction. The same algebraic tools you apply here — extended into relativistic mechanics — remain central to frontier physics.
