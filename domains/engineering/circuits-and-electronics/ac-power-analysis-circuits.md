---
id: ac-power-analysis-circuits
title: AC Power Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ac-circuit-analysis-methods
  type: hard
- id: electric-power
  type: soft
- id: ac-power-and-resonance
  type: soft
builds-toward:
- resonance-circuits
tags:
- real-power
- reactive-power
- apparent-power
- power-factor
- complex-power
- RMS
- power-factor-correction
stage: formal-systems
status: validated
---

# AC Power Analysis

## Core Idea
Instantaneous power p(t) = v(t)·i(t) oscillates at twice the source frequency in AC circuits. Average (real) power P = ½Vm·Im·cos(θ) in watts is actually dissipated; reactive power Q = ½Vm·Im·sin(θ) in VARs oscillates between source and reactive elements without dissipation. Complex power S = P + jQ = ½·V·I* (I* = conjugate of current phasor) unifies these. Power factor PF = cos(θ) = P/|S| measures how efficiently real power is delivered; unity PF is ideal. Power factor correction adds reactive elements to minimize reactive power demand from the source.

## How It's Best Learned
Compute complex power for simple RLC loads and verify that the real parts of complex power are conserved across all branches (Tellegen's theorem). Practice power factor correction by computing the required shunt capacitance to bring an inductive load to unity power factor.

## Common Misconceptions
- Equating apparent power |S| with real power P — only P performs useful work; |S| is the product of RMS voltage and current magnitudes.
- Using peak values in power formulas without the ½ factor, or using RMS values with the ½ factor — the two forms are equivalent but must not be mixed.
- Assuming reactive power is wasted — it is exchanged between source and reactive elements, but drawing it stresses generation and transmission equipment.
