---
id: system-identification-least-squares
title: System Identification Using Least-Squares Methods
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
- id: adaptive-filtering-lms
  type: soft
tags:
- system-identification
- least-squares
- parameter-estimation
stage: advanced
status: draft
---

# System Identification Using Least-Squares Methods

## Core Idea
System identification estimates unknown parameters (filter coefficients, plant poles) from input-output measurements. Least-squares minimizes prediction error ‖y – H·θ‖², with closed-form solution θ = (H^T·H)^(–1)·H^T·y. Recursive algorithms update estimates as new data arrives. Regularization prevents overfitting to noisy data by penalizing large parameter magnitudes.

## Explainer

The fundamental problem system identification solves is this: you have a black box, you can feed it inputs and record outputs, and you want to discover the rules governing its behavior. From your transfer-function prerequisite, you know that a linear system is characterized by its poles and zeros — but that theory tells you the *form* of the model, not its *parameters*. System identification uses data to fill in the numbers. The least-squares framework turns this into a geometry problem: you are looking for the parameter vector **θ** whose predictions are as close as possible (in the squared-error sense) to the actual measurements.

The construction works by building a **regressor matrix** H, where each row captures the system's observable history at one time step. For an AR (autoregressive) model, row k contains past output values; for an ARX model it also contains past inputs. The measurement vector **y** stacks the corresponding current outputs. The system is now just a linear equation: y ≈ H·θ. This is typically overdetermined — more equations than unknowns, because you have many data points but few parameters — so there is no exact solution and you minimize the residual. The normal equations H^T·H·θ = H^T·y give the optimal **θ** directly. The invertibility of H^T·H is your prerequisite's condition for a well-posed system: if the input is not **persistently exciting** (doesn't probe all system modes), H^T·H becomes singular and the identification fails.

**Recursive least squares (RLS)** extends this to the case where data arrives sequentially. Rather than re-solving the normal equations with each new point, RLS maintains a running estimate and updates it efficiently. The update equation is a form of the Kalman filter: the new estimate equals the old estimate plus a gain times the **innovation** (the difference between what you predicted and what you actually observed). If you studied the LMS adaptive filter, you saw a stochastic approximation to gradient descent; RLS is the exact (non-stochastic) counterpart — it converges faster but requires more computation per step.

**Regularization** becomes essential when the model is complex relative to the data, or when H^T·H is nearly singular. Ridge regression (Tikhonov regularization) adds a penalty λ‖θ‖² to the cost, replacing the normal equations with (H^T·H + λI)·θ = H^T·y. The matrix H^T·H + λI is always invertible for λ > 0, providing numerical stability. The tradeoff is **bias versus variance**: larger λ shrinks parameter estimates toward zero (adding bias) but reduces sensitivity to noise (reducing variance). The optimal λ is typically chosen by cross-validation or by physical knowledge about the system's expected parameter magnitudes. This bias-variance tradeoff is the central tension in all of statistical learning, and system identification is where many engineers first encounter it concretely.
