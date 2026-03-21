---
id: crustal-age-and-cooling-curves
title: Oceanic Crustal Cooling and Age Relationships
domain: earth-and-space-sciences
course: geophysics
prerequisites:
- id: mid-ocean-ridge-dynamics-and-geophysics
  type: hard
- id: heat-flow-conduction-steady-state
  type: hard
builds-toward:
- lithosphere-thickness-and-age
tags:
- geothermics
- plate-tectonics
- cooling
stage: advanced
status: draft
---

# Oceanic Crustal Cooling and Age Relationships

## Core Idea
Oceanic crust cools as it moves away from mid-ocean ridges following a half-space cooling model. Crustal thickness, heat flow, bathymetry, and seismic velocity all change predictably with age. The relationship between bathymetry and age (approximately 2600 m for young crust, increasing to 6000 m by 80 Ma) is a fundamental constraint on plate tectonics and mantle potential temperature.

## Questions

```yaml
- question: "Two sections of ocean floor are measured: one 25 Ma old and one 100 Ma old. According to the half-space cooling model, what is the approximate ratio of their seafloor depths below the ridge crest?"
  type: multiple-choice
  options:
    - "4:1 — the 100 Ma crust is four times deeper, because depth scales linearly with age"
    - "2:1 — the 100 Ma crust is about twice as deep, because depth scales as the square root of age"
    - "10:1 — the 100 Ma crust is ten times deeper, because older crust has lost far more heat"
    - "1:1 — depths are nearly equal, because most seafloor subsidence occurs in the first 10 Ma"
  answer: 1
  explanation: "The half-space cooling model predicts depth ∝ √(age). The ratio of depths is √100 / √25 = 10 / 5 = 2. The 100 Ma crust is about twice as deep as the 25 Ma crust. Option A (4:1) would be correct for a linear relationship. The square-root scaling is the hallmark of diffusive cooling: the thermal boundary layer thickens as √(κt), and the resulting isostatic subsidence follows the same dependence. This prediction was one of the first quantitative confirmations of plate tectonics — observed ocean depth profiles across multiple basins matched the √t curve."

- question: "Very old oceanic crust (>80 Ma) is consistently observed to be shallower than the half-space cooling model predicts. The best explanation for this systematic deviation is:"
  type: multiple-choice
  options:
    - "Hydrothermal circulation cools old crust more efficiently than young crust, paradoxically causing anomalous uplift"
    - "The lithosphere approaches a finite equilibrium thickness because of heat supplied from the underlying asthenosphere, preventing it from cooling indefinitely"
    - "Old crust becomes less dense over millions of years as iron is lost through seafloor weathering and alteration"
    - "The seafloor stops subsiding once it reaches isostatic equilibrium with the surrounding mantle at about 80 Ma"
  answer: 1
  explanation: "The half-space model assumes the lithosphere cools into an infinite half-space with no lower boundary. But old lithosphere is systematically shallower and warmer than this predicts — the cooling curve flattens. The plate model explains this by adding a lower thermal boundary condition: the base of the lithosphere is maintained at approximately mantle temperature by heat from the underlying asthenosphere (possibly via small-scale convection or radiogenic heating). This prevents the plate from growing thicker than ~125 km and causes the age-depth relationship to flatten for crust older than ~70–80 Ma. The plate model replaces the half-space model for old ocean floor."

- question: "Both seafloor heat flow and ocean depth can be predicted from crustal age alone using the half-space cooling model, because both observables arise from the same underlying thermal diffusion process."
  type: true-false
  answer: true
  explanation: "The half-space model provides a unified thermal picture connecting multiple independent observables to a single variable: age. Surface heat flow = κ × (temperature gradient) ∝ 1/√(age) — highest at the ridge, declining steadily. Ocean depth ∝ √(age) — shallowest at the ridge, deepening as the lithosphere cools, contracts, and isostatically subsides. Both predictions follow from the same one-dimensional heat conduction solution with identical parameters. This predictive unity — one physical model, two independent observables both confirmed — was enormously compelling evidence for plate tectonics in the 1960s–70s."

- question: "Under the half-space cooling model, the oceanic lithosphere (thermal boundary layer) grows thicker at a rate proportional to age — so lithosphere that is 4× older is 4× thicker."
  type: true-false
  answer: false
  explanation: "The thermal boundary layer grows as the square root of age: thickness ∝ √(κt). Lithosphere that is 4× older is only 2× thicker (√4 = 2). This square-root dependence is the universal signature of diffusive heat transport — heat spreads as √(Dt) in one dimension because diffusion slows as the temperature gradient decreases over time. Linear growth (4× older → 4× thicker) would require a constant rate of thickening, which is impossible by diffusion. Recognizing the √t signature distinguishes diffusive from advective processes and is the key to interpreting seafloor cooling observations."

- question: "Why does the half-space cooling model predict that seafloor depth increases as the square root of crustal age, and what physical process underlies this relationship?"
  type: short-answer
  answer: "As oceanic crust moves away from the mid-ocean ridge, it cools by conductive heat loss to the overlying ocean. The thermal diffusion equation governs this cooling: the depth to which cooling penetrates grows as √(κt), where κ is thermal diffusivity and t is time since crust formed. This thickening, cooler lithosphere is denser than the underlying asthenosphere, so it isostatically subsides — the denser column sinks deeper. Because the thermally controlled density excess ∝ thickness ∝ √t, the depth below the ridge also grows as √t. The square-root dependence is not specific to geophysics; it is the universal signature of one-dimensional diffusion."
  explanation: "Connecting the observation (bathymetric depth increasing with age) to the physical mechanism (diffusive cooling creating a dense boundary layer that sinks isostatically) is the key conceptual step. The √t scaling appears in every diffusion problem — heat conduction, mass diffusion, chemical diffusion — whenever a boundary condition is applied at one face of a semi-infinite medium. Recognizing this universality allows the geophysical result to be placed in a much broader physical context."
```

## Explainer

From your study of mid-ocean ridges, you know that new oceanic crust forms at spreading centers where hot mantle material rises, partially melts, and solidifies. From heat flow and conduction, you know that thermal energy moves through rock by conduction at a rate governed by thermal diffusivity. These two ideas combine into one of the most elegant quantitative relationships in geophysics: the **half-space cooling model**, which predicts how oceanic lithosphere evolves as it moves away from the ridge.

The model treats the newly formed crust as a semi-infinite half-space initially at mantle temperature (~1300°C at the surface), cooling from above into a zero-temperature ocean. The mathematics is identical to the one-dimensional heat conduction problem you solved in your thermal physics prerequisite. The key result is that the thermal boundary layer — the cooled lithosphere — thickens as the **square root of age**: thickness ∝ √(κt), where κ is thermal diffusivity and t is the time since the crust formed at the ridge. This square-root dependence is the signature of diffusive cooling and appears in every observable property of the aging ocean floor.

As the lithosphere cools, it contracts and becomes denser, causing the seafloor to **subside**. The predicted depth increases as the square root of crustal age: young crust near the ridge sits at roughly 2,600 m depth, while 80-million-year-old crust has sunk to about 5,500–6,000 m. This √t relationship between bathymetry and age was one of the first great confirmations of plate tectonics — it matched observed ocean depth profiles across every major basin. Heat flow measurements tell the same story from the thermal side: surface heat flow decreases as 1/√t, highest at the ridge and declining steadily with age.

The half-space model works remarkably well for crust younger than about 70–80 Ma, but older ocean floor is systematically shallower and warmer than predicted. This **flattening** of the cooling curve led to the development of the **plate model**, which assumes the lithosphere approaches a finite equilibrium thickness (~125 km) rather than cooling indefinitely. The plate model adds a lower thermal boundary condition — heat supply from the underlying asthenosphere — that prevents the lithosphere from growing thicker than observed. Whether this heat comes from small-scale convection beneath old plates or from radiogenic heating remains debated, but the empirical flattening is robust. Together, the half-space and plate models provide the quantitative framework connecting crustal age to nearly every measurable property of the ocean floor: depth, heat flow, seismic velocity, and elastic thickness.
