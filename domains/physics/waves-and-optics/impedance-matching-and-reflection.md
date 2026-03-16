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
status: draft
---

# Impedance Matching and Wave Reflection at Boundaries

## Core Idea
When a wave encounters a boundary between two media with different impedances, part of the wave reflects and part transmits. The reflection coefficient depends on impedance ratio: R = (Z₂ - Z₁)/(Z₂ + Z₁). Impedance matching (Z₁ = Z₂) eliminates reflection.

## Explainer

From your study of acoustic impedance, you know that **impedance** Z characterizes how strongly a medium resists wave-driven motion — it combines the medium's density and elasticity (Z = ρv for acoustic waves, or more generally the ratio of a driving quantity to a flow quantity). The central insight of impedance matching is that what happens at a boundary depends entirely on the ratio of impedances on either side, not on the properties of each medium in isolation.

Think of a wave as a chain of coupled oscillators transmitting energy. When the chain suddenly encounters a region where each oscillator is much harder or easier to move (a different impedance), the incoming energy has a problem: the new medium "expects" a different ratio of force to velocity. Part of the wave reflects backward because it cannot be absorbed at the original ratio; part transmits forward at an adjusted amplitude. The **reflection coefficient** R = (Z₂ − Z₁)/(Z₂ + Z₁) captures this mismatch. Notice that R = 0 when Z₂ = Z₁ — perfect impedance matching means perfect transmission and zero reflection. Notice also that R is negative when Z₂ < Z₁, which means the reflected wave undergoes a **phase inversion** (a compression reflects as a rarefaction). This phase flip is why a string tied to a fixed wall reflects with inversion, while a string tied to a free end reflects without inversion — the wall has infinite impedance, the free end has zero.

Impedance matching has enormous practical consequences. Ultrasound gel exists precisely because the acoustic impedance mismatch between air and tissue is so severe (Z_air ≈ 400 Pa·s/m, Z_tissue ≈ 1.5 × 10⁶ Pa·s/m) that essentially all sound energy would reflect at the skin surface without the gel acting as an intermediate layer. Electrical engineers use **quarter-wave transformers** and **matching networks** to prevent signal reflections in transmission lines — a mismatch at the end of a cable reflects energy back toward the source, causing standing waves and power loss. Optical lens coatings are thin films chosen to have an intermediate refractive index, matching impedance between air and glass to reduce reflection from about 4% per surface to less than 0.5%.

The power transmitted across a boundary is given by the **transmission coefficient** T = 1 − R², but the amplitude transmission coefficient has a different form: t = 2Z₂/(Z₁ + Z₂). It is possible for t > 1 (the transmitted wave has larger amplitude than the incident wave) while T < 1 (the transmitted wave carries less power) — this is not a contradiction. A large-amplitude wave in a low-impedance medium can carry less power than a small-amplitude wave in a high-impedance medium, because power is amplitude² × impedance. This subtlety is why amplitude and power must be tracked separately when analyzing wave transmission across impedance boundaries.
