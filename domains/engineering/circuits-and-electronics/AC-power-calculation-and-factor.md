---
id: AC-power-calculation-and-factor
title: AC Power Calculation and Power Factor
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: sinusoidal-AC-steady-state-fundamentals
  type: hard
- id: complex-impedance-networks-ac
  type: soft
builds-toward:
- circuit-resonance-concepts
tags:
- AC-power
- real-power
- reactive-power
- power-factor
stage: advanced
status: draft
---

# AC Power Calculation and Power Factor

## Core Idea
In AC circuits, real power P (watts) dissipates energy in resistances; reactive power Q (VAR) circulates in inductances and capacitances; apparent power S = |V||I| is the vector sum. Power factor PF = cos(φ) = P/S indicates how much of the apparent power is real. Leading (capacitive) or lagging (inductive) power factor affects load efficiency.

## Explainer

From your study of AC steady-state fundamentals, you know that voltage and current in reactive circuits are sinusoids that may be out of phase with each other. Power in AC circuits is not as simple as P = VI from DC analysis — because when voltage and current are out of phase, some of the time they have opposite signs, meaning power is actually flowing back into the source rather than being consumed by the load. Understanding AC power means understanding how to account for this phase relationship.

**Real power** P (measured in watts) is the time-average power actually consumed and converted to heat, work, or light. It's what you pay for on your electric bill. **Reactive power** Q (measured in volt-amperes reactive, or VAR) represents energy that oscillates back and forth between the source and the reactive elements — inductors store energy in magnetic fields during one half-cycle and release it during the next; capacitors do the same with electric fields. Reactive power does no net work over a complete cycle, but it must still be generated and transmitted by the utility, occupying current capacity in the lines. **Apparent power** S (measured in volt-amperes, VA) is simply |V||I| — the product of the RMS voltage and RMS current magnitudes, ignoring phase. The relationship S² = P² + Q² holds because P and Q are orthogonal components, and S is their vector sum.

**Power factor** PF = P/S = cos(φ) captures the phase angle φ between the voltage and current phasors — your phasor prerequisite makes this geometric interpretation immediate. A PF of 1.0 (purely resistive load) means all apparent power is real; a PF of 0 (purely reactive) means no real work is done despite current flowing. Industrial motors, transformers, and fluorescent lighting are inductive loads with lagging power factor (current lags voltage), which is the most common real-world scenario. Capacitive loads produce leading power factor (current leads voltage), which is less common in natural loads but deliberately introduced to correct lagging PF.

**Power factor correction** is the practical application: adding capacitors in parallel with inductive loads raises the overall power factor toward 1.0. This matters because utility companies must size their generators and transmission lines for apparent power (S = |V||I|), not just real power. A factory drawing 1 MW at 0.7 PF forces the utility to deliver 1.43 MVA of apparent power. By correcting to 0.95 PF, the same real power requires only 1.05 MVA of apparent power — smaller transformers, thinner cables, lower current losses in distribution wiring. Many utilities charge industrial customers for low power factor, creating a direct financial incentive for correction.
