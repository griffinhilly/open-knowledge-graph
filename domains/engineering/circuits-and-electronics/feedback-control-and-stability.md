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
stage: formal-systems
status: draft
---

# Feedback Control Systems and Stability Analysis

## Core Idea
Feedback modifies circuit behavior by returning a portion of the output to the input. Loop gain T(jω) = β·A(jω) (feedback fraction times forward gain) determines closed-loop behavior. Negative feedback reduces gain but improves linearity, bandwidth, and noise; positive feedback increases gain or causes oscillation if |T| ≥ 1. Stability requires |T(jω)| < 1 at frequencies where the phase of T crosses -180°.

## Explainer

From your Bode analysis, you know how to read a system's gain and phase as a function of frequency. Feedback uses that frequency behavior to either tame or amplify a circuit's response. In a **negative feedback** system, a fraction β of the output is subtracted from the input before entering the forward amplifier with gain A. The closed-loop gain becomes A / (1 + βA), or approximately 1/β when the loop gain T = βA is large. This is the central trade of negative feedback: you sacrifice raw gain in exchange for a response that is stable, predictable, and nearly independent of the amplifier's exact gain value.

The **loop gain** T(jω) = β · A(jω) is the quantity that governs everything. Think of it as asking: if a signal travels once around the entire feedback loop — through the amplifier, through the feedback network, and back to the summing junction — by what factor has it been multiplied, and by how many degrees has it been shifted? In the frequency domain, T is a complex number whose magnitude and angle both change with ω. The Bode plot of T(jω) directly shows this behavior.

Stability becomes critical because amplifiers introduce phase shift that grows with frequency. At low frequencies, the feedback is negative (phase shift near 0°, destructive at the summing junction). But at high frequencies, parasitic capacitances accumulate phase shift. If the total phase shift around the loop ever reaches −180° while |T| ≥ 1, the feedback that was subtracting from the input is now *adding* to it — negative feedback has become positive feedback. The circuit will oscillate or latch to a rail. This is the **Barkhausen stability criterion** in reverse: oscillation requires |T| = 1 at the frequency where the loop phase is exactly −180°. A stable amplifier must ensure that by the time the phase reaches −180°, the loop gain magnitude has already fallen below 1.

**Phase margin** and **gain margin** quantify how far the system is from this instability boundary. Phase margin is how many additional degrees of phase the system could tolerate at the unity-gain frequency before oscillating; gain margin is how much extra gain it could absorb at the −180° phase frequency. Both margins should be comfortably positive in a well-designed amplifier — typical targets are at least 45° of phase margin. Your Bode plots let you read these margins directly: find the frequency where |T| = 1 (0 dB), read off the phase at that frequency, and subtract from −180° to find the phase margin. Feedback design is largely the art of shaping T(jω) so these margins are adequate across all operating conditions.
