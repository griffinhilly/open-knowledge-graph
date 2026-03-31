---
id: cosmochemistry
title: Cosmochemistry
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: hard
- id: stable-isotope-fractionation
  type: soft
- id: u-pb-geochronology
  type: soft
builds-toward: []
tags:
- cosmochemistry
- meteorites
- solar-nebula
- nucleosynthesis
- planetary-formation
stage: expert
status: validated
---

# Cosmochemistry

## Core Idea
Cosmochemistry studies the chemical composition of extraterrestrial materials -- meteorites, lunar samples, interplanetary dust, comets, and presolar grains -- to understand the origin and evolution of the solar system. Chondritic meteorites (especially CI chondrites) preserve the bulk composition of the solar nebula for non-volatile elements and serve as the reference standard for planetary compositions. Isotopic anomalies in presolar grains record nucleosynthetic processes in individual stars that contributed material to the solar nebula. The condensation sequence predicts which minerals formed first as the hot solar nebula cooled (refractory oxides, then silicates, then metals, then volatiles), explaining the compositional zonation of the inner solar system. Radiometric dating of the oldest solar system materials (CAIs at 4.567 Ga) defines time zero for planetary evolution.

## Questions

```yaml
- question: "Calcium-aluminum-rich inclusions (CAIs) in chondritic meteorites are the oldest dated solid materials in the solar system at 4.567 Ga. What does their mineralogy (corundum, hibonite, perovskite, melilite) reveal about their formation conditions?"
  type: multiple-choice
  options:
    - "They formed by aqueous alteration on a parent body"
    - "Their highly refractory mineralogy (the highest-temperature condensates from a solar-composition gas) indicates they formed by condensation from the hot solar nebula, representing the first solids to form as the nebula cooled"
    - "They are fragments of Earth's core ejected during the Moon-forming impact"
    - "They formed by volcanism on a large asteroid"
  answer: 1
  explanation: "CAI mineralogy exactly matches thermodynamic predictions for the first minerals to condense from a cooling gas of solar composition. Corundum (Al2O3) condenses at ~1700 K, followed by hibonite (CaAl12O19), perovskite (CaTiO3), and melilite. These are the most refractory (highest condensation temperature) phases, consistent with being the first solids to form in the solar nebula. Their 4.567 Ga Pb-Pb age defines the start of the solar system."

- question: "CI chondrites are used as the reference for solar system elemental abundances because they match the composition of the Sun's photosphere for all elements."
  type: true-false
  answer: false
  explanation: "CI chondrites match solar photospheric abundances remarkably well for non-volatile elements (refractory lithophile, siderophile, and chalcophile elements), with agreement typically within 10-20%. However, they are depleted in the most volatile elements (H, He, C, N, O, noble gases) that were not fully incorporated into solid meteorite parent bodies. The solar photosphere better represents these volatile elements. For non-volatile elements, the CI chondrite-photosphere agreement is one of the most important observations in cosmochemistry, validating CI chondrites as proxies for bulk solar system composition."

- question: "Explain what presolar grains are and what they reveal about the stellar sources of solar system material."
  type: short-answer
  answer: "Presolar grains are tiny mineral particles (typically < 1 um) found within primitive meteorites that formed in the outflows of ancient stars before the solar system existed. They are identified by extremely anomalous isotopic compositions that cannot be produced by any solar system process -- for example, silicon carbide (SiC) grains with 12C/13C ratios 10-100x different from solar, recording nucleosynthesis in asymptotic giant branch (AGB) stars. Nanodiamond, corundum, and graphite grains record contributions from supernovae. These grains survived the formation of the solar nebula, incorporation into parent bodies, and residence in meteorites for 4.6 Gyr, providing direct samples of pre-solar stellar material and constraining the nucleosynthetic contributions to the solar system's elemental and isotopic inventory."
  explanation: "Presolar grains are literally stardust -- physical samples of other stars that predate our solar system, identifiable by isotopic signatures impossible to produce locally."
```

## Explainer

Cosmochemistry provides the initial conditions for all other geochemistry -- the elemental and isotopic inventory with which the solar system started, and the processes that distributed this material among the planets, asteroids, and comets. Without meteorites, we would have no direct knowledge of the bulk composition of the Earth or the age of the solar system.

Chondritic meteorites -- undifferentiated assemblages of chondrules (mm-scale melted silicate droplets), CAIs, metal grains, and fine-grained matrix -- are the most primitive solar system materials. CI chondrites (from the Ivuna meteorite class) are particularly important: their non-volatile element ratios match the Sun's photosphere within measurement uncertainty, establishing them as the chemical reference for the solar system. All planetary compositions are discussed relative to CI chondrite, and the term "chondritic" means "matching bulk solar system composition."

The condensation sequence, calculated from thermodynamic equilibrium in a cooling gas of solar composition, predicts the order in which minerals form: refractory oxides (>1400 K), silicates (~1300 K), metallic iron (~1100 K), FeS (~680 K), and hydrated silicates and ices (<300 K). This sequence explains the compositional gradient in the inner solar system: Mercury and Venus are enriched in refractory elements; Earth has an intermediate composition; and the outer solar system retained volatiles and ices. While the actual nebula was not perfectly equilibrated (disequilibrium processes like evaporation, flash heating, and mixing were important), the condensation sequence provides the thermodynamic framework for understanding solar system chemistry.

The chronology of the early solar system is anchored by high-precision radiometric dating. CAIs define time zero at 4.5672 +/- 0.0006 Ga (Pb-Pb dating). Chondrules formed 1-3 Myr later. Parent body differentiation (asteroid melting and core formation) occurred within 1-5 Myr of CAI formation, as constrained by the 26Al-26Mg and 182Hf-182W short-lived chronometers. Earth's core formation was essentially complete by 30-50 Myr after solar system formation (Hf-W systematics). The Moon-forming impact occurred at ~4.51 Ga. This precise chronology, built from multiple radiometric systems in meteorites and lunar samples, provides the timeline for understanding how the solar system assembled from nebular dust into differentiated planets.
