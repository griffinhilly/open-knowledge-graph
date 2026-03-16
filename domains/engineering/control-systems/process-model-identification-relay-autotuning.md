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
stage: abstract-reasoning
status: draft
---

# Process Model Identification and Relay Autotuning

## Core Idea
Relay feedback autotuning applies a relay controller to excite the process at its critical frequency (phase = −180°) without requiring an explicit plant model. Amplitude and frequency of resulting oscillation directly give the critical frequency and magnitude for PID tuning.

## Explainer

Traditional PID tuning methods like Ziegler-Nichols require knowing the process's **ultimate gain** (K_u) and **ultimate period** (T_u) — the gain at which the system marginally oscillates and the period of those oscillations. The classical way to find these was to close the loop with a proportional controller, increase gain manually until the system just begins to oscillate, and record the results. This was dangerous (the plant oscillates at full amplitude), operator-dependent, and impractical for automated commissioning. Relay autotuning, developed by Åström and Hägglund in 1984, automates this experiment safely.

The key insight comes from your prerequisite on sinusoidal frequency response. A linear system oscillates sustainably at the frequency where two conditions are simultaneously met: the loop gain equals 1 and the loop phase equals −180°. The −180° condition is the **phase crossover frequency** — it's where the process inverts the signal. A **relay** (also called a bang-bang controller) exploits this by design: it switches its output to +d when the process output is below setpoint and to −d when above. This forced switching naturally drives the system to oscillate at the phase crossover frequency, because that is the only frequency at which the relay's square-wave output can sustain a sinusoidal oscillation in the plant.

Once the relay is connected, the closed-loop system enters a **limit cycle**: a sustained, bounded oscillation. You measure two things from this oscillation — the period T_u (giving ω_u = 2π/T_u, the ultimate frequency) and the amplitude a of the process output oscillation. The relay output has magnitude d (a square wave switching between ±d). Using the **describing function** approximation — which represents the relay's nonlinear switching as if it were a linear gain at the fundamental frequency — the effective gain of the relay at amplitude a is 4d/(πa). At the limit cycle, this gain times the process gain equals 1, giving the **ultimate gain**: K_u = 4d/(πa). These two numbers, K_u and T_u, are exactly what Ziegler-Nichols requires to compute PID gains.

The safety advantage is decisive for industrial use. The relay limits the excitation: the process output oscillates by approximately ±a, and the process input never exceeds ±d. You choose d as a small fraction of the control range, so the plant barely moves. Compare this to open-loop step tests (large setpoint changes, operator attention required) or manual gain increase (risk of instability). The relay test runs in about one to three oscillation cycles, typically takes minutes, and can run unattended. This is why the "autotune" button on commercial PID controllers — from Honeywell, Siemens, and ABB to simple temperature controllers — implements relay autotuning. When you press it, the controller disconnects the PID, connects a relay, waits for two stable oscillation cycles, computes K_u and T_u, applies a tuning formula, and hands control back to the PID.

The main limitation is the describing function approximation: it assumes the process responds primarily to the fundamental harmonic of the relay's square wave and ignores higher harmonics. For processes with strong nonlinearities, the identified parameters can be inaccurate. Practical enhancements include adding hysteresis to the relay (reducing sensitivity to measurement noise), using asymmetric relays to handle integrating processes, or running multiple relay experiments at different amplitudes to detect nonlinearity. But for the typical industrial process — moderately nonlinear, with a dominant first- or second-order response plus dead time — the basic relay test delivers tuning parameters close enough to serve as an excellent starting point for manual refinement.
