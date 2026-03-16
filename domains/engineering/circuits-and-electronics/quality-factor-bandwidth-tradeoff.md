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

## Explainer

From your study of series resonance, you know that at ω₀ = 1/√(LC) the inductive and capacitive impedances exactly cancel, leaving only resistance in the circuit. Current peaks at resonance and falls off as frequency moves away in either direction. The **quality factor Q** quantifies precisely how sharp that peak is — how quickly current falls as you detune from resonance. The higher the Q, the more energy a circuit stores relative to what it dissipates per cycle, and the sharper the resonance peak.

The physical meaning of Q comes from its energy interpretation: Q = 2π × (energy stored)/(energy dissipated per cycle). In a series RLC circuit, Q = ω₀L/R. Since inductors store energy and resistors dissipate it, a larger L or smaller R produces a higher Q. Equivalently, Q = ω₀/(2α) where α = R/2L is the damping coefficient — confirming that Q is large when damping is low. For a parallel RLC circuit the formula inverts: Q = ω₀RC, because now a larger R means less energy dissipated per cycle by the parallel resistor.

The **fundamental relationship** Q = f₀/BW connects quality factor to bandwidth directly. If the resonant frequency is f₀ = 1 MHz and Q = 50, the **half-power bandwidth** (the frequency interval between the two points where power falls to half its peak value, equivalently where current magnitude falls to 1/√2 ≈ 0.707 of its peak) is BW = f₀/Q = 20 kHz. The half-power points are called the **-3dB frequencies** because a power ratio of 1/2 corresponds to 10·log₁₀(1/2) ≈ -3 dB. Doubling Q halves the bandwidth; the product Q·BW = f₀ remains constant for a given resonant frequency.

This tradeoff is engineering, not just mathematics. In AM radio tuning, you want a high-Q resonator to select one station (narrow bandwidth) without passing adjacent stations. But in audio amplifier design, you need a bandpass response wide enough to cover the 20 Hz–20 kHz range, so low Q is required. In oscillator design, high Q improves frequency stability because the resonator resists detuning. In impedance matching, the Q determines how much bandwidth the matching network trades away for power transfer efficiency. Every resonant circuit application involves choosing where on the Q–bandwidth tradeoff curve to operate, and there is no universally correct answer — only the right balance for the specific requirements.
