---
id: first-order-active-filters
title: First-Order Active Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: passive-filter-design
  type: hard
- id: operational-amplifier-fundamentals
  type: hard
builds-toward:
- second-order-active-filters
tags:
- active-filter
- low-pass
- high-pass
- op-amp-filter
- cutoff-frequency
- passband-gain
- roll-off
stage: formal-systems
status: draft
---

# First-Order Active Filters

## Core Idea
First-order active filters combine op-amps with RC networks to achieve frequency-selective behavior with passband gain — something passive filters cannot provide. An active low-pass filter places a capacitor in the feedback path of an inverting amplifier (or uses a non-inverting topology with an RC network at the input), producing a transfer function with a flat passband gain of -R_f/R_in and a -20 dB/decade roll-off above the cutoff frequency f_c = 1/(2*pi*R_f*C). The active high-pass filter places the capacitor in the input path, passing high frequencies with gain while attenuating frequencies below f_c. Unlike passive filters, active filters can provide gain greater than unity in the passband, have low output impedance (driven by the op-amp output), and do not suffer from loading effects when cascaded. The cutoff frequency and passband gain are independently adjustable through separate component choices. However, active filters are limited by the op-amp's gain-bandwidth product, supply voltage, and power consumption — constraints absent in passive designs.

## How It's Best Learned
Start from the inverting amplifier and replace either R_in or R_f with an impedance (R + 1/jwC or R || 1/jwC). Derive the transfer function, identify the cutoff frequency and passband gain, then sketch the Bode magnitude and phase plots. Compare directly to the equivalent passive RC filter to see the gain advantage and the independence of gain and cutoff frequency settings.

## Common Misconceptions
- Assuming active filters are always superior to passive filters — at very high frequencies (above the op-amp's useful bandwidth), passive filters outperform active ones, and passive filters require no power supply.
- Setting the passband gain arbitrarily high without considering the gain-bandwidth product — a first-order active filter with 40 dB passband gain and a 10 kHz cutoff requires an op-amp GBW of at least 1 MHz, and the roll-off will deviate from ideal well before that.
- Believing first-order active filters have sharper roll-off than first-order passive filters — both roll off at -20 dB/decade; the active version adds gain and buffering but does not change the filter order or roll-off rate.
