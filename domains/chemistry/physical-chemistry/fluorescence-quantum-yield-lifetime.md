---
id: fluorescence-quantum-yield-lifetime
title: Fluorescence Quantum Yield and Excited State Lifetime
domain: chemistry
course: physical-chemistry
prerequisites:
- id: franck-condon-principle
  type: hard
- id: electronic-spectroscopy-theory
  type: hard
builds-toward:
- phosphorescence-intersystem-crossing
tags:
- fluorescence
- photochemistry
- radiative-processes
stage: advanced
status: validated
---

# Fluorescence Quantum Yield and Excited State Lifetime

## Core Idea
Fluorescence quantum yield Φ_f = (radiative rate k_r) / (total decay rate k_r + k_nr) quantifies the fraction of absorbed photons re-emitted as fluorescence. Excited state lifetime τ = 1/(k_r + k_nr) determines how long molecules spend in excited states before relaxation. High quantum yields and long lifetimes require fast radiative decay and slow non-radiative processes.

## Questions

```yaml
- question: "Molecule A has Φ_f = 0.05 and τ = 2 ns. Molecule B also has Φ_f = 0.05 but τ = 40 ns. What can you conclude?"
  type: multiple-choice
  options:
    - "Both molecules have the same non-radiative decay rate, since their quantum yields are equal"
    - "Molecule A has fast non-radiative decay (large k_nr), while molecule B emits slowly (small k_r) — both are dim for different reasons"
    - "Molecule B is a better fluorophore because its longer lifetime makes it more useful in all applications"
    - "Molecule A has a smaller radiative rate constant k_r than molecule B"
  answer: 1
  explanation: "Both molecules are dim (Φ_f = 0.05), but for different reasons. From Φ_f = k_r/(k_r + k_nr) and τ = 1/(k_r + k_nr): molecule A has τ = 2 ns → k_r + k_nr = 5×10⁸ s⁻¹ (very fast total decay, dominated by large k_nr). Molecule B has τ = 40 ns → k_r + k_nr = 2.5×10⁷ s⁻¹ (slow total decay, with small k_r). This illustrates why measuring both Φ_f and τ is essential: the same quantum yield can arise from fundamentally different photophysical situations. Measuring only Φ_f cannot distinguish between them."

- question: "A newly synthesized fluorophore has a quantum yield of only 0.03 under physiological conditions. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The molecule absorbs photons only weakly, leaving little energy available for emission"
    - "Non-radiative decay pathways (molecular vibrations, rotations, or energy transfer) compete effectively with fluorescence"
    - "The molecule emits photons at a wavelength that is reabsorbed by the surrounding solvent"
    - "The molecule has a very short natural radiative lifetime τ₀, forcing rapid emission before excited-state population builds"
  answer: 1
  explanation: "Quantum yield measures what fraction of absorbed photons re-emerge as fluorescence. A low Φ_f means most absorbed energy is lost non-radiatively — as heat through vibrations, internal conversions, or rotational relaxation (increasing k_nr). Absorption strength (molar absorptivity) affects how many photons are captured but has no bearing on what fraction of those actually absorbed come back as fluorescence. A short τ₀ (fast radiative decay) would actually *increase* quantum yield, not decrease it. Option C describes inner filter effects, which change apparent but not intrinsic quantum yield."

- question: "A molecule with a high fluorescence quantum yield necessarily has a long excited-state lifetime."
  type: true-false
  answer: false
  explanation: "Quantum yield Φ_f = k_r/(k_r + k_nr) and lifetime τ = 1/(k_r + k_nr). High Φ_f requires k_r >> k_nr, but if k_r itself is very large, then k_r + k_nr is also large, making τ = 1/(k_r + k_nr) short. For example, a molecule with k_r = 10⁹ s⁻¹ and k_nr = 10⁸ s⁻¹ has Φ_f ≈ 0.91 (high) but τ ≈ 0.9 ns (short). High quantum yield means fast radiative decay *relative to* non-radiative decay — not absolutely fast — so the absolute lifetime depends on both rates together."

- question: "Measuring both fluorescence quantum yield and excited-state lifetime for the same molecule provides enough information to independently calculate k_r and k_nr."
  type: true-false
  answer: true
  explanation: "From the two equations Φ_f = k_r/(k_r + k_nr) and τ = 1/(k_r + k_nr), you have two equations and two unknowns. Solving: k_r = Φ_f/τ and k_nr = (1 − Φ_f)/τ. This decomposition reveals whether a dim molecule is dim because it emits slowly (small k_r) or because non-radiative pathways are fast (large k_nr) — a distinction with direct implications for molecular design. This is why combined quantum yield and lifetime measurements are standard characterization tools in photophysics."

- question: "Why do rigid aromatic fluorophores like fluorescein tend to have much higher quantum yields than flexible molecules with many rotatable bonds?"
  type: short-answer
  answer: "Rotatable bonds provide efficient non-radiative relaxation pathways — the molecule can dissipate electronic excitation energy as heat by changing conformation (bond rotation), increasing k_nr. This reduces Φ_f = k_r/(k_r + k_nr). A rigid aromatic structure has few low-energy conformational modes available in solution, so k_nr remains small and the radiative pathway captures the majority of excited-state energy. Rigidity essentially blocks the 'heat drain,' forcing the molecule to return to the ground state by emitting a photon."
  explanation: "This principle guides fluorescent dye design for microscopy and biosensing: rigidizing a flexible molecule (e.g., by locking a rotor with a chemical bridge) reliably boosts quantum yield. It also explains why some molecules are highly fluorescent in viscous solvents or when bound to proteins (restricted rotation) but dim in low-viscosity solvents."
```

## Explainer

From the Franck-Condon principle and electronic spectroscopy, you know that molecules absorb photons to reach excited electronic states, and that the intensity of absorption depends on the overlap between vibrational wavefunctions of the ground and excited states. But what happens after absorption? The molecule must eventually return to the ground state, and it has two broad categories of pathways: **radiative decay** (emitting a photon — fluorescence) and **non-radiative decay** (converting electronic energy into heat through vibrations, or transferring it to other molecules). The competition between these pathways determines both how brightly a molecule fluoresces and how long it stays excited.

The **fluorescence quantum yield** Φ_f is simply the fraction of absorbed photons that come back out as fluorescence: Φ_f = k_r / (k_r + k_nr), where k_r is the rate constant for radiative emission and k_nr is the sum of all non-radiative rate constants. If k_r dominates (k_nr ≈ 0), the quantum yield approaches 1.0 — nearly every absorbed photon produces a fluorescence photon. If non-radiative processes are fast (k_nr >> k_r), the quantum yield drops toward zero and the molecule converts most absorbed light into heat. Fluorescein in basic solution, for example, achieves Φ_f ≈ 0.95 because its rigid aromatic structure suppresses non-radiative vibrations, while flexible molecules with many rotatable bonds tend to have low quantum yields because those rotations provide efficient non-radiative relaxation pathways.

The **excited-state lifetime** τ = 1/(k_r + k_nr) measures the average time a molecule spends in the excited state before decaying by any pathway. Typical fluorescence lifetimes range from about 1 to 100 nanoseconds. The lifetime and quantum yield are connected through a useful relationship: Φ_f = τ/τ_0, where τ_0 = 1/k_r is the **natural radiative lifetime** — the hypothetical lifetime the molecule would have if fluorescence were the only decay pathway. Measuring both Φ_f and τ experimentally lets you separate k_r and k_nr individually, which reveals whether a dim fluorophore is dim because it emits slowly (small k_r) or because non-radiative processes are fast (large k_nr).

These quantities are central to applications across chemistry and biology. In fluorescence microscopy, high quantum yield means brighter signals with less excitation light (reducing photodamage). In **Förster resonance energy transfer (FRET)**, the donor's quantum yield and lifetime change when an acceptor molecule is nearby, providing a molecular ruler for measuring distances in the 1–10 nm range. In photochemistry and solar energy, maximizing excited-state lifetime gives the molecule more time to undergo productive chemistry before wasting its energy as heat. Understanding the competition between radiative and non-radiative pathways is therefore not just a spectroscopic exercise — it is the foundation for designing molecules with specific photophysical behavior.
