---
id: nmr-relaxation-and-correlation-times
title: NMR Relaxation Times and Correlation Functions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: nmr-quantum-theory
  type: hard
- id: fundamental-statistical-mechanics
  type: soft
builds-toward:
- chemical-exchange-kinetics-nmr
tags:
- nmr
- relaxation
- dynamics
- correlation
stage: advanced
status: draft
---

# NMR Relaxation Times and Correlation Functions

## Core Idea
Spin-lattice (T1) and spin-spin (T2) relaxation times quantify how fast magnetization decays and dephases, driven by molecular motion through fluctuating magnetic fields. T1ρ and NOE measurements probe these motions indirectly; correlation time τc relates motion timescales to relaxation rates. This connection to molecular dynamics makes NMR a powerful tool for studying protein folding, drug binding, and solution kinetics.

## How It's Best Learned
Measure T1 and T2 for ¹H NMR resonances using inversion recovery and CPMG sequences; extract correlation times using Solomon equations; plot relaxation rates vs. temperature to determine activation energies; compare to MD simulations.

## Common Misconceptions
- Confusing T1 (spin-lattice, energy dissipation) with T2 (spin-spin, phase coherence); T2 ≤ T1 always, and they reflect different physical processes. - Assuming longer T1 always indicates slower dynamics; T1 has a minimum at a specific correlation time (T1 vs τc is non-monotonic).
