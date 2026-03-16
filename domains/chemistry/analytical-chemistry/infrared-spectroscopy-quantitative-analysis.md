---
id: infrared-spectroscopy-quantitative-analysis
title: 'Infrared Spectroscopy: Quantitative Applications'
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: ir-spectroscopy-analytical
  type: hard
- id: beers-law
  type: soft
tags:
- IR-spectroscopy
- quantitative-IR
- functional-groups
- FTIR
stage: advanced
status: draft
---

# Infrared Spectroscopy: Quantitative Applications

## Core Idea
Quantitative IR spectroscopy measures functional group concentrations from characteristic absorption bands. Advanced applications include attenuated total reflectance (ATR) for solids without sample preparation, chemometric modeling of complex spectra, and in-situ monitoring of chemical processes where IR provides real-time kinetic and structural information.

## Explainer

From your IR spectroscopy prerequisite, you know that infrared radiation excites molecular vibrations and that each functional group absorbs at characteristic frequencies — the carbonyl stretch near 1700 cm⁻¹, O–H stretch near 3300 cm⁻¹, and so on. Qualitative IR tells you *what* functional groups are present. **Quantitative IR** tells you *how much* — and making that transition requires applying Beer's Law to infrared absorption bands, with several complications that do not arise in simpler UV-Vis applications.

Beer's Law states that absorbance is proportional to concentration and path length: A = εbc. In principle, you can measure the absorbance of a characteristic IR band and read concentration from a calibration curve, just as you would in UV-Vis spectroscopy. In practice, IR quantitation is harder because IR spectra are more complex — dozens of overlapping bands from multiple functional groups, baseline drift from scattering or instrument artifacts, and the fact that most solvents absorb strongly in the IR region. Selecting an **analytical band** that is intense, well-resolved from neighboring peaks, and free from interference is the critical first step. Often you must use a **baseline correction** method — drawing a tangent line between two points flanking the band and measuring peak height or area relative to that baseline rather than zero.

**Attenuated total reflectance (ATR)** has transformed quantitative IR by eliminating the most difficult sample preparation challenges. Instead of pressing a solid into a KBr pellet or dissolving it in an IR-transparent solvent, you simply press the sample against a crystal of high refractive index (diamond, zinc selenide, or germanium). The IR beam undergoes total internal reflection inside the crystal, and an **evanescent wave** penetrates a few micrometers into the sample surface, interacting with the analyte and producing an absorption spectrum. Because the effective path length is fixed and very short, ATR gives reproducible, quantitative spectra from powders, films, pastes, and liquids with minimal preparation — making it ideal for quality control and process monitoring.

For complex mixtures where no single band is free from spectral overlap, **chemometric methods** extend IR quantitation beyond what univariate Beer's Law can handle. Techniques like partial least squares (PLS) regression use the entire spectrum — or a selected region — to build a multivariate calibration model that relates spectral patterns to analyte concentration. These models can simultaneously quantify multiple components in a mixture even when their spectra overlap extensively. Combined with fiber-optic probes and flow cells, quantitative IR becomes a powerful **in-situ monitoring** tool — you can track a reaction in real time by watching characteristic bands grow or shrink, measuring conversion rates without withdrawing samples or stopping the process.
