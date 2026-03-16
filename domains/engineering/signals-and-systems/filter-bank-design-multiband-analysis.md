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
stage: formal-systems
status: draft
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

## Explainer

A single filter answers one question: how much of the signal lies above or below some cutoff frequency? A **filter bank** answers a richer question: how is the signal's energy distributed across many frequency bands simultaneously? From your work with Butterworth and Chebyshev filters, you know how to design individual lowpass and highpass filters with specified magnitude responses. A filter bank arranges multiple such filters in parallel, each covering a different portion of the spectrum, to decompose the signal into a frequency-indexed set of sub-signals. This is the mathematical foundation of equalizers, audio codecs, speech processors, and spectrum analyzers.

The two stages of a filter bank are named for their roles. The **analysis filter bank** takes a single input signal x[n] and produces K output streams x₀[n], x₁[n], ..., x_{K-1}[n], one per frequency band. Each output carries only the content of its assigned band — the low-frequency band, a mid-frequency band, a high-frequency band, and so on. After analysis, each band can be processed independently: compressed, encoded, transmitted, modified for equalization, or analyzed for spectral content. The **synthesis filter bank** takes the K (possibly modified) streams and recombines them into a reconstructed output ŷ[n]. Analysis is the measurement; synthesis is the reconstruction.

In a **critically-sampled** filter bank, each analysis output is downsampled by K — keeping only every K-th sample. Since each band occupies a bandwidth of approximately f_s/(2K), the Nyquist criterion allows this downsampling without aliasing (each sub-band has been spectrally limited by its filter). The result is that the total data rate across all K outputs equals the input data rate: K outputs × (1/K) sample rate = original rate. This critical sampling is efficient but creates a complication: the downsampling introduces aliasing within each sub-band, folding residual out-of-band energy back into the passband. Practical filter banks must either use oversampling (more outputs than the minimum, with redundancy) or design the filters specifically to cancel this aliasing.

**Perfect reconstruction (PR)** means that the synthesis bank exactly recovers the original signal: ŷ[n] = x[n − d] for some delay d, with no added distortion or aliasing error. This requires the analysis and synthesis filter pairs to satisfy precise mathematical constraints so that the aliasing terms introduced by downsampling in analysis are exactly canceled by the synthesis stage. The constraints link the design of all K filter pairs together — you cannot design one band's filter independently of the others. The quadrature mirror filter (QMF) is the classic 2-band PR solution; the more general solution leads to **paraunitary filter banks** where the analysis and synthesis filter matrices are inverses of each other.

The real-world applications reveal the design tradeoffs clearly. MP3 audio encoding splits audio into 32 equal-width frequency bands using a modified discrete cosine transform (a close relative of a filter bank), then quantizes each band — allocating more bits to bands where the ear is sensitive, fewer to masked bands. The synthesis bank reconstructs audio from quantized (lossy) coefficients, so perfect reconstruction is not achieved, but the quantization noise is shaped to be perceptually inaudible. Wavelet transforms form a special case of PR filter banks with octave-spaced bands: each successive decomposition level halves the bandwidth and doubles the time resolution of the coarser approximation. The unifying principle across all these applications is the same: decompose into bands, process independently, reconstruct — with the filter design determining both the quality of the frequency separation and the fidelity of reconstruction.
