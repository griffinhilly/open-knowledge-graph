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
status: validated
---

# Vis-Viva Equation

## Core Idea
The vis-viva ('living force') equation relates speed v at distance r to the semi-major axis a of the orbit: v² = G M (2/r − 1/a). This compact formula directly yields orbital speed anywhere without computing the full trajectory. For circular orbits, v = √(G M / r); for ellipses, speed is highest at perihelion (closest) and lowest at aphelion (farthest).

## Questions

```yaml
- question: "A spacecraft is in an elliptical orbit. At which point does the vis-viva equation predict the highest orbital speed?"
  type: multiple-choice
  options:
    - "Apogee — the highest point, where gravitational potential energy is greatest"
    - "Perigee — the closest point, where r is smallest and 2/r is largest"
    - "The midpoint of the ellipse, where kinetic and potential energy are equal"
    - "Speed is constant throughout an elliptical orbit by conservation of energy"
  answer: 1
  explanation: "The vis-viva equation v² = GM(2/r − 1/a) shows speed depends directly on 2/r. At perigee (closest point), r is minimum, so 2/r is maximum, giving maximum speed. At apogee, r is maximum, so 2/r is minimum, giving minimum speed. Option D is the classic error: energy (not speed) is conserved. Conservation of energy is exactly why speed varies — as the spacecraft moves closer, gravitational potential energy decreases and kinetic energy (speed) increases."

- question: "Using v² = GM(2/r − 1/a), what is the orbital speed of a satellite in a perfectly circular orbit of radius r?"
  type: multiple-choice
  options:
    - "v = √(2GM/r) — the escape velocity formula"
    - "v = √(GM/r)"
    - "v = √(GM/2r)"
    - "v = √(2GM/a)"
  answer: 1
  explanation: "For a circular orbit, the semi-major axis equals the orbital radius: a = r. Substituting: v² = GM(2/r − 1/r) = GM(1/r), so v = √(GM/r). Option A is the escape velocity formula, which corresponds to a → ∞ (parabolic orbit). The factor-of-√2 difference between escape speed and circular orbital speed (√(2GM/r) vs √(GM/r)) means escape speed is exactly √2 ≈ 1.41 times circular orbital speed at any given radius."

- question: "The vis-viva equation is an independent law of orbital mechanics, separate from and in addition to conservation of energy."
  type: true-false
  answer: false
  explanation: "The vis-viva equation is simply conservation of energy rearranged. Starting from ½v² − GM/r = −GM/(2a) (total specific orbital energy), solving for v² gives v² = GM(2/r − 1/a). No new physics is introduced — only algebra applied to the energy conservation equation. Understanding vis-viva as a restatement of energy conservation is the key insight: any change in orbital geometry (r and a) changes speed in a predictable way because energy is conserved throughout the orbit."

- question: "For an escape trajectory (parabolic orbit), the semi-major axis a approaches infinity, so the term 1/a vanishes and vis-viva gives escape speed v_esc = √(2GM/r)."
  type: true-false
  answer: true
  explanation: "As the orbit grows larger (more elongated), a → ∞ and total orbital energy −GM/(2a) → 0 (just barely bound). At this limit, vis-viva gives v² = GM(2/r − 0) = 2GM/r, so v_esc = √(2GM/r). The formula interpolates smoothly: circular orbit (a = r) gives v = √(GM/r); larger ellipses (a > r) give higher speed at any given r; parabolic orbit (a → ∞) gives v = √(2GM/r) = √2 × circular speed."

- question: "Explain using the vis-viva equation why an orbiting body moves faster at perihelion than at aphelion. What does this imply about how a comet on a highly elliptical orbit spends its time?"
  type: short-answer
  answer: "The vis-viva equation v² = GM(2/r − 1/a) shows that speed increases as r decreases, since 2/r grows when r shrinks. At perihelion r is smallest, giving maximum speed; at aphelion r is largest, giving minimum speed. For a highly elliptical orbit, the speed at perihelion is enormously faster than at aphelion. A comet therefore moves through the inner solar system rapidly but crawls through the outer solar system — spending most of its orbital period near aphelion, where it moves slowest."
  explanation: "This is why Halley's Comet spends roughly 70 of its 75-year period far from the Sun. The comet's fast, visible passage through the inner solar system occupies only a few years; the remaining decades are spent slowly traversing the outer solar system near aphelion. The same physics governs spacecraft: a Hohmann transfer ellipse has its fastest point at closest approach, which is why burn timing and placement are critical for efficient orbital mechanics. The vis-viva equation makes this speed-distance relationship immediately quantitative."
```

## Explainer

From your study of **orbital energy and escape velocity** you know that the total mechanical energy of an orbiting body is the sum of kinetic energy ½mv² and gravitational potential energy -GMm/r, and that this total is conserved throughout the orbit. The vis-viva equation is simply that conservation law rearranged into a maximally useful form — it tells you the speed at any point in the orbit if you know the geometry of the orbit, without needing to track the full trajectory.

The derivation is direct. The total specific energy (energy per unit mass) of an elliptical orbit is E/m = -GM/(2a), where a is the **semi-major axis** — a fact you can derive by evaluating the energy at the two endpoints of the major axis and using conservation. Setting kinetic plus potential specific energy equal to this total: ½v² - GM/r = -GM/(2a). Solving for v² gives **v² = GM(2/r - 1/a)**. That is the vis-viva equation. It is a direct consequence of energy conservation and the geometry of a Keplerian orbit; no dynamics beyond those two ingredients are needed.

The equation's utility becomes clear when you apply it to limiting cases. For a **circular orbit** of radius r, the semi-major axis equals r, so a = r and the formula gives v² = GM(2/r - 1/r) = GM/r. This is the orbital speed for a circular orbit — exactly what you would derive by setting centripetal acceleration equal to gravitational acceleration. For an **escape trajectory** (a parabolic orbit), a → ∞ and the term 1/a vanishes, giving v_esc = √(2GM/r). The vis-viva equation smoothly interpolates between these cases as a varies from r (circle) through larger ellipses to infinity (escape) through negative values of 1/a (hyperbola, the unbound case where total energy is positive).

The speed variation around an ellipse follows directly. At **perihelion** (closest approach, r = r_min), the 2/r term is large, so v is large. At **aphelion** (farthest point, r = r_max), the 2/r term is small, so v is small. This is why comets on highly elliptical orbits move slowly near aphelion, spending most of their orbital period at large distances from the Sun, and then accelerate dramatically as they plunge inward. Halley's Comet spends nearly 70 of its 75-year period far from the Sun; the whole drama of the inner solar system visit is crammed into a few years of fast inbound and outbound motion.

The vis-viva equation is the practical workhorse of orbital mechanics. To compute the delta-v needed for a Hohmann transfer between two circular orbits, you apply vis-viva twice: once at the first burn point to find the speed needed in the transfer ellipse, and once at the second burn point to find the speed change needed to circularize. The difference from the current circular speed at each point is the required velocity impulse. Every mission design calculation that involves moving between orbits uses this equation as its foundation. Kepler's laws tell you the shape and timing of orbits; vis-viva tells you the speed at every point along them.

