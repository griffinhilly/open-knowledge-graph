---
id: bandpass-sampling-and-undersampling
title: Bandpass Sampling and Undersampling
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
builds-toward:
- complex-baseband-iq-representation-analysis
tags:
- bandpass-sampling
- undersampling
- sampling-theorem
stage: expert
status: validated
---

# Bandpass Sampling and Undersampling

## Core Idea
Bandpass signals containing no DC or low-frequency content can be sampled below the Nyquist rate of the full signal bandwidth without aliasing. The sampling rate must exceed twice the signal bandwidth (not twice the highest frequency) and must be chosen to place the signal spectrum in the correct location after downsampling. Bandpass sampling enables lower sampling rates for high-frequency signals, reducing data rates and processing complexity.

## How It's Best Learned
Design a bandpass signal (FM radio example: 100 MHz bandwidth). Apply bandpass sampling theorem to calculate minimum sampling rate below the naive 2×100MHz. Verify no aliasing occurs.

## Common Misconceptions
- Confusing bandpass Nyquist rate with lowpass (depends on bandwidth, not highest frequency).
- Thinking any sampling rate less than 2fc works (must satisfy bandpass conditions).
- Not accounting for spectral folding into correct position for useful downsampling.

## Questions

```yaml
- question: "An FM radio signal occupies the band from 99.9 MHz to 100.1 MHz (200 kHz bandwidth). What is the minimum sampling rate required under the bandpass sampling theorem?"
  type: multiple-choice
  options:
    - "200.2 MHz — slightly above twice the highest frequency in the signal"
    - "400 kHz — twice the signal bandwidth"
    - "100.1 MHz — equal to the highest frequency"
    - "Any rate below 200.2 MHz works automatically, as long as it exceeds twice the bandwidth"
  answer: 1
  explanation: "The bandpass sampling theorem states that the minimum rate is 2B where B is the signal bandwidth, provided the rate is chosen carefully to avoid spectral overlap. With B = 200 kHz, the minimum is 400 kHz — a factor of 500× less than the naïve 200.2 MHz (2 × f_max). Option D is wrong because not any rate below 2f_max works: the rate must be selected so that spectral copies of the signal land in non-overlapping positions. The valid rates form discrete windows, and choosing carelessly within those windows can still cause aliasing."

- question: "A bandpass signal is centered at 1 GHz with a bandwidth of 10 MHz. An engineer samples it at 25 MHz. The resulting digital samples contain a version of the signal at a much lower frequency. What has happened?"
  type: multiple-choice
  options:
    - "The signal was destroyed by aliasing because the rate is far below 2 GHz"
    - "The sampling process has downconverted the signal to a lower frequency by deliberately exploiting aliasing"
    - "The signal was destroyed because 25 MHz is not an integer fraction of 1 GHz"
    - "The signal is present at 1 GHz in the digital samples, but the ADC only stores it at 25 MHz"
  answer: 1
  explanation: "Bandpass sampling deliberately exploits the aliasing mechanism: the spectral copies produced by sampling fold the high-frequency signal down to a lower frequency slot. This is intentional downconversion — the sampled signal is a low-frequency replica of the original bandpass signal, ready for digital processing at a fraction of the original rate. Option A applies only if the copies overlap and destroy each other. If the sampling rate was chosen correctly (validating the spectral window conditions), the folded copy is a clean, recoverable version of the original signal."

- question: "Bandpass sampling can achieve correct signal recovery even when sampling below the rate that would be required by the standard Nyquist theorem applied naïvely to the highest signal frequency."
  type: true-false
  answer: true
  explanation: "This is exactly the point of bandpass sampling. The standard Nyquist condition (f_s ≥ 2f_max) is a sufficient condition for a lowpass signal starting at DC. For a bandpass signal with no energy near DC, a lower rate suffices because the spectral copies need only avoid overlapping each other — not avoid overlapping with DC content that doesn't exist. The true requirement is that no two spectral copies overlap, and for a narrow-bandwidth bandpass signal, this can be satisfied at rates as low as 2B, where B is the bandwidth."

- question: "Any sampling rate that exceeds twice the signal bandwidth and is below twice the highest frequency will correctly recover a bandpass signal without aliasing."
  type: true-false
  answer: false
  explanation: "This is the most common misconception. The valid sampling rates for a bandpass signal form specific windows — not a continuous range from 2B to 2f_max. Within a given window, careful selection is required to ensure that spectral copies land in non-overlapping positions. A rate that technically satisfies 2B < f_s < 2f_max but is chosen carelessly can still cause aliasing if the folded spectrum partially overlaps an adjacent copy. The condition requires calculating valid windows for each integer n and verifying that f_s places the folded spectrum cleanly within an unoccupied frequency slot."

- question: "What does the true Nyquist sampling requirement actually state, and how does this differ from the common statement 'sample at twice the highest frequency'? Why does this distinction matter for bandpass signals?"
  type: short-answer
  answer: "The true requirement is that the sampling rate must be high enough that the spectral copies created by sampling do not overlap each other. When you sample at rate f_s, the spectrum is repeated at every multiple of f_s. Overlap-free copies allow perfect reconstruction with a filter. For a lowpass signal from DC to B, avoiding overlap requires f_s ≥ 2B — which equals 2f_max since f_max = B. For a bandpass signal from f_low to f_high with bandwidth B = f_high - f_low, the copies only need to avoid each other (not avoid DC), so a rate of 2B can suffice — far below 2f_high. The distinction matters because it enables sampling a 1 GHz signal at 20 MHz rather than 2 GHz, reducing hardware cost and processing burden by 100×."
  explanation: "The 'twice the highest frequency' rule is a correct consequence of the true rule for lowpass signals, where f_max = bandwidth. Teaching it as the fundamental rule causes confusion when students encounter bandpass signals, leading to the misconception that you always need to sample at 2f_max. Understanding the true requirement — spectral copy non-overlap — immediately reveals when and how lower rates are valid."
```

## Explainer

The Nyquist theorem you already know states that to recover a signal without aliasing, you must sample at least twice the highest frequency it contains. A 10 kHz audio signal needs at least 20 kHz sampling rate. That rule is correct — but it is actually more general than it first appears, and the generalization is what makes bandpass sampling powerful.

The real requirement behind the Nyquist theorem is not "sample at twice the highest frequency" but rather "sample fast enough that spectral copies don't overlap." When you sample at rate f_s, the spectrum of the sampled signal is the original spectrum repeated at every multiple of f_s. As long as those copies don't overlap each other, you can recover the original signal with a filter. For a low-pass signal from DC to B Hz, the copies are spaced f_s apart and you need f_s ≥ 2B to prevent overlap. But a **bandpass signal** is different: it lives in a narrow band from f_low to f_high, with a bandwidth B = f_high − f_low, and contains no energy below f_low. Its spectral copies only need to avoid each other — not avoid DC — which means a lower sampling rate can suffice.

Consider an FM radio signal centered at 100 MHz with 200 kHz bandwidth. A naïve interpretation of Nyquist says sample at 200 MHz. But the signal only occupies 200 kHz of bandwidth. Bandpass sampling says: choose a sampling rate f_s ≥ 2B = 400 kHz such that when the spectral copies land, they don't overlap. The condition is that there exists an integer n such that 2f_high/n ≥ f_s ≥ 2f_low/(n−1) — a window of valid sampling rates for each n. The copies fold the high-frequency signal down to a lower frequency band, effectively performing **downconversion for free** by exploiting aliasing deliberately. The output is a low-frequency replica of the original bandpass signal that a cheaper ADC and processor can handle.

The critical requirement is that the spectral copies must land cleanly — the folded spectrum must occupy a frequency slot without overlapping adjacent copies. If you choose f_s carelessly within the allowed range, the folded copy might partially overlap its neighbor, creating irrecoverable aliasing even though the rate technically satisfies a bandpass condition. This is why the "valid sampling windows" require careful calculation of the integer n and the exact f_s. The reward is significant: sampling a 1 GHz-centered signal with 10 MHz bandwidth at 25 MHz instead of 2 GHz, reducing data rates, converter cost, and power by 80× — which is why **undersampling** architectures are standard in software-defined radio receivers and radar signal processing.
