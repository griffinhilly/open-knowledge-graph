---
id: luenberger-observer
title: Luenberger Observer and State Estimation
domain: engineering
course: control-systems
prerequisites:
- id: controllability-and-observability
  type: hard
- id: state-feedback-pole-placement
  type: soft
- id: state-transition-matrix
  type: soft
tags:
- observer
- state-estimation
- luenberger
- separation-principle
- output-feedback
stage: advanced
status: validated
---

# Luenberger Observer and State Estimation

## Core Idea
A Luenberger observer is a dynamical system that estimates the full state vector x̂ from the available output y and known input u using the plant model: x̂̇ = Ax̂ + Bu + L(y − Cx̂), where L is the observer gain matrix chosen so that (A − LC) has stable, fast eigenvalues. The estimation error e = x − x̂ evolves as ė = (A − LC)e, decaying to zero exponentially if all eigenvalues of (A − LC) have negative real parts. By the separation principle, when a Luenberger observer is combined with a state-feedback controller (u = −Kx̂), the combined closed-loop poles are exactly the union of the independently designed controller poles and observer poles — they can be designed separately. Observer poles are conventionally placed 3–5 times faster than controller poles.

## How It's Best Learned
Design an observer for a 2nd order system by exploiting duality: observer gain L for (A, C) is the transpose of the state-feedback gain K for the dual system (Aᵀ, Cᵀ, Bᵀ). Simulate the combined observer-controller system and plot the state estimation error converging to zero.

## Common Misconceptions
- The observer maintains an internal model estimating the plant states — it does not modify the actual plant states, only the control signal computed from the estimates.
- The separation principle holds only for linear time-invariant systems; for nonlinear systems, controller and observer design generally cannot be decoupled.
- Making observer poles very fast reduces estimation lag but amplifies measurement noise in the state estimates — bandwidth of the observer should not exceed sensor noise characteristics.

## Explainer

From your prerequisite work on controllability and observability, you know that a system is observable if all internal states can be inferred from output measurements. The Luenberger observer is the concrete mechanism that performs this inference — it runs a parallel model of the plant in real time, corrects its estimates using measurement residuals, and produces state estimates accurate enough to feed a state-feedback controller. Understanding it requires seeing the observer as a feedback system in its own right.

The observer dynamics are: x̂̇ = Ax̂ + Bu + L(y − Cx̂). The first two terms (Ax̂ + Bu) are just the plant model running open-loop — this would be accurate if the model were perfect and initial conditions were known. The third term is the **correction**: (y − Cx̂) is the **innovation**, the difference between what the sensor actually measures and what the model predicts the sensor should measure. L is the observer gain matrix that weights how strongly each innovation term drives each state estimate. When y = Cx̂ (model predicts measurements perfectly), no correction is needed. When they disagree, the innovation signal drives the estimates toward the true states.

To see why this converges, subtract the true plant dynamics (ẋ = Ax + Bu) from the observer dynamics. The **estimation error** e = x − x̂ satisfies ė = Ax + Bu − (Ax̂ + Bu + L(Cx − Cx̂)) = (A − LC)e. This is a homogeneous linear system — the error evolves independently of the input u. If the eigenvalues of (A − LC) all have negative real parts, the error decays to zero exponentially regardless of initial conditions. Choosing L to place those eigenvalues is exactly the pole-placement problem from state feedback, applied to the matrix (A − LC) instead of (A − BK). By duality, computing the observer gain L for the pair (A, C) is mathematically equivalent to computing a state-feedback gain K for the dual system (Aᵀ, Cᵀ, Bᵀ).

The **separation principle** is what makes observer-based control tractable in design. When you combine the observer (x̂̇ = Ax̂ + Bu + L(y − Cx̂)) with state feedback (u = −Kx̂), the closed-loop system has 2n poles: n controller poles (eigenvalues of A − BK) and n observer poles (eigenvalues of A − LC). Crucially, these can be designed *independently* — the controller design doesn't need to account for observation dynamics, and the observer design doesn't need to account for control dynamics. The observer poles are conventionally placed 3–5 times faster than the controller poles so that estimation errors decay quickly and do not distort the control response. Place them too fast, however, and the observer amplifies sensor noise into the state estimates, degrading control performance — the speed-noise tradeoff is the practical limit that real observer designs must navigate.
