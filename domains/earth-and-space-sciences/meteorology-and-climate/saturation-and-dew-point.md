---
id: saturation-and-dew-point
title: Saturation, Relative Humidity, and Dew Point
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: latent-heat-and-phase-transitions
  type: hard
- id: gas-laws-ideal-gas
  type: soft
- id: saturation-vapor-pressure-clausius
  type: hard
builds-toward:
- convective-instability-indices
- thermodynamic-diagram-analysis
- moisture-transport-and-advection
tags:
- saturation
- humidity
- dew-point
- vapor-pressure
- moisture
stage: advanced
status: draft
---

# Saturation, Relative Humidity, and Dew Point

## Core Idea
Air's capacity to hold water vapor depends on temperature; warmer air can hold more vapor before saturation occurs. The dew point is the temperature at which air becomes saturated, and saturation vapor pressure increases exponentially with temperature (roughly doubling for every 10°C increase). This relationship means cooling or increase in moisture will trigger condensation, and understanding saturation is essential for predicting cloud formation and precipitation.

## How It's Best Learned
Use the Clausius-Clapeyron equation to show why saturation vapor pressure increases exponentially with temperature. Calculate dew point for sample soundings and relate it to cloud formation processes.

## Common Misconceptions
- Relative humidity depends only on absolute moisture; it depends on both moisture content and temperature. - Dew point changes with temperature; dew point is a fixed property of the air mass and changes only when moisture is added or removed.

## Explainer

From your study of latent heat and phase transitions, you know that water molecules constantly move between vapor, liquid, and ice phases, and that each transition absorbs or releases energy. From the Clausius-Clapeyron relation, you know that **saturation vapor pressure** — the maximum amount of water vapor air can hold at equilibrium — increases exponentially with temperature, roughly doubling for every 10°C rise. These ideas come together to explain why moisture, temperature, and condensation are so tightly linked in the atmosphere.

Think of the air as a container with a temperature-dependent capacity for water vapor. At 30°C, the saturation vapor pressure is about 42 hPa — the air can hold a lot of moisture before condensation begins. At 10°C, saturation vapor pressure drops to about 12 hPa. The actual amount of vapor present at any moment is the **vapor pressure** (e), and the ratio of actual to saturation vapor pressure gives the **relative humidity**: RH = (e / eₛ) × 100%. Crucially, relative humidity depends on both how much moisture is present and how warm the air is. On a hot afternoon, relative humidity might be 30% even though the air contains substantial moisture, because the warm air's capacity is so large. As the same air cools overnight without gaining or losing moisture, its capacity shrinks while its moisture stays constant — relative humidity climbs toward 100%.

The **dew point** is the temperature at which this process reaches completion: the temperature to which you must cool the air (at constant pressure and moisture content) for it to become saturated. Unlike relative humidity, the dew point does not change with temperature — it changes only when moisture is added to or removed from the air. This makes it a far more useful measure of actual moisture content for forecasting. A dew point of 20°C tells you the air contains the same amount of moisture regardless of whether the current temperature is 25°C or 40°C. When the air temperature equals the dew point, relative humidity is 100% and condensation begins — dew forms on surfaces, fog appears, or clouds develop if the cooling happens at altitude.

This framework is the basis for predicting cloud formation. As an air parcel rises and cools adiabatically, its temperature drops while its moisture content stays constant. At some altitude, the temperature reaches the dew point and condensation begins — this is the **lifted condensation level**, the base of cumulus clouds. The gap between surface temperature and dew point tells forecasters how high that cloud base will be: a large temperature-dew point spread means dry air and high cloud bases (or no clouds at all), while a narrow spread means moist air and low clouds. This is why meteorologists pay close attention to dew point values — they reveal the atmosphere's moisture state directly and predict where and when condensation will occur.
