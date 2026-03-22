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

## Questions

```yaml
- question: "A robot arm has position sensors but no velocity sensors. An engineer says: 'We cannot implement state feedback control because velocity is a required state variable and we cannot measure it.' What does observer theory say?"
  type: multiple-choice
  options:
    - "The engineer is correct — state feedback requires direct measurement of all states, so this system cannot use state feedback"
    - "The engineer is wrong — we can estimate velocity from position measurements using an observer and feed back the estimated states"
    - "The engineer is wrong — velocity is not a state variable in a robot arm and can be ignored"
    - "The engineer is partially right — we can use state feedback, but only if we add velocity sensors"
  answer: 1
  explanation: "This is exactly what observers are designed for. An observer (Luenberger observer) runs a parallel software model of the system, using the available output (position) to continuously correct its estimate of all states including velocity. The correction term L(y − Cx̂) drives the estimation error to zero, provided the system is observable. Once the observer has reliable state estimates, those estimates are fed back to the controller exactly as if they were direct measurements. The separation principle formalizes why this works without degrading stability."

- question: "In a Luenberger observer, what is the purpose of the correction term L(y − Cx̂)?"
  type: multiple-choice
  options:
    - "It computes the control input needed to drive the system to the desired setpoint"
    - "It amplifies the measured output signal to reduce sensor noise"
    - "It compares predicted output to actual output and nudges the state estimate toward reality"
    - "It replaces the system matrix A when states are unmeasurable"
  answer: 2
  explanation: "The term y − Cx̂ is the output prediction error: the difference between what the real system produces (y) and what the observer model predicts (Cx̂). If the state estimate is perfectly accurate, this difference is zero and no correction is needed. In practice, initial conditions are unknown and the model is imperfect, so the correction term continuously nudges the estimate toward the true state. The gain matrix L determines how aggressively the observer corrects — larger L means faster correction but greater noise amplification."

- question: "Observer poles (the eigenvalues of A − LC) can be placed at any location in the complex plane regardless of whether the system is observable."
  type: true-false
  answer: false
  explanation: "Observability is the necessary and sufficient condition for arbitrary observer pole placement — exactly as controllability is necessary and sufficient for arbitrary state feedback pole placement. If the system is not observable, there are directions in state space that cannot be inferred from the output, and no choice of L can make the estimation error converge in those directions. The duality between observability/observer design and controllability/state feedback design is fundamental: the mathematics of observer pole placement mirrors state feedback, with A − LC instead of A − BK."

- question: "Placing observer poles far to the left of the imaginary axis (fast observer) generally increases the observer's sensitivity to measurement noise."
  type: true-false
  answer: true
  explanation: "Observer speed and noise sensitivity are in fundamental tension. Placing poles far left requires a large gain matrix L, which means the observer correction term L(y − Cx̂) heavily weights the measured output. Since measurements contain noise, this amplifies high-frequency noise into the state estimate. A slow observer (poles close to the origin) produces smooth estimates but reacts sluggishly to initial errors or disturbances. The Kalman filter resolves this tradeoff optimally when noise statistics are known; for deterministic design, a common heuristic is to place observer poles 2–5 times faster than the controller poles."

- question: "Why does the estimation error in a Luenberger observer converge to zero exponentially, and what system property is required for this to be achievable?"
  type: short-answer
  answer: "The estimation error e = x − x̂ evolves according to ė = (A − LC)e. This is a linear system whose behavior is determined by the eigenvalues of A − LC (the observer poles). If L is chosen so that A − LC has all eigenvalues in the left half-plane (continuous time), the error decays exponentially to zero regardless of initial conditions. This is possible if and only if the system is observable — observability guarantees that L can be chosen to place the eigenvalues of A − LC anywhere, including in the stable left half-plane."
  explanation: "The key insight is that observer design is just eigenvalue placement for a different matrix (A − LC vs. A − BK for state feedback), and the enabling condition is the dual of controllability. Observability means every state variable leaves some trace in the output — so output measurements carry enough information to reconstruct all states over time. Without observability, some state directions are invisible to the output, and those unobservable modes cannot be stabilized by any observer."
```

## Explainer

State feedback control — placing closed-loop poles by choosing a gain matrix K — assumes you can measure all state variables directly and feed them back to the controller. In practice, this assumption fails constantly. A robot arm has position sensors but no direct velocity sensors. A chemical reactor has temperature measurements but no direct readings of reactant concentrations. An aircraft has inertial measurements but no direct measure of aerodynamic states. **Observers** (also called state estimators or Luenberger observers) solve this problem by building a parallel model of the system that runs in software and produces estimates of the unmeasurable states from the available outputs.

The construction of an observer mirrors the system equations almost exactly. If the real system evolves as ẋ = Ax + Bu with output y = Cx, the observer runs a copy: x̂̇ = Ax̂ + Bu + L(y − Cx̂). The extra term L(y − Cx̂) is the **correction term** or **observer injection**. It computes the difference between the actual output y and what the model predicts the output should be (Cx̂), then multiplies by a gain matrix L to correct the state estimate. If the model is perfect and the states are initialized correctly, y − Cx̂ = 0 and no correction is needed. In practice, initial conditions are unknown and the model is imperfect, so the correction term continuously nudges the estimate toward reality.

The dynamics of the **estimation error** e = x − x̂ follow ė = (A − LC)e. This is a linear system with matrix A − LC, and its eigenvalues — the **observer poles** — determine how fast the error decays. If you choose L so that A − LC has eigenvalues in the left half-plane (continuous) or inside the unit circle (discrete), the estimation error converges to zero exponentially regardless of initial conditions. Observability, your prerequisite concept, is the necessary and sufficient condition for this assignment to be possible: you can place the observer poles anywhere if and only if the system is observable. The mechanics of pole placement for observers are mathematically dual to state feedback pole placement — you are assigning eigenvalues of A − LC instead of A − BK, and the same techniques (matching characteristic polynomials, Ackermann's formula) apply directly.

The design tradeoff is between convergence speed and noise sensitivity. Placing observer poles far to the left (fast) makes the observer respond quickly to discrepancies — good for tracking, but large L gains amplify measurement noise, corrupting the estimates with high-frequency garbage. Placing poles close to the origin (slow) gives smooth estimates but reacts sluggishly to initial errors or disturbances. The **Kalman filter** is the optimal resolution of this tradeoff when noise statistics are known: it automatically computes the L matrix that minimizes the estimation error covariance, balancing model uncertainty against measurement noise in a principled way. For deterministic settings or when Kalman filter assumptions are too demanding, engineering judgment guides pole placement — a common rule of thumb is to set observer poles 2–5 times faster than the closed-loop controller poles, ensuring the observer tracks the true states faster than the controller acts on its estimates. The **separation principle** (which you will encounter next) formalizes why this works: under certain conditions, you can design the observer and the state feedback controller independently and combine them without stability degradation.
