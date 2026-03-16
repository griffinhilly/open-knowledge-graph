---
id: impulse-momentum-particles
title: Linear Impulse-Momentum for Particles
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: dynamics-newtons-second-law
  type: hard
- id: momentum-and-impulse
  type: hard
- id: conservation-of-momentum
  type: soft
- id: work-energy-particles
  type: soft
- id: newtons-second-law
  type: hard
builds-toward:
- impact-and-restitution
tags:
- dynamics
- impulse
- momentum
- linear momentum
- time-dependent forces
stage: formal-systems
status: validated
---
# Linear Impulse-Momentum for Particles

## Core Idea
The linear impulse-momentum principle states that the time integral of net force equals the change in linear momentum: ∫F dt = mv₂ − mv₁. This method is most efficient when force is given as a function of time or when an average force must be found from a velocity change over a known time interval. If the net external impulse is zero in a given direction, linear momentum is conserved in that direction. The principle applies independently in each coordinate direction.

## How It's Best Learned
Use impulse-momentum when time is explicitly involved in the problem. Choose between work-energy and impulse-momentum based on whether the problem involves displacement (work-energy) or time interval (impulse-momentum). Apply conservation of momentum only when net external impulse is truly zero.

## Common Misconceptions
- Confusing impulse (force × time, units N·s) with work (force × displacement, units J).
- Applying momentum conservation when significant external impulses (like gravity) act during the time interval.
- Forgetting that momentum conservation applies independently per direction — conserved in x does not imply conserved in y.

## Explainer

You already know Newton's second law: F = ma. Written out, this is F = m(dv/dt). Multiply both sides by dt and integrate: ∫F dt = m·v₂ − m·v₁. That integral of force over time is the **impulse**, and the right-hand side is the change in **linear momentum** (L = mv). This impulse-momentum principle is not a new law — it is Newton's second law rewritten for problems where time is the natural variable rather than displacement.

The key decision in dynamics is choosing your method before you start. Work-energy relates force to displacement: ΔKE = ∫F·ds. Impulse-momentum relates force to time: ΔL = ∫F dt. If the problem gives you a force as a function of time (like a rocket thrust profile) or asks for an average force over a known time interval, reach for impulse-momentum. If it gives displacement or asks about speed at a certain position, reach for work-energy. Mixing the methods on the same problem is a common error. Pick the one that matches what is known and what is unknown.

When the force varies with time, the impulse is the area under the F-vs-t curve. For constant force it simplifies to F·Δt. When the problem states that an **average force** acted over a known time (as in a bat striking a ball), you can find F_avg = ΔL/Δt directly without knowing any trajectory details. This is exactly how engineers measure impact forces: measure the velocity change (with high-speed cameras or accelerometers) and the contact duration (with force plates or strain gauges), and the average impact force follows immediately.

Because momentum is a vector, the principle applies **independently in each coordinate direction**. Write separate equations for x and y (and z in 3D): (∫F_x dt = m·v₂ₓ − m·v₁ₓ), and so on. This is especially useful in oblique impacts or problems where a component of external impulse is zero in one direction but not another. If there is no external x-impulse, x-momentum is conserved — you get a free equation. If gravity acts vertically during the time interval, it contributes an impulse of mg·Δt in the y-direction; this is often small for very brief impacts (and can be neglected) but is significant for slower interactions like a ball rolling or a rocket firing over seconds.


