---
id: anti-aliasing-filters-pre-sampling-design
title: Anti-Aliasing Filters and Pre-Sampling Design
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
builds-toward:
- decimation-anti-aliasing-and-downsampling
- reconstruction-filters-post-interpolation-design
tags:
- anti-aliasing
- filters
- sampling
- design
stage: advanced
status: draft
---

# Anti-Aliasing Filters and Pre-Sampling Design

## Core Idea
Aliasing occurs when frequency components above the Nyquist rate (fs/2) are not removed before sampling. Anti-aliasing filters (lowpass) eliminate out-of-band content before the ADC to prevent spectral folding. The filter must have sharp transition band near fs/2 and sufficient stopband attenuation to reduce aliases below noise floor. Trade-offs exist between filter sharpness (cost, latency) and aliasing suppression.

## How It's Best Learned
Demonstrate aliasing on a signal without anti-aliasing filter, then add a lowpass filter before sampling and observe aliased components are suppressed. Design filter specifications from acceptable alias level.

## Common Misconceptions
- Thinking sampling theorem eliminates need for anti-aliasing filters (it justifies their requirement).
- Assuming filter edge must be exactly at fs/2 (should be below to account for filter transition).
- Not accounting for filter delay when designing data acquisition pipelines.

## Explainer

From the Nyquist-Shannon sampling theorem, you know that to perfectly reconstruct a signal from its samples, the sampling rate fs must be at least twice the highest frequency in the signal — the **Nyquist rate**. But the theorem comes with a hidden assumption: the signal must contain no frequencies above fs/2 *before* sampling. In reality, every physical signal contains some energy at all frequencies (noise, harmonics, broadband interference), and the ADC has no way to know which frequencies are "real" and which are undesirable. When you sample, all frequencies above fs/2 fold back into the 0 to fs/2 range, permanently contaminating your data — this is **aliasing**, and it cannot be corrected after the fact.

An **anti-aliasing filter** is a lowpass filter placed between the analog signal source and the ADC. Its job is to attenuate all signal content above fs/2 before the ADC ever sees it, so that the sampled spectrum contains only frequencies you actually want. The filter specification comes directly from the sampling rate and your acceptable alias level: if your ADC has 12-bit resolution, aliased components must be attenuated below 1 part in 2¹² ≈ 0.024% of full scale — which typically means at least 72 dB of stopband attenuation above fs/2. The steeper the filter's roll-off in the **transition band** (the region between the passband edge, where you want minimal attenuation, and the stopband edge, which must be at or below fs/2), the better the suppression — but steeper roll-off requires higher filter order, which means more components, more cost, and more phase delay.

A critical practical subtlety is that the filter's passband edge must be set *below* fs/2, not at it. Real filters have a gradual transition, not a vertical cliff. If you set the filter cutoff exactly at fs/2, then frequencies just below fs/2 will be attenuated (hurting your signal), and frequencies just above fs/2 will only be partially attenuated (still causing aliasing). A conservative design places the passband edge at some fraction of fs/2 (say 0.4·fs) and requires the stopband attenuation to reach its target by the Nyquist frequency. The gap between passband edge and fs/2 is "used up" by the filter's transition band.

The filter also introduces **group delay** — a time shift that varies with frequency for most practical filter designs. For systems where precise timing of events matters (transient measurements, edge detection, multi-channel synchronization), this delay must be accounted for and possibly compensated. Linear-phase FIR filters can achieve constant group delay at the cost of higher order; minimum-phase IIR filters (Butterworth, Chebyshev) have non-constant delay but much lower order for the same roll-off. Choosing the right anti-aliasing filter is not just a cutoff frequency decision — it is a system-level tradeoff between sampling rate, signal bandwidth, alias suppression, filter complexity, and time-domain fidelity.
