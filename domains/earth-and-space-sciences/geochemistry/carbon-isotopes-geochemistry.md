---
id: carbon-isotopes-geochemistry
title: Carbon Isotopes in Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: stable-isotope-fractionation
  type: hard
builds-toward:
- organic-geochemistry
- biogeochemistry
- sedimentary-geochemistry
tags:
- carbon-isotopes
- delta-13C
- carbon-cycle
- organic-carbon
stage: expert
status: validated
---

# Carbon Isotopes in Geochemistry

## Core Idea
Carbon has two stable isotopes (12C, 13C) with delta-13C measured relative to VPDB. The carbon cycle creates a fundamental isotopic dichotomy: inorganic carbon (atmosphere, ocean DIC, carbonates) clusters around delta-13C = 0 +/- 5 per mil, while organic carbon (biologically fixed) clusters around -25 +/- 10 per mil due to kinetic fractionation during photosynthesis. This ~25 per mil offset between the organic and inorganic carbon reservoirs is maintained by continuous biological carbon fixation and is one of the most diagnostic isotopic signals on Earth. Perturbations to the global carbon cycle (mass extinctions, volcanic degassing, methane release, organic carbon burial) shift the delta-13C of ocean DIC, recorded in marine carbonates as carbon isotope excursions that are among the most important chemostratigraphic markers in the geological record.

## Questions

```yaml
- question: "A negative carbon isotope excursion (CIE) of -5 per mil in marine carbonates at the Paleocene-Eocene boundary (PETM, ~56 Ma) is interpreted as rapid release of isotopically light carbon. Which source is most consistent with this signal?"
  type: multiple-choice
  options:
    - "Enhanced weathering of silicate rocks"
    - "Massive release of methane from gas hydrates (delta-13C ~ -60 per mil) or thermogenic methane/CO2 from volcanic intrusion into organic-rich sediments (delta-13C ~ -30 to -50 per mil), both of which would shift ocean DIC toward more negative values"
    - "Increased productivity by marine phytoplankton"
    - "Release of 13C-enriched volcanic CO2"
  answer: 1
  explanation: "A rapid negative CIE requires addition of large quantities of 13C-depleted carbon to the ocean-atmosphere system. Methane hydrate dissociation (delta-13C ~ -60 per mil) and thermogenic carbon release are both very negative. Mantle-derived volcanic CO2 (delta-13C ~ -5 per mil) is similar to ocean DIC and cannot drive a significant negative excursion. The mass balance requires enough isotopically light carbon to shift the entire ocean-atmosphere reservoir."

- question: "All photosynthetic organisms produce organic matter with the same carbon isotopic composition of approximately -25 per mil."
  type: true-false
  answer: false
  explanation: "The delta-13C of organic matter depends on the photosynthetic pathway. C3 plants (most trees, rice, wheat) produce organic matter at -24 to -30 per mil. C4 plants (corn, sugarcane, tropical grasses) fractionate less, producing values of -10 to -14 per mil due to pre-concentration of CO2 by PEP carboxylase. Marine phytoplankton range from -18 to -28 per mil depending on CO2 availability and growth rate. Methanogens produce extremely 13C-depleted methane (-50 to -110 per mil). These differences enable source identification in sedimentary organic matter, food web studies, and paleodiet reconstruction."

- question: "Explain why a positive delta-13C excursion in marine carbonates is interpreted as enhanced organic carbon burial."
  type: short-answer
  answer: "The ocean's dissolved inorganic carbon (DIC) pool has a steady-state delta-13C maintained by the balance between carbon inputs (volcanic/weathering CO2 at ~-5 per mil) and outputs (carbonate burial at ~0 per mil, organic carbon burial at ~-25 per mil). When organic carbon burial increases, more 12C is preferentially removed from the ocean, leaving the remaining DIC pool enriched in 13C. Marine carbonates precipitating from this enriched DIC record higher delta-13C values. The magnitude of the excursion reflects the fraction of total carbon burial that is organic -- a fundamental parameter in Earth's carbon cycle and atmospheric O2 regulation."
  explanation: "Positive delta-13C excursions record periods when the fraction of carbon buried as organic matter (f-org) increased, drawing down 12C and leaving the ocean isotopically heavier."
```

## Explainer

Carbon isotopes trace the most fundamental biogeochemical cycle on Earth -- the cycle that regulates atmospheric CO2, produces atmospheric O2 (through organic carbon burial), and sustains all life. The ~25 per mil offset between organic and inorganic carbon, maintained by photosynthetic fractionation, is the isotopic expression of the biological carbon pump.

The fractionation during photosynthesis is primarily kinetic. The enzyme RuBisCO (ribulose-1,5-bisphosphate carboxylase/oxygenase), which fixes CO2 in the Calvin cycle, discriminates against 13CO2, producing organic matter depleted in 13C by 20-30 per mil relative to the CO2 substrate. C4 plants partially bypass this by first fixing carbon through PEP carboxylase (which discriminates less), then feeding the concentrated CO2 to RuBisCO -- resulting in less overall fractionation. These plant-specific signatures are preserved in soil organic matter, tooth enamel, and sediments, enabling reconstruction of past vegetation types and dietary sources.

In the marine realm, the delta-13C of dissolved inorganic carbon (DIC) varies with depth due to the biological pump. Surface waters are enriched in 13C (high delta-13C) because phytoplankton preferentially remove 12C during photosynthesis. Deep waters are depleted (low delta-13C) because remineralization of sinking organic matter adds 12C-rich carbon back to the DIC pool. This vertical gradient (~1-2 per mil in the modern ocean) is recorded by foraminifera at different depths, providing a proxy for deep water circulation and biological productivity in the past.

Carbon isotope excursions in the stratigraphic record mark major perturbations to the global carbon cycle. The late Neoproterozoic Shuram excursion (delta-13C to -12 per mil) may record massive oxidation of a dissolved organic carbon pool. The end-Permian negative CIE records volcanic carbon injection. Oceanic Anoxic Events in the Cretaceous show positive CIEs from enhanced organic carbon burial. These events, recognized globally through chemostratigraphy, demonstrate how carbon isotopes integrate biological, tectonic, and climatic processes into a single measurable signal.
