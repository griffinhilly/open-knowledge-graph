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
stage: expert
status: validated
---

# Nyquist Criterion for Zero Intersymbol Interference

## Core Idea
The Nyquist criterion specifies conditions on pulse response p(t) for zero intersymbol interference (ISI) at sampling times: p(nTs) = 1 for n=0 and p(nTs) = 0 for n≠0. In frequency domain: Σ P(f + k/Ts) = Ts. This ensures adjacent symbols do not interfere, enabling reliable symbol recovery from noisy channels.

## Questions

```yaml
- question: "A digital communication system transmits at 2000 symbols per second through a bandlimited channel. According to the Nyquist criterion, what is the minimum channel bandwidth required to achieve zero ISI?"
  type: multiple-choice
  options:
    - "2000 Hz — bandwidth must match the symbol rate"
    - "4000 Hz — the channel must support twice the symbol rate"
    - "1000 Hz — the minimum bandwidth is half the symbol rate"
    - "500 Hz — raised cosine filtering halves the required bandwidth"
  answer: 2
  explanation: "The Nyquist minimum bandwidth for zero ISI is f_min = R_s/2, where R_s is the symbol rate. For 2000 symbols/second, f_min = 1000 Hz. A channel of 1000 Hz bandwidth can support a sinc-pulse system at 2000 symbols/second with zero ISI. This is the direct analog of the sampling theorem: just as 2B samples/second can reconstruct a B-Hz signal, a B-Hz channel can support 2B symbols/second with Nyquist pulse shaping."

- question: "A system designer increases the raised cosine rolloff factor from α = 0.2 to α = 0.8, while keeping the symbol rate constant. What is the effect on the system?"
  type: multiple-choice
  options:
    - "Bandwidth efficiency improves because the filter is more selective at α = 0.8"
    - "ISI increases at α = 0.8 because the pulse tails decay more slowly"
    - "Bandwidth increases by a factor of (1 + 0.8)/(1 + 0.2) = 1.5, but the pulse is more robust to timing errors"
    - "The symbol rate must be reduced to compensate for the wider bandwidth at α = 0.8"
  answer: 2
  explanation: "Raised cosine bandwidth is (1 + α)/(2T), so increasing α from 0.2 to 0.8 increases bandwidth from 1.2/(2T) to 1.8/(2T) — a 50% increase. The tradeoff is that higher α produces pulses whose tails decay faster (as 1/t³), making them far more tolerant of timing jitter. At α = 0.2, the pulse tails are very slow-decaying and small timing errors cause severe ISI; at α = 0.8, timing errors have little effect. Real systems choose α as a tradeoff: more bandwidth for more robustness."

- question: "ISI is a structural problem caused by pulse shape and cannot be eliminated by simply increasing the transmitted signal power."
  type: true-false
  answer: true
  explanation: "ISI arises because the tails of a pulse spill into adjacent symbol intervals, and every other symbol in the stream contributes interference to any given sample. Increasing power amplifies both the desired symbol and all the interfering tails equally — the signal-to-ISI ratio does not improve. This is in contrast to additive noise, where more power improves the SNR. ISI must be addressed by designing the pulse shape to satisfy the Nyquist zero-crossing condition, or by equalizers that undo the channel's ISI at the receiver."

- question: "The ideal sinc pulse is widely used in practical digital communication systems because it achieves the theoretical minimum bandwidth for zero ISI."
  type: true-false
  answer: false
  explanation: "The sinc pulse satisfies the Nyquist condition perfectly in theory but is completely impractical for two reasons. First, its tails decay as 1/t — they are very slow to die away — so any timing error in sampling causes contributions from many neighboring symbols, producing catastrophic ISI. Second, implementing an ideal sinc filter requires an infinitely long impulse response (it is noncausal). Real systems use the raised cosine pulse, which sacrifices some spectral efficiency (using more bandwidth than the minimum) to achieve tails that decay as 1/t³, making the system robust to realistic timing errors."

- question: "Why is the raised cosine pulse preferred over the ideal sinc pulse in practice, even though both satisfy the Nyquist zero-ISI condition at the correct sampling instants?"
  type: short-answer
  answer: "Both pulses have zero crossings at all nonzero multiples of the symbol period T, so both produce zero ISI when sampled at exactly the right moments. The problem is that perfect sampling timing is impossible in real systems — there is always some jitter. The sinc pulse has tails that decay as 1/t: a small timing error ε means the pulse sampled at T + ε still has a large contribution from adjacent symbols. The raised cosine pulse's tails decay as 1/t³: the same timing error ε causes much smaller ISI, because the pulse value at T + ε is negligible. The raised cosine trades extra bandwidth (1+α times the Nyquist minimum) for this faster decay, making the system practical."
  explanation: "The core insight is that satisfying the Nyquist condition at exact sample points is necessary but not sufficient for reliable communication — you also need the pulse to be approximately zero near those sample points (not just exactly at them) to tolerate realistic timing imperfections. This is why rolloff factor α is a fundamental design parameter: α = 0 is theoretical perfection, and α > 0 is practical engineering."
```

## Explainer

From the sampling theorem, you know that a bandlimited signal with bandwidth B Hz can be reconstructed from samples taken at 2B samples per second, the Nyquist rate. Now consider the inverse problem in digital communications: you want to transmit discrete symbols (bits, or higher-order constellation points) through a channel with a limited bandwidth, at the highest possible symbol rate. Each transmitted symbol must be represented by a pulse that fits within the channel bandwidth — but narrow-bandwidth pulses have long time-domain tails that extend into neighboring symbol intervals. When those tails overlap and corrupt the detection of adjacent symbols, the result is **intersymbol interference (ISI)**.

Think concretely: you transmit symbol a₀ = +1 using a pulse p(t), then symbol a₁ at time T later, then a₂ at 2T, and so on. The received signal is the sum r(t) = Σ aₙ p(t − nT). When you sample r(t) at time t = 0 to recover a₀, you get not just p(0) · a₀ but also p(−T) · a₁ + p(−2T) · a₂ + …. If the pulse has nonzero values at those shifted sampling times, every other symbol leaks into your detection of a₀. ISI is the additive interference from every symbol in the sequence, and it cannot be removed by simply increasing signal power — it is a structural problem caused by the pulse shape.

The **Nyquist criterion** provides the exact condition on p(t) that guarantees zero ISI at the sampling instants: p(nT) = 1 for n = 0, and p(nT) = 0 for all nonzero integers n. In words, the pulse must pass through zero at every symbol period except its own. The sinc function sinc(t/T) = sin(πt/T)/(πt/T) satisfies this exactly — it equals 1 at t = 0 and crosses zero at every multiple of T. The sinc pulse corresponds to a **rectangular spectrum** of bandwidth 1/(2T), achieving the theoretical maximum symbol rate of 2B symbols per second over a channel of bandwidth B. This is the Nyquist rate for transmission, directly analogous to the sampling theorem you know.

In practice, the ideal sinc pulse is unusable: its tails decay as 1/t and never reach zero, so any timing error causes catastrophic ISI, and it requires an infinitely long filter. The **raised cosine spectrum** is the engineering solution. It modifies the rectangular spectrum with a smooth rolloff over an "excess bandwidth" Δf = α/2T, where α ∈ [0, 1] is the rolloff factor. The resulting pulse still satisfies the Nyquist zero-crossing condition, but its tails decay as 1/t³ instead of 1/t, making it robust to timing errors. The cost is reduced bandwidth efficiency: the raised cosine with rolloff α requires bandwidth (1+α)/(2T) instead of the minimum 1/(2T). Choosing α is a fundamental design tradeoff in every digital communication system — α = 0 maximizes spectral efficiency but demands perfect timing; α = 1 halves the spectral efficiency but tolerates practical timing jitter. Most real systems (cellular, satellite, cable modem) use α between 0.2 and 0.5 as a practical compromise.
