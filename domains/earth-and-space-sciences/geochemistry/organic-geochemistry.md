---
id: organic-geochemistry
title: Organic Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: carbon-isotopes-geochemistry
  type: hard
- id: sedimentary-geochemistry
  type: soft
builds-toward:
- biogeochemistry
tags:
- organic-geochemistry
- biomarkers
- kerogen
- petroleum-geochemistry
stage: expert
status: validated
---

# Organic Geochemistry

## Core Idea
Organic geochemistry studies the fate of carbon-based compounds from their biological origin through burial, diagenesis, catagenesis, and metamorphism. Organic matter in sediments ranges from recognizable biomolecules to complex, insoluble kerogen. Biomarkers (molecular fossils) are specific organic compounds whose structures preserve information about their biological source, even after millions of years of burial: steranes record eukaryotic input, hopanes indicate bacterial sources, and alkenones record sea surface temperature through their degree of unsaturation. The thermal maturation of kerogen generates petroleum (oil and gas) through catagenesis, with the type and thermal history of the organic matter controlling whether oil, gas, or neither is produced. Organic carbon burial is also a primary control on atmospheric O2 through geological time.

## Questions

```yaml
- question: "Sedimentary rocks from the late Archean (2.7 Ga) contain 2-alpha-methylhopanes, which are biomarkers specific to cyanobacteria. What is the significance of this finding?"
  type: multiple-choice
  options:
    - "Cyanobacteria evolved only 2.7 billion years ago"
    - "The presence of cyanobacterial biomarkers indicates that oxygenic photosynthesis existed by 2.7 Ga -- several hundred million years before the Great Oxidation Event -- suggesting oxygen production preceded its atmospheric accumulation, with sinks (reduced minerals, volcanic gases) consuming O2 until the balance tipped"
    - "The biomarkers were produced by non-biological processes"
    - "The rocks have been contaminated by modern organisms"
  answer: 1
  explanation: "2-alpha-methylhopanes are diagnostic of cyanobacteria, the only organisms that perform oxygenic photosynthesis. Their presence at 2.7 Ga indicates that O2 production had begun, but atmospheric O2 levels remained low until ~2.4 Ga (GOE) because oxygen sinks exceeded sources. This molecular fossil evidence predates the first unambiguous inorganic evidence for oxygenation, illustrating the power of biomarkers to detect biological innovation before its planetary-scale consequences."

- question: "All organic matter in sediments eventually converts to petroleum given sufficient burial depth and time."
  type: true-false
  answer: false
  explanation: "Petroleum generation requires organic matter of appropriate type and adequate thermal maturation. Type I kerogen (algal/lacustrine) generates oil; Type II (marine) generates oil and gas; Type III (terrestrial plant) generates mainly gas. But many organic-rich rocks never reach the thermal window for oil generation (60-160 C), remaining immature. Over-maturation destroys oil, leaving only methane or graphite. And organic matter preserved in oxidizing environments is mostly degraded before burial. Petroleum generation requires the right organic matter type, sufficient burial temperature, and appropriate timing."

- question: "Explain how the UK37' (alkenone unsaturation index) functions as a sea surface temperature proxy."
  type: short-answer
  answer: "Certain marine haptophyte algae (notably Emiliania huxleyi) synthesize long-chain alkenones (C37 methyl ketones) with varying numbers of double bonds. The ratio of di-unsaturated to tri-unsaturated alkenones (UK37') varies linearly with the growth temperature of the organism: colder waters produce more tri-unsaturated alkenones. Because alkenones are resistant to diagenesis and preserve their unsaturation pattern for millions of years, measuring UK37' in marine sediment cores provides a quantitative paleotemperature proxy calibrated against modern surface ocean temperatures. This is one of the most widely used organic geochemical proxies in paleoceanography."
  explanation: "Alkenones are molecular thermometers: the organism adjusts membrane lipid composition in response to temperature, and this adjustment is preserved in the sedimentary record."
```

## Explainer

Organic geochemistry bridges biology and geology, tracking the transformation of living matter into geological materials. The ~0.5% of photosynthetically fixed carbon that escapes remineralization and is buried in sediments drives two of the most important long-term geological processes: petroleum generation and atmospheric oxygen regulation.

Biomarkers are the most information-rich organic compounds because their molecular structures can be traced to specific biological sources. Sterols are produced exclusively by eukaryotes (their carbon skeletons -- steranes -- survive burial). Hopanoids are produced by bacteria. Specific compounds can be more diagnostic: dinosterol indicates dinoflagellates, oleanane indicates angiosperms, isorenieratane indicates green sulfur bacteria (requiring photic-zone euxinia). The presence or absence of these biomarkers in ancient rocks constrains the biological community and environmental conditions at the time of deposition.

Kerogen -- the insoluble organic fraction of sedimentary rocks -- is the most abundant form of organic carbon on Earth, vastly exceeding fossil fuels and living biomass combined. It is classified by its hydrogen/carbon and oxygen/carbon ratios (van Krevelen diagram) into types reflecting the biological source: Type I (high H/C, algal), Type II (intermediate, marine), Type III (low H/C, terrestrial plants). During burial and heating (catagenesis, 60-160 C), kerogen cracks to generate liquid hydrocarbons (oil). At higher temperatures (160-200+ C), oil is cracked to wet gas, then dry gas (methane). This oil window and gas window framework is the foundation of petroleum exploration geochemistry.

The connection between organic carbon burial and atmospheric O2 is fundamental. Photosynthesis produces O2 and organic carbon in a 1:1 stoichiometric ratio. If all organic carbon is remineralized (respired), the O2 is consumed and there is no net oxygen accumulation. Only organic carbon that escapes remineralization through burial produces a net gain of O2 to the atmosphere. The delta-13C record in marine carbonates tracks the fraction of carbon buried as organic matter (f-org), and secular trends in this record document the oxygenation history of Earth's atmosphere through the linked carbon-oxygen cycle.
