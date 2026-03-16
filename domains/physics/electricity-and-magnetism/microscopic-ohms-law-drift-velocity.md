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

## Explainer

You already know that resistivity σ (or its inverse ρ) is a material property that relates current density to an applied electric field, and that current density J describes how charge flows per unit area. What the microscopic Ohm's law does is derive that relationship from first principles — starting with individual electrons and building up to the macroscopic formula J = σE. This derivation turns a phenomenological observation (Ohm's law works) into a mechanical explanation (here's why it works).

In a metal, conduction electrons are not stationary — they move at high thermal speeds (roughly 10⁶ m/s) in random directions, constantly colliding with the ion lattice. When there is no electric field, the average velocity is zero: as many electrons go left as right. Apply an electric field E and each electron accelerates: a = qE/m. But the electron doesn't accelerate freely for long — it collides with a lattice ion after an average time τ (the **collision time**, or relaxation time), which for copper at room temperature is about 25 femtoseconds. After each collision, the electron's velocity is randomized again. The result is that between collisions, a small net velocity builds up in the direction of the field; after a collision it resets. The average net velocity that survives, accumulated over the collision interval, is the **drift velocity**: v_d = (qEτ)/m.

Now count up the current. There are n charge carriers per unit volume, each carrying charge q and moving with average velocity v_d. The current density is J = nqv_d = (nq²τ/m)E. This is J = σE with conductivity σ = nq²τ/m — derived entirely from mechanics and the definition of current density. The **Drude model** packages the same physics with an effective mass m* to account for quantum corrections to electron behavior in real crystals. The key insight is that σ is large when n is large (many carriers), q is large (each carries more charge), τ is long (carriers travel far before colliding), and m is small (carriers accelerate quickly).

A crucial number to internalize: in a copper wire carrying a typical household current of 1 A with cross-section 1 mm², the drift velocity is roughly 0.07 mm/s — about the speed of a slow ant. The electrons themselves are racing around at thermal speeds a billion times faster, but those random velocities cancel and only this tiny directed bias survives. The electric field, by contrast, propagates at nearly the speed of light — which is why a light switch responds instantly even though the electrons barely crawl. Resistivity increases with temperature because higher temperatures shorten τ (more vigorous lattice vibrations cause more frequent collisions) and decreases with added impurities for the same reason. Superconductivity, by contrast, corresponds to τ → ∞: electrons propagate without scattering, and σ diverges.
