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

## Questions

```yaml
- question: "On a summer afternoon, the temperature is 35°C and relative humidity is 40%. By nightfall, the temperature drops to 20°C with no rain, wind shift, or other change in the air mass. What happens to the dew point and relative humidity?"
  type: multiple-choice
  options:
    - "Both dew point and relative humidity decrease as the air cools"
    - "Dew point stays the same; relative humidity increases as the air cools because the air's capacity shrinks while moisture content stays constant"
    - "Dew point rises as the air cools; relative humidity stays constant"
    - "Both remain constant because no moisture has been added or removed"
  answer: 1
  explanation: "Dew point is a property of the air mass's actual moisture content — it only changes when moisture is added or removed. Cooling the air changes nothing about how much vapor is present, so dew point is unchanged. Relative humidity, however, is the ratio of actual vapor pressure to saturation vapor pressure at the current temperature. As temperature drops, the saturation vapor pressure drops (warmer air can hold more vapor), so the ratio increases — humidity rises even though no moisture was added. This is why dew forms on cool surfaces overnight in conditions that felt relatively dry during the day."

- question: "A weather forecast shows a surface temperature of 28°C and a dew point of 26°C. What can you correctly infer about current conditions?"
  type: multiple-choice
  options:
    - "The air is quite dry — a 2°C spread between temperature and dew point indicates low moisture content"
    - "Relative humidity is approximately 50% and any clouds will have high bases"
    - "The air is very moist; with only a 2°C spread, relative humidity is near 100% and low-level clouds, fog, or condensation are likely"
    - "The dew point is close to the temperature, meaning the air is about to freeze"
  answer: 2
  explanation: "A narrow temperature-dew point spread means the air is close to saturation. When temperature equals dew point, relative humidity hits 100% and condensation begins. A 2°C spread means the air needs to cool only slightly before clouds, fog, or dew form. Option A reflects the common error of thinking 'spread = dryness' — actually, a wide spread (e.g., temperature 35°C, dew point 5°C) means very dry air, while a narrow spread means moist air near saturation. Forecasters use this spread routinely to predict cloud base heights and fog risk."

- question: "Dew point is a more reliable indicator of actual moisture content than relative humidity because dew point changes only when moisture is physically added to or removed from the air mass, while relative humidity also changes when temperature changes."
  type: true-false
  answer: true
  explanation: "Exactly right. A dew point of 20°C tells you the same thing about moisture content regardless of whether the air temperature is 22°C or 40°C — the amount of water vapor present is unchanged. Relative humidity at those temperatures would be very different: near 100% in the first case, much lower in the second. Because relative humidity depends on both moisture and temperature, it can give a misleading picture of atmospheric moisture. Dew point strips out the temperature dependence, making it a cleaner measure for forecasting moisture-related phenomena."

- question: "At a relative humidity of 100%, the air contains the maximum possible number of water molecules that can exist in vapor form at any temperature."
  type: true-false
  answer: false
  explanation: "100% relative humidity means the air is saturated at its current temperature — not at the absolute maximum possible for any temperature. Warmer air can hold much more vapor before reaching saturation. On a hot day at 35°C, saturation vapor pressure is about 56 hPa; on a cool day at 10°C, it is only about 12 hPa. Air at 100% RH on a cool day actually contains far less water vapor than air at 50% RH on a hot day. The 'maximum' is always temperature-relative. This is why meteorologists use dew point rather than relative humidity to quantify true moisture content."

- question: "Explain why a rising air parcel cools and eventually forms clouds without any moisture being added to it, using the concepts of dew point and saturation."
  type: short-answer
  answer: "As an air parcel rises, it expands because atmospheric pressure decreases with altitude. This expansion is adiabatic — the parcel does work on its surroundings without exchanging heat, so it cools. The parcel's moisture content (and therefore its dew point) remains constant as it rises, because no moisture is added or removed. But its temperature drops steadily. At some altitude, the temperature reaches the dew point — the air becomes saturated (100% relative humidity). At this point, further cooling causes water vapor to condense into tiny droplets, forming cloud. This altitude is the lifted condensation level, and the surface temperature-dew point spread determines how high it is: a wide spread means the parcel must rise farther before cooling to saturation."
  explanation: "The key insight is that temperature and dew point converge as the parcel rises: temperature falls, dew point stays (nearly) constant, and cloud forms where they meet. This is why a large temperature-dew point spread on the surface predicts high cloud bases or no clouds, while a narrow spread predicts low bases. The mechanism requires no external moisture — the cooling itself drives the air to saturation by reducing the air's capacity to hold the vapor it already contains."
```

## Explainer

From your study of latent heat and phase transitions, you know that water molecules constantly move between vapor, liquid, and ice phases, and that each transition absorbs or releases energy. From the Clausius-Clapeyron relation, you know that **saturation vapor pressure** — the maximum amount of water vapor air can hold at equilibrium — increases exponentially with temperature, roughly doubling for every 10°C rise. These ideas come together to explain why moisture, temperature, and condensation are so tightly linked in the atmosphere.

Think of the air as a container with a temperature-dependent capacity for water vapor. At 30°C, the saturation vapor pressure is about 42 hPa — the air can hold a lot of moisture before condensation begins. At 10°C, saturation vapor pressure drops to about 12 hPa. The actual amount of vapor present at any moment is the **vapor pressure** (e), and the ratio of actual to saturation vapor pressure gives the **relative humidity**: RH = (e / eₛ) × 100%. Crucially, relative humidity depends on both how much moisture is present and how warm the air is. On a hot afternoon, relative humidity might be 30% even though the air contains substantial moisture, because the warm air's capacity is so large. As the same air cools overnight without gaining or losing moisture, its capacity shrinks while its moisture stays constant — relative humidity climbs toward 100%.

The **dew point** is the temperature at which this process reaches completion: the temperature to which you must cool the air (at constant pressure and moisture content) for it to become saturated. Unlike relative humidity, the dew point does not change with temperature — it changes only when moisture is added to or removed from the air. This makes it a far more useful measure of actual moisture content for forecasting. A dew point of 20°C tells you the air contains the same amount of moisture regardless of whether the current temperature is 25°C or 40°C. When the air temperature equals the dew point, relative humidity is 100% and condensation begins — dew forms on surfaces, fog appears, or clouds develop if the cooling happens at altitude.

This framework is the basis for predicting cloud formation. As an air parcel rises and cools adiabatically, its temperature drops while its moisture content stays constant. At some altitude, the temperature reaches the dew point and condensation begins — this is the **lifted condensation level**, the base of cumulus clouds. The gap between surface temperature and dew point tells forecasters how high that cloud base will be: a large temperature-dew point spread means dry air and high cloud bases (or no clouds at all), while a narrow spread means moist air and low clouds. This is why meteorologists pay close attention to dew point values — they reveal the atmosphere's moisture state directly and predict where and when condensation will occur.
