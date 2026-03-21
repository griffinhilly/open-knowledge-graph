---
id: newtons-law-of-gravitation
title: Newton's Law of Universal Gravitation
domain: physics
course: classical-mechanics
prerequisites:
- id: newtons-second-law
  type: hard
- id: free-fall
  type: soft
builds-toward:
- orbital-mechanics
- keplers-laws
tags:
- gravitation
- inverse-square-law
- gravitational-force
stage: formal-systems
status: validated
---

# Newton's Law of Universal Gravitation

## Core Idea
Every pair of masses attracts each other with a force proportional to the product of their masses and inversely proportional to the square of their separation: F = G m₁m₂/r². The gravitational constant G ≈ 6.674 × 10⁻¹¹ N·m²/kg². This universal law unifies terrestrial gravity (F = mg near Earth's surface) with celestial mechanics, showing that the same force that makes apples fall governs planetary orbits.

## How It's Best Learned
Derive g = GM_E/R_E² to connect the universal law to the familiar near-surface approximation. Then compute g at various heights above Earth to see how it weakens with the inverse-square dependence.

## Common Misconceptions
- Thinking gravity 'turns off' in space: gravity extends infinitely, it just weakens as 1/r².
- Believing G and g are the same quantity: G is the universal gravitational constant; g is the local gravitational field strength that depends on the planet's mass and radius.

## Questions

```yaml
- question: "Astronauts aboard the International Space Station (ISS), orbiting at about 400 km altitude, experience apparent weightlessness. What is the correct explanation?"
  type: multiple-choice
  options:
    - "At 400 km altitude, Earth's gravity is too weak to affect the astronauts measurably"
    - "The vacuum of space prevents gravitational force from being transmitted to the astronauts"
    - "The ISS and everything inside it are in free fall together, so astronauts experience no normal force from any surface"
    - "The astronauts' mass decreases in orbit, reducing the gravitational force to near zero"
  answer: 2
  explanation: "At 400 km, g is still about 90% of its surface value — gravity absolutely reaches the ISS. Weightlessness occurs because the station and everything inside it are all falling together toward Earth at the same rate. There is no surface pressing up on the astronauts, so they feel no normal force — the sensation of weight. This is the same physics as a falling elevator: all objects inside accelerate together and feel 'weightless.' This directly addresses the misconception that gravity 'turns off' in space; it merely goes undetected because there is nothing to push back against."

- question: "Why do a feather and a bowling ball fall at the same rate in a vacuum (ignoring air resistance)?"
  type: multiple-choice
  options:
    - "Gravity exerts the same force on all objects regardless of mass"
    - "The more massive object experiences a larger gravitational force, but also has proportionally more inertia — these effects cancel exactly, leaving the same acceleration"
    - "Near Earth's surface, the gravitational constant G adjusts to equalize acceleration across different masses"
    - "Gravity is a property of the gravitational field, so object mass is irrelevant to the resulting acceleration"
  answer: 1
  explanation: "From F = GM_E m / R_E², a more massive object experiences a larger gravitational force. But from Newton's second law, a = F/m. Substituting: a = GM_E m / (R_E² · m) = GM_E / R_E². The mass m cancels completely — heavier objects are pulled harder but are harder to accelerate in exactly equal measure. This is not a coincidence but a consequence of the fact that gravitational mass and inertial mass are equal (the equivalence principle). Option A is wrong: gravity does exert a larger force on the heavier object."

- question: "The gravitational acceleration at the Moon's surface is about 1/6 of Earth's because the Moon is approximately 6 times farther from Earth than the Moon's own surface is from Earth's center."
  type: true-false
  answer: false
  explanation: "The Moon's surface gravitational acceleration is g_Moon = GM_Moon / R_Moon², determined by the Moon's own mass and radius — not its distance from Earth. The Moon's mass is about 1/81 of Earth's and its radius is about 1/3.7 of Earth's. Plugging in: g_Moon ≈ (1/81)/(1/3.7)² × 9.8 ≈ 1.6 m/s², roughly 1/6 of g_Earth. The Moon's distance from Earth is irrelevant to what you feel standing on the Moon's surface."

- question: "The gravitational force Earth exerts on the Moon is greater than the force the Moon exerts on Earth, because Earth's mass is much larger."
  type: true-false
  answer: false
  explanation: "By Newton's third law, every force has an equal and opposite reaction. The gravitational force Earth exerts on the Moon and the force the Moon exerts on Earth are an action-reaction pair — they are exactly equal in magnitude and opposite in direction. Earth's greater mass means it accelerates much less (a = F/m), but the force magnitudes are identical. This is also visible in the universal law: F = Gm₁m₂/r² is symmetric in the two masses, so swapping which body is 'exerting' the force gives the same numerical result."

- question: "Derive the expression for surface gravitational acceleration g from Newton's universal law F = Gm₁m₂/r², and explain why this derivation shows that all objects fall at the same rate regardless of mass."
  type: short-answer
  answer: "For an object of mass m at Earth's surface: the gravitational force is F = GM_E m / R_E². By Newton's second law, F = ma, so GM_E m / R_E² = ma. The object's mass m cancels from both sides, giving a = GM_E / R_E² = g. Because m cancels, the acceleration is the same for every mass — a feather and a bowling ball accelerate identically under gravity alone."
  explanation: "The cancellation of m is the key step, and it relies on a deep physical fact: gravitational mass (how strongly gravity pulls on an object) and inertial mass (how much it resists acceleration) are the same quantity. This equivalence is the foundation of general relativity. Newton noticed it empirically; Einstein elevated it to a fundamental principle."
```

## Explainer

From Newton's second law — your key prerequisite — you know that the net force on an object equals its mass times acceleration: F = ma. Gravity is simply one particular force that enters this equation, but Newton's genius was recognizing that it is *universal*: the same type of force that causes objects to **free fall** near Earth's surface governs the orbit of the Moon and the motions of the planets. Before Newton, these seemed like entirely different phenomena. The universal law of gravitation unifies them with a single equation: **F = G m₁m₂ / r²**.

The structure of the law repays careful attention. The force grows with both masses: doubling either mass doubles the force, reflecting that gravity is a mutual interaction — Earth pulls on you just as hard as you pull on Earth (Newton's third law, applied). The force weakens as the square of the distance: doubling r reduces F by a factor of four. This **inverse-square law** is not arbitrary; it reflects the geometry of space — gravitational influence spreads over the surface of an expanding sphere, whose area grows as r², so the intensity per unit area falls as 1/r². The constant G ≈ 6.674 × 10⁻¹¹ N·m²/kg² sets the overall scale of gravitational strength and must be measured experimentally.

The connection to your everyday experience of g = 9.8 m/s² follows directly. Near Earth's surface, every object of mass m experiences F = mg downward. Setting this equal to the universal law with M_E and R_E: mg = G M_E m / R_E². The mass m cancels — explaining why all objects fall at the same rate regardless of mass — and you get **g = G M_E / R_E²**. This is not a separate law; it is the universal law evaluated at Earth's surface. On the Moon, the same formula with the Moon's mass and radius gives g_Moon ≈ 1.6 m/s², one sixth of Earth's value. At altitude h above Earth's surface, r = R_E + h, so g decreases — but it never reaches zero because r is always finite.

The inverse-square form also explains orbital motion. Your study of free fall showed that a falling object accelerates toward Earth. The Moon is *also* falling toward Earth — it simply has enough horizontal velocity that Earth's curved surface "falls away" from it at the same rate, producing a stable orbit. Newton famously illustrated this with a cannonball: fire it fast enough horizontally, and the arc of its fall curves to match Earth's curvature. This insight — that orbiting is just falling in a curve — connects the gravitational force law to Kepler's laws of planetary motion, which you will study next, and opens the door to the full analysis of orbital mechanics.
