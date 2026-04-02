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
stage: expert
status: validated
---

# NMR Spectroscopy: Chemical Shifts and Spin Coupling

## Core Idea
NMR spectroscopy exploits the magnetic moment of nuclei to determine molecular structure. Chemical shift reflects the local electron density around a nucleus through shielding effects. Spin-spin coupling (J-coupling) between neighboring nuclei causes splitting of NMR signals into multiplets, revealing connectivity. Integration and splitting patterns allow unambiguous determination of molecular structure and dynamics.

## How It's Best Learned
Start with simple molecules (ethanol, acetaldehyde) and analyze 1H NMR patterns. Correlate chemical shifts with functional groups using tabulated values. Use the n+1 rule to predict splitting patterns, then explain deviations using real coupling constants.

## Common Misconceptions
- All equivalent protons give a single line (accidentally equivalent protons may couple if magnetic field is weak).
- Chemical shift depends only on electronegativity of adjacent atoms (local ring currents and anisotropy effects also matter).

## Questions

```yaml
- question: "The ¹H NMR spectrum of a compound shows a signal at δ 9.5 ppm. Which functional group most likely accounts for this chemical shift?"
  type: multiple-choice
  options:
    - "Aromatic ring proton (δ 6–8 ppm range)"
    - "Alkyl CH₃ group adjacent to a carbonyl"
    - "Aldehyde C–H proton"
    - "Vinylic proton on an isolated double bond"
  answer: 2
  explanation: "Aldehyde protons (CHO) resonate at δ 9–10 ppm — one of the most downfield positions in common ¹H NMR spectra. The extreme deshielding occurs because the carbonyl oxygen withdraws electron density through both induction and anisotropy, leaving the aldehyde proton in a very electron-poor environment. Aromatic protons appear at δ 6–8 ppm (option A). Alkyl protons adjacent to a carbonyl appear around δ 2–3 ppm. Vinylic protons appear around δ 4.5–6 ppm."

- question: "In the ¹H NMR spectrum of ethanol (CH₃CH₂OH), the CH₂ group is adjacent to both CH₃ (3 protons) and OH (1 exchangeable proton). Assuming the OH proton does not couple under typical conditions, what splitting pattern does the CH₂ signal show?"
  type: multiple-choice
  options:
    - "A doublet, because the CH₂ sees two equivalent neighbors"
    - "A quartet, because the CH₂ sees three CH₃ protons and splits into n+1 = 4 lines"
    - "A quintet, because the CH₂ sees four total neighboring protons (3 from CH₃ + 1 from OH)"
    - "A singlet, because both neighboring groups cancel each other's splitting"
  answer: 1
  explanation: "Under typical NMR conditions, the OH proton exchanges rapidly with solvent or trace water, so it does not couple to adjacent protons and appears as a broad singlet or is averaged out. The CH₂ therefore only couples to the three equivalent CH₃ protons, giving n+1 = 3+1 = 4 lines — a quartet. Option C would be correct if the OH proton were coupled, but fast exchange typically eliminates this coupling in routine ¹H NMR of alcohols in common solvents."

- question: "The coupling constant J measured from a doublet signal in proton A is identical to the J measured from the doublet in proton B when A and B are mutually coupled."
  type: true-false
  answer: true
  explanation: "This is a fundamental property of J-coupling: the coupling constant between two nuclei is the same regardless of which partner you measure it from. If proton A shows a doublet with J = 7 Hz, proton B (to which A is coupled) will also show its splitting with J = 7 Hz. This symmetry arises because J reflects the interaction through shared bonding electrons, which is a property of the A–B bond, not of either nucleus alone. This fact allows you to identify which peaks are coupled to each other by matching J values across signals."

- question: "Increasing the external magnetic field strength (moving from a 300 MHz to a 600 MHz spectrometer) will increase the coupling constant J between two neighboring protons."
  type: true-false
  answer: false
  explanation: "Coupling constants J (in Hz) are independent of the external magnetic field strength. J-coupling is transmitted through bonding electrons and reflects the intrinsic spin-spin interaction between nuclei — a property of molecular structure, not of the spectrometer. Chemical shifts in Hz do scale with field strength (which is why moving to higher-field spectrometers improves resolution of overlapping signals), but J stays constant. This independence of J from field strength is one way to distinguish coupling from other line-broadening effects."

- question: "How does spin-spin coupling reveal information about molecular connectivity, and why does this complement (rather than duplicate) the structural information provided by chemical shifts?"
  type: short-answer
  answer: "Chemical shift tells you the electronic environment of each proton (shielding, nearby electron-withdrawing or -donating groups) but cannot tell you which protons are bonded to adjacent carbons. Spin-spin coupling provides this connectivity: the splitting pattern of a signal reveals how many non-equivalent protons are attached to neighboring atoms (via the n+1 rule), and the shared J value identifies which pairs of signals are coupled. Together, shift (identity of functional environment) and splitting (identity of neighboring groups) allow reconstruction of the full molecular skeleton."
  explanation: "Chemical shift alone would identify the types of environments present but could not tell you how they are connected. For example, two compounds could have identical sets of chemical shifts but different connectivity. Coupling resolves this because the splitting pattern — and specifically which signals share the same J value — reveals the graph of connections between proton-bearing carbons. NMR structure determination therefore reads connectivity from coupling first, then assigns functional group context from chemical shifts."
```

## Explainer

From your study of nuclear spin and magnetic moments, you know that certain nuclei (like ¹H and ¹³C) behave as tiny magnets: when placed in an external magnetic field B₀, their spin states split into distinct energy levels, and radiofrequency radiation can drive transitions between them. **NMR spectroscopy** exploits this phenomenon to determine molecular structure, but the raw resonance frequency alone would only tell you that protons are present. The power of NMR comes from two additional effects — chemical shift and spin-spin coupling — that encode the electronic environment and connectivity of each nucleus.

**Chemical shift** arises because the electrons surrounding a nucleus generate their own small magnetic field that opposes the external field. A nucleus surrounded by more electron density is more **shielded** — it experiences a weaker effective field and resonates at a lower frequency. A nucleus near electron-withdrawing groups (like halogens or carbonyls) has less shielding and resonates at a higher frequency, appearing further **downfield** on the spectrum. Chemical shift is reported in parts per million (ppm, symbol δ) relative to a reference compound (TMS), making it independent of the spectrometer's field strength. The chemical shift value immediately tells you the electronic neighborhood: δ ≈ 0–2 for alkyl protons, δ ≈ 6–8 for aromatic protons, δ ≈ 9–10 for aldehyde protons, and so on. But shift alone does not reveal connectivity.

**Spin-spin coupling** (J-coupling) provides the connectivity information. When two non-equivalent nuclei are separated by two or three bonds, the spin state of one nucleus subtly alters the local magnetic field experienced by the other, transmitted through the bonding electrons. If a proton has n equivalent neighboring protons, its signal splits into **n + 1 lines** (the n + 1 rule), with relative intensities following Pascal's triangle. A proton next to a CH₂ group sees two neighbors and splits into a triplet (1:2:1); the CH₂ protons, seeing one neighbor, split into a doublet (1:1). The **coupling constant** J, measured in hertz, is the same for both coupled partners and is independent of field strength — distinguishing coupling from chemical shift, which scales with B₀.

Putting these pieces together lets you reconstruct molecular structure from an NMR spectrum. First, count the number of distinct signals to determine how many chemically inequivalent proton environments exist. Second, use integration (the area under each peak) to find the ratio of protons in each environment. Third, read chemical shifts to identify functional group neighborhoods. Fourth, analyze splitting patterns to determine how many neighboring protons each group has, revealing the connectivity. For example, ethanol's ¹H spectrum shows three signals — a triplet (CH₃, split by adjacent CH₂), a quartet (CH₂, split by adjacent CH₃), and a singlet or broad peak (OH) — with integration ratio 3:2:1, immediately confirming the structure CH₃CH₂OH. This systematic approach makes NMR the single most powerful tool for organic structure determination.
