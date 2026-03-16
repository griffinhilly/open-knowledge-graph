---
id: phase-and-amplitude-forced-oscillations
title: Phase and Amplitude in Forced Oscillations
domain: physics
course: classical-mechanics
prerequisites:
- id: driven-harmonic-oscillator
  type: hard
builds-toward:
- resonance-and-resonance-frequency
tags:
- oscillations
- phase
- amplitude
- forcing
stage: formal-systems
status: draft
---

# Phase and Amplitude in Forced Oscillations

## Core Idea
In steady-state forced oscillation, the amplitude A(ω) = F₀/√[(k−mω²)² + (bω)²] and phase lag φ(ω) both vary with driving frequency. At low ω, the oscillator is nearly in phase with the drive (φ ≈ 0°); at ω = ω₀, the phase lag is 90°; at high ω, it lags by nearly 180°. Energy transfer from the driving force is maximum when force and velocity are in phase (at resonance for high-Q systems).

## Explainer

You studied the **driven harmonic oscillator** and saw how a system with its own natural frequency ω₀ responds when driven by an external periodic force at frequency ω. The steady-state response has two key characteristics: an **amplitude** A(ω) telling you how large the oscillations are, and a **phase lag** φ(ω) telling you by how much the oscillator's response trails behind the driving force. Both depend on driving frequency, and their behavior as ω sweeps through ω₀ reveals the underlying physics in a way the formulas alone don't.

Start with amplitude. The formula A(ω) = F₀/√[(k−mω²)² + (bω)²] shows a peak near ω₀ — this is **resonance**. At resonance, the driving force is in sync with the system's natural tendency to oscillate, and energy is transferred most efficiently. For a lightly damped system (small b), the amplitude peak is sharp and tall; for a heavily damped system, the peak is broad and low. The width of the resonance peak is inversely related to the **quality factor** Q = mω₀/b. High Q means sharply resonant — think of a bell, a tuning fork, or a high-quality electrical resonator — while low Q means sluggishly resonant, like a door damper. You will meet Q formally in the builds-toward topic on resonance frequency.

The phase behavior is in some ways more revealing than the amplitude. At low driving frequencies (ω << ω₀), the oscillator has time to follow the driving force almost instantaneously: it moves in phase with the force (φ ≈ 0°). Think of slowly pushing a child on a swing — push when they're moving forward, and they follow your lead. At ω = ω₀, the phase lag is exactly 90°: the oscillator's displacement peaks a quarter-cycle after the driving force peaks. At high driving frequencies (ω >> ω₀), the oscillator can't keep up at all: it lags by nearly 180°, moving almost opposite to the driving force.

The 90° phase shift at resonance is the key to understanding why resonance amplitude is large. Power delivered by any force equals force times velocity. Maximum power transfer occurs when force and velocity are in phase. At resonance, the 90° lag in displacement means that velocity — the time derivative of displacement — is exactly in phase with the driving force. Force and velocity are aligned, so power flows into the system at the maximum possible rate. When damping is small, this sustained power input drives the amplitude to large values. Engineers who design bridges, aircraft wings, and electronic circuits invest heavily in knowing where resonant frequencies lie and what Q values are tolerable — the Tacoma Narrows Bridge collapse is the standard cautionary tale, but the same physics drives vibration fatigue in any rotating machinery subjected to periodic forcing near a structural resonance.
