---
id: thermochronology-and-cooling-ages
title: Thermochronology and Crustal Cooling Ages
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: thermal-conductivity-and-rocks
  type: hard
- id: heat-equation-pde
  type: hard
- id: radioactive-decay
  type: hard
tags:
- thermochronology
- cooling-ages
- geochronology
- tectonics
stage: expert
status: draft
---

# Thermochronology and Crustal Cooling Ages

## Core Idea
Thermochronology exploits temperature-dependent closure of diffusion in isotope systems (K–Ar, ⁴⁰Ar/³⁹Ar, U–Pb, (U–Th)/He) to measure the age when rocks cooled through a closure temperature. Different isotopes close at different temperatures (muscovite ~350°C, biotite ~300°C, apatite ~75°C), yielding nested cooling ages. Combining multiple systems constructs a cooling history that reveals exhumation rates, denudation patterns, and burial-heating events, constraining lithospheric dynamics and surface processes.

## Questions

```yaml
- question: "A granite sample gives an apatite (U–Th)/He age of 8 Ma. A colleague reports this as 'the age when the granite formed.' What is the most fundamental error in this statement?"
  type: multiple-choice
  options:
    - "Apatite (U–Th)/He cannot be applied to granites — it only works on sedimentary rocks"
    - "The age records when the granite cooled below the apatite closure temperature (~75°C), not when it crystallized. The granite may have formed hundreds of millions of years earlier and only recently been exhumed near the surface"
    - "The error is the assumed closure temperature — apatite actually closes at ~350°C, not ~75°C"
    - "8 Ma is too young for a granite, since granites require at least 100 Ma to cool from magma"
  answer: 1
  explanation: "Thermochronology measures cooling ages, not formation ages. At temperatures above the closure temperature (~75°C for apatite (U–Th)/He), helium diffuses out of apatite grains as fast as it is produced — no clock accumulates. The clock only starts when the rock cools below that threshold. An 8 Ma apatite age means the rock passed through ~75°C at 8 Ma; it may have crystallized at 500 Ma and spent hundreds of millions of years at depth. Confusing a cooling age with a formation age is the most important conceptual error in thermochronology."

- question: "A geologist has muscovite ⁴⁰Ar/³⁹Ar (closes ~350°C), biotite ⁴⁰Ar/³⁹Ar (~300°C), and apatite (U–Th)/He (~75°C) ages of 60, 55, and 5 Ma for the same rock. What is the most geologically significant implication?"
  type: multiple-choice
  options:
    - "The three systems disagree, indicating the rock experienced three separate formation events at 60, 55, and 5 Ma"
    - "The rock cooled relatively slowly from 350°C to 300°C between 60–55 Ma, then stagnated tectonically until rapid exhumation brought it through 75°C at 5 Ma — a two-phase cooling history"
    - "All ages should be averaged (40 Ma) to determine the true crystallization age"
    - "The apatite age is most reliable because it has the lowest closure temperature"
  answer: 1
  explanation: "Each age marks when the rock crossed a specific temperature threshold. Plotting these: the rock was at ~350°C at 60 Ma and ~300°C at 55 Ma — slow cooling of ~10°C/Ma. Then from 55 Ma to 5 Ma (50 Myr), the rock had not yet cooled to ~75°C — suggesting very slow exhumation or thermal stagnation at depth. Then at 5 Ma, rapid exhumation brought it through 75°C. This reveals a history of early tectonic activity followed by quiescence, then a recent acceleration — information no single geochronometer could provide."

- question: "A thermochronological age records when the mineral originally crystallized from melt."
  type: true-false
  answer: false
  explanation: "A cooling age records when the rock cooled below the closure temperature of the specific mineral-isotope system — NOT when it formed. Above the closure temperature, daughter isotopes diffuse out as fast as they are produced and no radiometric clock accumulates. A biotite ⁴⁰Ar/³⁹Ar age of 30 Ma means biotite cooled through ~300°C at 30 Ma; it may have crystallized during a metamorphic event at 200 Ma. The crystallization age would require a system with a much higher closure temperature, or a different geochronological method entirely."

- question: "Applying multiple thermochronological systems with different closure temperatures to the same rock enables reconstruction of a temperature–time cooling path, not just a single date."
  type: true-false
  answer: true
  explanation: "Each system acts as a geothermometer at a specific threshold. Muscovite closes at ~350°C, biotite at ~300°C, zircon fission-track at ~240°C, and apatite (U–Th)/He at ~75°C. Multiple ages from the same rock define multiple points on a temperature–time curve. The slope between those points is the cooling rate, which can be converted to exhumation rate using the geothermal gradient. This multi-system approach reveals the history of how fast the rock moved toward the surface — far more informative than any single date."

- question: "What is the closure temperature, and why does it matter that different mineral-isotope pairs have different closure temperatures?"
  type: short-answer
  answer: "The closure temperature is the temperature below which a mineral effectively stops losing radiogenic daughter products by diffusion — below this point, daughters accumulate and the radiometric clock runs. Each mineral-isotope system has a different closure temperature because diffusion rates depend on the crystal structure and the size of the diffusing species (muscovite ~350°C, biotite ~300°C, apatite (U–Th)/He ~75°C). Having multiple systems at different temperatures means you can sample the rock's cooling history at multiple points and reconstruct a temperature–time path, revealing exhumation rates and tectonic events across different depths and times."
  explanation: "If all systems had the same closure temperature, you would get one date — when the rock crossed that single threshold. Multiple closure temperatures act like thermometers positioned at different depths in the crust: each one 'turns on' as the rock cools through it, leaving a dated record. The time spacing between records constrains the cooling rate, and with an assumed geothermal gradient, that translates to an exhumation rate — how fast erosion or faulting brought the rock toward the surface."
```

## Explainer

You already understand radioactive decay — parent isotopes transforming into daughter products at known rates — and you know from studying heat conduction that temperature within the Earth increases with depth along a geothermal gradient. Thermochronology combines these two ideas in a powerful way: it uses the accumulation of radiogenic daughter products not to date when a rock formed, but to date when it cooled below a specific temperature. This seemingly subtle distinction is what makes the technique so useful for understanding how rocks move through the crust over geological time.

The key concept is the **closure temperature**. At high temperatures, daughter isotopes (or other damage products like fission tracks and helium atoms) diffuse out of mineral grains as fast as they are produced — the system is "open" and no radiometric clock is ticking. Below the closure temperature, diffusion effectively stops, daughter products accumulate, and the clock starts. Each mineral-isotope pair has a different closure temperature because diffusion rates depend on the crystal structure and the size of the diffusing species. **Muscovite** in the ⁴⁰Ar/³⁹Ar system closes at about 350°C, **biotite** at roughly 300°C, **zircon** in the fission-track system at approximately 240°C, and **apatite** in the (U–Th)/He system at a remarkably low ~75°C. These are not precise thresholds — they depend on cooling rate and grain size — but the principle is robust.

The power of thermochronology comes from applying **multiple systems to the same rock**. If a granite sample yields a muscovite ⁴⁰Ar/³⁹Ar age of 50 Ma, a biotite age of 45 Ma, a zircon fission-track age of 35 Ma, and an apatite (U–Th)/He age of 10 Ma, you can plot temperature against time and reconstruct the rock's **cooling path** — it passed through 350°C at 50 Ma, 300°C at 45 Ma, 240°C at 35 Ma, and 75°C at 10 Ma. The slope of this cooling curve is the cooling rate, and if you know the geothermal gradient, you can convert cooling rate to **exhumation rate** — how fast the rock was being brought toward the surface by erosion or tectonic uplift. Rapid cooling (steep slope) implies fast exhumation; slow cooling (gentle slope) implies tectonic quiescence.

This approach has transformed our understanding of mountain building, landscape evolution, and basin history. In the Himalayas, thermochronology reveals that exhumation rates accelerated dramatically around 10–15 Ma, linked to intensified monsoon erosion. In extensional settings, cooling ages constrain when normal faults were active and how fast footwall rocks were exhumed. In sedimentary basins, **detrital thermochronology** — dating individual mineral grains eroded from source rocks and deposited in sediments — reveals the erosion history of mountain ranges that may no longer exist. The heat equation you studied provides the theoretical framework: given a model of how rocks move through the thermal field (advection by faulting and erosion, conduction through surrounding rock), you can predict cooling ages and compare them to observations, iteratively refining your model of crustal dynamics.
