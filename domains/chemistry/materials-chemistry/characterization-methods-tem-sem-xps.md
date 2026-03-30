---
id: characterization-methods-tem-sem-xps
title: 'Characterization Methods: TEM, SEM, XPS'
domain: chemistry
course: materials-chemistry
prerequisites:
- id: x-ray-powder-diffraction
  type: soft
- id: crystal-structures-and-unit-cells
  type: soft
- id: electronic-band-theory-of-solids
  type: soft
- id: nanomaterials-synthesis
  type: soft
builds-toward: []
tags:
- TEM
- SEM
- XPS
- electron microscopy
- surface analysis
- characterization
stage: expert
status: validated
---

# Characterization Methods: TEM, SEM, XPS

## Core Idea
Characterization connects synthesis to properties by revealing the structure, composition, and bonding of materials at length scales from atomic to macroscopic. Transmission electron microscopy (TEM) images internal structure with atomic resolution by passing an electron beam through a thin specimen. Scanning electron microscopy (SEM) images surface topography at nanometer resolution by scanning a focused beam across the surface and detecting secondary or backscattered electrons. X-ray photoelectron spectroscopy (XPS) determines surface elemental composition and chemical bonding state by measuring the kinetic energy of electrons ejected by X-ray irradiation. Together with XRD, these three techniques form the core characterization toolkit for materials chemistry.

## Questions

```yaml
- question: "A materials chemist wants to determine whether the iron in a thin film is present as Fe metal, Fe2O3, or Fe3O4. Which characterization technique would most directly answer this question, and what would be measured?"
  type: short-answer
  answer: "XPS (X-ray photoelectron spectroscopy) would most directly answer this. The Fe 2p XPS spectrum shows characteristic binding energies and satellite structures that differ for Fe(0) (metallic iron, ~707 eV), Fe(II) (in Fe3O4, ~709 eV with specific satellite), and Fe(III) (in Fe2O3, ~711 eV with strong shake-up satellite). The chemical shift in binding energy directly reflects the oxidation state — higher oxidation state = higher binding energy because the remaining electrons are more tightly bound. XPS also provides quantitative surface composition from peak areas."
  explanation: "XPS is uniquely suited for this question because it provides both elemental identification (which elements are present) and chemical state information (oxidation state, bonding environment) from the top 1-10 nm of the surface. XRD could distinguish crystalline Fe2O3 from Fe3O4 by their different diffraction patterns but would not detect amorphous phases and is a bulk technique. Electron diffraction in TEM could also help but requires specialized sample preparation."

- question: "TEM achieves atomic resolution while SEM does not, even though both use electron beams. The key difference is:"
  type: multiple-choice
  options:
    - "TEM uses a higher-energy electron beam that produces sharper images"
    - "TEM transmits electrons through a very thin specimen and forms an image from the transmitted/diffracted beam, enabling phase contrast and diffraction contrast at atomic resolution; SEM scans a focused beam across a thick specimen surface and detects emitted secondary electrons, which cannot achieve atomic resolution"
    - "SEM detects X-rays while TEM detects electrons"
    - "TEM requires a vacuum while SEM operates in air"
  answer: 1
  explanation: "The fundamental difference is geometry. In TEM, the electron beam passes through a specimen thin enough to be electron-transparent (<100 nm), and the transmitted electrons carry information about the internal structure at every point simultaneously — like medical X-ray imaging but with electrons. Phase contrast between transmitted and diffracted beams can resolve individual atomic columns. In SEM, electrons hit a thick surface and generate secondary electrons from the top few nanometers; the resolution is limited by the probe size and interaction volume (~1-10 nm typically, not atomic). Both operate in vacuum."

- question: "XPS can only detect elements present in the top 1-10 nm of a material surface, making it unsuitable for bulk composition analysis."
  type: true-false
  answer: true
  explanation: "XPS is intrinsically surface-sensitive because of the short inelastic mean free path of photoelectrons in solids. When an X-ray ejects an electron from an atom, that electron can only escape the solid without losing energy if it originated within a few nanometers of the surface. Deeper electrons undergo inelastic scattering, losing energy and contributing to the background rather than the characteristic peaks. This surface sensitivity (1-10 nm information depth, depending on the electron kinetic energy and the material) is both XPS's strength (surface composition and chemistry) and its limitation (not representative of bulk). Bulk composition requires techniques like XRF, ICP-OES, or EDS in SEM/TEM."

- question: "In SEM, what information do backscattered electrons (BSE) provide that secondary electrons (SE) do not?"
  type: short-answer
  answer: "Backscattered electrons are beam electrons that have been elastically scattered back out of the sample. The BSE yield increases with atomic number (Z-contrast), so BSE images show compositional contrast — heavier elements appear brighter. Secondary electrons are low-energy electrons ejected from sample atoms; they carry topographic information (surface morphology) but minimal compositional contrast. Using both detectors on the same area provides complementary information: SE images show surface texture and morphology; BSE images reveal compositional variations and phase distributions."
  explanation: "This dual-detector capability makes SEM a powerful tool for microstructural analysis. For example, imaging a polished cross-section of a multi-phase ceramic in BSE mode reveals the spatial distribution of phases with different average atomic numbers, even when they are topographically flat. Combining BSE imaging with energy-dispersive X-ray spectroscopy (EDS) provides both spatial distribution (where phases are) and composition (what elements they contain) from the same instrument."
```

## Explainer

Materials characterization is the experimental backbone of materials chemistry. You can design a synthesis with perfect logic, but without characterization, you cannot know what you actually made — whether the crystal structure is correct, the nanoparticles are the intended size, the surface has the expected composition, or the film has the right thickness. The three techniques covered here — TEM, SEM, and XPS — answer different but complementary questions.

**Scanning electron microscopy** is often the first characterization tool applied to a new material. SEM images the surface topography of a specimen by scanning a focused electron beam (typically 1-20 keV) across the surface and detecting the secondary electrons emitted from each point. The resulting image looks three-dimensional because secondary electron yield depends on the angle between the surface and the beam. SEM requires minimal sample preparation (conductive samples can be imaged directly; non-conducting samples need a thin metal coating), and modern field-emission SEMs achieve resolution below 1 nm. When equipped with an energy-dispersive X-ray (EDS) detector, SEM also provides elemental composition from characteristic X-rays emitted by the sample.

**Transmission electron microscopy** provides the highest spatial resolution of any materials characterization technique — modern aberration-corrected TEMs routinely resolve individual atomic columns. The specimen must be thinned to electron transparency (typically <100 nm), which requires careful preparation by focused ion beam milling, ultramicrotomy, or electropolishing. In bright-field imaging, contrast arises from differences in electron scattering (thicker regions and heavier elements appear darker). In high-resolution TEM (HRTEM), phase contrast between transmitted and diffracted beams produces images of the crystal lattice directly. Selected area electron diffraction (SAED) provides crystallographic information from regions as small as a few hundred nanometers. Scanning TEM (STEM) with a high-angle annular dark-field detector (HAADF-STEM) provides Z-contrast imaging where intensity scales as approximately Z^2.

**X-ray photoelectron spectroscopy** answers a fundamentally different question: what elements are at the surface, and what is their chemical state? XPS irradiates the sample with monochromatic X-rays (typically Al K-alpha, 1486.6 eV), which eject core electrons from atoms in the top few nanometers. The kinetic energy of these photoelectrons is measured by an electron energy analyzer. Since each element has characteristic core electron binding energies, the peak positions identify the elements present. Crucially, the exact binding energy shifts by 1-5 eV depending on the chemical environment (oxidation state, bonding partners) — this chemical shift is what makes XPS uniquely powerful for surface chemistry. Quantitative analysis from peak areas provides surface composition (atomic percentages), and depth profiling by ion sputtering reveals how composition varies with depth.
