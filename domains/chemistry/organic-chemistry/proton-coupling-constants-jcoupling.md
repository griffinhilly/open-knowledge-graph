---
id: proton-coupling-constants-jcoupling
title: Proton Coupling Constants and Spin-Spin Splitting
domain: chemistry
course: organic-chemistry
prerequisites:
- id: nmr-spectroscopy-organic
  type: hard
tags:
- coupling
- j-coupling
- splitting
- multiplet
- first-order
stage: formal-systems
status: draft
---

# Proton Coupling Constants and Spin-Spin Splitting

## Core Idea
Spin-spin coupling (J coupling) splits NMR signals into multiplets (doublets, triplets, etc.) via the n+1 rule: a proton coupled to n equivalent neighbors appears as an n+1-multiplet. Coupling constants (J, in Hz) are magnetic field-independent and characteristic: ³J (vicinal, 3 bonds) ≈ 8–14 Hz, ⁴J (allylic) ≈ 4–8 Hz, ²J (geminal) ≈ 12–16 Hz. Distinguishing ³J, ⁴J, and ²J helps assign connectivity and conformation.

## Questions

```yaml
- question: "A chemist measures a coupling constant of 7.5 Hz for a doublet on a 300 MHz spectrometer. When she remeasures the same compound on a 600 MHz spectrometer, what does she observe for this coupling constant?"
  type: multiple-choice
  options:
    - "15.0 Hz — coupling constants scale linearly with the magnetic field strength"
    - "7.5 Hz — coupling constants are field-independent molecular properties"
    - "3.75 Hz — coupling constants in ppm are halved when field strength doubles"
    - "The doublet disappears because higher fields resolve the coupling differently"
  answer: 1
  explanation: "Coupling constants (J) are intrinsic molecular properties transmitted through bonding electrons, not through the external magnetic field. They are reported and measured in Hz and do not change when you use a more powerful spectrometer. Chemical shifts in Hz do scale with field (a 1 ppm shift is 300 Hz at 300 MHz but 600 Hz at 600 MHz), but J remains constant. This field-independence is what makes J values reliable for structural assignment across instruments."

- question: "A CH proton in a molecule appears as a doublet of doublets (dd) with J values of 10.2 Hz and 4.5 Hz. What does this pattern indicate about its molecular connectivity?"
  type: multiple-choice
  options:
    - "It is adjacent to a CH₂ group (two equivalent protons), giving a triplet with an average J"
    - "It is coupled to two non-equivalent protons, each with a different coupling constant"
    - "It is on an aromatic ring where meta and ortho couplings produce two J values"
    - "It is geminal to two non-equivalent protons on the same carbon"
  answer: 1
  explanation: "A doublet of doublets arises when one proton is coupled to two other protons that are chemically non-equivalent and have different J values. First, coupling to one neighbor splits the signal into a doublet (J₁ = 10.2 Hz). Then coupling to the second, non-equivalent neighbor splits each of those lines again (J₂ = 4.5 Hz), producing four lines. If the two neighbors were equivalent, you would see a simple triplet (n+1 rule). The dd pattern is definitive evidence for two non-equivalent coupling partners."

- question: "Matching J values between two multiplets in a ¹H NMR spectrum is strong evidence that the corresponding protons are scalar-coupled to each other."
  type: true-false
  answer: true
  explanation: "Because J is a property of a specific pair of coupled nuclei, it appears with the same magnitude in both partners' multiplets. A doublet at 3.5 ppm with J = 7.2 Hz and a triplet at 1.2 ppm also with J = 7.2 Hz almost certainly share a coupling pathway. This matching is the primary tool for reading connectivity from a 1D spectrum. Accidental matches at very common J values (e.g., ~7 Hz) can occur, so corroboration from COSY is preferred in complex molecules."

- question: "The vicinal coupling constant (³J) is approximately the same value regardless of the dihedral angle between the two coupled protons."
  type: true-false
  answer: false
  explanation: "The Karplus equation explicitly relates ³J to the H–C–C–H dihedral angle: J is maximal (~12–14 Hz) when the dihedral is 0° or 180° (periplanar), and minimal (~0–4 Hz) near 90°. This angular dependence is exploited in conformational analysis — a small ³J indicates a ~90° dihedral, while a large ³J indicates a periplanar arrangement. Assuming a fixed vicinal J leads to incorrect conformational conclusions."

- question: "Why are coupling constants reported in hertz (Hz) rather than in parts per million (ppm), and what structural information can be extracted from their values?"
  type: short-answer
  answer: "Coupling constants are reported in Hz because they are field-independent: unlike chemical shifts in Hz, J values do not change when measured on a higher-field spectrometer. This makes J values true molecular constants that can be compared across instruments and used as a reliable structural fingerprint. The magnitude of J reveals the coupling pathway: ³J (vicinal, 3-bond) is typically 6–14 Hz with an angular dependence described by the Karplus equation, so it reports on dihedral angles and conformation; ²J (geminal, 2-bond) is typically 12–16 Hz; long-range ⁴J values are small (~1–3 Hz) except through unsaturation."
  explanation: "The field-independence of J is the key insight. Chemical shifts (in ppm) report on electronic environment; coupling constants report on connectivity and geometry. Together they provide complementary structural information: shift tells you what kind of environment a proton is in; J tells you which protons are nearby in the bonding network and at what angle."
```

## Explainer

From your study of NMR spectroscopy, you know that each chemically distinct proton produces a signal at a characteristic chemical shift. But most real spectra show peaks that are split into patterns — doublets, triplets, quartets — rather than single lines. This splitting arises from **spin-spin coupling** (also called **J coupling**): a proton's magnetic environment is subtly altered by the spin states of nearby protons, transmitted through the bonding electrons rather than through space. The result is that one signal becomes several lines, and the spacing between those lines — the **coupling constant J**, measured in hertz — encodes structural information about the relationship between coupled protons.

The **n+1 rule** is the practical workhorse: a proton with n equivalent neighboring protons splits into n+1 lines. A proton next to two equivalent CH protons appears as a triplet; next to three equivalent protons (as in CH₃), it appears as a quartet. The relative intensities follow Pascal's triangle — 1:1 for a doublet, 1:2:1 for a triplet, 1:3:3:1 for a quartet. This rule applies cleanly when coupled neighbors are equivalent and when chemical shift differences are much larger than J (the **first-order** approximation). When these conditions fail, you get more complex "roofing" patterns and second-order effects.

What makes J values so powerful is that they are **independent of the external magnetic field**. Chemical shifts (in Hz) change if you move from a 300 MHz to a 600 MHz spectrometer, but J values stay the same. This means coupling constants are intrinsic molecular properties. **Vicinal coupling** (³J, through three bonds, H–C–C–H) is the most commonly observed type, typically 6–14 Hz in saturated systems. The Karplus equation relates ³J to the dihedral angle between the coupled protons: J is largest (~12 Hz) when the dihedral angle is 0° or 180° (anti-periplanar) and smallest (~2–4 Hz) near 90°. This makes ³J a direct probe of molecular conformation.

**Geminal coupling** (²J, two bonds, H–C–H) appears when two protons on the same carbon are non-equivalent, typically 12–16 Hz. **Long-range coupling** (⁴J and beyond) is usually small (1–3 Hz) but becomes significant in unsaturated systems — allylic coupling through a C=C bond can reach 4–8 Hz because the π system efficiently transmits spin information. When analyzing a spectrum, matching J values between multiplets is the key to determining which protons are coupled to each other: if a doublet at 3.5 ppm has J = 7.2 Hz and a triplet at 1.2 ppm also has J = 7.2 Hz, those protons are neighbors in the molecular framework.
