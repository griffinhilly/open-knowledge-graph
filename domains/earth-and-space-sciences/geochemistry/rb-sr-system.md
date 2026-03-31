---
id: rb-sr-system
title: Rb-Sr Isotope System
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: soft
- id: trace-element-geochemistry
  type: soft
builds-toward:
- crustal-evolution-geochemistry
tags:
- Rb-Sr
- radiogenic-isotopes
- geochronology
- isochron
stage: expert
status: validated
---

# Rb-Sr Isotope System

## Core Idea
The Rb-Sr system is based on the beta decay of 87Rb to 87Sr (half-life 48.8 Gyr). Because Rb (an alkali metal) and Sr (an alkaline earth) have different geochemical behaviors, igneous processes fractionate Rb/Sr ratios: Rb is incompatible (concentrates in melts and K-bearing minerals like micas and K-feldspar), while Sr is compatible in plagioclase and apatite. The isochron method dates rocks by plotting 87Sr/86Sr versus 87Rb/86Sr for co-genetic samples: the slope gives the age and the y-intercept gives the initial 87Sr/86Sr ratio. Initial Sr ratios are themselves powerful petrogenetic tracers -- mantle-derived rocks have low initial 87Sr/86Sr (~0.703-0.704) while rocks incorporating ancient continental crust have higher values (>0.710), reflecting long-term Rb/Sr fractionation.

## Questions

```yaml
- question: "Five mineral separates from a granite yield a well-defined Rb-Sr isochron with an age of 350 Ma and an initial 87Sr/86Sr of 0.712. What do these results indicate about the granite's source?"
  type: multiple-choice
  options:
    - "The granite crystallized directly from mantle-derived basaltic magma"
    - "The high initial 87Sr/86Sr (>>0.704) indicates significant incorporation of old continental crustal material with elevated Rb/Sr ratios that had evolved high 87Sr/86Sr over time; the granite likely formed by partial melting of or extensive assimilation of continental crust"
    - "The granite formed at a mid-ocean ridge"
    - "The high initial ratio indicates contamination by seawater"
  answer: 1
  explanation: "Depleted mantle has 87Sr/86Sr of ~0.7025-0.704. An initial ratio of 0.712 requires a source that accumulated radiogenic 87Sr from 87Rb decay over a long period -- characteristic of old continental crust. This granite either formed by partial melting of continental crust or by extensive assimilation of crustal material by a mantle-derived magma."

- question: "An Rb-Sr isochron requires all samples to have had the same initial 87Sr/86Sr ratio when they formed."
  type: true-false
  answer: true
  explanation: "The isochron method assumes all samples (minerals or whole rocks) were in isotopic equilibrium at time zero, sharing a common initial 87Sr/86Sr. After formation, each sample evolves independently along a trajectory determined by its Rb/Sr ratio. Samples with higher Rb/Sr develop higher 87Sr/86Sr over time, producing the sloped isochron. If initial ratios were not uniform (e.g., mixing of isotopically distinct magmas without homogenization), the samples will scatter rather than define a line, and the apparent age will be meaningless."

- question: "Explain why the Rb-Sr system is readily reset by metamorphism while the Sm-Nd system is more resistant."
  type: short-answer
  answer: "Rb and Sr are relatively mobile during metamorphism because they substitute into minerals (micas, feldspars) that readily recrystallize at metamorphic conditions, and because both elements are moderately soluble in metamorphic fluids. Metamorphic recrystallization and fluid flow can re-homogenize Sr isotopes among minerals, resetting the isochron clock. Sm and Nd are rare earth elements with very similar geochemical behavior, high ionic potential, and low fluid mobility. They reside in refractory accessory minerals (garnet, monazite) that are more resistant to metamorphic resetting. This contrast makes Rb-Sr useful for dating the last metamorphic or thermal event, while Sm-Nd more often preserves the original igneous age."
  explanation: "The difference is fundamentally about element mobility: alkali/alkaline earth elements are mobile in crustal fluids; rare earth elements are not."
```

## Explainer

The Rb-Sr system was one of the first radiometric dating methods applied to rocks and remains important for both geochronology and petrogenetic tracing. Its power derives from the strong geochemical fractionation of Rb from Sr during igneous and metamorphic processes, which creates the range of parent/daughter ratios needed for isochron dating.

The isochron equation is: (87Sr/86Sr)_measured = (87Sr/86Sr)_initial + (87Rb/86Sr) * (e^(lambda*t) - 1). In a plot of 87Sr/86Sr versus 87Rb/86Sr, co-genetic samples that shared the same initial ratio define a line (the isochron) whose slope is (e^(lambda*t) - 1). With lambda known (1.42 x 10^-11 yr^-1), the age t is calculated from the slope. The y-intercept gives the initial 87Sr/86Sr ratio, which is a petrogenetic fingerprint of the source region.

Mineral isochrons use different minerals from a single rock (biotite has high Rb/Sr, plagioclase has low Rb/Sr, whole-rock is intermediate). Whole-rock isochrons use co-genetic rocks (from the same magmatic suite) with varying bulk Rb/Sr. Mineral isochrons are more easily reset by thermal events (because inter-mineral diffusion distances are short) and thus date cooling or metamorphism. Whole-rock isochrons are more robust because resetting requires homogenization at the whole-rock scale.

As a petrogenetic tracer, 87Sr/86Sr initial ratios discriminate mantle versus crustal sources. Mid-ocean ridge basalts have 87Sr/86Sr of 0.7025, reflecting the depleted mantle. Ocean island basalts range from 0.703 to 0.706, reflecting various mantle source enrichments. Continental crust, with higher Rb/Sr ratios and billions of years of 87Rb decay, has evolved to 87Sr/86Sr of 0.710-0.740. Granites, andesites, and other crustally influenced magmas plot between these endmembers, and the 87Sr/86Sr ratio quantifies the extent of crustal involvement in their petrogenesis. Paired with Nd isotopes, Sr isotopes provide the definitive discrimination between mantle and crustal components.
