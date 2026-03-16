---
id: response-specifications-performance-metrics
title: Response Specifications and Performance Metrics
domain: engineering
course: control-systems
prerequisites:
- id: steady-state-error-types-system-classification
  type: hard
builds-toward:
- first-order-system-transient-response
- second-order-system-damping-ratio
- compensation-design-tradeoffs-cascadefeedback
tags:
- response-specifications
- overshoot
- settling-time
- rise-time
- bandwidth
stage: formal-systems
status: draft
---

# Response Specifications and Performance Metrics

## Core Idea
Key transient response metrics: rise time (initial speed), peak time, overshoot (maximum deviation), settling time (2% band arrival). Steady-state error measures tracking accuracy. These specifications must be balanced against bandwidth and robustness. The design problem is choosing controller parameters to satisfy all specifications simultaneously.

## Explainer

When you design a feedback controller, you need a language to describe what "good" performance means. From your study of steady-state error and system types, you know one dimension: accuracy at rest. But a system could achieve perfect steady-state accuracy while oscillating violently on the way there, or while taking ten seconds to settle after a step command. **Response specifications** give you the vocabulary to describe the complete time-domain behavior — both the transient journey and the final destination — so that design requirements can be stated precisely and verified objectively against test data.

The standard step response — applying a unit step input and watching the output — reveals four key transient metrics. **Rise time** (t_r) is how quickly the output climbs from 10% to 90% of its final value; it characterizes initial speed of response. **Peak time** (t_p) is the time at which the output reaches its first maximum, relevant when overshoot is present. **Percent overshoot** (%OS) measures how far the first peak exceeds the final value, expressed as a percentage; a purely overdamped response has zero overshoot, while highly underdamped systems may overshoot by 50% or more. **Settling time** (t_s) is when the output permanently enters and stays within ±2% of its final value; it captures how long oscillations persist before the transient dies out. Together, these four metrics describe the shape of the transient response from the moment a step is applied until the system reaches its new steady state.

These metrics trade off against each other in fundamental ways, and this is not a deficiency of engineering — it reflects physical reality. Achieving very fast rise time requires high loop gain and bandwidth, which tend to drive the system into underdamped territory with large overshoot. Reducing overshoot to near zero requires overdamped behavior, which increases both rise time and settling time (because an overdamped response approaches its final value sluggishly). Minimizing settling time — the most common single objective — requires balancing fast response against adequate damping. The controller design problem is always a negotiation among competing specifications, not a search for perfection on every axis simultaneously.

**Steady-state error** completes the performance picture. A system with impeccable transient behavior that settles to the wrong value is useless for any tracking application. Steady-state error measures the discrepancy between the commanded value and the actual output after all transients have died out. Your prerequisite work on system types established that the steady-state error to a step depends on the open-loop gain and loop structure (Type 0, 1, 2, etc.). Together, the four transient metrics and steady-state error form a five-dimensional specification space in which real design requirements live: "less than 15% overshoot, settle within 0.5 seconds, steady-state error below 1%."

**Bandwidth** connects the time-domain specifications to frequency-domain design. A system with high bandwidth responds quickly to rapidly changing references and rejects high-frequency disturbances effectively; its step response has short rise time. The approximate relationship for a second-order system is t_r ≈ 1.8 / ω_BW, where ω_BW is the closed-loop −3 dB bandwidth. This bridge becomes essential when you move on to Bode plots and compensator design: shaping the loop's frequency response to hit a bandwidth target and phase margin target is equivalent to shaping the step response to meet rise time and overshoot targets. Percent overshoot is tied to phase margin (PM ≈ 100 · ζ for small ζ, with %OS = e^(−πζ/√(1−ζ²)) × 100). Specifications in the time domain and in the frequency domain are two descriptions of the same underlying system — the response specifications you are learning here are the translation key between them.
