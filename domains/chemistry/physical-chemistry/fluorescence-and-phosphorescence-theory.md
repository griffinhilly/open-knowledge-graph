---
id: fluorescence-and-phosphorescence-theory
title: Fluorescence, Phosphorescence, and Photophysical Decay Pathways
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electronic-spectroscopy-theory
  type: hard
- id: energy-level-transitions
  type: soft
- id: electronic-transitions-excited-states
  type: soft
builds-toward: []
tags:
- fluorescence
- phosphorescence
- Jablonski-diagram
- intersystem-crossing
- quantum-yield
- radiative-decay
- nonradiative-decay
stage: advanced
status: draft
---

# Fluorescence, Phosphorescence, and Photophysical Decay Pathways

## Core Idea
After absorbing a photon and reaching an excited electronic state, a molecule can return to the ground state through several competing pathways summarized by the Jablonski diagram. Fluorescence is the spin-allowed radiative decay from the lowest excited singlet state S1 to the ground state S0, typically occurring on nanosecond timescales. Phosphorescence involves intersystem crossing (ISC) from S1 to a triplet state T1, followed by spin-forbidden radiative decay T1 to S0 on microsecond-to-second timescales. Nonradiative pathways -- internal conversion (IC, same spin) and ISC (spin change) -- compete with emission, and the quantum yield Phi = k_r/(k_r + k_nr) quantifies the fraction of absorbed photons that produce emission. Heavy-atom effects, molecular rigidity, and solvent environment all modulate the relative rates of these pathways.

## How It's Best Learned
Trace the pathways on a Jablonski diagram for a real fluorophore (e.g., fluorescein or naphthalene), assigning rate constants to each arrow. Then predict how the quantum yield and lifetime change when you add a heavy atom (enhanced ISC, more phosphorescence) or rigidify the molecule (reduced IC, higher fluorescence yield).

## Common Misconceptions
- Conflating fluorescence and phosphorescence as simply "fast vs slow glow"; the fundamental distinction is spin multiplicity -- fluorescence preserves spin, phosphorescence requires a spin flip.
- Thinking phosphorescence requires a special material; most organic molecules can phosphoresce, but at room temperature nonradiative decay from the triplet is usually too fast to observe emission without special conditions (rigid matrix, heavy atoms).
