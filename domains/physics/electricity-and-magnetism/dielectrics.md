---
id: dielectrics
title: Dielectrics
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: capacitance
  type: hard
- id: electric-field
  type: soft
builds-toward:
- maxwells-equations-overview
tags:
- dielectric
- polarization
- permittivity
- capacitance
stage: formal-systems
status: validated
---

# Dielectrics

## Core Idea
A dielectric is an insulating material that, when placed in an electric field, becomes polarized — its molecules align or develop induced dipole moments that partially oppose the applied field. Inserting a dielectric with dielectric constant κ between capacitor plates increases capacitance to C = κε₀A/d and reduces the internal electric field by the factor κ. The permittivity of the material is ε = κε₀, replacing ε₀ in all electrostatic formulas for that medium.

## How It's Best Learned
Compare a capacitor charged to V₀ with battery connected vs. disconnected before dielectric insertion — two different physical scenarios with different outcomes. This sharpens understanding of when Q is fixed vs. V is fixed.

## Common Misconceptions
- Dielectrics do not conduct charge; they reduce E by polarization, not by charge redistribution.
- κ > 1 always for real materials, so inserting a dielectric always increases C.
- The dielectric constant is frequency-dependent in AC settings.

## Questions

```yaml
- question: "A battery maintains a constant 100 V across a parallel-plate capacitor. A dielectric with κ = 3 is inserted between the plates. What correctly describes the new state?"
  type: multiple-choice
  options:
    - "Voltage triples to 300 V because the dielectric amplifies the field"
    - "Charge on the plates triples because capacitance increases while voltage stays fixed at 100 V"
    - "Charge stays the same because charge is conserved"
    - "Capacitance triples but charge stays the same, so voltage must drop to 33 V"
  answer: 1
  explanation: "With the battery connected, voltage is held fixed at V = 100 V. Inserting the dielectric increases capacitance from C₀ to κC₀ = 3C₀. Since Q = CV, charge triples from Q₀ to 3Q₀ — the battery pumps extra charge onto the plates. Energy stored (½CV²) also triples. This contrasts sharply with the battery-disconnected scenario: the battery-connected case is governed by fixed V, while the disconnected case is governed by fixed Q."

- question: "A dielectric reduces the electric field inside a capacitor. How does this happen?"
  type: multiple-choice
  options:
    - "Mobile charges within the dielectric flow to the plates, partially neutralizing them"
    - "The dielectric absorbs energy from the field, converting it to heat"
    - "Molecular dipoles in the dielectric align to create an internal field opposing the applied field"
    - "The dielectric increases the effective plate separation, which reduces E = V/d"
  answer: 2
  explanation: "A dielectric is an insulator — no charge flows through it. Instead, its molecules respond to the applied field by polarizing: either permanent dipoles rotate to align with the field, or nonpolar molecules develop induced dipoles. These aligned dipoles collectively produce an internal electric field that points opposite to the applied field, partially canceling it. The net field inside is reduced by the factor κ. This is entirely distinct from a conductor's response, where free charges do physically redistribute."

- question: "Inserting any real dielectric material between capacitor plates always increases the capacitance, never decreases it."
  type: true-false
  answer: true
  explanation: "The dielectric constant κ is defined as the ratio of permittivity of the material to that of free space, and κ > 1 for all real dielectric materials. Therefore C = κε₀A/d > ε₀A/d = C₀ always. This is a universal property: polarization always partially opposes the applied field, which always reduces V for fixed Q (or equivalently, allows more Q to be stored for fixed V). There is no real material with κ < 1 that would decrease capacitance; such a material would have to amplify rather than oppose the field."

- question: "A capacitor is charged to voltage V₀ and then the battery is disconnected. Inserting a dielectric with κ = 2 increases the energy stored in the capacitor."
  type: true-false
  answer: false
  explanation: "With the battery disconnected, charge Q is fixed. Inserting the dielectric doubles capacitance (C → 2C₀) while Q stays constant. Energy stored = Q²/(2C). Since C doubled, energy is halved: U = Q²/(2·2C₀) = U₀/2. The dielectric is actually pulled between the plates by the fringe fields, and this mechanical work done by the field accounts for the energy decrease — the dielectric gains kinetic energy as it is pulled in. Energy is conserved; it just changes form. This is the opposite of the battery-connected case, where inserting the dielectric increases stored energy."

- question: "Explain why inserting a dielectric reduces the electric field inside the capacitor, and why this reduction does not involve any charge flowing through the material."
  type: short-answer
  answer: "The dielectric reduces E because its molecules polarize in the applied field — either rotating existing dipoles or inducing temporary ones. These aligned dipoles create their own internal electric field pointing opposite to the applied field, partially canceling it. No charge flows because the material is an insulator; the dipoles are bound within individual molecules and simply reorient. The result is a reduced net field E = E₀/κ inside the material."
  explanation: "The key distinction is between bound charge (dipole reorientation within molecules) and free charge (conduction). In a conductor, free electrons redistribute to cancel E completely. In a dielectric, bound charges merely shift slightly within their molecules. This partial, local response reduces E by κ but cannot eliminate it. The misconception that dielectrics work by conducting charge away is common but wrong — a dielectric that conducted charge would be a capacitor short circuit, not an insulator."
```

## Explainer

From your study of capacitance, you know that a capacitor stores energy in the electric field between its plates, with C = ε₀A/d for a parallel-plate geometry in vacuum. A **dielectric** is an insulating material that, when inserted between the plates, increases the capacitance by a factor κ — the **dielectric constant** (also called relative permittivity). The reason is microscopic: the material's molecules respond to the applied field by becoming polarized.

**Polarization** happens in two ways. In polar molecules (like water), permanent electric dipoles rotate to partially align with the external field. In nonpolar molecules, the applied field distorts the electron cloud slightly, inducing a temporary dipole. In both cases, the aligned dipoles create their own electric field inside the material that points opposite to the applied field. This internal "opposition field" partially cancels the applied field, reducing the net E inside the dielectric by the factor κ. Crucially, no charge flows — the material remains an insulator. The dipoles just rearrange internally, which is fundamentally different from a conductor's response.

Now consider the consequences for a capacitor. If you charge the capacitor to voltage V₀ with the battery connected and then insert a dielectric, the battery maintains V = V₀ while κ increases C from C₀ to κC₀. More charge flows from the battery to the plates — Q increases by the factor κ. If instead you charge the capacitor, disconnect the battery (so Q is fixed), and then insert the dielectric, the reduced internal field means lower voltage: V = V₀/κ. The energy stored also drops by κ (the dielectric has done work pulling itself between the plates). These two scenarios — **constant voltage** vs. **constant charge** — give different physics, and distinguishing them is essential for any dielectric problem.

The **permittivity** of the medium is defined as ε = κε₀. Every electrostatic formula valid in vacuum — Coulomb's law, the capacitance formula, the energy density u = ½ε₀E² — still holds inside a uniform dielectric if you replace ε₀ with ε = κε₀. This is why κ appears in Gauss's law and Maxwell's equations as a material property: it describes how much the medium reduces the electric field (and thus how much it enhances charge storage) compared to free space. For engineering purposes, high-κ dielectrics are valuable precisely because they allow large capacitance in compact devices.
