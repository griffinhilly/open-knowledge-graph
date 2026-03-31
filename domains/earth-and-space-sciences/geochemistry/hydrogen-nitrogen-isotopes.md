---
id: hydrogen-nitrogen-isotopes
title: Hydrogen and Nitrogen Isotopes
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: stable-isotope-fractionation
  type: hard
builds-toward:
- isotope-hydrology
- biogeochemistry
tags:
- hydrogen-isotopes
- nitrogen-isotopes
- delta-D
- delta-15N
stage: expert
status: validated
---

# Hydrogen and Nitrogen Isotopes

## Core Idea
Hydrogen (H, D with mass ratio 2:1) and nitrogen (14N, 15N with mass ratio 15:14) isotopes are powerful tracers of water sources and biological processes respectively. Hydrogen isotopes (delta-D, measured relative to VSMOW) co-vary with delta-18O in precipitation along the Global Meteoric Water Line (delta-D = 8 * delta-18O + 10), making them complementary hydrological tracers. The large mass difference (100%) produces the largest fractionation effects of any stable isotope system. Nitrogen isotopes (delta-15N, relative to atmospheric N2) trace biological nitrogen cycling: nitrogen fixation, nitrification, denitrification, and trophic-level enrichment each produce diagnostic fractionation patterns. Together, delta-D and delta-15N address questions from paleoclimate reconstruction to pollution source tracking.

## Questions

```yaml
- question: "A water sample plots below the Global Meteoric Water Line (GMWL) on a delta-D vs delta-18O diagram, with higher delta-18O than expected for its delta-D. What process most likely caused this?"
  type: multiple-choice
  options:
    - "Radioactive decay of deuterium"
    - "Evaporation from an open water body, which kinetically fractionates 18O more than D relative to equilibrium, producing an evaporation line with slope 3-5 (below the GMWL slope of 8)"
    - "Mixing with seawater"
    - "Geothermal heating of groundwater"
  answer: 1
  explanation: "During evaporation under non-equilibrium conditions, the kinetic fractionation factor for 18O/16O is larger relative to its equilibrium value than for D/H, because the diffusivity difference is proportionately larger for the lighter oxygen isotopes. This causes evaporated water to plot along a line with slope 3-5 rather than the GMWL slope of 8. Samples below the GMWL have experienced evaporative enrichment -- common in arid-region lakes, irrigation return flow, and soil water."

- question: "Delta-15N values increase by approximately 3-4 per mil with each trophic level in food webs."
  type: true-false
  answer: true
  explanation: "Metabolic processes preferentially excrete the lighter 14N isotope (in urine, feces, ammonia), leaving the organism's tissues enriched in 15N relative to its diet. This ~3.4 per mil per trophic level enrichment is remarkably consistent across ecosystems and is used to determine trophic position in ecological studies. A top predator (trophic level 4) would be enriched by ~10 per mil over the baseline primary producers."

- question: "Explain how nitrogen isotopes distinguish between agricultural fertilizer runoff and sewage as sources of nitrate contamination in a river."
  type: short-answer
  answer: "Synthetic fertilizer nitrogen is produced by the Haber-Bosch process from atmospheric N2, so it has delta-15N near 0 per mil (similar to air). Animal waste and sewage have delta-15N of +10 to +20 per mil because biological processing (volatilization of 14N-enriched ammonia) leaves the residual nitrogen enriched in 15N. Nitrate in the river with delta-15N near 0 indicates fertilizer origin; values above +10 per mil indicate sewage or manure. Intermediate values suggest mixing. Paired delta-15N and delta-18O of nitrate can further discriminate sources, since synthetic fertilizer nitrate has distinctive delta-18O values."
  explanation: "The source materials have fundamentally different isotopic compositions due to their different formation pathways, making delta-15N a direct tracer of contamination origin."
```

## Explainer

Hydrogen and nitrogen isotope systems each occupy distinct niches in geochemistry. Hydrogen isotopes are primarily hydrological tracers, while nitrogen isotopes are primarily biological tracers. Together with oxygen and carbon isotopes, they form the core light stable isotope toolkit.

The hydrogen isotope system has the largest relative mass difference of any stable pair (D/H, mass ratio 2.0). This produces enormous fractionation effects: delta-D of precipitation ranges from ~0 per mil in the tropics to -400 per mil in central Antarctica. The Global Meteoric Water Line (GMWL), defined as delta-D = 8 * delta-18O + 10, reflects the equilibrium fractionation of both isotopes during condensation. The slope of 8 arises from the ratio of equilibrium fractionation factors for D/H and 18O/16O during condensation. Deviations from this line diagnose secondary processes: evaporation (slope <8), kinetic effects during snow formation (deuterium excess > 10), and water-rock interaction at high temperature (exchange shifts delta-18O but not delta-D in rocks with little hydrogen).

Nitrogen isotopes trace the biogeochemical nitrogen cycle -- one of the most complex and environmentally important element cycles. Atmospheric N2 is the reference standard (delta-15N = 0 per mil by definition). Biological nitrogen fixation produces organic N with delta-15N near 0. Nitrification (NH4+ to NO3-) and denitrification (NO3- to N2) both strongly fractionate nitrogen, with the residual substrate becoming enriched in 15N. In marine systems, water column denitrification in oxygen minimum zones produces NO3- enriched in 15N, which is propagated through the food web and recorded in sedimentary organic nitrogen -- providing a proxy for past ocean oxygenation.

Applied uses span environmental forensics (pollution source identification), paleoecology (trophic structure reconstruction from bone collagen delta-15N), paleoclimate (delta-D in ice cores and leaf waxes as temperature and moisture source proxies), and hydrology (using delta-D and delta-18O to identify groundwater recharge sources and mixing). The increasing precision of compound-specific isotope analysis -- measuring delta-D and delta-15N on individual organic molecules -- is extending these tools to ever more specific process tracers.
