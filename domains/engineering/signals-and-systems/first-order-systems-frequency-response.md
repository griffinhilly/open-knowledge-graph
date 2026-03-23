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
stage: expert
status: validated
---

# First-Order Systems and Frequency Response

## Core Idea
First-order systems H(s) = ω_n/(s + ω_n) have a single pole at s = -ω_n. Time-domain response includes exponential approach to steady state with time constant τ = 1/ω_n. Frequency response has -20 dB/decade rolloff above the corner frequency ω_n; -45° phase shift at ω_n.

## Questions

```yaml
- question: "You apply a sinusoidal input at exactly the corner frequency ω_n to a first-order low-pass system. What do you observe in the steady-state output?"
  type: multiple-choice
  options:
    - "The output amplitude is the same as the input and there is no phase shift — the corner frequency is where the system passes signals without distortion"
    - "The output amplitude is 1/√2 times the input amplitude (−3 dB) and lags the input by exactly 45°"
    - "The output amplitude is zero because the corner frequency is the cutoff where the system stops passing signals"
    - "The output amplitude is half the input (−6 dB) and lags by 90°"
  answer: 1
  explanation: "At ω = ω_n, the magnitude is |H(jω_n)| = ω_n/√(ω_n² + ω_n²) = 1/√2 ≈ 0.707, which is −3 dB. The phase is −arctan(ω_n/ω_n) = −arctan(1) = −45°. These two values — −3 dB magnitude and −45° phase — are the defining characteristics of the corner frequency in a first-order system. The −45° phase measurement is particularly useful diagnostically: apply a sinusoid, sweep frequency until you observe exactly 45° lag, and you have located the pole. Option A describes DC behavior (ω << ω_n). Option C is wrong — the first-order system asymptotically approaches zero at high frequency but never reaches it at the corner. Option D describes the high-frequency asymptote, not the corner."

- question: "A first-order system's pole is moved from s = −10 to s = −100 rad/s (farther from the origin). How does the step response change?"
  type: multiple-choice
  options:
    - "The system responds more slowly because moving the pole farther left increases the time constant"
    - "The system responds faster because ω_n = 100 > 10, meaning τ = 1/100 = 10 ms is shorter than τ = 1/10 = 100 ms"
    - "The step response shape changes but the settling time remains the same because it depends only on damping"
    - "The system becomes unstable because poles in the left half-plane always cause instability when moved farther from the origin"
  answer: 1
  explanation: "The pole at s = −ω_n means τ = 1/ω_n. Moving the pole from −10 to −100 increases ω_n from 10 to 100, which *decreases* the time constant from τ = 0.1 s to τ = 0.01 s. The system becomes faster: it reaches 63% of its final value in 10 ms instead of 100 ms. The geometric interpretation is that distance from the origin equals ω_n equals 1/τ — farther left means faster. Option A reverses this relationship. Option C conflates second-order damping concepts with first-order behavior (first-order systems have no damping ratio). Option D is incorrect — left-half-plane poles indicate stability."

- question: "The time constant τ and the corner frequency ω_n of a first-order system carry independent information — knowing one does not tell you the other."
  type: true-false
  answer: false
  explanation: "Time constant and corner frequency are reciprocals of each other: τ = 1/ω_n, equivalently ω_n = 1/τ. They are two descriptions of exactly the same physical fact — the location of the single pole. Knowing the time constant from a step response (the time to reach 63% of steady state) immediately gives you the corner frequency (where the magnitude is −3 dB and the phase is −45°), and vice versa. First-order systems have only one degree of freedom in their dynamics: the single pole location. Every characterization — time constant, corner frequency, pole location, 63% rise time, −3 dB frequency, −45° phase frequency, −20 dB/decade rolloff onset — is a different perspective on that one number."

- question: "At frequencies well above the corner frequency ω_n, a first-order low-pass system's output magnitude continues to decrease at exactly −20 dB per decade indefinitely."
  type: true-false
  answer: true
  explanation: "For ω >> ω_n, the magnitude simplifies to |H(jω)| ≈ ω_n/ω, which decreases as 1/ω — exactly −20 dB per decade (a factor of 10 decrease in magnitude for every decade increase in frequency). This is the asymptotic behavior of a single-pole system. It holds indefinitely in the ideal first-order model; in physical systems, additional poles at higher frequencies eventually change the rolloff slope. The −20 dB/decade slope is the frequency-domain signature of a single real pole, just as the −3 dB point identifies the corner and the −45° phase identifies ω_n."

- question: "A technician measures the step response of an unknown first-order system and finds it reaches 63% of its final value after 5 ms. What can you determine about the system's frequency response without any additional measurements?"
  type: short-answer
  answer: "The 63% rise time in a first-order step response equals the time constant τ. Therefore τ = 5 ms = 0.005 s. Since ω_n = 1/τ, the pole is at s = −200 rad/s and the corner frequency is ω_n = 200 rad/s (approximately 31.8 Hz). The magnitude response will be flat (0 dB) for frequencies well below 200 rad/s, will be −3 dB at exactly 200 rad/s, will have a −45° phase shift at 200 rad/s, and will roll off at −20 dB/decade above 200 rad/s. At any frequency ω, the magnitude is 200/√(ω² + 200²) and the phase is −arctan(ω/200)."
  explanation: "This is the key insight about first-order systems: the single pole characterization is complete. One measurement (the 63% rise time) determines the time constant, which determines the pole location, which fully specifies every time-domain and frequency-domain characteristic. There is no additional information to uncover — the system has only one degree of freedom. This is why mastering the first-order case is foundational: it demonstrates the deep unity between time-domain and frequency-domain representations."
```

## Explainer

A first-order system is the simplest dynamic system that responds to changes over time — one energy storage element, one pole, one time constant. Physical examples are everywhere: an RC circuit charging a capacitor, a thermometer reaching thermal equilibrium, a damper resisting velocity, a liquid level in a tank with a drain. You already know from transfer function theory that a pole at s = −ω_n means the system's natural response is e^(−ω_n t) — a decaying exponential. The **time constant** τ = 1/ω_n is the single number that characterizes how fast: after one time constant, the response has reached 63% of its final value; after five time constants, it is effectively at steady state (99.3%).

The step response is the most intuitive window into first-order behavior. Apply a unit step input and the output rises as y(t) = 1 − e^(−t/τ). The initial slope of this curve at t = 0 equals 1/τ — the steeper the initial rise, the faster the system. A fast system (small τ, large ω_n, pole far left in the complex plane) tracks the input almost immediately. A slow system (large τ, pole close to the origin) responds sluggishly. The pole location on the negative real axis is the geometric representation of this speed: distance from the origin equals ω_n equals 1/τ.

Now evaluate the same transfer function on the imaginary axis by substituting s = jω to get H(jω). The **magnitude** is |H(jω)| = ω_n / √(ω² + ω_n²). At low frequencies ω << ω_n, the denominator is dominated by ω_n, and |H| ≈ 1 (0 dB) — signals pass through unattenuated. At high frequencies ω >> ω_n, the denominator grows as ω and |H| ≈ ω_n/ω — magnitude falls at −20 dB per decade, or a factor of 10 for every decade increase in frequency. The **corner frequency** ω_n (or equivalently f_n = ω_n/2π) is the transition point where magnitude is exactly 1/√2 = −3 dB. The **phase** of H(jω) is −arctan(ω/ω_n), starting at 0° at DC and approaching −90° at very high frequencies, with exactly −45° at ω = ω_n. This −45° at the corner frequency is a diagnostic: if you apply a sinusoid at the corner frequency and measure 45° phase lag in the output, you have measured the pole location directly.

Together, the time-domain picture (time constant, exponential approach) and frequency-domain picture (−3 dB corner, −20 dB/decade rolloff, −45° phase at corner) are two faces of the same fact: the single pole at s = −ω_n. Every parameter is interchangeable — measure any one and you know all the others. First-order systems are also the building block from which more complex systems are assembled: a cascade of two first-order sections gives a second-order system with a pair of poles; a feedback loop around a first-order plant creates a new first-order closed-loop system with a different pole location. Mastering this single-pole case thoroughly makes every more complex system easier to decompose and understand.
