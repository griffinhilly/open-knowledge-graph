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

## Explainer

From phasor algebra, you know how to represent sinusoidal voltages and currents as complex numbers and how impedance Z = R + jX characterizes how each component responds to AC. That framework tells you the magnitude and phase of the current for a given voltage. **AC power analysis** extends this further: it asks not just how much current flows, but which part of that current actually delivers energy to the load and which part merely oscillates back and forth between the source and reactive elements without doing useful work.

The key insight is that only the current component *in phase* with the voltage transfers net energy. Instantaneous power is p(t) = v(t)·i(t). For a purely resistive load, voltage and current are perfectly in phase, so p(t) is always non-negative — energy flows continuously from source to load. For a purely reactive load (inductor or capacitor), voltage and current are 90° out of phase, so p(t) alternates equally between positive and negative halves — energy sloshes back and forth between source and component but no net work is done per cycle. The **power factor** cos(φ), where φ is the phase angle between voltage and current phasors, quantifies this: 1 for pure resistors, 0 for pure reactances, and values in between for mixed loads.

This decomposition produces three quantities that form the **power triangle**. **Real power** P = |V||I|cos(φ) (watts) is the actual energy consumed per second by resistive elements — what your electricity bill measures. **Reactive power** Q = |V||I|sin(φ) (volt-amperes reactive, VARs) is the energy oscillating in and out of inductors and capacitors — it does no net work but demands current from the source. **Apparent power** S = |V||I| (volt-amperes, VA) is the total current-demand on the source, regardless of how much is doing useful work. These three quantities form a right triangle: S² = P² + Q², and complex power unifies them as **S** = P + jQ = V·I*, where I* is the complex conjugate of the current phasor.

The practical consequence of reactive power is equipment sizing and transmission losses. A motor with poor power factor might draw twice the current needed to deliver its mechanical output — meaning cables, transformers, and generators must be sized for the full apparent power, not just the real power. Utilities charge industrial customers penalties for poor power factors because reactive current loads their infrastructure without generating revenue. **Power factor correction** — adding capacitors in shunt with inductive loads — introduces a reactive power Q_C = −Q_L that cancels the inductive reactive power, bringing the net power factor toward unity and dramatically reducing the apparent power drawn from the grid.
