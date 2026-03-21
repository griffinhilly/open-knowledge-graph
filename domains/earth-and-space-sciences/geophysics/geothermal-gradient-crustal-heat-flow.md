---
id: geothermal-gradient-crustal-heat-flow
title: Geothermal Gradient and Crustal Heat Flow
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: earth-interior-structure
  type: hard
builds-toward:
- thermal-conductivity-and-rocks
- thermochronology-and-cooling-ages
- rock-rheology-elastic-plastic-deformation
- mantle-convection-and-dynamics
tags:
- heat-flow
- geothermal-gradient
- thermal-properties
- interior-heat
stage: advanced
status: draft
---

# Geothermal Gradient and Crustal Heat Flow

## Core Idea
The geothermal gradient (dT/dz) is typically 25–30 K/km in stable continental crust but varies with crustal thickness, composition, and age. Heat flow q = −k(dT/dz) depends on thermal conductivity k; high heat flows mark mid-ocean ridges and hot-spots, while low flows occur in cold subducting slabs. The global heat budget is dominated by mantle convection, radiogenic heat from the core and mantle, and cooling of the lithosphere away from spreading centers.

## Questions

```yaml
- question: "A borehole in region A shows a geothermal gradient of 40 K/km. A borehole in region B shows a gradient of 20 K/km. A geophysicist says region A has higher heat flow. Is this necessarily correct?"
  type: multiple-choice
  options:
    - "Yes — a steeper gradient always means more heat is flowing through the crust"
    - "No — heat flow depends on both the gradient and the thermal conductivity of the rock: q = −k(dT/dz)"
    - "Yes — gradient and heat flow are always proportional in crustal rocks"
    - "No — heat flow depends only on the age of the lithosphere, not the temperature gradient"
  answer: 1
  explanation: "Heat flow is q = −k(dT/dz), where k is thermal conductivity. A high gradient in rock with low thermal conductivity (e.g., shale, k ≈ 1–2 W/m·K) can produce the same or lower heat flow than a moderate gradient in rock with high conductivity (e.g., quartzite, k ≈ 5–7 W/m·K). Measuring both a temperature profile (for the gradient) and rock thermal conductivity is required to determine actual heat flow. The misconception of treating gradient as equivalent to heat flow is the most common error in geothermal analysis."

- question: "Mid-ocean ridges have the highest surface heat flow on Earth. As oceanic lithosphere ages and moves away from the ridge, what happens to its heat flow and why?"
  type: multiple-choice
  options:
    - "Heat flow increases because the lithosphere thickens, trapping more heat"
    - "Heat flow stays constant — the plate moves laterally, not vertically, so depth to mantle is unchanged"
    - "Heat flow decreases because the lithosphere cools conductively, increasing the distance between hot mantle and the surface"
    - "Heat flow decreases because radioactive element concentrations decay over millions of years"
  answer: 2
  explanation: "At the ridge, hot mantle material rises close to the seafloor, producing very high heat flow (often >200 mW/m²). As the plate moves away and ages, the lithosphere thickens and cools conductively — the thermal boundary layer grows, increasing the distance across which heat must diffuse. This cooling is so predictable that heat flow as a function of plate age follows a well-known curve: roughly proportional to 1/√(age). Option D confuses radioactive decay timescales (billions of years) with plate cooling timescales (tens of millions of years)."

- question: "The geothermal gradient and heat flow measure the same physical quantity expressed in different units."
  type: true-false
  answer: false
  explanation: "They are fundamentally different quantities. The geothermal gradient (dT/dz) is a temperature gradient — it measures how temperature changes with depth, in units of K/km or °C/m. Heat flow (q) is an energy flux — it measures the rate of thermal energy transfer per unit area per unit time, in units of mW/m². The relationship between them requires thermal conductivity k: q = −k(dT/dz). A high gradient in an insulating rock and a low gradient in a conducting rock can produce equal heat flows. Confusing the two leads to incorrect comparisons between regions with different rock types."

- question: "Continental crust can have higher heat flow than oceanic crust of the same age, partly because granitic rocks contain radioactive elements that generate heat within the crust itself."
  type: true-false
  answer: true
  explanation: "This is correct. Granitic upper continental crust is enriched in uranium (U), thorium (Th), and potassium (K) relative to oceanic basalt. These radioactive elements decay and produce heat within the crust — a process called radiogenic heat production. This means that a significant fraction of continental surface heat flow originates within the crust itself, rather than arriving from the mantle below. Oceanic crust (basaltic composition) has lower radiogenic element concentrations, so most of its heat flow comes from below — from the mantle and deep thermal structure. This compositional difference is why the heat flow budget varies between continental and oceanic settings independently of lithospheric age."

- question: "Why is measuring the geothermal gradient alone insufficient to determine how much thermal energy is flowing through the crust, and what additional measurement is required?"
  type: short-answer
  answer: "The geothermal gradient tells you how fast temperature increases with depth, but not how efficiently the rock transmits heat. To find heat flow (the rate of energy transfer per unit area), you need to apply Fourier's law: q = −k(dT/dz), where k is the thermal conductivity of the rock. Different rock types have very different conductivities — quartzite conducts heat roughly 5–7 times better than shale. A steep gradient in poor-conducting shale might produce the same heat flow as a gentle gradient in well-conducting quartzite. Borehole heat flow studies therefore require both a downhole temperature profile (for the gradient) and core sample analysis to measure thermal conductivity at each depth."
  explanation: "This is why heat flow measurements are more geophysically informative than temperature measurements alone, and why they are also harder to make. The gradient is measurable with a thermometer in a borehole; the conductivity requires laboratory measurements on rock samples. In practice, geophysicists combine both into the single number q (in mW/m²) that enables global comparisons across different geological settings."
```

## Explainer

You already know from studying Earth's interior structure that temperature increases with depth — the core is far hotter than the surface. The **geothermal gradient** quantifies this increase: it is the rate of temperature change with depth, typically expressed in degrees per kilometer. In stable continental crust, this gradient averages about 25–30 K/km, meaning that for every kilometer you descend into a mine or borehole, the temperature rises by roughly 25–30°C. But this average hides enormous variation. Near mid-ocean ridges, where hot mantle material rises close to the surface, the gradient can exceed 100 K/km. In old, cold continental shield regions, it may drop below 15 K/km.

The geothermal gradient alone tells you how fast temperature changes with depth, but to understand how much thermal energy is actually flowing through the crust, you need **heat flow**. Heat flow (q) relates the gradient to the rock's ability to conduct heat through Fourier's law: q = −k(dT/dz), where k is the **thermal conductivity** of the rock. A high gradient in a poor conductor might produce the same heat flow as a low gradient in an excellent conductor. Measuring heat flow requires both a temperature profile from a borehole and knowledge of the thermal conductivity of the rocks encountered — this is why heat flow measurements are more informative than temperature readings alone.

Earth's surface heat flow averages about 87 mW/m², but the pattern is far from uniform. The highest heat flows occur at mid-ocean ridges (often exceeding 200 mW/m²), where new lithosphere is being created and hot mantle material is close to the seafloor. As oceanic lithosphere ages and moves away from the ridge, it cools conductively and heat flow decreases — 50-million-year-old ocean floor typically shows about 50–60 mW/m². This cooling relationship is so predictable that it forms the basis of thermal models of oceanic lithosphere. On continents, heat flow varies with the concentration of **radiogenic elements** — uranium, thorium, and potassium — in crustal rocks. Granitic upper continental crust is enriched in these elements, so continental heat flow has a significant contribution from radioactive decay within the crust itself, unlike oceanic crust where most heat comes from below.

Understanding crustal heat flow matters for everything from predicting the depth at which rocks become ductile rather than brittle (which controls earthquake depth), to estimating the thermal maturity of sedimentary basins for petroleum exploration, to evaluating geothermal energy potential. The global heat budget — roughly 46 terawatts total — is powered by two main sources: primordial heat left over from Earth's formation and ongoing radiogenic heating. Mantle convection is the dominant mechanism for transporting this heat from the deep interior to the base of the lithosphere, where conduction takes over for the final journey to the surface. This thermal framework connects your knowledge of Earth's interior to the surface processes and tectonic features that the thermal regime ultimately controls.
