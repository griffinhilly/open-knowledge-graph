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

## Questions

```yaml
- question: "A small organic molecule in solution has a very short correlation time (τc ≈ 10⁻¹² s). You increase the viscosity of the solvent dramatically, slowing molecular tumbling (τc now ≈ 10⁻⁸ s). What happens to T₁?"
  type: multiple-choice
  options:
    - "T₁ decreases monotonically, because slower motion always increases spin-lattice relaxation"
    - "T₁ first decreases to a minimum then increases, because T₁ vs τc is non-monotonic"
    - "T₁ increases monotonically, because slower motion gives spins more time to relax"
    - "T₁ is unchanged, because T₁ depends only on the magnetic field strength"
  answer: 1
  explanation: "T₁ has a minimum when ω₀τc ≈ 1 — when the tumbling rate matches the Larmor frequency and energy transfer is maximally efficient. Starting from very fast tumbling (short τc, small molecule), increasing viscosity first moves τc toward this resonance condition, decreasing T₁. Once past the minimum (when τc > 1/ω₀, as for large proteins), further slowing increases T₁ again. This non-monotonic behavior is the key insight; it means you cannot simply say 'slower motion = faster or slower relaxation' without knowing where on the curve you are."

- question: "Why is T₂ always less than or equal to T₁, and why does the inequality become dramatic for large proteins?"
  type: multiple-choice
  options:
    - "T₂ ≤ T₁ because T₂ only depends on fast motions near the Larmor frequency, while T₁ is sensitive to all motions"
    - "T₂ ≤ T₁ because T₂ is sensitive to both fast and slow motions, while T₁ is primarily sensitive to motions near the Larmor frequency"
    - "T₂ ≤ T₁ because large proteins have fewer hydrogen atoms, reducing dipolar coupling"
    - "T₂ ≤ T₁ because phase coherence decays faster than the spin population can recover"
  answer: 1
  explanation: "T₁ requires energy exchange between spins and the lattice, which demands fluctuating fields at the Larmor frequency ω₀ — so only fast motions (short τc) drive T₁ efficiently. T₂ is damaged by any process that causes spins to dephase, including slow low-frequency motions that create persistent local field variations. For small rapidly-tumbling molecules, both types of motions average effectively and T₁ ≈ T₂. For large, slowly-tumbling proteins, slow motions destroy phase coherence quickly (short T₂) while T₁ becomes long because motions are too slow to efficiently transfer energy at ω₀. The large T₁/T₂ ratio is a signature of macromolecular systems."

- question: "A longer T₁ relaxation time always indicates slower molecular motion (larger correlation time)."
  type: true-false
  answer: false
  explanation: "Because T₁ vs τc is non-monotonic with a minimum at ω₀τc ≈ 1, a long T₁ is consistent with either very fast tumbling (small τc, well below the minimum) or very slow tumbling (large τc, beyond the minimum). Small molecules in low-viscosity solution often have long T₁ because they tumble far faster than needed for optimal energy transfer. Without additional information (e.g., measurements at multiple field strengths), you cannot determine whether long T₁ means fast or slow motion — this is a common source of misinterpretation."

- question: "The spectral density function J(ω) quantifies motional power at each frequency. For a slowly tumbling protein, J(0) is large while J(ω₀) is small."
  type: true-false
  answer: true
  explanation: "The spectral density J(ω) = 2τc/(1 + ω²τc²) is essentially a Lorentzian. For slow tumbling (large τc), the Lorentzian is narrow and concentrated at low frequencies, so J(0) is large but J(ω₀) and J(2ω₀) are small (since ω₀τc ≫ 1 and the denominator is large). This explains why T₂ is short for proteins (T₂ depends on J(0), which is large, driving fast dephasing) while T₁ is long (T₁ depends on J(ω₀) and J(2ω₀), which are small, giving slow spin-lattice relaxation)."

- question: "Explain physically why measuring NMR relaxation at multiple magnetic field strengths provides more information about molecular dynamics than a single-field measurement."
  type: short-answer
  answer: "T₁ depends on spectral density at the Larmor frequency ω₀, which scales with field strength. Measurements at different fields probe J(ω) at different frequencies, effectively sampling the spectral density function at multiple points. This allows you to distinguish between motions on different timescales, separate internal motions from overall tumbling, and fit models to extract τc values and order parameters — none of which is possible from a single-field measurement alone."
  explanation: "The spectral density function encodes the full distribution of molecular motions. A single T₁ or T₂ measurement gives only one number — one sample of J(ω) at one frequency. Multi-field relaxation measurements provide multiple constraints on the same underlying dynamic model, enabling proper extraction of correlation times and the separation of fast local fluctuations from slow global tumbling. This is the basis of 'model-free' analysis and field-dependent NMR studies of protein dynamics."
```

## Explainer

From NMR quantum theory, you know that nuclear spins in a magnetic field occupy quantized energy levels and that radiofrequency pulses can perturb this system away from equilibrium. Relaxation is the process by which the spin system returns to equilibrium after such a perturbation, and it contains a wealth of information about molecular dynamics because it is driven by molecular motion itself.

**Spin-lattice relaxation (T₁)** describes how fast the longitudinal magnetization (alignment along the external field B₀) recovers to its equilibrium value. The "lattice" refers to the molecular environment — the surrounding thermal bath. For energy to transfer from the spin system to the lattice, the spins need fluctuating magnetic fields at the right frequency — specifically, at the Larmor frequency ω₀. These fluctuating fields come from molecular tumbling: as a molecule rotates in solution, the magnetic dipoles of nearby nuclei generate oscillating local fields. If the tumbling rate matches the Larmor frequency, energy transfer is maximally efficient and T₁ reaches its minimum. This is the key insight — T₁ is not simply "faster motion = faster relaxation." It follows a non-monotonic curve when plotted against the **correlation time** τ_c, with a minimum where ω₀τ_c ≈ 1.

**Spin-spin relaxation (T₂)** describes how fast the transverse magnetization (coherence of spins precessing in the xy-plane) decays. T₂ reflects the loss of phase coherence among individual spins. Any process that causes different spins to precess at slightly different frequencies contributes to T₂ relaxation — including slow molecular motions that create static local field inhomogeneities. Because T₂ is sensitive to both fast and slow motions while T₁ is primarily sensitive to motions near the Larmor frequency, T₂ ≤ T₁ always. For small molecules tumbling rapidly in solution (short τ_c), T₁ ≈ T₂ because molecular motion efficiently averages local field differences. For large molecules like proteins (long τ_c), T₂ becomes much shorter than T₁ because slow tumbling creates persistent local field variations that accelerate dephasing.

The **correlation time** τ_c is the characteristic time for molecular reorientation — roughly, how long it takes a molecule to rotate by about one radian. Small molecules in low-viscosity solvents have τ_c values around 10⁻¹² s (picoseconds), while proteins in water have τ_c values of 10⁻⁹ to 10⁻⁸ s (nanoseconds). The relationship between relaxation rates (R₁ = 1/T₁, R₂ = 1/T₂) and τ_c is described by the **Solomon equations**, which express relaxation rates as sums of spectral density functions J(ω) evaluated at specific frequencies (0, ω₀, and 2ω₀). The spectral density J(ω) = 2τ_c/(1 + ω²τ_c²) quantifies how much motional power exists at frequency ω — it is the Fourier transform of the autocorrelation function of the fluctuating local fields.

This framework makes NMR relaxation a remarkably precise probe of molecular dynamics. By measuring T₁ and T₂ (and the nuclear Overhauser effect, which depends on the same spectral densities) at multiple magnetic field strengths, you can extract τ_c and determine whether a molecule or a specific segment of a macromolecule is tumbling freely, undergoing restricted motion, or exchanging between conformational states. This is why NMR relaxation is indispensable in structural biology — it reveals not just what a protein looks like, but how it moves, where its flexible loops are, and how fast ligands bind and unbind.
