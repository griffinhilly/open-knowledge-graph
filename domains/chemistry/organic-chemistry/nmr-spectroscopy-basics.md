---
id: nmr-spectroscopy-basics
title: NMR Spectroscopy Basics
domain: chemistry
course: organic-chemistry
prerequisites:
- id: organic-chemistry-intro
  type: hard
- id: atomic-structure-basics
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: wave-properties-intro
  type: soft
- id: spin-quantum-number
  type: soft
builds-toward:
- ir-spectroscopy-basics
tags:
- NMR
- spectroscopy
- chemical shift
- splitting
- integration
- structure determination
- 1H NMR
- 13C NMR
stage: formal-systems
status: validated
---

# NMR Spectroscopy Basics

## Core Idea
Nuclear Magnetic Resonance (NMR) spectroscopy exploits the quantum spin properties of atomic nuclei (especially ¹H and ¹³C) in an external magnetic field to provide detailed structural information. In ¹H NMR, the chemical shift (in ppm, referenced to TMS at 0 ppm) encodes the electronic environment of each proton — deshielded protons (near electronegative groups or in aromatic rings) resonate at higher ppm values. Integration gives the relative count of equivalent protons in each environment, and the splitting pattern (multiplet structure following the n+1 rule) reveals the number of adjacent non-equivalent protons. Together, these three features allow unambiguous structural assignment.

## How It's Best Learned
Work through ¹H NMR spectra of simple known molecules (ethanol, acetone, diethyl ether) before tackling unknowns. For each spectrum: first count signals (distinct environments), then use integration for H counts, then decode splitting. Sketch expected shift ranges: CH₃ (~1 ppm), vinyl (~5–6 ppm), aromatic (~7–8 ppm), aldehyde (~9–10 ppm), carboxylic acid (~11–12 ppm).

## Common Misconceptions
- Chemical shift values are not absolute — they are relative to TMS and can shift slightly with solvent, concentration, and temperature.
- The n+1 rule applies only to magnetically non-equivalent neighboring protons and assumes first-order coupling; complex molecules show higher-order patterns.
- ¹³C NMR spectra are typically broad-band decoupled and individual peak heights are NOT proportional to the number of carbons.

## Questions

```yaml
- question: "A ¹H NMR spectrum shows a triplet at 1.2 ppm integrating for 3H, and a quartet at 3.7 ppm integrating for 2H. Which functional group is most consistent with this pattern?"
  type: multiple-choice
  options: ["Methyl ketone (CH₃CO–)", "Ethyl ester (–OCH₂CH₃)", "Isopropyl group (–CH(CH₃)₂)", "Vinyl group (–CH=CH₂)"]
  answer: 1
  explanation: "An ethyl ester's –OCH₂CH₃ group produces exactly this pattern: the CH₃ is split into a triplet by the adjacent CH₂ (2+1=3 lines), and the CH₂ is split into a quartet by the adjacent CH₃ (3+1=4 lines). The downfield shift of the CH₂ (~3.7 ppm) reflects deshielding by the adjacent oxygen."

- question: "In a ¹H NMR spectrum, a proton with a higher chemical shift (more ppm) is more shielded by surrounding electrons."
  type: true-false
  answer: false
  explanation: "Higher ppm means more deshielded, not more shielded. Electronegative groups or aromatic ring currents pull electron density away from a proton, reducing the local magnetic field it experiences and causing it to resonate at higher frequency (higher ppm). A fully shielded reference proton (TMS) resonates at 0 ppm."

- question: "A compound shows a single ¹H NMR peak integrating for 6H. What does this tell you about the proton environments in the molecule?"
  type: short-answer
  answer: "All six protons are chemically equivalent — they exist in a single magnetic environment and produce one signal. This is consistent with a symmetric structure such as acetone (two equivalent CH₃ groups) or dimethyl ether."
  explanation: "One signal means one distinct chemical environment. The integration of 6H suggests either six equivalent protons (like a single CH₃CH₃ group) or two sets of three equivalent protons that happen to have the same shift — though the latter is much less common. Symmetry in the molecular structure is the usual cause."
```

## Explainer

NMR spectroscopy works because certain atomic nuclei — particularly ¹H and ¹³C — behave like tiny bar magnets. When placed in a strong external magnetic field, these nuclei can align with or against the field, and they absorb radiofrequency energy to flip between those states. The exact frequency at which a nucleus absorbs depends on its electronic environment: electrons surrounding a nucleus partially shield it from the external field, so electronegative neighbors that pull electrons away cause the nucleus to resonate at a higher frequency (higher ppm on the chemical shift axis). This is why an aldehyde proton (~10 ppm) appears far downfield compared to a simple alkyl CH (~1 ppm).

The three pieces of information you read from a ¹H NMR spectrum work together like three independent clues. The **chemical shift** tells you what type of environment a proton is in (alkyl, next to oxygen, aromatic, etc.). The **integration** tells you the relative number of protons producing each signal — if one signal is twice as tall as another, it represents twice as many equivalent protons. The **splitting pattern** (multiplicity) tells you how many non-equivalent protons are on adjacent carbons: the n+1 rule states that n neighboring protons split a signal into n+1 lines, creating doublets, triplets, quartets, and so on.

Consider ethanol (CH₃CH₂OH). You expect three signals: the CH₃ group, the CH₂ group, and the OH proton. The CH₃ is adjacent to two CH₂ protons, so it appears as a triplet (2+1=3). The CH₂ is adjacent to three CH₃ protons, so it appears as a quartet (3+1=4). The OH proton is often a broad singlet because fast proton exchange averages out coupling. Integration confirms the 3:2:1 ratio of protons.

¹³C NMR is complementary but interpreted differently. It tells you how many distinct carbon environments exist, but — crucially — peak heights are not proportional to the number of carbons (unlike ¹H integration). This is because different carbons relax at different rates during the experiment. Broad-band decoupling also removes the C-H splitting, so each carbon environment appears as a single line regardless of attached protons.

The power of NMR for structural determination comes from combining all these signals. Unknown compound? Count the ¹H signals to count distinct proton environments, use integration to tally protons in each, decode splitting to map connectivity, and match chemical shifts to functional group tables. Cross-checking with ¹³C NMR and other spectroscopic methods (IR, mass spec) allows complete structure assignment — often without ever synthesizing a reference compound.
