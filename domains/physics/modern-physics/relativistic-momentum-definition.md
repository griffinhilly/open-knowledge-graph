---
id: relativistic-momentum-definition
title: Relativistic Momentum and Inertia
domain: physics
course: modern-physics
prerequisites:
- id: special-relativity-postulates
  type: hard
- id: momentum-and-impulse
  type: hard
- id: relativistic-doppler-shift
  type: soft
builds-toward:
- relativistic-kinetic-energy
tags:
- special-relativity
- momentum
- dynamics
stage: advanced
status: validated
---
# Relativistic Momentum and Inertia

## Core Idea
Relativistic momentum is defined as p = γmv, where γ is the Lorentz factor (1/√(1−v²/c²)). Unlike classical momentum, relativistic momentum approaches infinity as velocity approaches light speed, preventing any massive object from reaching c. This modification preserves momentum conservation in all inertial frames.

## Questions

```yaml
- question: "A physicist applies a constant force to an object already moving at 0.99c. Compared to applying the same force to an identical object at rest, the resulting acceleration is:"
  type: multiple-choice
  options:
    - "The same — Newton's second law F = ma holds in all inertial frames regardless of speed"
    - "Zero — no force can produce acceleration in an object moving at near-light speed"
    - "Much smaller — the object's effective inertia has grown by a factor of γ ≈ 7, so each unit of force produces far less acceleration"
    - "Larger — the force acts on a faster-moving object and therefore delivers more kinetic energy per unit time"
  answer: 2
  explanation: "Relativistic momentum p = γmv means the effective inertia resisting further acceleration is γm, not just m. At 0.99c, γ ≈ 7, so the object resists acceleration about seven times more strongly than at rest. Each additional increment of speed costs far more momentum (and energy), and those increments keep shrinking. This is not a technological limitation — it is built into the structure of relativistic dynamics."

- question: "Why is p = γmv defined as relativistic momentum rather than the classical p = mv?"
  type: multiple-choice
  options:
    - "Because γmv approaches infinity near c, preventing massive objects from reaching light speed"
    - "Because γmv reduces to mv at low speeds, providing the correct classical limit"
    - "Because γmv is the quantity conserved in all inertial frames connected by Lorentz transformations, while mv is not — it is the Lorentz-invariant definition that preserves momentum conservation across frames"
    - "Because Einstein derived it directly from the mass-energy relation E = mc²"
  answer: 2
  explanation: "The conceptual reason for the definition is conservation. Consider a symmetric collision analyzed from two inertial frames related by a Lorentz boost. Classical momentum mv is NOT conserved in both frames simultaneously. Relativistic momentum p = γmv IS. This is what singles out γmv as the correct quantity — it transforms consistently under Lorentz transformations, preserving momentum conservation in every inertial frame. The infinity-at-c consequence follows from the definition; it is not the reason for it."

- question: "Near the speed of light, a particle's rest mass increases, which is why it becomes increasingly difficult to accelerate further."
  type: true-false
  answer: false
  explanation: "Rest mass m is a Lorentz invariant — it does not change with velocity. What grows with velocity is the effective inertia γm, because the relationship between force, acceleration, and velocity is fundamentally different in relativistic dynamics. This is sometimes described using 'relativistic mass' γm, but this is a pedagogical shortcut that can mislead. The physically meaningful invariant quantity is the rest mass m; γ captures the frame-dependent dynamical effect. The increased resistance to acceleration comes from the structure of relativistic momentum, not a literal change in mass."

- question: "If you could apply infinite force to a massive object for finite time, you could in principle accelerate it to exactly the speed of light."
  type: true-false
  answer: false
  explanation: "As v → c, γ → ∞, so p = γmv → ∞. Reaching c would require infinite momentum — and delivering infinite momentum requires infinite energy, regardless of the force magnitude or duration. Even an infinite force applied for finite time delivers finite impulse (momentum change), which cannot be infinite. The speed of light is an asymptote: you can always get closer, but each step requires more energy than the last, and the final step requires infinite energy. This is a structural consequence of relativistic momentum, not a practical engineering limit."

- question: "Why can't a massive object be accelerated to the speed of light, even in principle? Frame your answer in terms of relativistic momentum."
  type: short-answer
  answer: "Relativistic momentum is p = γmv where γ = 1/√(1−v²/c²). As v approaches c, γ diverges: at 0.99c, γ ≈ 7; at 0.9999c, γ ≈ 71. The momentum p = γmv also diverges as v → c, meaning you would need infinite momentum — and thus infinite energy — to push an object to exactly c. Any finite applied force over any finite time delivers only finite momentum. The speed c is an asymptote that can be approached but never reached by a massive object. This is not a limitation of our technology but a structural consequence of how relativistic momentum grows with velocity."
  explanation: "This is also why massless particles (photons) always travel at exactly c — they are not being 'accelerated to c' but simply cannot travel at any other speed given their zero rest mass. The prohibition on massive objects reaching c and the requirement for massless objects to travel at c are two sides of the same relativistic coin."
```

## Explainer

From your study of classical momentum, you know that p = mv and that applying a constant force to an object produces a constant acceleration — doubling the force doubles the rate of velocity change. Special relativity breaks this simple picture. Once you accept the two postulates — that the laws of physics are the same in all inertial frames, and that the speed of light c is the same for all observers — a contradiction emerges: classical momentum is not conserved under Lorentz transformations. The fix requires redefining momentum in a way that respects Lorentz symmetry.

The **Lorentz factor** γ = 1/√(1−v²/c²) is the key object. At everyday speeds (v ≪ c), γ ≈ 1 and p = γmv ≈ mv — classical mechanics is recovered, which is why Newton's laws work so well for cars and baseballs. But as v approaches c, γ grows without bound. At 99% of c, γ ≈ 7; at 99.9%, γ ≈ 22. The relativistic momentum p = γmv therefore also grows without bound as v → c, even though v itself is bounded. This is the mechanism that makes c a speed limit: to accelerate a massive object to c would require infinite momentum, and thus infinite energy.

A useful way to build intuition is to think about **effective inertia**. In classical mechanics, inertia (resistance to acceleration) is simply the rest mass m. In relativity, the resistance to further acceleration grows as γm — an object already moving at 0.99c is about 7 times harder to accelerate than the same object at rest. The faster it moves, the more energy you must supply to gain each additional increment of speed, and the increments of speed you gain keep shrinking. This is not because the mass literally increases (the invariant rest mass m is constant), but because the relationship between force, acceleration, and velocity is fundamentally different.

**Momentum conservation** is the deeper reason for this definition. Consider a symmetric collision viewed from two different inertial frames. With classical momentum, the collision appears to violate conservation in one of the frames after a Lorentz boost. With relativistic momentum p = γmv, conservation holds in every inertial frame simultaneously. This is what singles out γmv as the correct definition — it is the quantity that transforms consistently under the Lorentz transformations you already know. The relativistic momentum also forms part of the **four-momentum** (E/c, p), a Lorentz four-vector, which is why relativistic energy and momentum are naturally unified — a connection you will develop next in relativistic kinetic energy.
