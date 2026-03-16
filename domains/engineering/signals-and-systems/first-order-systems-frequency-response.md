---
id: first-order-systems-frequency-response
title: First-Order Systems and Frequency Response
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
- id: frequency-response-magnitude-phase
  type: hard
tags:
- first-order-systems
- transient-response
- steady-state
stage: advanced
status: draft
---

# First-Order Systems and Frequency Response

## Core Idea
First-order systems H(s) = ω_n/(s + ω_n) have a single pole at s = -ω_n. Time-domain response includes exponential approach to steady state with time constant τ = 1/ω_n. Frequency response has -20 dB/decade rolloff above the corner frequency ω_n; -45° phase shift at ω_n.

## Explainer

A first-order system is the simplest dynamic system that responds to changes over time — one energy storage element, one pole, one time constant. Physical examples are everywhere: an RC circuit charging a capacitor, a thermometer reaching thermal equilibrium, a damper resisting velocity, a liquid level in a tank with a drain. You already know from transfer function theory that a pole at s = −ω_n means the system's natural response is e^(−ω_n t) — a decaying exponential. The **time constant** τ = 1/ω_n is the single number that characterizes how fast: after one time constant, the response has reached 63% of its final value; after five time constants, it is effectively at steady state (99.3%).

The step response is the most intuitive window into first-order behavior. Apply a unit step input and the output rises as y(t) = 1 − e^(−t/τ). The initial slope of this curve at t = 0 equals 1/τ — the steeper the initial rise, the faster the system. A fast system (small τ, large ω_n, pole far left in the complex plane) tracks the input almost immediately. A slow system (large τ, pole close to the origin) responds sluggishly. The pole location on the negative real axis is the geometric representation of this speed: distance from the origin equals ω_n equals 1/τ.

Now evaluate the same transfer function on the imaginary axis by substituting s = jω to get H(jω). The **magnitude** is |H(jω)| = ω_n / √(ω² + ω_n²). At low frequencies ω << ω_n, the denominator is dominated by ω_n, and |H| ≈ 1 (0 dB) — signals pass through unattenuated. At high frequencies ω >> ω_n, the denominator grows as ω and |H| ≈ ω_n/ω — magnitude falls at −20 dB per decade, or a factor of 10 for every decade increase in frequency. The **corner frequency** ω_n (or equivalently f_n = ω_n/2π) is the transition point where magnitude is exactly 1/√2 = −3 dB. The **phase** of H(jω) is −arctan(ω/ω_n), starting at 0° at DC and approaching −90° at very high frequencies, with exactly −45° at ω = ω_n. This −45° at the corner frequency is a diagnostic: if you apply a sinusoid at the corner frequency and measure 45° phase lag in the output, you have measured the pole location directly.

Together, the time-domain picture (time constant, exponential approach) and frequency-domain picture (−3 dB corner, −20 dB/decade rolloff, −45° phase at corner) are two faces of the same fact: the single pole at s = −ω_n. Every parameter is interchangeable — measure any one and you know all the others. First-order systems are also the building block from which more complex systems are assembled: a cascade of two first-order sections gives a second-order system with a pair of poles; a feedback loop around a first-order plant creates a new first-order closed-loop system with a different pole location. Mastering this single-pole case thoroughly makes every more complex system easier to decompose and understand.
