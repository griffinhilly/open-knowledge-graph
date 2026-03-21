---
id: feedback-control-and-stability
title: Feedback Control Systems and Stability Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: frequency-response-analysis-bode
  type: hard
builds-toward:
- feedback-control-fundamentals
tags:
- feedback
- control-systems
- stability
stage: advanced
status: draft
---

# Feedback Control Systems and Stability Analysis

## Core Idea
Feedback modifies circuit behavior by returning a portion of the output to the input. Loop gain T(jω) = β·A(jω) (feedback fraction times forward gain) determines closed-loop behavior. Negative feedback reduces gain but improves linearity, bandwidth, and noise; positive feedback increases gain or causes oscillation if |T| ≥ 1. Stability requires |T(jω)| < 1 at frequencies where the phase of T crosses -180°.

## Questions

```yaml
- question: "A feedback amplifier's Bode plot shows |T(jω)| = 3 (about 10 dB) at the frequency where the loop phase equals −180°. What will this circuit do?"
  type: multiple-choice
  options:
    - "Operate normally with slightly reduced gain"
    - "Oscillate, because positive feedback with loop gain ≥ 1 at the −180° crossing is unstable"
    - "Saturate once, then settle to a stable DC output"
    - "Become stable at higher frequencies where gain rolls off"
  answer: 1
  explanation: "When the phase shift around the loop reaches −180°, the feedback that was negative (subtracting from the input) has become positive (adding to it). If the loop gain magnitude |T| is ≥ 1 at this frequency, the self-reinforcing loop satisfies the Barkhausen criterion for oscillation. A loop gain of 3 at the −180° crossing means the circuit has a large negative gain margin — it is far past the stability boundary and will oscillate. Option C (settling to DC) might occur in a nonlinear circuit, but from a linear stability analysis, the circuit is unstable."

- question: "Increasing the feedback fraction β in a negative feedback amplifier reduces the closed-loop gain but makes the circuit more stable and predictable."
  type: true-false
  answer: true
  explanation: "This is the fundamental trade of negative feedback. Increasing β increases the loop gain T = βA, which drives the closed-loop gain toward 1/β — a value that depends on the feedback network (often made from stable passive components) rather than on the amplifier's exact gain A. The circuit becomes less sensitive to variations in A (due to temperature, aging, or manufacturing variation) and has better-defined frequency response. The cost is that raw gain falls, but stability and predictability improve — the essence of why negative feedback is so widely used in amplifier design."

- question: "A circuit with 60° of phase margin will oscillate if the loop gain magnitude exceeds 1 at some frequency below the unity-gain crossover."
  type: true-false
  answer: false
  explanation: "Phase margin is measured at the specific frequency where |T(jω)| = 1 (0 dB). What matters for stability is not whether |T| > 1 somewhere, but whether it is ≥ 1 at the frequency where the phase crosses −180°. A circuit with 60° of phase margin has its phase at −120° (not −180°) when the gain crosses unity. The loop gain magnitude must be below 1 by the time the phase reaches −180° for stability. Having |T| > 1 at low frequencies (where phase is well above −180°) is completely normal and does not cause oscillation."

- question: "Negative feedback can become positive feedback at high frequencies due to accumulated phase shift in real amplifiers."
  type: true-false
  answer: true
  explanation: "Real amplifiers introduce phase shift that increases with frequency due to parasitic capacitances, finite transistor transit times, and pole-zero pairs in the gain function. At low frequencies, the feedback path subtracts from the input (true negative feedback, ~0° phase shift). As frequency rises, the accumulated phase shift grows. If total loop phase reaches −180°, the subtracted signal has been inverted again, making it additive — converting negative feedback into positive feedback. This is the fundamental instability mechanism in feedback amplifiers, and it is why stability analysis focuses on the high-frequency behavior of T(jω)."

- question: "Why is phase margin measured at the unity-gain (0 dB) frequency rather than at the −180° phase frequency?"
  type: short-answer
  answer: "Phase margin is measured at the unity-gain frequency because that is the frequency at which instability would actually occur if phase were the binding constraint. If |T| = 1 and phase = −180°, the Barkhausen criterion for oscillation is exactly met. By measuring how many degrees the phase is above −180° at the unity-gain crossing, we directly quantify how much additional phase shift the system could tolerate before oscillating. Measuring at the −180° frequency would tell us the gain margin (how much gain increase would cause instability) — a complementary measure — but phase margin answers: 'how close to −180° are we right now, when the gain is at the critical threshold of 1?'"
  explanation: "The two stability margins are complementary: phase margin asks 'how much phase can we afford to lose before oscillating?' (measured at 0 dB), while gain margin asks 'how much gain can we add before oscillating?' (measured at −180°). Both should be checked in a robust design because a system can fail either way — if gain increases unexpectedly (gain margin insufficient) or if additional poles add phase (phase margin insufficient)."
```

## Explainer

From your Bode analysis, you know how to read a system's gain and phase as a function of frequency. Feedback uses that frequency behavior to either tame or amplify a circuit's response. In a **negative feedback** system, a fraction β of the output is subtracted from the input before entering the forward amplifier with gain A. The closed-loop gain becomes A / (1 + βA), or approximately 1/β when the loop gain T = βA is large. This is the central trade of negative feedback: you sacrifice raw gain in exchange for a response that is stable, predictable, and nearly independent of the amplifier's exact gain value.

The **loop gain** T(jω) = β · A(jω) is the quantity that governs everything. Think of it as asking: if a signal travels once around the entire feedback loop — through the amplifier, through the feedback network, and back to the summing junction — by what factor has it been multiplied, and by how many degrees has it been shifted? In the frequency domain, T is a complex number whose magnitude and angle both change with ω. The Bode plot of T(jω) directly shows this behavior.

Stability becomes critical because amplifiers introduce phase shift that grows with frequency. At low frequencies, the feedback is negative (phase shift near 0°, destructive at the summing junction). But at high frequencies, parasitic capacitances accumulate phase shift. If the total phase shift around the loop ever reaches −180° while |T| ≥ 1, the feedback that was subtracting from the input is now *adding* to it — negative feedback has become positive feedback. The circuit will oscillate or latch to a rail. This is the **Barkhausen stability criterion** in reverse: oscillation requires |T| = 1 at the frequency where the loop phase is exactly −180°. A stable amplifier must ensure that by the time the phase reaches −180°, the loop gain magnitude has already fallen below 1.

**Phase margin** and **gain margin** quantify how far the system is from this instability boundary. Phase margin is how many additional degrees of phase the system could tolerate at the unity-gain frequency before oscillating; gain margin is how much extra gain it could absorb at the −180° phase frequency. Both margins should be comfortably positive in a well-designed amplifier — typical targets are at least 45° of phase margin. Your Bode plots let you read these margins directly: find the frequency where |T| = 1 (0 dB), read off the phase at that frequency, and subtract from −180° to find the phase margin. Feedback design is largely the art of shaping T(jω) so these margins are adequate across all operating conditions.
