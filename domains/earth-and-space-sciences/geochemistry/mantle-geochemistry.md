---
id: mantle-geochemistry
title: Mantle Geochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: trace-element-geochemistry
  type: hard
- id: sm-nd-system
  type: hard
- id: rb-sr-system
  type: soft
- id: mineral-stability-phase-diagrams
  type: soft
- id: partition-coefficients
  type: hard
- id: ree-patterns-geochemistry
  type: soft
builds-toward:
- crustal-evolution-geochemistry
- cosmochemistry
tags:
- mantle
- MORB
- OIB
- mantle-reservoirs
- isotope-geochemistry
stage: expert
status: validated
---

# Mantle Geochemistry

## Core Idea
The mantle is chemically heterogeneous, containing distinct geochemical reservoirs created by billions of years of differentiation, subduction recycling, and incomplete mixing. Mid-ocean ridge basalts (MORB) sample the shallow depleted mantle (DMM) -- residual after continental crust extraction -- characterized by low incompatible-element concentrations and depleted isotopic signatures (high epsilon-Nd, low 87Sr/86Sr). Ocean island basalts (OIB) sample deeper, more enriched mantle sources with diverse isotopic signatures defining several end-member components: HIMU (high-mu, recycled oceanic crust with high U/Pb), EM1 and EM2 (enriched mantle with recycled sediment or subcontinental lithosphere), and FOZO/C (a common deep mantle component). The isotopic variability of mantle-derived magmas is the primary evidence for large-scale chemical heterogeneity and long-term recycling within Earth's mantle.

## Questions

```yaml
- question: "Hawaiian basalts have higher 206Pb/204Pb ratios than mid-ocean ridge basalts. What does this indicate about the Hawaiian mantle source?"
  type: multiple-choice
  options:
    - "Hawaiian basalts have been contaminated by seawater Pb"
    - "The Hawaiian source has evolved with a higher time-integrated U/Pb ratio than the depleted MORB mantle, consistent with a contribution from recycled oceanic crust that concentrated U relative to Pb during seafloor alteration and subduction"
    - "Pb decays faster beneath Hawaii due to higher mantle temperatures"
    - "Hawaii is older than mid-ocean ridges"
  answer: 1
  explanation: "Higher 206Pb/204Pb requires higher time-integrated 238U/204Pb (mu). Recycled oceanic crust acquires elevated U/Pb during seafloor hydrothermal alteration (U is added from seawater; Pb is removed by sulfide precipitation). After subduction and long residence in the mantle, this elevated U/Pb evolves to high 206Pb/204Pb, which is then sampled by the Hawaiian hotspot. This is the basis of the HIMU mantle component."

- question: "The depleted mantle is complementary to the continental crust, meaning their isotopic and trace element compositions are mirror images."
  type: true-false
  answer: true
  explanation: "Continental crust was extracted from the mantle, preferentially removing incompatible elements (Rb, Ba, Th, U, LREE). The residual depleted mantle is the complementary reservoir with low incompatible-element concentrations, high Sm/Nd (evolving to high epsilon-Nd), and low Rb/Sr (evolving to low 87Sr/86Sr). Mass balance requires that the depleted mantle plus continental crust approximate the bulk silicate Earth (primitive mantle) composition. This complementary relationship is the cornerstone of crust-mantle geochemistry."

- question: "Explain why MORB has remarkably uniform isotopic composition globally compared to the extreme isotopic diversity of OIB."
  type: short-answer
  answer: "MORB is produced by large-degree melting (~10-20%) beneath spreading ridges, which effectively averages out small-scale heterogeneities in the shallow, convectively stirred upper mantle. The depleted MORB mantle (DMM) is relatively well-mixed by plate-scale convection. OIB is produced by smaller-degree melting of plume sources that may tap compositionally distinct domains in the deeper mantle -- recycled oceanic crust, subducted sediment, recycled lithosphere -- that have been isolated from the convecting upper mantle for billions of years. These deep sources preserve their isotopic diversity because they reside in less vigorously mixed regions of the mantle."
  explanation: "Homogeneity reflects mixing efficiency: the shallow convecting mantle is well-mixed (MORB uniformity), while the deep mantle preserves ancient compositional heterogeneities (OIB diversity)."
```

## Explainer

The geochemistry of mantle-derived rocks provides the primary window into Earth's deep interior. Since we cannot sample the mantle directly (with rare exceptions like xenoliths), we reconstruct its composition from the magmas it produces -- and the trace element and isotopic signatures of those magmas encode the mantle's compositional structure.

The depleted MORB mantle (DMM) is the best-characterized reservoir because mid-ocean ridges are the most voluminous volcanic system on Earth (~20 km3/year). DMM is depleted in incompatible elements by a factor of 2-10 relative to primitive mantle estimates, with epsilon-Nd of +8 to +12 and 87Sr/86Sr of 0.7022-0.7035. This depletion reflects the cumulative extraction of continental crust over 4+ billion years. The remarkable chemical homogeneity of N-MORB globally (within a factor of 2 for most incompatible elements) indicates efficient convective mixing of the upper mantle on ~100 Myr timescales.

Ocean island basalts reveal the mantle's hidden complexity. Isotopic plots (87Sr/86Sr vs epsilon-Nd, 206Pb/204Pb vs 207Pb/204Pb) show that OIB define arrays extending from DMM toward several enriched end-member compositions. HIMU (St. Helena, Mangaia) has extreme radiogenic Pb from recycled oceanic crust with high U/Pb. EM1 (Pitcairn, Walvis Ridge) has low epsilon-Nd and moderate 87Sr/86Sr, possibly from recycled lower continental crust or pelagic sediment. EM2 (Samoa, Society Islands) has the highest 87Sr/86Sr (>0.707), attributed to recycled terrigenous sediment. These end-members represent distinct lithologies subducted into the mantle at various times and later sampled by upwelling plumes.

The convergence of isotopic, trace element, and noble gas evidence points to a mantle that is layered in its heterogeneity if not in its convection. The upper mantle is depleted and relatively homogeneous. The lower mantle contains ancient, less-depleted material (evidenced by primitive noble gas ratios in some OIB) plus accumulated subducted material in various stages of mixing and thermal equilibration. Large Low Shear Velocity Provinces (LLSVPs) at the base of the mantle may be compositionally distinct thermochemical piles that anchor deep mantle heterogeneity. Understanding this chemical architecture is essential for models of mantle convection, plate recycling, and the long-term evolution of Earth's heat budget.
