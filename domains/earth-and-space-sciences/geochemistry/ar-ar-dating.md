---
id: ar-ar-dating
title: Ar-Ar Dating
domain: earth-and-space-sciences
course: geochemistry
prerequisites:
- id: geochemical-thermodynamics
  type: soft
builds-toward:
- crustal-evolution-geochemistry
tags:
- Ar-Ar
- K-Ar
- geochronology
- thermochronology
- step-heating
stage: expert
status: validated
---

# Ar-Ar Dating

## Core Idea
The 40Ar/39Ar method is a refined version of K-Ar dating where the sample is irradiated with neutrons to convert 39K to 39Ar, enabling measurement of both parent and daughter isotopes on the same aliquot by mass spectrometry. Step-heating (incrementally increasing temperature) releases argon from different crystallographic sites, producing an age spectrum that reveals the sample's thermal history. A flat (plateau) age spectrum indicates a single undisturbed cooling age. Disturbed spectra with young edges and old cores record partial argon loss during thermal events. The method dates cooling through the closure temperature of the mineral analyzed (K-feldspar ~150-350 C, biotite ~300 C, hornblende ~500 C, muscovite ~350 C), making it a thermochronometer that records when a rock cooled through specific temperatures.

## Questions

```yaml
- question: "An Ar-Ar step-heating experiment on hornblende produces a flat age plateau at 450 Ma across 80% of the total 39Ar released. What does this indicate?"
  type: multiple-choice
  options:
    - "The rock crystallized at 450 Ma from magma"
    - "The hornblende cooled through its closure temperature (~500 C) at 450 Ma and has not been significantly reheated since; the flat plateau indicates a single, undisturbed cooling event"
    - "The sample is contaminated with excess argon"
    - "The age has no geological meaning because Ar-Ar only works on volcanic rocks"
  answer: 1
  explanation: "A well-defined plateau (concordant step ages over a large fraction of gas release) indicates that argon is uniformly distributed in the mineral, consistent with undisturbed radiogenic accumulation since closure. The 450 Ma age records when hornblende cooled below ~500 C -- this could be primary cooling of an igneous rock or cooling after a metamorphic event. The key interpretive point is that Ar-Ar dates cooling, not necessarily crystallization."

- question: "The Ar-Ar method dates the same event as U-Pb zircon geochronology."
  type: true-false
  answer: false
  explanation: "U-Pb zircon dates crystallization (zircon has a very high closure temperature, >900 C, and incorporates U during crystal growth). Ar-Ar dates cooling through the analyzed mineral's closure temperature (300-500 C for common minerals). In a slowly cooled pluton, U-Pb might give 100 Ma (crystallization) while Ar-Ar hornblende gives 95 Ma (cooling through 500 C) and Ar-Ar biotite gives 90 Ma (cooling through 300 C). The difference reveals the cooling rate. In rapidly quenched volcanic rocks, both methods give effectively the same age."

- question: "Explain what excess argon is and how step-heating can detect it."
  type: short-answer
  answer: "Excess argon is 40Ar that was incorporated into the mineral from external sources (magmatic fluids, older material) rather than produced by in-situ 40K decay. It causes anomalously old apparent ages. In step-heating, excess argon typically resides in loosely bound sites or fluid inclusions released at low temperatures, producing anomalously old ages in the first few heating steps. If high-temperature steps (from retentive crystallographic sites) define a plateau while low-temperature steps are discordantly old, excess argon is diagnosed. The plateau age is then interpreted as reliable while the low-T steps are discarded."
  explanation: "Step-heating acts as a quality filter: excess argon in loosely bound sites is released first at low temperature, separated from the radiogenic argon released at high temperature from the crystal lattice."
```

## Explainer

The Ar-Ar method improved upon K-Ar dating by measuring the parent (K, via proxy 39Ar) and daughter (40Ar) on the same aliquot, eliminating the need for separate K concentration analysis and the assumption of sample homogeneity. The neutron irradiation that converts a known fraction of 39K to 39Ar is the key innovation -- it turns a two-aliquot measurement into a single-aliquot isotope ratio measurement.

The step-heating technique extracts argon at progressively higher temperatures, exploiting the fact that argon in different crystallographic sites has different retentivity. Loosely held argon (from grain boundaries, fluid inclusions, or partially disturbed zones) is released at low temperatures; argon from the intact crystal lattice is released at high temperatures. Plotting apparent age versus cumulative 39Ar fraction produces an age spectrum. A plateau -- a series of contiguous steps with statistically indistinguishable ages comprising >50% of the total 39Ar -- provides a robust age estimate.

The concept of closure temperature (Tc) is central. As a mineral cools, it transitions from a state where argon diffuses freely out of the crystal (open system, no age accumulation) to a state where argon is quantitatively retained (closed system, age accumulates). The closure temperature depends on the mineral's crystal structure, grain size, and cooling rate. Hornblende (Tc ~500 C) closes at higher temperature than muscovite (~350 C) or biotite (~300 C) or K-feldspar (~150-350 C). Dating multiple minerals from the same sample provides a cooling history -- a series of time-temperature points that define the cooling path.

Applications span tectonic studies (timing of metamorphism, exhumation, faulting), volcanology (eruption ages), extraterrestrial chronology (ages of meteorites and lunar rocks), and paleomagnetic calibration (dating lava flows for the geomagnetic polarity time scale). The method works from ~100 ka (young volcanic rocks with very little radiogenic 40Ar) to the age of the solar system (~4.56 Ga), making it one of the most versatile geochronological tools available.
