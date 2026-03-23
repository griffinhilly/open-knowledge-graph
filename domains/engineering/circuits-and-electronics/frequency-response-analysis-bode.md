---
id: frequency-response-analysis-bode
title: Frequency Response and Bode Plot Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-admittance-networks
  type: hard
builds-toward:
- filter-design-specifications
- feedback-control-fundamentals
tags:
- frequency-response
- bode-plots
stage: formal-systems
status: validated
---

# Frequency Response and Bode Plot Analysis

## Core Idea
Bode plots display magnitude (in dB) and phase (in degrees) of transfer functions versus frequency on logarithmic scales. For a transfer function H(jω), magnitude is 20·log₁₀|H(jω)| dB. Asymptotic Bode plots use slopes of ±20 dB/decade for poles/zeros and ±90°/decade for phase. Bode plots simplify design and analysis of frequency-dependent circuits by linearizing the logarithmic response.

## Questions

```yaml
- question: "Why does Bode magnitude analysis use the decibel scale (20 log₁₀|H|) rather than plotting |H| directly on a linear scale?"
  type: multiple-choice
  options:
    - "Decibels are the official SI unit for electrical gain and are required by engineering standards"
    - "The logarithm compresses the dynamic range and converts multiplicative gains into additive quantities, so the overall Bode plot of a cascade is simply the sum of the individual plots"
    - "The logarithmic scale makes the frequency response appear smoother and more aesthetically readable"
    - "Capacitors and inductors respond only to logarithmically-spaced frequency intervals"
  answer: 1
  explanation: "The most important reason is mathematical: log(A·B) = log(A) + log(B). A cascade of two stages with transfer functions H₁ and H₂ has overall gain |H₁·H₂| = |H₁|·|H₂|, which becomes |H₁|_dB + |H₂|_dB in the decibel domain. This additivity lets you draw the Bode plot of any cascade by simply summing the individual plots without multiplying complex numbers. It also compresses a dynamic range of millions into a legible scale. Option C describes an aesthetic consequence but not the fundamental mathematical reason."

- question: "A transfer function has a single pole at ω₀ = 100 rad/s and a single zero at ω₁ = 1000 rad/s, with DC gain of 0 dB. On the asymptotic Bode magnitude plot, what is the slope between ω = 100 rad/s and ω = 1000 rad/s?"
  type: multiple-choice
  options:
    - "0 dB/decade, since neither feature has fully activated yet in this range"
    - "+20 dB/decade, since the zero at 1000 rad/s begins contributing before it is reached"
    - "−20 dB/decade, since the pole at 100 rad/s has activated but the zero at 1000 rad/s has not yet"
    - "−40 dB/decade, since poles and zeros both affect the slope as soon as they are within a decade"
  answer: 2
  explanation: "In the asymptotic approximation, a pole at ω₀ contributes a slope change of −20 dB/decade starting at ω = ω₀, and a zero at ω₁ contributes +20 dB/decade starting at ω = ω₁. Between ω = 100 and ω = 1000 rad/s, only the pole has activated, contributing −20 dB/decade. At ω = 1000 rad/s the zero activates, and the slope returns to 0 dB/decade. The asymptotic approximation only uses the features that have been passed, not those still ahead."

- question: "For a simple RC low-pass filter, the corner frequency ω = 1/RC is also the −3 dB frequency, where the output signal power is exactly half the input power."
  type: true-false
  answer: true
  explanation: "At ω = 1/RC, the transfer function H(jω) = 1/(1 + j) has magnitude 1/√2. Power is proportional to voltage squared, so power is (1/√2)² = 1/2 of input power — a 3 dB reduction. This is why the corner frequency is also called the −3 dB bandwidth or half-power frequency. It represents the maximum error of the asymptotic Bode approximation: the asymptote predicts 0 dB at the corner, but the true response is −3 dB."

- question: "Adding more poles to a transfer function reduces its output gain at all frequencies, since each pole contributes −20 dB/decade of roll-off everywhere."
  type: true-false
  answer: false
  explanation: "Each pole only reduces the slope by 20 dB/decade above its corner frequency; below the corner frequency, the pole contributes negligibly to the response (the asymptotic approximation shows 0 dB contribution below the corner). A pole at 10 MHz has essentially no effect on the response at 1 kHz. The roll-off only begins when the operating frequency passes the pole's corner frequency. This is why a low-pass filter's pass-band gain is unaffected by its pole — the pole only attenuates frequencies in the stop band above it."

- question: "Explain why Bode plots make the analysis of cascaded circuit stages much simpler than working with the individual transfer functions multiplied together."
  type: short-answer
  answer: "When circuits are cascaded (connected in series so the output of one feeds the input of the next), their overall transfer function is the product of the individual transfer functions: H_total = H₁ · H₂ · H₃ · .... Multiplying complex-valued functions of frequency is tedious. But when converted to dB, multiplication becomes addition: |H_total|_dB = |H₁|_dB + |H₂|_dB + |H₃|_dB. This means the total Bode magnitude plot is simply the sum of the individual Bode plots. The same additivity applies to phase: phase_total = phase₁ + phase₂ + phase₃. The engineer sketches each stage's asymptotic Bode plot independently, then adds them graphically."
  explanation: "This additivity is why log scales were historically so powerful in engineering analysis (before computers) and why the Bode framework became standard. It turns a multiplication problem into an addition problem, allowing engineers to design and analyze multi-stage amplifiers, filters, and feedback controllers by inspection. The corner frequencies of each stage appear as kink points on the total plot, and the total slope at any frequency is simply the count of poles minus zeros that have been passed, multiplied by ±20 dB/decade."
```

## Explainer

From your study of impedance and admittance networks, you know that capacitors and inductors present reactances that depend on frequency: X_C = 1/(ωC), X_L = ωL. When a circuit contains these elements, its transfer function — the ratio of output to input as a function of frequency — varies across the spectrum. A **Bode plot** is a systematic way to visualize this dependence across many decades of frequency simultaneously. Rather than plotting the magnitude |H(jω)| directly, Bode plots use the **decibel** scale: 20 log₁₀|H|. This transforms multiplicative gains into additive dB values and compresses a dynamic range of millions into a readable scale. Separately, the phase angle of H(jω) is plotted in degrees versus log frequency.

The real power of Bode plots comes from how poles and zeros of H(jω) appear. A **pole** at angular frequency ω_p contributes a factor 1/(1 + jω/ω_p) to the transfer function. Below ω_p, this factor's magnitude is approximately 1 (0 dB). Above ω_p, the magnitude decreases as ω_p/ω — a straight line with slope −20 dB per decade on the log-log plot. The **asymptotic Bode approximation** replaces the actual smooth curve with two straight line segments meeting at the **corner frequency** ω_p; the true response deviates by at most 3 dB at the corner itself. A **zero** at ω_z contributes the mirror image: the factor (1 + jω/ω_z) adds +20 dB/decade above its corner frequency. For complex conjugate pole pairs (underdamped second-order systems), there is a resonant peak near the natural frequency, with height and width determined by the damping ratio.

The phase Bode plot follows parallel asymptotic logic. A real pole at ω_p contributes 0° phase well below the corner, −90° well above it, and a transition spanning roughly a decade on each side of ω_p. The complete circuit's phase response is the sum of contributions from all poles and zeros, readable directly from the Bode diagram by adding asymptotic segments. This additivity — a direct consequence of the logarithm converting products into sums — is what makes Bode analysis powerful for cascaded circuits: the overall Bode plot of a cascade is simply the sum of the individual plots in dB and degrees.

Putting it together: to sketch the Bode magnitude plot for a transfer function, identify the DC gain (value as ω → 0), locate each pole and zero on the frequency axis, and draw asymptotic magnitude starting from the DC gain, bending down by 20 dB/decade at each pole and up by 20 dB/decade at each zero. For a simple RC low-pass filter H(jω) = 1/(1 + jωRC), the single pole is at ω_p = 1/RC. Below 1/RC, the gain is 0 dB; above 1/RC, it rolls off at −20 dB/decade — this corner frequency defines the **−3 dB bandwidth** of the filter, the frequency at which the output power is halved.

Bode plots are the foundational tool for filter design and feedback control analysis, both of which you'll study next. In filter design, you specify the desired frequency response (pass-band gain, stop-band attenuation, transition bandwidth) and work backward to the pole-zero configuration that achieves it. In feedback control, Bode plots reveal **gain margin** and **phase margin** — how much gain increase or phase lag the loop can tolerate before becoming unstable. The Bode framework makes these analyses tractable by exposing the loop's frequency-dependent behavior in a form where design targets can be read directly off the graph.
