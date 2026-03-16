---
id: raised-cosine-pulse-shaping
title: Raised-Cosine Pulse Shaping
domain: engineering
course: signals-and-systems
prerequisites:
- id: nyquist-criterion-intersymbol-interference
  type: hard
tags:
- pulse-shaping
- raised-cosine
- isi
- bandwidth-efficiency
stage: advanced
status: draft
---

# Raised-Cosine Pulse Shaping

## Core Idea
Raised-cosine pulse shaping satisfies the Nyquist criterion with smooth spectral roll-off. The impulse response is p(t) = sinc(t/Ts)·cos(παt/Ts)/(1 – 4α²t²/Ts²), where roll-off factor α ∈ [0,1] trades bandwidth efficiency for time decay rate. Root-raised-cosine splits the response between transmit and receive filters, optimizing noise performance in communication systems.

## Explainer

Your prerequisite — the Nyquist ISI criterion — tells you that a pulse shape achieves zero intersymbol interference if and only if its spectrum, when periodically replicated at intervals of 1/Ts, sums to a constant. The canonical pulse satisfying this is the **sinc function**: sinc(t/Ts) = sin(πt/Ts)/(πt/Ts). Its spectrum is a perfect rectangle — bandwidth exactly 1/(2Ts). This is theoretically ideal, but in practice sinc pulses are a disaster. They decay only as 1/t, which means small timing errors at the receiver cause significant tails from neighboring symbols to pile up at the sample instant. You need a Nyquist pulse that decays faster.

The **raised-cosine filter** is the practical fix. Its spectrum adds smooth "cosine roll-off" transitions at the edges of the rectangular spectrum, blending from the full passband down to zero over a bandwidth controlled by the **roll-off factor** α ∈ [0,1]. When α = 0 the spectrum is exactly rectangular (the sinc case). When α = 1 the spectrum is a full raised-cosine shape, using twice the minimum bandwidth. The payoff is that the impulse response now decays as 1/t³ instead of 1/t — far more forgiving of timing jitter. The tradeoff is bandwidth: a roll-off of α = 0.5 uses 50% more bandwidth than the theoretical minimum, but the faster time-domain decay makes the system robust in practice.

The zero-crossings of the raised-cosine pulse still occur exactly at multiples of Ts, so the Nyquist criterion is still satisfied — there is no ISI when sampling at the correct instant. The ISI-free property is preserved regardless of α; α only controls the decay envelope. This is the key insight: roll-off is a parameter you tune based on how much extra bandwidth you can afford versus how much timing uncertainty you have to tolerate.

In a real communication link, the pulse-shaping filter must be split between transmitter and receiver. You cannot put the full raised-cosine at just one end, because the receiver needs a matched filter to maximize signal-to-noise ratio — which means the receiver filter must be the time-reverse of the transmit filter. For a symmetric raised-cosine filter, both filters are identical: the **root-raised-cosine** (RRC), whose spectrum is the square root of the raised-cosine spectrum. The cascaded transmitter and receiver RRC filters together produce the full raised-cosine pulse shape at the sampling instant, simultaneously achieving zero ISI and matched filtering. Understanding this split is what separates a block-diagram understanding of pulse shaping from a system-level design perspective.
