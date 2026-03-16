---
id: convective-available-potential-energy
title: Convective Available Potential Energy (CAPE)
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: atmospheric-inversion-temperature
  type: hard
- id: dry-adiabatic-lapse-rate
  type: hard
- id: moist-adiabatic-lapse-rate
  type: hard
- id: mixing-ratio-saturation-mixing-ratio
  type: soft
builds-toward:
- severe-weather-systems
- lifted-index-stability
- thunderstorms-and-lightning
tags:
- instability
- convection
- energy
- parcel
stage: abstract-reasoning
status: draft
---

# Convective Available Potential Energy (CAPE)

## Core Idea
CAPE measures the area between a lifted parcel's temperature curve and the environmental temperature profile on a thermodynamic diagram, representing the buoyant energy available for convection. Higher CAPE (>1500 J/kg) indicates strong instability and potential for severe storms. CAPE depends on both the temperature deficit (parcel warmer than environment) and the depth of unstable layer.

## How It's Best Learned
Use skew-T diagrams to lift a parcel from surface and shade the CAPE region. Compare CAPE values for stable vs. unstable soundings.

## Common Misconceptions
- Thinking CAPE alone predicts severe weather; wind shear and moisture are equally important. - Confusing CAPE with the lifted index; they measure different aspects of stability.

## Explainer

You already know that a rising air parcel cools at the dry adiabatic lapse rate until it reaches saturation, then cools more slowly at the moist adiabatic lapse rate as condensation releases latent heat. You also know that when the environment's temperature drops faster than the parcel's, the parcel remains warmer and more buoyant than its surroundings — it keeps rising. **Convective Available Potential Energy (CAPE)** puts a number on exactly how much buoyant energy is available to fuel that ascent.

Picture a skew-T log-P diagram — the standard thermodynamic chart meteorologists use. Plot the environmental temperature sounding as one curve and the temperature of a parcel lifted from the surface as another. Below the **Level of Free Convection (LFC)**, the parcel is cooler than the environment and must be forced upward (by a front, terrain, or outflow boundary). Above the LFC, the parcel becomes warmer than its surroundings and accelerates upward on its own. This continues until the parcel reaches the **Equilibrium Level (EL)**, where it is no longer warmer than the environment. CAPE is the area enclosed between the parcel's curve and the environment's curve in the region where the parcel is warmer. On the diagram, you literally shade this area — a larger shaded region means more energy available for convection.

Quantitatively, CAPE is measured in joules per kilogram (J/kg) and represents the maximum kinetic energy a parcel could gain from buoyancy if lifted through the entire unstable layer. Values below 1000 J/kg indicate weak instability; 1000–2500 J/kg is moderate; and values above 2500 J/kg signal an environment capable of producing violent thunderstorms. To convert CAPE to a maximum updraft speed, use the relation w = √(2 × CAPE) — so 2500 J/kg yields a theoretical maximum updraft of about 70 m/s, strong enough to loft hail and sustain supercell thunderstorms.

However, CAPE is a necessary but not sufficient condition for severe weather. A deep, moist atmosphere with high CAPE but no wind shear will produce ordinary, short-lived thunderstorms that quickly rain themselves out. It is the combination of CAPE (the fuel) with vertical wind shear (which tilts the updraft, separating it from the downdraft) that produces organized, long-lived convection like supercells and squall lines. Forecasters also consider **Convective Inhibition (CIN)** — the negative area below the LFC where the parcel is cooler than the environment and must be forced upward. High CIN acts as a cap: it prevents convection from initiating easily, but once the cap is broken (by heating, a front, or terrain), the stored CAPE is released explosively. This is why some of the most violent storms occur on days with moderate CIN and very high CAPE — the cap holds instability in check until it breaks, then convection erupts violently.
