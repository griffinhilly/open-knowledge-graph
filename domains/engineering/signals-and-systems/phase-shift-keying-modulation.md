---
id: phase-shift-keying-modulation
title: Phase Shift Keying Modulation
domain: engineering
course: signals-and-systems
prerequisites:
- id: quadrature-modulation-iq-representation
  type: hard
tags:
- psk
- bpsk
- qpsk
- modulation
- communication
stage: advanced
status: draft
---

# Phase Shift Keying Modulation

## Core Idea
Phase Shift Keying (PSK) encodes information in carrier phase: s(t) = A·cos(ωct + φ[n]) for symbol n. BPSK uses two phases (0, π), QPSK uses four phases at π/4, 3π/4, 5π/4, 7π/4, and M-ary PSK extends to M phases. Demodulation uses phase-locked loops or matched filters matched to each constellation point.

## Questions

```yaml
- question: "An engineer switches a communication link from BPSK to QPSK while keeping the same symbol rate and carrier power. What changes?"
  type: multiple-choice
  options:
    - "Spectral efficiency doubles — 2 bits per symbol instead of 1 — with no change in required bandwidth"
    - "Bit error rate improves, because more phase states provide better noise immunity"
    - "Required bandwidth doubles to accommodate the additional phase states"
    - "Carrier power per symbol must increase to maintain adequate phase separation"
  answer: 0
  explanation: "QPSK encodes 2 bits per symbol versus BPSK's 1 bit, but uses the same bandwidth (bandwidth depends on symbol rate, not modulation order). Spectral efficiency therefore doubles. Option 1 (BER improves) is the opposite of the truth: QPSK's four constellation points are closer together than BPSK's two, so it is more susceptible to noise for the same carrier power per symbol. Option 2 (bandwidth doubles) confuses bandwidth with constellation complexity — bandwidth is set by the symbol rate, which hasn't changed."

- question: "A BPSK receiver loses lock on carrier phase. What is the consequence for demodulation?"
  type: multiple-choice
  options:
    - "Demodulation fails — coherent PSK detection requires a phase reference to determine which constellation point the received signal is closest to"
    - "The receiver automatically switches to envelope (noncoherent) detection, recovering bits with higher error rate"
    - "Error rate doubles, but roughly 50% of bits are still correctly recovered by chance"
    - "Demodulation is unaffected because BPSK is inherently phase-insensitive"
  answer: 0
  explanation: "PSK encodes information entirely in phase. Coherent demodulation works by measuring the phase of the received signal relative to a reference and assigning it to the nearest constellation point. Without carrier phase recovery, the 'nearest point' comparison has no reference — the decision boundary is undefined. Option 3 (50% correct) is plausible but wrong: with no phase reference, symbol decisions are essentially random. This is precisely why carrier phase recovery (via a PLL or other scheme) is described as the central practical challenge of PSK systems."

- question: "In QPSK, Gray coding is used so that adjacent constellation points differ by exactly two bits, limiting burst errors when noise causes misdetection."
  type: true-false
  answer: false
  explanation: "Gray coding ensures adjacent constellation points differ by exactly ONE bit — not two. The purpose is exactly as stated (limiting error severity), but the mechanism is one-bit differences. When noise causes a detection error (misidentifying a QPSK point as a neighbor), Gray coding ensures only a single bit error results rather than two. With natural binary mapping, diagonal neighbors could differ by two bits, doubling the bit error cost of certain detection errors."

- question: "As M increases in M-ary PSK, each doubling of M adds one more bit per symbol transmitted but requires higher SNR to maintain the same bit error rate."
  type: true-false
  answer: true
  explanation: "With M phases equally spaced on a circle, adding more phases (doubling M) increases bits per symbol by 1 but shrinks the angular distance between adjacent points. Smaller angular separation means a smaller noise margin — the receiver must more precisely measure phase to distinguish neighbors. Each additional bit per symbol costs approximately 6 dB of required SNR in M-ary PSK, which is why practical systems switch to QAM rather than continuing to increase M."

- question: "Why do engineers switch from M-ary PSK to QAM for high spectral efficiency rather than simply increasing M indefinitely in PSK?"
  type: short-answer
  answer: "In M-ary PSK, all constellation points lie on a circle of fixed radius — they can only be spread angularly, so as M increases, points crowd together and angular separation shrinks rapidly. QAM uses both phase AND amplitude variation, placing points across a 2D grid. For the same average power and number of constellation points, QAM achieves larger minimum distances between points than PSK, yielding better noise immunity at the same spectral efficiency. Beyond 8-PSK, QAM constellations (16-QAM, 64-QAM) outperform M-PSK at the same spectral efficiency, making higher M-ary PSK impractical."
  explanation: "The geometric insight is key: PSK constrains points to a 1D manifold (a circle), while QAM uses the full 2D plane. This allows QAM to pack more points at larger minimum distances for the same average power. Modern high-throughput systems (Wi-Fi, 5G) use 256-QAM or 1024-QAM rather than M-ary PSK precisely for this reason."
```

## Explainer

From quadrature modulation and IQ representation, you know that any bandpass signal can be described by its in-phase (I) and quadrature (Q) components — effectively a 2D coordinate in the **IQ plane**. You also know that multiplying a baseband signal by cos(ω_c t) shifts it to carrier frequency ω_c without altering its information content. Phase Shift Keying builds directly on this: instead of varying amplitude (as in ASK) or frequency (as in FSK), PSK encodes information by varying the phase angle of the carrier for each transmitted symbol.

In **BPSK** (Binary PSK), there are only two possible phases: 0 and π (i.e., 0° and 180°). A bit value of 0 sends A·cos(ω_c t); a bit value of 1 sends A·cos(ω_c t + π) = −A·cos(ω_c t). In the IQ plane, these two constellation points sit at (+A, 0) and (−A, 0) — they are diametrically opposite on the I-axis. The receiver decides which symbol was sent by determining which constellation point the received signal is closest to (a **minimum distance decision**). BPSK transmits 1 bit per symbol and has the largest possible separation between points for a given amplitude, making it the most noise-resistant PSK scheme.

**QPSK** (Quadrature PSK) uses four phases: π/4, 3π/4, 5π/4, and 7π/4. In the IQ plane, these four constellation points sit at the corners of a square — two bits are encoded per symbol, doubling the spectral efficiency without increasing the required bandwidth. The two bits (b₀, b₁) select one of the four phases via **Gray coding**: adjacent constellation points differ by only one bit, so a detection error (misidentifying a point as a neighbor) typically causes only a single-bit error rather than two, improving practical bit error rate. QPSK achieves 2 bits per symbol with the same bandwidth as BPSK — a factor-of-two efficiency gain.

**M-ary PSK** generalizes to M equally-spaced phases, transmitting log₂(M) bits per symbol. Each additional doubling of M (8-PSK, 16-PSK, ...) adds one more bit per symbol but shrinks the angular distance between constellation points, requiring higher SNR to maintain the same error rate. Beyond 8-PSK, engineers typically switch to **QAM** (Quadrature Amplitude Modulation), which uses both phase and amplitude variation to spread constellation points more efficiently in 2D space. Demodulation of PSK requires accurate **carrier phase recovery** (typically via a phase-locked loop) because the receiver must know the reference phase to make correct decisions — this is the central practical challenge of PSK systems and the reason coherent demodulation is essential.

