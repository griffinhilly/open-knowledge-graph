---
id: multirate-decimation-interpolation
title: Multirate Signal Processing and Filter Banks
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
- id: aliasing-reconstruction-signals
  type: hard
- id: dft-and-fft-algorithms
  type: soft
tags:
- multirate
- decimation
- interpolation
- filter-banks
stage: advanced
status: draft
---

# Multirate Signal Processing and Filter Banks

## Core Idea
Decimation reduces sampling rate by integer factor M after anti-aliasing filtering; interpolation increases rate by factor L by inserting zeros and low-pass filtering. Polyphase filter structures decompose filters into parallel paths operating at reduced rates, enabling efficient implementation. Multirate systems are fundamental in audio codecs, communication systems, and signal processing applications.

## Questions

```yaml
- question: "A signal sampled at 48 kHz needs to be decimated by factor M = 4 to produce a 12 kHz signal. In what order must operations be performed, and to what frequency should the filter's cutoff be set?"
  type: multiple-choice
  options:
    - "Downsample first to 12 kHz, then low-pass filter at 6 kHz to clean up artifacts"
    - "Low-pass filter at 6 kHz cutoff, then downsample by 4 — to remove content that would alias after downsampling"
    - "Low-pass filter at 24 kHz cutoff (half of 48 kHz), then downsample by 4"
    - "Order doesn't matter for linear time-invariant systems — filtering before or after downsampling gives the same result"
  answer: 1
  explanation: "Downsampling compresses the time axis by M, which expands the spectrum by M in frequency. Any content between f_s/(2M) = 6 kHz and f_s/2 = 24 kHz would fold back (alias) into the 0–6 kHz band and become indistinguishable from genuine low-frequency content. The anti-aliasing filter must remove this content before downsampling occurs. Filtering after downsampling is too late — the aliased components have already merged with the signal and cannot be separated. Order absolutely matters; linear time-invariance applies to fixed-rate systems, not rate-changing operations."

- question: "A student says that polyphase decomposition is just 'a different hardware arrangement' that produces the same output as a direct FIR implementation, without any real computational savings. What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Polyphase decomposition changes the frequency response of the filter, producing slightly different output"
    - "Direct FIR implementation computes and then discards M − 1 out of every M outputs; polyphase restructures the computation to produce only the outputs that are kept, reducing multiply-accumulate operations by a factor of M"
    - "Polyphase only works when M is a power of two, so it is not a general technique"
    - "The computational savings only appear in hardware implementations, not in software"
  answer: 1
  explanation: "The student is correct that polyphase produces mathematically identical output — but wrong about savings. A naive N-tap FIR filter applied at rate f_s before decimation by M computes N multiplications per input sample, even though M − 1 of every M outputs are immediately discarded. Polyphase reorders the computation into M sub-filters of length N/M, each operating at the lower rate f_s/M. The result: N/M multiplications per output sample instead of N — an M-fold reduction. This is a real, substantial computational saving that makes real-time multirate processing practical."

- question: "In interpolation by factor L, inserting L − 1 zeros between every existing sample produces the correctly upsampled signal without any additional filtering."
  type: true-false
  answer: false
  explanation: "Zero-insertion (upsampling) increases the sample rate to L·f_s, but it introduces imaging: the original signal's spectrum is repeated at multiples of the original sampling frequency, creating unwanted spectral copies. These images appear as high-frequency artifacts that contaminate the upsampled signal. A low-pass filter at cutoff f_s/2 (in the new higher rate) must be applied after zero-insertion to remove these images, leaving a smooth bandlimited interpolation. The filter effectively 'fills in' the zero samples with correctly weighted values."

- question: "Decimation followed by interpolation with the same factor M is a lossless operation — the original signal can always be recovered exactly."
  type: true-false
  answer: false
  explanation: "Decimation is lossy. The anti-aliasing filter applied before downsampling removes all spectral content above f_s/(2M). This high-frequency content is permanently discarded — it is not present in the decimated signal and cannot be reconstructed by any subsequent interpolation. Interpolation fills in missing samples but cannot invent information that was filtered out. Only if the original signal was strictly bandlimited to f_s/(2M) from the start would decimation-then-interpolation be lossless."

- question: "Why does naive decimation — simply keeping every M-th sample without any pre-filtering — corrupt the downsampled signal, and what does the anti-aliasing filter prevent?"
  type: short-answer
  answer: "Keeping every M-th sample compresses the time axis by M, which in the frequency domain stretches the spectrum by M. Frequency components that were between f_s/(2M) and f_s/2 in the original signal now fold back into the baseband (0 to f_s/(2M)). These aliased components overlap with genuine low-frequency content and are mathematically indistinguishable from it — they corrupt the signal irreversibly. The anti-aliasing low-pass filter, applied before downsampling, removes all content above f_s/(2M), ensuring that nothing with the potential to alias is present. After filtering, the content that remains cannot fold on top of itself, so downsampling is safe."
  explanation: "This is the same principle as the Nyquist theorem, applied to a rate-reduction operation: the new, lower Nyquist rate is f_s/(2M), and the pre-filter enforces the bandwidth constraint that makes the reduced-rate sampling faithful."
```

## Explainer

From sampling theory, you know that a signal with bandwidth B Hz requires a sampling rate of at least 2B Hz to be reconstructed perfectly. From aliasing, you know what goes wrong when that rule is violated: high-frequency components fold back into the baseband and are indistinguishable from genuine low-frequency content. Multirate processing asks a more practical question: what if you have already sampled a signal and need to work with it at a *different* rate — either lower (to save computation or storage) or higher (to interface with another system)? The answers are **decimation** and **interpolation**, and both require careful anti-aliasing logic you already know how to reason about.

**Decimation by M** means keeping only every M-th sample and discarding the rest. Naively doing this would compress the time axis by M, which in the frequency domain expands the spectrum by M — any content between f_s/(2M) and f_s/2 would alias into the lower-frequency band. The solution is to low-pass filter the signal to bandwidth f_s/(2M) *before* discarding samples. This anti-aliasing filter ensures the content that would alias has been removed. The combined operation — filter then downsample — is decimation. The result is a signal at rate f_s/M that faithfully represents the original signal's content up to f_s/(2M). The computational payoff is that all subsequent processing happens at the lower rate, with fewer multiplications per second.

**Interpolation by L** is the reverse: you want more samples per second from a signal that currently has fewer. The procedure is to insert L−1 zeros between every existing sample (upsampling), then apply a low-pass filter at cutoff f_s/2 (in the new higher rate). The zero-insertion step creates a signal at rate L·f_s, but examining its DTFT reveals that the original spectrum now repeats at multiples of the original f_s — in other words, imaging artifacts (the interpolation analog of aliasing). The low-pass filter removes these images, leaving a smoothly interpolated signal. Conceptually, the filter "fills in" the inserted zeros with values that make the waveform continuous and bandlimited. Rational rate conversions by a factor L/M are achieved by cascading interpolation by L with decimation by M.

The efficiency bottleneck in both operations is the anti-aliasing or anti-imaging filter. A direct implementation of an N-tap FIR filter applied before decimation by M would compute N multiplications per input sample, even though M−1 out of every M outputs are immediately discarded — clearly wasteful. **Polyphase decomposition** resolves this by rearranging the filter computation. The filter's coefficients are split into M sub-filters (polyphase components), each of which operates at the lower rate. The computation now costs N/M multiplications per output sample — exactly what you'd expect after moving filtering to the lower rate. This factor-of-M efficiency gain is what makes multirate processing practical in real-time systems. In audio codecs (MP3, AAC), video processing, and software-defined radio, signals are routinely processed at different rates in different stages, and polyphase filter banks are the core computational structure enabling all of it.

