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
stage: abstract-reasoning
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

## Explainer

From filter bank design, you know that an analysis bank splits a signal into M frequency subbands using M filters, each followed by M-fold downsampling. The synthesis bank upsamples each subband and recombines them. This two-stage process is the foundation of audio codecs (MP3, AAC), image compression (JPEG 2000), and wavelet analysis. But downsampling introduces **aliasing** — frequency components fold back on top of each other — and upsampling followed by synthesis filtering must undo this folding exactly. The question **perfect reconstruction** (PR) answers is: under what conditions does the entire analysis-downsample-upsample-synthesis cascade reconstruct the original signal exactly?

Examine the two-band case to build intuition. The analysis filters H_0(z) (lowpass) and H_1(z) (highpass) split the signal; each output is downsampled by 2. In the synthesis bank, outputs are upsampled by 2 and filtered by F_0(z) and F_1(z), then summed. After z-transform algebra, the reconstructed signal X̂(z) = T(z)X(z) + A(z)X(−z), where T(z) is the **distortion term** (ideally a pure delay) and A(z)X(−z) is the **aliasing term** from the downsampling/upsampling operation. PR requires two conditions: **(1) aliasing cancellation** — A(z) = 0, meaning the synthesis filters are chosen so the aliased components from H_0 and H_1 cancel exactly when summed; and **(2) distortion-free condition** — T(z) = cz^{−n}, a pure gain and delay. These two constraints together define the PR design space.

The **conjugate quadrature filter** (CQF) or **orthogonal filter bank** solution satisfies both conditions elegantly. Given a prototype lowpass filter H_0(z), set H_1(z) = z^{−(N−1)}H_0(−z^{−1}) (the highpass filter is the modulated time-reversal of the lowpass), and F_0(z) = H_0(z^{−1}), F_1(z) = −H_1(z^{−1}) for the synthesis filters. With these choices, aliasing cancels algebraically and PR holds provided the prototype satisfies a **power complementary** condition: |H_0(e^{jω})|² + |H_0(e^{j(ω−π)})|² = 1. This is the constraint linking filter bank design to orthonormal wavelets — the orthogonal wavelet transform is precisely the iterated application of a 2-band CQF bank, and the PR constraint is why wavelet decomposition can be perfectly inverted.

The cost of PR is a constraint on filter shape. An ideal brickwall lowpass filter would partition frequencies perfectly, but it does not satisfy the power complementary condition (its alias term does not cancel). PR filter banks must use overlapping filters whose transition bands are carefully shaped so that aliasing from one band cancels aliasing from the neighboring band in the synthesis step. This is a fundamentally different design philosophy from a no-aliasing bank (where filters are non-overlapping, so no aliasing occurs in the first place but transition bands must be infinitely sharp). In practice, linear-phase FIR filter banks satisfying PR are designed by the Johnston or Smith-Barnwell families of filters, and they are the building blocks of every modern audio and image compression standard. Recognizing that PR is not a property of individual filters but of the *analysis-synthesis pair together* — and that it is achieved through algebraic cancellation of aliasing artifacts — is the conceptual leap this topic asks you to make.
