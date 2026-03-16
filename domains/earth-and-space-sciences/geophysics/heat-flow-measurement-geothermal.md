---
id: heat-flow-measurement-geothermal
title: Heat Flow Measurement and Geothermal Gradient
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: geothermal-gradient-crustal-heat-flow
  type: hard
- id: thermal-conductivity-and-rocks
  type: hard
builds-toward:
- conduction-models-crustal-heat
tags:
- heat-flow
- geothermal
- gradient
- measurement
stage: advanced
status: draft
---

# Heat Flow Measurement and Geothermal Gradient

## Core Idea
Heat flow (q = κ × dT/dz) is measured by combining borehole temperature profiles with thermal conductivity. Global heat flow varies from ~30 mW/m² in stable cratons to >150 mW/m² in rift zones and mid-ocean ridges.

## Explainer

You already understand that Earth's interior is hot and that temperature increases with depth — the geothermal gradient. You also know that different rock types conduct heat at different rates — thermal conductivity. Heat flow measurement brings these two concepts together into a single, quantitative measure of how much thermal energy is escaping through the surface at any given location. The fundamental equation is deceptively simple: **q = κ × dT/dz**, where q is heat flow in watts per square meter, κ is the thermal conductivity of the rock, and dT/dz is the temperature gradient measured in a borehole. Multiply how fast temperature rises with depth by how efficiently the rock conducts heat, and you get the rate of energy loss through the surface.

In practice, making this measurement requires drilling a borehole — or using an existing one — and lowering a temperature probe to record temperatures at multiple depths. The resulting **temperature-depth profile** ideally shows a steady, linear increase with depth once you get below the zone affected by seasonal surface temperature fluctuations (typically the upper 10–20 meters). The slope of this linear portion is the geothermal gradient, commonly expressed in °C per kilometer. Typical values range from about 20°C/km in old, stable continental interiors to 40°C/km or more in tectonically active regions. Separately, core samples from the borehole are brought to the laboratory and their **thermal conductivity** is measured, usually with a divided-bar apparatus or needle-probe method. The product of gradient and conductivity gives the heat flow.

Interpreting heat flow measurements requires understanding what controls the thermal energy budget at different locations. Earth's internal heat comes from two main sources: **radiogenic heat production** from the decay of uranium, thorium, and potassium concentrated in crustal rocks, and **primordial heat** left over from planetary formation and core crystallization flowing up from the mantle. In old, thick continental crust like the Canadian Shield or West African Craton, the crust has been stable for billions of years, radiogenic elements have decayed substantially, and heat flow is low — roughly 30–50 mW/m². At mid-ocean ridges, hot mantle material rises to within a few kilometers of the surface, and heat flow exceeds 150 mW/m² (though much of this is actually carried by hydrothermal circulation rather than pure conduction, complicating the measurement). Continental rift zones and volcanic arcs show elevated values for similar reasons — thinned lithosphere and shallow hot material.

The global pattern of heat flow measurements, compiled from thousands of boreholes and ocean-floor probes, reveals the thermal structure of the lithosphere and provides essential constraints for models of mantle convection, lithospheric cooling, and tectonic processes. Anomalously high heat flow can indicate geothermal energy potential, recent magmatic activity, or thinning crust. Anomalously low values may signal thick, cold lithospheric roots beneath ancient cratons. These measurements are the empirical foundation upon which conduction models and thermal evolution studies are built.
