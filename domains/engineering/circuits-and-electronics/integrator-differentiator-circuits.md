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
status: validated
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

## Questions

```yaml
- question: "An op-amp integrator (capacitor in feedback, no parallel resistor) is powered on with zero input signal. After a few seconds, the output saturates against the positive supply rail. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The op-amp's gain-bandwidth product is too low for the frequency of the input signal"
    - "A small DC input offset voltage and bias current are being continuously integrated, ramping the output to saturation"
    - "The feedback capacitor is too large, causing the integration time constant to be too long"
    - "The virtual ground assumption breaks down at DC, causing the output to drift"
  answer: 1
  explanation: "Real op-amps have a small but non-zero input offset voltage (typically millivolts) and input bias currents (nanoamps to microamps). These DC errors appear at the input and are integrated continuously — a constant DC input integrates to a ramp. With no DC feedback path to control the operating point, this ramp grows without bound until the output hits the supply rail. This is the fundamental reason ideal op-amp integrators cannot be used without modification. The parallel feedback resistor (or a reset switch) is mandatory, not optional."

- question: "An engineer needs to process an analog signal by computing its derivative. She builds the dual of the integrator — a capacitor in the input path and a resistor in the feedback path. The main practical problem with this differentiator circuit is:"
  type: multiple-choice
  options:
    - "The output is inverted, requiring an additional inverting stage to restore signal polarity"
    - "The gain increases with frequency, so high-frequency noise is amplified without bound, causing large output spikes and potential oscillation"
    - "The differentiator integrates rather than differentiates at frequencies above the RC break frequency"
    - "The circuit cannot differentiate signals with DC components, because the capacitor blocks DC"
  answer: 1
  explanation: "The differentiator's transfer function is H(jω) = −jωRC, so gain = ωRC rises linearly with frequency. Real signals always contain high-frequency noise, and the differentiator amplifies this noise aggressively. A small noise spike in the input produces a large, sharp spike in the output. Worse, the rising gain interacts with the op-amp's own phase shift to cause oscillation. This is why the differentiator is rarely used without a series input resistor to cap maximum gain, and why integrators vastly outnumber differentiators in practical analog design."

- question: "Adding a large resistor in parallel with the feedback capacitor of an op-amp integrator prevents output saturation by providing a DC feedback path that limits the gain at low frequencies, though this causes deviation from ideal integration below the break frequency."
  type: true-false
  answer: true
  explanation: "At DC (ω = 0), the capacitor is an open circuit, so without a parallel resistor there is no feedback at all and any DC offset integrates to saturation. The parallel resistor provides a feedback path at DC, limiting the DC gain to −Rf/Rin (finite). At frequencies above the break frequency 1/(2πRfC), the capacitor dominates and the circuit integrates normally. Below this frequency, it acts as an ordinary inverting amplifier. This is called a 'lossy integrator' — the only kind that works in practice."

- question: "Op-amp differentiators are preferred over integrators in analog signal processing because they respond more sensitively to rapid signal changes, making them better suited for real-time derivative computation."
  type: true-false
  answer: false
  explanation: "The opposite is true: op-amp integrators are far more widely used than differentiators in practical analog design. The differentiator's gain rises with frequency, making it extremely sensitive to high-frequency noise and prone to oscillation — serious problems in any real circuit. The integrator's gain falls with frequency, naturally attenuating noise. Integrators form the core of analog computers, PID controllers (the I term), active low-pass filters, and waveform generators. The differentiator's instability issues make it a circuit of last resort."

- question: "Why is the op-amp differentiator inherently less stable and less practical than the op-amp integrator?"
  type: short-answer
  answer: "The differentiator's gain increases without bound as frequency rises (|H(jω)| = ωRC), so it amplifies high-frequency noise dramatically. Real signals always contain high-frequency noise components, producing large output spikes. The rising gain also interacts with the op-amp's own internal phase shift to create positive feedback at high frequencies, causing oscillation. The integrator has the opposite frequency characteristic — gain decreases with frequency — naturally suppressing noise. This is why integrators are the dominant building block in practical analog signal processing."
  explanation: "The instability problem can be mitigated by adding a series resistor at the differentiator's input, which creates a pole that caps maximum gain. But this fix limits the frequency range over which the circuit actually differentiates. Every practical differentiator is therefore a compromise, while the integrator (with its parallel resistor fix for DC drift) is a cleaner design. The asymmetry is fundamental: integration smooths, differentiation sharpens — and in noisy environments, sharpening amplifies noise."
```

## Explainer

You know from op-amp circuit applications that the inverting amplifier has gain −R_f/R_in, set by the ratio of feedback to input resistors. You also know from capacitor and inductor energy storage that a capacitor's impedance is Z_C = 1/(jωC) — it looks like a very large resistor at low frequencies and a very small one at high frequencies. The op-amp integrator exploits both ideas: replace the feedback resistor with a capacitor, so the gain becomes −Z_C/R_in = −1/(jωRC). Low frequencies see enormous gain; high frequencies see tiny gain. This is mathematically equivalent to integration in the time domain: V_out(t) = −(1/RC) ∫ V_in(t) dt.

The square-wave-to-triangle-wave conversion makes the integration concrete. Feed a square wave into the integrator: during the positive half-cycle, the input is a constant positive voltage. Integrating a constant yields a linearly increasing output — a ramp. During the negative half-cycle, the ramp reverses. The output is a triangle wave, and its slope is proportional to the input amplitude and inversely proportional to RC. This is not filtering in the ordinary sense; it is continuous-time computation. Analog computers used chains of integrators to solve differential equations — a second-order DE becomes two cascaded integrators with appropriate feedback.

The practical problem is DC offset. Ideal integration assumes the output starts at zero and the input has zero DC component. Real op-amps have non-zero **input offset voltage** (a small DC error at the input) and **input bias current** (small DC currents flowing into both input terminals). When the integrator runs without bound on these DC terms, the output ramps to the power supply rail and saturates. The fix is a large **feedback resistor** in parallel with the capacitor: at DC (ω = 0), the capacitor is an open circuit and the feedback resistor limits gain to −R_f/R_in, a finite value. The circuit is now a lossy integrator — it integrates accurately for signals above a break frequency 1/(2πR_fC) but behaves like an ordinary inverting amplifier at DC.

The differentiator is the dual: the capacitor moves to the input path, the resistor to feedback. Gain becomes −R·Z_C⁻¹ = −jωRC, rising with frequency. In the time domain, V_out = −RC · dV_in/dt. A triangle wave in produces a square wave out; a ramp in produces a step out. The problem is the gain-versus-frequency shape: because gain keeps rising, high-frequency noise is amplified without limit. Any small noise spike at the input produces a large spike at the output. The circuit also tends toward oscillation because the rising gain interacts with the op-amp's own phase shift. The fix — a small series resistor at the input — caps the maximum gain and stabilizes the circuit, but at the cost of differentiating accurately only below a frequency set by that resistor. Differentiators are far less common than integrators in practice for exactly this reason.
