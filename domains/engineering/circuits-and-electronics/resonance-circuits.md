---
id: resonance-circuits
title: Resonance in RLC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-analysis
  type: hard
- id: second-order-transient-circuits
  type: soft
- id: ac-power-analysis-circuits
  type: soft
builds-toward:
- frequency-response-and-bode-plots
- passive-filter-design
tags:
- resonance
- quality-factor
- bandwidth
- series-resonance
- parallel-resonance
- selectivity
stage: advanced
status: validated
---

# Resonance in RLC Circuits

## Core Idea
Resonance occurs at ω₀ = 1/√(LC) where inductive and capacitive reactances are equal in magnitude and cancel. In a series RLC circuit at resonance, impedance is purely resistive (minimum), and current is maximum. In a parallel RLC circuit, admittance is minimum (impedance maximum), and the circuit draws minimum current from the source. The quality factor Q = ω₀L/R (series) measures sharpness of the resonance peak; the −3 dB bandwidth BW = ω₀/Q. High-Q circuits exhibit strong frequency selectivity and are used in filters, oscillators, and impedance matching networks.

## How It's Best Learned
Plot impedance magnitude versus frequency for series and parallel RLC circuits on the same graph. Compute ω₀, Q, and bandwidth from component values and locate the half-power frequencies on the plot. Explore how varying R changes Q and bandwidth while keeping ω₀ fixed.

## Common Misconceptions
- Using the same Q formula for series and parallel circuits — Q = ω₀L/R for series but Q = R/(ω₀L) = Rω₀C for parallel.
- Expecting voltages across individual reactive elements to equal the source voltage at resonance — in a high-Q series circuit, they can greatly exceed the source voltage by a factor of Q.
- Confusing bandwidth (frequency interval between half-power points) with the resonant frequency itself.

## Explainer

From your impedance analysis work, you know that Z_L = jωL increases with frequency while Z_C = 1/(jωC) decreases with frequency. Resonance is the frequency at which these two reactive elements cancel each other out. In a series RLC circuit, the total impedance is Z = R + j(ωL − 1/ωC). The imaginary part — the net reactance — equals zero when ωL = 1/ωC, giving the **resonant frequency** ω₀ = 1/√(LC). At this frequency, the circuit looks purely resistive, and current reaches its maximum value V/R, limited only by the resistance.

The physical picture is energy sloshing back and forth. Below resonance, the capacitor dominates — the circuit is capacitive and current leads voltage. Above resonance, the inductor dominates — the circuit is inductive and current lags voltage. At ω₀, the energy stored in the electric field of the capacitor and the magnetic field of the inductor are equal on average, and they exchange energy continuously with no net reactive power drawn from the source. The only real power consumed is in the resistance.

The **quality factor** Q measures how sharply this resonance peaks. Q = ω₀L/R for a series circuit: a high-Q circuit (low R, or high L/C ratio) has a very narrow resonance peak, while a low-Q circuit has a broad, flat response. The −3 dB **bandwidth** BW = ω₀/Q defines the frequency range over which the circuit responds strongly. A radio tuner exploits this: high Q means the circuit responds strongly to a narrow band of frequencies, rejecting adjacent stations. The half-power frequencies are ω₁ = ω₀ − BW/2 and ω₂ = ω₀ + BW/2 (approximately, for high Q).

A subtle consequence of high Q is voltage magnification. In a series RLC circuit at resonance, the voltages across the inductor and capacitor are each Q times the source voltage — they are large and nearly equal in magnitude but opposite in sign, so they cancel in the total. If Q = 50 and the source is 1 V, the voltage across the capacitor alone can be 50 V. This effect is useful in filter design and impedance matching, but dangerous if not anticipated — a high-Q resonant circuit in a power system can produce voltages far exceeding design limits. The parallel RLC circuit is the dual: at resonance, impedance is maximum (not minimum), and the circuit draws minimum current from the source while circulating large currents internally between L and C.
