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

## Explainer

In DC circuits, power is simple: P = VI, always positive, always consumed. In AC circuits, voltage and current are sinusoids that oscillate — and when they're out of phase with each other, the power story becomes richer and more useful. Your prerequisite on AC circuit analysis methods gave you phasors and impedance. Now you apply that machinery to power: not just how much energy flows, but what form it takes and how efficiently it's delivered.

Start from first principles. If v(t) = Vm·cos(ωt) and i(t) = Im·cos(ωt − θ), the instantaneous power p(t) = v(t)·i(t). Multiplying out using the product-to-sum trig identity yields a constant term plus a term oscillating at 2ω. The constant term is **real power** P = ½·Vm·Im·cos(θ) — measured in watts, this is the average energy delivered per second and is the only part that does sustained useful work (turns motors, generates heat, lights LEDs). The oscillating term involves **reactive power** Q = ½·Vm·Im·sin(θ), measured in VARs (volt-ampere reactive). Reactive power represents energy sloshing back and forth between the source and the inductors and capacitors in the load — it averages to zero over a full cycle.

**Complex power** S = P + jQ = ½·V̅·Ī* elegantly unifies these into one phasor quantity (where Ī* is the complex conjugate of the current phasor). The magnitude |S| is **apparent power** in volt-amperes — what you'd compute from the product of RMS voltage and RMS current without knowing the phase angle. The ratio P/|S| is the **power factor** (PF = cos θ), a number between 0 and 1 measuring how efficiently apparent power converts to real power. Unity power factor means all power drawn from the source is delivered as useful work. A lagging power factor (typical of inductive loads like motors) means the source must supply extra current to maintain the magnetic fields in the load, even though that current returns to the source each half-cycle.

That "extra current" is why reactive power matters economically. Transmission lines, transformers, and generators are sized for the current they carry — |S|/V — not the useful power P. A large industrial motor drawing current at PF = 0.7 forces the utility to size equipment for 43% more current than a PF = 1.0 load of the same real power. **Power factor correction** fixes this by adding a shunt capacitor in parallel with the inductive load. Capacitors have leading reactive power (Q < 0) that offsets the lagging reactive power of the inductor (Q > 0). If you size the capacitor correctly, Q_total → 0, the power factor approaches unity, and the source only sees the real power load — no reactive current component. The real power delivered to the motor is unchanged; only the reactive demand on the source is eliminated. This is one of the most economically significant circuit design choices in industrial power systems.
