---
id: weathering-soil-chemistry
title: Weathering and Soil Chemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: aqueous-geochemistry
  type: hard
- id: mineral-stability-phase-diagrams
  type: soft
builds-toward:
- environmental-geochemistry
tags:
- weathering
- soil-chemistry
- chemical-weathering
- clay-minerals
- pedogenesis
stage: expert
status: validated
---

# Weathering and Soil Chemistry

## Core Idea
Chemical weathering is the dissolution and transformation of primary minerals (formed at high T-P) to secondary minerals (stable at surface conditions) through reactions with water, dissolved CO2, organic acids, and oxygen. Silicate weathering -- the dominant long-term process -- consumes atmospheric CO2 (e.g., CaSiO3 + CO2 -> CaCO3 + SiO2), acting as Earth's primary thermostat over million-year timescales. Weathering intensity depends on temperature, precipitation, biological activity, rock type, and topography. The products -- dissolved ions (Ca, Mg, Na, K, Si, HCO3-) and secondary clay minerals (kaolinite, smectite, gibbsite) -- determine soil composition, river chemistry, and ultimately the geochemical inputs to the ocean. Soil profiles develop through these processes, with distinct horizons reflecting progressive leaching and mineral transformation with depth.

## Questions

```yaml
- question: "The silicate weathering feedback is considered Earth's long-term thermostat. How does this feedback stabilize climate?"
  type: multiple-choice
  options:
    - "Silicate weathering produces greenhouse gases that warm the climate"
    - "Higher temperatures and more rainfall increase silicate weathering rates, which consume more CO2, reducing the greenhouse effect and cooling the planet; lower temperatures reduce weathering, allowing volcanic CO2 to accumulate and warm the planet -- a negative feedback that stabilizes climate over million-year timescales"
    - "Silicate weathering reflects sunlight back to space"
    - "The feedback only operates during ice ages"
  answer: 1
  explanation: "This is the Walker feedback: CO2 is continuously added to the atmosphere by volcanism and removed by silicate weathering. Because weathering rates increase with temperature (through kinetics) and precipitation (through water availability and runoff), any warming increases CO2 drawdown, eventually cooling the planet. Any cooling reduces weathering, allowing volcanic CO2 to build up and warm the planet. This negative feedback has maintained habitable surface temperatures for >4 Gyr despite a 30% increase in solar luminosity."

- question: "A tropical soil profile shows gibbsite (Al(OH)3) as the dominant secondary mineral, with virtually no primary minerals remaining. This indicates extreme weathering conditions."
  type: true-false
  answer: true
  explanation: "Gibbsite is the end-product of silicate weathering -- all silica, alkalis, and alkaline earths have been completely leached, leaving only the most insoluble component (aluminum hydroxide). This extreme weathering (lateritization) occurs under prolonged tropical conditions with high rainfall, warm temperatures, and good drainage. The weathering sequence from fresh rock is: feldspar -> smectite -> kaolinite -> gibbsite, with each step removing more silica and cations. Gibbsite dominance indicates that weathering has progressed to its maximum extent."

- question: "Explain why chemical weathering rates are highest in warm, wet tropical environments but the thickest soil profiles can also develop on stable, low-relief surfaces in these regions."
  type: short-answer
  answer: "Chemical reaction rates increase with temperature (Arrhenius relationship), and water is both a reactant and transport medium that removes dissolved products (preventing saturation that would slow reactions). Tropical conditions maximize both kinetic rates and water throughput. Thick soils develop on stable surfaces because: (1) high weathering rates transform bedrock to soil faster than erosion removes it, (2) low topographic relief reduces physical erosion, allowing residual soil to accumulate, and (3) biological activity (root penetration, organic acid production, bioturbation) accelerates weathering at depth. The combination of intense chemical weathering and minimal physical erosion produces deeply weathered profiles (laterites) tens of meters thick that represent millions of years of cumulative weathering."
  explanation: "Thick tropical soils require two conditions: high weathering rates (climate) and low erosion rates (geomorphology). Where both are satisfied, the weathering front advances into bedrock faster than the surface is lowered."
```

## Explainer

Weathering is the fundamental process connecting solid Earth geochemistry to surface geochemistry. Every ion in every river, every clay mineral in every soil, and every grain of sand on every beach is a product of weathering. At the planetary scale, silicate weathering regulates atmospheric CO2 and has maintained habitable conditions for most of Earth's history.

The thermodynamic driving force for weathering is the instability of high-temperature minerals at surface conditions. Olivine, pyroxene, feldspar, and mica crystallized at 700-1200 C and pressures of kilobars. At 15 C and 1 atm, they are thermodynamically unstable with respect to clay minerals, oxides, and dissolved ions. The Goldich dissolution series (olivine weathers fastest, quartz slowest) mirrors the reverse of Bowen's reaction series -- minerals that crystallize at the highest temperatures are least stable at the surface. This reflects the greater structural adjustment required for high-T minerals to reach equilibrium with surface conditions.

Carbonic acid weathering dominates globally. Soil CO2 concentrations (10-100x atmospheric) from root respiration and microbial decomposition dissolve in soil water to form H2CO3. This attacks silicate minerals: 2KAlSi3O8 + 2H2CO3 + 9H2O -> Al2Si2O5(OH)4 + 4H4SiO4 + 2K+ + 2HCO3-. The products -- kaolinite (secondary clay), dissolved silica, potassium, and bicarbonate -- are transported by rivers to the ocean. The HCO3- eventually precipitates as marine carbonate (CaCO3), completing the long-term carbon cycle. This reaction consumes atmospheric CO2 only when silicate (not carbonate) minerals weather, because carbonate weathering is reversed by carbonate precipitation in the ocean.

Soil chemistry reflects the progressive stages of weathering with depth. A typical soil profile has organic-rich surface horizons (O, A), a leached eluvial horizon (E), a clay/iron-enriched illuvial horizon (B), and weathered parent material (C) grading into bedrock (R). The clay mineralogy changes systematically with weathering intensity: 2:1 clays (smectite, vermiculite) in moderately weathered soils; 1:1 clays (kaolinite) in more intensely weathered soils; and aluminum and iron oxides/hydroxides (gibbsite, goethite) in the most weathered tropical soils. This sequence records progressive loss of silica and base cations, driven by the thermodynamic imperative to reach surface equilibrium.
