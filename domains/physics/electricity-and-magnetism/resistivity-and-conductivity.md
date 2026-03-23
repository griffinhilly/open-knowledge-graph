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
status: validated
---

# Resistivity and Conductivity of Materials

## Core Idea
Resistivity ρ quantifies how strongly a material opposes current flow. Conductivity σ = 1/ρ. The resistance of a uniform conductor is R = ρL/A where L is length and A is area. Resistivity depends on temperature, composition, and can be nonlinear at high fields. It is a fundamental material property independent of shape.

## Questions

```yaml
- question: "Two resistors are both measured at R = 10 Ω. One is made of copper (ρ ≈ 1.7×10⁻⁸ Ω·m) and the other of silicon (ρ ≈ 640 Ω·m). A student concludes they are made of equivalent conducting materials since their resistances are identical. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is right — resistance is the only property that matters for circuit behavior, so equivalent resistance means equivalent material"
    - "Resistance depends on both material resistivity and geometry via R = ρL/A; the two resistors have the same R but vastly different resistivities — their dimensions must differ by many orders of magnitude to compensate"
    - "The student should compare conductance, not resistance, when evaluating material quality"
    - "Resistivity only differs between metals and non-metals, not within the same category"
  answer: 1
  explanation: "R = ρL/A separates material properties (ρ) from geometry (L/A). A tiny copper wire and a massive silicon block can have the same resistance if their L/A ratios compensate for the ~10²⁰ difference in resistivity. Same resistance tells you about the circuit element as a whole; resistivity tells you something intrinsic about the material regardless of shape. This is why engineers select materials based on resistivity, not resistance — a material spec is geometry-independent."

- question: "A copper wire of length L and cross-sectional area A has resistance R. It is replaced by a copper wire of length 2L and cross-sectional area A/2. What is the new resistance?"
  type: multiple-choice
  options:
    - "R — resistivity is a material property, so resistance is unchanged when using the same material"
    - "2R — only the length doubled, which doubles resistance"
    - "4R — resistance scales as L/A; doubling L multiplies R by 2, and halving A multiplies R by another factor of 2, giving 4R total"
    - "R/2 — the effects of longer length and smaller area cancel each other out"
  answer: 2
  explanation: "From R = ρL/A, resistance is proportional to L and inversely proportional to A. Doubling L doubles R (longer path, more resistance). Halving A also doubles R (narrower cross-section, less room for current). Both changes increase resistance, so they compound: new R = ρ(2L)/(A/2) = 4ρL/A = 4R. A common error is thinking the changes 'cancel' because one increases length and one decreases area — but both changes increase resistance, they don't oppose each other."

- question: "A piece of copper wire and a silicon semiconductor can have the same measured resistance even though their resistivities differ by a factor of roughly 10²⁰."
  type: true-false
  answer: true
  explanation: "Yes — because R = ρL/A, the geometry (the ratio L/A) can compensate for any difference in ρ. To match the resistance of a 1 cm copper wire, a silicon sample would need an L/A ratio about 10²⁰ times smaller (much shorter or much thicker). While impractical at extremes, the principle is sound: resistance is a property of the specific physical object, while resistivity is a property of the material. Two objects with the same R can be made of completely different materials."

- question: "When temperature rises, both metals and semiconductors become better conductors, because higher temperatures increase the kinetic energy of electrons and allow them to move more freely."
  type: true-false
  answer: false
  explanation: "Metals and semiconductors behave oppositely with temperature. In metals, higher temperatures increase atomic vibrations, which scatter conduction electrons more frequently — resistivity *increases* (conductivity decreases). In semiconductors, higher temperatures excite more electrons across the band gap into the conduction band, increasing the number of charge carriers — resistivity *decreases* (conductivity increases). The temperature dependence of resistivity is a key diagnostic for identifying whether a material behaves as a metal or semiconductor."

- question: "Explain why resistivity is considered a 'material property' while resistance is not. What does the formula R = ρL/A reveal about the relationship between them?"
  type: short-answer
  answer: "Resistivity ρ is intrinsic to the material — it is the same for every sample of copper, regardless of whether you have a thin wire or a thick rod, a short piece or a long one. Resistance R, on the other hand, depends on the geometry of the specific object: longer conductors have higher resistance (R ∝ L), and wider conductors have lower resistance (R ∝ 1/A). The formula R = ρL/A cleanly separates these: ρ carries the material information, while L/A carries the geometric information. This is why engineers choose materials based on resistivity (a material spec), then calculate resistance based on the object's dimensions."
  explanation: "This separation is exactly analogous to distinguishing material density from an object's mass — density is intrinsic, mass depends on how much material you have. Resistivity is the 'density of electrical resistance' in a sense: it tells you the resistance per unit length per unit cross-section."
```

## Explainer

From Ohm's law you know that resistance R = V/I is the ratio of voltage to current for a given component. But resistance as measured in a circuit depends on the *geometry* of the component — how long it is, how thick, what cross-section. **Resistivity** ρ strips that geometry away to reveal a pure material property. A copper wire and a carbon rod may have the same measured resistance, but completely different resistivities, because their dimensions differ. Resistivity tells you something intrinsic about the material itself.

The relationship R = ρL/A makes geometric sense through two analogies from fluid flow. First, a longer pipe offers more resistance to flow than a short one — doubling the length doubles the resistance, so R ∝ L. Second, a wider pipe lets more fluid through — doubling the cross-sectional area halves the resistance, so R ∝ 1/A. The resistivity ρ is the proportionality constant that converts geometry into resistance. Alternatively, thinking in terms of **conductivity** σ = 1/ρ (higher is better at conducting), the current density **J** = σ**E** directly relates local current density to local electric field — the microscopic version of Ohm's law.

The numerical range of resistivities across materials is staggering. Copper has ρ ≈ 1.7×10⁻⁸ Ω·m; a good insulator like glass has ρ ≈ 10¹² Ω·m — a factor of roughly 10²⁰ separating them. Semiconductors like silicon sit in between and are interesting precisely because their resistivity can be tuned by temperature, doping, and applied fields. Temperature dependence is significant: for metals, resistivity increases with temperature (more atomic vibrations scatter electrons); for semiconductors and insulators, it decreases (more charge carriers become available). These are signs of different microscopic transport mechanisms.

The formula R = ρL/A also guides engineering decisions. Long, thin wires have high resistance and dissipate more power as heat (P = I²R). High-voltage power transmission reduces current I to minimize I²R losses, which is why transformers exist. Resistivity is why household extension cords have a maximum length rating, why chip designers shrink transistor dimensions, and why superconductors — materials with ρ = 0 below a critical temperature — are so valuable for applications like MRI magnets. The concept bridges atomic-scale material physics and practical circuit design.
