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

## Questions

```yaml
- question: "A wireless sensor in an industrial environment is subject to amplitude fading — signal strength fluctuates unpredictably as it reflects off metal surfaces. An engineer must choose between ASK, FSK, and BPSK. Which scheme is LEAST suitable for this environment?"
  type: multiple-choice
  options:
    - "ASK, because amplitude fading directly corrupts the amplitude-encoded information"
    - "FSK, because frequency changes are distorted by amplitude fading"
    - "BPSK, because phase detection requires a very stable amplitude reference"
    - "All three are equally affected, since amplitude fading degrades signal energy regardless of modulation type"
  answer: 0
  explanation: "ASK (including on-off keying) encodes information in the amplitude of the carrier. When the channel introduces amplitude fading, the received signal amplitude no longer reliably reflects the transmitted symbol — a '1' may arrive looking like a '0'. FSK encodes information in frequency: fading changes signal strength but not which frequency is present, so the receiver can still detect the correct symbol. PSK encodes in phase, also robust to amplitude variations. Option D reflects the common misconception that fading affects all modulations equally — what matters is whether fading corrupts the information-bearing parameter, and only ASK has that vulnerability."

- question: "What are the two primary reasons for modulating a baseband signal onto a high-frequency carrier before wireless transmission?"
  type: multiple-choice
  options:
    - "To compress the signal and reduce file size; and to allow the receiver to filter noise more easily"
    - "To shift the signal spectrum to frequencies where antennas are physically practical; and to enable multiple signals to share the same medium via different carrier frequencies"
    - "To encrypt the data so the signal cannot be intercepted; and to reduce the bandwidth required"
    - "To increase the bit rate beyond what the baseband signal supports; and to eliminate the need for carrier synchronization"
  answer: 1
  explanation: "The two fundamental reasons are: (1) frequency shifting for practical antenna design — a 1 kHz audio signal has a 300 km wavelength requiring an impossible antenna, while 100 MHz has a ~1.5 m wavelength; and (2) frequency division multiplexing — different carrier frequencies allow many signals to coexist on the same medium without interfering. Options A, C, and D describe effects that are either wrong (modulation does not compress or encrypt) or not primary motivations for modulation."

- question: "In Binary Phase Shift Keying (BPSK), transmitting a '0' bit uses a carrier signal with zero amplitude."
  type: true-false
  answer: false
  explanation: "BPSK is a phase modulation scheme, not amplitude. Both '0' and '1' are transmitted at the same amplitude — what changes is the phase. A '1' is transmitted as cos(2πf_c t) (0° phase) and a '0' as cos(2πf_c t + π) = −cos(2πf_c t) (180° phase shift). The common confusion is with ASK on-off keying, where a '0' IS transmitted as zero amplitude. The distinction matters: BPSK's constant amplitude makes it far more robust to fading than ASK, which is why PSK is preferred in noise-prone environments."

- question: "Higher-order modulation schemes like 16-QAM transmit more bits per symbol than BPSK, making them more spectrally efficient but also more susceptible to noise and channel impairments."
  type: true-false
  answer: true
  explanation: "16-QAM encodes 4 bits per symbol using 16 amplitude-phase combinations; BPSK encodes 1 bit per symbol using 2 phase states. More bits per symbol means higher data rate in the same bandwidth — higher spectral efficiency. However, the 16 signal points must be packed more closely together in signal space, making them harder to distinguish when noise or channel distortion shifts a symbol. Higher-order modulation requires a higher signal-to-noise ratio to achieve the same bit error rate. This fundamental tradeoff drives the adaptive modulation schemes in modern 4G/5G systems."

- question: "Why does shifting a baseband signal to a higher carrier frequency enable more efficient wireless transmission, even though the information content is unchanged?"
  type: short-answer
  answer: "Antenna efficiency depends on wavelength — an antenna radiates most efficiently when its length is a significant fraction of the signal's wavelength. A 1 kHz audio signal has a 300 km wavelength, requiring a physically impossible antenna. Shifting that signal to 100 MHz (wavelength ~3 m) makes a practical ~1.5 m antenna feasible. Additionally, higher frequencies enable frequency division multiplexing: different transmitters use different carrier frequencies, allowing many signals to coexist on the same physical medium without interference. Baseband transmission cannot achieve this since all baseband signals occupy the same low-frequency region."
  explanation: "This is why modulation exists as a concept at all — baseband transmission of information is physically impractical for wireless channels. The information travels just as well at high frequency as low frequency, but the physical constraints of antennas and spectrum sharing are radically different. Every wireless communication system, from AM radio to 5G, exploits this principle."
```

## Explainer

From your study of frequency response, you know that signals have energy distributed across different frequencies, and that systems respond differently to different frequencies. **Modulation** exploits this directly: it takes a **baseband** signal (the information, centered near zero frequency) and shifts its spectrum up to a higher-frequency band centered on a **carrier frequency** f_c. The reason is practical — baseband audio at 100 Hz would require an antenna hundreds of kilometers long to radiate efficiently, but shifting it to 100 MHz requires an antenna about 1.5 meters long. More importantly, modulation allows multiple signals to coexist on the same medium without interfering by assigning each a different carrier frequency (frequency division multiplexing).

**Amplitude Shift Keying (ASK)** is the simplest digital modulation: the carrier is multiplied by a digital symbol that takes discrete amplitude values. In the binary case, the carrier is either present (1) or absent (0) — this is called on-off keying (OOK). In the frequency domain, this multiplication convolves the symbol spectrum with the carrier impulse, shifting the baseband symbol spectrum to ±f_c. ASK is simple to implement but sensitive to amplitude noise (fading channels attenuate the signal, making it hard to distinguish symbol levels). **Frequency Shift Keying (FSK)** encodes bits by switching between two (or more) carrier frequencies: a '1' uses frequency f_1, a '0' uses f_2. The receiver detects which frequency is present. FSK is more robust to amplitude variations than ASK because information is in frequency, not amplitude — hence its use in early modems and frequency-hopping radios.

**Phase Shift Keying (PSK)** encodes information in the phase of the carrier. In **Binary PSK (BPSK)**, '1' is transmitted as cos(2πf_c t) and '0' as cos(2πf_c t + π) = −cos(2πf_c t). The receiver must detect a 180° phase difference. In **Quadrature PSK (QPSK)**, four phase values (0°, 90°, 180°, 270°) each encode two bits, doubling spectral efficiency without changing bandwidth. PSK is more efficient than FSK because it packs more information per unit bandwidth, and more robust than ASK because energy per symbol is constant (only phase changes). **Quadrature Amplitude Modulation (QAM)** combines amplitude and phase modulation — 16-QAM encodes 4 bits per symbol using 16 different amplitude-phase combinations — and is the basis for modern Wi-Fi and 4G/5G cellular.

Demodulation recovers the baseband signal by reversing the modulation. A **coherent detector** multiplies the received signal by a locally generated replica of the carrier and low-pass filters the result. For BPSK: r(t)·cos(2πf_c t) produces a DC term proportional to the transmitted bit, plus a double-frequency term that the filter removes. This requires the receiver to know f_c and its phase — **carrier synchronization** — which is a significant engineering challenge. A **non-coherent detector** avoids this by detecting energy (amplitude) rather than phase, at the cost of worse noise performance. The tradeoff between complexity and noise robustness — **bit error rate** as a function of signal-to-noise ratio — is the central design criterion for choosing a modulation scheme in any communication system.
