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

## Explainer

From Newton's second law — your key prerequisite — you know that the net force on an object equals its mass times acceleration: F = ma. Gravity is simply one particular force that enters this equation, but Newton's genius was recognizing that it is *universal*: the same type of force that causes objects to **free fall** near Earth's surface governs the orbit of the Moon and the motions of the planets. Before Newton, these seemed like entirely different phenomena. The universal law of gravitation unifies them with a single equation: **F = G m₁m₂ / r²**.

The structure of the law repays careful attention. The force grows with both masses: doubling either mass doubles the force, reflecting that gravity is a mutual interaction — Earth pulls on you just as hard as you pull on Earth (Newton's third law, applied). The force weakens as the square of the distance: doubling r reduces F by a factor of four. This **inverse-square law** is not arbitrary; it reflects the geometry of space — gravitational influence spreads over the surface of an expanding sphere, whose area grows as r², so the intensity per unit area falls as 1/r². The constant G ≈ 6.674 × 10⁻¹¹ N·m²/kg² sets the overall scale of gravitational strength and must be measured experimentally.

The connection to your everyday experience of g = 9.8 m/s² follows directly. Near Earth's surface, every object of mass m experiences F = mg downward. Setting this equal to the universal law with M_E and R_E: mg = G M_E m / R_E². The mass m cancels — explaining why all objects fall at the same rate regardless of mass — and you get **g = G M_E / R_E²**. This is not a separate law; it is the universal law evaluated at Earth's surface. On the Moon, the same formula with the Moon's mass and radius gives g_Moon ≈ 1.6 m/s², one sixth of Earth's value. At altitude h above Earth's surface, r = R_E + h, so g decreases — but it never reaches zero because r is always finite.

The inverse-square form also explains orbital motion. Your study of free fall showed that a falling object accelerates toward Earth. The Moon is *also* falling toward Earth — it simply has enough horizontal velocity that Earth's curved surface "falls away" from it at the same rate, producing a stable orbit. Newton famously illustrated this with a cannonball: fire it fast enough horizontally, and the arc of its fall curves to match Earth's curvature. This insight — that orbiting is just falling in a curve — connects the gravitational force law to Kepler's laws of planetary motion, which you will study next, and opens the door to the full analysis of orbital mechanics.
