---
id: cyclotron-motion-and-frequency
title: Cyclotron Motion and Frequency
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lorentz-force-on-moving-charge
  type: hard
- id: circular-motion-kinematics
  type: hard
builds-toward:
- synchrotron-radiation
tags:
- magnetism
- circular motion
- charged particles
stage: formal-systems
status: draft
---

# Cyclotron Motion and Frequency

## Core Idea
A charged particle moving perpendicular to a uniform magnetic field undergoes circular motion with radius r = mv/(qB) and frequency f_c = qB/(2πm). The cyclotron frequency is independent of velocity and radius. This principle underlies cyclotron accelerators and is fundamental to plasma physics.

## How It's Best Learned
Derive the radius and frequency from Newton's second law for circular motion under Lorentz force. Trace trajectories of particles entering at different angles and speeds.

## Common Misconceptions
- Cyclotron frequency depends on velocity (it depends only on q, m, and B).
- Particles spiral outward in uniform fields (they move in circles at constant radius if v ⊥ B).
- Gyroradius is related to wavelength in the same way as in other contexts (it is not).

## Questions

```yaml
- question: "A proton enters a uniform magnetic field with speed v. A second proton enters the same field with speed 2v. Which statement correctly describes their orbital periods?"
  type: multiple-choice
  options:
    - "The second proton has twice the orbital period, since it travels a larger circle"
    - "The second proton has half the orbital period, since it moves faster"
    - "Both protons have the same orbital period — period depends only on charge-to-mass ratio and field strength, not speed"
    - "The second proton has a period √2 times larger, since radius grows with speed"
  answer: 2
  explanation: "The cyclotron period is T = 2πm/(qB), which contains no velocity term. The second proton has twice the gyroradius (r = mv/(qB) doubles when v doubles), but also travels twice as fast around that larger circle — these effects cancel exactly. T = 2πr/v = 2π(mv/qB)/v = 2πm/(qB). The common misconception is to notice the larger radius and conclude the period must be longer, forgetting that speed also increased proportionally."

- question: "Why can a cyclotron accelerator use a fixed-frequency alternating electric field to continuously accelerate particles, even as those particles gain energy and spiral outward?"
  type: multiple-choice
  options:
    - "The magnetic field increases as the particles spiral outward, compensating for the speed increase"
    - "The cyclotron frequency depends only on charge-to-mass ratio and field strength — as particles gain speed, their larger radius and higher speed cancel, keeping the orbital period constant"
    - "The electric field frequency is automatically adjusted by feedback from the particle beam"
    - "Only very slow particles can be accelerated by a cyclotron; fast particles require a different device"
  answer: 1
  explanation: "The key insight is that the cyclotron frequency f_c = qB/(2πm) is independent of velocity. As a particle gains energy and speed, its gyroradius grows — but the larger circle is traversed at proportionally higher speed, keeping the period exactly constant. A fixed-frequency electric field therefore stays in perfect resonance with the orbiting particle at every turn, continuously accelerating it. This elegant self-synchronization is the operating principle of the cyclotron. It breaks down only at relativistic speeds, where effective mass increases."

- question: "A proton moving at speed 2v in a magnetic field traces a larger circle than a proton at speed v, so the faster proton takes longer to complete one full orbit."
  type: true-false
  answer: false
  explanation: "This is the central misconception about cyclotron motion. The faster proton does trace a larger circle (r = mv/(qB) is proportional to v), but it also travels around that circle proportionally faster. The period T = 2πr/v = 2πm/(qB) — when you substitute r = mv/(qB), the v in the numerator and denominator cancel completely. The period is identical for both protons. This velocity-independence is the defining and counterintuitive feature of cyclotron motion."

- question: "Cyclotron motion eventually breaks down at relativistic particle speeds because the particle's effective mass increases with velocity, shifting the orbital frequency away from its non-relativistic value."
  type: true-false
  answer: true
  explanation: "The cyclotron frequency formula f_c = qB/(2πm) treats mass m as constant. At relativistic speeds, the effective mass increases as m_rel = γm₀ (where γ = 1/√(1 − v²/c²) increases with speed). As particles accelerate, the increasing effective mass causes the orbital period T = 2πm_rel/(qB) to grow — the particles fall out of sync with a fixed-frequency electric field. This is precisely why synchrotrons were developed: they vary the magnetic field or RF frequency to maintain resonance as the relativistic mass increases."

- question: "Derive why the cyclotron frequency is independent of a charged particle's velocity, starting from the condition that the magnetic Lorentz force provides the centripetal force."
  type: short-answer
  answer: "Setting the Lorentz force equal to the centripetal force: qvB = mv²/r. Solving for gyroradius: r = mv/(qB). The period is T = circumference/speed = 2πr/v = 2π(mv/qB)/v = 2πm/(qB). The velocity v cancels in the last step. Therefore the cyclotron frequency f_c = 1/T = qB/(2πm) contains no v — it depends only on the charge-to-mass ratio q/m and the magnetic field strength B."
  explanation: "The cancellation is exact and non-trivial: a faster particle has a larger radius (more v in the numerator of r) but also moves faster (more v in the denominator of T = 2πr/v), and these effects precisely cancel. This is not a coincidence but a consequence of the Lorentz force being linear in v — the centripetal acceleration requirement (v²/r) also contains a v that cancels with the v in the force. The result is one of the most elegant and practically important facts in classical electromagnetism."
```

## Explainer

Start from the two things you already know: the **Lorentz force** on a moving charge in a magnetic field, F = qv × B, is always perpendicular to the velocity; and from circular motion kinematics, a perpendicular force causes circular motion, requiring a centripetal force F = mv²/r directed inward. Cyclotron motion is simply what happens when these two facts collide. A charged particle moving perpendicular to a uniform magnetic field experiences a constant-magnitude force always pointed toward the center of its circular path — the magnetic force *is* the centripetal force.

Setting qvB = mv²/r and solving for the **gyroradius**: r = mv/(qB). Faster particles make larger circles; heavier particles make larger circles; stronger fields or larger charges make smaller circles. This formula is completely intuitive — radius grows with momentum and shrinks with the field's ability to bend the trajectory. Now compute the period: the particle must travel the circumference 2πr at speed v, so T = 2πr/v = 2πm/(qB). Notice that v cancels entirely. The **cyclotron frequency** f_c = qB/(2πm) depends only on the charge-to-mass ratio and field strength — not on the particle's speed.

This velocity-independence is the key insight. A slow proton and a fast proton in the same field trace circles of different sizes, but complete their orbits in exactly the same time. This is why cyclotron accelerators work: you can apply an alternating electric field at a fixed frequency and it stays in sync with the orbiting particles even as they gain energy and spiral outward. The timing never drifts because the orbital period is constant — a feature that makes the cyclotron elegantly self-synchronizing up to relativistic speeds (where the mass effectively increases and the synchrony breaks, requiring the synchrotron's variable-frequency correction).

In plasma physics, the same result defines the **Larmor radius** (gyroradius) and the **gyrofrequency** — quantities that appear throughout the description of plasma confinement, magnetic mirrors, and aurora formation. Any time charged particles travel through a magnetic field — from particle detectors to the Van Allen belts to the interior of tokamaks — the cyclotron motion framework is the first tool you reach for. The derivation is simple, the result is exact (in the non-relativistic limit), and its implications extend across an enormous range of physics.
