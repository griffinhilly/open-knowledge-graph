---
id: solar-radiation-and-earth-energy-balance
title: Solar Radiation and Earth's Energy Balance
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: electromagnetic-spectrum
  type: soft
- id: blackbody-radiation
  type: soft
- id: heat-transfer-radiation
  type: soft
- id: atmosphere-composition-and-structure
  type: soft
builds-toward:
- greenhouse-effect
- climate-zones-and-biomes
- feedback-mechanisms-in-climate
tags:
- solar
- albedo
- insolation
- energy-balance
- radiation
stage: formal-systems
status: validated
---

# Solar Radiation and Earth's Energy Balance

## Core Idea
The Sun emits shortwave radiation (visible and UV) that heats Earth's surface, while Earth re-emits longwave infrared radiation back to space. At equilibrium, incoming solar energy absorbed equals outgoing longwave radiation emitted. Albedo — the fraction of incoming sunlight reflected — determines how much energy is absorbed; snow and ice have high albedo, oceans and forests have low albedo. Unequal distribution of solar energy by latitude (tropics receive more than poles) is the primary driver of atmospheric and oceanic circulation.

## How It's Best Learned
Work through the planetary energy balance equation quantitatively, then explore how changing albedo shifts equilibrium temperature. Compare Earth's effective radiating temperature (~255 K) to actual surface temperature (~288 K) to motivate the greenhouse effect.

## Common Misconceptions
- Earth is not warmed by reflected sunlight — reflected light goes back to space.
- The tilt of Earth's axis, not distance from the Sun, is what causes seasons.
- Energy balance is a global average; locally and seasonally, imbalances drive weather and climate dynamics.

## Questions

```yaml
- question: "Earth's global average albedo is approximately 0.30. Which statement correctly describes what happens to incoming solar radiation?"
  type: multiple-choice
  options: ["30% is absorbed by the surface; 70% is reflected to space", "70% is absorbed by the Earth system; 30% is reflected to space", "30% heats the atmosphere directly; 70% reaches the surface", "70% is absorbed by greenhouse gases in the atmosphere"]
  answer: 1
  explanation: "Albedo is the fraction of incoming radiation that is reflected. An albedo of 0.30 means 30% is reflected back to space and 1 − 0.30 = 70% is absorbed by the Earth system (surface plus atmosphere combined). This absorbed fraction is what ultimately must be balanced by outgoing longwave radiation to maintain energy equilibrium."

- question: "Earth is warmer in the Northern Hemisphere summer than in winter because Earth is closer to the Sun during summer."
  type: true-false
  answer: false
  explanation: "This is one of the most pervasive misconceptions in Earth science. Seasons are caused by the tilt of Earth's rotational axis (~23.5°). When the Northern Hemisphere tilts toward the Sun, solar radiation strikes at a more direct angle and days are longer — both effects concentrate more energy per unit area. In fact, Earth is slightly farther from the Sun during Northern Hemisphere summer (at aphelion in early July) than in winter."

- question: "Earth's effective radiating temperature is about 255 K, but the observed global average surface temperature is about 288 K. What explains the 33 K difference?"
  type: short-answer
  answer: "The 33 K difference is due to the natural greenhouse effect. The atmosphere absorbs outgoing longwave radiation emitted by the surface and re-emits some of it back downward, supplementing the surface energy budget. As a result, the surface must reach a higher temperature than 255 K to ultimately radiate enough energy to space to balance incoming solar absorption."
  explanation: "The effective radiating temperature (255 K) is what Earth's temperature would be with no atmosphere — calculated by setting absorbed solar power equal to emitted blackbody power. The actual surface is warmer because the atmosphere acts as an insulating layer that intercepts and recycles outgoing radiation. This natural greenhouse effect is essential for life; without it, Earth's surface would be frozen."
```

## Explainer

The Sun continuously delivers energy to Earth in the form of shortwave radiation — mostly visible light and ultraviolet, peaking around 0.5 μm. From your study of blackbody radiation, you know that the wavelength of peak emission scales inversely with temperature (Wien's law): the Sun at ~5,778 K peaks in visible light, while Earth at ~288 K peaks around 10 μm in the thermal infrared. These two radiation streams — incoming shortwave, outgoing longwave — are the two sides of Earth's energy budget, and they must balance on a global average if the climate is to remain stable.

Not all incoming solar radiation is absorbed. Albedo quantifies the reflective fraction: snow, ice, and clouds are highly reflective (high albedo); dark oceans and forests absorb most incoming light (low albedo). Earth's global average albedo is about 0.30, meaning 30% of incoming solar radiation is immediately reflected back to space before doing any work. The remaining 70% is absorbed — partly by the atmosphere, mostly by the surface — and must eventually be re-emitted as longwave infrared radiation to close the energy budget.

You can estimate Earth's equilibrium temperature from first principles. The solar constant (power per unit area at Earth's orbit) is S ≈ 1361 W/m². Earth intercepts solar radiation over a disk of area πR², but it emits over its full spherical surface of area 4πR² — a factor-of-four difference. Setting absorbed power equal to emitted power: S/4 × (1 − albedo) = σT⁴ gives T ≈ 255 K. This is the effective radiating temperature. The actual surface is ~288 K, 33 K warmer — the natural greenhouse effect of the atmosphere cycling energy back to the surface.

Solar energy is not delivered uniformly. Because Earth is a sphere, tropical latitudes receive nearly perpendicular (concentrated) solar radiation year-round, while polar regions receive oblique (spread-out) radiation. This latitudinal gradient — tropics absorb more energy than poles — is the primary driver of atmospheric and oceanic circulation. The atmosphere and oceans transport heat poleward, trying to erase the temperature gradient. The Coriolis effect and continental geometry complicate this transport, generating the jet streams, ocean gyres, and climate zones we observe.

A critical distinction: the energy balance equation describes a global average at equilibrium. Regionally and seasonally, imbalances are normal and necessary — they drive weather. A region in summer absorbs more solar energy than it emits, warming up; in winter, the opposite. The global balance holds only when you average across all latitudes and all seasons. Changes to any component — albedo (from ice loss or land use change), greenhouse gas concentrations (affecting longwave emission), or the solar constant (from sunspot cycles) — perturb the balance and force the system to find a new equilibrium temperature.

