---
id: open-loop-vs-closed-loop-fundamentals
title: Open-Loop vs Closed-Loop Control
domain: engineering
course: control-systems
prerequisites:
- id: feedback-control-fundamentals
  type: hard
- id: control-systems-intro-engineering
  type: soft
builds-toward:
- error-signal-feedback-configuration
- gain-phase-margins-stability-robustness
tags:
- fundamentals
- feedback
- system-structure
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "A robotic arm operates in a controlled factory where the arm's mechanical properties are precisely characterized and no unexpected external forces act on it. An engineer proposes adding a closed-loop sensor to improve performance. What does control theory suggest?"
  type: multiple-choice
  options:
    - "Closed-loop is always better, so the sensor should be added regardless of environment"
    - "Open-loop is preferable here — the predictable environment and accurate model eliminate the main advantage of feedback"
    - "Closed-loop is necessary because open-loop systems cannot achieve precise positioning"
    - "The choice does not matter because both architectures perform identically in controlled conditions"
  answer: 1
  explanation: "The key insight is that the choice between open-loop and closed-loop is fundamentally about uncertainty. Closed-loop feedback earns its added complexity by correcting for disturbances and model errors. When the plant model is accurate and disturbances are negligible, those advantages disappear — and the open-loop design wins by being simpler, cheaper, and free from the stability risks that feedback introduces. Adding feedback to an already well-characterized, stable system can introduce instability without providing meaningful benefit."

- question: "What is the fundamental mechanism by which closed-loop control handles unpredictable disturbances that open-loop control cannot?"
  type: multiple-choice
  options:
    - "It uses a more powerful actuator that overwhelms disturbances before they affect the output"
    - "It predicts disturbances using an internal model and preemptively cancels their effects"
    - "It continuously measures output error and adjusts the control input to drive that error toward zero"
    - "It increases system bandwidth so disturbance effects decay faster"
  answer: 2
  explanation: "Closed-loop control works by sensing what actually happened and correcting for it — not by predicting or overpowering disturbances. The error signal (setpoint minus actual output) is computed continuously, and the controller adjusts its input to reduce that error. This works even for disturbances the designer never anticipated, because the mechanism responds to outcomes rather than causes. Open-loop has no such mechanism: it applies its command regardless of what the plant does, so any unmodeled disturbance goes uncorrected."

- question: "Closing the loop generally improves stability — a marginally stable open-loop plant will become more stable once feedback is added."
  type: true-false
  answer: false
  explanation: "This is a critical misconception. Feedback does not automatically stabilize — it can destabilize. If controller gains are too high, feedback causes overcorrection: an error triggers a corrective input, which creates a larger error in the opposite direction, which triggers a still-larger correction, leading to oscillation or divergence. A plant that is stable in open-loop can be made unstable by improperly tuned closed-loop feedback. Gain and phase margins exist precisely to quantify how much margin separates stable operation from instability in a feedback system."

- question: "A toaster with a timer is an example of an open-loop system: it cannot compensate if the bread is already partially toasted or if the heating element degrades over time."
  type: true-false
  answer: true
  explanation: "Correct. The toaster timer applies a fixed duration regardless of the actual toast darkness — it has no sensor to measure the output. This means it cannot compensate for varying initial conditions (bread already toasted) or plant changes (weakening heating element). This brittleness is the defining liability of open-loop systems: any deviation of the actual plant from the assumed model goes uncorrected. A feedback-based toaster would sense bread color and stop when the desired darkness was achieved, but would require a sensor and introduces the complexity of a control loop."

- question: "Why does adding feedback to a control system introduce the possibility of instability that was absent in the open-loop design?"
  type: short-answer
  answer: "Feedback creates a closed loop in which the output influences the input. If controller gains are too high, the system overcorrects: an error triggers a corrective input that drives the output past the setpoint in the other direction, creating a larger error, triggering an even larger correction, and so on. This self-reinforcing oscillation is impossible in open-loop because there is no loop — the controller applies its command without reference to what the plant does. Feedback trades the brittleness of open-loop (no correction for disturbances) for the stability risk of closed-loop (possible runaway oscillation if gains are wrong)."
  explanation: "The mathematical condition for instability is that the loop gain and phase combine to create net positive feedback at some frequency — meaning perturbations at that frequency grow rather than decay. Gain and phase margins measure how far the system is from this condition. Neither concept applies to open-loop systems, which have no loop to go unstable. This is why gain and phase margin analysis is exclusively a closed-loop concern."
```

## Explainer

From your prerequisite work on feedback control, you understand that a control system connects three main components: a **plant** (the physical process to be controlled), a **controller** (which generates input commands), and a **sensor** (which measures what the plant is doing). The distinction between open-loop and closed-loop lies entirely in whether the sensor output is fed back to influence the controller's decisions.

An **open-loop** controller fires off a predetermined command based on the desired output alone, with no reference to what the plant actually does. A toaster timer is a pure open-loop system: it runs for a fixed time regardless of how dark the bread becomes. A traffic light on a fixed cycle ignores actual traffic flow. The appeal of open-loop is simplicity—no sensor required, no risk of feedback-induced instability, easy to design and debug. The liability is brittleness: any deviation of the plant's behavior from the assumed model goes uncorrected. Open-loop works well when disturbances are small and predictable, and when the plant model is accurate and stable over time.

A **closed-loop** system continuously measures the output and computes an **error signal**—the difference between desired output (setpoint) and actual output—and adjusts the control input to drive that error toward zero. Cruise control is a closed-loop system: it measures actual speed, compares it to the set speed, and adjusts the throttle accordingly. When a hill slows the car, the error grows and the system responds automatically without the driver needing to anticipate every grade change. This automatic error correction is the defining advantage of feedback: it works even when the plant model is imperfect, disturbances are unpredictable, or operating conditions change over time.

But closing the loop introduces risk. Feedback systems can become **unstable** if controller gains are too high: the system overcorrects, the overcorrection triggers a larger error in the opposite direction, and the output oscillates or diverges. The margin between stable closed-loop behavior and instability is quantified by gain and phase margins—topics you will encounter shortly. Choosing between open-loop and closed-loop is fundamentally a question of uncertainty: if the plant is well characterized and disturbances are small or predictable, open-loop simplicity wins; if the plant varies, disturbances are significant, or steady-state accuracy matters, closed-loop robustness is worth the added complexity and stability risk.
