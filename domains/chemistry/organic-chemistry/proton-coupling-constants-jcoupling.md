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
stage: advanced
status: draft
---

# Proton Coupling Constants and Spin-Spin Splitting

## Core Idea
Spin-spin coupling (J coupling) splits NMR signals into multiplets (doublets, triplets, etc.) via the n+1 rule: a proton coupled to n equivalent neighbors appears as an n+1-multiplet. Coupling constants (J, in Hz) are magnetic field-independent and characteristic: ³J (vicinal, 3 bonds) ≈ 8–14 Hz, ⁴J (allylic) ≈ 4–8 Hz, ²J (geminal) ≈ 12–16 Hz. Distinguishing ³J, ⁴J, and ²J helps assign connectivity and conformation.

## Explainer

From your study of NMR spectroscopy, you know that each chemically distinct proton produces a signal at a characteristic chemical shift. But most real spectra show peaks that are split into patterns — doublets, triplets, quartets — rather than single lines. This splitting arises from **spin-spin coupling** (also called **J coupling**): a proton's magnetic environment is subtly altered by the spin states of nearby protons, transmitted through the bonding electrons rather than through space. The result is that one signal becomes several lines, and the spacing between those lines — the **coupling constant J**, measured in hertz — encodes structural information about the relationship between coupled protons.

The **n+1 rule** is the practical workhorse: a proton with n equivalent neighboring protons splits into n+1 lines. A proton next to two equivalent CH protons appears as a triplet; next to three equivalent protons (as in CH₃), it appears as a quartet. The relative intensities follow Pascal's triangle — 1:1 for a doublet, 1:2:1 for a triplet, 1:3:3:1 for a quartet. This rule applies cleanly when coupled neighbors are equivalent and when chemical shift differences are much larger than J (the **first-order** approximation). When these conditions fail, you get more complex "roofing" patterns and second-order effects.

What makes J values so powerful is that they are **independent of the external magnetic field**. Chemical shifts (in Hz) change if you move from a 300 MHz to a 600 MHz spectrometer, but J values stay the same. This means coupling constants are intrinsic molecular properties. **Vicinal coupling** (³J, through three bonds, H–C–C–H) is the most commonly observed type, typically 6–14 Hz in saturated systems. The Karplus equation relates ³J to the dihedral angle between the coupled protons: J is largest (~12 Hz) when the dihedral angle is 0° or 180° (anti-periplanar) and smallest (~2–4 Hz) near 90°. This makes ³J a direct probe of molecular conformation.

**Geminal coupling** (²J, two bonds, H–C–H) appears when two protons on the same carbon are non-equivalent, typically 12–16 Hz. **Long-range coupling** (⁴J and beyond) is usually small (1–3 Hz) but becomes significant in unsaturated systems — allylic coupling through a C=C bond can reach 4–8 Hz because the π system efficiently transmits spin information. When analyzing a spectrum, matching J values between multiplets is the key to determining which protons are coupled to each other: if a doublet at 3.5 ppm has J = 7.2 Hz and a triplet at 1.2 ppm also has J = 7.2 Hz, those protons are neighbors in the molecular framework.
