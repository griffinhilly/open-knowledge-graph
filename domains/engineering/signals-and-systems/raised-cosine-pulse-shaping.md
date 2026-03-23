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
stage: expert
status: validated
---

# Raised-Cosine Pulse Shaping

## Core Idea
Raised-cosine pulse shaping satisfies the Nyquist criterion with smooth spectral roll-off. The impulse response is p(t) = sinc(t/Ts)·cos(παt/Ts)/(1 – 4α²t²/Ts²), where roll-off factor α ∈ [0,1] trades bandwidth efficiency for time decay rate. Root-raised-cosine splits the response between transmit and receive filters, optimizing noise performance in communication systems.

## Questions

```yaml
- question: "A designer increases the raised-cosine roll-off factor from α = 0.2 to α = 0.8. What are the consequences for the communication link?"
  type: multiple-choice
  options:
    - "ISI increases because the wider spectrum causes more interference between adjacent symbols"
    - "ISI decreases because the extra bandwidth provides guard space; the Nyquist zero-crossing property is weakened"
    - "Bandwidth usage increases, but ISI is unchanged — the zero-crossing property is preserved; the benefit is faster time-domain decay that makes the system more robust to timing jitter"
    - "The symbol rate must decrease proportionally because the increased bandwidth consumes the available channel"
  answer: 2
  explanation: "The zero-ISI property (zero crossings at multiples of Ts) is preserved for all values of α — roll-off does not change whether there is ISI when sampling perfectly. What α controls is the decay rate of the impulse response: higher α gives 1/t³ decay instead of 1/t, making the system far more tolerant of timing errors. The tradeoff is that a wider roll-off uses more bandwidth (up to twice the minimum at α = 1). ISI robustness and bandwidth efficiency are what trade off, not ISI performance per se."

- question: "In a real digital communication system, why is pulse shaping typically split between a root-raised-cosine (RRC) filter at the transmitter and another RRC filter at the receiver, rather than placing the full raised-cosine at the transmitter?"
  type: multiple-choice
  options:
    - "Because receivers cannot implement complex spectral shapes — only simple filters like square windows"
    - "Because applying the full filter at the transmitter would violate FCC spectral mask regulations in most bands"
    - "Because the receiver must apply a matched filter (the time-reverse of the transmit pulse) to maximize SNR, and for the raised-cosine this matched filter is an RRC — the transmit and receive RRC filters cascade to produce the full raised-cosine at the sampling instant, achieving both zero ISI and optimal noise performance"
    - "Because splitting the filter reduces total computational cost equally between transmitter and receiver hardware"
  answer: 2
  explanation: "Matched filtering is required to maximize SNR at the sampling instant. The matched filter is the time-reverse of the transmit pulse. For a symmetric raised-cosine, the matched filter is also a raised-cosine — but if the receiver applies a full raised-cosine on top of the full transmit raised-cosine, the cascade is a 'double raised-cosine' that does NOT satisfy the Nyquist criterion and reintroduces ISI. Splitting each end into the square root solves this: RRC_tx × RRC_rx = full raised-cosine, achieving zero ISI and matched filtering simultaneously."

- question: "A raised-cosine filter with roll-off factor α = 0.5 has worse ISI performance at the sampling instant than the sinc pulse (α = 0), because it uses more bandwidth."
  type: true-false
  answer: false
  explanation: "The zero-ISI property (the Nyquist criterion) holds for all values of α — zero crossings occur at exactly multiples of Ts regardless of roll-off. ISI performance at the correct sampling instant is equally zero for any α. In practice, ISI is actually better with higher α because the faster 1/t³ decay (versus 1/t for sinc) means neighboring symbol tails are much smaller when timing is imperfect. The tradeoff is bandwidth, not ISI at the ideal sampling time."

- question: "The sinc pulse is theoretically optimal for bandwidth efficiency (minimum bandwidth for zero-ISI signaling) but impractical because small timing errors cause large ISI due to its slow 1/t amplitude decay."
  type: true-false
  answer: true
  explanation: "The sinc pulse's rectangular spectrum uses the absolute minimum bandwidth (1/(2Ts)), but it decays only as 1/t. Any receiver timing offset causes energy from many neighboring symbols to pile up at the sampling instant — even a tiny fractional-symbol timing error produces significant ISI from the slowly-decaying tails of dozens of surrounding symbols. This sensitivity to timing jitter makes the theoretically optimal sinc pulse impractical, which is exactly the problem the raised-cosine filter was designed to solve by trading some bandwidth for much faster temporal decay."

- question: "Explain why applying the full raised-cosine filter entirely at the transmitter (rather than splitting it as root-raised-cosine at both ends) would fail to achieve the goals of a well-designed digital communication link."
  type: short-answer
  answer: "Applying the full raised-cosine at the transmitter satisfies zero-ISI but fails noise optimization. The receiver must apply a matched filter — the time-reverse of the transmit pulse — to maximize signal-to-noise ratio. If the transmit pulse is a full raised-cosine, the matched receive filter is also a full raised-cosine, and the cascade is a double raised-cosine whose spectrum is the square of the raised-cosine spectrum. This does not satisfy the Nyquist zero-ISI criterion, reintroducing intersymbol interference. The root-raised-cosine split is the solution: transmit RRC × receive RRC = full raised-cosine, simultaneously achieving zero ISI and matched filtering."
  explanation: "This is the key system-level insight that goes beyond block-diagram understanding: the filter design is constrained by the need to jointly satisfy two requirements (zero ISI and matched filtering) that must be shared across the link. Neither requirement can be satisfied independently at one end without compromising the other."
```

## Explainer

Your prerequisite — the Nyquist ISI criterion — tells you that a pulse shape achieves zero intersymbol interference if and only if its spectrum, when periodically replicated at intervals of 1/Ts, sums to a constant. The canonical pulse satisfying this is the **sinc function**: sinc(t/Ts) = sin(πt/Ts)/(πt/Ts). Its spectrum is a perfect rectangle — bandwidth exactly 1/(2Ts). This is theoretically ideal, but in practice sinc pulses are a disaster. They decay only as 1/t, which means small timing errors at the receiver cause significant tails from neighboring symbols to pile up at the sample instant. You need a Nyquist pulse that decays faster.

The **raised-cosine filter** is the practical fix. Its spectrum adds smooth "cosine roll-off" transitions at the edges of the rectangular spectrum, blending from the full passband down to zero over a bandwidth controlled by the **roll-off factor** α ∈ [0,1]. When α = 0 the spectrum is exactly rectangular (the sinc case). When α = 1 the spectrum is a full raised-cosine shape, using twice the minimum bandwidth. The payoff is that the impulse response now decays as 1/t³ instead of 1/t — far more forgiving of timing jitter. The tradeoff is bandwidth: a roll-off of α = 0.5 uses 50% more bandwidth than the theoretical minimum, but the faster time-domain decay makes the system robust in practice.

The zero-crossings of the raised-cosine pulse still occur exactly at multiples of Ts, so the Nyquist criterion is still satisfied — there is no ISI when sampling at the correct instant. The ISI-free property is preserved regardless of α; α only controls the decay envelope. This is the key insight: roll-off is a parameter you tune based on how much extra bandwidth you can afford versus how much timing uncertainty you have to tolerate.

In a real communication link, the pulse-shaping filter must be split between transmitter and receiver. You cannot put the full raised-cosine at just one end, because the receiver needs a matched filter to maximize signal-to-noise ratio — which means the receiver filter must be the time-reverse of the transmit filter. For a symmetric raised-cosine filter, both filters are identical: the **root-raised-cosine** (RRC), whose spectrum is the square root of the raised-cosine spectrum. The cascaded transmitter and receiver RRC filters together produce the full raised-cosine pulse shape at the sampling instant, simultaneously achieving zero ISI and matched filtering. Understanding this split is what separates a block-diagram understanding of pulse shaping from a system-level design perspective.
