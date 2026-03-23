---
id: filter-bank-design-multiband-analysis
title: Filter Banks and Multiband Signal Decomposition
domain: engineering
course: signals-and-systems
prerequisites:
- id: butterworth-filter-maximally-flat-response
  type: soft
- id: chebyshev-filter-equiripple-response
  type: soft
builds-toward:
- perfect-reconstruction-filter-banks
- multirate-decimation-interpolation
tags:
- filter-banks
- multiband
- decomposition
- analysis
stage: expert
status: validated
---

# Filter Banks and Multiband Signal Decomposition

## Core Idea
Filter banks decompose a signal into multiple frequency bands using parallel banks of complementary filters. Analysis filter banks partition the spectrum; synthesis banks reconstruct the signal. Critically-sampled banks have one output sample per input sample in each band. Perfect reconstruction (PR) requires that analysis and synthesis stages cancel distortion. Applications include audio coding, speech processing, and spectrum analysis.

## How It's Best Learned
Design a simple 2-band filter bank with highpass and lowpass filters. Verify the frequency division and test on signals in each band.

## Common Misconceptions
- Thinking all filter banks achieve perfect reconstruction without special design.
- Assuming standard highpass-lowpass division is optimal for all applications.
- Not recognizing aliasing cancellation requirements in PR filter banks.

## Questions

```yaml
- question: "A student designs a 2-band filter bank by pairing a Butterworth lowpass filter with a Butterworth highpass filter at the same cutoff, downsampling each output by 2, then upsampling and summing to reconstruct the signal. Why will this not achieve perfect reconstruction?"
  type: multiple-choice
  options:
    - "Butterworth filters have non-ideal stopbands that always pass some signal energy, causing distortion"
    - "Downsampling introduces aliasing within each band, and the synthesis stage must be specifically designed to cancel this aliasing — standard Butterworth filters are not designed to do this"
    - "Perfect reconstruction requires at least 4 bands; a 2-band bank is inherently too coarse"
    - "The cutoff frequencies must differ between the highpass and lowpass filters to avoid spectral overlap at the boundary"
  answer: 1
  explanation: "Downsampling each sub-band by 2 folds residual out-of-band energy (from the filter's imperfect stopband) back into the passband — this is aliasing. The synthesis filters cannot undo this aliasing unless they are specifically designed together with the analysis filters so that aliasing terms cancel when the bands are summed. Off-the-shelf Butterworth filters carry no such guarantee. Perfect reconstruction imposes joint constraints on the entire analysis-synthesis system."

- question: "In a critically-sampled K-band filter bank, each analysis output is downsampled by K. What is the total data rate across all K outputs relative to the original input?"
  type: multiple-choice
  options:
    - "K times higher — each band produces a separate stream at the original sample rate"
    - "The same as the input — K outputs at 1/K the sample rate each multiplies back to the original rate"
    - "K times lower — downsampling discards most of the signal"
    - "It depends on the passband width of each individual filter"
  answer: 1
  explanation: "Critical sampling is designed to preserve the total data rate. Each of K bands is downsampled by K (keeping every K-th sample), so its sample rate drops to f_s/K. Across K bands: K × (f_s/K) = f_s. The total rate equals the input rate, making critical sampling maximally efficient — no redundancy. The tradeoff is that the aliasing introduced by downsampling must be actively canceled by the synthesis stage."

- question: "A filter bank that achieves perfect reconstruction guarantees that the reconstructed output is exactly equal to the original input signal, with no distortion or aliasing error."
  type: true-false
  answer: true
  explanation: "Perfect reconstruction (PR) is precisely defined: ŷ[n] = x[n − d] for some fixed delay d. The output is identical to the input up to a constant time delay, with no amplitude distortion, phase distortion, or aliasing. Achieving PR requires the analysis and synthesis filter pairs to jointly satisfy specific mathematical constraints that cancel all aliasing introduced by downsampling."

- question: "Once the analysis filter bank has been designed, the synthesis filters can be chosen freely and independently to best match the reconstruction application."
  type: true-false
  answer: false
  explanation: "In a PR filter bank, the analysis and synthesis filter pairs are linked by tight mathematical constraints — you cannot design one without the other. The synthesis filters must be chosen so that aliasing components introduced during downsampling in the analysis stage cancel exactly when the sub-band outputs are recombined. Choosing synthesis filters independently will generally violate these constraints and produce aliasing artifacts in the reconstruction."

- question: "Why does critical sampling in a filter bank introduce aliasing, and how does perfect reconstruction address this?"
  type: short-answer
  answer: "Critical sampling downsamples each analysis output by K. Any energy outside the passband (from imperfect filter stopbands) folds back into the passband during downsampling — this is aliasing. Perfect reconstruction addresses this not by eliminating aliasing in each band separately, but by designing the analysis and synthesis filter pairs so that the aliasing terms from all K bands cancel exactly when the synthesis stage sums them together. The synthesis bank orchestrates a system-wide cancellation of aliasing, which requires the filter pairs to be designed jointly rather than independently."
  explanation: "This is the central design challenge of filter banks. Aliasing is unavoidable in critically-sampled systems, but it can be made to cancel. The QMF (quadrature mirror filter) solution for 2-band banks and the paraunitary framework for K-band banks both exploit this cancellation principle. The key insight is that aliasing cancellation is a property of the entire analysis-synthesis system, not of individual filters."
```

## Explainer

A single filter answers one question: how much of the signal lies above or below some cutoff frequency? A **filter bank** answers a richer question: how is the signal's energy distributed across many frequency bands simultaneously? From your work with Butterworth and Chebyshev filters, you know how to design individual lowpass and highpass filters with specified magnitude responses. A filter bank arranges multiple such filters in parallel, each covering a different portion of the spectrum, to decompose the signal into a frequency-indexed set of sub-signals. This is the mathematical foundation of equalizers, audio codecs, speech processors, and spectrum analyzers.

The two stages of a filter bank are named for their roles. The **analysis filter bank** takes a single input signal x[n] and produces K output streams x₀[n], x₁[n], ..., x_{K-1}[n], one per frequency band. Each output carries only the content of its assigned band — the low-frequency band, a mid-frequency band, a high-frequency band, and so on. After analysis, each band can be processed independently: compressed, encoded, transmitted, modified for equalization, or analyzed for spectral content. The **synthesis filter bank** takes the K (possibly modified) streams and recombines them into a reconstructed output ŷ[n]. Analysis is the measurement; synthesis is the reconstruction.

In a **critically-sampled** filter bank, each analysis output is downsampled by K — keeping only every K-th sample. Since each band occupies a bandwidth of approximately f_s/(2K), the Nyquist criterion allows this downsampling without aliasing (each sub-band has been spectrally limited by its filter). The result is that the total data rate across all K outputs equals the input data rate: K outputs × (1/K) sample rate = original rate. This critical sampling is efficient but creates a complication: the downsampling introduces aliasing within each sub-band, folding residual out-of-band energy back into the passband. Practical filter banks must either use oversampling (more outputs than the minimum, with redundancy) or design the filters specifically to cancel this aliasing.

**Perfect reconstruction (PR)** means that the synthesis bank exactly recovers the original signal: ŷ[n] = x[n − d] for some delay d, with no added distortion or aliasing error. This requires the analysis and synthesis filter pairs to satisfy precise mathematical constraints so that the aliasing terms introduced by downsampling in analysis are exactly canceled by the synthesis stage. The constraints link the design of all K filter pairs together — you cannot design one band's filter independently of the others. The quadrature mirror filter (QMF) is the classic 2-band PR solution; the more general solution leads to **paraunitary filter banks** where the analysis and synthesis filter matrices are inverses of each other.

The real-world applications reveal the design tradeoffs clearly. MP3 audio encoding splits audio into 32 equal-width frequency bands using a modified discrete cosine transform (a close relative of a filter bank), then quantizes each band — allocating more bits to bands where the ear is sensitive, fewer to masked bands. The synthesis bank reconstructs audio from quantized (lossy) coefficients, so perfect reconstruction is not achieved, but the quantization noise is shaped to be perceptually inaudible. Wavelet transforms form a special case of PR filter banks with octave-spaced bands: each successive decomposition level halves the bandwidth and doubles the time resolution of the coarser approximation. The unifying principle across all these applications is the same: decompose into bands, process independently, reconstruct — with the filter design determining both the quality of the frequency separation and the fidelity of reconstruction.
