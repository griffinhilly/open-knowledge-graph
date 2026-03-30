---
id: spectrochemical-series
title: Spectrochemical Series
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
builds-toward:
- color-spectroscopy-coordination-compounds
- ligand-field-theory
tags:
- spectrochemical series
- ligand field strength
- delta splitting
stage: formal-systems
status: validated
---

# Spectrochemical Series

## Core Idea
The spectrochemical series ranks ligands by the magnitude of crystal field splitting (Δ) they produce when coordinated to a metal ion. Weak-field ligands like I⁻ and Br⁻ produce small Δ values, while strong-field ligands like CN⁻ and CO produce large Δ values. This ranking is determined experimentally from absorption spectra and is largely independent of the metal ion, making it a transferable tool for predicting electronic properties of coordination compounds.

## Questions

```yaml
- question: "Which of the following correctly places the ligands in order of increasing field strength?"
  type: multiple-choice
  options:
    - "CO < CN⁻ < NH₃ < H₂O < Cl⁻ < I⁻"
    - "I⁻ < Br⁻ < Cl⁻ < F⁻ < H₂O < NH₃ < CN⁻ < CO"
    - "F⁻ < Cl⁻ < Br⁻ < I⁻ < H₂O < NH₃ < CN⁻ < CO"
    - "I⁻ < Cl⁻ < F⁻ < H₂O < NH₃ < CO < CN⁻"
  answer: 1
  explanation: "The spectrochemical series from weakest to strongest field is: I⁻ < Br⁻ < Cl⁻ < F⁻ < H₂O < NH₃ < en < NO₂⁻ < CN⁻ < CO. Option A reverses the entire order. Option C reverses the halides (larger halides are weaker field, not stronger). Option D swaps CN⁻ and CO — while both are strong-field, CO is generally placed at the very end. Note that among the halides, the order follows inverse size: the larger, more polarizable halides produce weaker fields."

- question: "A chemist observes that [Co(NH₃)₆]³⁺ absorbs at shorter wavelengths than [Co(H₂O)₆]³⁺. This is consistent with NH₃ being a stronger-field ligand than H₂O."
  type: true-false
  answer: true
  explanation: "Absorption wavelength is inversely related to energy: shorter wavelengths correspond to higher-energy transitions. In an octahedral complex, the primary d-d absorption corresponds to promoting an electron across the Δ_oct gap. A stronger-field ligand produces a larger Δ_oct, requiring higher-energy (shorter-wavelength) light for this transition. Since [Co(NH₃)₆]³⁺ absorbs at shorter wavelengths, its Δ_oct must be larger, confirming NH₃ is a stronger-field ligand than H₂O — exactly as the spectrochemical series predicts."

- question: "The spectrochemical series can be fully explained by the electrostatic model of crystal field theory, where ligand field strength correlates directly with ligand charge."
  type: true-false
  answer: false
  explanation: "If field strength were purely electrostatic, anionic ligands (Cl⁻, CN⁻) should produce stronger fields than neutral ligands (NH₃, CO) simply because they carry more charge. But the series shows neutral CO and NH₃ are stronger-field ligands than anionic F⁻ and Cl⁻. The spectrochemical series actually reflects covalent interactions — particularly pi-bonding effects. Strong-field ligands like CO and CN⁻ are pi-acceptors that withdraw electron density from the metal t₂g orbitals, effectively increasing Δ. Weak-field ligands like halides are pi-donors that push electron density into the metal t₂g orbitals, decreasing Δ. This is why ligand field theory (which includes covalency) succeeds where pure CFT fails."

- question: "Explain why the spectrochemical series places the halides in the order I⁻ < Br⁻ < Cl⁻ < F⁻, and why all four are weaker-field than neutral NH₃, despite being negatively charged."
  type: short-answer
  answer: "Among halides, larger ions are more polarizable and have more diffuse lone pairs that interact poorly with metal d-orbitals. They are also better pi-donors, which raises the t₂g energy and decreases Δ. F⁻ is the strongest-field halide because its small size and low polarizability produce the least pi-donation. But even F⁻ is weaker than neutral NH₃ because all halides are pi-donors (they have filled p-orbitals that overlap with metal t₂g orbitals and raise their energy), while NH₃ is a pure sigma-donor with no pi-donating or pi-accepting capability. The pi-donation from halides partially cancels the sigma-donation effect, reducing Δ below what NH₃ achieves through sigma bonding alone."
  explanation: "This is a key insight: charge alone does not determine field strength. The nature of the metal-ligand interaction — whether the ligand donates or accepts pi-electron density — is the dominant factor. This is the point where crystal field theory's electrostatic model breaks down and ligand field theory becomes necessary."
```

## Explainer

Crystal field theory introduced the idea that ligands split the d-orbitals of a metal ion, creating an energy gap Δ that controls the electronic properties of the complex. The spectrochemical series answers the next natural question: which ligands produce the largest splitting? The answer comes directly from experiment. By measuring the absorption spectra of a series of complexes with the same metal ion but different ligands, you can rank ligands by the energy of the d-d transition — and therefore by the Δ they produce.

The experimentally determined ordering, from weakest to strongest field, is: I⁻ < Br⁻ < S²⁻ < Cl⁻ < N₃⁻ < F⁻ < OH⁻ < ox²⁻ < H₂O < NCS⁻ < CH₃CN < py < NH₃ < en < bipy < phen < NO₂⁻ < PPh₃ < CN⁻ < CO < NO⁺. This ranking is approximately independent of the metal — a remarkable empirical regularity that makes the series practically useful. If you know where a ligand sits in the series, you can immediately predict whether a given complex will be high-spin or low-spin, estimate its absorption wavelength, and anticipate its relative stability.

Several patterns in the series are instructive. Among the halides, field strength increases as the halide gets smaller: I⁻ < Br⁻ < Cl⁻ < F⁻. Yet all halides are weaker-field than the neutral ligand H₂O, which is itself weaker than NH₃. This immediately challenges the simple electrostatic picture of crystal field theory: if field strength were purely about charge, anions should beat neutrals. The resolution lies in pi-bonding effects. Halides have filled p-orbitals that overlap with metal t₂g orbitals, donating electron density into them and raising their energy — this shrinks Δ. Conversely, CO and CN⁻ have empty pi-antibonding orbitals that accept electron density from the metal t₂g orbitals, lowering their energy and increasing Δ. NH₃, with neither pi-donor nor pi-acceptor ability, sits in the middle as a pure sigma-donor.

The spectrochemical series is therefore more than a memorization list — it is a map of metal-ligand bonding character. Weak-field ligands are pi-donors. Medium-field ligands are pure sigma-donors. Strong-field ligands are pi-acceptors. This pattern will become central when you move from crystal field theory to ligand field theory, which explicitly incorporates covalent bonding and pi-interactions into the orbital model.
