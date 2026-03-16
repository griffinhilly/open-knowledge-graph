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

## Explainer

You know from op-amp circuit applications that the inverting amplifier has gain −R_f/R_in, set by the ratio of feedback to input resistors. You also know from capacitor and inductor energy storage that a capacitor's impedance is Z_C = 1/(jωC) — it looks like a very large resistor at low frequencies and a very small one at high frequencies. The op-amp integrator exploits both ideas: replace the feedback resistor with a capacitor, so the gain becomes −Z_C/R_in = −1/(jωRC). Low frequencies see enormous gain; high frequencies see tiny gain. This is mathematically equivalent to integration in the time domain: V_out(t) = −(1/RC) ∫ V_in(t) dt.

The square-wave-to-triangle-wave conversion makes the integration concrete. Feed a square wave into the integrator: during the positive half-cycle, the input is a constant positive voltage. Integrating a constant yields a linearly increasing output — a ramp. During the negative half-cycle, the ramp reverses. The output is a triangle wave, and its slope is proportional to the input amplitude and inversely proportional to RC. This is not filtering in the ordinary sense; it is continuous-time computation. Analog computers used chains of integrators to solve differential equations — a second-order DE becomes two cascaded integrators with appropriate feedback.

The practical problem is DC offset. Ideal integration assumes the output starts at zero and the input has zero DC component. Real op-amps have non-zero **input offset voltage** (a small DC error at the input) and **input bias current** (small DC currents flowing into both input terminals). When the integrator runs without bound on these DC terms, the output ramps to the power supply rail and saturates. The fix is a large **feedback resistor** in parallel with the capacitor: at DC (ω = 0), the capacitor is an open circuit and the feedback resistor limits gain to −R_f/R_in, a finite value. The circuit is now a lossy integrator — it integrates accurately for signals above a break frequency 1/(2πR_fC) but behaves like an ordinary inverting amplifier at DC.

The differentiator is the dual: the capacitor moves to the input path, the resistor to feedback. Gain becomes −R·Z_C⁻¹ = −jωRC, rising with frequency. In the time domain, V_out = −RC · dV_in/dt. A triangle wave in produces a square wave out; a ramp in produces a step out. The problem is the gain-versus-frequency shape: because gain keeps rising, high-frequency noise is amplified without limit. Any small noise spike at the input produces a large spike at the output. The circuit also tends toward oscillation because the rising gain interacts with the op-amp's own phase shift. The fix — a small series resistor at the input — caps the maximum gain and stabilizes the circuit, but at the cost of differentiating accurately only below a frequency set by that resistor. Differentiators are far less common than integrators in practice for exactly this reason.
