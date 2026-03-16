---
id: power-and-work-rate
title: Power and Work Rate
domain: physics
course: classical-mechanics
prerequisites:
- id: work-and-energy
  type: hard
- id: derivative-as-slope-of-tangent
  type: soft
builds-toward:
- energy-dissipation-in-damped-oscillations
tags:
- energy
- rate
- power
- calculus
stage: formal-systems
status: draft
---

# Power and Work Rate

## Core Idea
Power is the rate of energy transfer: P = dW/dt. For a constant force, P = F · v cos(θ), where θ is the angle between force and velocity. Instantaneous power is F · v (dot product); average power is total work divided by time. High power requires either large force, high velocity, or both—crucial for comparing motors, engines, and human performance.

## Explainer

From your study of work and energy, you know that work is the transfer of energy by a force: W = F · d (for a constant force along the displacement). You have a complete account of *how much* energy is transferred. But physics and engineering often care equally about *how fast* energy is transferred. Two cranes might do the same total work lifting the same load, but the one that does it in half the time is doing the work twice as fast — and in practical terms that difference matters enormously. **Power** is the concept that captures this: P = dW/dt, the rate of doing work or transferring energy.

The connection to velocity comes directly from the definition of work. If a constant force F acts on an object moving with velocity v, then in a small time interval dt the object moves a displacement ds = v dt, and the work done is dW = F · ds = F · v dt. Dividing both sides by dt gives P = F · v — instantaneous power is the dot product of force and velocity. This means power depends on both how hard you push and how fast the object moves. A car engine produces the same maximum power at high speed with moderate force as at low speed with high force; the engine's gear system lets the driver trade force for speed (or vice versa) while keeping power roughly constant.

The dot product matters: only the component of force parallel to the velocity contributes to power. A force perpendicular to motion (like the normal force on a horizontal surface, or centripetal force on a circular orbit) does zero work and delivers zero power. This is a direct extension of the work-energy theorem you already know — forces perpendicular to displacement do no work, and therefore change no kinetic energy. If you have studied the derivative as a slope, notice that P = dW/dt is precisely the slope of the work-versus-time graph at any instant, and average power $\bar{P} = \Delta W / \Delta t$ is the slope of the secant line over an interval.

Units and intuition: one watt (W) equals one joule per second. A 100-watt lightbulb consumes energy at 100 J/s. A human climbing stairs at moderate pace delivers roughly 100–200 W to their own body weight. A car engine may produce 100 kilowatts (≈134 horsepower). These benchmarks help you sanity-check calculations. When solving power problems, the most common error is confusing total work with power: a small motor running for a long time can do enormous total work at low power; a brief explosive burst can deliver high power for small total work. The two quantities answer different questions, and getting them confused leads to systematically wrong answers. Power becomes essential in the next topic — energy dissipation in damped oscillations — where the rate at which the damping force removes energy, P_damp = bv², is exactly an application of the F · v formula you have just learned.
