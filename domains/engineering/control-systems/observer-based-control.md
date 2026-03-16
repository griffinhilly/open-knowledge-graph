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

## Explainer

State feedback control — the law u = −Kx — delivers the clean pole placement results you know: choose K to place the closed-loop eigenvalues of A − BK wherever you want. But it assumes you can measure every component of the state vector x. In practice, sensors are expensive, some states are physically inaccessible, and you may have n state variables but only p < n outputs y = Cx. The **Luenberger observer** solves this by running a model of the plant in parallel with the actual system, continuously correcting the model's estimate x̂ using the discrepancy between the actual output y and the predicted output Cx̂. The observer dynamics are: dx̂/dt = Ax̂ + Bu + L(y − Cx̂). The gain matrix L is chosen to place the eigenvalues of A − LC, controlling how fast the estimation error e = x − x̂ decays to zero.

The estimation error obeys: de/dt = (A − LC)e. If A − LC is stable (all eigenvalues in the LHP), the error decays exponentially to zero regardless of the initial mismatch — the observer "forgets" its initial uncertainty. The rate of forgetting is set by the observer poles. A rule of thumb is to place observer poles **2–5 times faster** than the desired closed-loop controller poles: if you want the controlled system to settle in 1 second, place observer poles to settle in 0.2–0.5 seconds. This ensures estimation error is negligible before the controller needs accurate state information. The cost is that larger L amplifies sensor noise into the estimate — a fundamental tension between estimation speed and noise sensitivity.

The **separation principle** is the key theoretical result: the closed-loop poles of the combined observer-controller system are exactly the union of {eigenvalues of A − BK} (controller poles) and {eigenvalues of A − LC} (observer poles). The two sets are completely independent — you can design K as if you had full state feedback, then design L separately for desired observer speed, and the combined system will have both sets of poles without interaction. This is not obvious: you might worry that feeding estimated states x̂ (which contain error) into the control law would shift the controller poles. It doesn't, because the observer error dynamics are decoupled from the controlled state dynamics in the combined system's eigenvalue structure.

To see the combined system concretely, write the state equations for [x; e] jointly. The A-matrix of this combined system is block-triangular: [A−BK, BK; 0, A−LC]. A block-triangular matrix's eigenvalues are the union of the diagonal blocks' eigenvalues — this is the mathematical reason the separation principle holds. The resulting controller, viewed from the outside (from y to u), is a dynamic system of order n — a genuine transfer function that processes the output signal y and produces control input u. It is therefore a **dynamic compensator** in classical terms, but derived systematically from the state-space model rather than from frequency-domain intuition. This equivalence between state-space observer-controller design and classical compensator design is what connects the modern and classical control frameworks.
