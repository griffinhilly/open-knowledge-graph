---
id: sound-speed-temperature-and-media
title: 'Sound Speed: Temperature and Medium Dependence'
domain: physics
course: waves-and-optics
prerequisites:
- id: sound-waves-longitudinal
  type: hard
builds-toward:
- doppler-shift-observer-motion
tags:
- sound-speed
- temperature
- media
stage: formal-systems
status: draft
---

# Sound Speed: Temperature and Medium Dependence

## Core Idea
Sound speed in gases is proportional to √T (absolute temperature), so speed increases with temperature: v = √(γRT/M) where γ is heat capacity ratio, R is gas constant, T is temperature, and M is molar mass. In solids and liquids, speed depends on elastic modulus and density. Sound travels slower in less dense materials and faster in stiffer materials.

## How It's Best Learned
Measure sound speed using a resonance tube at different temperatures. Create a Kundt's tube to observe sound wavelengths in different gases.

## Common Misconceptions
- Higher temperature means sound always travels faster; speed depends on medium properties, not just temperature.
- Sound travels faster in denser materials; speed depends on elasticity/density ratio, not density alone.
- Sound speed is independent of humidity; humidity actually affects sound speed in air.

## Explainer

You already know from your study of longitudinal waves that sound is a pressure disturbance that propagates by each layer of a medium compressing the next. The speed of that propagation depends on two competing factors: how strongly the medium pushes back when compressed (the **restoring force**, captured by the elastic modulus or bulk modulus), and how much inertia that medium has (its density). Sound travels fast when the medium is stiff and light, and slow when it is soft and heavy. The general formula is v = √(elastic modulus / density), and every specific formula for sound speed in a particular medium is a version of this ratio.

In a gas like air, the relevant modulus is determined by how pressure changes when the gas is compressed. Temperature enters because it controls how fast the gas molecules are moving: hotter molecules have more kinetic energy and slam into their neighbors more forcefully, so compressions propagate faster. The formula v = √(γRT/M) makes this precise — speed is proportional to √T (absolute temperature), meaning that raising the temperature from 0°C (273 K) to 20°C (293 K) increases sound speed by about 3.5%. This is why a symphony orchestra sounds slightly sharp when the hall warms up during a concert.

In liquids and solids, the same elasticity-over-density logic applies, but the numbers are very different. Steel has an extremely high elastic modulus — it resists compression strongly — and sound travels through it at about 5,000 m/s, roughly fifteen times faster than through air. Water is less stiff than steel but still far stiffer than air under compression, giving sound a speed of about 1,480 m/s. The common misconception that "denser = faster" gets things backward: steel is much denser than air, yet sound is much faster in steel because the elastic modulus increases even more dramatically with material stiffness. The ratio is what governs speed, not either factor alone.

Humidity is a smaller but real effect: water vapor (H₂O, molar mass 18 g/mol) is lighter than the nitrogen and oxygen it displaces in air (molar masses 28 and 32 g/mol). Because the speed formula has M (molar mass) in the denominator, replacing heavier molecules with lighter water vapor slightly increases sound speed. At 100% humidity compared to dry air, this adds roughly 0.3% to the speed — small but measurable in precision acoustics. The broader lesson is that sound speed is a property of the medium, encoding its microscopic mechanical response, and any factor that alters the effective stiffness or inertia of that medium will shift the speed accordingly.
