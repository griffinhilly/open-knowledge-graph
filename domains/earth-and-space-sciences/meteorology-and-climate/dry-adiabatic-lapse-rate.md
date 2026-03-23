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
stage: formal-systems
status: validated
---

# Dry Adiabatic Lapse Rate

## Core Idea
The dry adiabatic lapse rate (~9.8 K/km) describes how temperature changes when unsaturated air parcel rises or descends adiabatically without external heat exchange. This rate is nearly constant regardless of latitude or initial air mass properties, making it a fundamental reference for atmospheric stability analysis. It arises from balancing gravitational potential energy with internal energy in the air parcel.

## How It's Best Learned
Derive the dry adiabatic lapse rate from the first law of thermodynamics applied to an air parcel. Use thermodynamic diagrams (skew-T plots) to visualize adiabatic processes.

## Common Misconceptions
- Confusing the dry adiabatic lapse rate with the environmental lapse rate; they are independent quantities. - Thinking the rate depends on initial temperature or pressure; it is independent of these initial conditions for dry air.

## Questions

```yaml
- question: "On a given day, a weather balloon measures the environmental lapse rate as 12°C/km. A dry air parcel is given an initial upward push. What happens next?"
  type: multiple-choice
  options:
    - "The parcel returns to its original level — the environment is cooling faster, so the parcel quickly becomes cooler than its surroundings"
    - "The parcel continues rising on its own — it cools at 9.8°C/km while the environment cools at 12°C/km, keeping the parcel warmer and more buoyant"
    - "The parcel cools at 12°C/km to match the environment, remaining neutrally buoyant"
    - "The parcel stops rising when it reaches the altitude where its temperature equals the dry adiabatic lapse rate"
  answer: 1
  explanation: "Stability is determined by comparing the parcel's temperature to the environment's temperature at each altitude. The parcel cools at 9.8°C/km (DALR). The environment cools faster (12°C/km), so at any altitude above the start, the environment is colder than the parcel. A warmer parcel is less dense and buoyant — it keeps rising without further forcing. This is the unstable condition. Option A has the logic backwards. Option C is wrong: the parcel always cools at the DALR, not the environmental rate — these are independent."

- question: "A Chinook wind event brings warm air to a valley after air crossed a mountain range and descended 3,000 meters dry-adiabatically. Approximately how much warmer is the descending air than it was at the same altitude on the windward side?"
  type: multiple-choice
  options:
    - "About 9.8°C warmer — adiabatic warming only applies over 1 km"
    - "About 14.7°C warmer — half the descent distance times the lapse rate"
    - "About 29.4°C warmer — 3 km × 9.8°C/km"
    - "No warmer — temperature changes on ascent and descent cancel exactly"
  answer: 2
  explanation: "Dry adiabatic descent warms air at 9.8°C per kilometer. Over 3,000 m (3 km): 3 × 9.8 = 29.4°C of warming. This is why Chinook winds can dramatically warm valleys. Note that option D would hold only if ascent and descent were both dry-adiabatic. If the air shed moisture as orographic precipitation on the windward side (ascending at the moist adiabatic rate, which is smaller), the net effect is a temperature gain — the air arrives warmer than it started."

- question: "The dry adiabatic lapse rate describes the actual temperature profile of the atmosphere at a given location and time."
  type: true-false
  answer: false
  explanation: "This is the most important misconception to avoid. The DALR (~9.8°C/km) describes how a specific rising air parcel cools due to adiabatic expansion — it is a property of the parcel's thermodynamic process, not of the atmosphere around it. The actual atmospheric temperature profile is the environmental lapse rate (ELR), which varies by location and time based on solar heating, advection, and moisture. The DALR and ELR are independent quantities, and comparing them is how meteorologists assess atmospheric stability."

- question: "A dry air parcel starting at 25°C at sea level and one starting at 0°C at a 2,000-meter plateau cool at different rates as they rise, because their initial temperatures differ."
  type: true-false
  answer: false
  explanation: "The dry adiabatic lapse rate is constant at approximately 9.8°C/km regardless of initial temperature, initial pressure, or geographic location. The rate depends only on gravitational acceleration (g) and the specific heat capacity of dry air at constant pressure (Cp) — both effectively constant throughout the lower atmosphere. Initial conditions determine the parcel's temperature at each altitude but not the rate of cooling."

- question: "Why does an air parcel cool as it rises in the atmosphere, and what source of energy drives this cooling?"
  type: short-answer
  answer: "As a parcel rises, surrounding atmospheric pressure decreases, so the parcel expands. This expansion requires the air molecules to do work pushing outward against lower external pressure. If the process is adiabatic (no heat exchanged with surroundings), the energy for this work comes from the parcel's own internal thermal energy — the molecules slow down on average and temperature drops. The cooling is a conversion of internal (thermal) energy into the mechanical work of expansion, with total energy conserved."
  explanation: "The reverse — compression warming during descent — follows the same logic. As air descends, it compresses, and work is done ON the parcel, converting mechanical energy back into thermal energy at the same 9.8°C/km rate. This symmetric process explains both Chinook warming and the constancy of the rate regardless of direction."
```

## Explainer

From your understanding of atmospheric pressure and altitude, you know that pressure decreases with height because there is less air above to weigh down on a given level. From thermochemistry and enthalpy, you know that energy is conserved during processes and that work done by or on a gas changes its temperature. The dry adiabatic lapse rate connects these ideas: it describes exactly how much an air parcel cools as it rises through the atmosphere, and this single number — roughly 9.8°C per kilometer — is the foundation of atmospheric stability analysis.

Imagine lifting a balloon of dry air upward. As it ascends, the surrounding atmospheric pressure drops, so the air inside the balloon expands. That expansion requires the air molecules to do work pushing outward against lower external pressure. If no heat enters or leaves the parcel (the definition of **adiabatic**), the energy for this work must come from the air's own internal thermal energy. The molecules slow down, and the temperature drops. The remarkable result is that this cooling rate is nearly constant — about 9.8°C for every kilometer of ascent — regardless of the starting temperature, starting pressure, or geographic location. A parcel beginning at 30°C at sea level and one beginning at −10°C at a mountaintop both cool at the same rate as they rise further. The constancy comes from the physics: the rate depends only on the gravitational acceleration and the specific heat capacity of dry air, both of which are effectively constant in the lower atmosphere.

The reverse is equally important. When air descends — perhaps forced down the lee side of a mountain or sinking in a high-pressure system — it compresses and warms at the same 9.8°C/km rate. This is why **downslope winds** like the Chinook or Föhn can bring dramatic warming: air forced over a mountain range and back down arrives much warmer than the ambient air at the same altitude on the leeward side.

The dry adiabatic lapse rate is a theoretical reference line, not a description of the actual atmosphere. The **environmental lapse rate** — the temperature profile you would measure by sending up a weather balloon — varies from place to place and hour to hour depending on solar heating, advection, and moisture. Comparing the two is how meteorologists assess stability: if the environment cools faster than 9.8°C/km, a rising dry parcel stays warmer than its surroundings and keeps accelerating upward (unstable). If the environment cools more slowly, the parcel becomes cooler and denser than its surroundings, and convection is suppressed (stable). This comparison is the entry point for understanding why thunderstorms erupt on some days and not others, and it sets the stage for the moist adiabatic lapse rate, where condensation changes the game entirely.
