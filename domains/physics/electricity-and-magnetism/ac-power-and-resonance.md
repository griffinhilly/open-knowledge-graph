---
id: ac-power-and-resonance
title: AC Power and Resonance
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: impedance-and-reactance
  type: hard
- id: electric-power
  type: hard
builds-toward:
- electromagnetic-waves
tags:
- AC-power
- resonance
- power-factor
- bandwidth
- transformers
stage: formal-systems
status: validated
---

# AC Power and Resonance

## Core Idea
Average power in an AC circuit is P = V_rms I_rms cos φ, where cos φ is the power factor — only the resistive component dissipates energy. Resonance occurs when X_L = X_C, i.e., ω₀ = 1/√(LC), giving maximum current for a series RLC circuit and minimum impedance. The quality factor Q = ω₀/Δω measures the sharpness of the resonance peak. Transformers use mutual inductance to step voltage up or down while conserving power (V₁/V₂ = N₁/N₂, I₁/I₂ = N₂/N₁).

## How It's Best Learned
Plot impedance |Z| vs. frequency and identify the resonance minimum. Calculate Q for different R values and observe how R broadens the resonance peak. Analyze the transformer equations and explain why high-voltage transmission minimizes resistive losses.

## Common Misconceptions
- Reactive elements (L and C) do not dissipate power on average, even though instantaneous power oscillates.
- A high power factor (cos φ → 1) means the circuit is behaving mostly resistively.
- Transformers only work with AC; they cannot step up or down DC voltages.
