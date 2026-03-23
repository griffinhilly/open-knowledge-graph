---
id: output-feedback-and-dynamic-compensation
title: Output Feedback and Dynamic Compensation
domain: engineering
course: control-systems
prerequisites:
- id: state-observer-full-and-partial-observation
  type: hard
- id: state-feedback-pole-placement
  type: hard
builds-toward:
- cascade-control-loop-interaction-analysis
tags:
- dynamic-controller
- observer-based-feedback
- output-feedback
- compensation
stage: expert
status: draft
---

# Output Feedback and Dynamic Compensation

## Core Idea
Output feedback control combines state observer with state feedback: estimate states from measurements, then apply state feedback law u = −Kx̂. The resulting compensator is dynamic (order equals plant order) and can place closed-loop poles at desired locations via the separation principle.

## Questions

```yaml
- question: "You design a state-feedback controller with desired closed-loop poles at {−2, −3} and an observer with poles at {−10, −15} for a 2nd-order plant. According to the separation principle, the poles of the combined output-feedback system are:"
  type: multiple-choice
  options:
    - "Only {−2, −3} — the observer poles are internal and do not appear in the closed-loop system"
    - "All four: {−2, −3, −10, −15} — the two sets combine with no coupling between the two designs"
    - "The average of the state-feedback and observer poles"
    - "Only determinable by solving the combined design equations simultaneously"
  answer: 1
  explanation: "The separation principle guarantees that the combined system's poles are the union of the state-feedback poles and the observer poles — here all four values. Crucially, the two sets can be chosen independently: K is designed to place the feedback poles, L is designed to place the observer poles, and they do not interfere. This separability is what makes output-feedback design tractable. The observer poles are typically placed 2–5 times faster than the feedback poles so estimation errors decay before significantly affecting control."

- question: "A student proposes using a static output feedback law u = −Ky(t) instead of an observer-based controller. The fundamental limitation compared to dynamic compensation is:"
  type: multiple-choice
  options:
    - "Static feedback cannot achieve closed-loop stability for any plant"
    - "Static feedback has no internal state, so it cannot reconstruct unmeasured state variables — it uses only the current output, losing information about the system's history"
    - "Static feedback places all closed-loop poles on the real axis"
    - "The separation principle does not apply, making the design computationally intractable"
  answer: 1
  explanation: "A static output gain maps the current output directly to the current input with no memory. If not all states are measured, the controller has no way to infer the unmeasured states from the output history. A dynamic controller — the observer-plus-feedback structure — maintains internal state that evolves over time, effectively accumulating information about past outputs to reconstruct the full state vector. This is what allows full state-feedback performance even when only outputs are measured."

- question: "The separation principle guarantees that observer gain L and feedback gain K can be designed independently, with the combined system's poles being exactly the union of the state-feedback poles and the observer poles."
  type: true-false
  answer: true
  explanation: "This is the separation principle for linear time-invariant systems. It is what makes output-feedback design via observers practical: choose K first to meet transient performance requirements, then choose L independently to make the observer fast enough. The closed-loop pole set is exactly the union of the two separately chosen sets, with no cross-coupling. This separability is a special property of LTI systems."

- question: "The separation principle applies to nonlinear systems as long as the observer error converges exponentially fast."
  type: true-false
  answer: false
  explanation: "The separation principle is specific to linear time-invariant systems. For nonlinear systems, the observer error dynamics and the control error dynamics are coupled — the observer error affects the control performance in a nonlinear way, and you cannot independently choose observer and feedback gains to achieve a desired combined behavior. Nonlinear output-feedback design is substantially more difficult and requires tools like Lyapunov-based separation conditions or high-gain observers, which come with stricter requirements."

- question: "Why is the output-feedback controller called 'dynamic,' and what is the significance of its order being equal to the plant order?"
  type: short-answer
  answer: "The observer-based controller is dynamic because it has internal state — the observer state x̂ — that evolves according to its own differential equations over time. For an nth-order plant, the observer reconstructs n state variables, making the controller itself nth-order. Unlike a static output gain (which only uses the current measurement), the dynamic controller effectively has memory of past outputs, using that history to reconstruct unmeasured states. The fact that its order equals the plant order is significant because it means any classical compensator — PID, lead-lag, notch filter — can be represented in exactly this observer-feedback form, connecting state-space and classical frequency-domain design as different languages for the same structure."
  explanation: "The order-equals-plant-order result is not coincidental: the observer must maintain n internal variables to track the n-dimensional plant state. This is the minimum information needed to reconstruct the full state from output measurements alone."
```

## Explainer

From your study of state-feedback pole placement, you know that if you can measure all state variables x(t), you can choose a gain matrix K such that u = −Kx places the closed-loop eigenvalues wherever observability and controllability allow, achieving arbitrary transient performance. The fundamental limitation is the word "if": in real systems you can only measure outputs y = Cx, not the full state vector. The **state observer** (Luenberger observer) you studied reconstructs an estimate x̂ of the full state from the measurable output history, using a correction term proportional to the output prediction error y − Cx̂.

**Output feedback** combines these two components into a single operating loop: run the observer continuously to generate x̂(t), then feed that estimate directly into the state feedback law u = −Kx̂. The controller now has internal state — the observer state x̂ — that evolves according to its own differential equations. This makes the controller **dynamic**: for an n-th order plant, the combined observer-plus-feedback controller is itself an n-th order system. This is a fundamental departure from a static output gain, which maps the current output to the current input with no memory. The dynamic controller can "remember" the trajectory of past outputs and use that history to infer unmeasured states.

The deep result enabling this design is the **separation principle**: under mild conditions, the observer gain L and the feedback gain K can be designed independently. First choose K to place the state-feedback poles at the desired closed-loop locations. Then choose L to place the observer poles — typically two to five times faster than the closed-loop poles, so the estimate converges quickly and estimation errors decay before they significantly affect control performance. The separation principle guarantees that the combined system's poles are exactly the union of the state-feedback poles and the observer poles, with no coupling between the two designs. This separability is specific to linear time-invariant systems; it does not hold for nonlinear systems in general.

The resulting structure is a **dynamic compensator**: from the outside, it maps the measured output y(t) to the control input u(t) through a transfer function of order equal to the plant. Any classical compensator you might encounter — lead-lag networks, PID controllers — can be realized in exactly this state-space form. The state-space framework provides a systematic, principled route to compensator design: specify desired pole locations, solve for K and L independently, and the compensator is determined. This connects the classical frequency-domain design methods of earlier courses to the modern state-space approach, showing that they are different languages for the same underlying goal: shaping the closed-loop dynamics to meet performance specifications.
