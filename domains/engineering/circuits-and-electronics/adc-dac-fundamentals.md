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
stage: formal-systems
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
