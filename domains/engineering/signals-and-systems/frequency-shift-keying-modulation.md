---
id: frequency-shift-keying-modulation
title: Frequency Shift Keying Modulation
domain: engineering
course: signals-and-systems
prerequisites:
- id: modulation-amplitude-frequency-shift-keying
  type: hard
tags:
- fsk
- modulation
- digital-modulation
- communication
stage: expert
status: validated
---

# Frequency Shift Keying Modulation

## Core Idea
FSK encodes binary information by switching carrier frequency between two values f1 and f0. Orthogonality between tones enables coherent demodulation using matched filters. Gaussian FSK (GFSK) smooths frequency transitions to reduce spectral width. Demodulation uses FM discriminators or frequency-selective matched filters.

## Questions

```yaml
- question: "A binary FSK system has symbol period T = 2 ms. What is the minimum frequency separation Δf that achieves tone orthogonality for coherent matched-filter demodulation?"
  type: multiple-choice
  options:
    - "Δf = 1/T = 500 Hz — one full cycle difference per symbol period"
    - "Δf = 1/(2T) = 250 Hz — minimum separation satisfying the orthogonality integral"
    - "Δf = 2/T = 1000 Hz — two cycles needed for reliable tone discrimination"
    - "Δf can be arbitrarily small if matched filters are designed with sufficient precision"
  answer: 1
  explanation: "Tone orthogonality requires ∫₀ᵀ cos(2πf₁t)cos(2πf₀t)dt = 0, which holds when Δf = n/(2T) for integer n. The minimum is n = 1, giving Δf = 1/(2T) = 250 Hz for T = 2 ms — this defines Minimum Shift Keying (MSK). Option A (1/T) achieves orthogonality but wastes bandwidth. Option D is wrong: orthogonality is a mathematical condition on Δf determined by the integral, not something achievable through filter design at arbitrary separation."

- question: "Bluetooth Classic uses GFSK with a bandwidth-time product BT = 0.5 instead of standard binary FSK. What tradeoff does this choice make?"
  type: multiple-choice
  options:
    - "It trades lower bit error rate for higher bandwidth — GFSK is less spectrally efficient but more reliable"
    - "It trades a small amount of inter-symbol interference for significantly reduced spectral bandwidth"
    - "It gains both lower bit error rate and lower bandwidth — GFSK is a strict improvement over standard FSK"
    - "It trades phase continuity for bandwidth — GFSK eliminates carrier phase discontinuities that standard FSK produces"
  answer: 1
  explanation: "The Gaussian pre-filter smooths frequency transitions between symbols, dramatically reducing spectral sidebands caused by abrupt rectangular transitions. The cost is mild inter-symbol interference: the smooth Gaussian tails of adjacent symbols overlap slightly. GFSK is not a strict improvement — standard FSK has zero ISI, while GFSK introduces a small ISI penalty. The tradeoff is worthwhile for Bluetooth because the congested 2.4 GHz ISM band demands spectral containment, and the ISI is manageable without complex equalization."

- question: "In binary FSK, when the two carrier tones are orthogonal over the symbol period, a matched filter tuned to frequency f₁ produces exactly zero output when frequency f₀ is transmitted."
  type: true-false
  answer: true
  explanation: "This is precisely the value of orthogonality in FSK. The matched filter for f₁ computes the inner product of the received signal with a reference sinusoid at f₁. When the transmitted signal is at f₀ and the tones are orthogonal (their inner product over T is zero), the matched filter output is exactly zero — no cross-talk. This is why orthogonality is the key design criterion: it enables perfect separation by matched filters in the absence of noise."

- question: "Non-coherent FSK demodulation is more reliable than coherent FSK demodulation because it avoids the carrier phase estimation errors that degrade coherent detection."
  type: true-false
  answer: false
  explanation: "Non-coherent detection is simpler but less reliable. Coherent detection uses the full phase information of the received signal, extracting maximum signal energy per bit. Non-coherent detection uses only amplitude (envelope detection), discarding phase information — this costs approximately 3 dB in required SNR for the same bit error rate. Non-coherent detection is chosen for implementation simplicity and phase noise tolerance, not for reliability. The statement reverses the tradeoff: coherent is more reliable; non-coherent is easier."

- question: "Explain why the orthogonality condition determines the minimum frequency separation in FSK, and what happens to demodulation performance when the tones are not orthogonal."
  type: short-answer
  answer: "Matched filter demodulation computes the inner product of the received signal with a reference tone. When f₁ and f₀ are orthogonal over the symbol period, the matched filter for f₁ produces a nonzero output only when f₁ was transmitted, and zero when f₀ was transmitted — clean discrimination with no cross-talk. When tones are not orthogonal, their inner product is nonzero, so the matched filter for f₁ produces a partial output even when f₀ is transmitted. This cross-talk adds to noise and reduces the effective SNR, increasing bit error rate. The minimum separation Δf = 1/(2T) achieves orthogonality with the smallest possible frequency gap, maximizing bandwidth efficiency while preserving clean detection."
  explanation: "Orthogonality gives the matched filter receiver exact zero rejection of the wrong tone — not just small, but exactly zero. Once orthogonality is violated, cross-talk scales with the overlap integral, which grows as Δf decreases below 1/(2T). This is a threshold condition: satisfy orthogonality and get clean detection regardless of filter quality; violate it and face a fundamental sensitivity penalty that no filter design can eliminate."
```

## Explainer

From amplitude and frequency shift keying fundamentals, you know that modulation maps digital bit values onto physical waveform parameters. **Frequency Shift Keying (FSK)** takes the simplest possible approach: assign each binary symbol its own carrier frequency. A "1" is transmitted as a sinusoidal burst at frequency f₁; a "0" as a burst at frequency f₀. The receiver's job is to determine which frequency is present in each symbol interval. This is conceptually close to two separate narrowband radio stations — the transmitter broadcasts on one channel or the other depending on the data.

The key design parameter is the frequency separation Δf = f₁ − f₀. Make it too small and the two tones are hard to distinguish, increasing error probability. Make it too large and the signal occupies unnecessary bandwidth. The optimal choice leverages **orthogonality**: two sinusoids are orthogonal over a symbol period T if their inner product (integral of product over T) is zero. For FSK, this occurs when Δf = n/(2T) for integer n. When the tones are orthogonal, a correlator (or **matched filter**) tuned to f₁ produces zero output when f₀ is transmitted, and vice versa — perfect separation with no inter-symbol interference from frequency overlap. The minimum orthogonality condition (n = 1, Δf = 1/2T) defines **Minimum Shift Keying (MSK)**, which has the narrowest bandwidth while preserving coherent demodulability.

A practical problem with binary FSK is its spectral efficiency: the signal's spectrum contains sidebands from the abrupt frequency transitions at symbol boundaries, and these extend broadly. **Gaussian FSK (GFSK)** addresses this by pre-filtering the digital bit stream with a Gaussian pulse-shaping filter before using it to frequency-modulate the carrier. The Gaussian filter smooths the sharp transitions, so instead of a rectangular frequency pulse causing sharp spectral sidebands, the frequency sweeps smoothly between f₀ and f₁. The trade-off is mild inter-symbol interference (adjacent symbols' smooth tails overlap slightly), but the occupied bandwidth reduction is dramatic. Bluetooth Classic uses GFSK with a bandwidth-time product BT = 0.5 precisely because it achieves sufficient spectral containment in the 2.4 GHz ISM band without requiring complex equalization.

Demodulation of FSK can be coherent or non-coherent. **Coherent demodulation** uses matched filters or correlators synchronized to the exact phase of each carrier frequency — it extracts maximum signal energy per bit but requires carrier phase recovery. **Non-coherent demodulation** uses envelope detection: bandpass filters centered at f₁ and f₀ pass the respective tones, envelope detectors measure the energy in each filter, and the symbol decision follows from whichever energy is larger. Non-coherent detection is simpler to implement and tolerates phase noise, at a cost of roughly 3 dB in required SNR compared to coherent detection. In practice, non-coherent FSK is common in low-cost, low-complexity implementations like RFID and simple sensor radio links where battery life and hardware simplicity matter more than spectral efficiency.
