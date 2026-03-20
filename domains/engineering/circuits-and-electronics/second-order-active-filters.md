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
stage: advanced
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

## Explainer

From first-order active filters, you know that a single RC section with an op-amp gives −20 dB/decade roll-off above the cutoff frequency — adequate for gentle frequency shaping but too gradual for sharp signal selection. A second-order filter adds a second RC section and uses the op-amp's gain to create two complex conjugate poles in the s-plane. Those two poles together produce −40 dB/decade roll-off and, more importantly, allow the frequency response shape near cutoff to be precisely sculpted using the **quality factor Q**.

The **Sallen-Key topology** is the workhorse implementation. In its low-pass form, two resistors and two capacitors feed a non-inverting op-amp. The op-amp's gain sets a feedback coefficient that effectively adds energy back into the resonance, allowing the poles to move off the real axis into the complex plane. The transfer function in standard form is H(s) = H₀ω₀² / (s² + (ω₀/Q)s + ω₀²), where ω₀ sets the cutoff frequency and Q controls pole placement. When Q < 1/√2 ≈ 0.707, the poles are real and overdamped — the roll-off near cutoff is sluggish and monotone. At Q = 0.707 (**Butterworth** response), the poles are at 45° angles in the left-half plane: the passband is maximally flat with no peaking, and the magnitude is exactly −3 dB at ω₀. At Q > 0.707 (**Chebyshev** territory), the poles move closer to the imaginary axis, creating a peak just before cutoff — you get a steeper transition band but at the cost of ripple in the passband. The **Bessel** response (Q ≈ 0.577) pulls the poles further into the left-half plane for maximally linear phase (flat group delay), preserving pulse shapes but with very gradual roll-off.

Connecting this to resonance circuits you may know: the s-plane pole locations are exactly the natural frequencies you computed in RLC transient analysis. A high-Q second-order filter is the frequency-domain version of a highly underdamped RLC circuit — one that rings for a long time in the time domain manifests as a sharp peak near ω₀ in the frequency domain. The Q factor in filters and the Q factor in resonance circuits are the same mathematical quantity viewed from two different domains.

Higher-order filters are built by **cascading** second-order sections. A fourth-order Butterworth is two Sallen-Key stages in series, each designed with specific Q values from filter tables (Q₁ ≈ 0.541, Q₂ ≈ 1.307 for 4th-order Butterworth). The individual sections don't each look like Butterworth responses — they are shaped so their combined product is Butterworth. Each section is called a **biquad** (for biquadratic transfer function). This modular architecture is powerful: you can design any order filter by stacking second-order building blocks, choosing Q values from standard tables for whichever response family you need. The tradeoff is sensitivity — each section's component tolerances contribute to the overall response error, which is why precision resistors and capacitors matter more as filter order and Q increase.
