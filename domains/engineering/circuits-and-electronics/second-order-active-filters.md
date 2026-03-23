---
id: second-order-active-filters
title: Second-Order Active Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: first-order-active-filters
  type: hard
- id: resonance-circuits
  type: soft
tags:
- sallen-key
- butterworth
- chebyshev
- q-factor
- second-order
- damping-ratio
- active-filter
- band-pass
stage: formal-systems
status: draft
---

# Second-Order Active Filters

## Core Idea
Second-order active filters achieve -40 dB/decade roll-off using a single op-amp with two reactive elements, providing steeper frequency selectivity than first-order designs. The Sallen-Key topology is the most common: it uses a non-inverting op-amp configuration with two RC sections and positive feedback through the filter network to create complex conjugate poles. The filter's behavior is characterized by three parameters: cutoff frequency f_0, quality factor Q (or equivalently damping ratio zeta = 1/2Q), and passband gain. Butterworth response (Q = 0.707, maximally flat passband) provides no ripple with moderate roll-off steepness. Chebyshev response (Q > 0.707) allows passband ripple in exchange for a steeper transition band. Bessel response (Q < 0.707) preserves signal waveform shape with maximally flat group delay at the expense of a more gradual roll-off. Higher-order filters are built by cascading second-order sections (biquads), each designed with specific Q values from filter tables to achieve the desired overall response. Band-pass and band-stop second-order filters are also realizable, with the band-pass Q determining selectivity.

## How It's Best Learned
Derive the transfer function of the Sallen-Key low-pass filter by writing KCL at both RC nodes, then express it in standard second-order form H(s) = H_0 * w_0^2 / (s^2 + (w_0/Q)*s + w_0^2). Plot the magnitude response for Q = 0.5, 0.707, and 2 to see underdamped peaking, maximally flat, and rippled responses. Use filter design tables to build a fourth-order Butterworth by cascading two Sallen-Key sections with prescribed Q values.

## Common Misconceptions
- Assuming higher Q is always better — high Q produces peaking near the cutoff that distorts signals with energy near that frequency; Butterworth (Q = 0.707) is the standard choice when flat passband response is needed.
- Believing a single Sallen-Key stage can achieve arbitrarily steep roll-off — it is always second-order (-40 dB/decade); steeper roll-off requires cascading multiple sections.
- Ignoring component sensitivity — the Sallen-Key topology is sensitive to component tolerances, especially at high Q; a 5% change in one resistor can shift the cutoff frequency and Q significantly, requiring precision components for demanding applications.

## Questions

```yaml
- question: "An audio engineer needs to remove frequencies above 5 kHz from a music signal without any amplitude coloration — no peaks or ripple — near the cutoff. Which second-order filter response should she choose?"
  type: multiple-choice
  options:
    - "Chebyshev, because it has the steepest roll-off in the transition band"
    - "Butterworth (Q = 0.707), because it provides a maximally flat passband with no peaking near cutoff"
    - "Bessel, because it has the sharpest transition band for a given filter order"
    - "A high-Q Sallen-Key stage with Q = 2, because higher Q always means sharper frequency selectivity"
  answer: 1
  explanation: "Butterworth is defined by its maximally flat passband — no ripple, no peaking anywhere in the passband. Chebyshev exchanges flatness for a steeper roll-off but introduces ripple in the passband, which would create audible coloration. High Q produces a peak near cutoff (which distorts audio), and Bessel prioritizes linear phase at the cost of a very gradual transition. For flat, uncolored frequency response, Butterworth is the correct choice."

- question: "A Sallen-Key second-order low-pass filter is designed with Q = 2. Compared to a Butterworth design (Q = 0.707) with the same cutoff frequency ω₀, what characterizes the frequency response of the high-Q design?"
  type: multiple-choice
  options:
    - "A steeper roll-off beyond ω₀ with a completely flat passband below ω₀"
    - "A more gradual roll-off everywhere, but with better preservation of pulse shapes"
    - "A peak in the magnitude response near ω₀, where the response exceeds the DC value before rolling off"
    - "Identical passband behavior to Butterworth, but with improved stopband attenuation"
  answer: 2
  explanation: "High Q places the poles close to the imaginary axis in the s-plane, which creates a resonant peak in the frequency response near ω₀. The filter's magnitude actually rises above the passband level before dropping, distorting any signals with energy near the cutoff frequency. This is not 'sharper selectivity' in the useful sense — it is distortion. The common misconception is that higher Q always means a better filter; in reality, Q must be chosen to match the desired response shape."

- question: "A single second-order Sallen-Key stage can achieve arbitrarily steep roll-off by increasing its quality factor Q to very high values."
  type: true-false
  answer: false
  explanation: "A second-order stage always produces -40 dB/decade roll-off in the stopband, regardless of Q. Increasing Q changes the shape of the response near cutoff — creating peaking — but does not increase the asymptotic roll-off rate. To achieve steeper roll-off (e.g., -80 dB/decade), you must cascade additional second-order sections (biquads) to build a 4th-order or higher filter. This is a fundamental constraint imposed by the number of poles, not by Q."

- question: "A high-Q second-order filter corresponds to a highly underdamped system in the time domain — the frequency-domain peaking near ω₀ and the time-domain ringing after a step input are two descriptions of the same underlying pole placement."
  type: true-false
  answer: true
  explanation: "The Q factor describes pole placement in the s-plane. High Q places poles close to the imaginary axis, which in the time domain means slow decay of natural oscillations (ringing) and in the frequency domain means a sharp resonant peak near ω₀. These are not separate phenomena — they are the same mathematical object viewed through the Laplace transform. Understanding this connection is why studying resonance in RLC circuits directly informs filter design."

- question: "Explain the tradeoff you accept when choosing a Chebyshev filter over a Butterworth filter for the same order and cutoff frequency."
  type: short-answer
  answer: "A Chebyshev filter achieves a steeper transition band — it rolls off faster outside the passband — but at the cost of ripple within the passband. The magnitude response oscillates between its maximum and minimum passband values, rather than monotonically decreasing as in Butterworth. In exchange, signals just outside the passband are more strongly attenuated. The tradeoff is: better rejection of unwanted frequencies vs. more distortion of signals inside the passband. Butterworth is better when passband flatness is required; Chebyshev is better when steep skirts matter more than passband uniformity."
  explanation: "The tradeoff is formalized in the filter design parameter Q. Chebyshev designs use Q > 0.707, which places poles closer to the imaginary axis — more resonance, sharper skirts, but also more peaking. Butterworth uses Q = 0.707 exactly, balancing response shape optimally. Neither is universally superior: the right choice depends on the application's tolerance for passband ripple versus its need for stopband rejection."
```

## Explainer

From first-order active filters, you know that a single RC section with an op-amp gives −20 dB/decade roll-off above the cutoff frequency — adequate for gentle frequency shaping but too gradual for sharp signal selection. A second-order filter adds a second RC section and uses the op-amp's gain to create two complex conjugate poles in the s-plane. Those two poles together produce −40 dB/decade roll-off and, more importantly, allow the frequency response shape near cutoff to be precisely sculpted using the **quality factor Q**.

The **Sallen-Key topology** is the workhorse implementation. In its low-pass form, two resistors and two capacitors feed a non-inverting op-amp. The op-amp's gain sets a feedback coefficient that effectively adds energy back into the resonance, allowing the poles to move off the real axis into the complex plane. The transfer function in standard form is H(s) = H₀ω₀² / (s² + (ω₀/Q)s + ω₀²), where ω₀ sets the cutoff frequency and Q controls pole placement. When Q < 1/√2 ≈ 0.707, the poles are real and overdamped — the roll-off near cutoff is sluggish and monotone. At Q = 0.707 (**Butterworth** response), the poles are at 45° angles in the left-half plane: the passband is maximally flat with no peaking, and the magnitude is exactly −3 dB at ω₀. At Q > 0.707 (**Chebyshev** territory), the poles move closer to the imaginary axis, creating a peak just before cutoff — you get a steeper transition band but at the cost of ripple in the passband. The **Bessel** response (Q ≈ 0.577) pulls the poles further into the left-half plane for maximally linear phase (flat group delay), preserving pulse shapes but with very gradual roll-off.

Connecting this to resonance circuits you may know: the s-plane pole locations are exactly the natural frequencies you computed in RLC transient analysis. A high-Q second-order filter is the frequency-domain version of a highly underdamped RLC circuit — one that rings for a long time in the time domain manifests as a sharp peak near ω₀ in the frequency domain. The Q factor in filters and the Q factor in resonance circuits are the same mathematical quantity viewed from two different domains.

Higher-order filters are built by **cascading** second-order sections. A fourth-order Butterworth is two Sallen-Key stages in series, each designed with specific Q values from filter tables (Q₁ ≈ 0.541, Q₂ ≈ 1.307 for 4th-order Butterworth). The individual sections don't each look like Butterworth responses — they are shaped so their combined product is Butterworth. Each section is called a **biquad** (for biquadratic transfer function). This modular architecture is powerful: you can design any order filter by stacking second-order building blocks, choosing Q values from standard tables for whichever response family you need. The tradeoff is sensitivity — each section's component tolerances contribute to the overall response error, which is why precision resistors and capacitors matter more as filter order and Q increase.
