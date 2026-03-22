---
id: microscopic-ohms-law-drift-velocity
title: Microscopic Ohm's Law and Drift Velocity
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: resistivity-and-conductivity
  type: hard
- id: current-density-current-distribution
  type: hard
builds-toward:
- joule-heating-resistive-power
tags:
- microscopic transport
- drift velocity
- electron motion
stage: formal-systems
status: draft
---

# Microscopic Ohm's Law and Drift Velocity

## Core Idea
Microscopic Ohm's law states J = σE. This emerges from charge carrier motion through a medium. Carriers accelerate under the electric force but collide with atoms, reaching average drift velocity v_d = μE where μ is mobility. The conductivity σ = nq²τ/m*, where τ is collision time and m* is effective mass.

## How It's Best Learned
Estimate drift velocity in copper wire carrying household current and compare to thermal velocities. Derive σ = nq²τ/m* from classical mechanics.

## Common Misconceptions
- Electrons drift at significant light speed fractions (drift velocity is typically mm/s).
- Collision time τ is constant (it depends on temperature and impurities).
- Drift velocity is the same as thermal velocity (drift is a slow superimposed bias).

## Questions

```yaml
- question: "A student reasons: 'When I flip a light switch, the light turns on almost instantly — so electrons must be traveling through the wire at nearly the speed of light.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — electrons in a conductor move at near-light speeds when a current flows"
    - "Electrons drift at roughly 0.07 mm/s in a typical household wire; the near-instant response occurs because the electric field configuration propagates through the wire at close to the speed of light, not because electrons race from switch to bulb"
    - "The signal travels at the speed of sound in copper, which is faster than in air but far below light speed"
    - "Electrons do move quickly, but collisions with the lattice slow them to roughly half the speed of light"
  answer: 1
  explanation: "This is the central misconception about electric current. Drift velocity — the tiny net bias electrons develop in the field direction — is about 0.07 mm/s in a typical copper wire, roughly the speed of a slow ant. But the switch responds instantly because the electromagnetic field configuration (not the electrons themselves) changes at nearly the speed of light throughout the circuit simultaneously. The electrons were already in the wire; they just need to start drifting, and the signal that tells them to do so propagates near-instantly."

- question: "Using the Drude model (σ = nq²τ/m), which change would INCREASE the conductivity of a metal?"
  type: multiple-choice
  options:
    - "Raising the temperature, which increases lattice vibration and shortens the collision time τ"
    - "Adding impurities, which introduces additional scattering sites and shortens τ"
    - "Choosing a material with higher carrier density n — more conduction electrons per unit volume"
    - "Using a material with larger effective mass m*, so each carrier carries more inertia"
  answer: 2
  explanation: "Conductivity σ = nq²τ/m is larger when n (carrier density) is large, τ (collision time) is long, and m (effective mass) is small. Raising temperature shortens τ by increasing lattice vibrations — this reduces conductivity, which is why most metals become more resistive when heated. Adding impurities also shortens τ through additional scattering. Larger effective mass m* reduces how quickly carriers accelerate in the field, lowering σ. Only increasing n — having more carriers per unit volume — unambiguously increases conductivity."

- question: "The drift velocity of electrons in a metal carrying a typical household current is comparable in magnitude to their thermal velocity."
  type: true-false
  answer: false
  explanation: "Thermal velocity of conduction electrons in a metal is roughly 10⁶ m/s (about 0.3% of the speed of light). Drift velocity in a copper wire carrying 1 A through a 1 mm² cross-section is approximately 0.07 mm/s — about 10 orders of magnitude slower. The thermal motion is enormous and random, averaging to zero net flow; drift is a tiny directed bias superimposed on top of this frantic random motion. Confusing the two is the most common misconception about microscopic current."

- question: "When you flip a light switch, the light responds almost instantly not because electrons race through the wire, but because the electric field propagates through the circuit at close to the speed of light."
  type: true-false
  answer: true
  explanation: "This is the key insight linking the microscopic model to everyday experience. Electrons in the wire are always present; the switch closing changes the electric field configuration throughout the circuit almost simultaneously. This field change — not electron transport — is what propagates at near-light speed. Individual electrons drift only millimeters per second, but because the driving signal (the field) is established everywhere at once, current effectively begins flowing at every point in the circuit at nearly the same time."

- question: "Explain why increasing temperature decreases conductivity in metals, while increasing the number of conduction electrons per unit volume increases it — using the microscopic model."
  type: short-answer
  answer: "In the Drude model, conductivity σ = nq²τ/m. Temperature increases the amplitude of lattice vibrations, which causes more frequent electron-lattice collisions, shortening the average collision time τ. Shorter τ means electrons accumulate less drift velocity between collisions, so J = σE falls — conductivity decreases. Increasing carrier density n means more charges contribute to the current at any given drift velocity; even if τ and m are unchanged, more carriers means more total charge flow per unit time and area, so conductivity increases."
  explanation: "The two effects act on different parameters in the same formula. Temperature degrades τ (the collision time), which reduces each carrier's contribution to current. Carrier density n multiplies the total number of contributors. This also explains why superconductivity corresponds to τ → ∞ (no scattering whatsoever, so σ diverges), and why insulators have very low n (essentially no free carriers, so σ → 0)."
```

## Explainer

You already know that resistivity σ (or its inverse ρ) is a material property that relates current density to an applied electric field, and that current density J describes how charge flows per unit area. What the microscopic Ohm's law does is derive that relationship from first principles — starting with individual electrons and building up to the macroscopic formula J = σE. This derivation turns a phenomenological observation (Ohm's law works) into a mechanical explanation (here's why it works).

In a metal, conduction electrons are not stationary — they move at high thermal speeds (roughly 10⁶ m/s) in random directions, constantly colliding with the ion lattice. When there is no electric field, the average velocity is zero: as many electrons go left as right. Apply an electric field E and each electron accelerates: a = qE/m. But the electron doesn't accelerate freely for long — it collides with a lattice ion after an average time τ (the **collision time**, or relaxation time), which for copper at room temperature is about 25 femtoseconds. After each collision, the electron's velocity is randomized again. The result is that between collisions, a small net velocity builds up in the direction of the field; after a collision it resets. The average net velocity that survives, accumulated over the collision interval, is the **drift velocity**: v_d = (qEτ)/m.

Now count up the current. There are n charge carriers per unit volume, each carrying charge q and moving with average velocity v_d. The current density is J = nqv_d = (nq²τ/m)E. This is J = σE with conductivity σ = nq²τ/m — derived entirely from mechanics and the definition of current density. The **Drude model** packages the same physics with an effective mass m* to account for quantum corrections to electron behavior in real crystals. The key insight is that σ is large when n is large (many carriers), q is large (each carries more charge), τ is long (carriers travel far before colliding), and m is small (carriers accelerate quickly).

A crucial number to internalize: in a copper wire carrying a typical household current of 1 A with cross-section 1 mm², the drift velocity is roughly 0.07 mm/s — about the speed of a slow ant. The electrons themselves are racing around at thermal speeds a billion times faster, but those random velocities cancel and only this tiny directed bias survives. The electric field, by contrast, propagates at nearly the speed of light — which is why a light switch responds instantly even though the electrons barely crawl. Resistivity increases with temperature because higher temperatures shorten τ (more vigorous lattice vibrations cause more frequent collisions) and decreases with added impurities for the same reason. Superconductivity, by contrast, corresponds to τ → ∞: electrons propagate without scattering, and σ diverges.
