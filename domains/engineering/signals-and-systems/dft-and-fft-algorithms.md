---
id: dft-and-fft-algorithms
title: Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT) Algorithms
domain: engineering
course: signals-and-systems
prerequisites:
- id: discrete-time-fourier-transform
  type: hard
- id: complex-numbers-intro
  type: hard
- id: fourier-transform-definition-properties
  type: soft
builds-toward:
- digital-signal-processing-fundamentals
tags:
- dft
- fft
- algorithms
- computational
stage: advanced
status: draft
---

# Discrete Fourier Transform (DFT) and Fast Fourier Transform (FFT) Algorithms

## Core Idea
The DFT X[k] = Σ x[n]e^(-j2πkn/N) computes the frequency content of a finite-length sequence, with O(N²) operations. The FFT (Cooley-Tukey algorithm) reduces this to O(N log N), making real-time spectral analysis practical. FFT is the foundation of digital signal processing.

## Explainer

From the discrete-time Fourier transform (DTFT), you know how to represent a sequence's frequency content — but the DTFT result X(e^jω) is a continuous, periodic function of frequency that you cannot store or compute exactly on a computer. The **DFT** solves this by sampling the DTFT at exactly N equally-spaced frequency points: ωₖ = 2πk/N for k = 0, 1, …, N−1. The result is N complex numbers X[0] through X[N−1] that completely represent the N-point input sequence x[0] through x[N−1]. Crucially, the DFT is invertible — you can recover x[n] exactly from X[k] using the inverse DFT. Nothing is lost; it is simply a change of basis.

The formula X[k] = Σₙ x[n] · e^(−j2πkn/N) says that each output X[k] is an inner product between the input sequence and a complex sinusoid at frequency k/N cycles per sample. From complex numbers, you know that e^(jθ) is a unit-magnitude complex number at angle θ — a point on the unit circle. The quantity W = e^(−j2π/N) is the fundamental **twiddle factor**: a rotation by 2π/N radians clockwise. The powers W^(kn) are N evenly-spaced points on the unit circle, and computing X[k] is equivalent to asking: how well does the input sequence correlate with each of these rotating complex exponentials? Large |X[k]| means the input contains a strong component at frequency k/N.

The computational problem with this approach is cost. Computing all N outputs requires, naively, N multiplications for each of the N outputs — N² complex multiplications total. For N = 1024, that is about one million operations. For N = 65536 (typical in audio processing), it is over four billion. The **Fast Fourier Transform** (FFT), specifically the Cooley-Tukey algorithm, reduces this to O(N log₂ N) by exploiting the algebraic structure of the twiddle factors. The key insight: W^(kn) is periodic with period N in both k and n, so many of the N² multiplications produce identical twiddle factors and their contributions can be combined rather than recomputed. The algorithm recursively splits the N-point DFT into two N/2-point DFTs (one for even-indexed inputs, one for odd-indexed inputs), each of which splits further, until the base case of 1-point DFTs (trivially equal to the input itself). After log₂(N) levels of splitting, the results are combined bottom-up using small **butterfly** operations. For N = 65536, this reduces four billion operations to about one million — a 4000× speedup.

Interpreting DFT output correctly requires knowing what each index k means. X[0] is the **DC component** — the average of the entire sequence. X[1] corresponds to exactly one complete cycle across the N samples (the fundamental frequency). X[k] at k = N/2 is the **Nyquist frequency** — the highest resolvable frequency, equal to half the sampling rate. For a real-valued input signal (which most physical signals are), the spectrum is **conjugate symmetric**: X[N−k] = X[k]*, meaning the second half of the DFT output mirrors the first half. Only the first N/2 values carry unique frequency information. When you see a spectrum plotted showing only the positive frequencies, this symmetry is why: the negative-frequency half is redundant for real signals and is typically discarded or folded.
