---
id: first-order-active-filters
title: First-Order Active Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: passive-filter-design
  type: hard
- id: operational-amplifier-fundamentals
  type: hard
builds-toward:
- second-order-active-filters
tags:
- active-filter
- low-pass
- high-pass
- op-amp-filter
- cutoff-frequency
- passband-gain
- roll-off
stage: formal-systems
status: draft
---

# First-Order Active Filters

## Core Idea
First-order active filters combine op-amps with RC networks to achieve frequency-selective behavior with passband gain — something passive filters cannot provide. An active low-pass filter places a capacitor in the feedback path of an inverting amplifier (or uses a non-inverting topology with an RC network at the input), producing a transfer function with a flat passband gain of -R_f/R_in and a -20 dB/decade roll-off above the cutoff frequency f_c = 1/(2*pi*R_f*C). The active high-pass filter places the capacitor in the input path, passing high frequencies with gain while attenuating frequencies below f_c. Unlike passive filters, active filters can provide gain greater than unity in the passband, have low output impedance (driven by the op-amp output), and do not suffer from loading effects when cascaded. The cutoff frequency and passband gain are independently adjustable through separate component choices. However, active filters are limited by the op-amp's gain-bandwidth product, supply voltage, and power consumption — constraints absent in passive designs.

## How It's Best Learned
Start from the inverting amplifier and replace either R_in or R_f with an impedance (R + 1/jwC or R || 1/jwC). Derive the transfer function, identify the cutoff frequency and passband gain, then sketch the Bode magnitude and phase plots. Compare directly to the equivalent passive RC filter to see the gain advantage and the independence of gain and cutoff frequency settings.

## Common Misconceptions
- Assuming active filters are always superior to passive filters — at very high frequencies (above the op-amp's useful bandwidth), passive filters outperform active ones, and passive filters require no power supply.
- Setting the passband gain arbitrarily high without considering the gain-bandwidth product — a first-order active filter with 40 dB passband gain and a 10 kHz cutoff requires an op-amp GBW of at least 1 MHz, and the roll-off will deviate from ideal well before that.
- Believing first-order active filters have sharper roll-off than first-order passive filters — both roll off at -20 dB/decade; the active version adds gain and buffering but does not change the filter order or roll-off rate.

## Questions

```yaml
- question: "An inverting active low-pass filter has passband gain = -Rf/Rin and cutoff frequency fc = 1/(2πRfC). An engineer wants to double the passband gain without changing the cutoff frequency. What should she do?"
  type: multiple-choice
  options:
    - "Halve Rin while keeping Rf and C unchanged — gain doubles, cutoff is unaffected since Rf and C don't change"
    - "Double Rf while keeping all other components unchanged — gain doubles and cutoff shifts proportionally"
    - "Double C while keeping Rf and Rin unchanged — the capacitor controls both gain and cutoff equally"
    - "Double both Rf and Rin proportionally — this maintains the gain ratio while adjusting for higher frequency"
  answer: 0
  explanation: "Passband gain = Rf/Rin; cutoff fc = 1/(2πRfC). To double gain, double the ratio Rf/Rin. To keep cutoff fixed, keep Rf and C unchanged. Therefore halve Rin: new gain = Rf/(Rin/2) = 2Rf/Rin. Option 1 (doubling Rf only) changes both gain and cutoff simultaneously. This demonstrates the key advantage of active filters: gain (set by resistor ratio) and cutoff (set by Rf × C) are independently adjustable through separate components."

- question: "A first-order active low-pass filter and a first-order passive RC low-pass filter are both designed with a cutoff frequency of 1 kHz. How do their roll-off rates above 1 kHz compare?"
  type: multiple-choice
  options:
    - "Both roll off at -20 dB/decade — the active version adds passband gain and buffering but does not change the filter order or roll-off rate"
    - "The active filter rolls off at -40 dB/decade, because the op-amp adds an additional pole to the transfer function"
    - "The active filter rolls off at -20 dB/decade; the passive rolls off at -10 dB/decade due to loading effects"
    - "The active filter maintains flat gain at all frequencies; only the passive version has a roll-off region"
  answer: 0
  explanation: "Roll-off rate is determined by filter ORDER — a first-order filter always rolls off at -20 dB/decade, regardless of whether it is active or passive. The op-amp does NOT add a pole in a first-order active filter; it provides gain and isolation. Option 1 (op-amp adds a pole, -40 dB/decade) is the most tempting misconception — active does not mean sharper. To get steeper roll-off, you need a higher-order filter design."

- question: "A first-order active high-pass filter has a steeper roll-off below the cutoff frequency than an equivalent first-order passive RC high-pass filter."
  type: true-false
  answer: false
  explanation: "Both are first-order filters and both roll off at exactly -20 dB/decade below the cutoff frequency. Adding an op-amp adds passband gain and prevents loading effects when cascaded, but it does not change the filter order. Roll-off slope is governed by the number of poles in the transfer function, not by whether the circuit is active or passive."

- question: "The gain-bandwidth product (GBW) of an op-amp limits the practical performance of active filters at high frequencies."
  type: true-false
  answer: true
  explanation: "An op-amp's open-loop gain drops at high frequencies. For a filter with passband gain A and cutoff frequency fc, the op-amp must supply gain × bandwidth = A × fc. If this product exceeds the op-amp's GBW, the op-amp's own rolloff will interfere with the designed filter response. For example, a 40 dB gain (100×) filter with a 10 kHz cutoff requires GBW ≥ 1 MHz. At very high frequencies, passive filters are often preferred precisely because they have no power supply or bandwidth limitations."

- question: "What is the fundamental capability that active filters have over passive RC filters, and what circuit property of the op-amp makes this possible?"
  type: short-answer
  answer: "Active filters can provide passband gain greater than unity — passive filters can only attenuate (maximum passband gain is 0 dB). The op-amp's near-zero output impedance also prevents loading effects when stages are cascaded, enabling each stage to be designed independently. These two properties — gain and isolation — are unavailable in passive designs and make active filters essential when signal amplification and multistage filtering are needed simultaneously."
  explanation: "The near-infinite input impedance and near-zero output impedance of the op-amp solve both problems passive filters face: inability to amplify and sensitivity to loading. When cascading two passive RC stages, the second stage loads the first, shifting the cutoff frequency. Active stages are perfectly isolated: the op-amp output drives the next stage from zero impedance, so the second stage has no effect on the first."
```

## Explainer

From your study of passive filters, you know that an RC low-pass filter attenuates signals above a cutoff frequency f_c = 1/(2πRC) at a rate of -20 dB/decade, while passing lower frequencies. The limitation is fundamental: a passive filter can only attenuate — it cannot amplify. Its passband gain is at most 0 dB (unity), and when you cascade two passive RC stages to improve roll-off, the second stage loads the first, shifting the cutoff frequency in a way that's hard to predict without careful analysis. From your study of op-amps, you know the op-amp has near-infinite input impedance and near-zero output impedance — properties that directly solve both of these problems.

An **active low-pass filter** combines an RC network with an op-amp amplifier. In the simplest inverting topology, you replace the feedback resistor R_f of an inverting amplifier with a parallel combination of R_f and a capacitor C. At DC and low frequencies, the capacitor is an open circuit, so the gain is simply -R_f/R_in — the ordinary inverting amplifier gain. At high frequencies, the capacitor's impedance Z_C = 1/(jωC) drops, progressively shorting out R_f and reducing the gain. The frequency where this transition occurs is the cutoff f_c = 1/(2πR_f C). The transfer function is H(f) = -(R_f/R_in) × 1/(1 + j f/f_c), which combines a flat passband gain of -R_f/R_in with the familiar first-order rolloff. Crucially, the gain magnitude R_f/R_in and the cutoff frequency 1/(2πR_f C) are controlled by separate components: you can independently set gain by choosing R_in and set cutoff by choosing C, then pick R_f to satisfy both.

The active high-pass filter reverses the placement: a capacitor C in series with the input resistor R_in. At low frequencies, C has high impedance and blocks the signal; at high frequencies, C acts like a short circuit and the circuit behaves like a standard inverting amplifier. The cutoff frequency is again f_c = 1/(2πR_in C), and the passband gain above f_c is -R_f/R_in. The Bode plot is the mirror image of the low-pass case: flat gain above f_c, -20 dB/decade rolloff below it.

The op-amp's output impedance advantage becomes clear when you cascade stages. Because the op-amp drives the next stage from a near-zero output impedance, the second stage has no effect on the first stage's transfer function — each stage is perfectly buffered. This lets you build a second-order active filter simply by cascading two first-order stages, with predictable independent cutoff frequencies. The one constraint to respect: op-amps have a finite **gain-bandwidth product** (GBW). An op-amp with GBW = 1 MHz used at a passband gain of 100 (40 dB) has only 10 kHz of usable bandwidth before the op-amp's own rolloff interferes. Always verify that your desired passband gain × cutoff frequency is well within the op-amp's GBW.
