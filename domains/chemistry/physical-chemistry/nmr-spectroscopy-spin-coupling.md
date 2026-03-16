---
id: nmr-spectroscopy-spin-coupling
title: 'NMR Spectroscopy: Chemical Shifts and Spin Coupling'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: nmr-quantum-theory
  type: hard
- id: electron-spin-magnetic-moment
  type: hard
tags:
- nmr
- spectroscopy
- coupling
- spin
- structure-determination
stage: advanced
status: draft
---

# NMR Spectroscopy: Chemical Shifts and Spin Coupling

## Core Idea
NMR spectroscopy exploits the magnetic moment of nuclei to determine molecular structure. Chemical shift reflects the local electron density around a nucleus through shielding effects. Spin-spin coupling (J-coupling) between neighboring nuclei causes splitting of NMR signals into multiplets, revealing connectivity. Integration and splitting patterns allow unambiguous determination of molecular structure and dynamics.

## How It's Best Learned
Start with simple molecules (ethanol, acetaldehyde) and analyze 1H NMR patterns. Correlate chemical shifts with functional groups using tabulated values. Use the n+1 rule to predict splitting patterns, then explain deviations using real coupling constants.

## Common Misconceptions
- All equivalent protons give a single line (accidentally equivalent protons may couple if magnetic field is weak).
- Chemical shift depends only on electronegativity of adjacent atoms (local ring currents and anisotropy effects also matter).

## Explainer

From your study of nuclear spin and magnetic moments, you know that certain nuclei (like ¹H and ¹³C) behave as tiny magnets: when placed in an external magnetic field B₀, their spin states split into distinct energy levels, and radiofrequency radiation can drive transitions between them. **NMR spectroscopy** exploits this phenomenon to determine molecular structure, but the raw resonance frequency alone would only tell you that protons are present. The power of NMR comes from two additional effects — chemical shift and spin-spin coupling — that encode the electronic environment and connectivity of each nucleus.

**Chemical shift** arises because the electrons surrounding a nucleus generate their own small magnetic field that opposes the external field. A nucleus surrounded by more electron density is more **shielded** — it experiences a weaker effective field and resonates at a lower frequency. A nucleus near electron-withdrawing groups (like halogens or carbonyls) has less shielding and resonates at a higher frequency, appearing further **downfield** on the spectrum. Chemical shift is reported in parts per million (ppm, symbol δ) relative to a reference compound (TMS), making it independent of the spectrometer's field strength. The chemical shift value immediately tells you the electronic neighborhood: δ ≈ 0–2 for alkyl protons, δ ≈ 6–8 for aromatic protons, δ ≈ 9–10 for aldehyde protons, and so on. But shift alone does not reveal connectivity.

**Spin-spin coupling** (J-coupling) provides the connectivity information. When two non-equivalent nuclei are separated by two or three bonds, the spin state of one nucleus subtly alters the local magnetic field experienced by the other, transmitted through the bonding electrons. If a proton has n equivalent neighboring protons, its signal splits into **n + 1 lines** (the n + 1 rule), with relative intensities following Pascal's triangle. A proton next to a CH₂ group sees two neighbors and splits into a triplet (1:2:1); the CH₂ protons, seeing one neighbor, split into a doublet (1:1). The **coupling constant** J, measured in hertz, is the same for both coupled partners and is independent of field strength — distinguishing coupling from chemical shift, which scales with B₀.

Putting these pieces together lets you reconstruct molecular structure from an NMR spectrum. First, count the number of distinct signals to determine how many chemically inequivalent proton environments exist. Second, use integration (the area under each peak) to find the ratio of protons in each environment. Third, read chemical shifts to identify functional group neighborhoods. Fourth, analyze splitting patterns to determine how many neighboring protons each group has, revealing the connectivity. For example, ethanol's ¹H spectrum shows three signals — a triplet (CH₃, split by adjacent CH₂), a quartet (CH₂, split by adjacent CH₃), and a singlet or broad peak (OH) — with integration ratio 3:2:1, immediately confirming the structure CH₃CH₂OH. This systematic approach makes NMR the single most powerful tool for organic structure determination.
