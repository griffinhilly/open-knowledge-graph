---
id: mimo-capacity
title: MIMO Capacity
domain: computer-science
course: information-theory
prerequisites:
- id: gaussian-channel
  type: hard
- id: channel-capacity
  type: hard
builds-toward:
- network-information-theory
tags:
- MIMO
- multiple antenna
- spatial multiplexing
- capacity scaling
- eigenmode
stage: expert
status: validated
---

# MIMO Capacity

## Core Idea
Multiple-input multiple-output (MIMO) channels use multiple transmit and receive antennas, modeled as Y = HX + Z where H is the channel matrix, X is the input vector, and Z is Gaussian noise. With n_T transmit and n_R receive antennas and known channel matrix H, the capacity is C = max_{tr(K_X)<=P} log2 det(I + (1/N) H K_X H^*), where K_X is the input covariance. This decomposes via SVD into min(n_T, n_R) parallel Gaussian channels (eigenmodes), with optimal power allocation via water-filling. MIMO capacity scales linearly with min(n_T, n_R) in rich scattering — a breakthrough that powers modern wireless systems (4G, 5G, Wi-Fi).

## Questions

```yaml
- question: "A MIMO system has 4 transmit and 4 receive antennas in a rich scattering environment with high SNR. Approximately how does its capacity compare to a single-antenna (SISO) system at the same total power?"
  type: multiple-choice
  options:
    - "About the same — more antennas don't help because total power is fixed"
    - "About 4x the SISO capacity — MIMO capacity scales linearly with min(n_T, n_R) at high SNR"
    - "About 16x — capacity scales with n_T * n_R"
    - "About 2x — capacity scales logarithmically with antenna count"
  answer: 1
  explanation: "At high SNR with rich scattering, H has min(n_T, n_R) = 4 significant singular values, creating 4 parallel spatial channels. Each carries roughly (1/4) of the total power and achieves roughly (1/4) of what a SISO system would with full power. But there are 4 of them, and at high SNR the log(1 + SNR/4) ≈ log(SNR/4) ≈ log(SNR) - 2, so total capacity ≈ 4*log(SNR) - 8 versus SISO's log(SNR). The ratio approaches 4 = min(n_T, n_R). This linear scaling in antenna count, without requiring more bandwidth or power, is why MIMO is transformative."

- question: "Water-filling power allocation across MIMO eigenmodes allocates more power to weaker channels."
  type: true-false
  answer: false
  explanation: "Water-filling allocates MORE power to STRONGER eigenmodes and less (or zero) to weaker ones. The name comes from the analogy of pouring water into a vessel: the channel gains are the bottom (inverted — weak channels have higher 'floors'), and water (power) fills the gaps, naturally putting more water where the floor is lower (stronger channels). Weak eigenmodes may receive zero power if their channel gain is below a threshold. This is optimal because a bit of power yields more capacity on a strong channel than on a weak one."

- question: "Explain why MIMO capacity depends critically on the channel matrix H, and describe the conditions under which MIMO fails to provide a capacity gain over SISO."
  type: short-answer
  answer: "MIMO capacity depends on the singular values of H. If H has rank r, only r independent spatial streams can be supported. In rich scattering (urban, indoor), H is typically full-rank with comparable singular values, yielding near-maximum capacity gain. In line-of-sight (LOS) with no scattering, H may be rank-1 regardless of antenna count — all antennas see essentially the same path, and MIMO degenerates to beamforming (array gain only, no multiplexing gain). Capacity is then similar to SISO plus a power gain from beamforming. Correlated fading (antennas too close together, or poor scattering) reduces the effective rank and diminishes MIMO's multiplexing advantage."
  explanation: "This is why 5G massive MIMO systems use large numbers of antennas (64-256) — even in partially correlated channels, the effective rank is large enough to serve many users simultaneously via spatial multiplexing (MU-MIMO), approaching the sum capacity of the multi-user channel."
```

## Explainer

The Gaussian channel capacity C = (1/2) log(1 + SNR) describes a single-antenna system. MIMO extends this to multiple antennas, revealing that capacity can scale linearly with the number of antennas — a result that revolutionized wireless communications when Foschini and Telatar published it in the late 1990s.

The MIMO channel model is Y = HX + Z, where X is an n_T-dimensional transmitted vector, Y is an n_R-dimensional received vector, H is the n_R x n_T channel matrix, and Z ~ N(0, NI) is Gaussian noise. The entry h_{ij} represents the complex channel gain from transmit antenna j to receive antenna i. The capacity depends on the singular value decomposition (SVD) of H = U * Sigma * V^*. The SVD decomposes the MIMO channel into min(n_T, n_R) parallel scalar Gaussian channels with gains equal to the singular values sigma_1 >= sigma_2 >= ... >= sigma_r. The capacity is the sum of the capacities of these parallel channels: C = sum_i (1/2) log2(1 + p_i * sigma_i^2 / N), where p_i is the power allocated to eigenmode i.

**Water-filling** determines the optimal power allocation. Modes with larger gains (sigma_i^2) get more power; modes below a threshold get none. At high SNR, all modes receive similar power and the capacity is approximately min(n_T, n_R) * (1/2) log2(SNR/min(n_T,n_R)), growing linearly with the number of spatial dimensions. At low SNR, only the strongest mode is used (beamforming).

The practical impact is immense. 4G LTE uses 2x2 and 4x4 MIMO. 5G NR supports massive MIMO with 64+ antennas at the base station, enabling both high per-user capacity and multi-user spatial multiplexing. Wi-Fi 6/7 uses up to 8x8 MIMO. In each case, the information-theoretic MIMO capacity formula guides system design, antenna spacing, and the decision of when to use multiplexing versus beamforming. The theory extends to multi-user MIMO (MU-MIMO), where the base station's antenna array serves multiple users simultaneously, approaching the sum capacity of the broadcast channel.
