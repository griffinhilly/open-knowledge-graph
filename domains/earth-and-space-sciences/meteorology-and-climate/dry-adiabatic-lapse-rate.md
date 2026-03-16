---
id: dry-adiabatic-lapse-rate
title: Dry Adiabatic Lapse Rate
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: atmospheric-pressure-and-altitude
  type: hard
- id: thermochemistry-enthalpy
  type: hard
builds-toward:
- moist-adiabatic-lapse-rate
- atmospheric-inversion-temperature
- environmental-lapse-rate
tags:
- thermodynamics
- adiabatic
- temperature
- lapse-rate
stage: abstract-reasoning
status: draft
---

# Dry Adiabatic Lapse Rate

## Core Idea
The dry adiabatic lapse rate (~9.8 K/km) describes how temperature changes when unsaturated air parcel rises or descends adiabatically without external heat exchange. This rate is nearly constant regardless of latitude or initial air mass properties, making it a fundamental reference for atmospheric stability analysis. It arises from balancing gravitational potential energy with internal energy in the air parcel.

## How It's Best Learned
Derive the dry adiabatic lapse rate from the first law of thermodynamics applied to an air parcel. Use thermodynamic diagrams (skew-T plots) to visualize adiabatic processes.

## Common Misconceptions
- Confusing the dry adiabatic lapse rate with the environmental lapse rate; they are independent quantities. - Thinking the rate depends on initial temperature or pressure; it is independent of these initial conditions for dry air.

## Explainer

From your understanding of atmospheric pressure and altitude, you know that pressure decreases with height because there is less air above to weigh down on a given level. From thermochemistry and enthalpy, you know that energy is conserved during processes and that work done by or on a gas changes its temperature. The dry adiabatic lapse rate connects these ideas: it describes exactly how much an air parcel cools as it rises through the atmosphere, and this single number — roughly 9.8°C per kilometer — is the foundation of atmospheric stability analysis.

Imagine lifting a balloon of dry air upward. As it ascends, the surrounding atmospheric pressure drops, so the air inside the balloon expands. That expansion requires the air molecules to do work pushing outward against lower external pressure. If no heat enters or leaves the parcel (the definition of **adiabatic**), the energy for this work must come from the air's own internal thermal energy. The molecules slow down, and the temperature drops. The remarkable result is that this cooling rate is nearly constant — about 9.8°C for every kilometer of ascent — regardless of the starting temperature, starting pressure, or geographic location. A parcel beginning at 30°C at sea level and one beginning at −10°C at a mountaintop both cool at the same rate as they rise further. The constancy comes from the physics: the rate depends only on the gravitational acceleration and the specific heat capacity of dry air, both of which are effectively constant in the lower atmosphere.

The reverse is equally important. When air descends — perhaps forced down the lee side of a mountain or sinking in a high-pressure system — it compresses and warms at the same 9.8°C/km rate. This is why **downslope winds** like the Chinook or Föhn can bring dramatic warming: air forced over a mountain range and back down arrives much warmer than the ambient air at the same altitude on the leeward side.

The dry adiabatic lapse rate is a theoretical reference line, not a description of the actual atmosphere. The **environmental lapse rate** — the temperature profile you would measure by sending up a weather balloon — varies from place to place and hour to hour depending on solar heating, advection, and moisture. Comparing the two is how meteorologists assess stability: if the environment cools faster than 9.8°C/km, a rising dry parcel stays warmer than its surroundings and keeps accelerating upward (unstable). If the environment cools more slowly, the parcel becomes cooler and denser than its surroundings, and convection is suppressed (stable). This comparison is the entry point for understanding why thunderstorms erupt on some days and not others, and it sets the stage for the moist adiabatic lapse rate, where condensation changes the game entirely.
