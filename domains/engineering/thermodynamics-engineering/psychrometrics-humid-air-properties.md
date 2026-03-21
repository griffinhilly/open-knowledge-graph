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

## Questions

```yaml
- question: "Cold outdoor air at −10°C with 80% relative humidity is brought indoors and heated to 20°C without adding any moisture. How does the relative humidity of the indoor air compare to the outdoor air?"
  type: multiple-choice
  options:
    - "It remains near 80% — the humidity ratio is constant, so relative humidity is constant"
    - "It increases — warmer air feels more humid because the water vapor is more energetic"
    - "It drops dramatically — P_sat rises steeply with temperature, so the same vapor content becomes a much smaller fraction of saturation capacity"
    - "It drops to 0% — heating destroys water vapor"
  answer: 2
  explanation: "Relative humidity φ = P_v / P_sat(T). When air is heated at constant humidity ratio (no moisture added or removed), P_v stays constant but P_sat rises steeply with temperature — roughly doubling every 10°C near typical indoor temperatures. At −10°C, P_sat is about 0.26 kPa; at 20°C it is about 2.34 kPa — nearly 9× higher. So 80% RH outdoors becomes roughly 80% × (0.26/2.34) ≈ 9% RH indoors. This is why heated winter air feels bone dry even though no moisture was removed. Option A is the classic misconception: constant ω does not mean constant φ."

- question: "An HVAC system cools a supply air stream from 28°C and 65% relative humidity down to 12°C. Which path on the psychrometric chart correctly describes this process?"
  type: multiple-choice
  options:
    - "A horizontal line moving left — temperature decreases while humidity ratio stays constant"
    - "A diagonal path moving down and left, eventually reaching the saturation curve, then descending along it as moisture condenses out"
    - "A vertical line moving downward — humidity ratio decreases at constant temperature"
    - "A path curving rightward — the air gains moisture from the cooling coil condensate"
  answer: 1
  explanation: "Initially, cooling the air without reaching the dew point traces a horizontal path leftward (constant ω, decreasing T). Once the air reaches the dew point, it hits the saturation curve (100% RH). Further cooling requires condensation: moisture is removed, and the state point descends along the saturation curve — both temperature and humidity ratio decrease together. This combined path (horizontal then along the saturation boundary) is characteristic of a cooling coil that dehumidifies. A horizontal path alone (option A) would only apply if cooling stopped before reaching the dew point."

- question: "Relative humidity is a reliable indicator of the actual mass of water vapor present in an air sample."
  type: true-false
  answer: false
  explanation: "Relative humidity indicates how close the air is to saturation at its current temperature, not the absolute moisture content. The same mass of water vapor per kilogram of dry air (same humidity ratio ω) produces very different relative humidity values at different temperatures. Desert air at 40°C with 20% RH contains far more moisture per kilogram of air than Arctic air at −20°C with 80% RH. For engineering calculations involving moisture addition, removal, or condensation, the humidity ratio ω is the relevant conserved quantity — not relative humidity."

- question: "On a psychrometric chart, sensible heating (adding heat without changing moisture content) is represented as a horizontal line moving to the right, because the humidity ratio stays constant while dry-bulb temperature increases."
  type: true-false
  answer: true
  explanation: "The humidity ratio ω (kg water per kg dry air) is constant during sensible heating because no moisture is added or removed — only temperature changes. Since the psychrometric chart's vertical axis is humidity ratio, a constant-ω process traces a horizontal line. Moving right means increasing dry-bulb temperature. This geometric representation is the psychrometric chart's primary utility: thermodynamic processes become predictable geometric paths, allowing engineers to read off all state properties at a glance and calculate enthalpy changes directly."

- question: "Explain why the humidity ratio (ω) rather than relative humidity (φ) is the conserved quantity during sensible heating, and why this distinction matters for HVAC design."
  type: short-answer
  answer: "Humidity ratio ω is the mass of water vapor per kilogram of dry air — a ratio that depends only on how much water is physically present in the air, independent of temperature. Adding heat does not add or remove water molecules, so ω is unchanged. Relative humidity φ = P_v / P_sat(T) depends on temperature through P_sat, so it changes whenever temperature changes even if water content is constant. For HVAC design, ω is what matters for calculating moisture loads, latent heat, condensation risk, and mixing calculations — because φ changes with every heating or cooling step, you cannot use it to track moisture through a system."
  explanation: "The practical consequence is significant: an engineer who designs a heating system based on keeping relative humidity 'the same' will deliver bone-dry indoor air in winter. Sizing a humidifier or calculating the load on a cooling coil requires working in humidity ratio, not relative humidity. The psychrometric chart makes this visible: sensible heating is a flat horizontal line (ω constant) while RH isolines curve — crossing multiple RH values as temperature increases along constant ω."
```

## Explainer

From your study of pure substance phase diagrams, you know that water can exist as a liquid, a vapor, or a two-phase mixture depending on temperature and pressure. Psychrometrics applies exactly this framework to the mixture of dry air and water vapor that constitutes the atmosphere. The key insight is that at normal atmospheric conditions, air and water vapor behave nearly as ideal gases — they share the total pressure but each occupies the full volume, consistent with Dalton's law. This means you can track the water vapor independently of the air, using its partial pressure to locate it on the steam property tables you already know.

The central property is the **humidity ratio** ω (also called specific humidity): the mass of water vapor per kilogram of dry air. Dry air is the fixed reference because it doesn't condense or evaporate during typical HVAC processes — it's conserved. ω stays constant when you heat or cool air without adding or removing moisture, and it changes only when you humidify, dehumidify, or mix air streams. **Relative humidity** φ = P_v / P_sat(T) compares the actual partial pressure of water vapor to the saturation pressure at the current temperature. Because P_sat rises steeply with temperature, the same ω gives very different φ values at different temperatures: 30% relative humidity in winter air heated from −10°C to 20°C means the indoor air feels bone dry, even though no water was removed.

The **dew point** is the temperature at which the current partial pressure of water vapor equals P_sat — the temperature you'd have to cool the air to in order to reach saturation and begin condensation. If you cool a surface (a window, a cold pipe) below the dew point of the surrounding air, water will condense on it. The **wet-bulb temperature** is trickier: it's the equilibrium temperature reached when water evaporates adiabatically into unsaturated air, limited by the cooling effect of evaporation. Dry bulb temperature minus wet bulb temperature is the **psychrometric depression** — larger gaps mean drier air. These three temperatures (dry bulb, wet bulb, dew point) together with ω and φ define the complete state of a moist air sample.

The **psychrometric chart** is simply a graph that plots all these properties simultaneously for moist air at standard atmospheric pressure (101.325 kPa). The horizontal axis is dry-bulb temperature; the curved boundary at the top is 100% relative humidity (saturation). Any state point on the chart encodes ω, φ, dew point, wet-bulb temperature, and enthalpy simultaneously — once you locate the point, you read everything off the scales. More importantly, thermodynamic *processes* become geometric *paths* on the chart. Sensible heating (no moisture change) is a horizontal line moving right. Cooling with dehumidification tracks along a diagonal until it hits saturation, then descends along the saturation curve as water condenses out. Humidification moves the point upward and to the right. This geometric picture makes the chart the primary design tool for HVAC engineers: you can immediately see what a cooling coil, heating element, or evaporative cooler does to the air state, and calculate the energy (enthalpy change) or moisture change involved.

