---
id: wavelet-transform-analysis
title: Wavelet Transform and Multiresolution Analysis
domain: engineering
course: signals-and-systems
prerequisites:
- id: short-time-fourier-transform
  type: hard
- id: fourier-series-representation
  type: soft
tags:
- wavelets
- multiresolution
- time-frequency
- decomposition
stage: expert
status: draft
---

# Wavelet Transform and Multiresolution Analysis

## Core Idea
Wavelets are localized oscillatory functions that analyze signals at multiple scales. Continuous wavelet transform (CWT) correlates signal with dilated and translated wavelets, providing time-scale representation. Discrete wavelet transform (DWT) uses dyadic scales and orthonormal wavelets for efficient, non-redundant decomposition into approximation and detail components.

## Questions

```yaml
- question: "An audio signal contains both a 1 ms mechanical click and a 3 Hz structural vibration. An analyst uses STFT with a fixed window. What fundamental problem arises, and how do wavelets address it?"
  type: multiple-choice
  options:
    - "STFT handles both equally well; wavelets offer no advantage for mixed-frequency signals"
    - "STFT forces a single window size, so the analyst must choose between time resolution (good for the click) and frequency resolution (good for the vibration) — wavelets adaptively scale, using short durations for the high-frequency click and long durations for the slow vibration"
    - "Wavelets cannot resolve low-frequency content below 10 Hz, so STFT is required for the vibration component"
    - "STFT provides better time localization than wavelets for transient events like the click"
  answer: 1
  explanation: "This is the fundamental limitation that wavelets solve. STFT applies a fixed window everywhere — short windows give good time resolution but smear frequency content, long windows give good frequency resolution but blur events in time. You cannot have both at once. Wavelets abandon the fixed window: a compressed mother wavelet captures the click with fine time resolution, while a stretched copy of the same wavelet resolves the slow vibration with fine frequency resolution. This automatic adaptation — short time/coarse frequency at high frequencies, long time/fine frequency at low frequencies — matches the natural structure of many real signals."

- question: "In the discrete wavelet transform, highpass filtering produces 'detail coefficients' and lowpass filtering produces 'approximation coefficients.' What do these represent?"
  type: multiple-choice
  options:
    - "Detail coefficients capture slow background variations; approximation coefficients capture rapid transient features"
    - "Detail coefficients capture fast variation (high-frequency content) from the highpass filter; approximation coefficients capture slow variation (low-frequency content) from the lowpass filter"
    - "Both capture the same information; the distinction is only about computational efficiency"
    - "Approximation coefficients are redundant and are discarded once detail coefficients are computed at all levels"
  answer: 1
  explanation: "The names are intuitive: the approximation is the coarse, smooth version of the signal, while the details are the fine-scale variations that distinguish the approximation from the original. The lowpass filter passes low-frequency content → approximation coefficients. The highpass filter passes high-frequency content → detail coefficients. At each DWT level, the approximation is recursively decomposed into a coarser approximation and another layer of details, building up the multi-resolution structure. The detail coefficients at each level capture features at a specific scale, and together with the final approximation they provide a complete reconstruction of the original signal."

- question: "The Fourier transform provides better time-frequency localization than the wavelet transform for analyzing non-stationary signals."
  type: true-false
  answer: false
  explanation: "The Fourier transform provides no time localization at all — it tells you which frequencies are present in the entire signal but cannot tell you when they occur. Wavelets are specifically designed to provide time-frequency localization: by correlating the signal with scaled and shifted copies of a localized mother wavelet, the CWT locates both when and at what frequency events occur. For non-stationary signals (where frequency content changes over time), wavelets are strictly superior to Fourier methods in this regard. The Fourier transform is best for stationary signals where time-localization is unnecessary."

- question: "A compressed (scaled-down) wavelet has a higher oscillation frequency and provides finer time resolution than a stretched version of the same mother wavelet."
  type: true-false
  answer: true
  explanation: "Scaling is the core mechanism of wavelets. When a mother wavelet ψ is compressed (small scale parameter), it oscillates faster — its temporal support is narrow, giving fine time resolution but spanning a broader frequency band. When stretched (large scale parameter), it oscillates slowly — its temporal support is wide, giving fine frequency resolution but poor time localization. This trade-off is not a fixed limitation (as in STFT) but an adaptive feature: the wavelet transform evaluates the signal at every scale, so both high-frequency events (captured by compressed wavelets) and low-frequency structure (captured by stretched wavelets) are analyzed optimally."

- question: "Explain why wavelets are particularly well-suited for signal compression compared to the STFT or standard Fourier transform."
  type: short-answer
  answer: "Wavelets concentrate signal energy into a small number of large coefficients by exploiting the structure of most real signals: smooth regions produce small detail coefficients, while sharp features and discontinuities produce large detail coefficients localized in time. Compression works by thresholding small coefficients to zero — removing them causes little reconstruction error. The DWT also produces a non-redundant decomposition (exactly as many coefficients as input samples), making storage efficient. In contrast, the Fourier transform spreads energy of localized features (like discontinuities) across many coefficients, and the STFT is redundant and uses a fixed resolution that may not match the signal's structure. Wavelets match resolution to signal content, which is why JPEG 2000 and audio codecs use them."
  explanation: "The key is sparsity: compression works best when most coefficients are near zero. Wavelets achieve sparsity for natural signals because most of the content is in smooth regions (few detail coefficients needed) with a few sharp transitions (localized large coefficients). The Fourier transform's coefficients are not sparse for signals with discontinuities — a single edge requires many sinusoids to represent, spreading energy widely."
```

## Explainer

The Fourier transform tells you *which* frequencies are present in a signal, but not *when* they occur. The Short-Time Fourier Transform you already know fixes this by chopping the signal into windowed segments and taking a Fourier transform of each. But STFT has a fundamental limitation: you choose one fixed window width and live with the resulting tradeoff — short windows give good time resolution but smear frequency information, while long windows resolve frequency well but blur events in time. You cannot have both at once, at any scale.

**Wavelets** escape this tradeoff by abandoning the fixed window entirely. A **mother wavelet** ψ is a short, localized oscillatory pulse with zero mean — not an infinite sinusoid. The **continuous wavelet transform (CWT)** computes the inner product of the signal with scaled and shifted copies of ψ. **Scaling** stretches or compresses the wavelet in time: a compressed wavelet oscillates faster and captures high-frequency content with fine time resolution; a stretched wavelet oscillates slowly and captures low-frequency content with fine frequency resolution. This adaptive behavior — fine time resolution at high frequencies, fine frequency resolution at low frequencies — matches the natural structure of many physical signals (a brief mechanical impact needs time resolution; a slow structural resonance needs frequency resolution).

The **discrete wavelet transform (DWT)** restricts scales to a dyadic grid (2^j for integer j) and uses orthonormal wavelet families such as Haar or Daubechies wavelets. The DWT is implemented as a cascade of highpass and lowpass **filter banks**. At each level, the signal passes through a highpass filter (producing **detail coefficients** capturing fast variation) and a lowpass filter (producing **approximation coefficients** capturing slow variation), each followed by downsampling by 2. The approximation output is then fed back into the same filter pair for the next level. This recursion produces a multi-level decomposition: detail coefficients at level j capture features at scale 2^j, and the final approximation captures the coarsest structure.

**Multiresolution analysis** (MRA) is the mathematical framework that makes this precise. The signal lives in a Hilbert space that decomposes as a nested sequence of approximation subspaces V_j ⊂ V_{j-1} ⊂ … ⊂ L²(ℝ). Each V_j is generated by scaled versions of a **scaling function** φ. The orthogonal complement of V_j inside V_{j-1} is the **detail subspace** W_j, generated by the wavelet ψ at scale 2^j. The DWT is the orthogonal projection of the signal onto each W_j plus the coarsest V_j — a complete, non-redundant decomposition. Unlike the CWT, which is highly redundant, the DWT stores exactly as many coefficients as the original signal, making it ideal for compression and denoising applications.

The practical power of wavelets is that smooth regions of a signal produce small detail coefficients (few coefficients needed), while discontinuities and sharp features produce large detail coefficients localized in time. Compression works by thresholding small coefficients to zero; denoising works by thresholding coefficients below a noise level. JPEG 2000 and many audio codecs use wavelet decomposition precisely because it concentrates signal energy into a small number of large coefficients, leaving most coefficients near zero and highly compressible.
