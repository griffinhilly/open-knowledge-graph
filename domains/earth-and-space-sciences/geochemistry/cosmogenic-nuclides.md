---
id: cosmogenic-nuclides
title: Cosmogenic Nuclides
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: soft
builds-toward:
- weathering-soil-chemistry
tags:
- cosmogenic-nuclides
- exposure-dating
- Be-10
- erosion-rates
- surface-processes
stage: expert
status: validated
---

# Cosmogenic Nuclides

## Core Idea
Cosmogenic nuclides (10Be, 26Al, 36Cl, 3He, 21Ne) are produced in surface rocks and the atmosphere by cosmic ray bombardment. In rocks, cosmic ray neutrons and muons interact with target atoms (O, Si, Ca, K, Fe) to produce these rare isotopes at known rates that decrease exponentially with depth below the surface. The concentration of a cosmogenic nuclide in a surface sample reflects the duration of exposure to cosmic rays -- providing exposure ages for glacial moraines, lava flows, fault scarps, and archaeological surfaces. In a steady-state eroding landscape, cosmogenic concentrations reflect erosion rates. The paired 26Al/10Be ratio exploits different half-lives to detect periods of burial and shielding. This method has revolutionized geomorphology by providing a direct means of quantifying surface exposure time and erosion rates over 10^3 to 10^6 year timescales.

## Questions

```yaml
- question: "A glacial moraine boulder has a 10Be concentration indicating an exposure age of 18,000 years. What geological event does this date?"
  type: multiple-choice
  options:
    - "The age of the bedrock from which the boulder was derived"
    - "The time when the glacier retreated and exposed the boulder to cosmic rays at the surface, recording the timing of deglaciation"
    - "The time when the boulder was first deposited by a river"
    - "The age of the cosmic rays that produced the 10Be"
  answer: 1
  explanation: "While buried under ice, the boulder was shielded from cosmic rays and accumulated negligible 10Be. When the glacier retreated and deposited the moraine, the boulder was exposed to cosmic radiation and 10Be began accumulating. The 18,000-year age dates the exposure event -- glacier retreat. This assumes the boulder had negligible pre-exposure (inheritance) and has not been eroded, buried by sediment, or toppled since deposition."

- question: "Cosmogenic nuclide production rates are uniform across Earth's surface regardless of latitude or altitude."
  type: true-false
  answer: false
  explanation: "Production rates vary significantly with latitude and altitude. Earth's magnetic field deflects low-energy cosmic rays, reducing production at low latitudes compared to high latitudes (where field lines are nearly vertical and provide less shielding). Production increases exponentially with altitude because there is less atmosphere to attenuate cosmic rays -- rates at 3000 m elevation are roughly 3-4 times higher than at sea level. Accurate age/erosion rate calculations require site-specific production rates scaled for latitude, altitude, and topographic shielding."

- question: "Explain how the 26Al/10Be ratio in a quartz sample can reveal a history of burial."
  type: short-answer
  answer: "Both 26Al and 10Be are produced in quartz by cosmic rays with a known production ratio of ~6.75. During surface exposure, both accumulate and their ratio remains near this production ratio. If the sample is then buried (by sediment, ice, or landslide), cosmic ray production ceases and both nuclides decay radioactively. Because 26Al has a shorter half-life (0.71 Myr) than 10Be (1.39 Myr), the 26Al/10Be ratio decreases during burial. A ratio significantly below the production ratio indicates a period of shielding from cosmic rays between periods of surface exposure, and the magnitude of the depression constrains the burial duration."
  explanation: "The differential decay clock works because both nuclides start at a known ratio, then diverge during burial when production stops but decay continues at different rates."
```

## Explainer

Cosmogenic nuclide geochemistry has transformed surface process science by providing a tool that directly measures the quantities that geomorphologists care most about: how long a surface has been exposed and how fast it is eroding. Before cosmogenic nuclides, these fundamental parameters could only be estimated indirectly.

The production mechanism is nuclear spallation: high-energy cosmic ray particles (primarily neutrons and muons) collide with target atoms in rock minerals, breaking off nuclear fragments. In quartz (SiO2), neutron spallation of oxygen and silicon produces 10Be and 26Al. The production rate decreases exponentially with depth below the surface, with an e-folding length of ~60 cm in rock (~160 g/cm2 attenuation length). This means that the top few meters of rock contain interpretable cosmogenic nuclide concentrations, while deeply buried rock has negligible concentrations.

For exposure dating, the interpretation is straightforward if erosion is negligible: the nuclide concentration divided by the production rate gives the exposure time. This works for stable, recently exposed surfaces like glacial polish, lava flows on flat terrain, and large boulders. For eroding surfaces, a steady-state model balances production against erosion-driven removal, and the concentration gives the erosion rate (typically mm/kyr to m/Myr for bedrock). Catchment-averaged erosion rates are obtained by analyzing quartz from river sediment, which integrates the erosion signal from the entire upstream basin.

The burial dating application using 26Al/10Be pairs has opened unique windows into sediment routing and landscape evolution. Cave sediments, deeply buried river terraces, and sediment cores beneath ice sheets have been dated using this technique, revealing when landscapes were buried and exhumed. The method fills a critical gap between the short timescale of radiocarbon (~50,000 years) and the long timescale of standard radiometric methods (~1 Myr and older), providing chronometric control over exactly the timescales of glacial-interglacial cycles, river terrace formation, and landscape response to climate change.
