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
stage: advanced
status: draft
---

# Output Feedback and Dynamic Compensation

## Core Idea
Output feedback control combines state observer with state feedback: estimate states from measurements, then apply state feedback law u = −Kx̂. The resulting compensator is dynamic (order equals plant order) and can place closed-loop poles at desired locations via the separation principle.

## Explainer

From your study of state-feedback pole placement, you know that if you can measure all state variables x(t), you can choose a gain matrix K such that u = −Kx places the closed-loop eigenvalues wherever observability and controllability allow, achieving arbitrary transient performance. The fundamental limitation is the word "if": in real systems you can only measure outputs y = Cx, not the full state vector. The **state observer** (Luenberger observer) you studied reconstructs an estimate x̂ of the full state from the measurable output history, using a correction term proportional to the output prediction error y − Cx̂.

**Output feedback** combines these two components into a single operating loop: run the observer continuously to generate x̂(t), then feed that estimate directly into the state feedback law u = −Kx̂. The controller now has internal state — the observer state x̂ — that evolves according to its own differential equations. This makes the controller **dynamic**: for an n-th order plant, the combined observer-plus-feedback controller is itself an n-th order system. This is a fundamental departure from a static output gain, which maps the current output to the current input with no memory. The dynamic controller can "remember" the trajectory of past outputs and use that history to infer unmeasured states.

The deep result enabling this design is the **separation principle**: under mild conditions, the observer gain L and the feedback gain K can be designed independently. First choose K to place the state-feedback poles at the desired closed-loop locations. Then choose L to place the observer poles — typically two to five times faster than the closed-loop poles, so the estimate converges quickly and estimation errors decay before they significantly affect control performance. The separation principle guarantees that the combined system's poles are exactly the union of the state-feedback poles and the observer poles, with no coupling between the two designs. This separability is specific to linear time-invariant systems; it does not hold for nonlinear systems in general.

The resulting structure is a **dynamic compensator**: from the outside, it maps the measured output y(t) to the control input u(t) through a transfer function of order equal to the plant. Any classical compensator you might encounter — lead-lag networks, PID controllers — can be realized in exactly this state-space form. The state-space framework provides a systematic, principled route to compensator design: specify desired pole locations, solve for K and L independently, and the compensator is determined. This connects the classical frequency-domain design methods of earlier courses to the modern state-space approach, showing that they are different languages for the same underlying goal: shaping the closed-loop dynamics to meet performance specifications.
