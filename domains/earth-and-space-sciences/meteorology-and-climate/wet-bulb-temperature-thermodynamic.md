---
id: wet-bulb-temperature-thermodynamic
title: Wet-Bulb Temperature and Psychrometric Process
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: water-vapor-saturation-mixing-ratio
  type: hard
- id: latent-heating-in-weather-systems
  type: hard
builds-toward:
- equivalent-potential-temperature
- thermodynamic-diagrams
tags:
- moisture
- thermodynamics
- evaporative-cooling
stage: formal-systems
status: validated
---

# Wet-Bulb Temperature and Psychrometric Process

## Core Idea
The wet-bulb temperature is the equilibrium temperature reached when air is saturated adiabatically by evaporating water. It represents the lowest temperature air can cool to via evaporation and is a measure of the combined effects of temperature and humidity. Wet-bulb temperature is crucial for assessing heat stress and extreme weather potential.

## Questions

```yaml
- question: "Air has a dry-bulb temperature of 38°C and a wet-bulb temperature of 24°C. Which statement best describes this air mass?"
  type: multiple-choice
  options:
    - "The air is nearly saturated — evaporation is almost impossible"
    - "The air is significantly below saturation; vigorous evaporation would cool a wet surface to 24°C"
    - "The wet-bulb temperature is below the dew point, indicating supersaturation"
    - "Relative humidity is 100% because the wet-bulb reading is valid"
  answer: 1
  explanation: "A 14°C wet-bulb depression (38 − 24 = 14°C) indicates dry air significantly below saturation. The wet-bulb temperature is the equilibrium temperature reached when evaporation saturates the surrounding air — the larger the depression, the drier the air and the more vigorous the evaporative cooling. Option C is wrong: the wet-bulb temperature always lies between the dry-bulb temperature and the dew point; it cannot be below the dew point. Option D is wrong: 100% RH would give zero wet-bulb depression."

- question: "City A has a forecast of 46°C dry-bulb, 26°C wet-bulb. City B has 36°C dry-bulb, 35°C wet-bulb. Which city poses a greater physiological heat risk to outdoor workers, and why?"
  type: multiple-choice
  options:
    - "City A, because the absolute air temperature is far higher and drives more heat into the body"
    - "City B, because with wet-bulb near 35°C, evaporative cooling from sweat becomes nearly ineffective, preventing the body from shedding metabolic heat"
    - "Both are equally dangerous because both exceed 35°C dry-bulb"
    - "Neither is dangerous — heat stress depends only on solar radiation, not air temperature or humidity"
  answer: 1
  explanation: "Human thermoregulation depends on evaporative cooling: sweat evaporates from skin, removing latent heat. This process requires that the ambient air be below saturation. When wet-bulb temperature approaches ~35°C (skin temperature), the gradient driving evaporation nearly vanishes — the body cannot cool itself regardless of how much it sweats. City A's 26°C wet-bulb still allows effective sweating. City B's 35°C wet-bulb is near the physiological lethal threshold, making it far more dangerous despite the lower dry-bulb temperature."

- question: "In mostly saturated air (100% relative humidity), the wet-bulb temperature is higher than the dry-bulb temperature because saturation stores more heat."
  type: true-false
  answer: false
  explanation: "In saturated air, evaporation from a wet surface cannot occur because the air cannot hold any more water vapor. With no evaporation, there is no evaporative cooling, and the wet thermometer reads the same temperature as the dry thermometer. At 100% RH, wet-bulb temperature = dry-bulb temperature = dew point. They converge to the same value, not with wet-bulb above dry-bulb. The wet-bulb temperature can never exceed the dry-bulb temperature."

- question: "The wet-bulb temperature encodes information about both air temperature and moisture content, making it a more complete thermodynamic descriptor than temperature alone."
  type: true-false
  answer: true
  explanation: "The wet-bulb temperature is determined by the combined effect of temperature (which drives evaporation rate) and moisture content (which limits how much evaporation can occur). Two air parcels at the same dry-bulb temperature but different humidities will have different wet-bulb temperatures. This is why the wet-bulb temperature appears on thermodynamic diagrams as a conserved variable along moist-adiabatic processes, and why it is used in precipitation-type forecasting — it captures the full thermodynamic state more compactly than temperature alone."

- question: "Why does whether precipitation reaches the surface as rain or sleet depend on the wet-bulb temperature of the sub-freezing air layer below a warm aloft layer, rather than the dry-bulb temperature?"
  type: short-answer
  answer: "As melted snowflakes fall through sub-freezing air, they evaporate slightly, and this evaporation draws heat from the surrounding air — cooling it below the dry-bulb reading. Whether the drops refreeze into sleet depends on the actual temperature of the air after accounting for this evaporative cooling, which is the wet-bulb temperature. If the wet-bulb temperature of the cold layer is below 0°C, the evaporatively cooled air can refreeze the drops; if the wet-bulb is above 0°C, rain reaches the surface. Using dry-bulb alone would overestimate the air temperature in the cold layer and lead to incorrect precipitation-type forecasts."
  explanation: "This is an elegant example of wet-bulb temperature's practical power: it captures the thermodynamic equilibrium that falling hydrometeors approach as they evaporate, not the initial state of the air. Forecasters therefore use wet-bulb temperature — not dry-bulb — as the threshold for sleet/freezing rain versus rain."
```

## Explainer

From your study of saturation mixing ratio and latent heating, you know that evaporation requires energy — specifically, the latent heat of vaporization drawn from the surrounding air. The **wet-bulb temperature** is the natural consequence of pushing this evaporative cooling to its limit. Imagine wrapping a thermometer bulb in a wet cloth and ventilating it with ambient air. Water evaporates from the cloth, drawing heat from the thermometer and cooling it. As the air immediately around the cloth gains moisture, the evaporation rate slows. Eventually, the air is saturated, evaporation stops, and the thermometer settles at a steady reading — the wet-bulb temperature.

The wet-bulb temperature always lies between the **dry-bulb temperature** (ordinary air temperature) and the **dew point** (the temperature at which the air would become saturated without adding or removing moisture). In very dry air, vigorous evaporation drives the wet-bulb far below the dry-bulb — this is why a desert breeze feels cool on wet skin despite scorching air temperatures. In saturated air (100% relative humidity), evaporation cannot occur, and the wet-bulb, dry-bulb, and dew point all converge to the same value. The **wet-bulb depression** — the difference between dry-bulb and wet-bulb temperature — is therefore a direct measure of how far the air is from saturation.

Thermodynamically, the wet-bulb process traces a specific path on a Skew-T diagram: starting from the air's current state, you follow a line of constant wet-bulb potential temperature (approximately a saturated adiabat) downward to the surface pressure. This is an **isobaric** process (constant pressure) in which sensible heat is converted to latent heat — the air cools while gaining moisture, with total enthalpy approximately conserved. This makes the wet-bulb temperature a powerful diagnostic because it encodes both temperature and moisture information in a single number.

The wet-bulb temperature has critical practical applications. In human physiology, the body cools itself by evaporating sweat. When the wet-bulb temperature approaches skin temperature (~35°C), evaporative cooling becomes ineffective and the body cannot shed metabolic heat — a condition that is lethal within hours even for healthy people in shade. Wet-bulb temperatures above 35°C are extraordinarily rare in today's climate but are projected to occur more frequently in tropical and subtropical regions under continued warming. In meteorology, the wet-bulb temperature determines the **precipitation type**: when a warm layer aloft melts falling snowflakes, whether they refreeze into sleet or remain as rain before reaching the surface depends on the wet-bulb temperature of the air below, not the dry-bulb temperature, because evaporative cooling of the melting hydrometeors can chill the surrounding air below the dry-bulb reading.
