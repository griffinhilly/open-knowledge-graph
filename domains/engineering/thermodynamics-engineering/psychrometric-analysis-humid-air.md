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
stage: advanced
status: draft
---

# Psychrometric Analysis and Humid Air Properties

## Core Idea
Humid air is a mixture of dry air and water vapor; key properties are dry-bulb temperature, wet-bulb temperature, relative humidity, dew point, and humidity ratio. The psychrometric chart plots these interrelationships and enables rapid analysis of HVAC processes: heating, cooling, humidification, and dehumidification. Accurate calculations use ideal-gas approximations and water saturation properties.

## Explainer

From your work with Dalton's law and gas mixtures, you know that the total pressure of a gas mixture equals the sum of each component's partial pressure. Humid air is a binary mixture: dry air and water vapor, each contributing its partial pressure to the total atmospheric pressure (~101.3 kPa). Psychrometrics is the application of mixture thermodynamics to this specific, practically ubiquitous mixture — the air you breathe, condition, and work with in HVAC and industrial processes.

The most important quantity is the **humidity ratio** ω (also called specific humidity): the mass of water vapor per kilogram of dry air. It determines how much moisture the air actually carries. Related but different is **relative humidity** φ: the ratio of the actual partial pressure of water vapor to the saturation pressure at the current temperature. When φ = 100%, the air is saturated — it is holding all the water vapor it can at that temperature. The **dew point** is the temperature at which your air would reach saturation if cooled at constant pressure; below this temperature, water condenses out.

The **wet-bulb temperature** (measured by a thermometer with a wet wick exposed to airflow) is lower than the **dry-bulb temperature** (ordinary thermometer) because evaporation from the wick cools it. The wet-bulb depression (dry-bulb minus wet-bulb) is proportional to how dry the air is — desert air shows a large depression; saturated air shows zero depression because no evaporation occurs. These two temperatures together uniquely specify the state of humid air, which is why standard weather reports often give them. The **psychrometric chart** encodes all five of these properties simultaneously: fixing any two of {dry-bulb, wet-bulb, dew point, relative humidity, humidity ratio} determines the rest.

Tracing HVAC processes on the psychrometric chart makes the physics visual. Sensible heating (turning on a furnace with no added moisture) moves horizontally rightward — temperature rises, but humidity ratio is unchanged. Cooling below the dew point moves along the saturation curve as moisture condenses out — this is how air conditioners dehumidify. Humidification (adding steam) moves upward — humidity ratio increases at roughly constant temperature. Adiabatic saturation (spraying water into airflow) moves along lines of constant wet-bulb temperature toward saturation. Each of these processes involves an energy balance on the air-water system, and the enthalpy values read from the chart let you calculate heating and cooling loads directly.
