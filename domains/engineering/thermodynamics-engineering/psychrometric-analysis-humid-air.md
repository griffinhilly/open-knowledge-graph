---
id: psychrometric-analysis-humid-air
title: Psychrometric Analysis and Humid Air Properties
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: psychrometrics-humid-air-properties
  type: hard
- id: gas-mixture-thermodynamics-daltons
  type: soft
builds-toward:
- humid-air-thermodynamic-properties
- combustion-stoichiometry-energy-release
tags:
- psychrometrics
- humid-air
- properties
- charts
stage: formal-systems
status: validated
---

# Psychrometric Analysis and Humid Air Properties

## Core Idea
Humid air is a mixture of dry air and water vapor; key properties are dry-bulb temperature, wet-bulb temperature, relative humidity, dew point, and humidity ratio. The psychrometric chart plots these interrelationships and enables rapid analysis of HVAC processes: heating, cooling, humidification, and dehumidification. Accurate calculations use ideal-gas approximations and water saturation properties.

## Questions

```yaml
- question: "A room contains air at 20°C with a relative humidity of 60%. A furnace heats the air to 30°C without adding any moisture. What happens to the relative humidity and the humidity ratio?"
  type: multiple-choice
  options:
    - "Relative humidity increases; humidity ratio increases — warming air draws moisture from walls"
    - "Relative humidity decreases; humidity ratio stays constant — warmer air can hold more vapor, but actual vapor content is unchanged"
    - "Relative humidity stays constant; humidity ratio increases — heating proportionally raises both"
    - "Both decrease — high temperature drives moisture out of the air stream"
  answer: 1
  explanation: "Humidity ratio ω (mass of water vapor per kg of dry air) is conserved when no moisture is added or removed — sensible heating only changes temperature. However, relative humidity φ = p_w / p_sat(T): since saturation pressure p_sat increases strongly with temperature (roughly doubles every ~10°C), the same partial pressure of water vapor now represents a smaller fraction of the new saturation pressure. So φ falls. On the psychrometric chart, sensible heating moves horizontally rightward — temperature increases while the horizontal humidity-ratio axis is unchanged. This is the fundamental reason why indoor winter air feels so dry: outdoor cold air with moderate RH is brought inside and heated, drastically dropping its relative humidity."

- question: "An air conditioning unit cools warm humid air. The air first cools sensibly, then the coil surface temperature drops below the air's dew point. On the psychrometric chart, which sequence of paths describes this process?"
  type: multiple-choice
  options:
    - "First moves horizontally leftward (T decreases, ω constant), then curves down along the saturation curve as condensation begins"
    - "Moves vertically downward throughout — temperature and humidity ratio both drop proportionally during cooling"
    - "Moves diagonally toward the origin — both temperature and relative humidity decrease simultaneously"
    - "Moves horizontally leftward throughout — temperature decreases but humidity ratio is always conserved during cooling"
  answer: 0
  explanation: "Cooling below the dew point happens in two stages. Before the dew point is reached, cooling is sensible: temperature falls but no condensation occurs, so humidity ratio is constant — the process moves horizontally leftward on the chart. Once temperature hits the dew point (where φ = 100%), the air is saturated. Further cooling forces condensation: liquid water drips off the cooling coil, removing moisture from the air stream. The air state now follows the saturation curve (φ = 100%) downward as both temperature and humidity ratio decrease together. This two-stage process explains why air conditioners both cool AND dehumidify — the dehumidification only begins after the dew point is crossed."

- question: "High relative humidity usually indicates that the air contains a large mass of water vapor per kilogram of dry air."
  type: true-false
  answer: false
  explanation: "False. Relative humidity tells you how close the air is to saturation at its current temperature, not the absolute amount of moisture. Cold saturated air (100% RH at 0°C) contains only about 3.8 g of water vapor per kg of dry air. Warm air at 30°C with just 50% RH contains about 13.4 g/kg — more than three times as much moisture as the cold saturated air. This distinction matters enormously in HVAC and meteorology: cold winter air is often nearly saturated (high RH) yet carries very little moisture mass; tropical air at moderate RH carries enormous amounts. Humidity ratio, not relative humidity, is the quantity that tracks actual moisture content."

- question: "When the dry-bulb temperature equals the wet-bulb temperature of an air sample, the relative humidity of that air is 100%."
  type: true-false
  answer: true
  explanation: "True. The wet-bulb thermometer reading is suppressed below the dry-bulb temperature by evaporative cooling — the faster water evaporates from the wet wick, the greater the cooling effect. Evaporation rate depends on how far the ambient air is from saturation: dry air evaporates quickly (large wet-bulb depression); air already near saturation evaporates slowly. When the air is fully saturated (φ = 100%), no net evaporation from the wick can occur — the air cannot accept any more moisture — so the wick temperature equals the ambient dry-bulb temperature. The wet-bulb depression (dry-bulb minus wet-bulb) is therefore zero if and only if the air is saturated."

- question: "Explain the difference between relative humidity and humidity ratio, and describe a situation where one is high while the other is low."
  type: short-answer
  answer: "Humidity ratio (ω) is the mass of water vapor per kilogram of dry air — it measures actual moisture content. Relative humidity (φ) is the ratio of actual water vapor pressure to saturation vapor pressure at the current temperature — it measures how close the air is to its moisture-holding limit. A clear example where RH is high but ω is low: cold outdoor air at −5°C at 90% RH contains only ~2.5 g/kg of water vapor. A clear example where ω is high but RH is low: tropical air at 35°C with 40% RH contains about 14 g/kg — far more moisture mass, yet well below saturation. Heating cold saturated air indoors takes it from high-RH/low-ω to low-RH/low-ω (unchanged ω, decreased RH)."
  explanation: "This distinction is fundamental to HVAC design and human comfort. Comfort is related more to ω than to φ — what matters for evaporative cooling of the human body is the actual vapor pressure gradient between skin and air, which depends on absolute moisture content. But mold growth and condensation risks depend on φ relative to surface temperatures. An HVAC engineer must track both: the psychrometric chart encodes them simultaneously, which is why it is the central design tool for air conditioning and ventilation analysis."
```

## Explainer

From your work with Dalton's law and gas mixtures, you know that the total pressure of a gas mixture equals the sum of each component's partial pressure. Humid air is a binary mixture: dry air and water vapor, each contributing its partial pressure to the total atmospheric pressure (~101.3 kPa). Psychrometrics is the application of mixture thermodynamics to this specific, practically ubiquitous mixture — the air you breathe, condition, and work with in HVAC and industrial processes.

The most important quantity is the **humidity ratio** ω (also called specific humidity): the mass of water vapor per kilogram of dry air. It determines how much moisture the air actually carries. Related but different is **relative humidity** φ: the ratio of the actual partial pressure of water vapor to the saturation pressure at the current temperature. When φ = 100%, the air is saturated — it is holding all the water vapor it can at that temperature. The **dew point** is the temperature at which your air would reach saturation if cooled at constant pressure; below this temperature, water condenses out.

The **wet-bulb temperature** (measured by a thermometer with a wet wick exposed to airflow) is lower than the **dry-bulb temperature** (ordinary thermometer) because evaporation from the wick cools it. The wet-bulb depression (dry-bulb minus wet-bulb) is proportional to how dry the air is — desert air shows a large depression; saturated air shows zero depression because no evaporation occurs. These two temperatures together uniquely specify the state of humid air, which is why standard weather reports often give them. The **psychrometric chart** encodes all five of these properties simultaneously: fixing any two of {dry-bulb, wet-bulb, dew point, relative humidity, humidity ratio} determines the rest.

Tracing HVAC processes on the psychrometric chart makes the physics visual. Sensible heating (turning on a furnace with no added moisture) moves horizontally rightward — temperature rises, but humidity ratio is unchanged. Cooling below the dew point moves along the saturation curve as moisture condenses out — this is how air conditioners dehumidify. Humidification (adding steam) moves upward — humidity ratio increases at roughly constant temperature. Adiabatic saturation (spraying water into airflow) moves along lines of constant wet-bulb temperature toward saturation. Each of these processes involves an energy balance on the air-water system, and the enthalpy values read from the chart let you calculate heating and cooling loads directly.
