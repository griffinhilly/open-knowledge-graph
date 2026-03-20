---
id: moist-adiabatic-lapse-rate
title: Moist Adiabatic Lapse Rate
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: dry-adiabatic-lapse-rate
  type: hard
- id: saturation-and-dew-point
  type: hard
- id: latent-heat-and-phase-transitions
  type: hard
builds-toward:
- atmospheric-inversion-temperature
- convective-available-potential-energy
- lifting-condensation-level
tags:
- thermodynamics
- adiabatic
- condensation
- saturation
stage: advanced
status: draft
---

# Moist Adiabatic Lapse Rate

## Core Idea
The moist adiabatic lapse rate (~6 K/km) describes temperature change for saturated air parcels as they rise and condense, with released latent heat partially offsetting adiabatic cooling. This rate is variable and depends on temperature and moisture content, making it essential for understanding convective instability. The difference between dry and moist rates explains why deep convection can occur.

## How It's Best Learned
Compare the rates graphically on a skew-T diagram. Study a parcel lifting through its lifting-condensation-level to see the transition from dry to moist lapse rate.

## Common Misconceptions
- Assuming the moist adiabatic lapse rate is a fixed constant like the dry rate. - Forgetting that latent heat release reduces cooling during condensation, making the rate gentler than the dry rate.

## Explainer

You already know from the dry adiabatic lapse rate that an unsaturated air parcel cools at a steady 9.8°C per kilometer as it rises, because it expands against lower surrounding pressure and loses internal energy in the process. That rate is essentially constant because it depends only on the specific heat of dry air and the gravitational acceleration — neither of which changes much. But something fundamentally different happens once the parcel reaches its **dew point** and water vapor begins condensing into liquid droplets.

Condensation is an exothermic process — it releases the **latent heat** that was absorbed when the water originally evaporated from the ocean or land surface. You studied this energy transfer in latent heat and phase transitions: roughly 2,500 joules per gram of water vapor condensed. When a rising, saturated parcel condenses moisture, this heat release warms the parcel from within, partially offsetting the cooling it experiences from adiabatic expansion. The parcel still cools as it rises — expansion always wins — but it cools more slowly than the dry rate. This slower cooling rate is the **moist adiabatic lapse rate**, averaging about 6°C/km but varying significantly.

The variability is the crucial detail. Unlike the dry rate, the moist rate depends on how much water vapor is available to condense — and that depends on temperature. Warm air near the tropics holds far more water vapor than cold polar air, so a saturated tropical parcel releases much more latent heat per kilometer of ascent and cools very slowly (perhaps 4–5°C/km near the surface). A cold, saturated parcel near the poles holds little moisture, releases little latent heat, and its moist lapse rate approaches the dry rate (8–9°C/km). This means the moist adiabatic lapse rate is steepest in cold air and gentlest in warm, humid air — a fact with enormous consequences for tropical convection.

The difference between the dry and moist rates is what makes deep convection possible. Imagine the environmental temperature decreasing at 7°C/km. An unsaturated parcel rising at 9.8°C/km cools faster than its surroundings — it is negatively buoyant and resists further lifting (stable). But once that same parcel reaches saturation and transitions to the moist rate of, say, 5°C/km, it now cools more slowly than the environment — it becomes warmer than its surroundings, positively buoyant, and accelerates upward. This is **conditional instability**: the atmosphere is stable for dry parcels but unstable for saturated ones. It explains why a seemingly calm atmosphere can erupt into towering cumulonimbus clouds once parcels are lifted past the condensation level — the latent heat engine takes over and drives the convection.
