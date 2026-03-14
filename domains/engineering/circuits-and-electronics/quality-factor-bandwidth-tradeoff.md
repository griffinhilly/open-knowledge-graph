---
id: quality-factor-bandwidth-tradeoff
title: Quality Factor and Bandwidth Tradeoffs
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: series-resonance-characteristics
  type: hard
- id: parallel-resonance-characteristics
  type: soft
builds-toward:
- frequency-response-analysis-bode
tags:
- quality-factor
- bandwidth
- resonance
stage: formal-systems
status: draft
---

# Quality Factor and Bandwidth Tradeoffs

## Core Idea
Quality factor Q = ω₀·L/R (series) or Q = ω₀·R·C (parallel) measures how sharp the resonance peak is. Higher Q implies narrower bandwidth BW ≈ f₀/Q and stronger filtering. The relationship Q·BW ≈ ω₀ shows the fundamental tradeoff: sharpness requires higher Q but produces narrower passband. This tradeoff is critical in filter design and tuned circuit applications.

## How It's Best Learned
Sweep the frequency of a series RLC circuit near resonance and measure the current response for different Q values. Plot the resonance curve and measure bandwidth at the half-power points (0.707 of peak current).

## Common Misconceptions
Students often assume higher Q is always better without recognizing the bandwidth narrowing. Some confuse the half-power bandwidth with full-power bandwidth, or incorrectly calculate Q from peak current alone without considering the impedance.
