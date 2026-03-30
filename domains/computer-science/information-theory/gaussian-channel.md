---
id: gaussian-channel
title: Gaussian Channel
domain: computer-science
course: information-theory
prerequisites:
- id: channel-capacity
  type: hard
- id: channel-coding-theorem
  type: hard
- id: differential-entropy
  type: hard
builds-toward:
- mimo-capacity
tags:
- Gaussian channel
- AWGN
- Shannon-Hartley
- SNR
- bandwidth
stage: expert
status: validated
---

# Gaussian Channel

## Core Idea
The additive white Gaussian noise (AWGN) channel models a continuous-valued channel where the received signal Y = X + Z, with Z ~ N(0, N) independent of the input X, and the input has a power constraint E[X^2] <= P. Its capacity is C = (1/2) log2(1 + P/N) bits per channel use — the Shannon-Hartley formula. The capacity-achieving input distribution is Gaussian: X ~ N(0, P). Combined with the bandwidth theorem, this gives C = W log2(1 + P/(NW)) bits per second for bandwidth W, establishing the fundamental tradeoff between bandwidth, power, and data rate that governs all modern wireless and wired communication.

## Questions

```yaml
- question: "A Gaussian channel has SNR = P/N = 15 dB (approximately 31.6 in linear scale). What is the channel capacity?"
  type: multiple-choice
  options:
    - "C = 15 bits per channel use"
    - "C = (1/2) log2(1 + 31.6) ≈ (1/2)(5.02) ≈ 2.51 bits per channel use"
    - "C = log2(15) ≈ 3.91 bits per channel use"
    - "C = 31.6 bits per channel use"
  answer: 1
  explanation: "First convert dB to linear: 15 dB means P/N = 10^(15/10) = 31.6. Then C = (1/2) log2(1 + 31.6) = (1/2) log2(32.6) ≈ (1/2)(5.03) ≈ 2.51 bits per channel use. The 1/2 factor comes from the real-valued channel; a complex channel (as in modern wireless systems) would give log2(1 + SNR) without the 1/2. Each 3 dB of SNR increase adds approximately 0.5 bits of capacity — this logarithmic scaling means gains get harder as SNR increases."

- question: "As SNR approaches infinity, the capacity of the Gaussian channel grows without bound. As SNR approaches zero, capacity approaches zero linearly. Which regime is more relevant for modern wireless communications?"
  type: multiple-choice
  options:
    - "The high-SNR regime, because modern systems operate at very high power levels"
    - "The low-SNR (bandwidth-rich, power-limited) regime, because technologies like spread-spectrum and IoT devices often operate below 0 dB SNR by using wide bandwidth and sophisticated coding"
    - "Neither — modern systems operate exactly at the Shannon limit"
    - "Both regimes are equally relevant"
  answer: 1
  explanation: "Many modern systems (GPS, spread-spectrum, IoT sensors, deep-space communication) operate at very low SNR by spreading the signal across wide bandwidth. At low SNR, C ≈ (P/N) * (1/(2*ln2)) bits per channel use, which is linear in SNR. The bandwidth-power tradeoff C = W*log2(1+P/(NW)) shows that as bandwidth W increases with fixed power, capacity approaches P/(N*ln2) — a finite limit determined by power alone. This 'ultimate Shannon limit' of -1.59 dB per bit is a key benchmark for power-efficient communication design."

- question: "Explain why the Gaussian distribution is the capacity-achieving input distribution for the AWGN channel, connecting this to the maximum-entropy property of the Gaussian."
  type: short-answer
  answer: "The capacity C = max I(X;Y) = max [h(Y) - h(Y|X)] = max h(Y) - h(Z), since h(Y|X) = h(Z) is fixed (the noise is independent of the input). So we need to maximize h(Y) subject to the power constraint. Y = X + Z, and the variance of Y is at most P + N (with equality when X has variance P). Among all distributions with variance P + N, the Gaussian maximizes differential entropy. This is achieved when X is Gaussian with variance P, since the sum of independent Gaussians is Gaussian. The maximum entropy property of the Gaussian is thus directly responsible for the Gaussian input being optimal."
  explanation: "This is a beautiful example of how information-theoretic properties (maximum entropy of the Gaussian) yield engineering results (the capacity-achieving strategy). The same reasoning extends to vector Gaussian channels: the capacity-achieving input is always Gaussian, with covariance structure determined by the channel and power constraints."
```

## Explainer

The additive white Gaussian noise (AWGN) channel is the most important continuous channel model in information theory. It models any communication system where the dominant impairment is thermal noise: Y = X + Z, where X is the transmitted signal, Z ~ N(0, N) is Gaussian noise, and E[X^2] <= P constrains the transmit power. The capacity of this channel — the Shannon-Hartley formula — is one of the most important equations in engineering.

The capacity derivation uses differential entropy. I(X;Y) = h(Y) - h(Y|X). Since Y|X = X + Z and Z is independent of X, h(Y|X) = h(Z) = (1/2) log2(2*pi*e*N), which is fixed. To maximize I(X;Y), we maximize h(Y). The variance of Y = X + Z is Var(X) + N <= P + N. Among all distributions with a given variance, the Gaussian maximizes differential entropy. So h(Y) <= (1/2) log2(2*pi*e*(P+N)), with equality when X ~ N(0, P). The capacity is C = (1/2) log2(2*pi*e*(P+N)) - (1/2) log2(2*pi*e*N) = (1/2) log2(1 + P/N).

The **bandwidth extension** connects to real-world systems. A band-limited channel of bandwidth W Hz can carry 2W independent real-valued samples per second (Nyquist's theorem). If the noise power spectral density is N_0/2, the total noise power in bandwidth W is N = N_0*W. With total signal power P, the capacity in bits per second is C = W * log2(1 + P/(N_0*W)). This formula captures the fundamental bandwidth-power tradeoff: you can increase data rate by using more bandwidth (but with diminishing returns) or more power (with logarithmic returns). The limit as W goes to infinity with fixed P is C = P/(N_0 * ln 2) — Shannon's ultimate limit, determined by power alone.

Modern communication systems (4G LTE, 5G NR, Wi-Fi 6/7, satellite links) are designed with this formula as the benchmark. The gap between a system's actual throughput and the Shannon-Hartley capacity quantifies how much room for improvement exists. Turbo codes and LDPC codes operate within 0.1 dB of the Gaussian channel capacity, a remarkable engineering achievement that took nearly 50 years after Shannon's theorem to attain.
