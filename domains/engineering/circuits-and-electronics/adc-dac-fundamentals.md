---
id: adc-dac-fundamentals
title: ADC and DAC Fundamentals
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: digital-logic-gates-basics
  type: hard
- id: operational-amplifier-fundamentals
  type: soft
tags:
- analog-to-digital
- digital-to-analog
- sampling
- quantization
- resolution
- nyquist
- sample-and-hold
- r2r-ladder
- flash-adc
- successive-approximation
stage: advanced
status: draft
---

# ADC and DAC Fundamentals

## Core Idea
Analog-to-digital converters (ADCs) and digital-to-analog converters (DACs) bridge the continuous analog world and discrete digital processing. A DAC converts an N-bit digital code to one of 2^N discrete voltage levels; the R-2R ladder DAC uses a resistor network to weight each bit by powers of two, producing V_out = V_ref * (digital code) / 2^N. An ADC performs the inverse: sampling the analog signal at discrete time intervals (sample rate f_s), holding each sample constant (sample-and-hold), and quantizing it to the nearest digital code. The Nyquist-Shannon theorem requires f_s > 2 * f_max to avoid aliasing — frequency components above f_s/2 fold back into the signal band as distortion. Resolution (number of bits N) determines the smallest detectable voltage change (LSB = V_ref / 2^N) and the signal-to-quantization-noise ratio (SQNR = 6.02*N + 1.76 dB). Common ADC architectures trade speed for resolution: flash converters (fastest, uses 2^N - 1 comparators), successive-approximation (moderate speed, one comparator with binary search logic), and sigma-delta (highest resolution, uses oversampling and noise shaping). Each additional bit of resolution doubles the number of quantization levels and improves SQNR by approximately 6 dB.

## How It's Best Learned
Build an R-2R ladder DAC and measure the output voltage for each binary input code to verify the binary weighting. Then study the successive-approximation ADC as a binary search: the internal DAC generates a comparison voltage, the comparator decides if the input is above or below, and the logic sets or clears each bit from MSB to LSB. Sample a sine wave at various rates relative to its frequency to observe aliasing when the Nyquist criterion is violated.

## Common Misconceptions
- Confusing sampling rate with resolution — increasing the sampling rate captures faster signals but does not improve voltage precision; increasing bit depth improves voltage precision but does not capture faster signals.
- Assuming aliasing can be removed after digitization — once aliased frequencies are folded into the signal band, they are indistinguishable from real signal components; an analog anti-aliasing filter before the ADC is mandatory.
- Thinking more bits of resolution is always achievable by simply specifying a higher-resolution ADC — thermal noise, reference voltage stability, and layout-induced errors set a practical floor below which additional bits represent noise rather than signal.

## Explainer

The real world is analog — temperatures, pressures, sounds, and voltages are continuous quantities that can take any value in a range. Digital processors, on the other hand, only understand discrete binary numbers. **Analog-to-digital converters (ADCs)** and **digital-to-analog converters (DACs)** are the translators that let digital systems sense and control the physical world. You already know from digital logic that a collection of N bits can represent 2^N distinct states. A DAC exploits that directly: each unique N-bit binary code maps to one of 2^N discrete output voltage levels, uniformly spaced between 0 and V_ref. The smallest possible voltage step is one **LSB** (least significant bit) = V_ref / 2^N.

The **R-2R ladder DAC** makes this concrete using only two resistor values. Each bit position contributes a current that is exactly half the contribution of the bit above it — MSB contributes V_ref/2, the next bit V_ref/4, and so on — because the R-2R network binary-weights the currents through each node. Summing these currents through a final resistor gives a voltage proportional to the binary code. This is the same weighted-sum idea you know from binary number representation: each bit position has a value that is a power of two relative to the LSB.

An **ADC** runs the process in reverse, but it must solve a harder problem: it needs to represent a continuously varying analog voltage as a discrete number, repeatedly over time. This requires two steps. First, **sampling** — the analog voltage is measured at regular intervals at rate f_s. Second, **quantization** — each sampled voltage is rounded to the nearest of the 2^N discrete code levels. The **Nyquist-Shannon theorem** constrains sampling rate: if the signal contains frequency components up to f_max, you must sample at f_s > 2·f_max or else **aliasing** occurs — high-frequency components fold back into the signal band, indistinguishable from real low-frequency content. This is why your phone records audio at 44.1 kHz: human hearing tops out near 20 kHz, and 44.1 kHz satisfies the Nyquist criterion with margin.

**Resolution** and **speed** trade off across ADC architectures. The **flash ADC** uses 2^N − 1 comparators to evaluate all possible code levels simultaneously — blindingly fast but exponentially expensive in hardware; 8-bit flash ADCs are feasible, 16-bit ones are not. The **successive-approximation register (SAR) ADC** performs a binary search in N clock cycles: compare input to V_ref/2, set or clear the MSB, then bisect the remaining range — moderate speed, one comparator, and well-suited to the 8–16 bit range common in microcontrollers. **Sigma-delta ADCs** oversample at many times f_s and use noise shaping to push quantization noise out of the signal band, achieving 16–24 bit resolution at audio frequencies but too slowly for fast signals. Understanding these architectures means knowing that "higher resolution" and "faster conversion" are not independently selectable — physics and cost force a choice.
