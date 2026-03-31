---
id: sm-nd-system
title: Sm-Nd Isotope System
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: rb-sr-system
  type: soft
- id: trace-element-geochemistry
  type: hard
builds-toward:
- mantle-geochemistry
- crustal-evolution-geochemistry
tags:
- Sm-Nd
- radiogenic-isotopes
- epsilon-Nd
- model-ages
stage: expert
status: validated
---

# Sm-Nd Isotope System

## Core Idea
The Sm-Nd system is based on the alpha decay of 147Sm to 143Nd (half-life 106 Gyr). Because both Sm and Nd are light rare earth elements with very similar geochemical behavior, Sm/Nd fractionation during geological processes is small but systematic: partial melting preferentially concentrates the lighter Nd over the slightly heavier Sm in the melt, giving the crust lower Sm/Nd (and therefore lower time-integrated 143Nd/144Nd) than the residual mantle. Epsilon-Nd notation expresses 143Nd/144Nd as deviations from a chondritic reference (CHUR): positive epsilon-Nd indicates a depleted-mantle source; negative epsilon-Nd indicates enriched or crustal source. The Sm-Nd system is resistant to metamorphic resetting and provides robust constraints on crust-mantle differentiation, mantle source heterogeneity, and crustal residence ages.

## Questions

```yaml
- question: "A mid-ocean ridge basalt has epsilon-Nd of +10, while a continental granite has epsilon-Nd of -15. What fundamental process creates this difference?"
  type: multiple-choice
  options:
    - "Radioactive decay rates differ between oceanic and continental settings"
    - "Extraction of continental crust from the mantle fractionated Sm/Nd: the crust acquired low Sm/Nd, evolving to low 143Nd/144Nd (negative epsilon-Nd) over time, while the residual depleted mantle retained high Sm/Nd, evolving to high 143Nd/144Nd (positive epsilon-Nd)"
    - "Seawater contamination of oceanic basalts increases their epsilon-Nd"
    - "Continental granites form at higher temperatures, shifting epsilon-Nd"
  answer: 1
  explanation: "Partial melting of the mantle to form continental crust concentrates Nd (light REE) preferentially over Sm in the melt. The crust accumulates lower Sm/Nd over time, so its 143Nd/144Nd grows more slowly than chondrite (negative epsilon-Nd). The complementary depleted mantle retains elevated Sm/Nd, growing 143Nd/144Nd faster than chondrite (positive epsilon-Nd). After billions of years, this produces the observed ~25 epsilon units difference between depleted mantle and old continental crust."

- question: "A Sm-Nd depleted mantle model age (T-DM) of 2.8 Ga for a granite means the granite crystallized 2.8 billion years ago."
  type: true-false
  answer: false
  explanation: "A T-DM age estimates when the granite's source material was extracted from the depleted mantle, not when the granite itself crystallized. If the granite formed at 350 Ma by melting 2.8 Ga crust, the T-DM would be 2.8 Ga while the crystallization age (from U-Pb zircon or Rb-Sr) would be 350 Ma. T-DM provides a crustal residence age -- how long the source material has been part of the continental crust."

- question: "Explain why the Sm-Nd system is more robust against metamorphic resetting than the Rb-Sr system."
  type: short-answer
  answer: "Sm and Nd are both rare earth elements (REE) with similar ionic radii, high charge, and very similar geochemical behavior. They are strongly bonded in refractory minerals (garnet, zircon, monazite) and have very low mobility in metamorphic fluids. Because metamorphic resetting requires redistribution of parent and daughter isotopes, and Sm-Nd redistribution requires either very high temperatures or complete recrystallization of host minerals, the system is resistant to all but the highest-grade metamorphism. Rb and Sr, being alkali/alkaline-earth metals in fluid-mobile phases (micas, feldspars), are much more easily redistributed during metamorphism and fluid flow."
  explanation: "Robustness correlates inversely with element mobility: the similar, refractory REE Sm and Nd resist mobilization while the dissimilar, fluid-mobile Rb and Sr do not."
```

## Explainer

The Sm-Nd system is the definitive tracer of crust-mantle differentiation because it directly records the fractionation between two elements that are separated only during major silicate melting events. Unlike Rb-Sr (where Rb and Sr have very different chemistry and are easily disturbed), Sm and Nd behave almost identically in all processes except partial melting of silicates.

The epsilon-Nd notation makes the system intuitive. CHUR (Chondritic Uniform Reservoir) represents the undifferentiated bulk Earth composition. Epsilon-Nd = [(143Nd/144Nd-sample)/(143Nd/144Nd-CHUR) - 1] x 10^4. Positive values mean the source has evolved with higher Sm/Nd than CHUR (depleted mantle, from which crust has been extracted). Negative values mean the source has evolved with lower Sm/Nd (continental crust or enriched mantle). The depleted mantle today has epsilon-Nd of approximately +8 to +12; old continental crust ranges from -10 to -40.

Epsilon-Nd vs 87Sr/86Sr plots (mantle arrays) are one of the most powerful discrimination tools in igneous petrology. Depleted mantle plots at high epsilon-Nd, low 87Sr/86Sr; continental crust plots at low epsilon-Nd, high 87Sr/86Sr. Mantle sources enriched by subducted sediment, metasomatism, or recycled oceanic crust plot in characteristic positions on this diagram, enabling identification of mantle source components in ocean island basalts, arc volcanics, and continental magmas.

Nd model ages (T-DM and T-CHUR) calculate when a sample's Nd isotopic composition intersects the depleted mantle or chondritic evolution curves, respectively. These are interpreted as crustal extraction ages -- the time when new continental crust was generated from the mantle. Global compilations of Nd model ages reveal episodic crustal growth, with major peaks at ~2.7, 1.9, and 1.1 Ga corresponding to supercontinent assembly events. This makes the Sm-Nd system a fundamental tool for understanding the growth and evolution of continental crust through Earth history.
