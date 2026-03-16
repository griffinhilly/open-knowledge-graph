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

## Explainer

From NMR quantum theory, you know that nuclear spins in a magnetic field occupy quantized energy levels and that radiofrequency pulses can perturb this system away from equilibrium. Relaxation is the process by which the spin system returns to equilibrium after such a perturbation, and it contains a wealth of information about molecular dynamics because it is driven by molecular motion itself.

**Spin-lattice relaxation (T₁)** describes how fast the longitudinal magnetization (alignment along the external field B₀) recovers to its equilibrium value. The "lattice" refers to the molecular environment — the surrounding thermal bath. For energy to transfer from the spin system to the lattice, the spins need fluctuating magnetic fields at the right frequency — specifically, at the Larmor frequency ω₀. These fluctuating fields come from molecular tumbling: as a molecule rotates in solution, the magnetic dipoles of nearby nuclei generate oscillating local fields. If the tumbling rate matches the Larmor frequency, energy transfer is maximally efficient and T₁ reaches its minimum. This is the key insight — T₁ is not simply "faster motion = faster relaxation." It follows a non-monotonic curve when plotted against the **correlation time** τ_c, with a minimum where ω₀τ_c ≈ 1.

**Spin-spin relaxation (T₂)** describes how fast the transverse magnetization (coherence of spins precessing in the xy-plane) decays. T₂ reflects the loss of phase coherence among individual spins. Any process that causes different spins to precess at slightly different frequencies contributes to T₂ relaxation — including slow molecular motions that create static local field inhomogeneities. Because T₂ is sensitive to both fast and slow motions while T₁ is primarily sensitive to motions near the Larmor frequency, T₂ ≤ T₁ always. For small molecules tumbling rapidly in solution (short τ_c), T₁ ≈ T₂ because molecular motion efficiently averages local field differences. For large molecules like proteins (long τ_c), T₂ becomes much shorter than T₁ because slow tumbling creates persistent local field variations that accelerate dephasing.

The **correlation time** τ_c is the characteristic time for molecular reorientation — roughly, how long it takes a molecule to rotate by about one radian. Small molecules in low-viscosity solvents have τ_c values around 10⁻¹² s (picoseconds), while proteins in water have τ_c values of 10⁻⁹ to 10⁻⁸ s (nanoseconds). The relationship between relaxation rates (R₁ = 1/T₁, R₂ = 1/T₂) and τ_c is described by the **Solomon equations**, which express relaxation rates as sums of spectral density functions J(ω) evaluated at specific frequencies (0, ω₀, and 2ω₀). The spectral density J(ω) = 2τ_c/(1 + ω²τ_c²) quantifies how much motional power exists at frequency ω — it is the Fourier transform of the autocorrelation function of the fluctuating local fields.

This framework makes NMR relaxation a remarkably precise probe of molecular dynamics. By measuring T₁ and T₂ (and the nuclear Overhauser effect, which depends on the same spectral densities) at multiple magnetic field strengths, you can extract τ_c and determine whether a molecule or a specific segment of a macromolecule is tumbling freely, undergoing restricted motion, or exchanging between conformational states. This is why NMR relaxation is indispensable in structural biology — it reveals not just what a protein looks like, but how it moves, where its flexible loops are, and how fast ligands bind and unbind.
