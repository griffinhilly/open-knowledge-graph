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
stage: formal-systems
status: validated
---

# Moist Adiabatic Lapse Rate

## Core Idea
The moist adiabatic lapse rate (~6 K/km) describes temperature change for saturated air parcels as they rise and condense, with released latent heat partially offsetting adiabatic cooling. This rate is variable and depends on temperature and moisture content, making it essential for understanding convective instability. The difference between dry and moist rates explains why deep convection can occur.

## How It's Best Learned
Compare the rates graphically on a skew-T diagram. Study a parcel lifting through its lifting-condensation-level to see the transition from dry to moist lapse rate.

## Common Misconceptions
- Assuming the moist adiabatic lapse rate is a fixed constant like the dry rate. - Forgetting that latent heat release reduces cooling during condensation, making the rate gentler than the dry rate.

## Questions

```yaml
- question: "On a calm morning, an air parcel is lifted to its lifting condensation level. Before saturation, it cools at 9.8°C/km (dry rate) and is denser than its surroundings — stable. After saturation, it cools at 5°C/km while the environment cools at 7°C/km. What happens?"
  type: multiple-choice
  options:
    - "The parcel remains stable because it is still cooler than the environment when averaged over the whole ascent"
    - "The parcel becomes positively buoyant — it now cools more slowly than the environment, so it is warmer than its surroundings and accelerates upward"
    - "The environment's lapse rate must change before the parcel can become unstable"
    - "The parcel stabilizes again once latent heat is exhausted and the dry rate resumes"
  answer: 1
  explanation: "This is conditional instability in action. A parcel is buoyant when it is warmer than its surroundings at the same altitude. Unsaturated, the parcel cools at 9.8°C/km while the environment cools at 7°C/km — the parcel cools faster, becoming denser and sinking back. Saturated, the parcel cools at 5°C/km — slower than the environment's 7°C/km — so the parcel is progressively warmer than its surroundings and accelerates upward. The atmosphere hasn't changed; the parcel's lapse rate changed when condensation began releasing latent heat. This is the trigger for deep convection and thunderstorm development."

- question: "Why is the moist adiabatic lapse rate significantly lower (gentler) in warm tropical air than in cold polar air?"
  type: multiple-choice
  options:
    - "Tropical air has higher pressure aloft, which reduces the rate of adiabatic expansion and therefore cooling"
    - "Warm air holds much more water vapor; more vapor condenses per kilometer of ascent, releasing more latent heat that partially offsets adiabatic cooling"
    - "The Coriolis effect in tropical regions deflects rising parcels horizontally, reducing vertical cooling"
    - "Tropical air contains more CO₂, which absorbs the heat released during condensation"
  answer: 1
  explanation: "The moist lapse rate is variable precisely because it depends on how much latent heat is released per kilometer of ascent — and that depends on how much water vapor is available to condense. Warm air near the tropics can hold far more water vapor than cold polar air (the Clausius-Clapeyron relationship makes water vapor content strongly temperature-dependent). A rising tropical parcel condenses more moisture per kilometer, releases more latent heat, and thus cools more slowly — perhaps 4–5°C/km. A rising polar parcel condenses little moisture, releases little latent heat, and its moist lapse rate approaches the dry rate of 9.8°C/km."

- question: "The moist adiabatic lapse rate averages about 6°C/km but varies depending on temperature and moisture content — unlike the dry adiabatic lapse rate, which is essentially constant."
  type: true-false
  answer: true
  explanation: "The dry adiabatic lapse rate (9.8°C/km) depends only on the specific heat of dry air and gravitational acceleration — both nearly constant. The moist rate adds a latent heat term whose magnitude varies with how much water vapor condenses per unit of ascent. Since water vapor content depends strongly on temperature (warm air holds more), the moist lapse rate is steepest in cold, dry air (approaching the dry rate) and gentlest in warm, humid air (as low as 4°C/km in the tropics). This variability is why the moist rate is described as approximately 6°C/km rather than a precise constant."

- question: "The moist adiabatic lapse rate is a fixed constant of approximately 6°C/km, similar to how the dry adiabatic lapse rate is fixed at approximately 9.8°C/km."
  type: true-false
  answer: false
  explanation: "This is one of the most common misconceptions about lapse rates. The dry rate is fixed because it depends only on constants (specific heat of dry air, gravitational acceleration). The moist rate is variable because the latent heat released per kilometer of ascent depends on how much water vapor condenses — which depends on temperature. A tropical surface parcel may cool at only 4–5°C/km; a cold high-latitude parcel may approach 9°C/km. Treating the moist rate as a fixed constant leads to errors in stability analysis, especially when comparing tropical and polar atmospheric profiles."

- question: "Why does the difference between the dry and moist adiabatic lapse rates create 'conditional instability' in the atmosphere?"
  type: short-answer
  answer: "An atmosphere is conditionally unstable when its environmental lapse rate falls between the dry (~9.8°C/km) and moist (~6°C/km) rates. In this condition, an unsaturated parcel cools faster than the environment (dry rate > environmental rate) and is stable. But once the parcel reaches saturation — its condensation level — it switches to the lower moist rate and now cools more slowly than the environment. The parcel becomes warmer than its surroundings, positively buoyant, and accelerates upward without further forcing. The condition is the saturation threshold; stability is conditional on whether the parcel is dry or saturated."
  explanation: "This mechanism explains how a clear-sky morning can produce towering afternoon thunderstorms. Surface heating lifts parcels; once they reach their lifting condensation level and saturation, the latent heat engine takes over and drives explosive vertical development. The atmosphere hasn't changed — what changed is the parcel's phase from unsaturated to saturated, crossing the threshold from stable to unstable behavior."
```

## Explainer

You already know from the dry adiabatic lapse rate that an unsaturated air parcel cools at a steady 9.8°C per kilometer as it rises, because it expands against lower surrounding pressure and loses internal energy in the process. That rate is essentially constant because it depends only on the specific heat of dry air and the gravitational acceleration — neither of which changes much. But something fundamentally different happens once the parcel reaches its **dew point** and water vapor begins condensing into liquid droplets.

Condensation is an exothermic process — it releases the **latent heat** that was absorbed when the water originally evaporated from the ocean or land surface. You studied this energy transfer in latent heat and phase transitions: roughly 2,500 joules per gram of water vapor condensed. When a rising, saturated parcel condenses moisture, this heat release warms the parcel from within, partially offsetting the cooling it experiences from adiabatic expansion. The parcel still cools as it rises — expansion always wins — but it cools more slowly than the dry rate. This slower cooling rate is the **moist adiabatic lapse rate**, averaging about 6°C/km but varying significantly.

The variability is the crucial detail. Unlike the dry rate, the moist rate depends on how much water vapor is available to condense — and that depends on temperature. Warm air near the tropics holds far more water vapor than cold polar air, so a saturated tropical parcel releases much more latent heat per kilometer of ascent and cools very slowly (perhaps 4–5°C/km near the surface). A cold, saturated parcel near the poles holds little moisture, releases little latent heat, and its moist lapse rate approaches the dry rate (8–9°C/km). This means the moist adiabatic lapse rate is steepest in cold air and gentlest in warm, humid air — a fact with enormous consequences for tropical convection.

The difference between the dry and moist rates is what makes deep convection possible. Imagine the environmental temperature decreasing at 7°C/km. An unsaturated parcel rising at 9.8°C/km cools faster than its surroundings — it is negatively buoyant and resists further lifting (stable). But once that same parcel reaches saturation and transitions to the moist rate of, say, 5°C/km, it now cools more slowly than the environment — it becomes warmer than its surroundings, positively buoyant, and accelerates upward. This is **conditional instability**: the atmosphere is stable for dry parcels but unstable for saturated ones. It explains why a seemingly calm atmosphere can erupt into towering cumulonimbus clouds once parcels are lifted past the condensation level — the latent heat engine takes over and drives the convection.
