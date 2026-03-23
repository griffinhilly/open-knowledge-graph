---
id: salinity-distribution-sources-sinks
title: Salinity Distribution and Sources and Sinks
domain: earth-and-space-sciences
course: oceanography
prerequisites:
- id: water-cycle-and-atmospheric-moisture
  type: hard
- id: ocean-density-thermal-stratification
  type: hard
builds-toward:
- water-mass-formation-types
- ocean-stratification-and-mixing
- haline-stratification-patterns
tags:
- salinity
- evaporation
- precipitation
- river-input
- ice
stage: formal-systems
status: validated
---

# Salinity Distribution and Sources and Sinks

## Core Idea
Ocean salinity results from a balance between evaporative loss, precipitation input, river discharge, and ice formation/melting. Salinity patterns create density contrasts that fuel thermohaline circulation, with regional salinity variations reflecting local hydrology and climate conditions.

## Questions

```yaml
- question: "Surface salinity is highest in which oceanic region, and why?"
  type: multiple-choice
  options:
    - "Near the equator, because the sun heats the surface most intensely there"
    - "In the subtropical ocean basins (~20–30° latitude), because dry descending air drives intense evaporation with little rainfall"
    - "At the poles, because cold water holds dissolved salts better"
    - "Near major river mouths, because rivers carry dissolved minerals into the ocean"
  answer: 1
  explanation: "Salinity reflects the freshwater budget — evaporation concentrates salt, precipitation dilutes it. Subtropical regions are dominated by the Hadley cell's descending dry air, producing high evaporation and sparse rainfall, so salinity exceeds 37 PSU there. Near the equator, heavy ITCZ rainfall depresses salinity despite intense sunlight. Temperature affects density, not salinity concentration directly — cold water is denser, but not saltier."

- question: "When seawater freezes to form sea ice, what happens to the salt in the freezing water?"
  type: multiple-choice
  options:
    - "Salt becomes incorporated into the ice lattice, increasing the ice's salinity"
    - "Salt is expelled through brine rejection, leaving the surrounding water saltier and denser"
    - "Salt dissolves into the atmosphere as water vapor carries it away"
    - "Salt concentration stays the same because no water is lost from the ocean"
  answer: 1
  explanation: "During sea ice formation, the growing ice crystal expels most dissolved salt in a process called brine rejection. The surrounding seawater becomes colder AND saltier — both effects increase its density. This dense brine sinks toward the ocean floor and is a key driver of the thermohaline circulation's deep limb. The reverse happens when ice melts: relatively fresh meltwater caps the surface and freshens the upper ocean."

- question: "The global pattern of surface ocean salinity is largely a mirror image of the pattern of evaporation minus precipitation."
  type: true-false
  answer: true
  explanation: "This is the central organizing principle of salinity distribution. Where evaporation exceeds precipitation (subtropics), fresh water is removed and salinity rises. Where precipitation exceeds evaporation (equator, high latitudes), fresh water is added and salinity falls. Rivers and ice formation create local exceptions, but the E−P pattern explains the large-scale structure."

- question: "Because the tropics are the warmest part of the ocean, surface salinity there is higher than anywhere else."
  type: true-false
  answer: false
  explanation: "Warmth drives evaporation, but the tropics also receive the most rainfall — the ITCZ delivers heavy precipitation near the equator that more than offsets evaporative concentration. The result is relatively low equatorial salinity. The highest surface salinities occur in the subtropical gyres (~20–30° latitude), where descending dry air produces strong evaporation with minimal rainfall. Temperature and salinity are linked through density but do not directly co-vary in the way this statement implies."

- question: "Why does a change in the ocean's freshwater budget — such as increased glacial meltwater — threaten to disrupt thermohaline circulation?"
  type: short-answer
  answer: "Thermohaline circulation depends on density-driven sinking of cold, salty water in polar regions. Increased meltwater adds a large volume of fresh water to the surface, decreasing salinity and therefore density. If surface water becomes too fresh to sink even when cold, the density-driven downwelling that feeds the deep circulation weakens or stops. This can slow or redirect the global conveyor belt, altering heat transport between ocean basins and affecting regional climates."
  explanation: "The key link is salinity → density → vertical sinking. Brine rejection during ice formation currently creates water dense enough to sink to the ocean floor. Fresh meltwater added on top of this region stratifies the surface, preventing sinking. Thermohaline circulation is sensitive not just to temperature but to the salinity side of the density equation — which is why the freshwater budget is a critical variable in climate projections."
```

## Explainer

You already know from ocean density and thermal stratification that seawater density depends on both temperature and salinity, and that density differences drive the ocean's vertical structure. Now consider the salinity side of that equation in detail. **Salinity** — the total mass of dissolved salts per kilogram of seawater, typically expressed in practical salinity units (PSU) — averages about 35 PSU globally, but varies significantly from place to place. Understanding why requires thinking about salinity as a budget: processes that add or remove fresh water change the salt concentration of what remains.

The two dominant controls on surface salinity are **evaporation** and **precipitation**. Evaporation removes pure water from the ocean surface, leaving salt behind and increasing salinity. Precipitation adds fresh water, diluting the salt and decreasing salinity. This is directly analogous to the water cycle you studied as a prerequisite — the same atmospheric processes that move water from ocean to atmosphere and back also reshape the ocean's salt distribution. In the subtropical ocean basins (around 20–30° latitude), where dry descending air from the Hadley cell drives intense evaporation and little rain falls, surface salinity is highest — often exceeding 37 PSU. Near the equator, where the Intertropical Convergence Zone delivers heavy rainfall, and at high latitudes, where precipitation exceeds evaporation, surface salinity drops below 34 PSU. The global pattern of surface salinity is essentially a mirror of the pattern of evaporation minus precipitation.

Two additional processes act as significant **freshwater sources and sinks**. River discharge injects large volumes of fresh water near coastlines, creating pronounced low-salinity plumes — the Amazon River, for example, depresses surface salinity across thousands of square kilometers of the tropical Atlantic. At high latitudes, **sea ice formation** is a powerful salt source: when seawater freezes, most of the dissolved salt is expelled from the growing ice crystal in a process called **brine rejection**, leaving behind cold, extremely salty water that is dense enough to sink to the ocean floor. Conversely, when sea ice melts in spring, it releases relatively fresh water that caps the surface and freshens the upper ocean.

These salinity contrasts matter because they directly affect density and therefore circulation. The dense, salty water produced by subtropical evaporation and polar brine rejection feeds the deep limb of the thermohaline circulation — the global conveyor belt that moves water masses between ocean basins over centuries. Changes in the freshwater budget — increased glacial meltwater, shifts in precipitation patterns, or altered river runoff — can weaken or redirect these density-driven flows. Salinity is not just a chemical property of seawater; it is a dynamical variable that links the atmosphere's water cycle to the ocean's deepest circulation.
