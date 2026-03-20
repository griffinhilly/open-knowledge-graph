---
id: conservation-of-momentum
title: Conservation of Linear Momentum
domain: physics
course: classical-mechanics
prerequisites:
- id: momentum-and-impulse
  type: hard
- id: newtons-third-law
  type: hard
- id: center-of-mass
  type: soft
- id: systems-of-linear-equations
  type: soft
builds-toward:
- collisions-elastic-inelastic
tags:
- conservation-of-momentum
- isolated-system
- collisions
stage: formal-systems
status: validated
---
# Conservation of Linear Momentum

## Core Idea
In an isolated system (no net external force), the total linear momentum is constant: Σp_i = Σp_f. This follows directly from Newton's third law: internal forces between objects in the system are equal and opposite, so they cancel in the sum. Conservation of momentum is valid even when energy is not conserved (inelastic collisions), making it an indispensable tool.

## How It's Best Learned
Apply in both 1D (one equation) and 2D (two component equations) scenarios. Verify the direction of each momentum vector carefully and use consistent sign conventions.

## Common Misconceptions
- Applying momentum conservation when external forces (friction, gravity with no vertical motion cancellation) act on the system.
- Treating momentum as a scalar and ignoring direction in 2D collisions.

## Questions

```yaml
- question: "Two identical hockey pucks on frictionless ice collide head-on. Puck A moves right at 4 m/s; Puck B moves left at 2 m/s. Which quantity is definitely conserved in this collision?"
  type: multiple-choice
  options:
    - "Kinetic energy only."
    - "Both kinetic energy and momentum."
    - "Total linear momentum only."
    - "Neither kinetic energy nor momentum, because the pucks exert forces on each other."
  answer: 2
  explanation: "On frictionless ice, no external horizontal forces act on the two-puck system, so total linear momentum is conserved. Kinetic energy is conserved only in a perfectly elastic collision — it may or may not be conserved here depending on the type of collision. Momentum conservation applies regardless of whether the collision is elastic or inelastic."

- question: "In an inelastic collision between two objects, momentum is not conserved because kinetic energy is lost to heat and deformation."
  type: true-false
  answer: false
  explanation: "Momentum conservation and energy conservation are independent principles. Momentum conservation follows from Newton's third law applied to internal forces — the internal forces between the two objects are equal and opposite, so they contribute zero net impulse to the system. This holds whether or not kinetic energy is conserved. Kinetic energy can be converted to heat, sound, or deformation without violating momentum conservation."

- question: "Explain how Newton's third law guarantees that total momentum is conserved in a two-object isolated system during a collision."
  type: short-answer
  answer: "During the collision, object A exerts force F_AB on object B, and by Newton's third law, object B exerts an equal and opposite force F_BA = -F_AB on object A. The impulses over the same time interval are equal and opposite: J_AB = -J_BA. The change in momentum of A is -ΔpB, so the total change in momentum of the system is zero: the total momentum is constant."
  explanation: "This derivation makes clear that momentum conservation is not an independent law but a consequence of Newton's third law. It also explains why the system must be isolated: if external forces act (e.g., friction on one puck), those forces are not paired with equal-and-opposite reactions within the system, so they produce a net impulse that changes total momentum."
```

## Explainer

Conservation of momentum is not a separate law tacked onto Newton's mechanics — it follows directly from Newton's third law, which you already know. During any collision or interaction between two objects A and B, the force A exerts on B is equal and opposite to the force B exerts on A. These forces act for exactly the same duration (they're simultaneous), so the impulses they deliver are equal and opposite. But impulse equals change in momentum (from your work on momentum and impulse), so the change in momentum of A exactly cancels the change in momentum of B. The total momentum of the system — Σp = p_A + p_B — does not change.

The crucial condition is *isolation*: the system must experience no net external force. Internal forces (between objects within the system) always cancel in pairs by Newton's third law. External forces don't cancel this way. Friction with the ground, air resistance, a rope attached to a wall — any of these can inject momentum into the system from outside and break conservation. When you set up a momentum problem, your first step should always be identifying the system and checking whether external horizontal (or vertical, depending on the setup) forces are negligible. Frictionless ice, negligible air resistance, or very short collision times (where external impulse during the collision is small) all justify treating the system as isolated.

What makes conservation of momentum especially powerful is that it works even when kinetic energy is not conserved. In a perfectly inelastic collision where two objects stick together, kinetic energy is lost to heat and deformation — but momentum is still conserved. Many students conflate these two conservation laws and conclude that momentum can't be conserved in "messy" collisions. That's wrong: they are independent. Momentum conservation holds whenever there's no net external impulse; energy conservation (in its kinetic-energy form) holds only for elastic collisions. In most real collisions, use momentum conservation confidently and treat energy as a separate question.

In two dimensions, momentum is a vector equation, which means you get two independent equations — one for each component. If a ball moving east hits a stationary ball and they scatter at angles, the x-component of total momentum is conserved and the y-component is conserved separately. Write the vector equation first (Σp_i = Σp_f), then project onto x and y axes. The most common error in 2D is treating momentum as a scalar — adding magnitudes instead of components — which gives wrong answers whenever the objects don't move along the same line.

Finally, note the connection to the center of mass. For an isolated system, the center of mass moves at constant velocity (including staying stationary if it starts at rest). This is another way of saying total momentum is conserved: Σp = MV_cm, and if Σp doesn't change, neither does V_cm. This framing is useful in explosion problems where a stationary object breaks apart — the center of mass stays put even as the pieces fly outward.
