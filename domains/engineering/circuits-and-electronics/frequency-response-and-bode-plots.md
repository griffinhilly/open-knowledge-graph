---
id: frequency-response-and-bode-plots
title: Frequency Response and Bode Plots
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ac-circuit-analysis-methods
  type: hard
- id: resonance-circuits
  type: soft
- id: logarithms-intro
  type: soft
- id: ac-power-and-resonance
  type: soft
- id: logarithm-properties
  type: hard
- id: frequency-response-Bode-plot-basics
  type: soft
builds-toward:
- passive-filter-design
tags:
- frequency-response
- transfer-function
- Bode-plot
- gain
- phase
- poles
- zeros
stage: formal-systems
status: validated
---
# Frequency Response and Bode Plots

## Core Idea
The frequency response of a circuit is described by its transfer function H(jω) = output/input phasors as ω varies. Bode plots display the magnitude |H(jω)| in decibels (20·log₁₀|H|) and phase ∠H in degrees, both on a logarithmic frequency axis. Each real pole at ωp contributes a break in the Bode magnitude plot: flat below ωp, then falling at −20 dB/decade above it, with a −45°/decade phase transition centered at ωp. Complex pole pairs (from underdamped second-order factors) produce a resonance peak. Asymptotic straight-line approximations enable rapid sketching from the factored transfer function.

## How It's Best Learned
Start with simple RC (single-pole) and LC (complex pole pair) circuits and derive their transfer functions by voltage divider. Sketch Bode plots from asymptotic approximations, then verify against computed frequency-response tables. Practice identifying poles and zeros from the shape of a given Bode plot.

## Common Misconceptions
- Using 10·log₁₀ instead of 20·log₁₀ for voltage or current ratios — the factor of 10 applies to power ratios only.
- Treating the −3 dB frequency as a perfect brick-wall cutoff — it is the half-power point, and signals above it are attenuated but not eliminated.
- Neglecting phase when designing filters or feedback systems — phase relationships are as important as magnitude for stability and signal fidelity.

## Questions

```yaml
- question: "A circuit's transfer function has a single real pole at ω_p = 1000 rad/s. Well above ω_p, the asymptotic Bode magnitude plot falls at approximately:"
  type: multiple-choice
  options:
    - "-10 dB/decade"
    - "-20 dB/decade"
    - "-40 dB/decade"
    - "-6 dB/octave only, which is not the same as -20 dB/decade"
  answer: 1
  explanation: "Each real pole contributes a -20 dB/decade slope above its break frequency. This is equivalent to -6 dB/octave (since one octave is a factor of 2 in frequency, and log₁₀(2) ≈ 0.301, so 20 × 0.301 ≈ 6 dB per factor-of-2). A common confusion: -6 dB/octave and -20 dB/decade are the same rate expressed in different units."

- question: "At the -3 dB frequency of a low-pass filter, the output signal power is half the input signal power."
  type: true-false
  answer: true
  explanation: "The -3 dB point means |H(jω)| = 1/√2 ≈ 0.707 in voltage ratio. Since power is proportional to voltage squared, power ratio = (1/√2)² = 1/2. So the -3 dB frequency is correctly called the half-power frequency. A misconception is that -3 dB represents a sharp cutoff — in reality, signals above this frequency are attenuated but not eliminated."

- question: "Why is the frequency axis on a Bode plot logarithmic rather than linear?"
  type: short-answer
  answer: "A logarithmic frequency axis allows a single plot to span many decades of frequency (e.g., 1 Hz to 1 MHz), and it causes the asymptotic magnitude segments to appear as straight lines with slopes in dB/decade. This makes pole and zero locations easy to identify visually and enables rapid hand sketching from the factored transfer function."
  explanation: "On a linear scale, low frequencies would be compressed into a tiny region and high frequencies would dominate the plot. The log scale gives equal visual space to each decade, matching how human perception and circuit behavior both span wide ranges. The straight-line asymptotes arise because each pole factor contributes a term proportional to log(ω), which plots as a straight line."
```

## Explainer

When you analyzed AC circuits using phasors, you found the steady-state response at a single frequency. Frequency response extends that analysis across all frequencies at once. The transfer function H(jω) = V_out(jω) / V_in(jω) is the ratio of output phasor to input phasor, and it is a complex-valued function of frequency. The magnitude |H(jω)| tells you how much the circuit amplifies or attenuates signals at each frequency; the phase ∠H(jω) tells you how much the circuit shifts the timing of those signals.

Bode plots make the frequency response readable across wide frequency ranges by using two tricks: a logarithmic frequency axis (so you can see behavior from 1 Hz to 1 MHz on one plot) and expressing magnitude in decibels (20·log₁₀|H| for voltage ratios). The factor of 20 — not 10 — is critical here because voltage squared is proportional to power, and the decibel was originally defined for power ratios using 10·log₁₀. Since power ∝ V², using 20·log₁₀|H| for voltage gives the same dB value you would get using 10·log₁₀(power ratio).

Each pole and zero in H(jω) creates a characteristic feature in the Bode plot. A real pole at ωp contributes a -20 dB/decade roll-off above ωp, and a -45°/decade phase transition centered at ωp. Below ωp, the magnitude is approximately flat and the phase contribution is near 0°; above ωp, the magnitude falls and the phase contribution approaches -90°. The asymptotic (straight-line) Bode plot stitches together these flat and sloped segments at the break frequencies — the actual curve deviates by at most 3 dB from the asymptote near each break. Zeros add slopes in the opposite direction: a zero at ωz contributes +20 dB/decade above ωz and +90° of phase.

The -3 dB frequency deserves special attention because it is often called the "cutoff frequency," which can be misleading. At this point, |H| = 1/√2, so the output amplitude is 70.7% of the input. More importantly, power (proportional to amplitude squared) is exactly half — hence the name "half-power frequency." This is not a brick wall: a signal at twice the cutoff frequency is attenuated by 7 dB in a single-pole filter, not eliminated.

Phase is the most commonly neglected part of frequency response. In audio applications, phase errors can cause comb filtering and smearing. In feedback control systems, phase shift directly determines stability margins — a feedback loop where the phase reaches -180° before the gain falls below 0 dB will oscillate. Reading both the magnitude and phase Bode plots together is essential for any application where timing between signals matters.
