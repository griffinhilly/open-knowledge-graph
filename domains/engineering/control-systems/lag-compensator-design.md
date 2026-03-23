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
stage: expert
status: validated
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

## Questions

```yaml
- question: "A system has adequate phase margin but Kv = 2, and you need Kv = 20. You place a lag compensator with zero at z_c = 1 rad/s and pole at p_c = 0.1 rad/s, with ωgc = 10 rad/s. What primarily determines that the phase margin is preserved?"
  type: multiple-choice
  options:
    - "The gain K_c is chosen to be exactly 1, contributing no gain at crossover"
    - "The zero and pole are placed one decade below ωgc, so the phase dip occurs far below the crossover frequency"
    - "The compensator adds a pole at the origin, increasing low-frequency gain without affecting phase"
    - "The lag compensator adds positive phase near crossover, offsetting any reduction from other factors"
  answer: 1
  explanation: "The negative phase contribution of a lag compensator (up to −90°) occurs between its pole p_c and zero z_c frequencies. By placing both well below ωgc (the rule of thumb is z_c ≤ ωgc/10), the phase dip peaks at the geometric mean of p_c and z_c — far from the crossover region. At ωgc itself, the compensator's phase contribution is small (roughly −6° or less), leaving the phase margin nearly intact. If z_c were placed near ωgc, the negative phase dip would directly erode the phase margin you designed."

- question: "An engineer places a lag compensator with z_c = ωgc/2 instead of the recommended ωgc/10. Compared to correct placement, what is the primary consequence?"
  type: multiple-choice
  options:
    - "The low-frequency gain boost β is reduced by a factor of 5"
    - "The system type increases by one, eliminating steady-state error to ramp inputs"
    - "The negative phase contribution at ωgc is significantly larger, eroding the designed phase margin"
    - "The compensator has no effect because the zero is still below the crossover frequency"
  answer: 2
  explanation: "Phase margin erosion is the primary danger of incorrect lag compensator placement. With z_c = ωgc/2, the geometric mean of p_c and z_c is √(p_c · z_c) = √(z_c/β · z_c) = z_c/√β — now potentially close to ωgc. The lag network's phase dip, which can reach −90°, occurs in this range. Even if the dip peak is still somewhat below ωgc, the phase at the crossover frequency is now substantially negative, potentially reducing phase margin by 20–40°. This can destabilize a system designed with tight margins."

- question: "A lag compensator adds a pole at the origin to the open-loop transfer function, changing the system type and enabling zero steady-state error to step inputs."
  type: true-false
  answer: false
  explanation: "A lag compensator C(s) = K_c(s + z_c)/(s + p_c) has a pole at s = −p_c, not at the origin (s = 0). The system type — determined by the number of open-loop poles at the origin — is unchanged. A lag compensator improves steady-state accuracy by multiplying the error constant (Kp, Kv, or Ka) by the finite factor β = z_c/p_c, not by adding an integrator. A Type 0 system with a lag compensator still has finite steady-state error to a step input — the error is simply smaller by factor β. Adding a pure integrator (pole at origin) would change system type and is an entirely different design choice."

- question: "A lag compensator increases the velocity error constant Kv by the ratio z_c/p_c = β, which reduces steady-state ramp tracking error by the same factor."
  type: true-false
  answer: true
  explanation: "For a unity-feedback system, Kv = lim(s→0) s·G(s)C(s). The lag compensator at DC (s→0) contributes z_c/p_c = β to this limit, multiplying Kv by β. Since steady-state ramp error = 1/Kv (for a Type 1 system), a β-fold increase in Kv produces a β-fold reduction in steady-state error. This is the compensator's purpose: if the uncompensated system gives Kv = 2 and you need Kv = 20, set β = 10 and design z_c and p_c accordingly. The gain improvement at DC is exactly the ratio of the zero and pole distances from the origin."

- question: "Explain why a lag compensator's zero and pole must be placed well below the gain crossover frequency, and what goes wrong if they are placed too close to it."
  type: short-answer
  answer: "Between its pole p_c and zero z_c, a lag compensator contributes negative phase — up to −90° at the geometric mean. If z_c is near ωgc, this phase dip occurs in the crossover region and erodes the phase margin that was carefully designed to give the desired transient response. The rule of placing z_c at least a decade below ωgc (z_c ≤ ωgc/10) ensures the phase dip peaks far below crossover, contributing only a few degrees of negative phase at ωgc. The low-frequency gain boost β is unaffected by placement — it is determined by z_c/p_c regardless of where in the frequency spectrum those frequencies fall."
  explanation: "This placement rule is the central practical discipline of lag compensator design. A common error is treating the lag compensator as a pure gain boost and ignoring its phase contribution. But every real compensator has both magnitude and phase responses. The 'free lunch' of increased low-frequency gain without reduced phase margin is only available when placement is correct. The slow pole-zero pair near the origin also introduces a long-duration tail in the step response — acceptable in most applications but worth verifying."
```

## Explainer

The fundamental challenge the lag compensator addresses is this: you have already chosen a gain K that places the gain crossover frequency at the desired location, giving you the phase margin (and therefore the transient response) you want. But when you compute the steady-state error, you find that the error constant (Kv for ramp inputs, Kp for step inputs) is too small by a factor β — the system tracks accurately enough in speed, but not precisely enough in steady-state. You need more low-frequency gain without disturbing the crossover region. That is exactly what a lag compensator provides.

The compensator C(s) = K_c · (s + z_c)/(s + p_c) with z_c > p_c has a simple frequency-domain interpretation. At frequencies well below both corner frequencies (ω ≪ p_c < z_c), the numerator and denominator both contribute approximately their DC values, and the **DC gain** of the compensator is z_c/p_c = β > 1. At frequencies well above both corner frequencies (ω ≫ z_c > p_c), numerator and denominator magnitudes cancel and the gain returns to 1. So the lag compensator is essentially a low-frequency gain booster: it multiplies the loop gain by β at DC and low frequencies, where steady-state accuracy is determined, while leaving the high-frequency Bode plot (including the crossover region) nearly unchanged.

The catch is that between the two corner frequencies, the phase response dips negative — up to -90° at the geometric mean of p_c and z_c. This is why **placement matters so much**: if z_c is close to the gain crossover frequency ωgc, that negative phase dip erodes the phase margin you carefully designed. The rule of thumb — place z_c at least one decade below ωgc, i.e., z_c ≤ ωgc/10 — ensures the phase contribution at crossover is small (roughly -6° or less). Then set p_c = z_c/β to achieve the target gain improvement.

Concretely: suppose you need Kv = 20 but the uncompensated system delivers Kv = 2 at the desired crossover frequency. You need β = 10 (a 20 dB low-frequency gain boost). If ωgc = 10 rad/s, place z_c = 1 rad/s and p_c = 0.1 rad/s. The compensator C(s) = (s + 1)/(s + 0.1) multiplies the low-frequency open-loop gain by 10, raises Kv from 2 to 20, and contributes only a small phase dip near ω = 0.3 rad/s — far from the crossover at 10 rad/s. Check the result on the Bode plot: the magnitude is shifted up 20 dB at low frequencies, the phase margin at ωgc is nearly unchanged, and the ramp tracking error has decreased by a factor of 10. The tradeoff is a slow pole-zero pair near the origin that can produce a long, low-amplitude transient tail — acceptable for most applications, but worth checking in the step response.
