---
id: ir-spectroscopy-basics
title: Infrared (IR) Spectroscopy
domain: chemistry
course: organic-chemistry
prerequisites:
- id: functional-groups-overview
  type: hard
- id: nmr-spectroscopy-basics
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: wave-properties-intro
  type: soft
tags:
- IR
- spectroscopy
- functional groups
- wavenumber
- carbonyl
- absorption
- fingerprint region
stage: formal-systems
status: validated
---

# Infrared (IR) Spectroscopy

## Core Idea
Infrared (IR) spectroscopy measures absorption of infrared radiation by molecular bonds as they undergo vibrational excitation (stretching and bending). Each functional group absorbs at characteristic wavenumber ranges (cm⁻¹), making IR a rapid tool for functional group identification. The most diagnostic regions are: broad O–H stretch (~3200–3550 cm⁻¹ for alcohols; sharper for carboxylic acids), N–H stretch (~3300 cm⁻¹), C=O stretch (~1680–1760 cm⁻¹, position sensitive to substitution and conjugation), and the fingerprint region (600–1500 cm⁻¹) unique to each compound. IR is primarily used to confirm presence or absence of functional groups and is most powerful when combined with NMR and mass spectrometry.

## How It's Best Learned
Memorize four key diagnostic peaks: broad O–H, C=O (and its position variants), N–H, and the C≡C/C≡N triple-bond region (~2100–2260 cm⁻¹). Practice interpreting simple IR spectra by first scanning the carbonyl region (1680–1760 cm⁻¹), then the high-frequency region (2500–3600 cm⁻¹). Pair each IR conclusion with a confirmatory NMR feature.

## Common Misconceptions
- Absence of a C=O absorption does NOT mean the molecule contains no oxygen — ethers, alcohols, and epoxides have no carbonyl.
- The C=O stretch position is highly diagnostic: esters absorb near 1735 cm⁻¹, carboxylic acids near 1710 cm⁻¹, amides near 1680 cm⁻¹, and conjugated carbonyls are shifted to lower wavenumbers.
- IR spectra cannot distinguish two structurally similar compounds (same functional groups, similar backbone) — mass spectrometry and NMR are needed for unambiguous identification.

## Questions

```yaml
- question: "An IR spectrum shows a strong, sharp absorption at approximately 1735 cm⁻¹ and no broad O–H stretch. Which functional group is most consistent with this observation?"
  type: multiple-choice
  options: ["Amide (R–CO–NR₂)", "Carboxylic acid (–COOH)", "Ester (–COO–)", "Conjugated ketone (ArCO–)"]
  answer: 2
  explanation: "Esters absorb near 1735 cm⁻¹, which is the high end of the C=O range. Carboxylic acids absorb near 1710 cm⁻¹ and also show a broad O–H stretch (2500–3300 cm⁻¹). Amides absorb near 1680 cm⁻¹. Conjugated carbonyls are shifted to lower wavenumbers (~1670–1690 cm⁻¹). The absence of O–H rules out alcohols and carboxylic acids."

- question: "If an IR spectrum shows no absorption in the 1680–1760 cm⁻¹ region, the molecule can rarely contain any oxygen atoms."
  type: true-false
  answer: false
  explanation: "The 1680–1760 cm⁻¹ region is specific to C=O stretching. Molecules with oxygen in ethers (C–O–C), alcohols (C–OH), or epoxides will show no carbonyl peak, yet clearly contain oxygen. The absence of a C=O peak eliminates aldehydes, ketones, esters, acids, and amides — but many oxygen-containing functional groups lack a carbonyl entirely."

- question: "A chemist obtains an IR spectrum of an unknown compound and identifies a broad O–H absorption and a C=O stretch at ~1710 cm⁻¹. What additional technique would best confirm whether the compound is a carboxylic acid rather than a β-ketoalcohol, and why?"
  type: short-answer
  answer: "¹H NMR spectroscopy — it would show the distinctive downfield carboxylic acid proton (δ 10–12 ppm) and reveal the carbon skeleton connectivity, which IR cannot provide."
  explanation: "IR identifies functional groups by bond vibrations but cannot distinguish two compounds sharing the same groups arranged differently. NMR reveals the chemical environment of each hydrogen (and carbon), directly confirming whether the O–H and C=O belong to a –COOH unit or are separate groups on the molecule."
```

## Explainer

Infrared spectroscopy exploits the fact that covalent bonds are not rigid — they vibrate continuously, stretching and bending at frequencies determined by bond strength and the masses of the atoms involved. When infrared radiation of exactly the right frequency strikes a bond, the bond absorbs that energy and vibrates more intensely. By measuring which frequencies are absorbed, you get a direct readout of which types of bonds are present in the molecule.

The key unit is the wavenumber (cm⁻¹), which is inversely proportional to wavelength. Higher wavenumber means higher energy, which corresponds to lighter atoms and stronger bonds. This is why O–H and N–H stretches appear at high wavenumbers (~3000–3600 cm⁻¹) — hydrogen is very light. The C=O stretch appears around 1680–1760 cm⁻¹ because the double bond is strong but carbon and oxygen are heavier than hydrogen. Single bonds (C–C, C–O, C–N) absorb at lower wavenumbers, clustering in the fingerprint region below ~1500 cm⁻¹.

The most strategically important peak to look for first is the carbonyl stretch. Its exact position tells you more than just "there's a C=O" — esters sit near 1735 cm⁻¹ (the carbonyl is electron-poor due to the adjacent oxygen), carboxylic acids near 1710 cm⁻¹, and amides near 1680 cm⁻¹ (nitrogen donation weakens the C=O). Conjugation with a double bond or aromatic ring pulls electron density into the π system, lowering the C=O stretching frequency by ~20–40 cm⁻¹. These position shifts are diagnostic and worth memorizing as a small table.

After scanning the carbonyl region, check the high-frequency region (2500–3600 cm⁻¹). A broad, often ugly absorption spanning 2500–3300 cm⁻¹ indicates a carboxylic acid O–H. A broad but somewhat sharper O–H around 3200–3550 cm⁻¹ points to an alcohol. A pair of absorptions near 3300–3500 cm⁻¹ suggests a primary amine (two N–H stretches) or amide. A very sharp, thin peak near 2100–2260 cm⁻¹ — in a region where almost nothing else absorbs — flags a triple bond (C≡C or C≡N).

IR is most powerful when used alongside NMR and mass spectrometry. It rapidly confirms the presence or absence of key functional groups, but it cannot tell you how the molecule is connected. Two compounds with the same functional groups and similar carbon skeletons may have nearly identical IR spectra. Think of IR as a fast first filter: it narrows down the candidates quickly, and then NMR closes the case.
