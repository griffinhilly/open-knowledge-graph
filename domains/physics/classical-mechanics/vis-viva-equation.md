---
id: vis-viva-equation
title: Vis-Viva Equation
domain: physics
course: classical-mechanics
prerequisites:
- id: orbital-energy-and-escape-velocity
  type: hard
tags:
- orbits
- energy
- gravitation
- equations
stage: formal-systems
status: draft
---

# Vis-Viva Equation

## Core Idea
The vis-viva ('living force') equation relates speed v at distance r to the semi-major axis a of the orbit: v² = G M (2/r − 1/a). This compact formula directly yields orbital speed anywhere without computing the full trajectory. For circular orbits, v = √(G M / r); for ellipses, speed is highest at perihelion (closest) and lowest at aphelion (farthest).

## Explainer

From your study of **orbital energy and escape velocity** you know that the total mechanical energy of an orbiting body is the sum of kinetic energy ½mv² and gravitational potential energy -GMm/r, and that this total is conserved throughout the orbit. The vis-viva equation is simply that conservation law rearranged into a maximally useful form — it tells you the speed at any point in the orbit if you know the geometry of the orbit, without needing to track the full trajectory.

The derivation is direct. The total specific energy (energy per unit mass) of an elliptical orbit is E/m = -GM/(2a), where a is the **semi-major axis** — a fact you can derive by evaluating the energy at the two endpoints of the major axis and using conservation. Setting kinetic plus potential specific energy equal to this total: ½v² - GM/r = -GM/(2a). Solving for v² gives **v² = GM(2/r - 1/a)**. That is the vis-viva equation. It is a direct consequence of energy conservation and the geometry of a Keplerian orbit; no dynamics beyond those two ingredients are needed.

The equation's utility becomes clear when you apply it to limiting cases. For a **circular orbit** of radius r, the semi-major axis equals r, so a = r and the formula gives v² = GM(2/r - 1/r) = GM/r. This is the orbital speed for a circular orbit — exactly what you would derive by setting centripetal acceleration equal to gravitational acceleration. For an **escape trajectory** (a parabolic orbit), a → ∞ and the term 1/a vanishes, giving v_esc = √(2GM/r). The vis-viva equation smoothly interpolates between these cases as a varies from r (circle) through larger ellipses to infinity (escape) through negative values of 1/a (hyperbola, the unbound case where total energy is positive).

The speed variation around an ellipse follows directly. At **perihelion** (closest approach, r = r_min), the 2/r term is large, so v is large. At **aphelion** (farthest point, r = r_max), the 2/r term is small, so v is small. This is why comets on highly elliptical orbits move slowly near aphelion, spending most of their orbital period at large distances from the Sun, and then accelerate dramatically as they plunge inward. Halley's Comet spends nearly 70 of its 75-year period far from the Sun; the whole drama of the inner solar system visit is crammed into a few years of fast inbound and outbound motion.

The vis-viva equation is the practical workhorse of orbital mechanics. To compute the delta-v needed for a Hohmann transfer between two circular orbits, you apply vis-viva twice: once at the first burn point to find the speed needed in the transfer ellipse, and once at the second burn point to find the speed change needed to circularize. The difference from the current circular speed at each point is the required velocity impulse. Every mission design calculation that involves moving between orbits uses this equation as its foundation. Kepler's laws tell you the shape and timing of orbits; vis-viva tells you the speed at every point along them.

