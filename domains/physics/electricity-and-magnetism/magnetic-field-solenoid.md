---
id: magnetic-field-solenoid
title: Magnetic Fields in Solenoids and Toroids
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: ampere-law-field
  type: hard
builds-toward:
- self-inductance
tags:
- solenoid
- toroid
- field
stage: formal-systems
status: validated
---

# Magnetic Fields in Solenoids and Toroids

## Core Idea
A solenoid with N turns, length ℓ, and cross-sectional area A produces a uniform field B = μ₀nI = μ₀NI/ℓ inside, and essentially zero outside (ideal solenoid). A toroid has field B = μ₀NI/(2πr) at radius r in the toroidal cross-section, zero outside. These geometries confine magnetic fields efficiently and are fundamental to transformers, electromagnets, and inductors.

## Questions

```yaml
- question: "A long solenoid has 1000 turns per meter carrying 2 A. You measure the magnetic field at the central axis and then at a point 3 cm off-axis but still well inside the solenoid. What do you find?"
  type: multiple-choice
  options:
    - "The field is stronger on the axis — it falls off toward the edges like a bar magnet"
    - "The field is the same at both points — it is uniform throughout the interior of an ideal solenoid"
    - "The field is weaker off-axis because that point is closer to one side of the winding"
    - "The field varies sinusoidally from one end of the solenoid to the other"
  answer: 1
  explanation: "The derivation via Ampère's law shows B = μ₀nI inside an ideal solenoid — this result contains no positional dependence. The rectangular Amperian loop argument works regardless of where inside the solenoid the loop is placed, so the field is the same everywhere in the interior. This uniformity is precisely what makes solenoids useful for applications requiring a controlled, homogeneous magnetic field (like MRI machines). Outside the solenoid, the field is essentially zero."

- question: "An engineer needs a magnetic device that produces effectively zero field outside its volume so it won't interfere with neighboring circuits. Which geometry is preferable?"
  type: multiple-choice
  options:
    - "A solenoid, since its external field is approximately zero for a long solenoid"
    - "A toroid, since the geometry completely confines the magnetic field within the toroidal volume"
    - "Both confine the field equally well — the toroid is chosen only for its compact shape"
    - "A longer solenoid, which progressively reduces fringe fields at the ends"
  answer: 1
  explanation: "A toroid confines the field exactly to zero outside: any Amperian circle outside the toroid encloses equal amounts of current going in opposite directions, so the net enclosed current is zero and B = 0 exactly. A solenoid is only approximately zero outside (ideal solenoid: zero; real solenoid: small fringe fields at the ends). For applications where stray fields would cause interference — like inductors in electronic circuits or transformer cores — the toroid's exact confinement makes it the correct choice."

- question: "Doubling the current through a solenoid while keeping the number of turns per unit length constant will double the magnetic field inside the solenoid."
  type: true-false
  answer: true
  explanation: "B = μ₀nI — the field is directly proportional to both n (turns per unit length) and I (current). All other factors held constant, doubling I doubles B. This linear relationship is what makes solenoids precisely controllable: you can dial in a specific target field by adjusting current. The same linear scaling holds for changing n, allowing engineers to tune either the winding density or the current to achieve a desired field strength."

- question: "The magnetic field inside a toroid is uniform throughout the toroidal cross-section, just as the field inside an ideal solenoid is uniform along its length."
  type: true-false
  answer: false
  explanation: "The field inside a toroid is NOT uniform — it varies as 1/r, where r is the distance from the central axis. B = μ₀NI/(2πr), so the field is strongest at the inner radius of the torus and weakest at the outer radius. In contrast, the solenoid's field is uniform everywhere inside. This non-uniformity in toroids is a practical consideration: for applications requiring a truly uniform field, a solenoid is better; for applications requiring complete external confinement, a toroid is better."

- question: "Why does a solenoid produce a uniform magnetic field inside while a toroid does not? What about their geometries accounts for this difference?"
  type: short-answer
  answer: "A solenoid is geometrically uniform along its axis: the Amperian rectangle argument gives B = μ₀nI with no dependence on position within the solenoid. A toroid is a solenoid bent into a ring, so the Amperian loop is a circle of radius r. Since circumference = 2πr, the Ampère's law equation B·(2πr) = μ₀NI gives B = μ₀NI/(2πr), which decreases with radius. The inner edge of the toroid is at a shorter radius than the outer edge, so the field is stronger at the inner edge."
  explanation: "The key is that symmetry determines what the Amperian loop integral looks like. For the solenoid, a rectangular loop gives B·L = μ₀·(nL)·I regardless of where L is placed — no r-dependence. For the toroid, a circular loop of different radii encloses the same total current NI but has different circumferences, so B must vary with r to satisfy Ampère's law."
```

## Explainer

From Ampère's law, you know that the line integral of B around any closed path equals μ₀ times the total current threading through that path: ∮B·dl = μ₀I_enc. The solenoid and toroid are the two canonical geometries where a clever choice of Amperian loop reduces this integral to a trivial calculation, much as a Gaussian sphere reduces Gauss's law to a single multiplication.

For a **solenoid** — a tightly wound helix of N turns, length ℓ — draw a rectangular Amperian loop with one long side inside the solenoid and one outside. Along the inside, B is uniform and parallel to the loop edge, contributing B·ℓ_side. Along the outside, B is essentially zero (the fields from opposite sides of the helix cancel for an ideal solenoid, and field lines form closed loops that spread out far from the solenoid). The two short sides contribute nothing because B is perpendicular to them. The total current threading the loop is I times the number of turns in the rectangle, which is n·ℓ_side where n = N/ℓ is the turn density. Setting B·ℓ_side = μ₀·n·ℓ_side·I gives B = μ₀nI. The field inside is **perfectly uniform** — independent of position along the axis — and the field outside is zero. This makes solenoids ideal field-generation devices for applications requiring a controlled, uniform magnetic field.

A **toroid** is a solenoid bent into a closed ring. Now the Amperian loop is a circle at radius r centered on the axis. By symmetry, B must be constant in magnitude and tangent to the circle everywhere. The enclosed current is N·I (all N turns thread through), so B·(2πr) = μ₀NI, giving B = μ₀NI/(2πr). The field is confined entirely within the toroidal volume and is not uniform — it varies as 1/r, being strongest at the inner radius. Outside the toroid, any Amperian circle encloses zero net current (every turn contributes both an inward and an outward threading as you go around), so B = 0 exactly. The complete confinement of the field is what makes toroids essential in transformers and inductors where stray fields would interfere with neighboring circuits.

The key conceptual thread is that these geometries convert the continuous current distribution into a problem with high symmetry, and symmetry is what makes Ampère's law calculationally tractable. Both results also reveal the solenoid and toroid as controlled magnetic field factories: the field inside scales linearly with n (or N) and I, making it easy to design a device with a specific target field by choosing the winding density and current. This linear control, combined with efficient field confinement, explains their ubiquity in inductors, magnetic resonance machines, and particle accelerators.
