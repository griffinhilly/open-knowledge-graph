---
id: ligand-field-theory
title: Ligand Field Theory
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
- id: spectrochemical-series
  type: hard
- id: molecular-orbital-theory-advanced
  type: soft
builds-toward:
- electronic-spectra-tanabe-sugano
- mo-theory-transition-metal-complexes
tags:
- ligand field theory
- pi bonding
- sigma bonding
- covalent bonding in complexes
stage: advanced
status: validated
---

# Ligand Field Theory

## Core Idea
Ligand field theory (LFT) combines the orbital splitting picture of crystal field theory with the covalent bonding description of molecular orbital theory. It retains CFT's practical framework of d-orbital splitting and high-spin/low-spin configurations while adding the crucial insight that metal-ligand bonds have substantial covalent character. LFT explains why the spectrochemical series exists: pi-donor ligands decrease Δ, pure sigma-donors give intermediate Δ, and pi-acceptor ligands increase Δ through back-bonding interactions.

## Questions

```yaml
- question: "In ligand field theory, how does a pi-acceptor ligand like CO increase Δ_oct compared to a pure sigma-donor like NH₃?"
  type: multiple-choice
  options:
    - "CO forms stronger electrostatic interactions with the metal due to its dipole moment"
    - "CO has empty pi-antibonding orbitals that accept electron density from the filled metal t₂g orbitals (back-bonding), lowering the t₂g energy and increasing the gap to the eg set"
    - "CO is a stronger sigma-donor than NH₃, pushing the eg orbitals to higher energy"
    - "CO reduces the electron-electron repulsion in the eg orbitals by withdrawing charge from them"
  answer: 1
  explanation: "The key mechanism is pi-back-bonding. The metal's filled t₂g orbitals have the correct symmetry to overlap with CO's empty π* orbitals. Electron density flows from metal to ligand through this overlap, stabilizing (lowering the energy of) the t₂g set. Since Δ_oct is the gap between t₂g and eg, lowering t₂g while eg stays roughly the same (or rises slightly from sigma interactions) increases Δ. This is why CO sits at the far end of the spectrochemical series. NH₃ has no empty pi-orbitals, so it cannot accept back-donation — it only interacts through sigma-donation, giving a moderate Δ."

- question: "Ligand field theory predicts that halide ligands (F⁻, Cl⁻, Br⁻, I⁻) are weak-field ligands because their filled p-orbitals act as pi-donors, raising the energy of the metal t₂g orbitals and decreasing Δ."
  type: true-false
  answer: true
  explanation: "Halides have filled p-orbitals perpendicular to the metal-ligand bond axis. These orbitals have the correct symmetry to overlap with the metal t₂g orbitals. Since the ligand p-orbitals are filled, electron density is donated from ligand to metal t₂g, raising the t₂g energy. This decreases the t₂g-eg gap (Δ), making halides weak-field ligands. The effect is strongest for larger, more polarizable halides (I⁻ > Br⁻ > Cl⁻ > F⁻), which is why the spectrochemical series places I⁻ at the very bottom."

- question: "Ligand field theory reduces to crystal field theory when all metal-ligand interactions are treated as purely electrostatic."
  type: true-false
  answer: true
  explanation: "LFT is a more general framework that includes CFT as a limiting case. When you remove all covalent interactions (sigma and pi bonding between metal and ligand orbitals) and treat ligands as point charges, LFT reproduces exactly the CFT predictions: the d-orbital splitting pattern depends only on geometry, and Δ is determined solely by electrostatic parameters. The power of LFT is that it adds covalency without discarding the intuitive d-orbital splitting picture — you can still talk about t₂g and eg sets, high-spin and low-spin, and CFSE, while also explaining trends (like the spectrochemical series) that CFT cannot."

- question: "Explain why CO is a stronger-field ligand than CN⁻, even though CN⁻ is negatively charged and should interact more strongly with a positively charged metal ion in an electrostatic model."
  type: short-answer
  answer: "In the electrostatic model of CFT, CN⁻ should produce a stronger field because its negative charge creates a stronger point-charge interaction with the metal cation. But LFT shows that field strength is dominated by covalent interactions, not electrostatics. CO is a superior pi-acceptor: its π* orbitals are lower in energy and better matched to the metal t₂g orbitals than those of CN⁻, making back-bonding more effective. CO is also an excellent sigma-donor through its carbon lone pair. The combination of strong sigma-donation (raising eg) and strong pi-acceptance (lowering t₂g) produces the largest Δ of any common ligand. CN⁻, while also a good pi-acceptor, is slightly less effective because its negative charge raises the energy of its π* orbitals, making them a less favorable target for back-donation."
  explanation: "This example perfectly illustrates why CFT alone is insufficient: the relative field strengths of CO and CN⁻ cannot be rationalized without invoking covalent pi-interactions. LFT resolves this and many similar puzzles in the spectrochemical series."
```

## Explainer

Crystal field theory gave you a powerful intuition: ligands split d-orbitals, and the magnitude of that splitting controls color, magnetism, and stability. But CFT treats ligands as point charges — a fiction that works for some predictions but fails for others. Why is neutral CO a stronger-field ligand than anionic F⁻? Why do the spectrochemical series ligands fall in a specific, reproducible order? Ligand field theory answers these questions by incorporating the covalent nature of metal-ligand bonds while preserving the d-orbital splitting framework you already know.

LFT classifies ligands by their bonding capabilities: sigma-only donors (like NH₃), sigma-donors that are also pi-donors (like halides), and sigma-donors that are also pi-acceptors (like CO and CN⁻). These categories map directly onto the spectrochemical series. Sigma donation is the baseline — every ligand donates at least one electron pair to the metal through a sigma bond, raising the energy of the metal orbitals that point at the ligands (the eg set in an octahedral complex). The pi interactions then modulate the energy of the t₂g set. Pi-donor ligands (halides, OH⁻, H₂O) have filled orbitals that overlap with the metal t₂g orbitals, pushing electron density onto the metal and raising the t₂g energy — this shrinks Δ. Pi-acceptor ligands (CO, CN⁻, phosphines) have empty orbitals that draw electron density out of the metal t₂g orbitals, lowering the t₂g energy — this enlarges Δ.

The pi-acceptance mechanism, often called back-bonding or back-donation, deserves closer examination because it is central to organometallic chemistry. In a metal-CO bond, the carbon lone pair donates into an empty metal orbital (sigma donation), while the filled metal t₂g orbitals donate into the empty π* antibonding orbitals of CO (pi back-bonding). This is a synergistic cycle: sigma donation increases electron density on the metal, making back-donation more favorable; back-donation removes electron density from the metal, making sigma donation more favorable. The net result is a strong, short metal-carbon bond and a weakened C-O bond (observable as a lowered CO stretching frequency in infrared spectroscopy).

LFT thus provides a unified explanation for the entire spectrochemical series. Weak-field ligands are pi-donors that raise t₂g. Medium-field ligands are pure sigma-donors. Strong-field ligands are pi-acceptors that lower t₂g. This three-category model replaces memorization with understanding. It also bridges the gap between the ionic picture of crystal field theory and the fully covalent picture of molecular orbital theory, making it the standard working model for most practicing inorganic chemists.
