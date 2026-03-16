---
id: feedback-control-fundamentals
title: Feedback Control Fundamentals
domain: engineering
course: control-systems
prerequisites:
- id: differential-equations-intro-separable
  type: hard
- id: first-order-transient-circuits
  type: soft
- id: second-order-transient-circuits
  type: soft
- id: differential-equations-intro
  type: soft
builds-toward:
- laplace-transform-control
- transfer-functions-control
tags:
- feedback
- closed-loop
- open-loop
- control
- error-signal
stage: advanced
status: validated
---

# Feedback Control Fundamentals

## Core Idea
Feedback control uses the difference between a desired output (setpoint) and the actual output (error signal) to drive a system toward its goal. Open-loop systems apply input without measuring output, while closed-loop systems continuously correct based on feedback. The block diagram of a closed-loop system includes the plant (process being controlled), the controller, sensors, and the feedback path. Key performance goals include stability, accuracy, and speed of response.

## How It's Best Learned
Start by analyzing simple thermostats or cruise control systems as physical intuitions for feedback before formalizing with math. Draw block diagrams of everyday control systems and compare open-loop vs. closed-loop responses to understand why feedback matters.

## Common Misconceptions
- More feedback gain is not always better — too much gain causes oscillation or instability.
- Open-loop control is not always inferior; it is appropriate when the plant is well-characterized and disturbances are minimal.
- The 'negative' in negative feedback refers to the subtraction operation at the summing junction, not a negative system outcome.

## Questions

```yaml
- question: "A cruise control system maintains a car's speed by comparing the actual speed to the desired speed and adjusting the throttle. This is an example of which type of control?"
  type: multiple-choice
  options: ["Open-loop control", "Feedforward control", "Closed-loop (feedback) control", "Bang-bang control"]
  answer: 2
  explanation: "The system continuously measures the actual output (speed), computes the error relative to the setpoint, and uses that error to drive the actuator — the defining structure of closed-loop feedback control. Open-loop control would apply a fixed throttle without measuring actual speed."

- question: "Increasing the feedback gain in a closed-loop control system always improves performance by reducing error faster."
  type: true-false
  answer: false
  explanation: "High gain amplifies the error correction signal, which can cause the system to overcorrect repeatedly, leading to oscillation or outright instability. There is a fundamental tradeoff between speed of response and stability: gain must be tuned to balance these competing demands."

- question: "What is the role of the error signal in a closed-loop control system, and how is it computed?"
  type: short-answer
  answer: "The error signal is the difference between the desired output (setpoint) and the actual measured output. It is computed at the summing junction by subtracting the feedback signal from the reference input. The controller acts on this error to drive the plant toward the setpoint."
  explanation: "The error signal is the core mechanism of feedback: if error is zero, the system has reached its goal and no correction is needed. If error is nonzero, the controller uses its magnitude and sign to decide how much corrective action to apply. Without measuring error, there is no feedback."
```

## Explainer

Imagine a thermostat: you set a desired temperature (the setpoint), the thermostat measures the actual temperature, computes how far off it is, and turns the heater on or off accordingly. This loop — measure, compare, correct — is the essence of feedback control. Every closed-loop system has the same fundamental structure: a reference input, a sensor measuring actual output, a summing junction computing the error, a controller deciding what action to take, and a plant (the physical system being controlled) that responds.

The key insight separating open-loop from closed-loop control is whether the system knows what it actually produced. An open-loop system applies a predetermined input and hopes for the best — like setting a microwave timer without checking if food is cooked. A closed-loop system continuously checks and corrects. This makes closed-loop systems robust to disturbances and modeling errors, which is why they dominate real engineering applications. However, closed-loop control requires reliable sensors and introduces the possibility of instability.

Gain is the amplification applied to the error signal before it reaches the plant. Intuitively, higher gain means stronger corrections, which reduces steady-state error and speeds response. But there is a catch: if gain is too high, the system overcorrects, then overcorrects its overcorrection, and so on — producing oscillations or instability. This tradeoff is one of the central challenges of control design and motivates the rigorous tools you will encounter next (Laplace transforms, transfer functions, root locus, Bode plots).

The block diagram is the standard language for describing control systems. Each block represents a component characterized by how it transforms an input signal into an output signal. The feedback path takes the plant output, feeds it back through the sensor, and subtracts it from the reference at the summing junction. The signal flowing into the controller is always the error — not the reference, and not the output directly. Understanding this distinction is critical when analyzing how disturbances enter the system and where they can be rejected.
