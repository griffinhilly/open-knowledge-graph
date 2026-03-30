---
id: photovoltaic-materials-chemistry
title: Photovoltaic Materials
domain: chemistry
course: materials-chemistry
prerequisites:
- id: semiconductor-materials-chemistry
  type: hard
- id: electronic-band-theory-of-solids
  type: hard
- id: thin-film-deposition-cvd-pvd
  type: soft
builds-toward: []
tags:
- solar cells
- photovoltaics
- silicon
- perovskites
- band gap engineering
- Shockley-Queisser limit
stage: expert
status: validated
---

# Photovoltaic Materials

## Core Idea
Photovoltaic materials convert sunlight to electricity through the photovoltaic effect: photons with energy greater than the band gap generate electron-hole pairs that are separated by a built-in electric field (p-n junction or heterojunction) and collected as current. The Shockley-Queisser limit sets the maximum theoretical efficiency for a single-junction cell at about 33% (for a 1.34 eV band gap) — photons below the gap are not absorbed, and excess energy above the gap is lost as heat. Materials chemistry drives PV technology: crystalline silicon dominates (95%+ market share, ~26% record efficiency), but thin-film technologies (CdTe, CIGS, perovskites) and multi-junction cells offer routes to higher efficiency or lower cost.

## Questions

```yaml
- question: "The Shockley-Queisser limit for a single-junction solar cell is approximately 33%. A tandem cell stacking two junctions (1.7 eV top cell on 1.1 eV bottom cell) can exceed this limit. Why?"
  type: short-answer
  answer: "A tandem cell splits the solar spectrum between two absorbers. The wide-gap top cell absorbs high-energy photons efficiently (less thermalization loss because the photon energy is closer to the gap). Low-energy photons pass through to the narrow-gap bottom cell, which absorbs them. Each junction operates closer to its optimal voltage, reducing the total energy lost to thermalization. The theoretical limit for an optimal two-junction tandem is about 46%. The materials challenge is finding two absorbers with complementary band gaps and compatible processing — perovskite (1.7 eV) on silicon (1.1 eV) is the leading tandem configuration, with lab efficiencies above 33%."
  explanation: "The Shockley-Queisser limit arises from a fundamental tradeoff: a narrow gap absorbs many photons but with low voltage; a wide gap gives high voltage but absorbs fewer photons. Tandem cells break this tradeoff by using multiple gaps. In the limit of infinite junctions, the theoretical efficiency approaches 68% under concentrated sunlight. Multi-junction III-V cells (GaInP/GaAs/Ge) achieve ~47% under concentration and are used in space and concentrated PV."

- question: "Halide perovskite solar cells (e.g., CH3NH3PbI3) have increased from 3.8% to over 26% efficiency in just 15 years. Which materials properties explain this rapid progress?"
  type: multiple-choice
  options:
    - "Perovskites are cheaper than silicon, so more research funding has been available"
    - "Perovskites have a direct band gap with sharp absorption onset, long carrier diffusion lengths despite being processed from solution, tunable band gap through halide composition, and defect tolerance that maintains performance despite high defect densities"
    - "Perovskites are more stable than silicon, allowing higher operating temperatures"
    - "Perovskites use only abundant, non-toxic elements"
  answer: 1
  explanation: "The remarkable defect tolerance of halide perovskites — high efficiency despite defect densities millions of times higher than in silicon — is the most surprising property. In silicon, a single deep trap kills carrier lifetime; in perovskites, defects tend to be shallow (near band edges) and relatively benign. The direct band gap provides strong absorption in thin (~500 nm) films, and the tunable band gap (1.2-2.3 eV by mixing I/Br/Cl) makes perovskites ideal for both single-junction and tandem configurations. The main unsolved challenge is long-term operational stability — degradation by moisture, heat, and light."

- question: "Silicon solar cells use an indirect band gap material, which means they require thicker absorber layers than direct-gap materials to absorb the same fraction of sunlight."
  type: true-false
  answer: true
  explanation: "Silicon's indirect band gap requires a phonon to assist optical absorption, making the absorption coefficient much lower than for direct-gap materials near the band edge. A crystalline silicon cell needs a ~180 micrometer wafer to absorb most above-gap photons (with light-trapping texturing). A direct-gap material like GaAs or CH3NH3PbI3 absorbs the same light in just 1-2 micrometers. This is why silicon solar cells are relatively thick and rigid, while thin-film technologies (CdTe, CIGS, perovskites) can be deposited as thin layers on flexible substrates. Silicon compensates with mature manufacturing, high material purity, and excellent passivation chemistry."
```

## Explainer

Photovoltaic technology converts the most abundant energy source on Earth — sunlight — into electricity, and the chemistry of the absorber material determines the efficiency, cost, and practicality of every solar cell. The fundamental physics is the same for all PV materials: a photon with energy above the band gap is absorbed, creating an electron-hole pair; a built-in electric field separates the carriers before they recombine; and external contacts collect the photocurrent. The materials chemistry challenge is finding absorbers that maximize this process while being manufacturable at scale.

**Crystalline silicon** dominates photovoltaics because of four decades of manufacturing optimization, not because silicon is the ideal PV material. Its indirect band gap requires thick wafers (~180 micrometers) and elaborate light-trapping texturing. Its surface must be passivated (typically with SiNx or Al2O3) to prevent carrier recombination at dangling bonds. The p-n junction is formed by diffusing phosphorus into a boron-doped wafer. Despite these complications, silicon cell efficiencies now exceed 26% in the lab and 24% in production, approaching the Shockley-Queisser limit. The manufacturing learning curve has driven module costs below $0.20/watt, making solar electricity cheaper than fossil fuel generation in most of the world.

**Thin-film technologies** use direct-gap materials that absorb sunlight in layers 100-1000 times thinner than silicon. **CdTe** (1.45 eV direct gap, close to the S-Q optimum) is the leading thin-film technology, manufactured by First Solar at GW scale. The chemistry challenge is controlling the CdTe/CdS heterojunction and managing the toxicity of cadmium. **CIGS** (Cu(In,Ga)Se2) offers band gap tunability through the In/Ga ratio but suffers from compositional complexity (four elements that must be precisely controlled). **Halide perovskites** (methylammonium or formamidinium lead halides) have achieved >26% efficiency from solution processing — a manufacturing paradigm-shift — but stability under real-world conditions remains the critical unsolved problem.

The frontier of PV materials chemistry is **tandem cells** that exceed the single-junction Shockley-Queisser limit. A perovskite top cell (1.7 eV) on a silicon bottom cell (1.1 eV) can theoretically reach ~43% efficiency by using each part of the solar spectrum more efficiently. Perovskite/silicon tandems have already exceeded 33% in the lab, surpassing the theoretical limit for silicon alone. The materials chemistry challenges are formidable: the perovskite must be stable for 25+ years, the intermediate recombination layer must be optically transparent and electrically conductive, and the processing of the perovskite must not damage the underlying silicon cell. Solving these challenges represents one of the highest-impact applications of materials chemistry to global energy problems.
