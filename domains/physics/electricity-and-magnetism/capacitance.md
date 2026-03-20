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
status: validated
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

## Explainer

A **capacitor** is essentially a charge reservoir: it accepts charge on one conductor and induces an equal but opposite charge on the facing conductor, building up a potential difference between them. You already know from electric potential that moving charge against an electric field costs energy — that energy is what gets stored. The ratio C = Q/V, called **capacitance**, tells you how much charge you can store per volt of potential difference. A large capacitance means the geometry is favorable for accumulating charge without requiring a large voltage.

The parallel-plate capacitor is the cleanest geometry to analyze. You know from Gauss's law that a uniformly charged plate produces a uniform field E = σ/ε₀ between the plates (where σ = Q/A is surface charge density). The voltage across the gap is just V = Ed = σd/ε₀. Plugging Q = σA back in gives C = Q/V = ε₀A/d. This result captures the geometry intuitively: a larger plate area stores more charge for the same field, increasing C; a larger gap requires a larger voltage for the same field, decreasing C. Everything about capacitor geometry follows this pattern — larger facing area and smaller separation always increase capacitance.

When capacitors are combined in circuits, the combination rules follow directly from how charge and voltage behave. In **series**, the same charge Q sits on each capacitor (charge has nowhere else to go), but the voltages add: V_total = Q/C₁ + Q/C₂ = Q(1/C₁ + 1/C₂). So 1/C_series = Σ(1/Cᵢ) — series combination is always smaller than any individual capacitor. In **parallel**, both capacitors see the same voltage V, so their charges add: Q_total = C₁V + C₂V = (C₁ + C₂)V. Thus C_parallel = ΣCᵢ — parallel combination just pools the storage capacity.

The energy stored in a capacitor takes three equivalent forms: U = ½CV² = Q²/2C = ½QV. But the most physically revealing form comes from asking where the energy lives. The energy density in an electric field is u = ½ε₀E². Integrating this over the volume between the plates (volume = Ad) gives exactly U = ½CV² — the energy is distributed throughout the field, not sitting on the charges. This is a preview of a deeper principle: in electrodynamics, fields are real physical entities that carry energy, momentum, and more.
