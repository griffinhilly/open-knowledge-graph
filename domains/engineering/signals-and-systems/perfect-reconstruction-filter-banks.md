---
id: perfect-reconstruction-filter-banks
title: Perfect Reconstruction Filter Banks and Constraints
domain: engineering
course: signals-and-systems
prerequisites:
- id: filter-bank-design-multiband-analysis
  type: hard
builds-toward:
- wavelet-transform-analysis
tags:
- filter-banks
- perfect-reconstruction
- PR-FB
- multirate
stage: advanced
status: draft
---

# Perfect Reconstruction Filter Banks and Constraints

## Core Idea
Perfect reconstruction (PR) filter banks reconstruct the input signal exactly (or with only a delay) despite analysis, downsampling, upsampling, and synthesis stages. PR requires that analysis filters partition the spectrum, downsampling rates match the number of bands, and synthesis filters satisfy special cancellation conditions. PR is essential in audio and image compression codecs. The orthogonal wavelet transform is a special case of PR filter banks.

## How It's Best Learned
Design a 2-band PR filter bank (orthogonal case). Verify that the analysis, downsampling, upsampling, and synthesis cascade produces perfect reconstruction.

## Common Misconceptions
- Thinking PR requires non-overlapping filters (overlapping filters can achieve PR with cancellation).
- Confusing PR constraints with no-aliasing constraint (PR is stronger).
- Not recognizing that PR limits achievable filter characteristics compared to non-PR banks.

## Questions

```yaml
- question: "In a two-band filter bank, a designer uses a perfect lowpass and perfect highpass filter (ideal brickwall filters with no frequency overlap). Why does this NOT achieve perfect reconstruction?"
  type: multiple-choice
  options:
    - "Brickwall filters introduce too much delay, violating the distortion-free condition"
    - "Non-overlapping brickwall filters cannot satisfy the power complementary condition required for aliasing cancellation in the synthesis stage"
    - "The downsampling operation requires overlapping filters to avoid spectral gaps"
    - "Brickwall filters are FIR, and PR requires IIR synthesis filters"
  answer: 1
  explanation: "Perfect reconstruction requires two conditions: aliasing cancellation (A(z) = 0) and distortion-free reconstruction (T(z) = cz^{-n}). The aliasing cancellation condition requires the analysis and synthesis filters to satisfy a power complementary relationship: |H_0(e^{jω})|² + |H_0(e^{j(ω−π)})|² = 1. Ideal brickwall filters do not satisfy this — their transition from 1 to 0 is a step function, not a smoothly complementary shape. Non-overlapping filters eliminate aliasing differently (by preventing it from occurring), but their infinitely sharp transition bands are physically unrealizable and cannot satisfy the algebraic PR conditions."

- question: "Perfect reconstruction in a filter bank is a property of the individual analysis filters alone — if each analysis filter is well-designed, reconstruction will be exact."
  type: multiple-choice
  options:
    - "True, because good frequency selectivity in analysis ensures no information is lost"
    - "False — PR is a property of the analysis-synthesis pair together; the synthesis filters must be specifically designed to cancel the aliasing introduced by the analysis filters and downsampling"
    - "True, because the synthesis filters are just the inverses of the analysis filters by construction"
    - "False — PR depends on the downsampling factor, not the filter design"
  answer: 1
  explanation: "PR is not a property of individual filters — it is a property of the complete analysis-downsample-upsample-synthesis cascade. The downsampling operation introduces aliasing (frequency folding), and the synthesis filters must be specifically designed relative to the analysis filters so that this aliasing cancels exactly when the subbands are recombined. The conjugate quadrature filter (CQF) solution defines synthesis filters as specific transformations of the analysis prototype precisely to guarantee this cancellation. Designing analysis filters independently without constraining the synthesis filters provides no PR guarantee."

- question: "Perfect reconstruction filter banks must use overlapping filters in the frequency domain — non-overlapping (brickwall) filters cannot satisfy PR constraints."
  type: true-false
  answer: true
  explanation: "This is a key counterintuitive result. One might expect that filters with perfectly separated frequency bands (no overlap) would be ideal since downsampling of non-overlapping bands introduces no aliasing. However, ideal brickwall filters are unrealizable in practice, and more importantly, the PR condition requires the power complementary relationship |H_0(e^{jω})|² + |H_0(e^{j(ω−π)})|² = 1, which a step-function brickwall filter cannot satisfy. Practical PR filter banks use carefully shaped overlapping filters where the transition bands are designed so that aliasing from neighboring subbands cancels algebraically in the synthesis stage."

- question: "Perfect reconstruction means that each individual subband output of the analysis filter bank has no aliasing — each subband is a clean, alias-free version of its spectral portion."
  type: true-false
  answer: false
  explanation: "This is a common misconception. Downsampling after the analysis filters does introduce aliasing into each subband — frequency components fold back on themselves. PR does not mean each subband is alias-free; it means the aliasing introduced in all subbands cancels exactly when they are synthesized (upsampled and recombined). This algebraic cancellation across subbands is the core mechanism. A 'no-aliasing' bank would require non-overlapping brickwall filters to prevent aliasing in the first place, which is a completely different (and less practical) design philosophy than PR."

- question: "What are the two conditions that must be simultaneously satisfied for a two-band filter bank to achieve perfect reconstruction, and why must both hold?"
  type: short-answer
  answer: "The two conditions are: (1) aliasing cancellation — the term A(z)X(−z) in the reconstructed signal must be zero, meaning the synthesis filters are chosen so that aliased components from H_0 and H_1 cancel exactly when summed; and (2) distortion-free reconstruction — the remaining term T(z) must equal a pure gain and delay (cz^{-n}), meaning the signal passes through without amplitude or phase distortion beyond a constant delay. Both must hold because they address different failure modes: aliasing cancellation ensures that frequency-folded artifacts from downsampling don't contaminate the output, while the distortion condition ensures the signal's spectral shape is preserved. Satisfying aliasing cancellation alone still allows amplitude and phase distortion; satisfying distortion-free alone still allows aliasing artifacts."
  explanation: "The z-transform analysis of the two-band filter bank yields X̂(z) = T(z)X(z) + A(z)X(−z). For X̂(z) = cz^{-n}X(z) (perfect reconstruction with a delay), we need A(z) = 0 (kill the aliasing term) and T(z) = cz^{-n} (make the distortion term a pure delay). The conjugate quadrature filter family achieves both simultaneously through a specific relationship between the analysis and synthesis filter prototypes."
```

## Explainer

From filter bank design, you know that an analysis bank splits a signal into M frequency subbands using M filters, each followed by M-fold downsampling. The synthesis bank upsamples each subband and recombines them. This two-stage process is the foundation of audio codecs (MP3, AAC), image compression (JPEG 2000), and wavelet analysis. But downsampling introduces **aliasing** — frequency components fold back on top of each other — and upsampling followed by synthesis filtering must undo this folding exactly. The question **perfect reconstruction** (PR) answers is: under what conditions does the entire analysis-downsample-upsample-synthesis cascade reconstruct the original signal exactly?

Examine the two-band case to build intuition. The analysis filters H_0(z) (lowpass) and H_1(z) (highpass) split the signal; each output is downsampled by 2. In the synthesis bank, outputs are upsampled by 2 and filtered by F_0(z) and F_1(z), then summed. After z-transform algebra, the reconstructed signal X̂(z) = T(z)X(z) + A(z)X(−z), where T(z) is the **distortion term** (ideally a pure delay) and A(z)X(−z) is the **aliasing term** from the downsampling/upsampling operation. PR requires two conditions: **(1) aliasing cancellation** — A(z) = 0, meaning the synthesis filters are chosen so the aliased components from H_0 and H_1 cancel exactly when summed; and **(2) distortion-free condition** — T(z) = cz^{−n}, a pure gain and delay. These two constraints together define the PR design space.

The **conjugate quadrature filter** (CQF) or **orthogonal filter bank** solution satisfies both conditions elegantly. Given a prototype lowpass filter H_0(z), set H_1(z) = z^{−(N−1)}H_0(−z^{−1}) (the highpass filter is the modulated time-reversal of the lowpass), and F_0(z) = H_0(z^{−1}), F_1(z) = −H_1(z^{−1}) for the synthesis filters. With these choices, aliasing cancels algebraically and PR holds provided the prototype satisfies a **power complementary** condition: |H_0(e^{jω})|² + |H_0(e^{j(ω−π)})|² = 1. This is the constraint linking filter bank design to orthonormal wavelets — the orthogonal wavelet transform is precisely the iterated application of a 2-band CQF bank, and the PR constraint is why wavelet decomposition can be perfectly inverted.

The cost of PR is a constraint on filter shape. An ideal brickwall lowpass filter would partition frequencies perfectly, but it does not satisfy the power complementary condition (its alias term does not cancel). PR filter banks must use overlapping filters whose transition bands are carefully shaped so that aliasing from one band cancels aliasing from the neighboring band in the synthesis step. This is a fundamentally different design philosophy from a no-aliasing bank (where filters are non-overlapping, so no aliasing occurs in the first place but transition bands must be infinitely sharp). In practice, linear-phase FIR filter banks satisfying PR are designed by the Johnston or Smith-Barnwell families of filters, and they are the building blocks of every modern audio and image compression standard. Recognizing that PR is not a property of individual filters but of the *analysis-synthesis pair together* — and that it is achieved through algebraic cancellation of aliasing artifacts — is the conceptual leap this topic asks you to make.
