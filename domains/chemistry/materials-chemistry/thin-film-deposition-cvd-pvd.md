---
id: thin-film-deposition-cvd-pvd
title: 'Thin Film Deposition: CVD and PVD'
domain: chemistry
course: materials-chemistry
prerequisites:
- id: semiconductor-materials-chemistry
  type: soft
- id: crystal-structures-and-unit-cells
  type: soft
- id: chemical-kinetics
  type: soft
builds-toward:
- photovoltaic-materials-chemistry
tags:
- thin films
- chemical vapor deposition
- physical vapor deposition
- sputtering
- epitaxy
stage: expert
status: validated
---

# Thin Film Deposition: CVD and PVD

## Core Idea
Thin film deposition creates layers of material from nanometers to micrometers thick on a substrate, enabling the fabrication of semiconductor devices, optical coatings, protective layers, and functional surfaces. Chemical vapor deposition (CVD) uses gas-phase chemical reactions to deposit material: volatile precursors decompose or react at the heated substrate surface to form a solid film. Physical vapor deposition (PVD) transfers material from a source to a substrate without chemical transformation: evaporation, sputtering, or pulsed laser ablation ejects atoms that condense on the substrate. The choice between CVD and PVD depends on the desired film composition, crystallinity, conformality, deposition rate, and substrate compatibility.

## Questions

```yaml
- question: "In chemical vapor deposition of silicon from silane (SiH4), the film growth rate can be limited by either gas-phase mass transport or surface reaction kinetics. At low temperatures, which regime dominates and why?"
  type: short-answer
  answer: "At low temperatures, the surface reaction is slow because the decomposition of SiH4 on the surface has an activation energy barrier (~1.6 eV). Mass transport of SiH4 to the surface is relatively fast and temperature-insensitive. Therefore, the overall rate is limited by the surface reaction — this is the reaction-rate-limited (or kinetically controlled) regime. Growth rate increases exponentially with temperature (Arrhenius behavior). At high temperatures, the surface reaction becomes fast enough that the rate is limited by how quickly fresh SiH4 can diffuse through the boundary layer to the surface — the mass-transport-limited regime, where growth rate depends on gas flow and geometry rather than temperature."
  explanation: "The transition between regimes has practical importance: the reaction-limited regime gives better film uniformity because the growth rate depends only on local temperature (which is uniform on a well-designed substrate heater), not on local gas flow patterns. The mass-transport-limited regime gives higher deposition rates. Industrial CVD processes are usually designed to operate in the reaction-limited regime for uniform films or the mass-transport-limited regime when throughput matters more than uniformity."

- question: "Sputtering (a PVD technique) can deposit alloy films with compositions matching the target material, which is difficult to achieve by thermal evaporation."
  type: true-false
  answer: true
  explanation: "In thermal evaporation, each element evaporates at a rate proportional to its vapor pressure at the source temperature. Since different elements have different vapor pressures, the film composition differs from the source composition — the more volatile element is enriched. In sputtering, energetic ions (typically Ar+) physically knock atoms out of the target surface. The sputter yield depends on atomic mass and binding energy, not vapor pressure, and the differences between elements are much smaller. As a result, a multi-component target produces a film with nearly the same composition. This makes sputtering the preferred PVD method for depositing alloys and complex oxides."

- question: "Atomic layer deposition (ALD) achieves atomic-level thickness control by using sequential, self-limiting surface reactions. Why is ALD preferred over conventional CVD for depositing conformal films in high-aspect-ratio features?"
  type: multiple-choice
  options:
    - "ALD uses lower temperatures, preventing thermal damage to the substrate"
    - "Each ALD cycle deposits exactly one monolayer regardless of local precursor flux, so growth is uniform even in deep trenches where gas flow is restricted"
    - "ALD precursors are less toxic than CVD precursors"
    - "ALD films are always crystalline, while CVD films are always amorphous"
  answer: 1
  explanation: "The key advantage of ALD is self-limiting growth. In each half-cycle, precursor A reacts with the surface until every available site is occupied — then the reaction stops, regardless of how much more precursor arrives. The excess is purged, and precursor B reacts with the A-covered surface, again self-limiting. Each full cycle adds a fixed thickness (typically 0.5-1.5 Angstroms). Because the reaction is self-limiting, it does not matter whether the surface is at the top of a trench or at the bottom — every surface atom gets the same exposure if given enough time. This produces perfectly conformal films even in features with aspect ratios above 100:1."
```

## Explainer

Thin films are ubiquitous in modern technology. Every semiconductor chip contains dozens of deposited thin films — gate oxides, metal interconnects, diffusion barriers, anti-reflection coatings. Solar cells, low-emissivity windows, hard coatings on cutting tools, and anti-corrosion layers on turbine blades all rely on thin film deposition. The chemistry of how these films form, and the resulting structure and properties, differ fundamentally between CVD and PVD.

**Chemical vapor deposition** delivers volatile precursor molecules to a heated substrate, where they undergo chemical reactions — decomposition, oxidation, reduction, or exchange — to deposit a solid film. The chemistry is rich and varied. Silicon films from SiH4 decomposition; SiO2 from SiH4 + O2 or from tetraethyl orthosilicate (TEOS); TiN from TiCl4 + NH3; diamond from CH4/H2 plasmas. The precursor chemistry determines not only what film you can deposit but also the deposition temperature, impurity levels, and film microstructure. Metal-organic CVD (MOCVD) uses organometallic precursors to achieve lower deposition temperatures and access compositions that chloride precursors cannot. Plasma-enhanced CVD (PECVD) uses plasma activation to lower substrate temperatures further, enabling deposition on temperature-sensitive substrates.

**Physical vapor deposition** bypasses chemistry entirely — atoms or molecules are physically transferred from a source to a substrate. In **thermal evaporation**, the source material is heated until it evaporates, and the vapor condenses on a cooler substrate. In **sputtering**, energetic ions (usually Ar+) bombard a solid target, ejecting atoms that travel to the substrate. In **pulsed laser deposition** (PLD), a focused laser ablates material from a target, producing a plasma plume that deposits on the substrate. PVD operates in vacuum, produces high-purity films, and allows precise thickness control through deposition rate monitoring (quartz crystal microbalance).

**Atomic layer deposition** (ALD) is a special variant of CVD that achieves ultimate thickness control. By alternating two self-limiting half-reactions — each precursor reacts only with the surface functional groups left by the previous precursor — ALD deposits exactly one atomic layer per cycle. The self-limiting nature means that film thickness depends only on the number of cycles, not on precursor flux, temperature variations, or substrate geometry. ALD of Al2O3 from trimethylaluminum and water is the canonical example: each cycle adds about 1.1 Angstroms. This precision makes ALD indispensable for gate dielectrics in sub-10-nm transistors, conformal coatings in 3D NAND flash memory, and catalytic coatings on nanostructured substrates.
