---
id: redox-geochemistry
title: Redox Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: aqueous-geochemistry
  type: hard
- id: geochemical-thermodynamics
  type: hard
builds-toward:
- environmental-geochemistry
- sedimentary-geochemistry
- biogeochemistry
tags:
- redox
- oxidation-reduction
- Eh-pH
- electron-transfer
stage: expert
status: validated
---

# Redox Geochemistry

## Core Idea
Redox (reduction-oxidation) reactions involve the transfer of electrons between chemical species and are among the most important processes in Earth systems. The redox state of natural environments -- quantified by Eh (voltage) or pe (electron activity) -- controls the speciation and mobility of many elements (Fe, Mn, S, N, U, As, Cr, Se), governs the stability of minerals (sulfides vs. oxides, reduced vs. oxidized iron minerals), and drives biogeochemical cycling. Earth's surface is fundamentally a redox boundary: the atmosphere is oxidizing (O2-rich), while the subsurface becomes increasingly reducing with depth as oxygen is consumed by organic matter decomposition and mineral reactions. This redox gradient drives much of Earth's surface chemistry.

## Questions

```yaml
- question: "Groundwater flowing through an organic-rich aquifer transitions from oxic to anoxic conditions. The sequence of electron acceptors consumed is: O2, then NO3-, then Mn(IV), then Fe(III), then SO4 2-, then CO2 (methanogenesis). What governs this sequence?"
  type: multiple-choice
  options:
    - "The concentration of each electron acceptor"
    - "Thermodynamic favorability -- each successive electron acceptor yields less free energy per electron transferred when oxidizing organic matter, so organisms preferentially use the most energetically favorable acceptor available"
    - "Microbial species appear in this order by chance"
    - "The sequence is controlled by pH, not redox"
  answer: 1
  explanation: "The terminal electron acceptor sequence reflects decreasing free energy yield. Aerobic respiration (O2) yields the most energy, so O2 is consumed first. When O2 is depleted, denitrification (NO3-) is next most favorable, followed by Mn-reduction, Fe-reduction, sulfate reduction, and finally methanogenesis. This thermodynamic ordering creates predictable redox zones in aquifers, sediments, and stratified water bodies. Organisms using each pathway outcompete those using less favorable acceptors as long as their preferred acceptor remains available."

- question: "The Eh (redox potential) of a natural water can be measured accurately with a platinum electrode in all geological environments."
  type: true-false
  answer: false
  explanation: "Platinum electrodes give reliable Eh measurements only in systems dominated by electroactive couples that equilibrate rapidly with the electrode (Fe2+/Fe3+ in acidic waters, H2S/SO4 in some systems). In many natural waters, multiple redox couples are in disequilibrium with each other, and the electrode responds to a mixed potential that does not correspond to any single couple. Dissolved oxygen, for example, does not equilibrate with a platinum electrode at ambient temperature. Field Eh measurements are therefore interpreted cautiously and often supplemented with direct analysis of redox-sensitive species."

- question: "Explain why arsenic contamination of groundwater is often associated with reducing (anoxic) conditions in aquifers."
  type: short-answer
  answer: "Under oxidizing conditions, arsenic is adsorbed onto iron oxyhydroxide minerals (ferrihydrite, goethite) that coat aquifer sediments. When conditions become reducing (due to organic matter decomposition consuming dissolved oxygen), these iron oxyhydroxides undergo reductive dissolution -- Fe(III) in the mineral is reduced to soluble Fe(II), releasing the adsorbed arsenic into solution. Additionally, arsenate (As(V)) is reduced to arsenite (As(III)), which adsorbs less strongly and is more mobile. This coupled iron-arsenic redox process is the primary mechanism for arsenic contamination affecting tens of millions of people in Bangladesh, India, Vietnam, and other regions with organic-rich, reducing aquifer sediments."
  explanation: "The arsenic crisis illustrates how redox chemistry controls element mobility: arsenic locked on iron oxides under oxidizing conditions is released when reducing conditions dissolve the host mineral."
```

## Explainer

Redox chemistry is the electron economy of the Earth system. Every time an electron is transferred from one species to another, oxidation states change, mineral stabilities shift, and element mobilities are altered. The redox state of an environment -- whether it is oxidizing or reducing -- is among the most important controls on its chemistry and mineralogy.

The Nernst equation provides the quantitative framework: Eh = Eh-naught + (RT/nF) ln(oxidized/reduced). Eh measures the tendency of a system to accept or donate electrons. Positive Eh (oxidizing conditions) means strong electron acceptors are present (O2, NO3-, Fe3+). Negative Eh (reducing conditions) means strong electron donors dominate (organic matter, H2S, Fe2+). The combination of Eh and pH defines the stability fields of redox-sensitive species, plotted on Eh-pH (Pourbaix) diagrams.

The biogeochemical dimension is inseparable from redox geochemistry. Microorganisms catalyze most redox reactions in near-surface environments, using the energy released by electron transfer to fuel their metabolism. The terminal electron acceptor sequence -- O2, NO3-, Mn(IV), Fe(III), SO4 2-, CO2 -- creates systematic redox zonation in aquifers, marine sediments, soils, and wetlands. Each zone has characteristic chemistry: the sulfate reduction zone produces H2S (and sulfide minerals); the Fe-reduction zone mobilizes dissolved iron (and arsenic); the methanogenic zone produces methane. Understanding this zonation is essential for groundwater quality assessment, contaminant fate modeling, and carbon cycle research.

Redox processes also operate at geological time scales. The Great Oxidation Event (~2.4 Ga) transformed Earth's atmosphere from reducing to oxidizing, fundamentally altering mineral stability, chemical weathering, and the geochemical cycling of iron, sulfur, manganese, and uranium. The appearance of red beds (Fe3+-bearing sediments), the disappearance of detrital pyrite and uraninite, and the evolution of sulfate evaporites all record this planetary-scale redox transition. The sedimentary record of redox-sensitive elements is a primary archive of atmospheric and ocean chemistry through time.
