---
id: triple-point-and-phase-coexistence
title: Triple Point and Phase Coexistence
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: phase-diagrams
  type: soft
- id: phase-diagrams-thermodynamics
  type: soft
tags:
- triple-point
- phase-equilibrium
- three-phases
stage: advanced
status: validated
---
# Triple Point and Phase Coexistence

## Core Idea
The triple point is where solid, liquid, and gas phases coexist in equilibrium—a unique condition for each substance. For water, it occurs at 273.16 K and 611.7 Pa. The triple point is used as the definition of the Kelvin temperature scale, providing a fundamental reference standard.

## Questions

```yaml
- question: "For a pure substance (one component) with all three phases coexisting, the Gibbs phase rule gives F = 0. What does this imply about the triple point?"
  type: multiple-choice
  options:
    - "The triple point can occur over a range of temperatures at fixed pressure"
    - "The triple point is a single unique (T, P) coordinate — there are no free variables to adjust while maintaining three-phase coexistence"
    - "The triple point can only exist at atmospheric pressure"
    - "F = 0 means the system has zero entropy and is at absolute zero"
  answer: 1
  explanation: "F = C − P + 2 = 1 − 3 + 2 = 0. Zero degrees of freedom means there is no freedom to adjust temperature or pressure while maintaining three-phase coexistence. The triple point is thus a single point on the phase diagram — a specific (T, P) pair — not a line or region. This is why every substance has exactly one triple point, and why water's triple point (273.16 K, 611.7 Pa) is so reproducibly precise that it served as the definition of the Kelvin scale."

- question: "You heat a solid sample of a substance at a pressure below its triple point pressure. What phase transition sequence occurs?"
  type: multiple-choice
  options:
    - "Solid → liquid → gas, as usual"
    - "Solid → gas directly (sublimation), because the liquid phase is thermodynamically unstable below the triple point pressure"
    - "No transition occurs — the substance cannot change phase below the triple point pressure"
    - "Gas → solid (deposition), because low pressure favors the solid phase"
  answer: 1
  explanation: "Below the triple point pressure, the liquid phase does not appear on the phase diagram as a stable state. As you add heat to a solid at this pressure, you cross directly from the solid region into the vapor region — sublimation. This is exactly why dry ice (solid CO₂) sublimates at atmospheric pressure: CO₂'s triple point is at about 5.1 atm, well above atmospheric pressure, so at 1 atm the liquid phase of CO₂ is inaccessible regardless of temperature."

- question: "The triple point of water occurs at approximately atmospheric pressure (around 101,325 Pa)."
  type: true-false
  answer: false
  explanation: "False — water's triple point is at 611.7 Pa, which is less than 1% of atmospheric pressure (101,325 Pa). This is why we never observe all three phases of water coexisting in everyday conditions: atmospheric pressure is far above the triple point pressure, so as we heat ice at 1 atm, it melts to liquid before it can coexist with vapor. Only in a partial vacuum near 611.7 Pa and 273.16 K would you see ice, liquid water, and water vapor simultaneously."

- question: "The triple point of a pure substance is a fixed, apparatus-independent (T, P) coordinate that is a fundamental property of that substance."
  type: true-false
  answer: true
  explanation: "True — this is what makes the triple point scientifically powerful. Unlike the normal melting point or boiling point (which change with applied pressure and dissolved impurities), the triple point is defined by thermodynamic equilibrium of three phases, and the Gibbs phase rule guarantees it is fully determined (F = 0). Every sample of pure water, anywhere, will have its triple point at exactly 273.16 K and 611.7 Pa. This reproducibility made it the defining fixed point of the Kelvin temperature scale."

- question: "Explain using the Gibbs phase rule why the triple point is a single point rather than a line or region on the phase diagram."
  type: short-answer
  answer: "The Gibbs phase rule is F = C − P + 2, where F is degrees of freedom, C is the number of chemical components, and P is the number of coexisting phases. For a pure substance (C = 1) with three phases coexisting (P = 3): F = 1 − 3 + 2 = 0. Zero degrees of freedom means there are no intensive variables (temperature or pressure) that can be freely adjusted while maintaining three-phase coexistence. The state is completely determined — there is exactly one (T, P) pair where this can occur. A two-phase boundary has F = 1 (a line: you can vary T and P must adjust accordingly). With three phases, all freedom is exhausted and the result is a point."
  explanation: "Contrast with the melting curve: solid and liquid coexist (P = 2), giving F = 1, so coexistence is possible along an entire line of (T, P) pairs. Add a third phase and you lose the last degree of freedom — only one point satisfies all the simultaneous equilibrium conditions."
```

## Explainer

From your study of phase transitions, you know that matter changes state when it crosses a boundary on a phase diagram — for example, liquid water boils when you add enough heat at a given pressure. Each of those boundaries represents a pressure-temperature combination where two phases are in equilibrium simultaneously: ice and liquid water coexist along the melting curve, liquid and vapor coexist along the vaporization curve. The **triple point** is the one unique pressure-temperature combination where all three of those curves meet — meaning solid, liquid, and gas are all in equilibrium with each other at the exact same time.

For water, this happens at 273.16 K (just barely above 0°C) and 611.7 Pa — a pressure far below ordinary atmospheric pressure (101,325 Pa). This is why you've never seen ice, liquid water, and steam coexist in a kitchen pot: atmospheric pressure is far above the triple point pressure, so water goes from solid to liquid to vapor as you heat it in the usual way. But if you reduced the pressure enough — into a vacuum chamber near 611.7 Pa — and held the temperature at exactly 273.16 K, you'd see all three phases present simultaneously in stable equilibrium. **Phase coexistence** at the triple point is not a fleeting transition; it's a fixed thermodynamic state.

What makes the triple point scientifically powerful is its absolute reproducibility. Every substance has exactly one triple point — a single (T, P) coordinate that is a fundamental property of the material, not dependent on apparatus or calibration. For water, this reproducibility made it the definition of the Kelvin temperature scale for decades: 273.16 K was defined as the temperature of water's triple point, anchoring the entire absolute temperature scale to a natural physical phenomenon. Even though the SI redefined the kelvin in 2019 in terms of the Boltzmann constant, the triple point of water (273.16 K ± 0.0001 K) remains a primary thermometric calibration reference used in precision laboratories worldwide.

To see why no fourth coexistence point can exist, think about the **Gibbs phase rule**: F = C − P + 2, where F is degrees of freedom, C is number of components, and P is the number of phases present. For pure water (C = 1) with three phases coexisting (P = 3), F = 1 − 3 + 2 = 0. Zero degrees of freedom means the state is fully determined — there is no freedom to adjust temperature or pressure and still maintain three-phase coexistence. This is why the triple point is a single point, not a line or region. Below the triple point pressure, the liquid phase is thermodynamically unstable: matter transitions directly from solid to vapor (**sublimation**) without passing through the liquid state at all — exactly what happens to dry ice (CO₂) at atmospheric pressure, since CO₂'s triple point pressure is above one atmosphere.
