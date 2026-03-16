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
stage: advanced
status: draft
---

# Thermochronology and Crustal Cooling Ages

## Core Idea
Thermochronology exploits temperature-dependent closure of diffusion in isotope systems (K–Ar, ⁴⁰Ar/³⁹Ar, U–Pb, (U–Th)/He) to measure the age when rocks cooled through a closure temperature. Different isotopes close at different temperatures (muscovite ~350°C, biotite ~300°C, apatite ~75°C), yielding nested cooling ages. Combining multiple systems constructs a cooling history that reveals exhumation rates, denudation patterns, and burial-heating events, constraining lithospheric dynamics and surface processes.

## Explainer

You already understand radioactive decay — parent isotopes transforming into daughter products at known rates — and you know from studying heat conduction that temperature within the Earth increases with depth along a geothermal gradient. Thermochronology combines these two ideas in a powerful way: it uses the accumulation of radiogenic daughter products not to date when a rock formed, but to date when it cooled below a specific temperature. This seemingly subtle distinction is what makes the technique so useful for understanding how rocks move through the crust over geological time.

The key concept is the **closure temperature**. At high temperatures, daughter isotopes (or other damage products like fission tracks and helium atoms) diffuse out of mineral grains as fast as they are produced — the system is "open" and no radiometric clock is ticking. Below the closure temperature, diffusion effectively stops, daughter products accumulate, and the clock starts. Each mineral-isotope pair has a different closure temperature because diffusion rates depend on the crystal structure and the size of the diffusing species. **Muscovite** in the ⁴⁰Ar/³⁹Ar system closes at about 350°C, **biotite** at roughly 300°C, **zircon** in the fission-track system at approximately 240°C, and **apatite** in the (U–Th)/He system at a remarkably low ~75°C. These are not precise thresholds — they depend on cooling rate and grain size — but the principle is robust.

The power of thermochronology comes from applying **multiple systems to the same rock**. If a granite sample yields a muscovite ⁴⁰Ar/³⁹Ar age of 50 Ma, a biotite age of 45 Ma, a zircon fission-track age of 35 Ma, and an apatite (U–Th)/He age of 10 Ma, you can plot temperature against time and reconstruct the rock's **cooling path** — it passed through 350°C at 50 Ma, 300°C at 45 Ma, 240°C at 35 Ma, and 75°C at 10 Ma. The slope of this cooling curve is the cooling rate, and if you know the geothermal gradient, you can convert cooling rate to **exhumation rate** — how fast the rock was being brought toward the surface by erosion or tectonic uplift. Rapid cooling (steep slope) implies fast exhumation; slow cooling (gentle slope) implies tectonic quiescence.

This approach has transformed our understanding of mountain building, landscape evolution, and basin history. In the Himalayas, thermochronology reveals that exhumation rates accelerated dramatically around 10–15 Ma, linked to intensified monsoon erosion. In extensional settings, cooling ages constrain when normal faults were active and how fast footwall rocks were exhumed. In sedimentary basins, **detrital thermochronology** — dating individual mineral grains eroded from source rocks and deposited in sediments — reveals the erosion history of mountain ranges that may no longer exist. The heat equation you studied provides the theoretical framework: given a model of how rocks move through the thermal field (advection by faulting and erosion, conduction through surrounding rock), you can predict cooling ages and compare them to observations, iteratively refining your model of crustal dynamics.
