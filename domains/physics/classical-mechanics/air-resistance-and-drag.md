---
id: air-resistance-and-drag
title: Air Resistance, Drag Forces, and Terminal Velocity
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: free-fall
  type: hard
- id: projectile-motion
  type: soft
- id: separable-differential-equations
  type: soft
builds-toward:
- drag-coefficient-bluff-bodies
tags:
- drag
- air-resistance
- terminal-velocity
- differential-equations
stage: formal-systems
status: validated
---

# Air Resistance, Drag Forces, and Terminal Velocity

## Core Idea
A body moving through air or water feels a drag force opposite to its velocity. For very small or slow objects the drag is roughly linear in speed, F = bv. For everyday objects such as balls and skydivers it is roughly quadratic, F = ½C_dρAv². A falling object speeds up until drag balances its weight; it then moves at a constant terminal velocity.

## How It's Best Learned
Drop coffee filters stacked one, two, and four high and time their fall; the terminal speed grows with weight in a way students can measure. Then write Newton's second law with a drag term and solve the linear case by separating variables. Compare the exponential approach to terminal speed with a numerical solution for quadratic drag. Discuss which regime applies by comparing the two drag terms for a given size and speed.

## Common Misconceptions
- At terminal velocity no forces act on the object. (Gravity and drag both act; they are equal and opposite, so the net force is zero and the speed stays constant.)
- Heavier objects fall faster in every situation. (In a vacuum all objects fall with the same acceleration. With air, a heavier object of the same size and shape has a higher terminal speed.)
- Drag is always proportional to speed. (The linear form holds for small, slow objects; most everyday objects in air follow the quadratic form more closely.)

## Questions

```yaml
- question: "A skydiver falls at constant terminal velocity. Which statement is correct?"
  type: multiple-choice
  options: ["No forces act on the skydiver", "Drag is larger than the skydiver's weight", "Drag equals the skydiver's weight, so the net force is zero", "Gravity has switched off"]
  answer: 2
  explanation: "Constant velocity means zero acceleration, so the net force is zero. Drag balances weight."
- question: "An object falls with quadratic drag F = cv². A second object has the same shape and size but four times the mass. How does its terminal speed compare?"
  type: multiple-choice
  options: ["The same", "Twice as large", "Four times as large", "Sixteen times as large"]
  answer: 1
  explanation: "At terminal speed mg = cv², so v_t = √(mg/c). Four times the mass gives √4 = 2 times the terminal speed."
- question: "With linear drag, a falling object reaches exactly its terminal speed after one time constant τ = m/b."
  type: true-false
  answer: false
  explanation: "The speed is v(t) = v_t(1 − e^(−t/τ)). After one time constant it has reached about 63% of v_t. It approaches v_t only as time goes on without limit."
- question: "A 0.010 kg object experiences linear drag with b = 0.0020 kg/s. Using g = 9.8 m/s², what is its terminal speed?"
  type: short-answer
  answer: "49 m/s"
  explanation: "Setting mg = bv_t gives v_t = mg/b = (0.010 × 9.8)/0.0020 = 49 m/s."
```

## Explainer
Drag arises because a moving body must push fluid out of its way and drag fluid along its surface. Two simple models cover most cases. Linear drag, F = bv, dominates when the object is small, slow, or moving through a thick fluid. A dust grain settling in air or a small bead in honey is a good example. For a sphere in this regime, Stokes found b = 6πηR, where η is the fluid's viscosity and R the radius. Quadratic drag, F = ½C_dρAv², dominates for larger and faster objects. Here ρ is the fluid density, A the cross-sectional area, and C_d a drag coefficient near 0.5 for a smooth sphere over a wide range of speeds. A dimensionless ratio called the Reynolds number tells which regime applies; a small value means linear drag and a large value means quadratic drag.

Take a ball dropped from rest with linear drag, measuring down as positive. Newton's second law gives m dv/dt = mg − bv. As v grows, the drag grows until it equals the weight. At that point the acceleration is zero, and the speed stops changing. This terminal speed is v_t = mg/b. Separating variables and integrating gives

v(t) = v_t(1 − e^(−t/τ)), with τ = m/b.

The speed rises quickly at first and then levels off. After one τ it reaches about 63% of v_t, and after five τ it is within 1%.

With quadratic drag the balance mg = ½C_dρAv_t² gives v_t = √(2mg/(C_dρA)). The approach to terminal speed follows a hyperbolic tangent rather than an exponential, but the shape is similar. A skydiver falling belly-down reaches roughly 50 to 60 m/s. Opening a parachute increases A by a large factor, which lowers v_t to a safe landing speed of a few metres per second.

Drag also changes projectile motion. Without air, a launched ball follows a symmetric parabola, and a 45° launch gives the longest range on level ground. With drag, the ball loses horizontal speed throughout its flight, the path comes down more steeply than it went up, and the best launch angle for range falls below 45°. Most quadratic-drag trajectories have no simple formula. Students usually solve them with a short numerical integration, stepping the velocity forward in small time steps.
