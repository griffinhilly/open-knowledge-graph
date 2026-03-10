---
id: capacitance
title: Capacitance and Capacitors
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential
  type: hard
- id: conductors-in-electrostatics
  type: soft
builds-toward:
- dielectrics
- rc-circuits
- energy-stored-in-fields
tags:
- capacitance
- capacitors
- charge-storage
- parallel-plate
stage: formal-systems
status: draft
---

# Capacitance and Capacitors

## Core Idea
A capacitor is a device that stores electric charge and energy by maintaining a potential difference between two conductors. Capacitance C = Q/V measures how much charge is stored per unit voltage, with unit farads (F). For a parallel-plate capacitor with plate area A and separation d, C = ε₀A/d. Capacitors in series combine as 1/C_total = Σ(1/Cᵢ), and in parallel as C_total = ΣCᵢ.

## How It's Best Learned
Derive the parallel-plate formula from Gauss's law + potential difference integral. Then practice series/parallel combinations and energy storage U = ½CV² = Q²/(2C) = ½QV in varied circuit configurations.

## Common Misconceptions
- Capacitance depends only on geometry and material, not on the charge or voltage applied.
- Capacitors in series store less charge than any individual capacitor; in parallel, more.
- The energy is stored in the electric field between the plates, not in the charges themselves.
