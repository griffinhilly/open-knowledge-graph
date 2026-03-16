---
id: resistivity-and-conductivity
title: Resistivity and Conductivity of Materials
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-current-and-resistance
  type: hard
- id: ohms-law
  type: hard
builds-toward:
- microscopic-ohms-law-drift-velocity
tags:
- materials
- conduction
- transport properties
stage: formal-systems
status: draft
---

# Resistivity and Conductivity of Materials

## Core Idea
Resistivity ρ quantifies how strongly a material opposes current flow. Conductivity σ = 1/ρ. The resistance of a uniform conductor is R = ρL/A where L is length and A is area. Resistivity depends on temperature, composition, and can be nonlinear at high fields. It is a fundamental material property independent of shape.

## Explainer

From Ohm's law you know that resistance R = V/I is the ratio of voltage to current for a given component. But resistance as measured in a circuit depends on the *geometry* of the component — how long it is, how thick, what cross-section. **Resistivity** ρ strips that geometry away to reveal a pure material property. A copper wire and a carbon rod may have the same measured resistance, but completely different resistivities, because their dimensions differ. Resistivity tells you something intrinsic about the material itself.

The relationship R = ρL/A makes geometric sense through two analogies from fluid flow. First, a longer pipe offers more resistance to flow than a short one — doubling the length doubles the resistance, so R ∝ L. Second, a wider pipe lets more fluid through — doubling the cross-sectional area halves the resistance, so R ∝ 1/A. The resistivity ρ is the proportionality constant that converts geometry into resistance. Alternatively, thinking in terms of **conductivity** σ = 1/ρ (higher is better at conducting), the current density **J** = σ**E** directly relates local current density to local electric field — the microscopic version of Ohm's law.

The numerical range of resistivities across materials is staggering. Copper has ρ ≈ 1.7×10⁻⁸ Ω·m; a good insulator like glass has ρ ≈ 10¹² Ω·m — a factor of roughly 10²⁰ separating them. Semiconductors like silicon sit in between and are interesting precisely because their resistivity can be tuned by temperature, doping, and applied fields. Temperature dependence is significant: for metals, resistivity increases with temperature (more atomic vibrations scatter electrons); for semiconductors and insulators, it decreases (more charge carriers become available). These are signs of different microscopic transport mechanisms.

The formula R = ρL/A also guides engineering decisions. Long, thin wires have high resistance and dissipate more power as heat (P = I²R). High-voltage power transmission reduces current I to minimize I²R losses, which is why transformers exist. Resistivity is why household extension cords have a maximum length rating, why chip designers shrink transistor dimensions, and why superconductors — materials with ρ = 0 below a critical temperature — are so valuable for applications like MRI magnets. The concept bridges atomic-scale material physics and practical circuit design.
