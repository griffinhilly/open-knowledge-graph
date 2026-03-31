---
id: sedimentary-geochemistry
title: Sedimentary Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: aqueous-geochemistry
  type: hard
- id: redox-geochemistry
  type: soft
- id: ree-patterns-geochemistry
  type: soft
builds-toward:
- organic-geochemistry
- environmental-geochemistry
tags:
- sedimentary-geochemistry
- diagenesis
- provenance
- chemostratigraphy
stage: expert
status: validated
---

# Sedimentary Geochemistry

## Core Idea
Sedimentary geochemistry examines the chemical processes and signatures in sediments and sedimentary rocks, from their formation through weathering and transport to their burial and diagenetic transformation. Sediment chemistry records source rock composition (provenance), weathering intensity, redox conditions in the depositional environment, and post-depositional diagenetic modifications. Key tools include major-element weathering indices (CIA, CIW), REE patterns for provenance, redox-sensitive trace elements (Mo, U, V, Re) for paleoenvironmental reconstruction, and stable isotope chemostratigraphy (delta-13C, delta-34S, delta-18O) for global biogeochemical changes. Sedimentary rocks are the archive of Earth's surface conditions through time.

## Questions

```yaml
- question: "A black shale has extremely high Mo (100 ppm) and U (20 ppm) concentrations compared to average shale (Mo ~1 ppm, U ~3 ppm). What does this indicate about the depositional environment?"
  type: multiple-choice
  options:
    - "The shale was deposited in a highly oxidizing environment"
    - "The shale was deposited under euxinic (anoxic, sulfidic) conditions where Mo is quantitatively scavenged from seawater by reaction with dissolved H2S and organic matter, and U(VI) is reduced to insoluble U(IV) and concentrated in the sediment"
    - "The shale has been hydrothermally altered"
    - "The high Mo reflects volcanic ash input"
  answer: 1
  explanation: "Mo is soluble in oxygenated seawater as molybdate (MoO4 2-) but is quantitatively removed under euxinic conditions where H2S converts it to particle-reactive thiomolybdate species that are scavenged. Similarly, U is soluble as U(VI) but reduced to insoluble U(IV) in anoxic waters. Extreme enrichments of both elements together are diagnostic of euxinic bottom waters -- a key indicator used to reconstruct ocean redox through Earth history."

- question: "The Chemical Index of Alteration (CIA) can be used to assess the intensity of chemical weathering recorded in sedimentary rocks."
  type: true-false
  answer: true
  explanation: "CIA = [Al2O3 / (Al2O3 + CaO* + Na2O + K2O)] x 100, where CaO* is silicate-bound CaO only. During chemical weathering, Ca, Na, and K are progressively leached from feldspars while Al remains in residual clay minerals. Fresh feldspar-rich rocks have CIA ~50; intensely weathered residual clays approach CIA ~100. Sedimentary rock CIA values between 50 and 100 record the cumulative intensity of source-area weathering, providing a proxy for paleoclimate (warm, humid climates produce more intense weathering)."

- question: "Explain why redox-sensitive trace elements are more reliable paleoenvironmental indicators than sediment color alone."
  type: short-answer
  answer: "Sediment color is qualitative, can be modified by diagenesis (organic matter oxidation, secondary iron reduction), and depends on mineral type as much as redox conditions. Redox-sensitive elements (Mo, U, V, Re) have quantitative enrichment patterns that are directly tied to dissolved-oxygen and sulfide concentrations in bottom water through well-understood aqueous chemistry. Their enrichment factors can be calibrated against modern environments with known redox conditions. Multi-element ratios (e.g., Mo/U) discriminate between suboxic, anoxic, and euxinic conditions. These geochemical proxies provide reproducible, quantitative redox reconstruction that sediment color cannot."
  explanation: "Color is ambiguous and alterable; element enrichments are quantitative and mechanistically linked to specific redox thresholds."
```

## Explainer

Sedimentary rocks are Earth's memory. They record the chemistry of past oceans, atmospheres, weathering regimes, and biological systems in mineral assemblages, major and trace element concentrations, and isotopic compositions that can be measured billions of years after deposition. Sedimentary geochemistry reads this archive.

Provenance analysis uses immobile elements and their ratios to identify the tectonic setting and lithology of the source terrain. REE patterns (Eu anomaly, LREE/HREE slope), Th/Sc ratios (felsic sources have high Th/Sc), and Cr/Th ratios (mafic sources have high Cr) discriminate between felsic continental, mafic oceanic, and recycled sedimentary sources. These ratios survive weathering, transport, and moderate diagenesis, preserving source information in ancient sediments.

Paleoenvironmental reconstruction relies on elements whose behavior changes dramatically with redox conditions. In modern oceans, Mo, V, Re, and U are dissolved under oxygenated conditions but become insoluble and accumulate in sediments under anoxic or euxinic conditions. By measuring their enrichments in ancient sediments and calibrating against modern analogs (Black Sea, Cariaco Basin), geochemists reconstruct the redox state of past water bodies. The secular record of these elements through Earth history documents major oxygenation events, ocean anoxic events, and the long-term evolution of marine redox chemistry.

Diagenesis -- the chemical and physical changes occurring after deposition -- modifies the primary geochemical signal. Organic matter is microbially degraded through the terminal electron acceptor sequence. Pore waters evolve as minerals dissolve and precipitate. Authigenic minerals (pyrite, siderite, dolomite, glauconite) form in the sediment column. Understanding diagenesis is essential for interpreting primary signals correctly and for recognizing which geochemical proxies survive burial and which are overprinted.
