---
id: observer-state-estimation-design
title: State Observer Design and Estimation
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: controllability-and-observability
  type: hard
builds-toward:
- separation-principle-control-theory
tags:
- observer
- estimation
- state-space
- sensor
stage: advanced
status: draft
---

# State Observer Design and Estimation

## Core Idea
Not all states are measurable; observers estimate unmeasurable states from available outputs. Full-state observer reconstructs all n states from m outputs (requires observability). Observer eigenvalues are assigned like state feedback to control estimation error convergence. Faster observer response improves tracking but increases noise sensitivity. Trade-off between estimation accuracy and robustness to measurement noise.

## Explainer

State feedback control — placing closed-loop poles by choosing a gain matrix K — assumes you can measure all state variables directly and feed them back to the controller. In practice, this assumption fails constantly. A robot arm has position sensors but no direct velocity sensors. A chemical reactor has temperature measurements but no direct readings of reactant concentrations. An aircraft has inertial measurements but no direct measure of aerodynamic states. **Observers** (also called state estimators or Luenberger observers) solve this problem by building a parallel model of the system that runs in software and produces estimates of the unmeasurable states from the available outputs.

The construction of an observer mirrors the system equations almost exactly. If the real system evolves as ẋ = Ax + Bu with output y = Cx, the observer runs a copy: x̂̇ = Ax̂ + Bu + L(y − Cx̂). The extra term L(y − Cx̂) is the **correction term** or **observer injection**. It computes the difference between the actual output y and what the model predicts the output should be (Cx̂), then multiplies by a gain matrix L to correct the state estimate. If the model is perfect and the states are initialized correctly, y − Cx̂ = 0 and no correction is needed. In practice, initial conditions are unknown and the model is imperfect, so the correction term continuously nudges the estimate toward reality.

The dynamics of the **estimation error** e = x − x̂ follow ė = (A − LC)e. This is a linear system with matrix A − LC, and its eigenvalues — the **observer poles** — determine how fast the error decays. If you choose L so that A − LC has eigenvalues in the left half-plane (continuous) or inside the unit circle (discrete), the estimation error converges to zero exponentially regardless of initial conditions. Observability, your prerequisite concept, is the necessary and sufficient condition for this assignment to be possible: you can place the observer poles anywhere if and only if the system is observable. The mechanics of pole placement for observers are mathematically dual to state feedback pole placement — you are assigning eigenvalues of A − LC instead of A − BK, and the same techniques (matching characteristic polynomials, Ackermann's formula) apply directly.

The design tradeoff is between convergence speed and noise sensitivity. Placing observer poles far to the left (fast) makes the observer respond quickly to discrepancies — good for tracking, but large L gains amplify measurement noise, corrupting the estimates with high-frequency garbage. Placing poles close to the origin (slow) gives smooth estimates but reacts sluggishly to initial errors or disturbances. The **Kalman filter** is the optimal resolution of this tradeoff when noise statistics are known: it automatically computes the L matrix that minimizes the estimation error covariance, balancing model uncertainty against measurement noise in a principled way. For deterministic settings or when Kalman filter assumptions are too demanding, engineering judgment guides pole placement — a common rule of thumb is to set observer poles 2–5 times faster than the closed-loop controller poles, ensuring the observer tracks the true states faster than the controller acts on its estimates. The **separation principle** (which you will encounter next) formalizes why this works: under certain conditions, you can design the observer and the state feedback controller independently and combine them without stability degradation.
