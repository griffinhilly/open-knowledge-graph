---
id: ac-power-analysis-apparent-reactive
title: 'AC Power: Real, Reactive, and Apparent Power'
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: phasor-algebra-complex-impedance
  type: hard
tags:
- ac-power
- power-analysis
stage: formal-systems
status: draft
---

# AC Power: Real, Reactive, and Apparent Power

## Core Idea
Real power P = |V||I|cos(φ) (in Watts) represents energy consumed; reactive power Q = |V||I|sin(φ) (in VARs) represents energy oscillating between components; apparent power S = |V||I| (in VA) is the complex magnitude. The power factor cos(φ) indicates efficiency: unity for purely resistive circuits, zero for purely reactive. Power triangle and complex power S = P + jQ relate these quantities.

## Questions

```yaml
- question: "An industrial motor delivers 10 kW of real power to a load at a power factor of 0.5. What apparent power must the utility supply?"
  type: multiple-choice
  options:
    - "5 kVA — apparent power is real power multiplied by power factor"
    - "10 kVA — apparent power equals real power for any load"
    - "20 kVA — apparent power is real power divided by power factor"
    - "17.3 kVA — apparent power equals the vector sum of real and reactive power"
  answer: 2
  explanation: "Apparent power S = P / cos(φ) = 10 kW / 0.5 = 20 kVA. This is the total current demand on the source. A power factor of 0.5 means only half the supplied current is doing useful work — the other half is reactive current oscillating in and out of inductive elements. The utility must size its cables, transformers, and generators for 20 kVA even though only 10 kW is delivered as useful work. Option D is a plausible distractor: it confuses the calculation by using S² = P² + Q² without solving correctly — Q here would be 17.3 kVAR and S = 20 kVA."

- question: "Why do utilities charge industrial customers penalty fees for low power factors, even when the customer's real power consumption (measured in kWh) stays the same?"
  type: multiple-choice
  options:
    - "Low power factor increases the frequency of the supply voltage, damaging equipment"
    - "Reactive power is dissipated as heat in the utility's transformers, increasing their fuel costs"
    - "Reactive current loads the utility's cables and generators with current that does no net work, requiring them to be oversized to serve the load"
    - "Low power factor customers use more real power than their meters record, effectively stealing energy"
  answer: 2
  explanation: "Reactive current must flow through the utility's cables, transformers, and generators even though it returns to the source each cycle and does no net work. The I²R transmission losses in cables depend on total current (real + reactive), not just the real component. Equipment must be sized for apparent power. A customer with poor power factor causes the utility to spend on infrastructure capacity that generates no revenue — hence the penalty. Option B is wrong: reactive power is not dissipated as heat in an ideal transformer; it oscillates between source and reactive load elements."

- question: "Adding a capacitor in parallel with an inductive load can reduce the apparent power drawn from the grid without changing the real power delivered to the load."
  type: true-false
  answer: true
  explanation: "Power factor correction works by adding capacitive reactive power Q_C = −Q_L that partially or fully cancels the inductive reactive power. The load still receives the same real power P — the motor still spins, the heat still flows. But the net reactive power seen by the source decreases, so the apparent power S = √(P² + Q_net²) decreases. The source now supplies a smaller total current at a higher power factor, reducing I²R losses in transmission and freeing infrastructure capacity."

- question: "Reactive power represents energy permanently dissipated in the reactive components of an AC circuit — it is lost, just like the heat dissipated in a resistor."
  type: true-false
  answer: false
  explanation: "Reactive power represents energy that oscillates back and forth between the source and the reactive elements (inductors and capacitors) — it is not dissipated. In each half-cycle, an inductor absorbs energy from the source; in the next half-cycle, it returns that energy. The net energy transfer per complete cycle is zero. This is why Q is measured in VARs (volt-amperes reactive) rather than watts — it is not a rate of energy consumption. Only real power P (in watts) represents true energy dissipation. The confusion arises because reactive current does cause *real* I²R losses in wiring, but that is a secondary effect, not the reactive power itself."

- question: "Explain why a circuit with a low power factor forces the source to supply more current than necessary, and how power factor correction reduces this without reducing delivered power."
  type: short-answer
  answer: "Power factor cos(φ) measures the fraction of supplied current that is in phase with the voltage and therefore transfers net energy. At low power factor, a large component of the current is 90° out of phase (reactive), doing no net work but still flowing through source and transmission equipment. For a fixed real power requirement P, the total current I = P / (V · cos(φ)) — as cos(φ) falls, I must rise. Power factor correction adds a capacitor whose reactive current is 180° out of phase with the inductor's reactive current, so they cancel. The load still needs the same real power, but the net reactive demand falls, reducing total current and apparent power."
  explanation: "The key insight is that reactive current is 'wasted' in the sense of occupying infrastructure capacity, even though the energy itself returns to the source. Correction cancels reactive demand at the load rather than at the source, so the reactive current circulates locally between the capacitor and inductor rather than traveling through the utility's lines."
```

## Explainer

From phasor algebra, you know how to represent sinusoidal voltages and currents as complex numbers and how impedance Z = R + jX characterizes how each component responds to AC. That framework tells you the magnitude and phase of the current for a given voltage. **AC power analysis** extends this further: it asks not just how much current flows, but which part of that current actually delivers energy to the load and which part merely oscillates back and forth between the source and reactive elements without doing useful work.

The key insight is that only the current component *in phase* with the voltage transfers net energy. Instantaneous power is p(t) = v(t)·i(t). For a purely resistive load, voltage and current are perfectly in phase, so p(t) is always non-negative — energy flows continuously from source to load. For a purely reactive load (inductor or capacitor), voltage and current are 90° out of phase, so p(t) alternates equally between positive and negative halves — energy sloshes back and forth between source and component but no net work is done per cycle. The **power factor** cos(φ), where φ is the phase angle between voltage and current phasors, quantifies this: 1 for pure resistors, 0 for pure reactances, and values in between for mixed loads.

This decomposition produces three quantities that form the **power triangle**. **Real power** P = |V||I|cos(φ) (watts) is the actual energy consumed per second by resistive elements — what your electricity bill measures. **Reactive power** Q = |V||I|sin(φ) (volt-amperes reactive, VARs) is the energy oscillating in and out of inductors and capacitors — it does no net work but demands current from the source. **Apparent power** S = |V||I| (volt-amperes, VA) is the total current-demand on the source, regardless of how much is doing useful work. These three quantities form a right triangle: S² = P² + Q², and complex power unifies them as **S** = P + jQ = V·I*, where I* is the complex conjugate of the current phasor.

The practical consequence of reactive power is equipment sizing and transmission losses. A motor with poor power factor might draw twice the current needed to deliver its mechanical output — meaning cables, transformers, and generators must be sized for the full apparent power, not just the real power. Utilities charge industrial customers penalties for poor power factors because reactive current loads their infrastructure without generating revenue. **Power factor correction** — adding capacitors in shunt with inductive loads — introduces a reactive power Q_C = −Q_L that cancels the inductive reactive power, bringing the net power factor toward unity and dramatically reducing the apparent power drawn from the grid.
