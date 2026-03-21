---
id: ir-spectroscopy-analytical
title: Infrared Spectroscopy for Qualitative Analysis
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: ir-spectroscopy-basics
  type: hard
- id: vibrational-spectroscopy-theory
  type: soft
- id: functional-groups-overview
  type: hard
- id: electromagnetic-waves
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: vibrational-energy-levels-selection-rules
  type: soft
tags:
- IR
- FTIR
- functional groups
- fingerprint region
- ATR
stage: advanced
status: validated
---

# Infrared Spectroscopy for Qualitative Analysis

## Core Idea
Infrared spectroscopy identifies functional groups and molecular structure through characteristic absorption bands arising from molecular vibrations. The mid-IR region (4000–400 cm⁻¹) divides into the functional-group region (4000–1500 cm⁻¹), where broad categories of bonds absorb, and the fingerprint region (1500–400 cm⁻¹), which provides a unique molecular 'fingerprint' for library matching. Fourier-transform IR (FTIR) instruments collect all wavelengths simultaneously, offering superior signal-to-noise. Attenuated total reflectance (ATR) sampling allows analysis of solids and viscous liquids without sample preparation.

## How It's Best Learned
Systematically interpret spectra of a homologous series (e.g., primary, secondary, tertiary alcohols) by first assigning the major functional-group bands, then using the fingerprint region to distinguish isomers. Comparing spectra to reference databases before attempting interpretation avoids anchoring bias.

## Common Misconceptions
- Absence of a band is not always diagnostic — some symmetrical vibrations are IR-inactive (Raman-active instead).
- The carbonyl stretch position (~1715 cm⁻¹ for ketones) shifts predictably with conjugation and ring strain, so exact wavenumber assignments require contextual knowledge.

## Questions

```yaml
- question: "Two unknown compounds both show a strong carbonyl absorption at 1715 cm⁻¹ and no O-H or N-H peaks in their IR spectra. How can IR spectroscopy distinguish between them?"
  type: multiple-choice
  options:
    - "It cannot — the functional-group region is identical, so the compounds cannot be differentiated by IR"
    - "Compare the fingerprint region (1500–400 cm⁻¹) against reference spectra — two distinct molecules will show different patterns even with identical functional-group peaks"
    - "Measure the exact carbonyl peak position more precisely — structural isomers always differ by at least 10 cm⁻¹"
    - "Use ATR sampling instead of transmission — ATR changes relative band positions and may reveal the difference"
  answer: 1
  explanation: "The functional-group region identifies which classes of bonds are present, but the fingerprint region (1500–400 cm⁻¹) contains complex combinations of C-C, C-O, and C-N stretches and bends that are unique to each molecule's full structure. Two structural isomers may share all major functional-group absorptions yet have completely different fingerprint patterns, enabling library matching to distinguish them. This two-region strategy — functional-group region first, then fingerprint region — is the core analytical workflow."

- question: "An ATR spectrum of a compound shows that the carbonyl band at 1715 cm⁻¹ appears relatively weaker compared to bands near 1000 cm⁻¹ than it does in the corresponding transmission spectrum. What explains this?"
  type: multiple-choice
  options:
    - "The diamond ATR crystal absorbs in the carbonyl region, reducing the observed peak intensity"
    - "ATR evanescent wave penetration depth increases at lower wavenumbers, so longer-wavelength absorptions appear relatively stronger in ATR vs transmission"
    - "The sample was not pressed firmly enough against the crystal, reducing signal only in the high-wavenumber region"
    - "ATR inverts band intensities compared to transmission — this is an artifact to be corrected by background subtraction"
  answer: 1
  explanation: "The evanescent wave generated at the ATR crystal surface penetrates further into the sample at lower wavenumbers (longer wavelengths). This means absorptions at lower wavenumbers (1000 cm⁻¹) benefit from deeper penetration and appear relatively stronger compared to high-wavenumber bands (1715 cm⁻¹). ATR spectra therefore show systematically different relative band intensities compared to transmission spectra. ATR-specific reference databases or software corrections account for this when performing library matching."

- question: "The absence of an O-H absorption band in the 3200–3600 cm⁻¹ region definitively confirms that the compound contains no hydroxyl groups."
  type: true-false
  answer: false
  explanation: "Absence of a band is not always diagnostic because some vibrations are IR-inactive. For a vibration to absorb IR radiation, it must involve a change in dipole moment. Highly symmetrical vibrations — particularly in molecules with centers of symmetry — can be IR-inactive while remaining Raman-active. Additionally, in practice, weak or overlapping bands can be missed. The correct interpretation is that the absence of an O-H band is consistent with no hydroxyl groups, but additional evidence (NMR, MS, Raman) is needed for a definitive conclusion."

- question: "The fingerprint region of two different molecules will differ even when both molecules contain identical functional groups."
  type: true-false
  answer: true
  explanation: "The fingerprint region (1500–400 cm⁻¹) arises from complex coupled vibrations involving the entire molecular framework — C-C, C-O, and C-N stretches, bending modes, and skeletal deformations — that are uniquely sensitive to molecular structure beyond just functional group type. Two structural isomers sharing the same functional groups will have the same major peaks in the functional-group region but distinct fingerprint patterns, just as two people may have the same eye color but different fingerprints. This makes the fingerprint region essential for confirming identity, not just classification."

- question: "Explain why the fingerprint region is essential for distinguishing structural isomers, even when their functional-group region spectra appear identical."
  type: short-answer
  answer: "The functional-group region (4000–1500 cm⁻¹) reports which bond types are present — O-H, C=O, N-H, C-H — without fully encoding the molecular framework connecting them. Structural isomers share the same functional groups but differ in connectivity. The fingerprint region (1500–400 cm⁻¹) contains absorptions from coupled skeletal vibrations (C-C, C-O, ring deformations, bending modes) that are sensitive to the complete three-dimensional arrangement of atoms. These vibrational patterns are complex enough to be unique to each molecule, like a fingerprint. Library matching algorithms compare this entire pattern rather than individual peaks, allowing isomers with identical functional-group regions to be reliably distinguished."
  explanation: "A practical example: pentanone isomers (2-pentanone and 3-pentanone) both show a C=O stretch near 1715 cm⁻¹, C-H stretches, and no other heteroatom bands — their functional-group regions look nearly identical. But their fingerprint patterns diverge substantially, enabling identification by library comparison."
```

## Explainer

You already know that molecules absorb infrared light when the photon energy matches a vibrational transition, and you can identify common functional groups like O-H, C=O, and N-H from their characteristic absorption frequencies. Analytical IR spectroscopy takes these fundamentals and turns them into a systematic method for identifying unknown compounds, verifying the identity of known materials, and detecting structural changes — making it one of the most widely used qualitative tools in chemistry.

The practical strategy for interpreting an IR spectrum follows a predictable sequence. Start in the **functional-group region** (4000–1500 cm⁻¹), where you look for the big diagnostic absorptions: a broad O-H stretch around 3200–3600 cm⁻¹, sharp N-H peaks near 3300–3500 cm⁻¹, C-H stretches just below 3000 cm⁻¹ (sp³) or just above (sp², sp), and the strong carbonyl C=O stretch between 1650–1800 cm⁻¹. These bands tell you which functional groups are present. Then move to the **fingerprint region** (1500–400 cm⁻¹), where complex combinations of C-C, C-O, and C-N stretches and bending modes create a pattern unique to each molecule. Two compounds might both show a carbonyl peak at 1715 cm⁻¹, but their fingerprint regions will differ — just as two people might share the same eye color but have different fingerprints.

**FTIR instruments** have largely replaced older dispersive spectrometers because of the **multiplex advantage** (Fellgett's advantage): an interferometer collects all wavelengths simultaneously, then a Fourier transform converts the resulting interferogram into a conventional spectrum. This means faster data collection and better signal-to-noise ratios for the same measurement time. The **throughput advantage** (Jacquinot's advantage) adds further sensitivity because the interferometer uses a large circular aperture rather than narrow slits. In practice, you can collect a high-quality FTIR spectrum in under a minute, and modern instruments include searchable spectral libraries containing hundreds of thousands of reference spectra for automated matching.

**Attenuated total reflectance (ATR)** sampling has revolutionized how samples are handled. Instead of preparing KBr pellets or thin films — tedious procedures prone to artifacts — you simply press the sample against a high-refractive-index crystal (diamond, germanium, or zinc selenide). IR light entering the crystal undergoes total internal reflection, but an **evanescent wave** penetrates a few micrometers into the sample surface, where it is selectively absorbed by the sample's functional groups. The reflected light carries the absorption information back to the detector. ATR works for solids, powders, pastes, and liquids with virtually no preparation, making it the default sampling mode in quality control labs, forensic analysis, and pharmaceutical identity testing. The one caveat is that ATR spectra show slightly different relative band intensities than transmission spectra — longer-wavelength absorptions appear stronger because the evanescent wave penetrates deeper at lower wavenumbers — so library matching algorithms must account for this or use ATR-specific reference databases.
