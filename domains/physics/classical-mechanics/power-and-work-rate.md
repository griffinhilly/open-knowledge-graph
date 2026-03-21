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

## Questions

```yaml
- question: "Two cars have identical engines producing the same power output. Car A climbs a steep hill slowly, exerting a large force. Car B drives on a flat road at high speed, exerting a small forward force. Which statement is correct?"
  type: multiple-choice
  options:
    - "Car A transfers more energy per second because the hill requires a larger force"
    - "Car B transfers more energy per second because its speed is higher"
    - "Both cars transfer energy at the same rate, since they have the same power output"
    - "Car A has greater power because it exerts more force against gravity"
  answer: 2
  explanation: "Power is the rate of energy transfer: P = F · v. Two machines with identical power output transfer energy at the same rate, even if they operate at very different forces and speeds. Car A uses high force × low velocity; Car B uses low force × high velocity — the product F · v is the same for both. Options A and D confuse force magnitude with power; a larger force does not imply a higher power output if the speed is proportionally lower."

- question: "A centripetal force keeps a satellite moving in a circular orbit at constant speed. How much power does the centripetal force deliver to the satellite?"
  type: multiple-choice
  options:
    - "P = mv²/r, since that is the centripetal force magnitude times the speed"
    - "A large positive power, because the satellite is moving at high speed"
    - "Zero, because the centripetal force is always perpendicular to the velocity"
    - "Negative power, because the centripetal force acts inward while the satellite moves tangentially outward"
  answer: 2
  explanation: "Power is P = F · v = |F||v|cos(θ), where θ is the angle between force and velocity. For circular motion, the centripetal force always points toward the center while the velocity is always tangential — these are perpendicular, so θ = 90° and cos(90°) = 0. Therefore P = 0. This is consistent with the work-energy theorem: the satellite's speed (and kinetic energy) doesn't change during uniform circular motion, confirming that no net energy is transferred. Option A multiplies the force magnitude by speed without accounting for the perpendicularity."

- question: "A machine that does twice as much total work in the same amount of time has twice the power."
  type: true-false
  answer: true
  explanation: "Average power is defined as P̄ = ΔW/Δt — total work done divided by the time interval. If two machines operate over the same time interval and one does twice the work, it is delivering energy at twice the rate, so it has twice the average power. This follows directly from the definition. Note the distinction from instantaneous power P = dW/dt = F · v, which can vary moment to moment; the statement here concerns average power over a fixed interval."

- question: "A high-power engine always does more total work than a lower-power engine."
  type: true-false
  answer: false
  explanation: "Power is the *rate* of doing work, not the total amount. A low-power motor running for a long time can do far more total work than a high-power motor that runs briefly. For example, a 1 W motor running for a year does about 31.5 MJ of work; a 1 MW motor running for 1 second does only 1 MJ. Total work equals power multiplied by time (W = P · t for constant power), so time horizon matters as much as power level. The two quantities answer different questions."

- question: "Why is instantaneous power given by the dot product F · v rather than simply the product of magnitudes |F| × |v|?"
  type: short-answer
  answer: "Only the component of force parallel to the velocity does work and transfers energy. A force perpendicular to motion — like the normal force on a surface, or centripetal force in circular motion — does no work and delivers no power, even though it may be large. The dot product F · v = |F||v|cos(θ) automatically accounts for this by including only the parallel component (|F|cos(θ)). Using the product of magnitudes alone would incorrectly count perpendicular forces as contributing to energy transfer."
  explanation: "This is a direct consequence of the definition of work: dW = F · ds. Dividing both sides by dt gives P = F · (ds/dt) = F · v. A force perpendicular to ds contributes zero to dW regardless of its magnitude, so it contributes zero to power. The dot product is not a mathematical convenience — it encodes the physical fact that energy transfer depends on alignment between force and motion."
```

## Explainer

From your study of work and energy, you know that work is the transfer of energy by a force: W = F · d (for a constant force along the displacement). You have a complete account of *how much* energy is transferred. But physics and engineering often care equally about *how fast* energy is transferred. Two cranes might do the same total work lifting the same load, but the one that does it in half the time is doing the work twice as fast — and in practical terms that difference matters enormously. **Power** is the concept that captures this: P = dW/dt, the rate of doing work or transferring energy.

The connection to velocity comes directly from the definition of work. If a constant force F acts on an object moving with velocity v, then in a small time interval dt the object moves a displacement ds = v dt, and the work done is dW = F · ds = F · v dt. Dividing both sides by dt gives P = F · v — instantaneous power is the dot product of force and velocity. This means power depends on both how hard you push and how fast the object moves. A car engine produces the same maximum power at high speed with moderate force as at low speed with high force; the engine's gear system lets the driver trade force for speed (or vice versa) while keeping power roughly constant.

The dot product matters: only the component of force parallel to the velocity contributes to power. A force perpendicular to motion (like the normal force on a horizontal surface, or centripetal force on a circular orbit) does zero work and delivers zero power. This is a direct extension of the work-energy theorem you already know — forces perpendicular to displacement do no work, and therefore change no kinetic energy. If you have studied the derivative as a slope, notice that P = dW/dt is precisely the slope of the work-versus-time graph at any instant, and average power $\bar{P} = \Delta W / \Delta t$ is the slope of the secant line over an interval.

Units and intuition: one watt (W) equals one joule per second. A 100-watt lightbulb consumes energy at 100 J/s. A human climbing stairs at moderate pace delivers roughly 100–200 W to their own body weight. A car engine may produce 100 kilowatts (≈134 horsepower). These benchmarks help you sanity-check calculations. When solving power problems, the most common error is confusing total work with power: a small motor running for a long time can do enormous total work at low power; a brief explosive burst can deliver high power for small total work. The two quantities answer different questions, and getting them confused leads to systematically wrong answers. Power becomes essential in the next topic — energy dissipation in damped oscillations — where the rate at which the damping force removes energy, P_damp = bv², is exactly an application of the F · v formula you have just learned.
