---
id: solenoid-magnetic-field-properties
title: Solenoid Magnetic Field and Properties
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: biot-savart-law
  type: hard
- id: amperes-law
  type: hard
- id: magnetic-field-lines-flux-density
  type: soft
builds-toward:
- inductance-and-inductors
tags:
- magnetism
- solenoids
- field geometry
stage: formal-systems
status: validated
---
# Solenoid Magnetic Field and Properties

## Core Idea
A solenoid (helical coil) produces a magnetic field when current flows through it. Inside an ideal solenoid, the field is uniform: B = μ₀nI, where n is turns per unit length. Outside, the field is negligible. A finite solenoid produces a field similar to a bar magnet. Field energy is proportional to B². Solenoids are essential in electromagnets, relays, and inductors.

## Questions

```yaml
- question: "Two solenoids have the same number of turns per unit length and carry the same current, but one has twice the radius of the other. How do their interior magnetic fields compare?"
  type: multiple-choice
  options:
    - "The wider solenoid has twice the field, since it encloses more area"
    - "The narrower solenoid has twice the field, since the field lines are more concentrated"
    - "Both solenoids have the same field — B = μ₀nI depends only on turn density and current, not on radius"
    - "The fields cannot be compared without knowing the solenoids' total lengths"
  answer: 2
  explanation: "B = μ₀nI for an ideal solenoid, where n is turns per unit length and I is current. Radius does not appear in the formula — the Ampère's law derivation shows the interior field is uniform and independent of the solenoid's radius. What matters is how densely turns are packed (n) and how much current flows, not the solenoid's diameter. Both solenoids with the same n and I have identical interior fields."

- question: "A solenoid carries current I and has n turns per unit length. The current is doubled while n is halved (turns are spread more loosely). What happens to the interior field?"
  type: multiple-choice
  options:
    - "The field doubles, since more current creates more field"
    - "The field is halved, since fewer turns per unit length means less field generation"
    - "The field is unchanged — B = μ₀nI, and (n/2)(2I) = nI, so the product nI is unchanged"
    - "The field changes in a way that depends on the solenoid's total length"
  answer: 2
  explanation: "B = μ₀nI depends only on the product nI. If n is halved and I is doubled, nI → (n/2)(2I) = nI — unchanged. The field is the same. What matters physically is the current-per-unit-length (sometimes written as the surface current density K = nI): the total ampere-turns packed into each unit of length. The same field can be achieved with few dense turns carrying high current, or many loose turns carrying low current, as long as the product nI is equal."

- question: "For an ideal (infinitely long) solenoid, the magnetic field outside is exactly zero — all magnetic flux is confined to the interior."
  type: true-false
  answer: true
  explanation: "True. This follows from the Ampère's law derivation: a rectangular Amperian loop with one side outside and one inside has its outer contribution equal to zero (the external field is zero) because neighboring turns produce external fields in opposite directions that cancel exactly for an infinite solenoid. The interior leg contributes B·L = μ₀nLI. In reality, finite solenoids produce fringe fields at their ends, and the exterior field is not exactly zero — but it becomes negligible far from the ends compared to the strong uniform interior field."

- question: "A solenoid's magnetic field B = μ₀nI is proportional to the current squared, which is why the energy stored in a solenoid scales as I²."
  type: true-false
  answer: false
  explanation: "False — with an important distinction. The magnetic field B = μ₀nI is proportional to I (linear, not squared). However, the energy stored in the magnetic field is proportional to B², which means energy ∝ (μ₀nI)² ∝ I². So energy scales as I², not the field itself. Inductance L is defined such that energy = ½LI², where L ∝ n². The statement conflates the field (linear in I) with the stored energy (quadratic in I)."

- question: "Explain why the magnetic field inside a solenoid is approximately uniform, and why this is surprising given that the solenoid is made of discrete wire loops."
  type: short-answer
  answer: "Each circular loop produces a dipole-like field that is strongest near that loop's center and falls off with distance. When many loops are stacked tightly, their interior contributions all point in the same axial direction and add constructively regardless of position inside the stack. Meanwhile, their exterior fields cancel destructively, because adjacent loops generate opposing external fields at any exterior point. The result is a uniform axial interior field B = μ₀nI independent of position — an emergent collective property of the ensemble, not a property of any individual loop."
  explanation: "The Ampère's law derivation confirms this: no matter where inside the solenoid you place the interior leg of the Amperian loop, the same nL turns thread through it and the same B·L appears in the line integral. The field cannot depend on radial position inside because the Amperian analysis gives the same answer regardless of where the interior leg is placed. This is the power of Ampère's law for symmetric configurations — it extracts the field from global symmetry without having to sum contributions from each individual current element."
```

## Explainer

A solenoid is built by stacking many circular current loops along a common axis. You already know from Biot-Savart that a single circular loop creates a dipole-like magnetic field: strong and roughly uniform near the center, curving outward and weakening rapidly away from the loop. When you stack many loops tightly together, something remarkable happens: the field contributions inside the stack add constructively (all pointing in the same axial direction), while outside the stack they cancel destructively (neighboring loops create opposing external fields at any exterior point). The result is a device that concentrates magnetic flux into a uniform, confined interior field — effectively manufacturing a controlled field region.

**Ampère's law** makes the calculation clean. Imagine a rectangular Amperian loop whose long side runs parallel to the solenoid axis: one leg inside the solenoid (where B is uniform and axial), and one leg outside (where B ≈ 0). The line integral ∮B·dl = μ₀I_enc reduces to B·L = μ₀(nL)I, where n is the number of turns per unit length and nL turns thread through the rectangle, each carrying current I. Solving: **B = μ₀nI**. Notice that the result is independent of position inside the solenoid — the field is truly uniform — and independent of the solenoid's radius. Only the turn density n and current I matter.

The confinement of field to the interior is the solenoid's defining property. For an ideal (infinitely long) solenoid, the exterior field is exactly zero — all flux that enters one end exits the other, and none leaks out through the sides. A finite solenoid leaks field at its ends, producing a **fringe field** pattern identical to a bar magnet: field lines emerge from one end (the "north pole") and re-enter the other (the "south pole"). This is not a coincidence — a solenoid and a bar magnet are both magnetic dipoles, and their far-field behavior is identical. The difference is that a solenoid's strength is electrically controllable, making it the basis for electromagnets, MRI machines, relays, and solenoid valves.

The energy stored in the solenoid's field is proportional to B², meaning it scales as (nI)². This stored energy is the physical basis for **inductance**: when you change the current through a solenoid, the changing field induces an EMF (by Faraday's law) that opposes the change. The solenoid "resists" current changes by storing or releasing magnetic energy. This makes the solenoid the archetypal inductor — the central component in any circuit that involves energy storage in magnetic fields, from power supplies to radio tuning circuits.
