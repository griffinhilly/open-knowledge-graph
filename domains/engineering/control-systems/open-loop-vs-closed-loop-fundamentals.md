---
id: open-loop-vs-closed-loop-fundamentals
title: Open-Loop vs Closed-Loop Control
domain: engineering
course: control-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
builds-toward:
- error-signal-feedback-configuration
- gain-phase-margins-stability-robustness
tags:
- fundamentals
- feedback
- system-structure
stage: advanced
status: draft
---

# Open-Loop vs Closed-Loop Control

## Core Idea
Open-loop systems apply predetermined control inputs without sensing output, while closed-loop systems measure output and adjust input based on error to achieve desired behavior. Closed-loop control enables systems to automatically compensate for disturbances and model uncertainties, but introduces stability risks if feedback gains are improperly tuned. Understanding the tradeoffs between simplicity (open-loop) and robustness (closed-loop) is fundamental to control system design.

## How It's Best Learned
Compare simple examples like manual vs cruise control, or thermostat behavior. Simulate both architectures and observe response to disturbances (speed bump, outdoor temperature change).

## Common Misconceptions
- Closed-loop is always better; actually, simpler open-loop designs are preferable when disturbances are predictable.
- Closing the loop always stabilizes a system; incorrect feedback can destabilize even stable open-loop plants.
- Feedback eliminates all steady-state error; error type depends on system order and controller structure.

## Explainer

From your prerequisite work on feedback control, you understand that a control system connects three main components: a **plant** (the physical process to be controlled), a **controller** (which generates input commands), and a **sensor** (which measures what the plant is doing). The distinction between open-loop and closed-loop lies entirely in whether the sensor output is fed back to influence the controller's decisions.

An **open-loop** controller fires off a predetermined command based on the desired output alone, with no reference to what the plant actually does. A toaster timer is a pure open-loop system: it runs for a fixed time regardless of how dark the bread becomes. A traffic light on a fixed cycle ignores actual traffic flow. The appeal of open-loop is simplicity—no sensor required, no risk of feedback-induced instability, easy to design and debug. The liability is brittleness: any deviation of the plant's behavior from the assumed model goes uncorrected. Open-loop works well when disturbances are small and predictable, and when the plant model is accurate and stable over time.

A **closed-loop** system continuously measures the output and computes an **error signal**—the difference between desired output (setpoint) and actual output—and adjusts the control input to drive that error toward zero. Cruise control is a closed-loop system: it measures actual speed, compares it to the set speed, and adjusts the throttle accordingly. When a hill slows the car, the error grows and the system responds automatically without the driver needing to anticipate every grade change. This automatic error correction is the defining advantage of feedback: it works even when the plant model is imperfect, disturbances are unpredictable, or operating conditions change over time.

But closing the loop introduces risk. Feedback systems can become **unstable** if controller gains are too high: the system overcorrects, the overcorrection triggers a larger error in the opposite direction, and the output oscillates or diverges. The margin between stable closed-loop behavior and instability is quantified by gain and phase margins—topics you will encounter shortly. Choosing between open-loop and closed-loop is fundamentally a question of uncertainty: if the plant is well characterized and disturbances are small or predictable, open-loop simplicity wins; if the plant varies, disturbances are significant, or steady-state accuracy matters, closed-loop robustness is worth the added complexity and stability risk.
