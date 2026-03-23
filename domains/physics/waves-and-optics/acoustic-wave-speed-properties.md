---
id: acoustic-wave-speed-properties
title: Sound Wave Speed and Temperature Dependence
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relation
  type: hard
- id: kinetic-theory-of-gases
  type: soft
builds-toward:
- vibrating-string-normal-modes
- vibrating-air-column-modes
tags:
- sound
- acoustics
- temperature
stage: advanced
status: validated
---

# Sound Wave Speed and Temperature Dependence

## Core Idea
Sound speed in an ideal gas is v = √(γRT/M), depending on the gas's adiabatic index γ, temperature T, and molar mass M. In air at 20°C, v ≈ 343 m/s. Speed is independent of pressure but increases with temperature (≈ 0.6 m/s per °C in air). Sound travels faster in solids and liquids due to stronger intermolecular forces.

## Questions

```yaml
- question: "A student claims that compressing air to twice its pressure should make sound travel faster, because the air is more 'energetic.' What does the formula v = √(γRT/M) say about this?"
  type: multiple-choice
  options:
    - "The student is correct — higher pressure increases molecular collisions, raising speed"
    - "Partially correct — higher pressure increases speed, but only by √2"
    - "Incorrect — pressure does not appear in the formula; doubling pressure also doubles density, and these effects cancel exactly in an ideal gas"
    - "Incorrect — only molar mass M matters; pressure and temperature are irrelevant at constant volume"
  answer: 2
  explanation: "The formula v = √(γRT/M) contains no pressure term. For an ideal gas, the elastic modulus of the gas (the 'stiffness') is proportional to pressure γP, while density is also proportional to pressure ρ = PM/(RT). When you form the ratio stiffness/density, pressure cancels, leaving v = √(γRT/M). This is why sound speed in air is the same at sea level and at altitude (if temperature is the same), despite very different pressures."

- question: "In which medium does sound travel fastest?"
  type: multiple-choice
  options:
    - "Air at high pressure, because compressed air has more molecules to transmit the disturbance"
    - "Water, because it is much denser than air"
    - "Steel, because its elastic stiffness far outweighs the penalty of its higher density"
    - "Helium gas, because its low molar mass makes molecules lighter and faster"
  answer: 2
  explanation: "Sound speed = √(stiffness/inertia). Steel has an elastic modulus roughly a million times larger than air; even though it is also ~7,000 times denser, stiffness wins decisively, giving ~5,100 m/s. Water (~1,480 m/s) beats air for the same reason. Helium is faster than air (~970 m/s vs ~343 m/s) because of its low molar mass, but this still falls far short of solids. The key insight is that stiffness, not density, is the dominant factor."

- question: "Sound travels faster at higher temperatures because warmer gas molecules move faster and transmit pressure disturbances more quickly through the medium."
  type: true-false
  answer: true
  explanation: "This is the correct physical intuition. Temperature is a measure of average molecular kinetic energy; higher temperature means molecules are moving faster, colliding more frequently, and propagating pressure pulses more rapidly. The formula v = √(γRT/M) confirms this: v is proportional to √T. In air, speed rises by roughly 0.6 m/s per °C."

- question: "Because steel is far denser than water, sound travels more slowly in steel than in water."
  type: true-false
  answer: false
  explanation: "Sound speed depends on the ratio of elastic stiffness to inertia (density). Steel is indeed denser than water, but its elastic modulus (stiffness) is enormously larger — roughly 200 GPa vs. ~2 GPa for water. The stiffness advantage overwhelms the density penalty: sound travels at ~5,100 m/s in steel versus ~1,480 m/s in water. This counterintuitive result is why denser does not mean slower for sound."

- question: "Why does doubling the air pressure at constant temperature not change the speed of sound?"
  type: short-answer
  answer: "Doubling pressure also doubles the density of the air (from PV = nRT, at constant T and V, density ∝ P). The elastic restoring force scales with pressure (the bulk modulus of an ideal gas is γP), while the inertia scales with density (also ∝ P). In the formula v = √(bulk modulus / density), both numerator and denominator double and the ratio stays constant. Speed depends on temperature and molecular properties, not on pressure."
  explanation: "This is a key test of whether students understand the formula mechanically versus conceptually. Many students expect denser or more compressed air to carry sound better, but the cancellation is exact for ideal gases. The only way to change sound speed is to change temperature (which changes molecular velocities) or the gas itself (different γ or M)."
```

## Explainer

From your study of the wavelength-frequency-speed relation, you know that v = fλ — wave speed connects how rapidly a pattern oscillates in time (frequency) with how it stretches in space (wavelength). But what sets the speed itself? For mechanical waves, the answer is always the same in form: speed depends on how stiff or elastic the medium is relative to how massive it is. A stiffer medium responds faster, and a lighter medium accelerates more readily. For sound in an ideal gas, this gives v = √(γRT/M), where the numerator captures the elastic restoring force (via the adiabatic index γ and thermal energy RT) and the denominator M captures the inertia of the gas molecules.

The kinetic theory of gases you've encountered provides the intuition here. Temperature measures the average kinetic energy of gas molecules. Higher temperature means molecules are moving faster on average, which means they collide and transmit pressure disturbances — sound pulses — more quickly. This is why the sound speed in air rises by roughly 0.6 m/s for every 1°C increase in temperature. On a hot summer day (35°C), sound travels about 351 m/s; on a cold winter morning (−10°C), it falls to about 325 m/s. The speed depends on molecular activity, not on how compressed the air is — doubling the pressure also roughly doubles the density, and the two effects cancel exactly for an ideal gas.

A surprising consequence is medium dependence. Steel is far stiffer than air — its elastic modulus is roughly a million times larger — and while it is also denser, the stiffness wins decisively. Sound in steel travels at about 5,100 m/s, nearly 15 times faster than in air. In water, sound travels at about 1,480 m/s. This is why you can hear a distant train before you feel the vibration in the rails: the rails deliver the sound in a fraction of the time the air does. In all cases, the underlying mechanism is the same — elastic restoring forces transmit the disturbance, and **wave speed** is determined by the ratio of stiffness to inertia in the medium.

Understanding acoustic speed is foundational for the vibrating string and air column problems you will encounter next. In those contexts, the medium's sound speed sets the natural frequencies — the normal modes. A longer column of air or a longer string has lower-frequency resonances not because of any change in wave speed, but because the wavelengths of standing waves scale with the physical dimensions. You will apply v = fλ in those situations with the wave speed fixed by the medium's properties — the groundwork you've established here.

