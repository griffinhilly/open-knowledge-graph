---
id: quadrature-modulation-iq-representation
title: Quadrature Modulation and I/Q Representation
domain: engineering
course: signals-and-systems
prerequisites:
- id: modulation-amplitude-frequency-shift-keying
  type: hard
- id: hilbert-transform-analytic-signals
  type: soft
builds-toward:
- phase-shift-keying-modulation
tags:
- modulation
- iq-modulation
- quadrature
- communication
stage: advanced
status: draft
---

# Quadrature Modulation and I/Q Representation

## Core Idea
Quadrature modulation uses two carriers in phase quadrature (90° apart) to transmit two information streams: s(t) = I(t)·cos(ωct) – Q(t)·sin(ωct). Complex notation s_c(t) = (I + jQ)·e^(jωct) simplifies analysis where s_c is the complex envelope. Demodulation by correlating with local carriers recovers I and Q components, enabling bandwidth-efficient communication.

## Explainer

From your study of AM, FM, and shift-keying modulation, you know the basic idea: modulation is the process of imprinting information onto a high-frequency carrier so it can be transmitted over a channel. AM encodes information in the carrier's amplitude; FM in its frequency. Each of these uses a single real carrier and transmits one stream of information per channel. But a fundamental insight — partially anticipated by the analytic signal concept you encountered with the Hilbert transform — is that a sinusoidal carrier actually has two degrees of freedom available simultaneously: its amplitude and its phase. **Quadrature modulation** exploits both degrees of freedom at once, doubling the information density without using any additional bandwidth.

The core idea is that two sinusoids at the same frequency but 90° apart in phase are **orthogonal**: their product integrated over a complete cycle is exactly zero. This means they can coexist on the same carrier without interfering with each other. The transmitted signal is s(t) = I(t)·cos(ωct) − Q(t)·sin(ωct), where I(t) is the **in-phase** component (the baseband signal multiplied onto the cosine carrier) and Q(t) is the **quadrature** component (multiplied onto the sine carrier, which lags the cosine by 90°). To recover I(t) at the receiver, you multiply s(t) by 2cos(ωct) and lowpass filter — the cosine×cosine term gives I(t) while the cosine×sine term (the Q contribution) integrates to zero. Symmetrically, multiplying by −2sin(ωct) recovers Q(t). The orthogonality of sine and cosine is what makes this separation perfect.

The **complex envelope** notation unifies this. Define the complex baseband signal as ẑ(t) = I(t) + jQ(t). The transmitted passband signal is s(t) = Re[ẑ(t)·e^(jωct)]. This is exactly the analytic signal framework from your Hilbert transform study: ẑ(t) is the **complex envelope**, and the passband signal is its real part modulated onto the carrier. The magnitude |ẑ(t)| = √(I² + Q²) is the instantaneous amplitude; the angle ∠ẑ(t) = arctan(Q/I) is the instantaneous phase. AM is ẑ(t) = A(t) with constant phase; PM is ẑ(t) = e^(jφ(t)) with constant magnitude; QAM and PSK are ẑ(t) choosing from a **constellation** — a discrete set of complex points in the I-Q plane. Plotting I vs Q gives the **constellation diagram**, where different modulation orders (QPSK, 16-QAM, 64-QAM) appear as grids of points at different distances and angles from the origin.

The practical power of I/Q representation is that all signal processing — pulse shaping, equalization, matched filtering, carrier recovery — can be done entirely in the complex baseband domain at low frequency, without ever working at the RF carrier frequency. The hardware architecture separates naturally: a **quadrature modulator** chip takes digital I and Q samples, converts them to analog, and multiplies by cosine and sine carriers (with a 90° phase shift between them), summing the result for transmission. The receiver uses a **quadrature demodulator** to split the incoming RF signal into I and Q paths and downconvert each to baseband. All the intelligence — OFDM, MIMO, adaptive equalization — operates on the I/Q streams. This is why every modern software-defined radio, WiFi chip, LTE modem, and satellite receiver is built around I/Q architecture: it cleanly separates the carrier physics from the signal processing.
