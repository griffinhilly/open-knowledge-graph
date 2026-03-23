---
id: stability-of-circular-orbits
title: Stability of Circular Orbits
domain: physics
course: classical-mechanics
prerequisites:
- id: orbital-elements-and-trajectories
  type: hard
- id: circular-motion-dynamics
  type: hard
tags:
- orbits
- stability
- gravitation
- dynamics
stage: formal-systems
status: validated
---

# Stability of Circular Orbits

## Core Idea
Circular orbits in a 1/r gravitational potential are stable: small radial or tangential perturbations lead to slightly elliptical orbits that remain bound, not runaway trajectories. The effective potential U_eff(r) = L²/(2μr²) − G M μ / r has a minimum at the stable circular orbit radius. This stability is specific to the 1/r force law; other force laws (e.g., f ∝ r) can be unstable.

## Questions

```yaml
- question: "A planet is nudged slightly outward from its circular orbit around a star in a 1/r² gravitational field. Which correctly describes what happens?"
  type: multiple-choice
  options:
    - "The planet spirals outward — any outward perturbation increases potential energy, making the orbit unstable"
    - "The planet's orbit becomes slightly elliptical, oscillating around the original circular radius without drifting away"
    - "The planet escapes because the gravitational force decreases at larger r, removing the restoring force"
    - "The orbit becomes elliptical and slowly precesses — the major axis rotates over many orbits"
  answer: 1
  explanation: "In a 1/r² field, the effective potential has a minimum at r₀ — the circular orbit sits at the bottom of a bowl. A small outward nudge increases U_eff, producing a restoring force that pushes r back. The orbit becomes slightly elliptical, rocking around r₀ but not departing from it. Option C is the common misconception: gravity weakening at larger r doesn't eliminate the restoring force — it's the *shape* of U_eff (a minimum) that matters, not the absolute strength of gravity. Option D is interesting: precession does occur for other force laws, but for 1/r² specifically, ω_r = ω_orbit so orbits close on themselves exactly — no precession."

- question: "Why are gravitationally bound orbits in Newtonian gravity closed ellipses rather than precessing rosettes?"
  type: multiple-choice
  options:
    - "All stable orbits under any force law are closed — stability implies closure"
    - "Because the unperturbed orbit is circular, perturbations always return to the same path without rotation"
    - "Because for the 1/r² force specifically, the radial oscillation frequency equals the orbital frequency — ω_r = ω_orbit — so the orbit traces the same path every revolution"
    - "Because Kepler's laws guarantee all bound orbits are ellipses regardless of the force law"
  answer: 2
  explanation: "The equality ω_r = ω_orbit is a special, non-generic property of the 1/r² force. When these frequencies match, the radial oscillation (r expanding and contracting) completes one full cycle in exactly the same time as one full orbit, so the orbit traces the same closed path every revolution. For other force laws, ω_r ≠ ω_orbit, and bound orbits precess — the approximate ellipse slowly rotates, tracing a rosette. Option A is false: a stable orbit can precess (stability and closure are distinct properties). Option D is wrong: Kepler's laws are specific to 1/r² and are not universal."

- question: "A circular orbit is stable if the effective potential has a minimum at the orbital radius, meaning small perturbations produce bounded oscillations rather than runaway departures."
  type: true-false
  answer: true
  explanation: "This is the central stability criterion. At the circular orbit radius r₀, U_eff has a minimum: dU_eff/dr = 0 (the circular orbit condition) and d²U_eff/dr² > 0 (stability). A small displacement from r₀ moves the orbit into a region of higher U_eff, which generates a restoring force — exactly like a ball in a bowl. The positive second derivative is the mathematical signature of stability; a maximum (negative second derivative) at r₀ would make the orbit unstable to any perturbation."

- question: "All stable circular orbits precess — the fact that Earth's orbit appears to repeat annually is due to the very slow rate of precession."
  type: true-false
  answer: false
  explanation: "Precession is not a universal feature of stable orbits. For the 1/r² force specifically, ω_r = ω_orbit, so the orbit repeats exactly after one revolution — zero precession. Earth's orbit genuinely closes annually (to high accuracy) rather than slowly rotating. Precession occurs for other force laws and for real orbits when perturbations from other planets are present (Mercury precesses noticeably), and general relativity adds an additional correction. But in a pure two-body 1/r² problem, stable orbits are exactly closed ellipses."

- question: "What does the effective potential U_eff tell us about whether a circular orbit is stable, and how does the shape of U_eff differ between force laws that allow stable circular orbits and those that don't?"
  type: short-answer
  answer: "U_eff combines the gravitational potential with the centrifugal term L²/(2μr²). A circular orbit corresponds to a minimum of U_eff. If that minimum exists and is bowl-shaped (d²U_eff/dr² > 0 at r₀), perturbations produce bounded radial oscillation — the orbit is stable. If U_eff has no local minimum (only a maximum or a monotone region), any perturbation causes runaway. The 1/r² force produces a true minimum; some force laws (F ∝ 1/rⁿ with n > 2) produce no local minimum, so stable circular orbits are impossible."
  explanation: "The effective potential framework reduces 2D orbital mechanics to a 1D stability question: is there a bowl-shaped potential minimum at the orbital radius? This geometric reasoning explains why planetary orbit stability is specific to the 1/r² force law — it depends on the particular mathematical form of Newtonian gravity, not on 'gravity' generically. General relativity slightly modifies U_eff, producing the small precession of Mercury's perihelion even in the two-body case — a measurable deviation from the perfectly-closed Newtonian ellipse."
```

## Explainer

A **circular orbit** is the simplest type of bound orbit: the radius stays constant, and the orbiting body traces a perfect circle around the central mass. It exists at the specific radius r₀ where the net radial acceleration is exactly zero — where gravitational attraction perfectly balances the centrifugal effect of circular motion. The deeper question is whether this is a **stable equilibrium**: if you slightly perturb the orbit — a small rocket burn, a passing body's tug — does the orbit remain nearly circular, or does it spiral inward or outward to disaster?

From your study of **circular motion dynamics** and **orbital elements**, you know the conditions for circular motion and the geometry of orbits. The effective potential framework connects both. Recall that in the central-force treatment, radial motion obeys the same energy equation as a 1D particle in U_eff(r) = L²/(2μr²) − GMμ/r. The circular orbit corresponds to the **minimum** of U_eff — the particle sits at the bottom of a potential energy bowl. This minimum is why circular orbits in gravity are stable: U_eff has a true minimum, not a maximum or inflection point, so a small perturbation in r causes U_eff to increase, providing a restoring force that pushes r back toward r₀. The orbit rocks gently around the circular radius rather than departing from it.

To make this quantitative, expand U_eff around r₀. At the minimum, dU_eff/dr = 0 (this is the circular orbit condition), and d²U_eff/dr² > 0 (this is the stability condition — a positive second derivative means the bottom of the bowl is concave up). The **radial oscillation frequency** ω_r = √(d²U_eff/dr² / μ), evaluated at r₀, describes how fast the radius oscillates around r₀ after a perturbation. For a 1/r² gravitational force, this radial frequency equals the orbital angular frequency: ω_r = ω_orbit. This exact equality is the reason bound gravitational orbits are **closed ellipses** — the radial oscillation completes one cycle in exactly the same time as one full orbit, so the orbit traces the same path repeatedly. This is a special, non-generic property of the 1/r² force law (and also of the harmonic oscillator potential).

For other force laws, the ratio ω_r / ω_orbit need not equal one, and bound orbits **precess** — the axis of the approximately elliptical orbit slowly rotates over many orbits, tracing a rosette pattern rather than a closed curve. This is not a sign of instability; the orbit can still be stable while precessing. True **orbital instability** occurs when the effective potential has no minimum — only a maximum or no turning point at all — meaning that any perturbation causes runaway departure. Some force laws (with n > 2, where F ∝ 1/rⁿ) produce this behavior, making stable circular orbits impossible. The stability of planetary orbits in our solar system is therefore not automatic; it depends specifically on the 1/r² character of Newtonian gravity, which gives U_eff a well-defined minimum and ensures that the planets' slightly elliptical paths remain bound for billions of years.
