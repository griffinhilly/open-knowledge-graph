---
id: frequency-response-Bode-plot-basics
title: Frequency Response and Bode Plot Basics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: AC-Kirchhoff-laws-phasor-domain
  type: hard
- id: passive-filter-transfer-function-analysis
  type: soft
- id: logarithms-intro
  type: hard
- id: logarithmic-functions-review
  type: hard
builds-toward:
- filter-selection-and-practical-applications
tags:
- Bode-plots
- magnitude-plot
- phase-plot
- gain
- logarithmic-scale
stage: formal-systems
status: draft
---

# Frequency Response and Bode Plot Basics

## Core Idea
Bode plots display magnitude (in dB) and phase versus frequency on a logarithmic scale. Magnitude in dB is 20 log₁₀|H(jω)|; phase is ∠H(jω). Bode plots make it easy to visualize filtering action, identify resonances, and understand stability margins. Asymptotic Bode plots can be sketched by hand from the transfer function poles and zeros.

## Questions

```yaml
- question: "A first-order low-pass filter has a corner frequency of 1 kHz. Using the asymptotic Bode plot approximation, what is the magnitude of H(jω) at 10 kHz?"
  type: multiple-choice
  options:
    - "0 dB — the filter passes all frequencies below its bandwidth"
    - "-3 dB — this is the standard definition of the corner frequency"
    - "-20 dB — one decade above the corner frequency, the asymptotic slope gives -20 dB"
    - "-40 dB — each decade above the corner adds 40 dB of attenuation"
  answer: 2
  explanation: "A single real pole contributes a slope of -20 dB/decade above the corner frequency. At 10 kHz, which is exactly one decade above the 1 kHz corner, the asymptotic approximation gives 0 dB - 20 dB = -20 dB. Option B (-3 dB) is the actual attenuation at the corner frequency itself (where the asymptotic approximation has its largest error of 3 dB), not a decade above it. Option D (-40 dB/decade) would apply to a two-pole system."

- question: "Why does the Bode plot convert gain to decibels using 20·log₁₀|H(jω)| instead of simply plotting |H(jω)| directly?"
  type: multiple-choice
  options:
    - "Decibels are the standard unit of electrical power, making results comparable across different circuit types"
    - "The log scale compresses large dynamic ranges and converts cascaded stage multiplication into simple addition of dB values"
    - "Converting to dB linearizes the frequency response, making curves easier to sketch as straight lines"
    - "Decibels eliminate the phase information, simplifying the two-plot Bode format"
  answer: 1
  explanation: "Two motivations: (1) Gains can range from near-zero to thousands, and a linear scale cannot display this range readably. The log scale compresses it so both small and large gains are visible. (2) When two stages are cascaded, the total gain is |H₁|·|H₂|, which requires multiplication. In dB: 20log|H₁H₂| = 20log|H₁| + 20log|H₂|, so cascaded stages add in dB. Option C is partially correct — dB with a log-frequency axis does allow straight-line asymptotic sketching — but the primary motivation for dB is the dynamic range compression and the additive property, not linearization per se."

- question: "If two amplifier stages are cascaded, their overall gain in decibels equals the sum of their individual dB gains."
  type: true-false
  answer: true
  explanation: "This is precisely why the dB scale is used. If stage 1 has gain |H₁| and stage 2 has gain |H₂|, the combined gain is |H₁|·|H₂|. In decibels: 20log₁₀(|H₁|·|H₂|) = 20log₁₀|H₁| + 20log₁₀|H₂|. So 40 dB + 20 dB = 60 dB total gain, without any multiplication. This additive property makes cascaded filter and amplifier analysis straightforward on Bode plots."

- question: "A real pole at s = -p contributes exactly -90° of phase shift at the corner frequency ω = p."
  type: true-false
  answer: false
  explanation: "This is a common misconception. The exact phase contributed by a real pole at ω = p is -45°, not -90°. The -90° value is the asymptotic limit that the phase approaches as ω → ∞ (far above the corner frequency). The asymptotic Bode approximation simplifies the phase as: 0° below ω/10, a linear transition from 0° to -90° spanning one decade on each side of the corner, and -90° above 10ω. The exact value at the corner itself is exactly -45° — halfway through the transition."

- question: "Explain how the asymptotic Bode plot technique allows you to sketch the magnitude response of a transfer function without evaluating complex arithmetic at each frequency."
  type: short-answer
  answer: "Each real pole at s = -p contributes two straight-line asymptotes: 0 dB with 0° slope for ω ≪ p, and a -20 dB/decade slope for ω ≫ p, meeting at the corner frequency ω = p. Each zero contributes the reverse: +20 dB/decade above its corner. To sketch the full response, you factor the transfer function to identify all corner frequencies, note any constant gain factor (in dB), then draw the composite magnitude by summing the contributions of all poles and zeros at each frequency region. The result is a piecewise-linear approximation requiring only the identification of corner frequencies — no complex arithmetic."
  explanation: "The power of the technique is that a transfer function with n poles and m zeros has at most n+m straight-line breakpoints in the log-frequency domain. Between breakpoints, the slope changes by ±20 dB/decade per pole/zero. Students who understand this can sketch the response of a multi-pole filter in seconds by inspection, which is the gateway to intuitive filter design and stability analysis."
```

## Explainer

From your AC circuit analysis using phasors, you know that a circuit's behavior at a single frequency ω is captured by its **transfer function** H(jω) = V_out/V_in — a complex number whose magnitude tells you how much the circuit amplifies or attenuates, and whose angle tells you the phase shift. A **frequency response** is simply the collection of all these H(jω) values as ω sweeps from near-zero to very large. The challenge is displaying this information clearly, since frequency can span many orders of magnitude and gain can range from nearly 1 to nearly 0.

The **Bode plot** solves both display problems by using logarithms. The horizontal axis uses log₁₀(ω) so that each factor-of-ten change in frequency occupies equal space — a decade from 100 Hz to 1000 Hz takes the same width as a decade from 1 kHz to 10 kHz. The magnitude is converted to **decibels**: |H|_dB = 20·log₁₀|H(jω)|. This transformation turns multiplicative gain into addition (useful when cascading stages: dB totals add) and compresses large dynamic ranges into a readable scale. A gain of 1/10 becomes -20 dB; a gain of 100 becomes +40 dB. The phase plot shows ∠H(jω) in degrees on a linear vertical scale, also versus log frequency.

The most powerful feature of Bode plots is that they can be **sketched by hand** using asymptotic approximations. Every real pole at s = -p contributes a term 1/(1 + jω/p) to H(jω). At frequencies well below p, this factor contributes 0 dB and 0° phase. At frequencies well above p, the magnitude drops at -20 dB/decade and the phase approaches -90°. The transition happens near ω = p — the **corner frequency** (also called the break frequency or cutoff frequency). You simply draw two straight-line asymptotes meeting at the corner frequency. Each additional pole adds another -20 dB/decade slope break and another -90° of eventual phase lag. Zeros at s = -z work the same way but in reverse: +20 dB/decade slope increase and +90° phase lead.

This asymptotic technique lets you read a transfer function and sketch its Bode plot in minutes, without evaluating complex arithmetic at every frequency. The approximation is exact at the asymptotes and off by at most 3 dB and 6° at the corner frequency itself. The skill is worth practicing carefully because it builds the intuition you will need to understand filter design (why cascading stages multiplies attenuation), resonance (why a complex pole pair produces a peak), and control system stability (why phase lag near the gain crossover frequency is dangerous).
