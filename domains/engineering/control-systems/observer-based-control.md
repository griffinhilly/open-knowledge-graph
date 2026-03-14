---
id: observer-based-control
title: Observer-Based Control
domain: engineering
course: control-systems
prerequisites:
- id: luenberger-observer
  type: hard
- id: state-feedback-pole-placement
  type: hard
tags:
- separation-principle
- output-feedback
- observer-controller
- state-estimation
- closed-loop-poles
stage: advanced
status: draft
---

# Observer-Based Control

## Core Idea
Observer-based control combines a state feedback control law u = −Kx̂ with a Luenberger observer that estimates the full state vector x̂ from the measured output y, enabling state feedback design even when not all states are directly measurable. The separation principle guarantees that the closed-loop poles of the combined observer-controller system are the union of the state feedback poles (eigenvalues of A − BK) and the observer poles (eigenvalues of A − LC), and that these two sets can be designed independently. This means the control gain K can be designed as if full state feedback were available, and the observer gain L can be designed separately to achieve desired estimation dynamics, without either design affecting the other's pole locations. The observer poles are typically placed 2-5 times faster than the controller poles so that estimation errors decay quickly relative to the controlled response. The resulting output feedback controller can be written as a dynamic compensator: a transfer function from y to u with order equal to the number of states, making it equivalent to classical compensator design but derived from the state-space framework. The separation principle holds for linear time-invariant systems but does not generally extend to nonlinear or time-varying systems.

## How It's Best Learned
Design a state feedback controller for a third-order system assuming full state measurement, then replace the true states with estimates from a Luenberger observer and simulate the combined system. Compare the response when observer poles are placed at different speeds relative to controller poles — too slow and the transient is degraded by estimation error, too fast and the observer becomes noise-sensitive. Verify the separation principle by computing the combined closed-loop eigenvalues and confirming they equal the union of independently designed sets.

## Common Misconceptions
- The separation principle does not mean the observer has no effect on performance — while pole locations are independent, the transient response includes observer error dynamics that manifest as initial deviations from the ideal full-state-feedback response, especially when the initial state estimate is poor.
- Making the observer arbitrarily fast (placing observer poles very far to the left) is not free — faster observers have larger gains L, amplifying measurement noise and potentially exciting unmodeled high-frequency plant dynamics.
- Observer-based control requires the system to be both controllable (for K design) and observable (for L design) — if either property is missing, the combined design fails, and checking both is a prerequisite before beginning the design.
