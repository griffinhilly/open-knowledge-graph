---
id: iir-filter-design-realization
title: IIR Filter Design and Realization
domain: engineering
course: signals-and-systems
prerequisites:
- id: z-transform-properties-inverse
  type: hard
- id: digital-signal-processing-fundamentals
  type: hard
tags:
- iir-filter
- filter-design
- digital-filters
stage: advanced
status: draft
---

# IIR Filter Design and Realization

## Core Idea
Infinite Impulse Response (IIR) filters have feedback and can achieve steep rolloff with low order. Design methods (Butterworth, Chebyshev, Elliptic) map analog filters to the digital domain via bilinear transform or impulse invariance. Realization structures (Direct Form I/II, cascade, parallel) balance computational efficiency and numerical stability.

## Explainer

From your prerequisites in z-transforms and DSP fundamentals, you know that digital filters are characterized by difference equations: the output at each time step depends on current and past inputs and — for IIR filters — on past outputs as well. That feedback is the defining feature, and it creates poles in the z-domain that give IIR filters a long (theoretically infinite) impulse response. The practical payoff is efficiency: sharp frequency selectivity that would require a 30th-order FIR filter to match can be achieved with a 5th or 6th order IIR. For computationally constrained real-time systems — audio codecs, sensor processing, control loops — this order reduction is decisive.

The standard IIR design workflow begins in the analog domain, exploiting classical analog filter theory. You first choose a filter type based on the passband and stopband requirements. **Butterworth** filters have maximally flat magnitude in the passband — no ripple at all — at the cost of a gradual rolloff. They are the conservative choice when you cannot tolerate passband variation. **Chebyshev Type I** filters allow equiripple in the passband to achieve a steeper rolloff for the same order; Type II moves the ripple to the stopband instead. **Elliptic** (Cauer) filters place equiripple in both the passband and stopband and achieve the steepest possible rolloff for a given filter order — optimal in the minimax sense — at the cost of more complex pole-zero geometry. Once you have chosen the type and specified the cutoff frequencies, ripple tolerances, and required attenuation, the analog prototype poles are determined by closed-form formulas.

Translating the analog prototype H_a(s) to a digital filter H(z) is done via the **bilinear transform**: substitute s = (2/T)·(z−1)/(z+1). This maps the entire left half of the s-plane to the interior of the unit circle in the z-plane, guaranteeing that a stable analog filter produces a stable digital filter. The entire imaginary jω axis maps onto the unit circle, so there is no aliasing of spectral content — a critical advantage over the alternative mapping method (impulse invariance), which aliases the frequency axis for wideband filters. The bilinear transform introduces **frequency warping**: the mapping from analog frequency Ω to digital frequency ω is nonlinear — ω = 2·arctan(ΩT/2) — compressing high analog frequencies toward the Nyquist frequency. You must compensate by **pre-warping** your design cutoff frequencies before designing the analog prototype: the analog cutoff Ω_c = (2/T)·tan(ω_c/2), where ω_c is the desired digital cutoff. After the bilinear transform, the pre-warped frequency lands precisely where you want it in the digital spectrum.

Once H(z) is obtained, it must be **realized** as a network of delays, multiplications, and additions. **Direct Form I** implements the numerator and denominator polynomials sequentially, requiring 2N delay registers for an N-th order filter. **Direct Form II** (the standard form) shares delay registers between the recursive and non-recursive sections, halving the register count to N. However, high-order filters in any Direct Form are numerically sensitive in fixed-point arithmetic: small quantization errors in the coefficients shift pole locations significantly, and poles can drift outside the unit circle, destabilizing the filter. The remedy is **cascade realization**: factor H(z) into second-order sections (biquads), pair each conjugate pole pair with a nearby zero, and implement each biquad in its own Direct Form II. A biquad has only 5 coefficients, its poles are far from the unit circle boundary in the z-plane, and quantization sensitivity is dramatically reduced. **Parallel realization** — partial-fraction expansion of H(z) — is an alternative that also uses second-order sections and offers advantages for certain signal flow architectures. For virtually all fixed-point IIR implementations, cascade of second-order sections is the default choice.
