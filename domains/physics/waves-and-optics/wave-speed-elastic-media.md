---
id: wave-speed-elastic-media
title: Wave Speed in Elastic Media
domain: physics
course: waves-and-optics
prerequisites:
- id: wavelength-frequency-speed-relationship
  type: hard
builds-toward:
- sound-speed-temperature-and-media
- acoustic-impedance-mechanical
tags:
- wave-speed
- medium-properties
- elasticity
stage: formal-systems
status: draft
---

# Wave Speed in Elastic Media

## Core Idea
Wave speed in a medium depends on the medium's elastic properties and inertia: v = √(stiffness/density). For sound in gases, liquids, and solids, this relationship explains why sound travels faster in denser elastic media.

## How It's Best Learned
Compare sound speeds in air, water, and steel to see the pattern. Derive the relationship from Newton's second law and Hooke's law.

## Common Misconceptions
- Thinking sound travels faster in denser media without considering elasticity; density alone doesn't determine speed.
- Confusing sound speed with particle velocity in the wave.

## Explainer

From the wavelength-frequency-speed relationship, you know that wave speed is a property of the medium — changing the frequency of a wave doesn't change its speed, it changes its wavelength instead. But what property of the medium determines speed? For mechanical waves, the answer involves a competition between two opposing tendencies: the medium's tendency to snap back when disturbed (its **stiffness** or elastic modulus) and its tendency to resist changes in motion (its **inertia** or density). Stiffer media transmit waves faster; denser media transmit waves slower. The formula v = √(elastic modulus / density) captures this competition exactly.

The physical logic is intuitive once you think about what a wave actually does. A wave propagates by each layer of the medium disturbing the next. A stiffer medium transmits the restoring force more forcefully to the next layer, so the disturbance moves along faster. A denser medium has more inertia per unit volume, so each layer accelerates more sluggishly in response to the force — the wave moves slower. The formula v = √(stiffness/density) means that doubling stiffness multiplies speed by √2, while doubling density divides speed by √2. Neither property alone determines the speed; the ratio is what matters.

This same structural form v = √(elastic property / inertial property) appears across all mechanical wave types. For longitudinal waves (sound) in a fluid, the elastic property is the **bulk modulus** B (resistance to compression), and v = √(B/ρ). For waves on a stretched string, v = √(tension / linear density). The specific elastic property changes with the wave type, but the structural formula is universal. This makes it a powerful pattern to internalize: when you encounter a new mechanical wave type, you can immediately identify the relevant elastic and inertial properties and predict how speed will respond to changes in each.

The classic counterintuitive example is sound in water versus air. Water is about 800 times denser than air — yet sound travels about 4.4 times faster in water (~1500 m/s vs ~340 m/s). The reason: water's bulk modulus is roughly 10,000 times larger than air's. The stiffness advantage overwhelmingly outweighs the density disadvantage. Steel pushes this even further: it is about 8 times denser than water but has a bulk modulus thousands of times higher, so sound in steel travels at ~5100 m/s. The lesson is that density alone is a misleading predictor of wave speed. What matters is the ratio — and that ratio can surprise you.
