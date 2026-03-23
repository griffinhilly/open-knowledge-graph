---
id: thermobarometry-cooling-history
title: Thermobarometry and Pressure-Temperature Paths
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: thermochronology-and-cooling-ages
  type: hard
builds-toward:
- lithospheric-thermal-evolution
tags:
- thermobarometry
- pt-path
- cooling-history
stage: expert
status: draft
---

# Thermobarometry and Pressure-Temperature Paths

## Core Idea
Mineral assemblages and their chemical compositions constrain pressure and temperature at crystallization. P-T paths traced through metamorphic grade document tectonic history; closure ages from radiometric dating mark cooling rates and exhumation.

## Questions

```yaml
- question: "Why is the Fe/Mg ratio in coexisting garnet and biotite useful as a geothermometer?"
  type: multiple-choice
  options:
    - "Iron and magnesium have very different atomic masses, so their ratio changes predictably as rock density increases with depth"
    - "The partitioning of Fe and Mg between the two minerals is temperature-dependent: the equilibrium Fe/Mg ratio in each mineral shifts in a known way with temperature and has been experimentally calibrated"
    - "Garnet always contains more iron and biotite always contains more magnesium regardless of temperature, so their ratio reflects pressure rather than temperature"
    - "Iron and magnesium undergo radioactive decay at different rates, so their ratio acts as a radiometric clock recording crystallization age"
  answer: 1
  explanation: "Geothermometers rely on element partitioning: how an element distributes itself between two coexisting phases depends on temperature. For garnet-biotite, more Mg enters garnet (and more Fe enters biotite) at higher temperatures, shifting the KD = (Fe/Mg)garnet / (Fe/Mg)biotite value in a calibrated, reproducible way. By measuring the ratio in both minerals from the same rock and applying the experimental calibration, you calculate the temperature at which they last equilibrated. This is exchange thermometry — no radioactive decay involved (option D is a different technique: geochronology)."

- question: "A metamorphic rock preserves a garnet crystal whose core records high pressure and moderate temperature, while the rim records lower pressure and higher temperature. What tectonic setting and history does this P-T path suggest?"
  type: multiple-choice
  options:
    - "A counterclockwise path, indicating the rock was heated by a nearby igneous intrusion before being buried"
    - "A clockwise P-T path consistent with deep burial during continental collision (high P), followed by heating during exhumation and then cooling at the surface"
    - "A simple burial path with no uplift — the core formed deeper and the rim formed shallower as the crust compressed"
    - "An isothermal path indicating the rock was transported horizontally through the crust without significant heating or cooling"
  answer: 1
  explanation: "A sequence of high pressure → lower pressure + higher temperature describes a clockwise P-T path: rapid burial to depth (increasing pressure), then heating at depth (temperature rises as the rock equilibrates with the geotherm), then exhumation (pressure decreases while temperature may briefly continue rising due to slow thermal equilibration). This is the hallmark of continent-continent collision zones like the Himalaya. A counterclockwise path (option A) would show heating before pressure increase, characteristic of contact metamorphism near intrusions. The core-to-rim chemical evolution records this path over millions of years."

- question: "A P-T-t path records not just the pressures and temperatures a rock experienced during its history, but also the rate at which it moved through those conditions."
  type: true-false
  answer: true
  explanation: "P-T paths from thermobarometry are combined with 't' (time) from thermochronology — radiometric systems that close at specific temperatures, giving cooling ages. Rapid cooling (many °C per million years, constrained by two or more thermochronometers at different closure temperatures) implies fast exhumation by faulting or erosion. Slow cooling implies gradual uplift or thermal relaxation. The rate dimension is what converts a geometric path in P-T space into an actual tectonic history with rates of burial, heating, and exhumation."

- question: "Thermobarometry determines the closure temperature of a rock's radiometric system — the temperature at which isotopes stopped diffusing — making it equivalent to thermochronology."
  type: true-false
  answer: false
  explanation: "Thermobarometry and thermochronology answer different questions. Thermobarometry uses the chemical compositions of coexisting mineral pairs to determine the P-T conditions at which those minerals last equilibrated (crystallization or peak metamorphism conditions). Thermochronology uses the accumulation of radiogenic daughter isotopes to determine when a mineral cooled through its closure temperature. They are complementary techniques: thermobarometry constrains the P-T history, thermochronology constrains the timing and rate of that history. Combining them yields the full P-T-t path."

- question: "How does the chemical composition of a zoned garnet crystal record a P-T path, and why do the core and rim record different conditions?"
  type: short-answer
  answer: "Garnet grows incrementally as a rock is buried and metamorphosed. The core crystallizes at the earliest (lowest P-T) conditions and its Fe/Mg and Ca/Mn ratios are set by equilibrium with the surrounding mineral assemblage at that point. As burial continues and P and T rise, new garnet overgrows the existing crystal as a rim, equilibrating with the new conditions. Diffusion within the garnet interior is slow enough that the core composition is largely preserved rather than re-equilibrating. The result is a chemical profile across the crystal — core to rim — that archives the changing P-T conditions during the rock's burial and heating history."
  explanation: "Zoned garnets are natural recorders of metamorphic history because garnet is a slow diffuser at moderate temperatures — it preserves compositional gradients that would be erased in faster-diffusing minerals. A geologist can measure a microprobe transect across a garnet (measuring Fe, Mg, Ca, Mn at intervals from core to rim) and decode the P-T conditions at each growth stage. Combining multiple garnet zones with independent barometers (e.g., Al-in-hornblende) and geochronology can reveal a detailed history of burial, peak metamorphism, and exhumation across tens of millions of years of tectonic activity."
```

## Explainer

From your study of thermochronology and cooling ages, you know that different radiometric systems "close" — stop exchanging parent and daughter isotopes with their surroundings — at different temperatures. **Thermobarometry** extends this concept by using the chemical compositions of coexisting minerals to determine the actual pressure and temperature conditions at which a rock crystallized or equilibrated, not just the temperature at which a clock started ticking.

The principle relies on **exchange thermometry** and **net-transfer barometry**. Certain mineral pairs exchange elements between them in a temperature-dependent way. For example, the partitioning of iron and magnesium between garnet and biotite depends strongly on temperature: at higher temperatures, more magnesium enters the garnet and more iron enters the biotite. By measuring the Fe/Mg ratio in both minerals, you can calculate the temperature at which they last equilibrated using an experimentally calibrated thermometer. Similarly, some reactions involve a change in the total number of moles of solid phases, making them sensitive to pressure. The aluminum content of amphibole in the presence of specific other minerals, for instance, increases with pressure — providing a barometer. Combining a thermometer and barometer from the same rock gives you a **P-T point**: the pressure and temperature conditions that rock last experienced.

The real power of thermobarometry emerges when you can determine multiple P-T points from the same rock, recorded at different stages of its history. Metamorphic minerals often grow in zones — a garnet crystal might have a core that formed at one P-T condition and a rim that equilibrated at another. Chemical profiles across such zoned minerals trace a **P-T path**: the trajectory through pressure-temperature space that the rock followed during burial, heating, and eventual exhumation. A rock that was buried to 30 km depth (high pressure) and heated to 600°C before being uplifted records a **clockwise P-T path** typical of continent-continent collision zones. A rock heated at shallow depth before burial follows a counterclockwise path, characteristic of contact metamorphism near igneous intrusions.

When you combine P-T paths with cooling ages from thermochronology, the result is a **P-T-t path** — pressure, temperature, and time. This tells you not just where the rock has been in P-T space, but how fast it moved through those conditions. Rapid cooling (many degrees per million years) implies fast exhumation — the rock was brought to the surface quickly by faulting or erosion. Slow cooling implies gradual uplift or thermal relaxation. Together, thermobarometry and thermochronology reconstruct the tectonic history of a rock from its mineral chemistry and isotopic clocks, turning a hand sample into a record of mountain building, burial, and exhumation spanning millions of years.
