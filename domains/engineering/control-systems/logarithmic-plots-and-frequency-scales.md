---
id: logarithmic-plots-and-frequency-scales
title: Logarithmic Plots and Frequency Scales
domain: engineering
course: control-systems
prerequisites:
- id: sinusoidal-response-magnitude-phase-angle
  type: hard
- id: bode-plot-construction
  type: soft
builds-toward:
- control-loop-design-via-bode-plots
tags:
- bode-plot
- decibel
- logarithmic-frequency
- asymptotic-approximation
stage: expert
status: validated
---

# Logarithmic Plots and Frequency Scales

## Core Idea
Logarithmic frequency and magnitude scales compress wide dynamic ranges into manageable plots. Magnitude in decibels is 20 log₁₀|G(jω)| dB; logarithmic frequency enables asymptotic approximations of Bode plots where poles and zeros contribute straight-line segments with slopes of ±20 dB/decade.

## Questions

```yaml
- question: "A student plots a system's Bode magnitude response using a linear frequency axis. The gain is 60 dB at 1 rad/s and falls to 0 dB at 1,000 rad/s, with a single pole at ωc = 10 rad/s. Why is this plot nearly useless for analysis?"
  type: multiple-choice
  options:
    - "Decibel values cannot be displayed on a linear frequency axis"
    - "The interesting behavior near the corner frequency occupies an extremely narrow region of the plot; most of the horizontal space shows a flat region at one end and a compressed roll-off at the other"
    - "Gain values above 40 dB cannot be accurately represented without a log-magnitude axis"
    - "The phase plot cannot be overlaid on a magnitude plot with a linear frequency axis"
  answer: 1
  explanation: "A log frequency axis compresses the ratio between frequencies, not their absolute difference. On a linear axis spanning 0–1000 rad/s, the corner frequency at 10 rad/s occupies just 1% of the plot width — everything interesting (the transition from flat to rolling-off) is squeezed into a tiny sliver on the left. A logarithmic axis allocates equal visual space to each decade (1–10, 10–100, 100–1000), spreading the interesting features evenly. This is the fundamental motivation for Bode's design: most systems have dynamics spanning many decades of frequency, and only a log axis reveals them clearly."

- question: "A second-order system has two poles at the same corner frequency ωc (a double pole). What slope does the Bode magnitude asymptote approach at frequencies much greater than ωc?"
  type: multiple-choice
  options:
    - "−20 dB/decade, same as a single pole"
    - "−40 dB/decade, because each pole contributes −20 dB/decade and they add on the log scale"
    - "−6 dB/decade, because the poles interact and partially cancel"
    - "The slope depends on the damping ratio, not just the number of poles"
  answer: 1
  explanation: "Each first-order pole contributes −20 dB/decade slope above its corner frequency. For a double pole at the same corner frequency, both poles start contributing simultaneously, giving a total slope of −40 dB/decade. This additivity on the log scale is one of the key advantages of Bode plots: gains multiply in the linear domain, but they add in the log (dB) domain, so you can simply sum the contributions of individual poles and zeros. More generally, an nth-order pole or zero cluster contributes ±20n dB/decade in the asymptotic region."

- question: "On a logarithmic frequency axis, a first-order pole contributes a slope of −20 dB/decade above its corner frequency — this asymptote is a straight line."
  type: true-false
  answer: true
  explanation: "Above the corner frequency ωc, a first-order pole term (1 + jω/ωc) ≈ jω/ωc, so its magnitude is |ω/ωc| = ω/ωc. In dB: 20 log₁₀(ω/ωc). On a log-ω axis, this is 20 × (log₁₀ω − log₁₀ωc), which is a linear function of log₁₀ω — a straight line with slope −20 dB per decade of frequency. This piecewise-linear structure is the mathematical reason Bode's asymptotic approximation works: the log scale turns the nonlinear magnitude function into a slope that can be sketched with a straightedge."

- question: "The asymptotic straight-line approximation of a Bode magnitude plot is exact at the corner frequency — the primary errors occur far from the corner."
  type: true-false
  answer: false
  explanation: "The maximum error of the asymptotic approximation occurs right at the corner frequency, not far from it. At ωc, the true gain is |1 + j1| = √2, which is 20 log₁₀(√2) ≈ 3 dB above the asymptote (which predicts 0 dB at that point). The approximation is actually most accurate far from the corner frequency, where one or the other asymptote dominates. The 3 dB error at the corner is a known, systematic deviation that engineers account for when using asymptotic Bode plots — the 'corner frequency' is also called the '−3 dB frequency' for this reason."

- question: "What property of logarithmic scales makes the Bode plot's asymptotic straight-line approximation possible? Explain why the same simplification would not work on a linear frequency axis."
  type: short-answer
  answer: "Logarithmic scales turn multiplicative relationships into additive ones. A factor of (1 + jω/ωc) in a transfer function becomes 20 log₁₀|1 + jω/ωc| in dB. When ω >> ωc, this is approximately 20 log₁₀(ω/ωc) = 20(log₁₀ω − log₁₀ωc). Plotted against log₁₀ω (the log frequency axis), this is a linear function — a straight line with slope +20. On a linear frequency axis, the same quantity would be 20 log₁₀(ω/ωc) plotted against ω itself, which is a logarithmic curve, not a line. The straightness of the asymptote is entirely a consequence of plotting a log-domain quantity against a log-domain axis."
  explanation: "The deeper point is that Bode plots exploit the algebraic structure of transfer functions: poles and zeros multiply in the frequency domain, but they add in the log domain. On log-log axes, each pole or zero contributes an independent straight-line segment, and the total response is simply the sum of the segments. This linearity collapses on any other scale choice."
```

## Explainer

From your work with sinusoidal frequency response, you know that a system's behavior changes as frequency sweeps from near zero to very high values — filters pass some frequencies and attenuate others, and the gain can vary by factors of thousands. Plotting this on linear axes is nearly useless: a gain of 1000 at low frequency and 0.001 at high frequency would compress all the interesting detail into an unreadable spike at one end. Logarithmic scales solve this by displaying the ratio between values rather than their absolute difference.

The **decibel** (dB) is the standard unit for log-scale magnitude: magnitude in dB = 20 log₁₀|G(jω)|. The factor of 20 comes from the convention for power ratios (10 log₁₀ for power, 20 log₁₀ for amplitude). Key reference points: 0 dB means unity gain (output = input), +20 dB means a factor of 10 gain, −20 dB means a factor of 10 attenuation, +6 dB ≈ factor of 2, −6 dB ≈ factor of ½. These are worth memorizing because they let you read Bode plots at a glance: a gain that drops from 40 dB to 0 dB spans a factor of 100 in amplitude.

The logarithmic frequency axis creates the key simplification: the gain of a first-order pole or zero — a factor like (1 + jω/ωc) — becomes piecewise linear in dB when plotted against log ω. Below the **corner frequency** ωc, the term ≈ 1 (0 dB contribution). Above ωc, the term grows like ω/ωc, contributing 20 log₁₀(ω/ωc) dB — a straight line with slope +20 dB/decade (or −20 dB/decade for a pole). These **asymptotic approximations** let you sketch the entire Bode magnitude plot by hand: start at the DC gain, then add a slope change of ±20 dB/decade at each corner frequency, with the sign determined by whether it is a zero (+) or pole (−). Higher-order poles or zeros contribute multiples: a double pole contributes −40 dB/decade. The approximation is exact at frequencies far from the corner; the maximum error is 3 dB right at the corner frequency itself.

The phase plot does not become piecewise linear in the same clean way, but it does have a useful approximation. Each pole contributes −45° at its corner frequency, transitioning from 0° to −90° over roughly a decade on either side. The full transition spans about two decades (from 0.1ωc to 10ωc). The combination of magnitude and phase asymptotes lets you sketch the complete Bode plot for a transfer function in minutes without numerical computation — which is why Bode plots were developed in the first place, before computers, as a rapid tool for frequency-domain design.
