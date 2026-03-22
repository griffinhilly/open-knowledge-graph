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

## Questions

```yaml
- question: "Borehole A passes through granite (thermal conductivity κ = 3.0 W/m·K) and shows a temperature gradient of 30°C/km. Borehole B passes through shale (κ = 1.5 W/m·K) and also shows a gradient of 30°C/km. What can you conclude about the surface heat flow at each location?"
  type: multiple-choice
  options:
    - "Both locations have identical heat flow because they have the same temperature gradient"
    - "Location A has twice the heat flow of location B because its rock conducts heat more efficiently at the same gradient"
    - "Location B has higher heat flow because shale is a better insulator and retains more geothermal energy"
    - "You cannot determine relative heat flow without knowing the absolute temperatures at each borehole"
  answer: 1
  explanation: "Heat flow is q = κ × dT/dz. With the same gradient (dT/dz = 30°C/km = 0.03°C/m), heat flow is simply proportional to thermal conductivity. Location A: q = 3.0 × 0.03 = 0.090 W/m². Location B: q = 1.5 × 0.03 = 0.045 W/m². Location A has exactly twice the heat flow. This is the key insight: the temperature gradient alone is not heat flow — you must multiply by conductivity. A steep gradient in low-conductivity rock can yield lower heat flow than a shallow gradient in high-conductivity rock."

- question: "What two independent measurements must be combined to calculate surface heat flow at a borehole site?"
  type: multiple-choice
  options:
    - "Surface temperature and depth of the borehole"
    - "Temperature at the surface and temperature at the bottom of the borehole"
    - "The temperature gradient (dT/dz) from the borehole temperature profile and the thermal conductivity (κ) from laboratory analysis of core samples"
    - "Crustal thickness and the mantle temperature below the lithosphere"
  answer: 2
  explanation: "Heat flow q = κ × dT/dz requires both components. The temperature gradient is obtained by lowering a temperature probe through the borehole and fitting a slope to the linear portion of the temperature-depth profile. Thermal conductivity is measured separately on rock cores in the laboratory (using a divided-bar apparatus or needle probe). Neither measurement alone gives heat flow — a steep gradient in insulating rock may carry the same heat flux as a gentle gradient in conducting rock."

- question: "The temperature gradient measured in the upper 10–20 meters of a borehole reliably reflects the steady-state geothermal heat flow from Earth's interior."
  type: true-false
  answer: false
  explanation: "False. The shallow subsurface is contaminated by surface temperature fluctuations — seasonal cycles, multi-decadal climate variability, and even the annual temperature wave — which penetrate tens of meters into the crust. These signals superimpose a non-geothermal component on the temperature profile, making shallow gradients unreliable indicators of deep heat flow. Geothermal measurements use deeper portions of the borehole, where surface temperature signals have attenuated and the profile reflects only the steady conduction of internal heat."

- question: "Mid-ocean ridges generally have higher surface heat flow than stable continental cratons because hot asthenospheric material rises close to the surface at ridges."
  type: true-false
  answer: true
  explanation: "True. At mid-ocean ridges, upwelling mantle material reaches within a few kilometers of the seafloor, driving heat flow well above 150 mW/m² (though much is carried by hydrothermal circulation rather than pure conduction). Stable cratons like the Canadian Shield have thick, cold lithospheric roots that insulate the surface from deep heat, giving values of only 30–50 mW/m². This dramatic range reflects the fundamental difference in lithospheric thermal structure between tectonically active and ancient stable regions."

- question: "Explain why two boreholes with identical temperature gradients can have very different surface heat flow values, and what additional measurement is required to resolve the difference."
  type: short-answer
  answer: "The temperature gradient (dT/dz) is only one factor in the heat flow equation q = κ × dT/dz. The other factor is thermal conductivity (κ), which varies substantially among rock types — granite has much higher conductivity than shale or mudstone. Two sites with the same gradient but different rock types will have different heat flows. To resolve the difference, rock cores from each borehole must be analyzed in the laboratory to measure thermal conductivity. Heat flow is then computed as the product of the measured gradient and the measured conductivity."
  explanation: "This is the central practical challenge of heat flow measurement and why it requires both a borehole temperature survey and a separate petrophysical measurement. High-conductivity rocks like quartzite transmit heat efficiently even at low gradients; low-conductivity rocks like organic shale retain more heat and steepen the gradient at the same flux. Geothermal surveys that neglect conductivity variation systematically misinterpret temperature gradients as heat flow."
```

## Explainer

You already understand that Earth's interior is hot and that temperature increases with depth — the geothermal gradient. You also know that different rock types conduct heat at different rates — thermal conductivity. Heat flow measurement brings these two concepts together into a single, quantitative measure of how much thermal energy is escaping through the surface at any given location. The fundamental equation is deceptively simple: **q = κ × dT/dz**, where q is heat flow in watts per square meter, κ is the thermal conductivity of the rock, and dT/dz is the temperature gradient measured in a borehole. Multiply how fast temperature rises with depth by how efficiently the rock conducts heat, and you get the rate of energy loss through the surface.

In practice, making this measurement requires drilling a borehole — or using an existing one — and lowering a temperature probe to record temperatures at multiple depths. The resulting **temperature-depth profile** ideally shows a steady, linear increase with depth once you get below the zone affected by seasonal surface temperature fluctuations (typically the upper 10–20 meters). The slope of this linear portion is the geothermal gradient, commonly expressed in °C per kilometer. Typical values range from about 20°C/km in old, stable continental interiors to 40°C/km or more in tectonically active regions. Separately, core samples from the borehole are brought to the laboratory and their **thermal conductivity** is measured, usually with a divided-bar apparatus or needle-probe method. The product of gradient and conductivity gives the heat flow.

Interpreting heat flow measurements requires understanding what controls the thermal energy budget at different locations. Earth's internal heat comes from two main sources: **radiogenic heat production** from the decay of uranium, thorium, and potassium concentrated in crustal rocks, and **primordial heat** left over from planetary formation and core crystallization flowing up from the mantle. In old, thick continental crust like the Canadian Shield or West African Craton, the crust has been stable for billions of years, radiogenic elements have decayed substantially, and heat flow is low — roughly 30–50 mW/m². At mid-ocean ridges, hot mantle material rises to within a few kilometers of the surface, and heat flow exceeds 150 mW/m² (though much of this is actually carried by hydrothermal circulation rather than pure conduction, complicating the measurement). Continental rift zones and volcanic arcs show elevated values for similar reasons — thinned lithosphere and shallow hot material.

The global pattern of heat flow measurements, compiled from thousands of boreholes and ocean-floor probes, reveals the thermal structure of the lithosphere and provides essential constraints for models of mantle convection, lithospheric cooling, and tectonic processes. Anomalously high heat flow can indicate geothermal energy potential, recent magmatic activity, or thinning crust. Anomalously low values may signal thick, cold lithospheric roots beneath ancient cratons. These measurements are the empirical foundation upon which conduction models and thermal evolution studies are built.
