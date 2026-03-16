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
stage: advanced
status: draft
---

# Frequency Shift Keying Modulation

## Core Idea
FSK encodes binary information by switching carrier frequency between two values f1 and f0. Orthogonality between tones enables coherent demodulation using matched filters. Gaussian FSK (GFSK) smooths frequency transitions to reduce spectral width. Demodulation uses FM discriminators or frequency-selective matched filters.

## Explainer

From amplitude and frequency shift keying fundamentals, you know that modulation maps digital bit values onto physical waveform parameters. **Frequency Shift Keying (FSK)** takes the simplest possible approach: assign each binary symbol its own carrier frequency. A "1" is transmitted as a sinusoidal burst at frequency f₁; a "0" as a burst at frequency f₀. The receiver's job is to determine which frequency is present in each symbol interval. This is conceptually close to two separate narrowband radio stations — the transmitter broadcasts on one channel or the other depending on the data.

The key design parameter is the frequency separation Δf = f₁ − f₀. Make it too small and the two tones are hard to distinguish, increasing error probability. Make it too large and the signal occupies unnecessary bandwidth. The optimal choice leverages **orthogonality**: two sinusoids are orthogonal over a symbol period T if their inner product (integral of product over T) is zero. For FSK, this occurs when Δf = n/(2T) for integer n. When the tones are orthogonal, a correlator (or **matched filter**) tuned to f₁ produces zero output when f₀ is transmitted, and vice versa — perfect separation with no inter-symbol interference from frequency overlap. The minimum orthogonality condition (n = 1, Δf = 1/2T) defines **Minimum Shift Keying (MSK)**, which has the narrowest bandwidth while preserving coherent demodulability.

A practical problem with binary FSK is its spectral efficiency: the signal's spectrum contains sidebands from the abrupt frequency transitions at symbol boundaries, and these extend broadly. **Gaussian FSK (GFSK)** addresses this by pre-filtering the digital bit stream with a Gaussian pulse-shaping filter before using it to frequency-modulate the carrier. The Gaussian filter smooths the sharp transitions, so instead of a rectangular frequency pulse causing sharp spectral sidebands, the frequency sweeps smoothly between f₀ and f₁. The trade-off is mild inter-symbol interference (adjacent symbols' smooth tails overlap slightly), but the occupied bandwidth reduction is dramatic. Bluetooth Classic uses GFSK with a bandwidth-time product BT = 0.5 precisely because it achieves sufficient spectral containment in the 2.4 GHz ISM band without requiring complex equalization.

Demodulation of FSK can be coherent or non-coherent. **Coherent demodulation** uses matched filters or correlators synchronized to the exact phase of each carrier frequency — it extracts maximum signal energy per bit but requires carrier phase recovery. **Non-coherent demodulation** uses envelope detection: bandpass filters centered at f₁ and f₀ pass the respective tones, envelope detectors measure the energy in each filter, and the symbol decision follows from whichever energy is larger. Non-coherent detection is simpler to implement and tolerates phase noise, at a cost of roughly 3 dB in required SNR compared to coherent detection. In practice, non-coherent FSK is common in low-cost, low-complexity implementations like RFID and simple sensor radio links where battery life and hardware simplicity matter more than spectral efficiency.
