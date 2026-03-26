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
- id: filter-design-specifications
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
stage: formal-systems
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

## Questions

```yaml
- question: "In a first-order RC circuit, the output is taken across the capacitor. You want to convert this to a high-pass filter. What is the simplest change?"
  type: multiple-choice
  options:
    - "Replace the capacitor with a larger capacitor to shift the cutoff frequency higher"
    - "Move the output to be taken across the resistor instead of the capacitor"
    - "Add a second resistor in series to increase the filter order"
    - "Replace the resistor with an inductor to invert the frequency response"
  answer: 1
  explanation: "The low-pass RC filter takes output across the capacitor: H(jω) = Z_C/(R + Z_C) = 1/(1 + jωRC). At low ω, Z_C is large and dominates the divider — output ≈ input. At high ω, Z_C is small — output ≈ 0. Swapping the output to the resistor gives H(jω) = R/(R + Z_C) = jωRC/(1 + jωRC). Now at low ω, R is small relative to Z_C — output ≈ 0. At high ω, Z_C shrinks and the resistor dominates — output ≈ input. The cutoff frequency ωc = 1/RC is identical; only the shape changes (from low-pass to high-pass). This swap is the cleanest transformation because it uses the same two-element voltage divider with components interchanged."

- question: "You are designing a filter to eliminate 60 Hz power-line noise from an audio signal while passing all other frequencies. Which filter topology is most appropriate?"
  type: multiple-choice
  options:
    - "First-order RC low-pass filter with cutoff at 60 Hz"
    - "First-order RC high-pass filter with cutoff at 60 Hz"
    - "Band-pass RLC filter centered at 60 Hz"
    - "Band-stop (notch) RLC filter centered at 60 Hz"
  answer: 3
  explanation: "The requirement is to attenuate a *specific* narrow frequency (60 Hz) while passing all others — both below and above. A low-pass filter would block all frequencies above 60 Hz (eliminating most of the audio signal). A high-pass filter would block all frequencies below 60 Hz. A band-pass filter passes only the noise you want to remove. The correct choice is a band-stop (notch) filter, which attenuates a narrow band around the resonant frequency (here, 60 Hz) and passes everything else. The notch is implemented in a series RLC circuit by taking the output across the LC combination: the LC impedance is zero at resonance, short-circuiting the output at exactly the unwanted frequency."

- question: "A passive RC filter attenuates signals at and above the cutoff frequency — signals below the cutoff pass through largely unattenuated."
  type: true-false
  answer: false
  explanation: "This describes the common misconception of a 'brick-wall' filter. Real passive filters have a gradual transition, not an abrupt cutoff. At the cutoff frequency ωc = 1/RC, the gain is 1/√2 ≈ 0.707 (-3 dB) — not zero. Below the cutoff, the signal is progressively less attenuated as frequency decreases; above the cutoff, it is progressively more attenuated. The roll-off rate for a first-order RC filter is -20 dB/decade — for every factor-of-10 increase in frequency beyond the cutoff, the gain drops by a factor of 10. Only an ideal (mathematical) filter has an instantaneous transition; real filters have a gradual passband-to-stopband transition whose steepness depends on filter order."

- question: "A passive filter using primarily resistors, capacitors, and inductors can provide signal gain greater than unity at the resonant frequency of an RLC circuit."
  type: true-false
  answer: false
  explanation: "Passive components can only attenuate — they cannot amplify. The maximum gain a passive filter can achieve is unity (0 dB), which occurs in the passband when the signal passes through essentially unchanged. Although a series RLC circuit can exhibit a resonant peak in the frequency response that *approaches* unity for a lightly damped circuit, it cannot exceed it. The apparent 'peaking' in high-Q RLC filters means the response near resonance is less attenuated than at other frequencies — but still ≤ 1. To achieve gain > 1, active elements (op-amps, transistors) are required. This is a fundamental distinction between passive and active filters."

- question: "Why does a capacitor block low-frequency (DC) signals but pass high-frequency signals, and how does this property produce a low-pass filter when the output is taken across the capacitor?"
  type: short-answer
  answer: "A capacitor's impedance is Z_C = 1/(jωC). At low frequencies (ω → 0), Z_C → ∞ (the capacitor acts as an open circuit, blocking DC). At high frequencies (ω → ∞), Z_C → 0 (the capacitor acts as a short circuit, passing high-frequency signals to ground). In an RC voltage divider with output across the capacitor, at low frequencies the capacitor's large impedance dominates the divider, so most of the input voltage appears across the output — low frequencies pass. At high frequencies the capacitor's small impedance means the resistor dominates, and most voltage drops across the resistor rather than the output — high frequencies are attenuated. This produces the low-pass response."
  explanation: "The voltage divider intuition is the foundation of all passive filter design. For any filter topology, the key question is always: at what frequencies does each impedance dominate the divider? Whichever element the output is taken across determines what passes. Swapping which element is the output node transforms low-pass to high-pass (or vice versa) without changing the cutoff frequency."
```

## Explainer

From your work on frequency response and Bode plots, you know that circuits can have different gains at different frequencies. From impedance analysis, you know that capacitors and inductors have frequency-dependent impedance: Z_C = 1/(jωC) rises as frequency falls (capacitors block DC), and Z_L = jωL rises as frequency rises (inductors block high frequencies). Passive filter design is the craft of exploiting these frequency-dependent impedances — through voltage dividers and resonant networks — to sculpt a desired gain profile across frequency.

The conceptual starting point is the **voltage divider with complex impedances**. A first-order RC low-pass filter is a resistor and capacitor in series, with output taken across the capacitor. The voltage divider gives: H(jω) = Z_C / (R + Z_C) = (1/jωC) / (R + 1/jωC) = 1 / (1 + jωRC). At low frequencies (ω → 0), the denominator approaches 1 and gain approaches unity — DC passes unattenuated. At high frequencies (ω → ∞), the denominator grows large and gain → 0 — high frequencies are blocked. The **cutoff frequency** ωc = 1/RC is the frequency where the gain equals 1/√2 ≈ 0.707, corresponding to half-power (−3 dB). Swapping R and C so the output is taken across R gives a high-pass filter: H(jω) = jωRC / (1 + jωRC), with the complementary behavior — high frequencies pass, low frequencies are blocked, same cutoff.

The cutoff is not a wall but the edge of a gradual transition. A first-order RC filter attenuates by an additional factor of 10 for every decade of frequency beyond the cutoff — a slope of −20 dB/decade. For sharper discrimination between passband and stopband, second-order RLC filters add an inductor, producing a quadratic denominator in the transfer function and a roll-off of −40 dB/decade. The cost of this steeper roll-off is a potential **resonant peak** just before the cutoff (when the circuit is lightly damped): the series RLC circuit's denominator 1 + j(ω/ω₀)(1/Q) − (ω/ω₀)² creates a peak near ω₀ = 1/√LC whose height is controlled by the quality factor Q = ω₀L/R. High Q means sharp resonance and a pronounced peak; low Q means overdamped behavior and a smooth rolloff. Filter design is largely the art of choosing Q and ω₀ to balance roll-off sharpness against in-band flatness.

**Band-pass and band-stop filters** extend these principles by combining low-pass and high-pass responses. A series RLC with output across R passes a band of frequencies centered on resonance while attenuating both higher and lower frequencies. The bandwidth of this passband is BW = ω₀/Q — a higher Q circuit selects a narrower band. Taking the output across the LC pair instead gives a notch (band-stop) response, attenuating a specific frequency while passing others — useful for eliminating power-line interference at 60 Hz or removing a specific interference frequency. In every topology, the design workflow is the same: identify the desired transfer function shape (low-pass, high-pass, band-pass, notch), use the voltage divider / impedance framework to derive the component relationships, and choose R, L, C values to set the desired cutoff or resonant frequency. The mathematics of impedance analysis is the complete toolkit; filter design is its application toward intentional frequency shaping.
