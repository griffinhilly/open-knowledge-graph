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

## Explainer

From quadrature modulation and IQ representation, you know that any bandpass signal can be described by its in-phase (I) and quadrature (Q) components — effectively a 2D coordinate in the **IQ plane**. You also know that multiplying a baseband signal by cos(ω_c t) shifts it to carrier frequency ω_c without altering its information content. Phase Shift Keying builds directly on this: instead of varying amplitude (as in ASK) or frequency (as in FSK), PSK encodes information by varying the phase angle of the carrier for each transmitted symbol.

In **BPSK** (Binary PSK), there are only two possible phases: 0 and π (i.e., 0° and 180°). A bit value of 0 sends A·cos(ω_c t); a bit value of 1 sends A·cos(ω_c t + π) = −A·cos(ω_c t). In the IQ plane, these two constellation points sit at (+A, 0) and (−A, 0) — they are diametrically opposite on the I-axis. The receiver decides which symbol was sent by determining which constellation point the received signal is closest to (a **minimum distance decision**). BPSK transmits 1 bit per symbol and has the largest possible separation between points for a given amplitude, making it the most noise-resistant PSK scheme.

**QPSK** (Quadrature PSK) uses four phases: π/4, 3π/4, 5π/4, and 7π/4. In the IQ plane, these four constellation points sit at the corners of a square — two bits are encoded per symbol, doubling the spectral efficiency without increasing the required bandwidth. The two bits (b₀, b₁) select one of the four phases via **Gray coding**: adjacent constellation points differ by only one bit, so a detection error (misidentifying a point as a neighbor) typically causes only a single-bit error rather than two, improving practical bit error rate. QPSK achieves 2 bits per symbol with the same bandwidth as BPSK — a factor-of-two efficiency gain.

**M-ary PSK** generalizes to M equally-spaced phases, transmitting log₂(M) bits per symbol. Each additional doubling of M (8-PSK, 16-PSK, ...) adds one more bit per symbol but shrinks the angular distance between constellation points, requiring higher SNR to maintain the same error rate. Beyond 8-PSK, engineers typically switch to **QAM** (Quadrature Amplitude Modulation), which uses both phase and amplitude variation to spread constellation points more efficiently in 2D space. Demodulation of PSK requires accurate **carrier phase recovery** (typically via a phase-locked loop) because the receiver must know the reference phase to make correct decisions — this is the central practical challenge of PSK systems and the reason coherent demodulation is essential.

