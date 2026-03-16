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
status: draft
---

# Fluorescence Quantum Yield and Excited State Lifetime

## Core Idea
Fluorescence quantum yield Φ_f = (radiative rate k_r) / (total decay rate k_r + k_nr) quantifies the fraction of absorbed photons re-emitted as fluorescence. Excited state lifetime τ = 1/(k_r + k_nr) determines how long molecules spend in excited states before relaxation. High quantum yields and long lifetimes require fast radiative decay and slow non-radiative processes.

## Explainer

From the Franck-Condon principle and electronic spectroscopy, you know that molecules absorb photons to reach excited electronic states, and that the intensity of absorption depends on the overlap between vibrational wavefunctions of the ground and excited states. But what happens after absorption? The molecule must eventually return to the ground state, and it has two broad categories of pathways: **radiative decay** (emitting a photon — fluorescence) and **non-radiative decay** (converting electronic energy into heat through vibrations, or transferring it to other molecules). The competition between these pathways determines both how brightly a molecule fluoresces and how long it stays excited.

The **fluorescence quantum yield** Φ_f is simply the fraction of absorbed photons that come back out as fluorescence: Φ_f = k_r / (k_r + k_nr), where k_r is the rate constant for radiative emission and k_nr is the sum of all non-radiative rate constants. If k_r dominates (k_nr ≈ 0), the quantum yield approaches 1.0 — nearly every absorbed photon produces a fluorescence photon. If non-radiative processes are fast (k_nr >> k_r), the quantum yield drops toward zero and the molecule converts most absorbed light into heat. Fluorescein in basic solution, for example, achieves Φ_f ≈ 0.95 because its rigid aromatic structure suppresses non-radiative vibrations, while flexible molecules with many rotatable bonds tend to have low quantum yields because those rotations provide efficient non-radiative relaxation pathways.

The **excited-state lifetime** τ = 1/(k_r + k_nr) measures the average time a molecule spends in the excited state before decaying by any pathway. Typical fluorescence lifetimes range from about 1 to 100 nanoseconds. The lifetime and quantum yield are connected through a useful relationship: Φ_f = τ/τ_0, where τ_0 = 1/k_r is the **natural radiative lifetime** — the hypothetical lifetime the molecule would have if fluorescence were the only decay pathway. Measuring both Φ_f and τ experimentally lets you separate k_r and k_nr individually, which reveals whether a dim fluorophore is dim because it emits slowly (small k_r) or because non-radiative processes are fast (large k_nr).

These quantities are central to applications across chemistry and biology. In fluorescence microscopy, high quantum yield means brighter signals with less excitation light (reducing photodamage). In **Förster resonance energy transfer (FRET)**, the donor's quantum yield and lifetime change when an acceptor molecule is nearby, providing a molecular ruler for measuring distances in the 1–10 nm range. In photochemistry and solar energy, maximizing excited-state lifetime gives the molecule more time to undergo productive chemistry before wasting its energy as heat. Understanding the competition between radiative and non-radiative pathways is therefore not just a spectroscopic exercise — it is the foundation for designing molecules with specific photophysical behavior.
