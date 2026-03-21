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

## Questions

```yaml
- question: "An engineer wants to maximize the power delivered by a periodic driving force to a mechanical oscillator. At what condition is power transfer maximized?"
  type: multiple-choice
  options:
    - "When the driving force and the oscillator's displacement are in phase (φ = 0°)"
    - "When the driving force and the oscillator's velocity are in phase, which occurs when displacement lags force by 90°"
    - "When the driving force and the oscillator's velocity are 180° out of phase"
    - "When the driving frequency ω is much higher than the natural frequency ω₀"
  answer: 1
  explanation: "Power delivered by a force equals force times velocity (P = F·v). This is maximized when force and velocity are in phase — they point in the same direction simultaneously. At resonance (ω = ω₀), displacement lags the driving force by 90°. Since velocity is the time derivative of displacement, a 90° lag in displacement means velocity is exactly in phase with force. This is why resonance maximizes power input: not because of any special alignment of force and displacement, but because the 90° lag in displacement produces a 0° lag between force and velocity. Option A (force and displacement in phase) would mean velocity leads force by 90°, which actually minimizes power transfer."

- question: "What happens to the phase lag between driving force and oscillator displacement as the driving frequency increases from far below to far above the natural frequency ω₀?"
  type: multiple-choice
  options:
    - "Phase lag stays near 0° throughout, since the oscillator tracks the force at all frequencies"
    - "Phase lag stays near 90° throughout, since resonance dominates the response"
    - "Phase lag increases continuously from near 0° at low frequencies to near 180° at high frequencies, passing through exactly 90° at resonance"
    - "Phase lag jumps abruptly from 0° to 180° at the resonant frequency"
  answer: 2
  explanation: "The phase behavior sweeps continuously: at low driving frequencies (ω << ω₀), the oscillator has time to follow the force nearly instantaneously, so φ ≈ 0°. At ω = ω₀, the lag is exactly 90°. At high driving frequencies (ω >> ω₀), the oscillator cannot keep up and lags by nearly 180° — moving almost opposite to the driving force. This continuous sweep from 0° to 180° is a universal feature of driven oscillators and is more diagnostically useful than the amplitude curve alone for identifying resonance."

- question: "The 90° phase lag at resonance is directly responsible for large oscillation amplitudes, because it brings the oscillator's velocity into phase with the driving force and maximizes the rate of energy input."
  type: true-false
  answer: true
  explanation: "This is the mechanistic explanation for why resonance produces large amplitude. Power = F·v is maximized when force and velocity are in phase. At resonance, the 90° displacement lag means velocity is in phase with force (since v = dx/dt, and differentiating a cosine delayed by 90° gives a sine, which aligns with the cosine driving force). Sustained maximum power input drives the amplitude to its peak, limited only by damping. Without this phase relationship, the energy input would be partially cancelled each cycle."

- question: "At very low driving frequencies (ω << ω₀), the oscillator significantly lags behind the driving force because its inertia prevents it from responding to slow oscillations."
  type: true-false
  answer: false
  explanation: "At low driving frequencies, the opposite is true: the oscillator has plenty of time to follow each slow oscillation of the driving force and responds nearly in phase (φ ≈ 0°). Inertia matters at high frequencies, where the oscillator cannot accelerate fast enough to keep up with rapid direction changes — that is when the phase lag approaches 180°. The intuition is like slowly pushing a child on a swing: if you push gently and slowly, they follow your lead easily. It is the fast-oscillation case where lag becomes large."

- question: "Explain, using the relationship between force, velocity, and power, why the 90° phase lag at resonance causes the oscillator's amplitude to grow large."
  type: short-answer
  answer: "The time-averaged power delivered to an oscillator is ⟨P⟩ = (F₀Aω/2)sin(φ), where φ is the phase lag between the driving force and displacement. This is maximized when sin(φ) = 1, i.e., φ = 90°. At resonance, displacement lags the driving force by exactly 90°, which means velocity — the time derivative of displacement — is exactly in phase with the force. Force and velocity pointing in the same direction at every instant means the driving force always does positive work on the oscillator. This sustained maximum power input drives the amplitude to its resonant peak, limited only by the rate at which damping dissipates energy."
  explanation: "The 90° phase lag is not just a coincidental feature of resonance — it is the mechanism that makes resonance energetically special. At any other phase lag, sin(φ) < 1, meaning some fraction of the driving force's work is cancelled each cycle. Only at φ = 90° is every joule of work done by the driving force pumped into the oscillator. For lightly damped systems, this produces very large amplitudes before a steady state is reached between energy input and dissipation."
```

## Explainer

You studied the **driven harmonic oscillator** and saw how a system with its own natural frequency ω₀ responds when driven by an external periodic force at frequency ω. The steady-state response has two key characteristics: an **amplitude** A(ω) telling you how large the oscillations are, and a **phase lag** φ(ω) telling you by how much the oscillator's response trails behind the driving force. Both depend on driving frequency, and their behavior as ω sweeps through ω₀ reveals the underlying physics in a way the formulas alone don't.

Start with amplitude. The formula A(ω) = F₀/√[(k−mω²)² + (bω)²] shows a peak near ω₀ — this is **resonance**. At resonance, the driving force is in sync with the system's natural tendency to oscillate, and energy is transferred most efficiently. For a lightly damped system (small b), the amplitude peak is sharp and tall; for a heavily damped system, the peak is broad and low. The width of the resonance peak is inversely related to the **quality factor** Q = mω₀/b. High Q means sharply resonant — think of a bell, a tuning fork, or a high-quality electrical resonator — while low Q means sluggishly resonant, like a door damper. You will meet Q formally in the builds-toward topic on resonance frequency.

The phase behavior is in some ways more revealing than the amplitude. At low driving frequencies (ω << ω₀), the oscillator has time to follow the driving force almost instantaneously: it moves in phase with the force (φ ≈ 0°). Think of slowly pushing a child on a swing — push when they're moving forward, and they follow your lead. At ω = ω₀, the phase lag is exactly 90°: the oscillator's displacement peaks a quarter-cycle after the driving force peaks. At high driving frequencies (ω >> ω₀), the oscillator can't keep up at all: it lags by nearly 180°, moving almost opposite to the driving force.

The 90° phase shift at resonance is the key to understanding why resonance amplitude is large. Power delivered by any force equals force times velocity. Maximum power transfer occurs when force and velocity are in phase. At resonance, the 90° lag in displacement means that velocity — the time derivative of displacement — is exactly in phase with the driving force. Force and velocity are aligned, so power flows into the system at the maximum possible rate. When damping is small, this sustained power input drives the amplitude to large values. Engineers who design bridges, aircraft wings, and electronic circuits invest heavily in knowing where resonant frequencies lie and what Q values are tolerable — the Tacoma Narrows Bridge collapse is the standard cautionary tale, but the same physics drives vibration fatigue in any rotating machinery subjected to periodic forcing near a structural resonance.
