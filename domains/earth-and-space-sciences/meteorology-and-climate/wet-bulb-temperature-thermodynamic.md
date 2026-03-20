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
stage: advanced
status: draft
---

# Wet-Bulb Temperature and Psychrometric Process

## Core Idea
The wet-bulb temperature is the equilibrium temperature reached when air is saturated adiabatically by evaporating water. It represents the lowest temperature air can cool to via evaporation and is a measure of the combined effects of temperature and humidity. Wet-bulb temperature is crucial for assessing heat stress and extreme weather potential.

## Explainer

From your study of saturation mixing ratio and latent heating, you know that evaporation requires energy — specifically, the latent heat of vaporization drawn from the surrounding air. The **wet-bulb temperature** is the natural consequence of pushing this evaporative cooling to its limit. Imagine wrapping a thermometer bulb in a wet cloth and ventilating it with ambient air. Water evaporates from the cloth, drawing heat from the thermometer and cooling it. As the air immediately around the cloth gains moisture, the evaporation rate slows. Eventually, the air is saturated, evaporation stops, and the thermometer settles at a steady reading — the wet-bulb temperature.

The wet-bulb temperature always lies between the **dry-bulb temperature** (ordinary air temperature) and the **dew point** (the temperature at which the air would become saturated without adding or removing moisture). In very dry air, vigorous evaporation drives the wet-bulb far below the dry-bulb — this is why a desert breeze feels cool on wet skin despite scorching air temperatures. In saturated air (100% relative humidity), evaporation cannot occur, and the wet-bulb, dry-bulb, and dew point all converge to the same value. The **wet-bulb depression** — the difference between dry-bulb and wet-bulb temperature — is therefore a direct measure of how far the air is from saturation.

Thermodynamically, the wet-bulb process traces a specific path on a Skew-T diagram: starting from the air's current state, you follow a line of constant wet-bulb potential temperature (approximately a saturated adiabat) downward to the surface pressure. This is an **isobaric** process (constant pressure) in which sensible heat is converted to latent heat — the air cools while gaining moisture, with total enthalpy approximately conserved. This makes the wet-bulb temperature a powerful diagnostic because it encodes both temperature and moisture information in a single number.

The wet-bulb temperature has critical practical applications. In human physiology, the body cools itself by evaporating sweat. When the wet-bulb temperature approaches skin temperature (~35°C), evaporative cooling becomes ineffective and the body cannot shed metabolic heat — a condition that is lethal within hours even for healthy people in shade. Wet-bulb temperatures above 35°C are extraordinarily rare in today's climate but are projected to occur more frequently in tropical and subtropical regions under continued warming. In meteorology, the wet-bulb temperature determines the **precipitation type**: when a warm layer aloft melts falling snowflakes, whether they refreeze into sleet or remain as rain before reaching the surface depends on the wet-bulb temperature of the air below, not the dry-bulb temperature, because evaporative cooling of the melting hydrometeors can chill the surrounding air below the dry-bulb reading.
