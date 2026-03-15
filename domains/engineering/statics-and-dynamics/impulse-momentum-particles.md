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
