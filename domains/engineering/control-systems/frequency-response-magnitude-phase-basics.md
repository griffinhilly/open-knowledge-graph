---
id: frequency-response-magnitude-phase-basics
title: 'Frequency Response: Magnitude and Phase Relationships'
domain: engineering
course: control-systems
prerequisites:
- id: impulse-response-and-convolution-control
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- bode-plot-magnitude-asymptotes-rules
- bode-plot-phase-response-analysis
- gain-phase-margin-stability-measures
- nyquist-stability-from-frequency-response
tags:
- frequency-response
- magnitude
- phase
- jω
stage: advanced
status: validated
---

# Frequency Response: Magnitude and Phase Relationships

## Core Idea
Frequency response G(jω) describes how a system responds to sinusoidal inputs at different frequencies. The magnitude |G(jω)| indicates gain (amplification or attenuation), while ∠G(jω) indicates phase shift. Together, these quantities define stability margins and closed-loop performance.

## Questions

```yaml
- question: "A feedback control system is designed to eliminate errors using negative feedback. At a particular frequency, the open-loop system has accumulated −180° of phase shift and its magnitude is 2 (greater than 1). What will happen to the closed-loop system at this frequency?"
  type: multiple-choice
  options:
    - "The system will be stable — negative feedback always corrects errors regardless of phase"
    - "The system will oscillate and become unstable — the −180° phase shift turns negative feedback into positive feedback, and gain > 1 amplifies the error"
    - "The system will exhibit a steady-state tracking error proportional to the phase lag"
    - "The system will attenuate signals at that frequency, making the closed loop inherently more stable"
  answer: 1
  explanation: "Negative feedback works by feeding back an inverted error signal to correct deviations. But if the system itself introduces −180° of phase shift, the fed-back signal arrives inverted again — turning intended subtraction into addition. At −180° with |G| > 1, the error is fed back amplified and in phase with the disturbance: the system now reinforces errors rather than correcting them. This is the mechanism of instability. Gain margin and phase margin measure how close a system is to this condition. The critical insight: negative feedback is only stabilizing if phase lag remains below 180° where gain exceeds 1."

- question: "A system's transfer function gives |G(jω)| = 0.1 at a particular frequency. What does this mean for a sinusoidal input at that frequency?"
  type: multiple-choice
  options:
    - "The output amplitude is ten times larger than the input — the system amplifies by a factor of 10"
    - "The output amplitude is one-tenth of the input — the system attenuates that frequency by a factor of 10"
    - "The output phase leads the input by 0.1 radians at that frequency"
    - "The system is unstable at that frequency because the gain is non-unity"
  answer: 1
  explanation: "|G(jω)| is the ratio of output amplitude to input amplitude. If |G(jω)| = 0.1, a sinusoidal input of amplitude A produces an output of amplitude 0.1A — attenuation by a factor of 10. In decibels: 20·log₁₀(0.1) = −20 dB. Values greater than 1 mean amplification; values less than 1 mean attenuation; a value of exactly 1 (0 dB) means the amplitude passes through unchanged. Phase information is carried separately by ∠G(jω), not by the magnitude."

- question: "A phase shift of −90° at frequency f represents a real time delay: the output arrives exactly one quarter-period (1/(4f) seconds) after the input."
  type: true-false
  answer: true
  explanation: "Phase shift translates directly into time delay. One full cycle (360°) corresponds to a period of T = 1/f seconds. A −90° shift is 90/360 = 1/4 of a full cycle, corresponding to a time delay of T/4 = 1/(4f) seconds. This is why phase lag is not a cosmetic nuisance — it represents real latency between input and output. In a feedback loop, this delay means the corrective action always arrives late, and accumulated delays (across multiple poles) can push the total lag past −180°, causing instability."

- question: "In a linear time-invariant (LTI) system, a sinusoidal input at frequency ω will generally produce an output containing energy at multiple frequencies — not just ω."
  type: true-false
  answer: false
  explanation: "This is the defining property of linear time-invariant systems: a sinusoidal input at frequency ω always produces a sinusoidal output at the SAME frequency ω. The output may differ in amplitude (scaled by |G(jω)|) and phase (shifted by ∠G(jω)), but no new frequencies are introduced. This is why frequency response analysis works: you can characterize the system's behavior at each frequency independently. Non-linear systems (and linear time-VARIANT systems) can generate outputs at frequencies not present in the input — but that is precisely what 'linear' rules out."

- question: "Explain why accumulated phase lag — rather than the magnitude of the gain — is the primary concern for stability in a negative feedback control system."
  type: short-answer
  answer: "Negative feedback relies on inverting the error signal (a built-in 180° inversion) and subtracting it from the input to reduce error. If the system accumulates additional phase lag in the loop, the fed-back signal arrives with a different phase relationship to the input. At exactly −180° of additional lag (total −360°, which is equivalent to 0°), the inversion disappears and the loop acts as positive feedback. If the gain at that frequency is greater than 1, any disturbance is amplified each time around the loop, causing oscillation or divergence. This is why the phase margin (how many degrees short of −180° the phase is at unity gain) is the critical stability measure — the magnitude can be reduced (gain margin), but phase lag from dynamics is harder to compensate."
  explanation: "This is why phase-lag compensators and lead compensators exist: a lead compensator adds positive phase shift at the crossover frequency to increase the phase margin. Pure gain changes cannot fix a phase problem — they change where unity gain occurs on the frequency axis but do not change the fundamental phase relationship at that point."
```

## Explainer

From your study of impulse response and convolution, you know that a linear system's time-domain output is the convolution of the input with the impulse response h(t). The **frequency response** G(jω) is the Fourier transform of h(t) — it tells you exactly the same information, but organized by frequency instead of by time. The key insight: a sinusoidal input A·sin(ωt) always produces a sinusoidal output at the same frequency ω, but with a different amplitude and a shifted phase. G(jω) captures both changes. This is the defining property of linear time-invariant systems, and it makes frequency-domain analysis the natural language for understanding how systems filter, delay, and distort signals.

The **magnitude** |G(jω)| is the ratio of output amplitude to input amplitude at frequency ω. If |G(jω)| = 3 at some frequency, a sinusoid at that frequency is amplified threefold. If |G(jω)| = 0.1, the system attenuates that frequency by a factor of ten. Magnitude greater than one means amplification; less than one means attenuation. When plotted in decibels — 20·log₁₀(|G|) — a magnitude of 1 becomes 0 dB, attenuation to half becomes −6 dB, and tenfold amplification becomes +20 dB. The decibel scale converts multiplicative effects into additive ones, which makes cascaded systems easy to analyze: just add the dB gains of each stage.

The **phase** ∠G(jω) is the angle by which the output sinusoid lags behind the input. If ∠G(jω) = −90° at some frequency, the output is a quarter-cycle behind the input. Phase shift is not just a curiosity — it represents real time delay. A −90° shift at frequency f means the output lags by a time t = (90°/360°) · (1/f) = 1/(4f). Accumulated phase lag is the primary mechanism by which feedback systems become unstable: if a system intended as negative feedback accumulates −180° of phase at the frequency where its gain is still high, the fed-back signal arrives inverted and amplified, driving the system into oscillation.

Evaluating G(jω) is straightforward from the transfer function G(s): substitute s = jω and compute the resulting complex number at each frequency of interest. If G(s) = 1/(s + a), then G(jω) = 1/(jω + a), which has magnitude 1/√(ω² + a²) and phase −arctan(ω/a). These expressions reveal the system's behavior across all frequencies at once — no simulation needed. As you move toward Bode plots and stability analysis, you'll use these magnitude and phase expressions to build asymptotic approximations, read off stability margins, and design compensators that reshape the frequency response to meet performance specifications.
