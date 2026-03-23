---
id: greenhouse-gas-absorption-emission
title: Greenhouse Gas Absorption and Emission Spectra
domain: earth-and-space-sciences
course: climate-science
prerequisites:
- id: radiative-transfer-atmospheric
  type: hard
- id: atmosphere-composition-and-structure
  type: hard
- id: ir-spectroscopy-basics
  type: soft
- id: spectroscopy-fundamentals
  type: hard
- id: quantum-mechanics-postulates-core
  type: soft
- id: electromagnetic-spectrum
  type: soft
builds-toward:
- radiative-forcing-greenhouse-gases
- line-by-line-radiative-transfer
tags:
- spectroscopy
- greenhouse-gases
- infrared-radiation
- molecular-properties
stage: expert
status: validated
---

# Greenhouse Gas Absorption and Emission Spectra

## Core Idea
Greenhouse gases absorb and emit thermal infrared radiation at wavelengths determined by their vibrational and rotational transitions. Different gases have distinct spectral signatures; for example, CO₂ absorbs strongly at 15 μm while methane and water vapor absorb at different frequencies. These molecular spectral properties, combined with atmospheric abundance, determine each gas's radiative forcing and contribution to the greenhouse effect.

## Questions

```yaml
- question: "Why are nitrogen (N₂) and oxygen (O₂) not greenhouse gases, despite making up 99% of the atmosphere?"
  type: multiple-choice
  options:
    - "They absorb ultraviolet radiation instead of infrared, so their effect occurs in the upper atmosphere only"
    - "They are greenhouse gases, but their concentrations are so high their absorption bands are already completely saturated"
    - "They have no vibrational modes that produce a changing dipole moment, making them infrared-inactive"
    - "Their absorption bands fall outside the wavelength range of Earth's emitted infrared radiation"
  answer: 2
  explanation: "Interaction with infrared radiation requires a molecule to have a dipole moment that changes during vibration. Symmetric diatomic molecules like N₂ and O₂ have no permanent dipole, and their symmetric stretching mode produces no change in dipole — there is no oscillating electric field for the infrared photon to couple with. This is a quantum mechanical selection rule, not a matter of concentration or saturation. Even if N₂ and O₂ were present in trace amounts, they would still be infrared-inactive."

- question: "CO₂ concentration has increased from 280 ppm (pre-industrial) to 420 ppm today, an increase of 50%. If CO₂ concentration were to double again (from 420 to 840 ppm), how would the additional radiative forcing compare to what occurred going from 280 to 560 ppm?"
  type: multiple-choice
  options:
    - "The forcing from 420→840 ppm would be roughly double the forcing from 280→560 ppm, since more molecules absorb more radiation"
    - "The forcing from 420→840 ppm would be roughly the same as from 280→560 ppm, because each doubling adds approximately the same increment of forcing"
    - "The forcing from 420→840 ppm would be less, because CO₂'s absorption band is becoming saturated and additional molecules have diminishing effect per doubling"
    - "The forcing from 420→840 ppm would be larger, because more CO₂ means more absorption across more atmospheric levels"
  answer: 1
  explanation: "The relationship between CO₂ concentration and radiative forcing is logarithmic: each doubling of CO₂ concentration adds approximately the same increment of forcing (roughly 3.7 W/m²). This means 280→560 ppm adds ~3.7 W/m², 560→1120 ppm adds another ~3.7 W/m², and so on. The reason is that CO₂'s 15 μm core absorption band is already largely saturated — additional CO₂ matters at the band edges and in the upper atmosphere, but these contributions diminish as a fraction of the total with each doubling."

- question: "The greenhouse effect works by greenhouse gases absorbing incoming solar radiation and preventing it from reaching Earth's surface, which heats the atmosphere."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Greenhouse gases are largely transparent to incoming solar radiation (mostly visible and near-infrared wavelengths). The greenhouse effect operates on *outgoing* thermal infrared radiation emitted by Earth's surface and lower atmosphere. Greenhouse gases absorb this outgoing radiation and re-emit it in all directions, including back toward the surface. The net effect is that energy that would otherwise escape to space is retained in the lower atmosphere, warming the surface. Solar radiation that is absorbed gets absorbed by the surface and clouds, not primarily by greenhouse gases."

- question: "CO₂'s dominant absorption band near 15 μm is climatically important partly because it coincides with the peak wavelength range of Earth's outgoing infrared emission at typical surface temperatures."
  type: true-false
  answer: true
  explanation: "Earth's surface emits thermal radiation as an approximate blackbody at ~288 K (15°C), with emission peaking near 10–15 μm. CO₂'s bending mode absorption band is centered near 15 μm, placing it squarely where Earth is radiating most strongly. This spectral coincidence is why CO₂ is so climatically effective despite its relatively low atmospheric concentration (~0.04%). A gas absorbing at wavelengths where Earth emits strongly intercepts a large fraction of the outgoing energy flux."

- question: "Explain why the relationship between CO₂ concentration and radiative forcing is logarithmic rather than linear, and what this implies about the climate impact of each successive doubling."
  type: short-answer
  answer: "The relationship is logarithmic because CO₂'s core absorption band near 15 μm is already largely saturated at current concentrations — the atmosphere is already nearly opaque at that wavelength. Additional CO₂ cannot meaningfully increase absorption at the band center; instead, it widens the absorption at the band edges where the atmosphere is still partially transparent, and increases absorption in the upper atmosphere where air is thinner. Each doubling of CO₂ adds a roughly constant increment of forcing (~3.7 W/m²) because it provides a constant fractional expansion of the absorbing band. This means that, while each doubling has the same warming effect, successive absolute increases in CO₂ (in ppm) have a decreasing marginal effect."
  explanation: "The practical implication is that going from 280 to 560 ppm has the same forcing as going from 560 to 1120 ppm — each doubling adds ~3.7 W/m². This is why climate sensitivity is expressed per doubling, not per ppm increase. It also means early emissions had a larger per-molecule effect than current emissions, since the band was less saturated at lower concentrations."
```

## Explainer

From your study of spectroscopy and radiative transfer, you know that molecules absorb and emit electromagnetic radiation at specific wavelengths determined by their quantum energy levels. For greenhouse gases, the crucial wavelengths fall in the **thermal infrared** (roughly 4–100 μm), which is where Earth's surface and atmosphere emit most of their radiation. The greenhouse effect exists because certain atmospheric gases are transparent to incoming solar radiation (mostly visible light) but opaque to outgoing infrared radiation, trapping energy that would otherwise escape to space.

The reason only certain gases are greenhouse gases comes down to molecular structure. A molecule must have a **dipole moment that changes during vibration** to interact with infrared radiation. Symmetric diatomic molecules like N₂ and O₂ — which make up 99% of the atmosphere — have no permanent dipole and no dipole change during their symmetric stretch, making them infrared-inactive and invisible to thermal radiation. In contrast, molecules like CO₂, H₂O, CH₄, and N₂O have vibrational modes that produce oscillating dipole moments. CO₂, though symmetric overall, has an asymmetric stretch and a bending mode that create temporary dipoles, making it a potent infrared absorber despite having no permanent dipole moment. Water vapor, with its bent geometry, has a permanent dipole and multiple strong absorption bands.

Each greenhouse gas has a characteristic **absorption spectrum** — a fingerprint of wavelengths where it absorbs strongly. CO₂'s dominant absorption band is centered near **15 μm** (the bending mode), which happens to coincide with the peak of Earth's outgoing infrared emission at typical surface temperatures. This spectral coincidence is why CO₂ is so climatically important despite its relatively low concentration. Methane absorbs near 3.3 μm and 7.7 μm, while water vapor absorbs broadly across much of the infrared, with key windows near 8–12 μm where the atmosphere is relatively transparent. The **atmospheric window** near 10 μm is critical because it is one of the few spectral regions where surface radiation can escape directly to space; any gas that absorbs in this window (like ozone near 9.6 μm) has an outsized climate effect.

The radiative impact of a greenhouse gas depends on both its absorption strength and its atmospheric concentration. A gas can be molecule-for-molecule a powerful absorber but climatically insignificant if present in trace amounts. Conversely, a weaker absorber at high concentration can dominate the greenhouse effect — water vapor is the single largest contributor precisely because it is abundant. For CO₂, doubling its concentration does not double its radiative effect because its core absorption band is already nearly **saturated** (the atmosphere is already opaque at 15 μm). Additional CO₂ matters because it widens the absorption band at its edges, where the atmosphere is still partially transparent, and because it absorbs in the upper atmosphere where the air is thinner and emission to space is more efficient. This logarithmic relationship between concentration and forcing — each doubling adds roughly the same increment of forcing — is fundamental to understanding why climate sensitivity is expressed per doubling of CO₂.
