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

## Questions

```yaml
- question: "A designer implements a 12th-order IIR lowpass filter in Direct Form II on a fixed-point DSP. During testing, the filter output diverges exponentially. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The bilinear transform was applied incorrectly, mapping stable analog poles to unstable z-domain positions"
    - "Coefficient quantization in the high-order Direct Form II polynomial caused poles to drift outside the unit circle"
    - "The sampling rate was set too low, causing the passband to alias into the stopband"
    - "The Butterworth prototype specification was incorrect, selecting a filter order too high for the cutoff frequency"
  answer: 1
  explanation: "High-order IIR filters in Direct Form II are numerically sensitive: the coefficients of a high-degree polynomial in z must be represented with limited fixed-point precision, and small quantization errors cause significant displacement of pole locations. Poles that were designed to sit safely inside the unit circle can drift outside it, producing instability. This is not a design error in the bilinear transform — it is an implementation problem unique to high-order direct-form structures. The remedy is cascade realization as second-order biquad sections, which confines each polynomial to order 2 and dramatically reduces sensitivity."

- question: "Why must the analog cutoff frequency be pre-warped before applying the bilinear transform when designing a digital IIR filter?"
  type: multiple-choice
  options:
    - "Because the bilinear transform introduces aliasing that shifts the entire passband upward by a fixed amount"
    - "Because the bilinear transform maps analog to digital frequencies nonlinearly, compressing high frequencies, so the digital cutoff will not match the intended frequency without correction"
    - "Because the impulse invariance method requires pre-warping to prevent aliasing of the imaginary-axis poles"
    - "Because pre-warping corrects for the group delay introduced by the feedback poles in the IIR structure"
  answer: 1
  explanation: "The bilinear transform maps the entire analog frequency axis (−∞ to +∞) onto the digital frequency range (−π to +π) through a nonlinear (tangent) compression. A specified analog cutoff frequency Ω_c does not land at the corresponding digital frequency ω_c = Ω_c · T after transformation — it gets compressed. Pre-warping adjusts the analog prototype's cutoff to Ω_c = (2/T)·tan(ω_c/2) before designing, so that after the bilinear transform is applied, the digital filter's cutoff lands exactly where intended. Without pre-warping, the passband edge will be systematically off."

- question: "An elliptic IIR filter achieves a steeper rolloff than a Butterworth filter of the same order by allowing equiripple in both the passband and the stopband."
  type: true-false
  answer: true
  explanation: "Butterworth filters achieve maximally flat magnitude in the passband — zero ripple — at the cost of a gradual transition from passband to stopband. Chebyshev filters trade passband (or stopband) flatness for a steeper rolloff. Elliptic (Cauer) filters allow equiripple in both the passband AND the stopband, achieving the steepest possible rolloff for a given filter order — they are optimal in the minimax sense. The tradeoff is more complex pole-zero geometry and less predictable group delay. For strict attenuation specs with tight order constraints, elliptic filters deliver the most selectivity."

- question: "Cascade realization of an IIR filter as second-order biquad sections requires more multiply-add operations per output sample than Direct Form II, which is why Direct Form II is preferred in practice."
  type: true-false
  answer: false
  explanation: "The computational cost of cascade realization and Direct Form II is approximately the same — both require roughly 2N multiplications and additions per sample for an N-th order filter. The reason cascade realization is preferred in fixed-point implementations is numerical stability, not computation. In cascade form, each biquad has only 5 coefficients and represents a well-conditioned second-order polynomial; quantization errors cause small, manageable pole displacement. High-order Direct Form II is numerically ill-conditioned. Computation is essentially equivalent; stability is the decisive factor."

- question: "Explain why cascade realization of an IIR filter as a series of second-order sections is preferred over Direct Form II for high-order fixed-point implementations."
  type: short-answer
  answer: "In Direct Form II, the filter's poles are roots of a single high-degree polynomial whose coefficients must be stored in fixed-point arithmetic. Small quantization errors in high-degree polynomial coefficients cause large shifts in pole locations — sensitivity grows rapidly with order — and poles can drift outside the unit circle, destabilizing the filter. In cascade realization, H(z) is factored into second-order sections (biquads), each with only five coefficients representing one conjugate pole pair and nearby zeros. Each biquad's poles are far from the unit circle boundary in that section's coefficient space, and quantization errors cause much smaller, manageable displacements. The filter remains stable even under fixed-point limitations."
  explanation: "The numerical sensitivity of polynomial root locations to coefficient errors is a classical result: roots of high-degree polynomials can shift dramatically in response to tiny coefficient perturbations. By decomposing the filter into biquads, the cascade approach avoids high-degree polynomial representation entirely, confining sensitivity to small, isolated second-order polynomials. This is the key insight that makes cascade of biquads the standard for practical IIR implementation."
```

## Explainer

From your prerequisites in z-transforms and DSP fundamentals, you know that digital filters are characterized by difference equations: the output at each time step depends on current and past inputs and — for IIR filters — on past outputs as well. That feedback is the defining feature, and it creates poles in the z-domain that give IIR filters a long (theoretically infinite) impulse response. The practical payoff is efficiency: sharp frequency selectivity that would require a 30th-order FIR filter to match can be achieved with a 5th or 6th order IIR. For computationally constrained real-time systems — audio codecs, sensor processing, control loops — this order reduction is decisive.

The standard IIR design workflow begins in the analog domain, exploiting classical analog filter theory. You first choose a filter type based on the passband and stopband requirements. **Butterworth** filters have maximally flat magnitude in the passband — no ripple at all — at the cost of a gradual rolloff. They are the conservative choice when you cannot tolerate passband variation. **Chebyshev Type I** filters allow equiripple in the passband to achieve a steeper rolloff for the same order; Type II moves the ripple to the stopband instead. **Elliptic** (Cauer) filters place equiripple in both the passband and stopband and achieve the steepest possible rolloff for a given filter order — optimal in the minimax sense — at the cost of more complex pole-zero geometry. Once you have chosen the type and specified the cutoff frequencies, ripple tolerances, and required attenuation, the analog prototype poles are determined by closed-form formulas.

Translating the analog prototype H_a(s) to a digital filter H(z) is done via the **bilinear transform**: substitute s = (2/T)·(z−1)/(z+1). This maps the entire left half of the s-plane to the interior of the unit circle in the z-plane, guaranteeing that a stable analog filter produces a stable digital filter. The entire imaginary jω axis maps onto the unit circle, so there is no aliasing of spectral content — a critical advantage over the alternative mapping method (impulse invariance), which aliases the frequency axis for wideband filters. The bilinear transform introduces **frequency warping**: the mapping from analog frequency Ω to digital frequency ω is nonlinear — ω = 2·arctan(ΩT/2) — compressing high analog frequencies toward the Nyquist frequency. You must compensate by **pre-warping** your design cutoff frequencies before designing the analog prototype: the analog cutoff Ω_c = (2/T)·tan(ω_c/2), where ω_c is the desired digital cutoff. After the bilinear transform, the pre-warped frequency lands precisely where you want it in the digital spectrum.

Once H(z) is obtained, it must be **realized** as a network of delays, multiplications, and additions. **Direct Form I** implements the numerator and denominator polynomials sequentially, requiring 2N delay registers for an N-th order filter. **Direct Form II** (the standard form) shares delay registers between the recursive and non-recursive sections, halving the register count to N. However, high-order filters in any Direct Form are numerically sensitive in fixed-point arithmetic: small quantization errors in the coefficients shift pole locations significantly, and poles can drift outside the unit circle, destabilizing the filter. The remedy is **cascade realization**: factor H(z) into second-order sections (biquads), pair each conjugate pole pair with a nearby zero, and implement each biquad in its own Direct Form II. A biquad has only 5 coefficients, its poles are far from the unit circle boundary in the z-plane, and quantization sensitivity is dramatically reduced. **Parallel realization** — partial-fraction expansion of H(z) — is an alternative that also uses second-order sections and offers advantages for certain signal flow architectures. For virtually all fixed-point IIR implementations, cascade of second-order sections is the default choice.
