---
id: filter-classification-design-basics
title: Filter Classification and Design Basics
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-magnitude-phase
  type: hard
- id: bode-plot-construction-interpretation
  type: hard
builds-toward:
- iir-filter-design-realization
- fir-filter-design-realization
tags:
- filter-design
- filter-classification
- frequency-response
stage: advanced
status: draft
---

# Filter Classification and Design Basics

## Core Idea
Filters are classified by passband type (low-pass, high-pass, band-pass, band-stop) and response shape (Butterworth maximizes flatness, Chebyshev allows ripple for steeper rolloff, Elliptic trades passband/stopband ripple for minimum order). Design trade-offs balance order, rolloff steepness, passband ripple, and phase linearity.

## Explainer

Your Bode plot skills give you a visual language for what filters do: the magnitude plot shows, at every frequency, how much the filter amplifies or attenuates a sinusoidal input. **Filter design** is the inverse problem: given a desired shape for that Bode magnitude plot, construct the transfer function H(s) or H(z) whose Bode plot matches it. The four passband archetypes — **low-pass** (pass below ωc, attenuate above), **high-pass** (reverse), **band-pass** (pass a frequency band, attenuate outside), and **band-stop** (attenuate a band, pass outside) — each arise directly from the shape of the magnitude plot you're targeting. Every signal-processing application maps onto one: anti-aliasing before sampling needs a low-pass; carrier isolation in radio needs a band-pass; 60 Hz hum rejection needs a notch (band-stop).

Once you have chosen the passband type, you must specify the transition: how sharply does the filter move from "pass" to "attenuate"? A brick-wall transition (zero at ωc, infinite attenuation at ωc + ε) requires infinite order, which is physically unrealizable. A realizable filter of order N rolls off at −20N dB/decade beyond the cutoff — so higher order means steeper rolloff, but also more poles, more computation (digital) or more components (analog). The design problem is to achieve the required attenuation in the stopband while keeping ripple in the passband below specification, using the minimum filter order. Three classical **approximation strategies** solve this problem differently.

**Butterworth filters** achieve the flattest possible passband by making all derivatives of |H(jω)|² zero at ω = 0. The magnitude response is |H(jω)|² = 1/(1 + (ω/ωc)^(2N)) — it rolls off smoothly from unity with no ripple. The cost is that this flatness "wastes" degrees of freedom on passband smoothness rather than stopband rejection, requiring higher N than other approximations for the same rolloff steepness. **Chebyshev Type I** filters accept equiripple oscillations in the passband (you specify the allowed ripple in dB, e.g., 0.5 dB) in exchange for steeper rolloff at the same order. The Chebyshev polynomials, which oscillate between ±1 on [−1,1], generate this equiripple property — the filter magnitude oscillates within the passband tolerance band exactly N times. For the same order N and cutoff, a Chebyshev filter reaches a given stopband attenuation at a lower stopband frequency than Butterworth. **Elliptic (Cauer)** filters place equiripple in both passband and stopband, achieving the absolute minimum filter order for given passband ripple, stopband ripple, and transition-band width. They are optimal by this measure but have the most non-linear phase response.

The phase response trade-off runs orthogonal to magnitude: Butterworth has the most linear phase of the three; elliptic the least. In applications where timing matters — data communications, high-fidelity audio, control systems — phase non-linearity causes group delay distortion that corrupts signal shape. If phase linearity is critical, a **Bessel** filter (not listed in the core idea but important in practice) maximizes group delay flatness at the expense of poor rolloff steepness, or a separate all-pass phase equalizer can be added after an elliptic magnitude filter. The practical design workflow is: specify passband edge and ripple, stopband edge and attenuation, note whether phase linearity matters; compute the minimum order for each approximation type; choose based on available order budget and phase requirements. Tables of normalized prototype poles (or one-line software calls like `scipy.signal.butter`) handle the arithmetic — your job is knowing which approximation to choose and why.
