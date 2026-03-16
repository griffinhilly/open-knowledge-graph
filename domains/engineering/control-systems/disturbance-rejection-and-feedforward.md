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
stage: advanced
status: draft
---

# Disturbance Rejection and Feedforward Control

## Core Idea
Disturbance rejection capability depends on where the disturbance enters the plant relative to the feedback path. Feedback alone cannot reject disturbances before they affect output. Feedforward control (estimating disturbances and applying compensating input) can reject measured disturbances without feedback delay. Combined feedback-feedforward architectures offer superior disturbance attenuation.

## Explainer

From your study of the feedback configuration, you know that a closed-loop controller measures output, computes an error, and adjusts input to drive that error toward zero. This is a powerful paradigm, but it has a structural limitation: feedback can only correct an error *after it appears in the output*. If a disturbance enters the plant, the loop must first detect the resulting output deviation, then correct it—incurring both detection delay and correction time. For slow or small disturbances this is acceptable; for fast or large ones, the correction arrives too late to prevent significant performance degradation.

The **entry point** of a disturbance relative to the feedback loop determines how well feedback can handle it. A disturbance entering at the plant input—before the main process—causes output deviations that the feedback loop must work backward to correct; high loop gain is required to keep these deviations small. A disturbance entering between two cascaded stages will propagate through only the downstream portion before the sensor catches it—better, but still reactive. The key insight is that **feedback is inherently reactive**: it waits for consequences before acting, and no amount of loop gain eliminates the latency between a disturbance occurring and the corrective action arriving.

**Feedforward control** breaks this reactive constraint by measuring the disturbance directly and applying a compensating input simultaneously—before the disturbance has time to affect the output. If the disturbance is measurable and the plant's response is known, the feedforward controller can ideally cancel the disturbance completely. In a building heating system, an outdoor temperature sensor can trigger increased heating *before* the indoor temperature begins to drop, rather than waiting for the thermostat to detect an error. The feedforward compensator acts as an inverse plant model: it pre-computes what correction is needed and injects it without waiting for feedback.

Pure feedforward's limitation is its dependence on an accurate plant model. Model errors, unmeasured disturbances, and parameter drift leave residual errors that feedforward cannot address. This is where the **combined feedforward-feedback architecture** achieves the best of both worlds: feedforward provides fast, anticipatory rejection of the *measured* disturbance, while feedback corrects the residuals that feedforward cannot eliminate due to modeling imperfection. The two mechanisms are complementary—feedforward handles what is measurable and modeled; feedback handles what is not—and their combination is the standard approach in high-performance industrial control wherever disturbances can be sensed directly.
