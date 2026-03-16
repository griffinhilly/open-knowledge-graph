---
id: coulomb-law-point-interactions
title: Coulomb's Law for Point Charges
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: elementary-charge-conservation
  type: hard
- id: inverse-square-law
  type: soft
builds-toward:
- electric-field-superposition-principle
- electric-field-point-charges
tags:
- force
- point-charges
- law
stage: formal-systems
status: draft
---

# Coulomb's Law for Point Charges

## Core Idea
Coulomb's law states that the electrostatic force between two point charges q₁ and q₂ separated by distance r is F = k|q₁q₂|/r², where k ≈ 8.99×10⁹ N⋅m²/C². The force is attractive if charges have opposite signs, repulsive if same sign, and acts along the line joining them.

## Explainer

Coulomb's law is the electrostatic counterpart of Newton's law of gravitation — and comparing the two is the fastest way to build intuition. Both forces decrease as 1/r², meaning doubling the distance reduces the force by a factor of four. Both forces are proportional to the "charges" involved (mass for gravity, electric charge for electrostatics). The key difference is sign: gravity is always attractive, but electrostatic forces can be either attractive or repulsive depending on whether the charges are opposite or like signs. This sign dependence is everything in electricity — it is what allows neutral matter to exist and what gives the structure of atoms their stability.

From your prerequisite, you know that charge comes in discrete units of e ≈ 1.6×10⁻¹⁹ C and is conserved. Coulomb's law tells you the force that those discrete charges exert on each other. The constant k = 1/(4πε₀) ≈ 8.99×10⁹ N⋅m²/C² looks large, but keep it in perspective: a proton and electron separated by 0.053 nm (the Bohr radius of hydrogen) experience an attractive force of about 8.2×10⁻⁸ N — enormous on the atomic scale, which is why electrons are tightly bound to nuclei.

The inverse-square structure is not coincidental — it reflects a deep geometric fact. Imagine the field "influence" from a point charge spreading uniformly in all directions, like light from a candle. The surface area of a sphere grows as r², so the intensity of that influence at distance r must fall as 1/r² to conserve the total flux through any surrounding sphere. This geometric argument reappears more formally when you learn Gauss's law.

The law as stated applies to **point charges** — idealized charges concentrated at a single location. Real charged objects require summing (integrating) Coulomb contributions over all their constituent charge elements. When multiple charges are present, the **superposition principle** applies: the total force on a charge is the vector sum of individual Coulomb forces from every other charge, each computed independently. Getting the direction right — along the line joining the pair, attractive toward opposite signs, repulsive from like signs — requires care with vector components and will become the core skill in electric field calculations you build toward next.
