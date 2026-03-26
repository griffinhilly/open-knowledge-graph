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

## Questions

```yaml
- question: "A rocket motor applies a varying thrust force to a spacecraft over 20 seconds. What is the most direct method to find the spacecraft's change in velocity?"
  type: multiple-choice
  options:
    - "Use kinematics: find instantaneous acceleration from F = ma at each moment, then integrate twice"
    - "Use work-energy: calculate the work done by thrust over the displacement traveled"
    - "Use impulse-momentum: compute the integral of force over time (area under the F-vs-t curve) and divide by mass"
    - "Use conservation of energy: set the initial kinetic energy equal to the work done by thrust"
  answer: 2
  explanation: "When force is given as a function of time, impulse-momentum is the natural method: Δv = (∫F dt)/m. The impulse is simply the area under the F-vs-t curve. Work-energy would require knowing force as a function of position — much harder here. The explainer states the method-selection rule directly: 'If the problem gives you a force as a function of time... reach for impulse-momentum.' Time as the key variable → impulse-momentum; displacement as the key variable → work-energy."

- question: "A bat strikes a baseball over a contact time of 0.002 s, changing its momentum by 15 kg·m/s. An observer then argues 'momentum was conserved because the collision was brief.' What key condition is actually required for momentum conservation?"
  type: multiple-choice
  options:
    - "The collision must be perfectly elastic — kinetic energy must also be conserved"
    - "Net external impulse must be zero in the direction of interest during the time interval"
    - "Both objects must have the same mass for momentum exchange to balance"
    - "One object must be stationary before the collision"
  answer: 1
  explanation: "Momentum conservation requires that net external impulse (∫F_external dt) be zero in the relevant direction. During the bat-ball collision, the bat and ball exert equal and opposite internal forces on each other — but the bat is swung by a player and connected to the ground through arms and legs, providing substantial external impulse. The system's momentum is not conserved. The collision being brief reduces gravitational impulse but doesn't eliminate the bat's external driving force. 'Brief' and 'conserved' are not synonyms."

- question: "The impulse-momentum principle applies independently in each coordinate direction, so linear momentum can be conserved in the x-direction while not conserved in the y-direction."
  type: true-false
  answer: true
  explanation: "Momentum is a vector, and the impulse-momentum principle gives separate equations per direction: ∫F_x dt = Δ(mv_x) and ∫F_y dt = Δ(mv_y). If there is no external horizontal impulse (no friction, no horizontal applied force), x-momentum is conserved. If gravity acts vertically throughout the interaction, it contributes an impulse mg·Δt in the y-direction, so y-momentum is not conserved. The explainer states: 'conserved in x does not imply conserved in y.'"

- question: "In impulse-momentum analysis, the impulse due to gravity can generally be neglected because collisions happen too quickly for gravity to have any effect."
  type: true-false
  answer: false
  explanation: "Whether gravitational impulse is negligible depends entirely on the duration of the interaction. For very brief impacts — a bat-ball contact of ~0.001 s — the gravitational impulse mg·Δt is tiny compared to the contact impulse and can be neglected. But for slower interactions lasting seconds — a rocket firing, two skaters pushing apart, a ball rolling — mg·Δt accumulates to a significant value. The explainer distinguishes these cases explicitly: gravitational impulse 'is often small for very brief impacts... but is significant for slower interactions.'"

- question: "Why is the impulse-momentum method preferred over directly applying Newton's second law (F = ma) when a force varies with time?"
  type: short-answer
  answer: "Impulse-momentum directly integrates force over time to get momentum change in one step: ΔL = ∫F dt, so Δv = ΔL/m. Applying F = ma to a time-varying force would require computing acceleration as a function of time and then integrating again to get velocity — two integration steps instead of one. Impulse-momentum matches the problem structure: when the input is a force-vs-time relationship and the output is a velocity change, the method's variables align perfectly with the given information."
  explanation: "Both methods are mathematically equivalent — impulse-momentum is simply Newton's second law integrated once over time. The practical advantage is that impulse-momentum bypasses acceleration entirely. This is especially powerful for impact problems where average force is measured from a known velocity change and a measured contact time: F_avg = ΔL/Δt requires no trajectory information at all."
```

## Explainer

You already know Newton's second law: F = ma. Written out, this is F = m(dv/dt). Multiply both sides by dt and integrate: ∫F dt = m·v₂ − m·v₁. That integral of force over time is the **impulse**, and the right-hand side is the change in **linear momentum** (L = mv). This impulse-momentum principle is not a new law — it is Newton's second law rewritten for problems where time is the natural variable rather than displacement.

The key decision in dynamics is choosing your method before you start. Work-energy relates force to displacement: ΔKE = ∫F·ds. Impulse-momentum relates force to time: ΔL = ∫F dt. If the problem gives you a force as a function of time (like a rocket thrust profile) or asks for an average force over a known time interval, reach for impulse-momentum. If it gives displacement or asks about speed at a certain position, reach for work-energy. Mixing the methods on the same problem is a common error. Pick the one that matches what is known and what is unknown.

When the force varies with time, the impulse is the area under the F-vs-t curve. For constant force it simplifies to F·Δt. When the problem states that an **average force** acted over a known time (as in a bat striking a ball), you can find F_avg = ΔL/Δt directly without knowing any trajectory details. This is exactly how engineers measure impact forces: measure the velocity change (with high-speed cameras or accelerometers) and the contact duration (with force plates or strain gauges), and the average impact force follows immediately.

Because momentum is a vector, the principle applies **independently in each coordinate direction**. Write separate equations for x and y (and z in 3D): (∫F_x dt = m·v₂ₓ − m·v₁ₓ), and so on. This is especially useful in oblique impacts or problems where a component of external impulse is zero in one direction but not another. If there is no external x-impulse, x-momentum is conserved — you get a free equation. If gravity acts vertically during the time interval, it contributes an impulse of mg·Δt in the y-direction; this is often small for very brief impacts (and can be neglected) but is significant for slower interactions like a ball rolling or a rocket firing over seconds.


