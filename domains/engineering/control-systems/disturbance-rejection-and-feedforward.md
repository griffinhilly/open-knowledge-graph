---
id: disturbance-rejection-and-feedforward
title: Disturbance Rejection and Feedforward Control
domain: engineering
course: control-systems
prerequisites:
- id: error-signal-feedback-configuration
  type: hard
- id: cascade-and-feedforward-control
  type: soft
builds-toward:
- sensitivity-and-robustness-functions
tags:
- disturbance
- rejection
- feedforward
- control-architecture
stage: expert
status: draft
---

# Disturbance Rejection and Feedforward Control

## Core Idea
Disturbance rejection capability depends on where the disturbance enters the plant relative to the feedback path. Feedback alone cannot reject disturbances before they affect output. Feedforward control (estimating disturbances and applying compensating input) can reject measured disturbances without feedback delay. Combined feedback-feedforward architectures offer superior disturbance attenuation.

## Questions

```yaml
- question: "A room temperature control system uses a thermostat measuring indoor air temperature. A cold front arrives, dropping outdoor temperature sharply. What is the fundamental limitation of this pure feedback approach?"
  type: multiple-choice
  options:
    - "The thermostat gain is too low to detect rapid temperature changes"
    - "The feedback loop cannot act until the indoor temperature has already dropped, meaning the disturbance has already degraded the output"
    - "Feedback control is inherently unstable when outdoor disturbances are fast"
    - "The sensor cannot distinguish between setpoint changes and external disturbances"
  answer: 1
  explanation: "Feedback is inherently reactive: it measures the output, detects an error, and then corrects — but the error must already exist in the output before any correction begins. When the cold front hits, indoor temperature must first drop before the thermostat triggers heating. A feedforward controller using an outdoor temperature sensor would act the moment outdoor temperature falls, before any indoor effect occurs. This reactive delay is structural, not a tuning problem."

- question: "A process has a large, fast disturbance that is directly measurable at its source. Which control architecture best handles this situation?"
  type: multiple-choice
  options:
    - "Pure feedback with very high loop gain, since this minimizes steady-state error regardless of disturbance speed"
    - "Pure feedforward, since it completely eliminates the disturbance before it affects the output with no model dependency"
    - "Combined feedforward-feedback: feedforward quickly cancels the measured disturbance; feedback corrects residuals from model error"
    - "Cascade control, which uses a secondary feedback loop to handle fast inner dynamics"
  answer: 2
  explanation: "Combined FF+FB is the standard answer for measurable disturbances. Feedforward provides fast, anticipatory rejection by acting before the disturbance reaches the output — but only as well as the plant model is accurate. Feedback corrects the residuals that model imperfection leaves behind, plus any unmeasured disturbance components. Pure feedforward fails with model error; pure feedback is reactive; high gain alone cannot eliminate reactive delay."

- question: "A feedforward controller can reject unmeasured disturbances more effectively than a feedback controller, since it acts before they affect the output."
  type: true-false
  answer: false
  explanation: "Feedforward requires that the disturbance be measurable — it acts by detecting the disturbance at its source and computing a compensating signal. If a disturbance is unmeasured, the feedforward controller has no information about it and cannot act. For unmeasured disturbances, feedback is the only option: it corrects reactively once the disturbance causes an output error. This is precisely why combining both architectures is superior to either alone."

- question: "Feedback control is inherently reactive: it can only apply corrective action after a disturbance has already caused a detectable error in the output."
  type: true-false
  answer: true
  explanation: "This is the defining structural limitation of feedback control. The sensor must detect an output deviation before the controller computes an error signal and applies a correction. This sequence means the output error exists before the correction arrives — the latency is irreducible, not a tuning artifact. Feedforward control was developed specifically to overcome this limitation for cases where disturbances can be sensed directly at their source."

- question: "Why does the combined feedforward-feedback architecture outperform pure feedforward or pure feedback alone when rejecting a large, measurable disturbance?"
  type: short-answer
  answer: "Feedforward alone is fast but fragile: it can only cancel disturbances it measures and can only do so as accurately as its plant model. Model error, parameter drift, and unmeasured disturbance components leave residuals that feedforward cannot address. Feedback alone is robust but reactive: it corrects any error eventually, but only after the disturbance has already affected the output. Combined, feedforward rapidly attenuates the bulk of the measured disturbance while feedback corrects the residuals — each mechanism compensates for the other's weakness."
  explanation: "The complementarity is the key insight: feedforward handles what is measurable and modeled; feedback handles what is not. High-performance industrial control always uses both wherever disturbances can be sensed, because neither alone achieves fast AND robust disturbance rejection."
```

## Explainer

From your study of the feedback configuration, you know that a closed-loop controller measures output, computes an error, and adjusts input to drive that error toward zero. This is a powerful paradigm, but it has a structural limitation: feedback can only correct an error *after it appears in the output*. If a disturbance enters the plant, the loop must first detect the resulting output deviation, then correct it—incurring both detection delay and correction time. For slow or small disturbances this is acceptable; for fast or large ones, the correction arrives too late to prevent significant performance degradation.

The **entry point** of a disturbance relative to the feedback loop determines how well feedback can handle it. A disturbance entering at the plant input—before the main process—causes output deviations that the feedback loop must work backward to correct; high loop gain is required to keep these deviations small. A disturbance entering between two cascaded stages will propagate through only the downstream portion before the sensor catches it—better, but still reactive. The key insight is that **feedback is inherently reactive**: it waits for consequences before acting, and no amount of loop gain eliminates the latency between a disturbance occurring and the corrective action arriving.

**Feedforward control** breaks this reactive constraint by measuring the disturbance directly and applying a compensating input simultaneously—before the disturbance has time to affect the output. If the disturbance is measurable and the plant's response is known, the feedforward controller can ideally cancel the disturbance completely. In a building heating system, an outdoor temperature sensor can trigger increased heating *before* the indoor temperature begins to drop, rather than waiting for the thermostat to detect an error. The feedforward compensator acts as an inverse plant model: it pre-computes what correction is needed and injects it without waiting for feedback.

Pure feedforward's limitation is its dependence on an accurate plant model. Model errors, unmeasured disturbances, and parameter drift leave residual errors that feedforward cannot address. This is where the **combined feedforward-feedback architecture** achieves the best of both worlds: feedforward provides fast, anticipatory rejection of the *measured* disturbance, while feedback corrects the residuals that feedforward cannot eliminate due to modeling imperfection. The two mechanisms are complementary—feedforward handles what is measurable and modeled; feedback handles what is not—and their combination is the standard approach in high-performance industrial control wherever disturbances can be sensed directly.
