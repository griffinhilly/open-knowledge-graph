---
id: jahn-teller-effect
title: Jahn-Teller Effect
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: crystal-field-theory
  type: hard
- id: magnetism-coordination-compounds
  type: soft
- id: group-theory-applications-inorganic
  type: soft
- id: term-symbols-d-electron
  type: soft
builds-toward: []
tags:
- Jahn-Teller distortion
- tetragonal distortion
- d-orbital degeneracy
- structural distortion
stage: expert
status: validated
---

# Jahn-Teller Effect

## Core Idea
The Jahn-Teller theorem states that any non-linear molecule in an orbitally degenerate electronic state will undergo a geometric distortion that removes the degeneracy and lowers the total energy. In coordination chemistry, this manifests most strongly in octahedral complexes with unequally occupied eg orbitals (especially d⁴ high-spin, d⁷ low-spin, and d⁹ configurations), which distort from perfect octahedral to tetragonally elongated (or compressed) geometries. The effect explains anomalous bond lengths, thermodynamic stabilities, and spectroscopic properties.

## Questions

```yaml
- question: "Cu²⁺ (d⁹) octahedral complexes almost always show tetragonal elongation — four short equatorial bonds and two long axial bonds. Why?"
  type: multiple-choice
  options:
    - "Cu²⁺ is too small to accommodate six equivalent ligands"
    - "The d⁹ configuration places three electrons in the eg set (one orbital filled, one half-filled), creating an unequal occupation that is stabilized by elongating along the z-axis, which lowers d_z² below d_x²−y² and places the paired electrons in the lower orbital"
    - "Crystal packing forces always favor elongation over compression for copper compounds"
    - "The d⁹ configuration causes Hund's rule to break down, forcing distortion"
  answer: 1
  explanation: "For d⁹ in Oh, the electron configuration is t₂g⁶ eg³ — three electrons in two eg orbitals (one orbital must have 2, the other must have 1). This unequal occupation creates an orbital degeneracy: either d_z² has 2 and d_x²−y² has 1, or vice versa. The Jahn-Teller theorem says this degeneracy is unstable. Tetragonal elongation along z weakens the axial bonds, lowering the d_z² orbital energy. The configuration becomes (d_z²)² (d_x²−y²)¹ — placing the pair in the lower orbital. This is why virtually all Cu²⁺ octahedral complexes show two long axial bonds and four shorter equatorial bonds."

- question: "The Jahn-Teller effect applies only to complexes with eg orbital degeneracy; t₂g orbital degeneracy does not cause significant structural distortion."
  type: true-false
  answer: false
  explanation: "The Jahn-Teller theorem applies to ANY orbital degeneracy. However, the magnitude of the distortion depends on which orbitals are involved. Unequal occupation of the eg orbitals (which point directly at the ligands) causes large distortions because these orbitals are strongly antibonding and their occupancy directly affects metal-ligand bond lengths. Unequal occupation of the t₂g orbitals (which point between the ligands) causes much smaller distortions because these orbitals are weakly bonding or nonbonding. The distinction is between 'strong' (eg) and 'weak' (t₂g) Jahn-Teller effects. d¹ and d² configurations have t₂g degeneracy but show only minor structural effects."

- question: "A d⁴ high-spin octahedral complex (t₂g³ eg¹) is expected to show a Jahn-Teller distortion, while a d³ octahedral complex (t₂g³ eg⁰) is not."
  type: true-false
  answer: true
  explanation: "d³ has the configuration t₂g³ — one electron in each of the three t₂g orbitals. The t₂g set is evenly occupied (no degeneracy), and eg is empty, so there is no Jahn-Teller distortion. d⁴ high-spin has t₂g³ eg¹ — the single eg electron can be in either d_z² or d_x²−y², creating an orbital degeneracy. The Jahn-Teller effect removes this degeneracy through tetragonal distortion. This is seen in Cr²⁺ (d⁴) and Mn³⁺ (d⁴) octahedral complexes, which show characteristic elongated octahedral geometries with measurably different axial and equatorial bond lengths."

- question: "Explain why the double-humped shape of the lattice energy curve across the first-row transition metal divalent ions (the 'double-humped' plot of hydration enthalpy vs. atomic number) provides evidence for both crystal field stabilization energy and the Jahn-Teller effect."
  type: short-answer
  answer: "If crystal field effects were absent, hydration enthalpies would decrease smoothly across the transition series (due to the steady increase in effective nuclear charge and decrease in ionic radius). The actual plot shows two humps: values for d³ (Cr²⁺ is anomalous due to JT) and d⁸ are higher than the smooth baseline, while d⁰, d⁵ (high-spin), and d¹⁰ fall on the baseline. The humps reflect CFSE — configurations with large CFSE (d³, d⁶ low-spin, d⁸) gain extra stabilization in the octahedral aqua complex. The anomalously high value for Cu²⁺ (d⁹) — higher than expected from CFSE alone — is attributed to the additional stabilization from the Jahn-Teller distortion, which lowers the total energy by splitting the eg degeneracy and placing the electron pair in the lower orbital."
  explanation: "This plot is one of the most cited pieces of evidence for crystal field effects in real chemistry. The Jahn-Teller contribution at d⁹ (and to a lesser extent at d⁴) adds a specific, identifiable increment above the CFSE-only prediction."
```

## Explainer

The Jahn-Teller theorem, proven by Hermann Jahn and Edward Teller in 1937, is a remarkable result from group theory: it states that for any non-linear molecule in an electronically degenerate state, there always exists at least one vibrational mode that breaks the symmetry and lowers the energy. In plain language: if a molecule has a choice of putting electrons in two orbitals of equal energy, it will distort its geometry to make those orbitals unequal — spontaneously breaking its own symmetry to achieve a lower total energy.

For coordination chemistry, the most important cases involve unequal occupation of the eg orbitals in octahedral complexes. The eg orbitals (d_z² and d_x²−y²) point directly at the ligands. If one has more electrons than the other, the metal-ligand bonds along the more-populated orbital's axis experience greater repulsion. The complex distorts — typically by elongating along the z-axis — to relieve this asymmetric repulsion. The elongation weakens the axial metal-ligand interaction, lowering d_z² relative to d_x²−y². The electrons redistribute to favor the lower orbital, and the net energy is reduced. The configurations most affected are d⁴ high-spin (t₂g³ eg¹), d⁷ low-spin (t₂g⁶ eg¹), and d⁹ (t₂g⁶ eg³).

Copper(II) is the textbook Jahn-Teller ion. Every Cu²⁺ octahedral complex shows measurable tetragonal distortion: four equatorial bonds of one length and two axial bonds typically 10-30% longer. This is not a subtle crystallographic effect — it is a fundamental electronic phenomenon visible in crystal structures, absorption spectra (which show multiple bands instead of the single band expected for a regular octahedron), and thermodynamic data. The anomalously large hydration enthalpy of Cu²⁺ compared to the smooth trend across the transition series is partly attributable to this additional Jahn-Teller stabilization.

The Jahn-Teller effect also applies to t₂g degeneracy, but with much weaker structural consequences because the t₂g orbitals do not point at the ligands and therefore have less influence on bond lengths. This "dynamic" Jahn-Teller effect in t₂g-degenerate systems is observable spectroscopically (broadened absorption bands) but rarely produces the dramatic structural distortions seen with eg degeneracy. Understanding when to expect strong versus weak Jahn-Teller effects — and recognizing their signatures in structural and spectroscopic data — is an essential skill for interpreting the properties of transition metal compounds.
