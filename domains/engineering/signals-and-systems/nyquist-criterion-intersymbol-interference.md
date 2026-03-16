---
id: nyquist-criterion-intersymbol-interference
title: Nyquist Criterion for Zero Intersymbol Interference
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
- id: matched-filter-signal-detection
  type: soft
builds-toward:
- raised-cosine-pulse-shaping
tags:
- nyquist-criterion
- isi
- pulse-shaping
- communication
stage: advanced
status: draft
---

# Nyquist Criterion for Zero Intersymbol Interference

## Core Idea
The Nyquist criterion specifies conditions on pulse response p(t) for zero intersymbol interference (ISI) at sampling times: p(nTs) = 1 for n=0 and p(nTs) = 0 for n≠0. In frequency domain: Σ P(f + k/Ts) = Ts. This ensures adjacent symbols do not interfere, enabling reliable symbol recovery from noisy channels.

## Explainer

From the sampling theorem, you know that a bandlimited signal with bandwidth B Hz can be reconstructed from samples taken at 2B samples per second, the Nyquist rate. Now consider the inverse problem in digital communications: you want to transmit discrete symbols (bits, or higher-order constellation points) through a channel with a limited bandwidth, at the highest possible symbol rate. Each transmitted symbol must be represented by a pulse that fits within the channel bandwidth — but narrow-bandwidth pulses have long time-domain tails that extend into neighboring symbol intervals. When those tails overlap and corrupt the detection of adjacent symbols, the result is **intersymbol interference (ISI)**.

Think concretely: you transmit symbol a₀ = +1 using a pulse p(t), then symbol a₁ at time T later, then a₂ at 2T, and so on. The received signal is the sum r(t) = Σ aₙ p(t − nT). When you sample r(t) at time t = 0 to recover a₀, you get not just p(0) · a₀ but also p(−T) · a₁ + p(−2T) · a₂ + …. If the pulse has nonzero values at those shifted sampling times, every other symbol leaks into your detection of a₀. ISI is the additive interference from every symbol in the sequence, and it cannot be removed by simply increasing signal power — it is a structural problem caused by the pulse shape.

The **Nyquist criterion** provides the exact condition on p(t) that guarantees zero ISI at the sampling instants: p(nT) = 1 for n = 0, and p(nT) = 0 for all nonzero integers n. In words, the pulse must pass through zero at every symbol period except its own. The sinc function sinc(t/T) = sin(πt/T)/(πt/T) satisfies this exactly — it equals 1 at t = 0 and crosses zero at every multiple of T. The sinc pulse corresponds to a **rectangular spectrum** of bandwidth 1/(2T), achieving the theoretical maximum symbol rate of 2B symbols per second over a channel of bandwidth B. This is the Nyquist rate for transmission, directly analogous to the sampling theorem you know.

In practice, the ideal sinc pulse is unusable: its tails decay as 1/t and never reach zero, so any timing error causes catastrophic ISI, and it requires an infinitely long filter. The **raised cosine spectrum** is the engineering solution. It modifies the rectangular spectrum with a smooth rolloff over an "excess bandwidth" Δf = α/2T, where α ∈ [0, 1] is the rolloff factor. The resulting pulse still satisfies the Nyquist zero-crossing condition, but its tails decay as 1/t³ instead of 1/t, making it robust to timing errors. The cost is reduced bandwidth efficiency: the raised cosine with rolloff α requires bandwidth (1+α)/(2T) instead of the minimum 1/(2T). Choosing α is a fundamental design tradeoff in every digital communication system — α = 0 maximizes spectral efficiency but demands perfect timing; α = 1 halves the spectral efficiency but tolerates practical timing jitter. Most real systems (cellular, satellite, cable modem) use α between 0.2 and 0.5 as a practical compromise.
