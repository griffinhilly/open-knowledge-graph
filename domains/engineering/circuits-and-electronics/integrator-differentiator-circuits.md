---
id: integrator-differentiator-circuits
title: Integrator and Differentiator Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: op-amp-circuit-applications
  type: hard
- id: capacitor-inductor-energy-storage
  type: hard
builds-toward:
- first-order-active-filters
tags:
- integrator
- differentiator
- op-amp
- capacitor-feedback
- frequency-response
- dc-offset
- reset-switch
stage: formal-systems
status: draft
---

# Integrator and Differentiator Circuits

## Core Idea
The op-amp integrator replaces the feedback resistor of the inverting amplifier with a capacitor: V_out(t) = -(1/R_in*C) * integral of V_in(t) dt. It performs mathematical integration in continuous time, converting a constant input to a linearly ramping output and a square wave to a triangle wave. In the frequency domain, it has gain |H(jw)| = 1/(w*R*C), acting as a low-pass filter with gain that increases without bound at low frequencies — the fundamental practical problem. Any DC offset or bias current at the input integrates over time, driving the output to saturation. A large feedback resistor in parallel with C limits the DC gain and prevents saturation at the cost of deviating from ideal integration at low frequencies. The op-amp differentiator places the capacitor in the input path with a feedback resistor: V_out(t) = -R_f*C * dV_in/dt. Its gain increases with frequency (|H(jw)| = w*R*C), amplifying high-frequency noise and making it inherently unstable without a series input resistor to limit high-frequency gain. Both circuits are building blocks for analog computers, PID controllers, and active filter design.

## How It's Best Learned
Derive the integrator transfer function by writing KCL at the virtual ground node using impedance Z_C = 1/(jwC) for the capacitor, then transform to the time domain using the capacitor voltage-current relationship. Apply a square wave input and sketch the output by hand. Then add a parallel feedback resistor and re-derive the transfer function to see how it modifies the low-frequency behavior. Repeat the dual analysis for the differentiator.

## Common Misconceptions
- Assuming the ideal integrator works in practice without modification — any real op-amp has input offset voltage and bias current that cause unbounded output drift; a parallel feedback resistor or periodic reset switch is mandatory.
- Thinking the differentiator is equally practical as the integrator — the differentiator's rising gain with frequency amplifies noise and can cause oscillation; integrators are far more commonly used in analog signal processing.
- Confusing the integrator's low-pass behavior with a simple RC filter — the integrator has a gain that theoretically goes to infinity at DC (limited by open-loop gain), while a passive RC filter has at most unity gain.
