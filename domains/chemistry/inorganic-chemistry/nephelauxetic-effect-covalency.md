---
id: nephelauxetic-effect-covalency
title: Nephelauxetic Effect and Covalency
domain: chemistry
course: inorganic-chemistry
prerequisites:
- id: electronic-spectra-tanabe-sugano
  type: hard
- id: ligand-field-theory
  type: hard
builds-toward: []
tags:
- nephelauxetic effect
- Racah parameters
- covalency
- cloud-expanding
- beta ratio
stage: expert
status: validated
---

# Nephelauxetic Effect and Covalency

## Core Idea
The nephelauxetic effect ("cloud-expanding" in Greek) describes the reduction of interelectronic repulsion parameters (Racah B and C) in a coordination compound compared to the free ion. When ligands form covalent bonds with the metal, the d-electron cloud expands into ligand-based orbitals, reducing electron-electron repulsion. The nephelauxetic ratio β = B_complex/B_free ion quantifies the degree of covalency: smaller β indicates greater covalency. This effect provides a direct experimental measure of how "ionic" or "covalent" a metal-ligand bond is.

## Questions

```yaml
- question: "The Racah parameter B for [Cr(H₂O)₆]³⁺ is 725 cm⁻¹, while the free-ion value for Cr³⁺ is 918 cm⁻¹. What is the nephelauxetic ratio, and what does it indicate?"
  type: multiple-choice
  options:
    - "β = 1.27, indicating the complex has stronger electron repulsion than the free ion"
    - "β = 0.79, indicating that the d-electron cloud has expanded due to covalent metal-ligand interaction, reducing interelectronic repulsion to 79% of the free-ion value"
    - "β = 0.79, indicating that 79% of the crystal field splitting comes from electrostatic interactions"
    - "β = 193, representing the absolute reduction in repulsion energy"
  answer: 1
  explanation: "β = B_complex/B_free ion = 725/918 = 0.79. A value less than 1 means the interelectronic repulsion in the complex is less than in the free ion. This reduction occurs because the d-electron cloud is no longer confined to the metal — it delocalizes partially onto the ligands through covalent bonding, effectively expanding the cloud and reducing electron-electron repulsion. The 21% reduction for [Cr(H₂O)₆]³⁺ indicates modest covalent character. More covalent complexes (like [Cr(CN)₆]³⁻) have even smaller β values."

- question: "The nephelauxetic series ranks ligands by their ability to reduce the Racah parameter: F⁻ > H₂O > NH₃ > en > ox > NCS⁻ > Cl⁻ > CN⁻ > Br⁻ > I⁻ (from least to most cloud-expanding)."
  type: true-false
  answer: true
  explanation: "This series ranks ligands from most ionic (F⁻, smallest nephelauxetic effect, β closest to 1) to most covalent (I⁻, largest nephelauxetic effect, smallest β). The ordering correlates with ligand polarizability and the extent of orbital overlap with the metal: small, hard, electronegative ligands like F⁻ interact primarily electrostatically and do not expand the d-cloud much. Large, soft, polarizable ligands like I⁻ and CN⁻ engage in significant covalent bonding, delocalizing d-electron density onto the ligand and strongly reducing B. Note that this series is NOT the same as the spectrochemical series — it measures covalency, not field strength."

- question: "A complex with β = 0.5 has more ionic character in its metal-ligand bonds than one with β = 0.9."
  type: true-false
  answer: false
  explanation: "β = 0.5 means the Racah parameter is reduced to half the free-ion value — a large reduction indicating substantial d-electron delocalization onto the ligands, which means high covalent character. β = 0.9 means only 10% reduction — the d-electrons remain largely metal-centered, indicating predominantly ionic character. Lower β = more covalent, higher β = more ionic. A perfectly ionic complex (point-charge ligands with zero orbital overlap) would have β = 1.0."

- question: "Explain why the nephelauxetic effect and the spectrochemical series are related but distinct, using a specific example where a ligand ranks differently in each series."
  type: short-answer
  answer: "The spectrochemical series ranks ligands by crystal field splitting Δ (which includes both sigma and pi bonding effects), while the nephelauxetic series ranks them by covalency (the degree of d-electron delocalization). These are related — more covalent bonding generally affects Δ — but they measure different things. F⁻ illustrates the difference: it is a moderate-field ligand in the spectrochemical series (above I⁻ and Cl⁻ but below H₂O and NH₃) but has the smallest nephelauxetic effect (most ionic). Its small size and high electronegativity create a strong electrostatic interaction (contributing to Δ) but poor orbital overlap (low covalency). CN⁻ ranks high in both series because it is both a strong-field ligand (pi-acceptor, large Δ) and highly covalent (strong orbital overlap, small β)."
  explanation: "This distinction matters because models that treat all metal-ligand bonding as either purely electrostatic (CFT) or purely covalent (naive MO theory) miss the spectrum of bonding character that real complexes display. The nephelauxetic ratio provides the experimental evidence for where each specific metal-ligand combination falls on this spectrum."
```

## Explainer

Crystal field theory treats ligands as point charges, but real ligands are not points — they have orbitals that overlap with the metal d-orbitals, creating genuine covalent bonds. The nephelauxetic effect provides direct experimental evidence for this covalency by measuring how much the interelectronic repulsion within the d-shell is reduced when the metal ion is placed in a coordination environment.

The physical picture is intuitive. In a free metal ion, the d-electrons are confined to a relatively small volume around the nucleus. When ligands approach and form covalent bonds, the d-orbitals acquire some ligand character — the electron cloud literally expands ("nephelauxetic" comes from the Greek for "cloud-expanding"). This expansion increases the average distance between d-electrons, reducing their mutual repulsion. The Racah parameter B, which quantifies this repulsion, decreases from its free-ion value B₀ to a smaller value B in the complex. The ratio β = B/B₀ directly measures the extent of covalent delocalization.

The nephelauxetic series ranks both ligands and metal ions by their contribution to the effect. For ligands: F⁻ (most ionic, β ≈ 1) < H₂O < NH₃ < Cl⁻ < CN⁻ < Br⁻ < I⁻ (most covalent, smallest β). For metals: Mn²⁺ (most ionic) < Ni²⁺ < Co²⁺ < Fe²⁺ < Cr²⁺ (most covalent among the divalent first-row metals). The total nephelauxetic reduction is approximately the product of the metal and ligand contributions: β ≈ 1 − h_ligand × k_metal, where h and k are empirical parameters tabulated for common ligands and metals. This empirical formula works remarkably well, supporting the idea that the metal and ligand contributions to covalency are approximately independent.

The nephelauxetic effect has practical consequences for spectroscopy. When fitting electronic spectra using Tanabe-Sugano diagrams, you must use the reduced B value for the complex, not the free-ion value. The difference between B and B₀ is often 20-40% for common complexes — too large to ignore. Moreover, the nephelauxetic ratio provides information that the spectrochemical series alone cannot: two ligands may produce similar Δ values but very different β values, indicating different bonding character. This dual characterization — Δ for field strength, β for covalency — gives a much more complete picture of the metal-ligand bond than either parameter alone.
