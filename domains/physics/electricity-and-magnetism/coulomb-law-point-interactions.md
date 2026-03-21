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

## Questions

```yaml
- question: "Two point charges are separated by a distance of 1 cm. The distance is then increased to 3 cm. By what factor does the electrostatic force change?"
  type: multiple-choice
  options:
    - "Decreases by a factor of 3"
    - "Decreases by a factor of 9"
    - "Increases by a factor of 9"
    - "Decreases by a factor of 6"
  answer: 1
  explanation: "Coulomb's law states F = k|q₁q₂|/r². Tripling the distance (r → 3r) replaces r² with (3r)² = 9r², so the force becomes F/9 — it decreases by a factor of 9. This is the inverse-square law: force falls as the square of the distance, not linearly. A common error is applying a linear factor of 3 rather than 3² = 9. The same inverse-square relationship governs gravity, and for the same geometric reason."

- question: "A negative charge −q is placed exactly halfway between two identical positive charges +q. What is the net electrostatic force on the negative charge?"
  type: multiple-choice
  options:
    - "Directed toward the left positive charge"
    - "Directed toward the right positive charge"
    - "Zero, because the equal attractive forces from each side cancel"
    - "Nonzero, directed away from both charges — unlike charges repel at the midpoint"
  answer: 2
  explanation: "By symmetry, each positive charge exerts an attractive force on −q of equal magnitude, but in opposite directions (one pulls left, the other pulls right). These forces cancel exactly, giving a net force of zero. This result requires careful application of the vector nature of Coulomb's law — you must compute direction as well as magnitude for each force and then add them as vectors. Option D is wrong because unlike charges always attract, not repel. The midpoint is a position of equilibrium (though unstable for transverse displacements)."

- question: "Doubling the distance between two point charges reduces the electrostatic force between them by half."
  type: true-false
  answer: false
  explanation: "The electrostatic force follows an inverse-square law: F ∝ 1/r². Doubling the distance means r → 2r, so r² → 4r², and F → F/4 — the force is reduced to one-quarter, not one-half. A linear (inverse-first-power) law would reduce force by half when distance doubles. The 1/r² dependence is fundamental and comes from the three-dimensional geometry of how influence spreads from a point source."

- question: "Unlike the gravitational force between masses, the electrostatic force between two charges can be repulsive rather than attractive."
  type: true-false
  answer: true
  explanation: "Gravity is always attractive — there is no negative mass. Electrostatic force depends on the signs of the charges: like signs (both positive or both negative) repel, opposite signs attract. This sign dependence is physically profound: it allows macroscopic matter to be electrically neutral (electrons and protons attract and bind), whereas if all matter attracted all other matter electrostatically (like gravity), neutral objects would not exist. The ability to have repulsion is what gives electricity its richness compared to gravity."

- question: "Why does the electrostatic force between point charges follow an inverse-square law? Explain the geometric reasoning rather than just citing the formula."
  type: short-answer
  answer: "A point charge exerts influence uniformly in all directions. Think of this influence as spreading outward like light from a candle. At distance r, this influence is spread over the surface area of a sphere, which is 4πr². Since the total influence is constant and the surface area grows as r², the intensity per unit area — and thus the force experienced at distance r — must fall as 1/r² to keep the total flux constant across any surrounding sphere."
  explanation: "This geometric argument is not just a heuristic — it becomes Gauss's law when formalized. Any force that propagates in three-dimensional space from a point source and obeys conservation (no 'leakage') must follow an inverse-square law, because that is the only scaling that keeps total flux constant as the sphere radius varies. Gravity obeys the same law for the same reason. The inverse-square character is a consequence of living in three spatial dimensions, not a separate empirical coincidence for each of these forces."
```

## Explainer

Coulomb's law is the electrostatic counterpart of Newton's law of gravitation — and comparing the two is the fastest way to build intuition. Both forces decrease as 1/r², meaning doubling the distance reduces the force by a factor of four. Both forces are proportional to the "charges" involved (mass for gravity, electric charge for electrostatics). The key difference is sign: gravity is always attractive, but electrostatic forces can be either attractive or repulsive depending on whether the charges are opposite or like signs. This sign dependence is everything in electricity — it is what allows neutral matter to exist and what gives the structure of atoms their stability.

From your prerequisite, you know that charge comes in discrete units of e ≈ 1.6×10⁻¹⁹ C and is conserved. Coulomb's law tells you the force that those discrete charges exert on each other. The constant k = 1/(4πε₀) ≈ 8.99×10⁹ N⋅m²/C² looks large, but keep it in perspective: a proton and electron separated by 0.053 nm (the Bohr radius of hydrogen) experience an attractive force of about 8.2×10⁻⁸ N — enormous on the atomic scale, which is why electrons are tightly bound to nuclei.

The inverse-square structure is not coincidental — it reflects a deep geometric fact. Imagine the field "influence" from a point charge spreading uniformly in all directions, like light from a candle. The surface area of a sphere grows as r², so the intensity of that influence at distance r must fall as 1/r² to conserve the total flux through any surrounding sphere. This geometric argument reappears more formally when you learn Gauss's law.

The law as stated applies to **point charges** — idealized charges concentrated at a single location. Real charged objects require summing (integrating) Coulomb contributions over all their constituent charge elements. When multiple charges are present, the **superposition principle** applies: the total force on a charge is the vector sum of individual Coulomb forces from every other charge, each computed independently. Getting the direction right — along the line joining the pair, attractive toward opposite signs, repulsive from like signs — requires care with vector components and will become the core skill in electric field calculations you build toward next.
