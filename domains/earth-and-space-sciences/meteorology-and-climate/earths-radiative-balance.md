---
id: earths-radiative-balance
title: Earth's Radiative Balance and Energy Budget
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: solar-radiation-and-earth-energy-balance
  type: hard
- id: greenhouse-effect
  type: soft
- id: thermal-structure-of-atmosphere
  type: soft
builds-toward:
- climate-change-science
- climate-feedbacks-and-sensitivity
- radiative-forcing-greenhouse-gases
tags:
- radiation
- balance
- energy-budget
- solar
- terrestrial
stage: formal-systems
status: validated
---

# Earth's Radiative Balance and Energy Budget

## Core Idea
Earth's climate is controlled by the balance between incoming solar radiation and outgoing terrestrial radiation. The atmosphere is partially transparent to incoming sunlight but absorbs and re-radiates outgoing infrared radiation back to the surface, creating the natural greenhouse effect that makes Earth habitable. An imbalance where more radiation is absorbed than escapes (due to increased greenhouse gases) leads to net warming; understanding this budget is fundamental to climate science.

## Questions

```yaml
- question: "If atmospheric greenhouse gas concentrations increase, which sequence of events correctly explains the resulting surface warming?"
  type: multiple-choice
  options:
    - "More sunlight reaches the surface because greenhouse gases reduce cloud cover and increase transparency to solar radiation"
    - "Greenhouse gases raise the effective emission height to a colder altitude, temporarily reducing outgoing infrared radiation, creating a radiative imbalance that drives warming until a new equilibrium is reached"
    - "The surface albedo decreases as ice melts, absorbing more incoming solar radiation — this is the primary warming mechanism"
    - "Greenhouse gas molecules emit infrared radiation directly toward the surface, which heats the ground independently of the solar input"
  answer: 1
  explanation: "The correct mechanistic chain: greenhouse gases absorb outgoing infrared emitted by the surface and re-radiate it. Adding more gases raises the altitude (effective emission height) from which the planet radiates to space. Higher altitude means colder temperature; colder temperature means less infrared emitted (Stefan-Boltzmann law). Temporarily, outgoing radiation drops below ~240 W/m² while incoming solar is unchanged — a radiative imbalance. Earth then warms until the emission-height temperature rises enough to restore the required outgoing flux. Option A confuses greenhouse gases with albedo; option C describes a feedback, not the primary mechanism."

- question: "Earth without any atmosphere would have a surface temperature near −18°C instead of the observed +15°C. What accounts for the ~33°C difference?"
  type: multiple-choice
  options:
    - "The troposphere absorbs incoming solar radiation and warms the surface through conduction and convection"
    - "Ocean currents redistribute latent heat from tropics to poles, raising the global average"
    - "Greenhouse gases absorb outgoing infrared and re-radiate some of it back toward the surface as downwelling longwave radiation, adding a second energy input beyond direct sunlight"
    - "Earth's albedo without an atmosphere would be higher due to ice coverage, reflecting more sunlight and paradoxically warming the surface"
  answer: 2
  explanation: "The natural greenhouse effect adds downwelling longwave radiation as a second energy input to the surface. Without the atmosphere, the surface must balance absorbed solar (~240 W/m²) alone, yielding ~−18°C. With greenhouse gases, the atmosphere intercepts outgoing infrared and re-radiates some back toward the ground. The surface now receives solar plus downwelling longwave, so it warms to ~+15°C where its own emission balances the combined input. This 33°C enhancement is the natural greenhouse effect, without which liquid water and life would be impossible."

- question: "At radiative equilibrium, the amount of solar radiation Earth absorbs must equal the amount of infrared radiation Earth emits to space."
  type: true-false
  answer: true
  explanation: "This is the definition of radiative equilibrium. Earth absorbs roughly 240 W/m² of incoming solar radiation (after accounting for ~30% albedo reflection). At steady state, exactly 240 W/m² of outgoing longwave radiation must escape to space. Any imbalance — more in than out, or vice versa — drives temperature change until equilibrium is restored. This energy balance is the fundamental constraint governing Earth's long-term mean temperature."

- question: "Adding greenhouse gases to the atmosphere warms Earth by increasing the amount of solar (shortwave) radiation that reaches the surface."
  type: true-false
  answer: false
  explanation: "Greenhouse gases are largely transparent to incoming shortwave (visible) solar radiation — they do not redirect sunlight toward the surface. They work by absorbing *outgoing* longwave (infrared) radiation emitted by the warm surface and re-radiating it in all directions, including back downward. The warming mechanism is therefore about reducing how efficiently infrared escapes to space, not about increasing the solar input arriving at the surface. Confusing these mechanisms is one of the most common misconceptions about the greenhouse effect."

- question: "Why does raising the effective emission height cause Earth's surface temperature to increase?"
  type: short-answer
  answer: "The effective emission height is the altitude from which Earth radiates infrared to space. Higher altitudes are colder (following the environmental lapse rate). Because infrared emission depends on temperature (Stefan-Boltzmann law: emission ∝ T⁴), a colder emission level radiates less energy to space. When greenhouse gases raise this height, outgoing radiation temporarily falls below the ~240 W/m² needed to balance incoming solar — more energy arrives than escapes. Earth then warms until the emission-level temperature rises enough to restore the required outgoing flux, which requires a higher surface temperature throughout the atmospheric column."
  explanation: "This chain — higher emission height → colder emission → reduced outgoing flux → warming until new equilibrium — is the fundamental mechanism of greenhouse-gas-driven climate change. Understanding it requires connecting altitude, temperature lapse rate, and Stefan-Boltzmann emission, which is why the effective emission height concept is central to quantitative climate science."
```

## Explainer

From your study of solar radiation and Earth's energy balance, you know that the Sun delivers about 1,361 watts per square meter to the top of the atmosphere (the **solar constant**). But Earth is a sphere, so this energy is spread over four times the area that intercepts it, giving an average input of roughly 340 W/m². Of this incoming shortwave radiation, about 30% is immediately reflected back to space by clouds, ice, and bright surfaces — this fraction is Earth's **albedo**. The remaining ~240 W/m² is absorbed by the surface and atmosphere, warming the planet. For Earth's temperature to remain stable, exactly 240 W/m² must be radiated back to space as outgoing longwave (infrared) radiation. When incoming and outgoing fluxes balance, the planet is in **radiative equilibrium**.

If Earth had no atmosphere, this balance would produce a surface temperature of about −18°C — far too cold for liquid water. The reason our actual average surface temperature is around +15°C is the **greenhouse effect**, which you encountered as a prerequisite. The atmosphere is largely transparent to incoming solar radiation (visible light passes through easily), but greenhouse gases — water vapor, CO₂, methane, and others — absorb outgoing infrared radiation emitted by the warm surface. These gases then re-radiate energy in all directions, including back toward the ground. This **downwelling longwave radiation** is an additional energy input to the surface beyond direct sunlight, raising the surface temperature by about 33°C above what bare radiative equilibrium would predict.

The full energy budget includes more than just radiation. The surface also loses energy through **latent heat flux** (evaporation of water, which carries energy into the atmosphere where it is released during condensation) and **sensible heat flux** (direct warming of air in contact with the ground). These non-radiative transfers move about 100 W/m² from surface to atmosphere, which is why the surface radiative budget alone would overestimate surface warming. The atmosphere, in turn, radiates this energy to space from its upper layers. The key insight is that the planet radiates to space primarily from an **effective emission height** several kilometers up, where the temperature is cold enough to emit the required 240 W/m². Adding greenhouse gases raises this emission height, where it is colder, temporarily reducing outgoing radiation and creating a **radiative imbalance** — more energy comes in than goes out, and the system warms until a new equilibrium is reached at a higher temperature. This is the fundamental mechanism of anthropogenic climate change: human emissions shift the radiative balance, and Earth's temperature adjusts until outgoing radiation once again matches incoming.
