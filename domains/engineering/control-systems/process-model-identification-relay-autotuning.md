---
id: process-model-identification-relay-autotuning
title: Process Model Identification and Relay Autotuning
domain: engineering
course: control-systems
prerequisites:
- id: pid-tuning-methods
  type: hard
- id: sinusoidal-response-magnitude-phase-angle
  type: soft
builds-toward:
- practical-control-system-implementation
tags:
- system-identification
- relay-feedback
- autotuning
- critical-frequency
- model-estimation
stage: expert
status: draft
---

# Process Model Identification and Relay Autotuning

## Core Idea
Relay feedback autotuning applies a relay controller to excite the process at its critical frequency (phase = −180°) without requiring an explicit plant model. Amplitude and frequency of resulting oscillation directly give the critical frequency and magnitude for PID tuning.

## Questions

```yaml
- question: "In a relay autotuning test, the relay switches between ±d and the resulting process output oscillates with amplitude a. Using the describing function approximation, what is the ultimate gain K_u?"
  type: multiple-choice
  options:
    - "K_u = πa / (4d)"
    - "K_u = 4d / (πa)"
    - "K_u = d / a"
    - "K_u = 2d / a"
  answer: 1
  explanation: "The describing function of a relay with amplitude d, evaluated at oscillation amplitude a, gives an effective gain of 4d/(πa). At the limit cycle, the loop gain equals 1: this relay gain times the process gain at the critical frequency must equal 1. Solving for the process gain (which is K_u) gives K_u = 4d/(πa). The factor of π comes from the Fourier series of a square wave — the fundamental harmonic has amplitude 4/π times the relay amplitude."

- question: "Why does a relay feedback system naturally oscillate at the phase crossover frequency (the frequency where the open-loop phase is −180°), rather than at some other frequency?"
  type: multiple-choice
  options:
    - "The relay is tuned in advance to that frequency based on a process model"
    - "The phase crossover frequency is where the process gain is highest, so oscillations grow largest there"
    - "Sustained oscillation requires loop gain = 1 and loop phase = −180°; the relay automatically satisfies the phase condition, so the system settles at the only frequency where both conditions hold"
    - "The relay's switching speed is physically matched to the natural frequency of the process"
  answer: 2
  explanation: "A sustained limit cycle requires two simultaneous conditions: loop gain = 1 and loop phase = −180°. The relay is a sign-inverting nonlinear element — its switching behavior introduces an effective −180° phase inversion (like a sign flip in feedback). A sinusoidal oscillation can persist only at the frequency where the process itself also contributes −180° of phase, making the total loop phase −360° (≡ 0°) or equivalently where the process phase is −180°. At any other frequency, the phase relationship causes the oscillation to die out or grow; only the phase crossover frequency supports a stable limit cycle."

- question: "The relay autotuning test is safer than finding the ultimate gain by manually increasing proportional gain because the relay limits the amplitude of the process excitation."
  type: true-false
  answer: true
  explanation: "This is the key practical advantage. In the classical Ziegler-Nichols closed-loop method, the operator increases proportional gain until the system marginally oscillates — the process can swing widely during this experiment, and the operator must intervene quickly if instability develops. In contrast, the relay limits the controller output to ±d (a designer-chosen fraction of the control range), so the process output oscillates by approximately ±a. The test runs in a few oscillation cycles, often unattended, with predictable and bounded excitation — which is why commercial PID controllers implement it as a push-button 'autotune' feature."

- question: "Relay autotuning requires an explicit mathematical model of the process (transfer function or state-space) to determine the critical frequency before the experiment begins."
  type: true-false
  answer: false
  explanation: "This is precisely what relay autotuning avoids. Traditional PID tuning using Ziegler-Nichols requires knowing K_u and T_u — which requires either an explicit model or a dangerous manual gain-increase experiment. Relay autotuning determines these parameters from the limit cycle itself: the period of oscillation gives T_u (and hence ω_u), and the oscillation amplitude combined with the relay amplitude gives K_u via the describing function. No prior model is needed, which is the key advantage for automated commissioning of industrial controllers."

- question: "What is the 'describing function' approximation in the context of relay autotuning, and why is it necessary for the analysis?"
  type: short-answer
  answer: "The describing function is a method for approximately analyzing nonlinear elements (like a relay) in frequency-domain terms. A relay is nonlinear — its output is a square wave, not a sinusoid — so standard linear frequency-response analysis cannot be directly applied. The describing function approximates the relay as an equivalent linear gain at the fundamental frequency of its output, equal to 4d/(πa) where d is the relay amplitude and a is the amplitude of the input sinusoid. This approximation is valid when the process acts as a low-pass filter that attenuates higher harmonics of the square wave, leaving primarily the fundamental frequency in the output. The approximation enables us to use linear analysis (the condition loop gain = 1 at phase crossover) to relate the observable oscillation parameters to K_u."
  explanation: "The describing function is the mathematical bridge that allows the nonlinear relay to be handled with linear tools. Its limitation is that it assumes higher harmonics are negligible — if the process passes harmonics significantly, the identified K_u and T_u will be inaccurate. For most industrial processes (which are low-pass in nature), this assumption holds well enough for practical PID tuning."
```

## Explainer

Traditional PID tuning methods like Ziegler-Nichols require knowing the process's **ultimate gain** (K_u) and **ultimate period** (T_u) — the gain at which the system marginally oscillates and the period of those oscillations. The classical way to find these was to close the loop with a proportional controller, increase gain manually until the system just begins to oscillate, and record the results. This was dangerous (the plant oscillates at full amplitude), operator-dependent, and impractical for automated commissioning. Relay autotuning, developed by Åström and Hägglund in 1984, automates this experiment safely.

The key insight comes from your prerequisite on sinusoidal frequency response. A linear system oscillates sustainably at the frequency where two conditions are simultaneously met: the loop gain equals 1 and the loop phase equals −180°. The −180° condition is the **phase crossover frequency** — it's where the process inverts the signal. A **relay** (also called a bang-bang controller) exploits this by design: it switches its output to +d when the process output is below setpoint and to −d when above. This forced switching naturally drives the system to oscillate at the phase crossover frequency, because that is the only frequency at which the relay's square-wave output can sustain a sinusoidal oscillation in the plant.

Once the relay is connected, the closed-loop system enters a **limit cycle**: a sustained, bounded oscillation. You measure two things from this oscillation — the period T_u (giving ω_u = 2π/T_u, the ultimate frequency) and the amplitude a of the process output oscillation. The relay output has magnitude d (a square wave switching between ±d). Using the **describing function** approximation — which represents the relay's nonlinear switching as if it were a linear gain at the fundamental frequency — the effective gain of the relay at amplitude a is 4d/(πa). At the limit cycle, this gain times the process gain equals 1, giving the **ultimate gain**: K_u = 4d/(πa). These two numbers, K_u and T_u, are exactly what Ziegler-Nichols requires to compute PID gains.

The safety advantage is decisive for industrial use. The relay limits the excitation: the process output oscillates by approximately ±a, and the process input never exceeds ±d. You choose d as a small fraction of the control range, so the plant barely moves. Compare this to open-loop step tests (large setpoint changes, operator attention required) or manual gain increase (risk of instability). The relay test runs in about one to three oscillation cycles, typically takes minutes, and can run unattended. This is why the "autotune" button on commercial PID controllers — from Honeywell, Siemens, and ABB to simple temperature controllers — implements relay autotuning. When you press it, the controller disconnects the PID, connects a relay, waits for two stable oscillation cycles, computes K_u and T_u, applies a tuning formula, and hands control back to the PID.

The main limitation is the describing function approximation: it assumes the process responds primarily to the fundamental harmonic of the relay's square wave and ignores higher harmonics. For processes with strong nonlinearities, the identified parameters can be inaccurate. Practical enhancements include adding hysteresis to the relay (reducing sensitivity to measurement noise), using asymmetric relays to handle integrating processes, or running multiple relay experiments at different amplitudes to detect nonlinearity. But for the typical industrial process — moderately nonlinear, with a dominant first- or second-order response plus dead time — the basic relay test delivers tuning parameters close enough to serve as an excellent starting point for manual refinement.
