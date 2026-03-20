---
id: passive-filter-design
title: Passive Filter Design
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
- id: impedance-analysis
  type: hard
- id: resonance-circuits
  type: soft
builds-toward:
- op-amp-circuit-applications
tags:
- filters
- low-pass
- high-pass
- band-pass
- band-stop
- notch
- RC-filter
- RLC-filter
- cutoff-frequency
stage: advanced
status: validated
---

# Passive Filter Design

## Core Idea
Passive filters use R, L, and C elements to pass signals in desired frequency bands and attenuate others. A first-order RC low-pass filter has transfer function H(jω) = 1/(1 + jωRC) with cutoff ωc = 1/RC; swapping R and C gives a high-pass filter. Combining low-pass and high-pass stages creates band-pass and band-stop (notch) responses. Adding inductors allows second-order filters with sharper roll-off (−40 dB/decade) and the resonant peaking characteristic of RLC networks. Filter order n determines the asymptotic roll-off rate of −20n dB/decade beyond the cutoff.

## How It's Best Learned
Design filters by specifying the cutoff frequency first, then choosing component values. Use the voltage divider approach with impedances to derive the transfer function algebraically. Compare first-order and second-order responses side by side to see how order affects roll-off sharpness and in-band flatness.

## Common Misconceptions
- Treating the cutoff frequency as an absolute boundary — real filters have gradual roll-offs into the stopband.
- Ignoring loading effects: attaching a load resistance modifies the frequency response unless the load impedance is much larger than the filter's output impedance.
- Assuming passive filters can provide signal gain — passive components can only attenuate; active filters using op-amps are required for gain.

## Explainer

From your work on frequency response and Bode plots, you know that circuits can have different gains at different frequencies. From impedance analysis, you know that capacitors and inductors have frequency-dependent impedance: Z_C = 1/(jωC) rises as frequency falls (capacitors block DC), and Z_L = jωL rises as frequency rises (inductors block high frequencies). Passive filter design is the craft of exploiting these frequency-dependent impedances — through voltage dividers and resonant networks — to sculpt a desired gain profile across frequency.

The conceptual starting point is the **voltage divider with complex impedances**. A first-order RC low-pass filter is a resistor and capacitor in series, with output taken across the capacitor. The voltage divider gives: H(jω) = Z_C / (R + Z_C) = (1/jωC) / (R + 1/jωC) = 1 / (1 + jωRC). At low frequencies (ω → 0), the denominator approaches 1 and gain approaches unity — DC passes unattenuated. At high frequencies (ω → ∞), the denominator grows large and gain → 0 — high frequencies are blocked. The **cutoff frequency** ωc = 1/RC is the frequency where the gain equals 1/√2 ≈ 0.707, corresponding to half-power (−3 dB). Swapping R and C so the output is taken across R gives a high-pass filter: H(jω) = jωRC / (1 + jωRC), with the complementary behavior — high frequencies pass, low frequencies are blocked, same cutoff.

The cutoff is not a wall but the edge of a gradual transition. A first-order RC filter attenuates by an additional factor of 10 for every decade of frequency beyond the cutoff — a slope of −20 dB/decade. For sharper discrimination between passband and stopband, second-order RLC filters add an inductor, producing a quadratic denominator in the transfer function and a roll-off of −40 dB/decade. The cost of this steeper roll-off is a potential **resonant peak** just before the cutoff (when the circuit is lightly damped): the series RLC circuit's denominator 1 + j(ω/ω₀)(1/Q) − (ω/ω₀)² creates a peak near ω₀ = 1/√LC whose height is controlled by the quality factor Q = ω₀L/R. High Q means sharp resonance and a pronounced peak; low Q means overdamped behavior and a smooth rolloff. Filter design is largely the art of choosing Q and ω₀ to balance roll-off sharpness against in-band flatness.

**Band-pass and band-stop filters** extend these principles by combining low-pass and high-pass responses. A series RLC with output across R passes a band of frequencies centered on resonance while attenuating both higher and lower frequencies. The bandwidth of this passband is BW = ω₀/Q — a higher Q circuit selects a narrower band. Taking the output across the LC pair instead gives a notch (band-stop) response, attenuating a specific frequency while passing others — useful for eliminating power-line interference at 60 Hz or removing a specific interference frequency. In every topology, the design workflow is the same: identify the desired transfer function shape (low-pass, high-pass, band-pass, notch), use the voltage divider / impedance framework to derive the component relationships, and choose R, L, C values to set the desired cutoff or resonant frequency. The mathematics of impedance analysis is the complete toolkit; filter design is its application toward intentional frequency shaping.
