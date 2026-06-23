---
id: sound-speed-temperature-and-media
title: 'Sound Speed: Temperature and Medium Dependence'
domain: physics
course: waves-and-optics
prerequisites:
- id: sound-waves-longitudinal
  type: hard
- id: how-sound-travels
  type: soft
- id: sound-properties-and-speed
  type: soft
- id: wave-speed-elastic-media
  type: soft
builds-toward:
- doppler-shift-observer-motion
tags:
- sound-speed
- temperature
- media
stage: advanced
status: validated
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

## Questions

```yaml
- question: "Sound travels through steel (~5,000 m/s) much faster than through air (~340 m/s). What is the primary reason?"
  type: multiple-choice
  options:
    - "Steel is denser than air, and denser media carry sound faster"
    - "Steel has a much higher elastic modulus relative to its density than air does"
    - "Steel molecules are closer together, so vibrations transfer more quickly"
    - "Sound travels faster in solids because solids are at a higher temperature than air"
  answer: 1
  explanation: "Sound speed is v = √(elastic modulus / density). Steel is far denser than air, which alone would slow sound down. But steel's elastic modulus — its resistance to compression — is enormously larger than air's, and this increase dominates. The ratio (modulus/density) is much larger for steel than for air, so sound is faster in steel. Proximity of molecules (option C) is a folk explanation that doesn't hold up — what matters is not spacing but the mechanical stiffness of the medium relative to its mass."

- question: "Air temperature rises from 0°C to 100°C (273 K to 373 K). By approximately what factor does the speed of sound in air increase?"
  type: multiple-choice
  options:
    - "By a factor of about 1.04 — speed increases very slightly with temperature"
    - "By a factor of about 1.17 — speed increases as the square root of absolute temperature"
    - "By a factor of about 1.37 — speed increases proportionally to absolute temperature"
    - "By a factor of about 2 — sound speed doubles when temperature doubles in Celsius"
  answer: 1
  explanation: "Speed is proportional to √T (absolute temperature). The ratio is √(373/273) ≈ √1.366 ≈ 1.17, so sound is about 17% faster. The key error in option C is treating speed as proportional to T rather than √T. Option D conflates Celsius ratios with Kelvin ratios: 'doubling' from 0°C to 100°C is not a temperature doubling in absolute terms — 0°C is 273 K, so the ratio is 373/273 ≈ 1.37, not 2."

- question: "The statement 'sound travels faster in denser materials' is generally true."
  type: true-false
  answer: false
  explanation: "This is one of the most persistent misconceptions in wave physics. Sound speed depends on the ratio of elastic modulus to density, not on density alone. Lead is much denser than aluminum, yet sound travels faster in aluminum because aluminum's elastic modulus is higher relative to its density. Air has very low density, yet sound is slow in it because its elastic modulus (bulk modulus) is also tiny. Density in the denominator of v = √(modulus/density) actually works against speed — it is the stiffness term in the numerator that must overcome density to produce fast propagation."

- question: "Humid air carries sound faster than dry air, even though water is heavier than nitrogen."
  type: true-false
  answer: true
  explanation: "This seems counterintuitive but is correct. Water vapor molecules (molar mass 18 g/mol) are lighter than the N₂ (28 g/mol) and O₂ (32 g/mol) they displace in humid air. Because sound speed in a gas is v = √(γRT/M) and M (molar mass) is in the denominator, replacing heavier molecules with lighter water vapor lowers the effective molar mass and increases sound speed. The effect is small (~0.3% at full saturation) but real. The misconception — that heavier water makes sound slower — ignores that individual water molecules are actually lighter than the diatomic molecules they replace."

- question: "Why does the formula for sound speed in a gas include the square root of absolute temperature rather than just temperature, and what physical phenomenon does this reflect?"
  type: short-answer
  answer: "Sound speed in a gas is v = √(γRT/M). The square root of temperature appears because sound speed is proportional to the average molecular speed (or more precisely, the root-mean-square molecular speed), which itself scales as √T from the kinetic theory of gases. Temperature measures the average kinetic energy (½mv² ∝ T), so molecular speed scales as √T. Hotter molecules hit their neighbors harder and more frequently, propagating pressure disturbances faster — but the relationship is sublinear (square root) because it is speed, not energy, that governs propagation."
  explanation: "The √T dependence is not an arbitrary formula feature; it reflects the microscopic mechanism of sound propagation. A compression wave moves at a speed set by how fast energy can be handed off between neighboring molecules. That transfer rate scales with molecular kinetic speed, which is √(kT/m) by kinetic theory. This is why doubling absolute temperature increases sound speed by only ~41% (√2 ≈ 1.41), not by 100%."
```

## Explainer

You already know from your study of longitudinal waves that sound is a pressure disturbance that propagates by each layer of a medium compressing the next. The speed of that propagation depends on two competing factors: how strongly the medium pushes back when compressed (the **restoring force**, captured by the elastic modulus or bulk modulus), and how much inertia that medium has (its density). Sound travels fast when the medium is stiff and light, and slow when it is soft and heavy. The general formula is v = √(elastic modulus / density), and every specific formula for sound speed in a particular medium is a version of this ratio.

In a gas like air, the relevant modulus is determined by how pressure changes when the gas is compressed. Temperature enters because it controls how fast the gas molecules are moving: hotter molecules have more kinetic energy and slam into their neighbors more forcefully, so compressions propagate faster. The formula v = √(γRT/M) makes this precise — speed is proportional to √T (absolute temperature), meaning that raising the temperature from 0°C (273 K) to 20°C (293 K) increases sound speed by about 3.5%. This is why a symphony orchestra sounds slightly sharp when the hall warms up during a concert.

In liquids and solids, the same elasticity-over-density logic applies, but the numbers are very different. Steel has an extremely high elastic modulus — it resists compression strongly — and sound travels through it at about 5,000 m/s, roughly fifteen times faster than through air. Water is less stiff than steel but still far stiffer than air under compression, giving sound a speed of about 1,480 m/s. The common misconception that "denser = faster" gets things backward: steel is much denser than air, yet sound is much faster in steel because the elastic modulus increases even more dramatically with material stiffness. The ratio is what governs speed, not either factor alone.

Humidity is a smaller but real effect: water vapor (H₂O, molar mass 18 g/mol) is lighter than the nitrogen and oxygen it displaces in air (molar masses 28 and 32 g/mol). Because the speed formula has M (molar mass) in the denominator, replacing heavier molecules with lighter water vapor slightly increases sound speed. At 100% humidity compared to dry air, this adds roughly 0.3% to the speed — small but measurable in precision acoustics. The broader lesson is that sound speed is a property of the medium, encoding its microscopic mechanical response, and any factor that alters the effective stiffness or inertia of that medium will shift the speed accordingly.
