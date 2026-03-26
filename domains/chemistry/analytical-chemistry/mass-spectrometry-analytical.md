---
id: mass-spectrometry-analytical
title: Mass Spectrometry
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: analytical-chemistry-intro
  type: hard
- id: organic-chemistry-intro
  type: soft
- id: electron-configuration
  type: soft
- id: magnetic-force-moving-charges
  type: soft
- id: electric-field
  type: soft
- id: lorentz-force-complete-em
  type: soft
- id: conservation-of-momentum
  type: soft
- id: kinetic-energy
  type: soft
- id: lorentz-force-on-moving-charge
  type: soft
- id: ion-formation-from-electron-transfer
  type: soft
tags:
- mass spectrometry
- ionization
- fragmentation
- molecular ion
- m/z
stage: advanced
status: validated
---

# Mass Spectrometry

## Core Idea
Mass spectrometry separates gaseous ions by their mass-to-charge ratio (m/z), producing a spectrum that reveals molecular mass and structural information through fragmentation patterns. Ionization methods — electron ionization (EI), electrospray (ESI), matrix-assisted laser desorption (MALDI) — determine which analytes are accessible and how much fragmentation occurs. The molecular ion peak (M⁺) gives the nominal molecular mass; high-resolution MS provides exact mass for molecular formula determination. Tandem MS (MS/MS) isolates and fragments selected ions for greater structural specificity and is widely used in metabolomics, proteomics, and environmental analysis.

## How It's Best Learned
Interpret EI spectra of small organic molecules by identifying M⁺, M+1, and M+2 isotope patterns (for heteroatom detection) and predicting major fragmentation pathways using McLafferty rearrangement and alpha-cleavage rules. Connecting fragmentation to structural features is more instructive than memorizing masses.

## Common Misconceptions
- The base peak (most intense) is not necessarily the molecular ion — extensive fragmentation can reduce M⁺ to negligible intensity in EI.
- ESI produces multiply charged ions, so the observed m/z is not the molecular mass — charge state deconvolution is required.

## Questions

```yaml
- question: "In an electron ionization (EI) mass spectrum, what does the base peak represent?"
  type: multiple-choice
  options: ["The molecular ion (M⁺)", "The most abundant ion in the spectrum", "The ion with exactly half the molecular mass", "The ion with the highest mass-to-charge ratio"]
  answer: 1
  explanation: "The base peak is simply the most intense peak in the spectrum — it is defined by abundance, not by identity. A common misconception is equating the base peak with the molecular ion. Extensive EI fragmentation often destroys most of the M⁺, so a fragment ion may be far more abundant and become the base peak, while M⁺ appears as a tiny peak or not at all."

- question: "In electrospray ionization (ESI), the m/z value of the most intense peak directly gives the molecular mass of the analyte."
  type: true-false
  answer: false
  explanation: "ESI routinely produces multiply charged ions — a molecule of mass M may appear at m/z ≈ (M + z·1)/z for charge states z = 1, 2, 3, … The observed m/z is lower than M for every z > 1. Charge-state deconvolution (identifying the pattern of peaks from multiple charge states) is required to calculate the true molecular mass."

- question: "Why might the molecular ion (M⁺) peak be absent or very small in an electron ionization (EI) spectrum, even though the sample was successfully introduced into the instrument?"
  type: short-answer
  answer: "EI bombards analyte molecules with high-energy electrons (typically 70 eV), far exceeding the ~10 eV needed to ionize most molecules. The excess energy causes rapid fragmentation of the newly formed M⁺ into smaller fragment ions. For labile molecules, nearly all M⁺ fragments before detection, so fragment peaks dominate the spectrum and M⁺ is negligible."
  explanation: "This question targets the misconception that a missing molecular ion means the experiment failed. The M⁺ was formed but then broke apart. Softer ionization methods (ESI, MALDI) were developed precisely to preserve the intact molecular ion for fragile biomolecules."
```

## Explainer

Mass spectrometry works by converting analyte molecules into gas-phase ions, separating those ions by their mass-to-charge ratio (m/z), and counting them to produce a spectrum. The horizontal axis is m/z and the vertical axis is relative abundance — the result is a bar chart of fragment masses that acts like a molecular fingerprint.

The ionization step determines what kind of information you get. Electron ionization (EI) fires high-energy electrons at the molecule, ripping off an electron to produce a radical cation M⁺, then typically shattering it into smaller fragments. EI spectra are rich in structural information because each bond has a characteristic probability of breaking — recognizing patterns like alpha-cleavage (breaking adjacent to a heteroatom) or McLafferty rearrangement (involving a gamma-hydrogen) lets you read the connectivity of the molecule. However, EI is hard on fragile molecules. Electrospray ionization (ESI) and MALDI are "soft" methods that deposit much less energy: they produce intact charged molecules, ideal for proteins and nucleic acids, but provide less fragmentation for structural diagnosis.

The molecular ion peak (M⁺) in an EI spectrum is the highest m/z peak from the intact molecule — it tells you the nominal molecular mass. A critical distinction: the molecular ion is not necessarily the base peak (the tallest bar). Base peak just means most abundant ion at the time of detection, which is often a stable fragment. If M⁺ is weak or absent, chemists can switch to a softer ionization technique or use the fragmentation pattern itself to work backward to the molecular mass.

High-resolution mass spectrometry (HRMS) adds a precision layer. Because different elements have slightly different exact atomic masses (C = 12.000, H = 1.00783, N = 14.003, O = 15.995…), measuring m/z to four or five decimal places lets you calculate the molecular formula directly from the exact mass — a technique called elemental composition determination. Tandem MS (MS/MS) adds another dimension: a selected ion is isolated and deliberately fragmented a second time, giving structural information specific to that precursor mass. This is the backbone of proteomics and metabolomics, where thousands of compounds must be identified in a single run.

When interpreting a spectrum, start at the high m/z end: find M⁺ (or [M+H]⁺ in ESI), then look at isotope patterns — the M+2 peak is enhanced by chlorine or bromine (distinctive 3:1 or 1:1 ratios), and the M+1 peak scales with carbon count. Then work down through the major fragments, asking which bonds broke and what structural features they reveal. Connecting fragmentation to molecular structure, rather than memorizing masses, is what makes mass spectrometry interpretable across novel compounds.

