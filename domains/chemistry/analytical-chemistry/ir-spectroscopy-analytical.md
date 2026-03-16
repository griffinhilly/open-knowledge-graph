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

## Explainer

You already know that molecules absorb infrared light when the photon energy matches a vibrational transition, and you can identify common functional groups like O-H, C=O, and N-H from their characteristic absorption frequencies. Analytical IR spectroscopy takes these fundamentals and turns them into a systematic method for identifying unknown compounds, verifying the identity of known materials, and detecting structural changes — making it one of the most widely used qualitative tools in chemistry.

The practical strategy for interpreting an IR spectrum follows a predictable sequence. Start in the **functional-group region** (4000–1500 cm⁻¹), where you look for the big diagnostic absorptions: a broad O-H stretch around 3200–3600 cm⁻¹, sharp N-H peaks near 3300–3500 cm⁻¹, C-H stretches just below 3000 cm⁻¹ (sp³) or just above (sp², sp), and the strong carbonyl C=O stretch between 1650–1800 cm⁻¹. These bands tell you which functional groups are present. Then move to the **fingerprint region** (1500–400 cm⁻¹), where complex combinations of C-C, C-O, and C-N stretches and bending modes create a pattern unique to each molecule. Two compounds might both show a carbonyl peak at 1715 cm⁻¹, but their fingerprint regions will differ — just as two people might share the same eye color but have different fingerprints.

**FTIR instruments** have largely replaced older dispersive spectrometers because of the **multiplex advantage** (Fellgett's advantage): an interferometer collects all wavelengths simultaneously, then a Fourier transform converts the resulting interferogram into a conventional spectrum. This means faster data collection and better signal-to-noise ratios for the same measurement time. The **throughput advantage** (Jacquinot's advantage) adds further sensitivity because the interferometer uses a large circular aperture rather than narrow slits. In practice, you can collect a high-quality FTIR spectrum in under a minute, and modern instruments include searchable spectral libraries containing hundreds of thousands of reference spectra for automated matching.

**Attenuated total reflectance (ATR)** sampling has revolutionized how samples are handled. Instead of preparing KBr pellets or thin films — tedious procedures prone to artifacts — you simply press the sample against a high-refractive-index crystal (diamond, germanium, or zinc selenide). IR light entering the crystal undergoes total internal reflection, but an **evanescent wave** penetrates a few micrometers into the sample surface, where it is selectively absorbed by the sample's functional groups. The reflected light carries the absorption information back to the detector. ATR works for solids, powders, pastes, and liquids with virtually no preparation, making it the default sampling mode in quality control labs, forensic analysis, and pharmaceutical identity testing. The one caveat is that ATR spectra show slightly different relative band intensities than transmission spectra — longer-wavelength absorptions appear stronger because the evanescent wave penetrates deeper at lower wavenumbers — so library matching algorithms must account for this or use ATR-specific reference databases.
