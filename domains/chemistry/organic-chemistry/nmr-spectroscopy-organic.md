---
id: nmr-spectroscopy-organic
title: Nuclear Magnetic Resonance Spectroscopy for Structure Determination
domain: chemistry
course: organic-chemistry
prerequisites:
- id: nmr-spectroscopy-basics
  type: hard
- id: ir-spectroscopy-organic
  type: soft
- id: magnetic-field-intro
  type: soft
- id: spin-angular-momentum
  type: soft
- id: quantum-mechanics-postulates-core
  type: soft
- id: nuclear-magnetic-moments
  type: soft
- id: electromagnetic-waves
  type: soft
- id: c-13-nmr-and-ir-structural-determination
  type: soft
builds-toward:
- nmr-chemical-shift-prediction
- proton-coupling-constants-jcoupling
- carbon-13-nmr-analysis
tags:
- nmr
- proton-nmr
- carbon-nmr
- chemical-shift
- integration
stage: formal-systems
status: validated
---
# Nuclear Magnetic Resonance Spectroscopy for Structure Determination

## Core Idea
¹H NMR measures proton environments: chemical shifts (0–10 ppm) reflect the electronic environment; integration shows the relative number of protons; multiplicity (singlet, doublet, etc.) results from coupling to neighboring protons. ¹³C NMR directly observes carbon atoms; offsets reflect carbon environment. 2D techniques (COSY, HSQC, HMBC) correlate nuclei across bonds. NMR is the most powerful routine tool for determining connectivity and confirming molecular structure.

## Questions

```yaml
- question: "A ¹H NMR signal at 3.5 ppm integrates for 2 protons and appears as a triplet. What do these three pieces of information collectively indicate?"
  type: multiple-choice
  options:
    - "Two protons that are adjacent to one neighboring proton"
    - "Two protons near an electronegative atom that are coupled to two neighboring protons"
    - "Three protons that are coupled to two neighboring protons"
    - "Two protons in an aromatic ring with two equivalent neighbors"
  answer: 1
  explanation: "Integration of 2 means there are 2 protons in this environment. A triplet means n+1 = 3, so n = 2 neighboring protons are coupling to this signal. The chemical shift of ~3.5 ppm suggests proximity to an electronegative atom (O, N, halogen), which deshields protons and shifts them downfield from the alkyl region (~1 ppm). All three pieces of information are independent and must be read separately."

- question: "In ¹H NMR, a proton with a larger chemical shift (more ppm) is more shielded by surrounding electrons."
  type: true-false
  answer: false
  explanation: "Larger chemical shift (more ppm, downfield) means the proton is more DESHIELDED — it has less electron density around it and resonates at higher frequency relative to TMS. Electron-withdrawing groups pull electron density away from nearby protons, reducing shielding and increasing their chemical shift. Protons on carbons attached to O, N, or halogens, as well as aromatic and vinyl protons, appear at higher ppm precisely because they are deshielded."

- question: "The ¹H NMR spectrum of ethanol (CH₃CH₂OH) shows a triplet for CH₃ and a quartet for CH₂. Explain why these multiplicities arise and what structural information they provide."
  type: short-answer
  answer: "The CH₃ group has 2 neighboring protons (on CH₂), so n+1 = 3 lines (triplet). The CH₂ group has 3 neighboring protons (on CH₃), so n+1 = 4 lines (quartet). These coupling patterns confirm that the CH₃ and CH₂ groups are on adjacent carbons — the multiplicity directly encodes which carbons are bonded to each other."
  explanation: "The n+1 rule (first-order approximation) predicts the multiplicity of a proton signal based on how many equivalent neighboring protons couple to it. J-coupling occurs through bonds, typically up to 3 bonds. Reading the multiplicity pattern across a spectrum lets you reconstruct adjacencies: if signal A is split by signal B and vice versa, A and B are on neighboring carbons. This makes multiplicity one of NMR's most powerful connectivity-mapping tools."
```

## Explainer

NMR spectroscopy exploits the fact that certain atomic nuclei — especially ¹H and ¹³C — behave like tiny magnets. In a strong external magnetic field, these nuclei align either with or against the field, with a small energy gap between the two states. When a radiofrequency pulse exactly matches that energy gap, the nucleus absorbs energy and "flips." The frequency at which a nucleus flips depends on its local electronic environment, which is what chemical shift measures. Every chemically distinct proton environment gives a separate signal in the spectrum.

Chemical shift (in ppm, measured relative to the reference compound TMS at 0 ppm) tells you about electron density. Protons surrounded by electron-donating groups are shielded — they experience a smaller effective magnetic field and resonate at low ppm (upfield). Protons near electron-withdrawing groups (O, N, halogens, carbonyl) are deshielded and appear at high ppm (downfield). The pattern is reliable: alkyl protons cluster around 0.5–2 ppm; protons on carbons adjacent to heteroatoms appear around 2.5–4.5 ppm; vinyl and aromatic protons are 4.5–8 ppm; aldehyde protons can exceed 9 ppm.

Integration gives the relative number of protons producing each signal. If one signal integrates as 3 and another as 2, the actual proton counts are in a 3:2 ratio — say, a CH₃ and a CH₂. Integration does not give absolute counts; you need some independent information (like molecular formula from mass spectrometry) to convert ratios to absolute numbers. If the molecular formula tells you there are 5 protons total and you see a 3:2 ratio, you know the signals represent 3H and 2H.

Multiplicity arises from spin–spin coupling (J-coupling): the magnetic moment of nearby protons slightly perturbs the magnetic field experienced by the proton you are observing. Under the first-order approximation (n+1 rule), a proton with n equivalent neighboring protons shows n+1 lines. A singlet (1 line) means no neighboring protons; a doublet (2 lines) means 1 neighbor; a triplet means 2; a quartet means 3; and so on. Crucially, coupling is mutual: if proton A splits proton B into a quartet, then proton B splits proton A into a quartet as well, with the same coupling constant J. Reading multiplicities across the spectrum lets you piece together which carbons are adjacent, effectively tracing the molecular skeleton.

¹³C NMR complements ¹H NMR by showing the carbon framework directly. Because ¹³C is only 1.1% naturally abundant, sensitivity is lower, but modern techniques compensate. ¹³C spectra are usually broad-band decoupled, showing a single peak per unique carbon with no splitting. 2D techniques like COSY (which maps H–H coupling) and HSQC (which correlates each ¹H to the ¹³C it is directly attached to) extend these ideas to resolve overlapping signals and confirm assignments in complex molecules. Together, ¹H NMR, ¹³C NMR, and 2D methods form a complete toolkit that can determine the structure of most small organic molecules without X-ray crystallography.
