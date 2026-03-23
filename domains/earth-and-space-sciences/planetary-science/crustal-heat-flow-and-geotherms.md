---
id: crustal-heat-flow-and-geotherms
title: Crustal Heat Flow and Planetary Geothermal Gradients
domain: earth-and-space-sciences
course: planetary-science
prerequisites:
- id: planetary-thermal-modeling
  type: hard
- id: heat-flow-measurement-geothermal
  type: soft
builds-toward:
- core-crystallization-and-reversals
- thermal-evolution-terrestrial-planets
tags:
- heat-flow
- geotherm
- temperature-profile
- crustal-structure
stage: expert
status: validated
---

# Crustal Heat Flow and Planetary Geothermal Gradients

## Core Idea
The surface heat flow combined with rock thermal conductivity defines the geothermal gradient—how temperature increases with depth. Planetary geotherms constrain crustal composition, mantle temperature, and convection rates; steeper gradients on young or tectonically active planets reflect higher internal temperatures and vigor of mantle convection.

## Questions

```yaml
- question: "A geologist constructs a geotherm for a tectonic region and finds it intersects the rock solidus (onset of melting) at a depth of only 15 km. What does this most likely indicate about the tectonic setting?"
  type: multiple-choice
  options:
    - "The region is an ancient stable craton with very low heat flow"
    - "The region is a mid-ocean ridge or hotspot with high heat flow and active volcanism"
    - "The region has an unusually thick lithosphere that conducts heat poorly"
    - "The geotherm must be incorrect; solidus intersections only occur at mantle depths"
  answer: 1
  explanation: "When the geotherm reaches the solidus (melting onset temperature) at shallow depth, rock is melting near the surface — the condition for active volcanism and thin lithosphere. This is exactly the situation at mid-ocean ridges and mantle hotspots, where high heat flow drives steep geotherms that intersect the solidus at relatively shallow depths. Ancient cratons have low heat flow and gentle geotherms that remain well below the solidus, consistent with their thick, cold, stable lithospheres and absence of volcanism."

- question: "Earth's continental cratons show much lower surface heat flow (~40–50 mW/m²) than mid-ocean ridges (>200 mW/m²). What best explains this difference?"
  type: multiple-choice
  options:
    - "Cratons have lower thermal conductivity rocks that trap heat at depth"
    - "Mid-ocean ridges have more uranium and thorium, producing far more radiogenic heat"
    - "Cratons have thick, old lithospheres that have cooled over billions of years; ridges sit above upwelling hot mantle"
    - "Cratons have no water, so heat cannot be transported to the surface by hydrothermal circulation"
  answer: 2
  explanation: "The fundamental control on surface heat flow is the underlying mantle temperature and the age and thickness of the overlying lithosphere. At mid-ocean ridges, hot asthenospheric mantle upwells directly beneath thin, young oceanic crust — the heat source is close and vigorous. Cratons are ancient continental regions with thick, cold lithospheres that have had billions of years to cool; their heat flow reflects slow conduction of residual primordial heat and radiogenic decay at depth. The contrast is primarily about the thermal state of the underlying mantle and lithospheric age, not differences in rock conductivity or radiogenic element content alone."

- question: "By comparing a planet's geotherm to the melting curves of its constituent rocks, scientists can infer whether partial melting is occurring at depth and where the boundary between rigid lithosphere and convecting asthenosphere lies."
  type: true-false
  answer: true
  explanation: "The geotherm is a predictive tool, not merely a temperature measurement. Where the geotherm plots above the solidus, partial melting is expected — this corresponds to magma generation zones. The depth at which the geotherm crosses below the solidus marks the base of the mechanically rigid lithosphere; below that, rock is close enough to its melting point to flow viscously on geological timescales (the asthenosphere). This intersection approach is how geologists infer the depth of melt zones and lithospheric thickness on Earth and other planets without direct sampling."

- question: "A steeper geothermal gradient always indicates higher surface heat flow, regardless of the rock's thermal conductivity."
  type: true-false
  answer: false
  explanation: "Surface heat flow = geothermal gradient × thermal conductivity. The gradient and heat flow are linked through thermal conductivity, which varies substantially between rock types. A steep gradient through poorly conducting rock (low conductivity) may represent the same heat flow as a gentle gradient through highly conducting rock. To determine actual heat flow, you must measure both the temperature gradient and the thermal conductivity of the rock. Failing to account for conductivity variation leads to incorrect heat flow estimates and misinterpretation of the geothermal regime."

- question: "Explain how comparing a planet's geotherm to the rock solidus allows scientists to infer that planet's tectonic activity and interior state."
  type: short-answer
  answer: "The geotherm (temperature vs. depth) and the solidus (onset of melting vs. depth) for the same rock type can be plotted together. Where the geotherm lies above the solidus, partial melting occurs — indicating active magma sources that drive volcanism and potentially plate tectonics. Where the geotherm lies well below the solidus throughout, all rock at depth is solid and cold, indicating thick rigid lithosphere and no active volcanism. The depth at which the geotherm approaches the solidus determines the lithosphere-asthenosphere boundary. A steep geotherm (high heat flow) intersects the solidus at shallow depth, implying thin lithosphere and active geology. A gentle geotherm (low heat flow) stays far below the solidus, implying a thick, cold, tectonically quiet lithosphere — as seen on the Moon or Mars today."
  explanation: "This approach allows planetary scientists to compare Earth with Mars, the Moon, and Venus using surface heat flow measurements, seismic data, and volcanic history. The geotherm-solidus relationship encodes the thermal vigor of a planet's interior and its capacity for geological activity."
```

## Explainer

From your study of planetary thermal modeling and heat flow measurement, you know that planets are hot inside and that this internal heat drives geological activity. The **geothermal gradient** — the rate at which temperature increases with depth — is the most direct expression of how efficiently a planet moves its internal heat outward. On Earth, the average geothermal gradient in continental crust is about 25–30°C per kilometer of depth. This means that just 30 km down, temperatures reach 750–900°C — hot enough to partially melt some rock types. But this number varies enormously depending on tectonic setting, and those variations tell you about the processes operating below.

**Surface heat flow** is measured in milliwatts per square meter (mW/m²) and is the product of the geothermal gradient and the rock's **thermal conductivity** — how easily heat passes through it. Earth's average surface heat flow is about 87 mW/m², but it ranges from roughly 40 mW/m² in old, stable continental cratons to over 200 mW/m² at mid-ocean ridges. The heat itself comes from two sources: **primordial heat** left over from planetary accretion and differentiation, and **radiogenic heat** produced by the decay of uranium, thorium, and potassium in rocks. In Earth's continental crust, radiogenic heat production is concentrated in the upper crust (which is enriched in these elements), meaning a significant fraction of the surface heat flow originates within the crust itself rather than flowing up from the mantle.

The **geotherm** — the full temperature-depth profile through a planet — is constructed by integrating the thermal gradient downward, accounting for changes in heat production and thermal conductivity with depth. A geotherm is not just a temperature curve; it is a predictive tool. By comparing a planet's geotherm to the melting curves (solidus) of its constituent rocks, you can determine where melting occurs, where the lithosphere transitions to the convecting asthenosphere, and how viscous the mantle is at any given depth. A steep geotherm that intersects the solidus at shallow depth indicates active volcanism and thin lithosphere — the situation at mid-ocean ridges and hotspots. A gentle geotherm that stays well below the solidus implies a thick, rigid, cold lithosphere — the situation beneath ancient continental shields.

Comparing geotherms across planets reveals their thermal evolution. Mars, being smaller than Earth, has cooled more efficiently and likely has a relatively gentle modern geotherm, consistent with its lack of current plate tectonics and infrequent volcanism. The Moon, smaller still, cooled so effectively that its interior is largely solid and its surface heat flow is very low. Venus, similar in size to Earth, presents a puzzle: it may have a steep geotherm but lacks plate tectonics, suggesting its heat escapes through episodic global resurfacing events rather than steady-state convection. Understanding crustal heat flow and geotherms is therefore foundational for inferring the internal state, tectonic mode, and geological vitality of any rocky world.
