---
id: modulation-amplitude-frequency-shift-keying
title: 'Modulation: Amplitude, Frequency, and Phase Shift Keying'
domain: engineering
course: signals-and-systems
prerequisites:
- id: frequency-response-magnitude-phase
  type: hard
tags:
- modulation
- communications
- signal-transmission
stage: advanced
status: draft
---

# Modulation: Amplitude, Frequency, and Phase Shift Keying

## Core Idea
Modulation embeds information into a carrier signal by varying its amplitude (AM, ASK), frequency (FM, FSK), or phase (PM, PSK). Modulation shifts signal spectra to higher frequencies for efficient transmission, and demodulation recovers the original baseband signal. These techniques are fundamental to radio, cellular, and digital communications.

## Explainer

From your study of frequency response, you know that signals have energy distributed across different frequencies, and that systems respond differently to different frequencies. **Modulation** exploits this directly: it takes a **baseband** signal (the information, centered near zero frequency) and shifts its spectrum up to a higher-frequency band centered on a **carrier frequency** f_c. The reason is practical — baseband audio at 100 Hz would require an antenna hundreds of kilometers long to radiate efficiently, but shifting it to 100 MHz requires an antenna about 1.5 meters long. More importantly, modulation allows multiple signals to coexist on the same medium without interfering by assigning each a different carrier frequency (frequency division multiplexing).

**Amplitude Shift Keying (ASK)** is the simplest digital modulation: the carrier is multiplied by a digital symbol that takes discrete amplitude values. In the binary case, the carrier is either present (1) or absent (0) — this is called on-off keying (OOK). In the frequency domain, this multiplication convolves the symbol spectrum with the carrier impulse, shifting the baseband symbol spectrum to ±f_c. ASK is simple to implement but sensitive to amplitude noise (fading channels attenuate the signal, making it hard to distinguish symbol levels). **Frequency Shift Keying (FSK)** encodes bits by switching between two (or more) carrier frequencies: a '1' uses frequency f_1, a '0' uses f_2. The receiver detects which frequency is present. FSK is more robust to amplitude variations than ASK because information is in frequency, not amplitude — hence its use in early modems and frequency-hopping radios.

**Phase Shift Keying (PSK)** encodes information in the phase of the carrier. In **Binary PSK (BPSK)**, '1' is transmitted as cos(2πf_c t) and '0' as cos(2πf_c t + π) = −cos(2πf_c t). The receiver must detect a 180° phase difference. In **Quadrature PSK (QPSK)**, four phase values (0°, 90°, 180°, 270°) each encode two bits, doubling spectral efficiency without changing bandwidth. PSK is more efficient than FSK because it packs more information per unit bandwidth, and more robust than ASK because energy per symbol is constant (only phase changes). **Quadrature Amplitude Modulation (QAM)** combines amplitude and phase modulation — 16-QAM encodes 4 bits per symbol using 16 different amplitude-phase combinations — and is the basis for modern Wi-Fi and 4G/5G cellular.

Demodulation recovers the baseband signal by reversing the modulation. A **coherent detector** multiplies the received signal by a locally generated replica of the carrier and low-pass filters the result. For BPSK: r(t)·cos(2πf_c t) produces a DC term proportional to the transmitted bit, plus a double-frequency term that the filter removes. This requires the receiver to know f_c and its phase — **carrier synchronization** — which is a significant engineering challenge. A **non-coherent detector** avoids this by detecting energy (amplitude) rather than phase, at the cost of worse noise performance. The tradeoff between complexity and noise robustness — **bit error rate** as a function of signal-to-noise ratio — is the central design criterion for choosing a modulation scheme in any communication system.
