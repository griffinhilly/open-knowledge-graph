---
id: non-conservative-forces-dissipation
title: Non-Conservative Forces and Energy Dissipation
domain: physics
course: classical-mechanics
prerequisites:
- id: friction-forces
  type: hard
- id: conservative-vector-fields-mechanics
  type: hard
builds-toward:
- energy-dissipation-and-irreversibility
tags:
- forces
- dissipation
- irreversibility
stage: formal-systems
status: draft
---

# Non-Conservative Forces and Energy Dissipation

## Core Idea
Non-conservative forces like friction, air resistance, and viscosity convert mechanical energy into heat and internal energy. Their work is path-dependent, and mechanical energy decreases over time.

## Questions

```yaml
- question: "A 1 kg block slides 2 m across a rough floor (kinetic friction force = 3 N), then slides back 2 m to its starting position. What is the total work done by friction over the round trip?"
  type: multiple-choice
  options:
    - "0 J — the block returns to its starting position, so net displacement is zero"
    - "−12 J — friction opposes motion in both directions, doing −6 J each way"
    - "+12 J — friction does positive work when the block returns"
    - "−6 J — friction only does work on the outward leg"
  answer: 1
  explanation: "Friction always opposes motion, so it does negative work on both legs of the journey. Going forward: W = −(3 N)(2 m) = −6 J. Returning: friction now points backward (opposing the return motion), again doing W = −6 J. Total: −12 J. This is the defining behavior of non-conservative forces — unlike gravity (which does zero net work on a round trip), friction dissipates energy on every leg regardless of direction. Net displacement of zero does not mean zero work done by friction."

- question: "A student explains: 'Friction converts kinetic energy to heat, so friction violates conservation of energy — the mechanical energy lost is simply gone.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — friction does violate conservation of energy at the macroscopic scale"
    - "Friction converts mechanical energy to thermal energy (heat and internal energy of the materials), but total energy across all forms is conserved. The mechanical energy portion decreases, but thermal energy increases by exactly the same amount"
    - "The student is wrong because friction converts thermal energy into mechanical energy"
    - "The student is correct, but only for large friction forces where the effect becomes significant"
  answer: 1
  explanation: "Energy conservation holds universally — friction does not destroy energy, it converts it. When a block slides to a stop, kinetic energy becomes thermal energy: the floor and block get slightly warmer. The first law of thermodynamics ensures total energy (mechanical + thermal + internal) is constant. What friction does destroy is the *mechanical* portion of energy — it cannot be recovered as mechanical energy without external input. This is a crucial distinction: 'mechanical energy is not conserved' ≠ 'total energy is not conserved.'"

- question: "A non-conservative force cannot be described by a potential energy function because the work it does between two points depends on the path taken, not just the endpoints."
  type: true-false
  answer: true
  explanation: "True — this is the defining criterion. A conservative force has path-independent work: the work done moving from A to B is the same regardless of the route, and this is exactly what allows a potential energy function to exist (V(B) − V(A) = −W). Friction's work depends on path length, not just endpoints: the longer the path, the more friction dissipates. A round trip with friction always costs energy; the same round trip under gravity costs nothing. This path-dependence is why no potential energy function for friction exists."

- question: "A frictionless pendulum and a pendulum with air resistance are physically equivalent in energy terms, because both conserve total energy."
  type: true-false
  answer: false
  explanation: "False — they are not equivalent. A frictionless pendulum conserves total *mechanical* energy (KE + PE) and is time-reversible: playing the motion backward produces a physically valid sequence. A pendulum with air resistance continuously converts mechanical energy to thermal energy; total energy is conserved only if thermal energy is included, but the mechanical portion shrinks irreversibly. The two systems are also dynamically different: the air-resistance pendulum has a decreasing amplitude and eventually stops; the frictionless pendulum oscillates indefinitely. Physical equivalence would require them to be indistinguishable — they are not."

- question: "Explain why non-conservative forces make physical processes irreversible. What would have to happen for a block sliding to a stop due to friction to 'play backward' as a valid physical process?"
  type: short-answer
  answer: "For the motion to play backward, the thermal energy dispersed into the floor and block would need to spontaneously reconcentrate and accelerate the block — heat flowing from slightly warmer materials into organized kinetic energy. This never happens spontaneously; it would violate the second law of thermodynamics. Non-conservative forces generate a definite direction in time: the forward slide is characterized by kinetic energy converting to heat and entropy increasing. The reverse process would require entropy to decrease spontaneously. Conservative systems are time-reversible because their equations of motion are symmetric under t → −t; non-conservative dissipation breaks this symmetry, giving physical processes an arrow of time."
  explanation: "This irreversibility is the mechanical foundation of the second law — the tendency toward increased entropy in isolated systems. Every real system has some dissipation (even 'near-frictionless' systems have air resistance, internal friction, electromagnetic radiation), which is why thermodynamic irreversibility is universal. Non-conservative forces are the bridge between Newton's time-symmetric equations and the time-directed thermodynamic world we experience."
```

## Explainer

From your prerequisite on **conservative vector fields**, you know the defining property of conservative forces: the work they do is path-independent, and there exists a potential energy function V such that F = −∇V. Gravity and the spring force are conservative — any energy you "spend" lifting an object or compressing a spring is stored as potential energy and is fully recoverable. Total mechanical energy KE + PE stays constant. **Non-conservative forces** break this symmetry: the work they do depends on the path taken, not just the endpoints, and the "spent" energy does not return as mechanical energy.

**Friction** is the canonical example. When you slide a block across a floor, kinetic friction opposes motion at every instant along the path. Take the block on a round trip — push it forward 1 m, then pull it back 1 m — and friction does negative work in *both* legs of the journey. The work done going forward is −f·d; the work done going back is also −f·d. You end where you started, but you have lost 2f·d of mechanical energy. There is no potential energy function for friction because energy is not stored and recovered — it is genuinely lost to heat and sound. This is the precise meaning of path-dependence: the total work done by friction between two points depends on how you travel between them, not just the endpoints.

The energy accounting equation for systems with non-conservative forces is ΔKE + ΔPE = W_nc, where W_nc is the work done by all non-conservative forces. Because friction and drag always oppose motion, W_nc is negative, and total **mechanical energy decreases**. This "missing" mechanical energy does not vanish — it converts into **thermal energy** (heat) and internal energy of the materials. The first law of thermodynamics ensures total energy is conserved across all forms, but the mechanical portion steadily shrinks. In any real-world system — a pendulum in air, a car slowing to a stop, a ball bouncing — dissipation is always present.

The deepest consequence is **irreversibility**. A conservative system — a frictionless pendulum, an ideal spring — is time-reversible: play the motion backward and it obeys the same physical laws as forward motion. Add friction, and reversal becomes impossible: the reversed motion would require friction to spontaneously *add* energy to the system, which never happens. Dissipation gives physical processes a **direction in time**: the forward slide and the backward slide are distinguishable by the heat generated. This asymmetry is the mechanical foundation of the second law of thermodynamics — the tendency of isolated systems toward greater disorder and energy dispersal — which you will explore in the topic on energy dissipation and irreversibility. Non-conservative forces are the bridge between Newton's reversible equations of motion and the irreversible thermal world we actually inhabit.
