---
id: impedance-matching-and-reflection
title: Impedance Matching and Wave Reflection at Boundaries
domain: physics
course: waves-and-optics
prerequisites:
- id: acoustic-impedance-mechanical
  type: hard
builds-toward:
- total-internal-reflection
tags:
- reflection
- impedance-mismatch
- boundary-conditions
stage: formal-systems
status: validated
---

# Impedance Matching and Wave Reflection at Boundaries

## Core Idea
When a wave encounters a boundary between two media with different impedances, part of the wave reflects and part transmits. The reflection coefficient depends on impedance ratio: R = (Z₂ - Z₁)/(Z₂ + Z₁). Impedance matching (Z₁ = Z₂) eliminates reflection.

## Questions

```yaml
- question: "A wave travels from a medium with impedance Z₁ = 4 into a medium with impedance Z₂ = 12. What is the reflection coefficient R?"
  type: multiple-choice
  options:
    - "R = 0.5"
    - "R = -0.5"
    - "R = 1/3"
    - "R = -1/3"
  answer: 0
  explanation: "R = (Z₂ - Z₁)/(Z₂ + Z₁) = (12 - 4)/(12 + 4) = 8/16 = 0.5. Since Z₂ > Z₁, R is positive — no phase inversion. The reflected wave has the same phase as the incident wave. Option C inverts the formula; option B confuses the sign convention."

- question: "An engineer measures that the amplitude of a transmitted wave is larger than the amplitude of the incident wave at an impedance boundary. What does this tell us about energy conservation?"
  type: multiple-choice
  options:
    - "Energy conservation is violated because the transmitted wave has more amplitude"
    - "The transmitted wave carries more power since power scales with amplitude"
    - "Energy is conserved because the transmitted medium has lower impedance, so higher amplitude can carry less power"
    - "This situation is impossible — transmitted amplitude can never exceed incident amplitude"
  answer: 2
  explanation: "Power is proportional to amplitude² × impedance. A wave entering a low-impedance medium can have larger amplitude while carrying less power, because the lower impedance factor compensates. The amplitude transmission coefficient t = 2Z₂/(Z₁+Z₂) can exceed 1 while the power transmission coefficient T = 1 − R² is always ≤ 1. Energy is fully conserved."

- question: "A wave reflecting from a boundary where Z₂ < Z₁ undergoes a phase inversion."
  type: true-false
  answer: true
  explanation: "When Z₂ < Z₁, the reflection coefficient R = (Z₂ − Z₁)/(Z₂ + Z₁) is negative. A negative R means the reflected wave is inverted in phase relative to the incident wave. This is why a string tied to a fixed wall (Z₂ → ∞) reflects with inversion, while a string attached to a free end (Z₂ = 0) reflects without inversion — both cases are captured by the sign of R."

- question: "Perfect impedance matching (Z₁ = Z₂) is impossible to achieve in practice, so reflection can only be minimized but never eliminated."
  type: true-false
  answer: false
  explanation: "Impedance matching can be exact. Two cable sections with identical characteristic impedance have zero reflection at their junction. Optical coatings and electrical matching networks can also achieve near-zero reflection. The formula R = (Z₂ − Z₁)/(Z₂ + Z₁) shows R = 0 exactly when Z₁ = Z₂, which is an achievable condition."

- question: "Why does an acoustic impedance mismatch between air and biological tissue cause nearly total reflection of sound waves at the skin surface, and how does ultrasound gel solve this problem?"
  type: short-answer
  answer: "Air has acoustic impedance ~400 Pa·s/m while tissue has ~1.5 × 10⁶ Pa·s/m — a ratio of ~3,750:1. Plugging into R = (Z₂ − Z₁)/(Z₂ + Z₁) gives R ≈ 1, so nearly all acoustic energy reflects. Ultrasound gel has impedance close to tissue, replacing the air-tissue boundary with a gel-tissue boundary where the impedance difference is small, dramatically reducing reflection and allowing sound to enter the body."
  explanation: "The reflection coefficient is determined by the ratio of impedances, not their absolute values. A large ratio produces near-total reflection regardless of actual impedance values. The gel acts as an impedance-matching intermediate layer — the same principle as a quarter-wave transformer in electronics or an anti-reflection coating on a lens."
```

## Explainer

From your study of acoustic impedance, you know that **impedance** Z characterizes how strongly a medium resists wave-driven motion — it combines the medium's density and elasticity (Z = ρv for acoustic waves, or more generally the ratio of a driving quantity to a flow quantity). The central insight of impedance matching is that what happens at a boundary depends entirely on the ratio of impedances on either side, not on the properties of each medium in isolation.

Think of a wave as a chain of coupled oscillators transmitting energy. When the chain suddenly encounters a region where each oscillator is much harder or easier to move (a different impedance), the incoming energy has a problem: the new medium "expects" a different ratio of force to velocity. Part of the wave reflects backward because it cannot be absorbed at the original ratio; part transmits forward at an adjusted amplitude. The **reflection coefficient** R = (Z₂ − Z₁)/(Z₂ + Z₁) captures this mismatch. Notice that R = 0 when Z₂ = Z₁ — perfect impedance matching means perfect transmission and zero reflection. Notice also that R is negative when Z₂ < Z₁, which means the reflected wave undergoes a **phase inversion** (a compression reflects as a rarefaction). This phase flip is why a string tied to a fixed wall reflects with inversion, while a string tied to a free end reflects without inversion — the wall has infinite impedance, the free end has zero.

Impedance matching has enormous practical consequences. Ultrasound gel exists precisely because the acoustic impedance mismatch between air and tissue is so severe (Z_air ≈ 400 Pa·s/m, Z_tissue ≈ 1.5 × 10⁶ Pa·s/m) that essentially all sound energy would reflect at the skin surface without the gel acting as an intermediate layer. Electrical engineers use **quarter-wave transformers** and **matching networks** to prevent signal reflections in transmission lines — a mismatch at the end of a cable reflects energy back toward the source, causing standing waves and power loss. Optical lens coatings are thin films chosen to have an intermediate refractive index, matching impedance between air and glass to reduce reflection from about 4% per surface to less than 0.5%.

The power transmitted across a boundary is given by the **transmission coefficient** T = 1 − R², but the amplitude transmission coefficient has a different form: t = 2Z₂/(Z₁ + Z₂). It is possible for t > 1 (the transmitted wave has larger amplitude than the incident wave) while T < 1 (the transmitted wave carries less power) — this is not a contradiction. A large-amplitude wave in a low-impedance medium can carry less power than a small-amplitude wave in a high-impedance medium, because power is amplitude² × impedance. This subtlety is why amplitude and power must be tracked separately when analyzing wave transmission across impedance boundaries.
