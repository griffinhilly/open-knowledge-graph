---
id: keplers-laws
title: Kepler's Laws of Planetary Motion
domain: physics
course: classical-mechanics
prerequisites:
- id: orbital-mechanics
  type: hard
- id: conservation-of-angular-momentum
  type: soft
- id: conic-sections-ellipses
  type: soft
- id: polar-coordinates
  type: soft
tags:
- Kepler
- planetary-motion
- elliptical-orbit
- orbital-period
stage: formal-systems
status: validated
---

# Kepler's Laws of Planetary Motion

## Core Idea
Kepler's three empirical laws describe planetary orbits: (1) Planets move in ellipses with the Sun at one focus. (2) A line from the Sun to a planet sweeps equal areas in equal times (consequence of angular momentum conservation). (3) The square of the orbital period is proportional to the cube of the semi-major axis: T² ∝ a³ (specifically T² = 4π²a³/GM). Newton derived all three from his law of universal gravitation, showing they are not independent empirical facts but consequences of deeper physics.

## How It's Best Learned
Derive Kepler's third law for circular orbits from Newton's law of gravitation and centripetal force. Then generalize to ellipses by replacing r with the semi-major axis a. Use Kepler's second law to explain why planets move fastest at perihelion.

## Common Misconceptions
- Thinking planetary orbits are perfect circles: they are ellipses, though many planets have low eccentricity that makes them nearly circular.
- Confusing Kepler's third law: it is T² ∝ a³, not T ∝ a or T² ∝ a².
- Believing Kepler's laws only apply to planets: they apply to any two-body gravitational system (moons, comets, binary stars).

## Questions

```yaml
- question: "Planet X orbits a star with a semi-major axis of 4 AU. Planet Y orbits the same star with a semi-major axis of 1 AU. How do their orbital periods compare?"
  type: multiple-choice
  options:
    - "Planet X has a period 4 times longer, because T ∝ a"
    - "Planet X has a period 8 times longer, because T² ∝ a³ means T ∝ a^(3/2)"
    - "Planet X has a period 16 times longer, because T ∝ a²"
    - "Planet X has a period 64 times longer, because T² ∝ a³"
  answer: 1
  explanation: "Kepler's Third Law states T² ∝ a³, so T ∝ a^(3/2). With a ratio of 4:1 in semi-major axes, the period ratio is 4^(3/2) = (4³)^(1/2) = 64^(1/2) = 8. Planet X takes 8 times as long. Option A (T ∝ a, giving ratio 4) confuses the law with a linear relationship. Option C (T ∝ a², giving ratio 16) has the wrong exponent. Option D confuses T with T², applying the cube without taking the square root. Getting the exponent right — a^(3/2) on a, not a³ on T — is the key computational skill."

- question: "A planet is at aphelion (its farthest point from the Sun). At this point, the planet is moving at its fastest orbital speed."
  type: true-false
  answer: false
  explanation: "A planet moves fastest at perihelion (closest approach) and slowest at aphelion (farthest point). This follows directly from conservation of angular momentum: L = mrv = constant. When r is smallest (perihelion), v must be largest. Kepler's Second Law — equal areas in equal times — is the geometric expression of this: to sweep equal areas in equal times when close to the focus, the planet must cover a longer arc per unit time. The common confusion reverses this relationship."

- question: "Kepler discovered his three laws by deriving them mathematically from the law of gravity and Newton's laws of motion."
  type: true-false
  answer: false
  explanation: "Kepler's laws are empirical — he derived them from patient analysis of Tycho Brahe's observational data, not from theory. Newton came later and showed that all three laws could be derived from universal gravitation and his laws of motion, demonstrating they are not independent empirical facts but consequences of deeper physics. The historical sequence matters: Kepler (observation → pattern) preceded Newton (theory → derivation). Kepler did not know why his laws were true; Newton explained why."

- question: "Two moons orbit a planet, one with a semi-major axis of 100,000 km and one with a semi-major axis of 400,000 km. The outer moon has a period exactly 4 times longer than the inner moon."
  type: true-false
  answer: false
  explanation: "By Kepler's Third Law, T ∝ a^(3/2). The ratio of semi-major axes is 400,000/100,000 = 4, so the period ratio is 4^(3/2) = 8, not 4. The outer moon takes 8 times longer. A factor of 4 in the period would require a factor of 4^(2/3) ≈ 2.52 in the semi-major axis. This is the most common computational error with the third law: applying a linear or square relationship instead of the a^(3/2) relationship."

- question: "If Kepler's Third Law is T² = 4π²a³/GM, how could astronomers use it to calculate the distance to a planet before space probes existed?"
  type: short-answer
  answer: "By timing how long a planet takes to complete one full orbit (observing T through telescope observations), astronomers can solve for a: a = (GMT²/4π²)^(1/3). Since G and M (mass of the Sun) are determined from Earth's orbital data, the semi-major axis follows directly from the period. This allows calculation of planetary distances using only timing — no spacecraft needed. The ratio T²/a³ = 4π²/GM is constant for all objects orbiting the same star, so once Earth's distance (1 AU) is calibrated, all planetary distances follow from period measurements alone."
  explanation: "This is the quantitative power of the Third Law. It creates a direct algebraic bridge between an observable quantity (period, measured by timing a planet's return to the same position against the stars) and a geometric quantity (semi-major axis, the average orbital distance). Most planetary distances were calculated this way before the space age, using the constant ratio T²/a³ across all planets to bootstrap from Earth's known distance of 1 AU."
```

## Explainer

From your work on orbital mechanics, you know that a satellite in a circular orbit maintains constant speed because gravity provides exactly the centripetal force needed. Kepler's laws generalize this: real orbits are not circles but **ellipses**, and the geometry of the ellipse encodes everything about how speed and position vary over the orbit.

An ellipse has two foci. The **First Law** states that the Sun sits at one focus — not the center — of each planet's elliptical orbit. This means the planet's distance from the Sun varies continuously. The closest point is called **perihelion**; the farthest is **aphelion**. For most planets the eccentricity is small (Earth's is about 0.017), so the orbit looks nearly circular, but the Sun is still slightly off-center. For comets, eccentricity can be close to 1, producing very elongated orbits that sweep far from the Sun.

The **Second Law** — equal areas in equal times — is a direct consequence of conservation of angular momentum, which you already know. As a planet approaches perihelion, it speeds up; as it recedes toward aphelion, it slows. The reason is the same as for a spinning ice skater pulling her arms in: as radius decreases, angular velocity must increase to conserve L = mrv. Near perihelion, the planet is moving fastest; near aphelion, slowest. The swept-area law is an elegant geometric expression of this: to cover equal areas in equal times, the planet must move along the arc faster when close to the focus and slower when far.

The **Third Law**, T² = 4π²a³/GM, is the most quantitatively powerful. To derive it for a circular orbit: set gravitational force equal to centripetal force, GMm/r² = mv²/r, and substitute v = 2πr/T. Solving gives T² = 4π²r³/GM, which is already the right form with r = a for circular orbits. For ellipses, the same result holds with the semi-major axis *a* replacing *r*, a result that requires calculus to prove in full generality. The practical power is enormous: if you know the orbital period of any body in the solar system, you can immediately determine the semi-major axis of its orbit, and vice versa. This is how the distances of the planets were first calculated — using timing from telescope observations before spacecraft were ever possible.
