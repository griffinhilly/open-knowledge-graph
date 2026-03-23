---
id: biot-savart-field
title: Magnetic Field from Biot-Savart Law
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: magnetic-torque-dipole
  type: soft
builds-toward:
- ampere-law-field
tags:
- biot-savart
- field
- current
stage: formal-systems
status: validated
---

# Magnetic Field from Biot-Savart Law

## Core Idea
The Biot-Savart law gives magnetic field from a current element: dB⃗ = (μ₀/4π) I (d⃗ℓ × r̂) / r². Total field: B⃗ = (μ₀/4π) I ∫ (d⃗ℓ × r̂) / r². For an infinite straight wire: B = μ₀I/(2πr). For a circular loop on axis: B = μ₀IR²/[2(R² + z²)^(3/2)]. This fundamental law applies to all current distributions.

## Questions

```yaml
- question: "A long straight wire carries current in the +x direction. At a point directly above the wire (displaced in the +y direction), what is the direction of the magnetic field?"
  type: multiple-choice
  options:
    - "In the +y direction, pointing radially away from the wire (like an electric field from a positive charge)"
    - "In the +x direction, parallel to the current"
    - "In the +z direction, perpendicular to both the current direction and the radial direction"
    - "In the −y direction, pointing toward the wire"
  answer: 2
  explanation: "By the Biot-Savart law, dB ∝ dℓ × r̂. Here dℓ = x̂ (current direction) and r̂ = ŷ (from wire toward field point). The cross product x̂ × ŷ = ẑ, so B points in the +z direction. This perpendicularity — the field wrapping around the wire rather than pointing radially — is the fundamental character of magnetic fields. Unlike electric fields from charges (which point along r̂), magnetic fields from currents always point perpendicular to the radial direction."

- question: "Why does the magnetic field from an infinite straight wire fall off as 1/r rather than 1/r² like the electric field from a point charge?"
  type: multiple-choice
  options:
    - "Because magnetic fields are fundamentally weaker than electric fields at any given distance"
    - "Because the 1/r² in Biot-Savart is less accurate than Coulomb's law for extended sources"
    - "Because integrating contributions from an infinite number of current elements (each falling off as 1/r² from Biot-Savart) over the full length of the wire yields a net 1/r dependence"
    - "Because the cross product in Biot-Savart adds an extra factor of r in the denominator"
  answer: 2
  explanation: "Each infinitesimal current element contributes dB ∝ 1/r² (from the Biot-Savart denominator), exactly like Coulomb's law. But integrating over an infinite wire sums these contributions — elements far along the wire are at large distance but still contribute. The geometry of the integration effectively adds one factor of r in the numerator (from the off-axis angle), resulting in a net 1/r dependence for the complete field. This is the same reason a line charge creates a 1/r electric field, while a point charge creates 1/r²."

- question: "Magnetic field lines always form closed loops — they never begin or end on any source, in contrast to electric field lines which begin on positive charges and end on negative charges."
  type: true-false
  answer: true
  explanation: "This reflects one of Maxwell's equations: ∇·B = 0 everywhere, which means there are no magnetic monopoles. Magnetic field lines have no sources or sinks — they form closed loops encircling currents. Electric field lines, by contrast, begin on positive charges and end on negative charges (∇·E = ρ/ε₀). This topological difference between E and B is one of the fundamental asymmetries in electromagnetism."

- question: "The Biot-Savart law gives the magnetic field contribution from a current element as pointing radially away from the current, analogous to how Coulomb's law gives the electric field pointing radially away from a charge."
  type: true-false
  answer: false
  explanation: "This is the key misconception. Electric fields from charges DO point radially along r̂ (Coulomb's law: dE ∝ r̂/r²). Magnetic fields from current elements point PERPENDICULAR to both the current direction dℓ and the radial direction r̂, encoded by the cross product dℓ × r̂. This perpendicularity is not a minor geometric detail — it is the defining character of the magnetic interaction. Magnetic fields always wrap around currents rather than pointing radially outward from them."

- question: "What does ∇·B = 0 mean physically, and how does it contrast with the corresponding statement for electric fields?"
  type: short-answer
  answer: "∇·B = 0 means magnetic fields have no sources or sinks — there are no magnetic monopoles. Every magnetic field line that enters a region must also exit it; field lines form closed loops around currents rather than beginning or ending anywhere. For electric fields, ∇·E = ρ/ε₀ (Gauss's law): electric fields diverge from positive charges and converge on negative charges. Electric field lines have sources (positive charges) and sinks (negative charges), while magnetic field lines are sourceless. This is one of the deep structural asymmetries between electricity and magnetism."
  explanation: "The contrast between ∇·E ≠ 0 (in the presence of charges) and ∇·B = 0 (always) reflects the absence of magnetic monopoles in nature. Despite extensive searching, no isolated magnetic 'charge' has ever been found. The Biot-Savart law encodes this: its cross product structure guarantees that the resulting field always curls around the current and never points radially outward from it."
```

## Explainer

The Biot-Savart law is the magnetic analog of Coulomb's law: it gives the magnetic field contributed by each tiny piece of current-carrying wire. Just as Coulomb's law says a point charge contributes a field dE pointing radially outward, Biot-Savart says a current element Idℓ contributes a dB pointing *perpendicular* to both the current direction and the line from the element to the field point. The cross product dℓ × r̂ encodes this geometry: if you point your fingers in the direction of current and curl them toward r̂, your thumb points in the direction of dB. This perpendicularity is the magnetic signature — magnetic fields always curl around currents rather than pointing radially outward like electric fields from charges.

For an infinite straight wire, every element contributes a dB that circles the wire, and integration yields B = μ₀I/(2πr). This follows from the translational symmetry of the infinite wire: since the field cannot vary along the axis, it can only depend on the perpendicular distance r, and it wraps in concentric circles. For a circular loop, the on-axis result B = μ₀IR²/[2(R² + z²)^(3/2)] falls off more steeply at large z — it behaves like a **magnetic dipole** far from the loop, exactly analogous to an electric dipole's field, because contributions from opposite sides of the loop partially cancel off-axis.

The key to applying Biot-Savart is a systematic integration strategy. Choose a coordinate along the wire, express r (the displacement from each source element to your field point) as a function of that coordinate, evaluate the cross product, and integrate. For symmetric geometries, use symmetry first: for a straight wire, every element above and below the perpendicular plane contributes dB in the same circling sense, so there is no cancellation and only the magnitude integral remains. Getting the geometry of dℓ × r̂ right before integrating is the most common point of difficulty.

The deeper lesson from Biot-Savart is that **magnetic fields have no sources** — they form closed loops around currents, never beginning or ending on anything. This contrasts with electric fields, which begin on positive charges and end on negative charges. Mathematically, this means ∇·B = 0 everywhere, a symmetry you will formalize when you study Maxwell's equations in differential form. Ampere's law (the next topic) encodes the same physics more efficiently for symmetric current distributions, just as Gauss's law simplifies Coulomb for symmetric charge distributions.
