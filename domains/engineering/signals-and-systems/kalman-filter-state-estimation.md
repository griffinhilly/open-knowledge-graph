---
id: kalman-filter-state-estimation
title: Kalman Filter for State Estimation
domain: engineering
course: signals-and-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: random-signals-autocorrelation-psd
  type: soft
tags:
- state-estimation
- optimal-filtering
- recursive
- kalman
stage: advanced
status: draft
---

# Kalman Filter for State Estimation

## Core Idea
The Kalman filter provides optimal recursive state estimation for linear systems with white Gaussian noise. It alternates between time update (prediction from dynamics) and measurement update (correction using observations), using the innovation weighted by the Kalman gain. The filter minimizes estimation error covariance and scales efficiently to high-dimensional problems.

## Explainer

From state-space representation, you know that a dynamical system can be described as ẋ = Ax + Bu, y = Cx + Du, where x is the state vector capturing everything needed to predict future behavior. In practice you rarely have direct access to the state — you have noisy measurements y that tell you something about the state but not everything, and the system dynamics themselves are subject to random disturbances. The Kalman filter is the optimal algorithm for estimating x from y when the system is linear and the noise is Gaussian.

The filter alternates between two steps at each time instant. In the **predict** step, you project the current state estimate forward using the dynamics: x̂(k|k-1) = Ax̂(k-1|k-1) + Bu(k). You simultaneously propagate the **error covariance** matrix P — which quantifies how uncertain you are about the state — forward: P(k|k-1) = AP(k-1|k-1)Aᵀ + Q, where Q is the covariance of process noise (disturbances driving the system). This is your best guess before the new measurement arrives. In the **update** step, you see measurement y(k) and compute the **innovation**: y(k) − Cx̂(k|k-1), the discrepancy between what you measured and what you predicted. The **Kalman gain** K = P(k|k-1)Cᵀ(CP(k|k-1)Cᵀ + R)⁻¹ determines how much weight to place on the innovation, where R is the measurement noise covariance. The updated estimate is x̂(k|k) = x̂(k|k-1) + K·(innovation).

The intuition for the Kalman gain is a trust ratio. When R is small (measurements are precise), K is large and the filter aggressively corrects toward the measurement. When Q is small (the model is accurate and disturbances are tiny), K is small and the filter stays close to the prediction. The filter automatically adjusts this tradeoff based on relative uncertainties — this is what "optimal" means. A GPS/IMU navigation system illustrates this directly: when GPS fixes arrive regularly, the filter trusts them heavily; during a GPS outage (tunnel, canyon), it relies on the IMU's dynamic model to propagate position, with growing uncertainty, until the next fix arrives.

The connection to your prerequisite in random signals is that the covariance matrix P is the state-space analog of the power spectral density — it is a full statistical description of the estimation error, including how errors in different state components are correlated. For time-invariant systems, the Kalman gain converges to a steady-state value that can be precomputed by solving the **algebraic Riccati equation**, making real-time implementation efficient. Extensions handle nonlinear systems (Extended Kalman Filter linearizes around the current estimate; Unscented Kalman Filter uses a sigma-point approximation) and non-Gaussian noise (particle filters), but the linear Kalman filter is the foundational algorithm underlying all of them. Applications span aerospace navigation, robotics, financial time-series filtering, weather prediction, radar tracking, and any problem requiring optimal estimation of a hidden evolving state from partial, noisy observations.
