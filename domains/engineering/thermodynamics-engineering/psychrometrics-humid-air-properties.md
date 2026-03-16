---
id: psychrometrics-humid-air-properties
title: Psychrometrics and Humid Air Properties
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: pure-substance-phase-diagrams
  type: hard
tags:
- psychrometrics
- humid-air
- HVAC
stage: advanced
status: draft
---

# Psychrometrics and Humid Air Properties

## Core Idea
Psychrometrics deals with moist air properties: humidity ratio, relative humidity, dew point, and enthalpy. The psychrometric chart graphically displays these relationships for air at constant pressure and is the primary design tool for HVAC systems. Processes like sensible heating, cooling with dehumidification, and adiabatic saturation (evaporative cooling) are readily visualized and analyzed on the chart.

## How It's Best Learned
Use the psychrometric chart to trace processes for HVAC equipment: cooling coils (temperature and humidity decrease), heating (temperature increases, humidity ratio constant), humidification, and dehumidification. Memorize key definitions: relative humidity φ = P_v / P_sat, dew point (temperature at saturation), and wet-bulb temperature (cooling limit in adiabatic saturation). Practice reading chart scales to extract properties for detailed analysis.

## Common Misconceptions
- Humid air enthalpy includes only sensible heat of air; humid air enthalpy includes latent heat of water vapor.
- Higher humidity always means higher water vapor density; relative humidity accounts for saturation pressure variation with temperature.
- Cooling air below its dew point always causes condensation; condensation occurs only if the air is cooled to or below dew point, removing water from the air stream.

## Explainer

From your study of pure substance phase diagrams, you know that water can exist as a liquid, a vapor, or a two-phase mixture depending on temperature and pressure. Psychrometrics applies exactly this framework to the mixture of dry air and water vapor that constitutes the atmosphere. The key insight is that at normal atmospheric conditions, air and water vapor behave nearly as ideal gases — they share the total pressure but each occupies the full volume, consistent with Dalton's law. This means you can track the water vapor independently of the air, using its partial pressure to locate it on the steam property tables you already know.

The central property is the **humidity ratio** ω (also called specific humidity): the mass of water vapor per kilogram of dry air. Dry air is the fixed reference because it doesn't condense or evaporate during typical HVAC processes — it's conserved. ω stays constant when you heat or cool air without adding or removing moisture, and it changes only when you humidify, dehumidify, or mix air streams. **Relative humidity** φ = P_v / P_sat(T) compares the actual partial pressure of water vapor to the saturation pressure at the current temperature. Because P_sat rises steeply with temperature, the same ω gives very different φ values at different temperatures: 30% relative humidity in winter air heated from −10°C to 20°C means the indoor air feels bone dry, even though no water was removed.

The **dew point** is the temperature at which the current partial pressure of water vapor equals P_sat — the temperature you'd have to cool the air to in order to reach saturation and begin condensation. If you cool a surface (a window, a cold pipe) below the dew point of the surrounding air, water will condense on it. The **wet-bulb temperature** is trickier: it's the equilibrium temperature reached when water evaporates adiabatically into unsaturated air, limited by the cooling effect of evaporation. Dry bulb temperature minus wet bulb temperature is the **psychrometric depression** — larger gaps mean drier air. These three temperatures (dry bulb, wet bulb, dew point) together with ω and φ define the complete state of a moist air sample.

The **psychrometric chart** is simply a graph that plots all these properties simultaneously for moist air at standard atmospheric pressure (101.325 kPa). The horizontal axis is dry-bulb temperature; the curved boundary at the top is 100% relative humidity (saturation). Any state point on the chart encodes ω, φ, dew point, wet-bulb temperature, and enthalpy simultaneously — once you locate the point, you read everything off the scales. More importantly, thermodynamic *processes* become geometric *paths* on the chart. Sensible heating (no moisture change) is a horizontal line moving right. Cooling with dehumidification tracks along a diagonal until it hits saturation, then descends along the saturation curve as water condenses out. Humidification moves the point upward and to the right. This geometric picture makes the chart the primary design tool for HVAC engineers: you can immediately see what a cooling coil, heating element, or evaporative cooler does to the air state, and calculate the energy (enthalpy change) or moisture change involved.

