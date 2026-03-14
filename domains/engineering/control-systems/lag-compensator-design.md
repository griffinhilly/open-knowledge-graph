---
id: lag-compensator-design
title: Lag Compensator Design
domain: engineering
course: control-systems
prerequisites:
- id: lead-lag-compensators
  type: hard
- id: steady-state-error-analysis
  type: hard
tags:
- lag-compensator
- steady-state-error
- low-frequency-gain
- bode-design
- error-constants
stage: advanced
status: draft
---

# Lag Compensator Design

## Core Idea
Lag compensator design improves steady-state accuracy by increasing the low-frequency loop gain without significantly altering the gain crossover frequency or phase margin. The compensator C(s) = K_c · (s + z_c)/(s + p_c) with z_c > p_c (zero farther from origin than pole) provides a gain increase of z_c/p_c = β at frequencies well below z_c while contributing negligible magnitude change near the crossover frequency. The design procedure is: (1) set the gain K_c to meet the transient response specification (desired crossover frequency and phase margin) as if no lag network were present; (2) compute the improvement factor β needed to meet the steady-state error specification (e.g., β = K_v,required/K_v,current for a velocity error constant); (3) place the zero z_c well below the gain crossover frequency (typically one decade or more below ωgc) to avoid contributing negative phase at crossover; (4) set p_c = z_c/β. The lag compensator's negative phase contribution near its corner frequencies is kept harmless by placing both z_c and p_c at low frequencies far from ωgc. The result is improved steady-state performance with minimal impact on the transient response already established by the gain selection.

## How It's Best Learned
Design a lag compensator for a unity-feedback system where the uncompensated gain meets phase margin requirements but the velocity error constant K_v is too low by a factor of 10. Walk through the β calculation, zero/pole placement, and verify on the Bode plot that the phase margin is preserved while the low-frequency gain increases by 20 dB. Compare step and ramp responses before and after compensation to see the steady-state error reduction directly.

## Common Misconceptions
- A lag compensator does not add a pole at the origin and therefore does not change the system type — it increases the error constant (Kp, Kv, or Ka) by a finite factor β, but a Type 0 system remains Type 0 with a finite steady-state error to a step input.
- The lag compensator does contribute negative phase (up to −90° between p_c and z_c), which can erode phase margin if the corner frequencies are placed too close to the gain crossover frequency — the "place it a decade below ωgc" rule is a practical necessity, not a minor detail.
- Lag compensation can slow down the transient response because the closed-loop system acquires a slow pole-zero pair near the origin, producing a long-duration, low-amplitude tail in the step response that can extend the effective settling time.
