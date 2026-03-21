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

## Questions

```yaml
- question: "Sound travels about 4.4 times faster in water (~1500 m/s) than in air (~340 m/s), even though water is approximately 800 times denser than air. The best explanation is:"
  type: multiple-choice
  options:
    - "Sound waves in water are transverse while in air they are longitudinal, making them faster"
    - "Water's bulk modulus is approximately 10,000 times greater than air's, more than compensating for the higher density"
    - "Denser media always carry sound faster because more mass is available to transmit the wave"
    - "Water molecules are closer together, so each vibration travels a shorter distance between collisions"
  answer: 1
  explanation: "Wave speed = √(bulk modulus / density). Water is ~800× denser than air, which alone would make it slower by √800 ≈ 28×. But water's bulk modulus is ~10,000× greater than air's, which alone would make it faster by √10000 = 100×. The ratio favors water: √(10000/800) ≈ 3.5, consistent with the observed 4.4× difference. Option C states the common misconception — density alone does not determine speed. Sound waves in both water and air are longitudinal."

- question: "A new elastic material has twice the bulk modulus and four times the density of steel. Compared to steel, the wave speed in this material is:"
  type: multiple-choice
  options:
    - "Twice the speed of steel (modulus doubled)"
    - "1/√2 times the speed of steel (approximately 0.71×)"
    - "The same speed as steel (factors cancel)"
    - "Four times the speed of steel (density quadrupled)"
  answer: 1
  explanation: "v = √(B/ρ). If the new material has B' = 2B and ρ' = 4ρ, then v' = √(2B/4ρ) = √(B/2ρ) = v/√2 ≈ 0.71v. Doubling the modulus increases speed by √2; quadrupling density decreases speed by 2. The net effect is a factor of √2/2 = 1/√2. This illustrates that both properties matter and must be considered together — doubling the modulus does not simply double the speed."

- question: "Whether a medium transmits waves faster or slower than another medium depends on the ratio of elastic modulus to density — not on either property alone."
  type: true-false
  answer: true
  explanation: "This is the central insight: v = √(stiffness/density). A medium can be denser yet faster (like water vs. air) if its stiffness increases proportionally more. A medium can be lighter yet slower if it is also much less stiff. Neither density nor stiffness alone predicts wave speed; only their ratio does. This is why intuitions like 'denser = slower' or 'stiffer = faster' are incomplete without the other factor."

- question: "A denser medium always transmits sound more slowly than a less dense medium."
  type: true-false
  answer: false
  explanation: "This is the classic misconception. Density is in the denominator of v = √(B/ρ), so higher density does decrease speed — all else being equal. But all else is rarely equal. Water is ~800× denser than air yet transmits sound ~4.4× faster, because its bulk modulus is ~10,000× greater. Steel is denser than water yet transmits sound even faster (~5100 m/s) because its elastic modulus is orders of magnitude higher. The correct statement is: higher density decreases wave speed, but this effect can be overwhelmed by a sufficiently higher elastic modulus."

- question: "Explain the physical logic behind the formula v = √(stiffness/density). Why does higher stiffness increase wave speed, and why does higher density decrease it?"
  type: short-answer
  answer: "A wave propagates when each layer of the medium disturbs the next. A stiffer medium transmits the restoring force more forcefully to its neighbors, so the disturbance moves along faster — stiffness is in the numerator. A denser medium has greater inertia per unit volume, so each layer accelerates more sluggishly in response to the same restoring force — density is in the denominator. The formula v = √(stiffness/density) captures this competition: speed increases with stiffness and decreases with density, with both appearing under a square root because the relationship derives from Newton's second law."
  explanation: "The square root comes from dimensional analysis and the underlying wave equation derivation (applying F = ma to an infinitesimal slice of the medium). Neither factor acts independently — doubling stiffness multiplies speed by √2, while doubling density divides speed by √2. The same structural formula v = √(elastic property / inertial property) appears for all mechanical wave types (sound in fluids, waves on strings, seismic waves), making it a universal pattern worth internalizing."
```

## Explainer

From the wavelength-frequency-speed relationship, you know that wave speed is a property of the medium — changing the frequency of a wave doesn't change its speed, it changes its wavelength instead. But what property of the medium determines speed? For mechanical waves, the answer involves a competition between two opposing tendencies: the medium's tendency to snap back when disturbed (its **stiffness** or elastic modulus) and its tendency to resist changes in motion (its **inertia** or density). Stiffer media transmit waves faster; denser media transmit waves slower. The formula v = √(elastic modulus / density) captures this competition exactly.

The physical logic is intuitive once you think about what a wave actually does. A wave propagates by each layer of the medium disturbing the next. A stiffer medium transmits the restoring force more forcefully to the next layer, so the disturbance moves along faster. A denser medium has more inertia per unit volume, so each layer accelerates more sluggishly in response to the force — the wave moves slower. The formula v = √(stiffness/density) means that doubling stiffness multiplies speed by √2, while doubling density divides speed by √2. Neither property alone determines the speed; the ratio is what matters.

This same structural form v = √(elastic property / inertial property) appears across all mechanical wave types. For longitudinal waves (sound) in a fluid, the elastic property is the **bulk modulus** B (resistance to compression), and v = √(B/ρ). For waves on a stretched string, v = √(tension / linear density). The specific elastic property changes with the wave type, but the structural formula is universal. This makes it a powerful pattern to internalize: when you encounter a new mechanical wave type, you can immediately identify the relevant elastic and inertial properties and predict how speed will respond to changes in each.

The classic counterintuitive example is sound in water versus air. Water is about 800 times denser than air — yet sound travels about 4.4 times faster in water (~1500 m/s vs ~340 m/s). The reason: water's bulk modulus is roughly 10,000 times larger than air's. The stiffness advantage overwhelmingly outweighs the density disadvantage. Steel pushes this even further: it is about 8 times denser than water but has a bulk modulus thousands of times higher, so sound in steel travels at ~5100 m/s. The lesson is that density alone is a misleading predictor of wave speed. What matters is the ratio — and that ratio can surprise you.
