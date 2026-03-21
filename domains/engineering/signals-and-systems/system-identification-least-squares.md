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

## Questions

```yaml
- question: "An engineer applies least-squares system identification to a linear system, using a step-function input. The resulting H^T·H matrix is singular, making the normal equations unsolvable. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The measurement noise is too high, corrupting H^T·H"
    - "A step input is not persistently exciting — it only excites the DC (zero frequency) component and fails to probe the system's dynamic modes, making some columns of H linearly dependent"
    - "The model order is too low; adding more parameters would make H^T·H invertible"
    - "The sampling rate is too fast, causing aliasing that corrupts the regressor matrix"
  answer: 1
  explanation: "Persistent excitation is the key condition: the input must contain enough frequency content to probe all the system's modes. A step function has energy only at zero frequency (DC) — it tells you the system's steady-state gain but nothing about its dynamics (poles, resonances). This makes columns of the regressor matrix H linearly dependent, causing H^T·H to become singular (or near-singular). A system with n poles requires an input with at least n distinct frequency components to be fully identifiable. This is not a noise problem (option A) or model complexity problem (option C) — it's a fundamental identifiability condition related to input design."

- question: "You increase the regularization parameter λ in ridge regression from 0.01 to 10 for a system identification problem. What effect does this have?"
  type: multiple-choice
  options:
    - "The estimates become unbiased and the variance decreases — both improve simultaneously"
    - "The estimates become more biased (shrunk toward zero) but less sensitive to noise — a bias-variance tradeoff"
    - "The estimates become less biased and more sensitive to noise — trading variance for accuracy"
    - "Regularization has no effect on bias; it only improves the numerical conditioning of H^T·H"
  answer: 1
  explanation: "Regularization introduces a deliberate bias by pulling parameter estimates toward zero (the prior that parameters are small). In exchange, it reduces variance — the estimates are less sensitive to noise fluctuations in the data. Larger λ = more bias, less variance. At λ = 0 you have ordinary least squares (minimum bias, maximum variance). The optimal λ balances these two effects to minimize total prediction error. Option A is the key misconception: bias and variance are in fundamental tension — you cannot reduce both simultaneously by changing λ. Option D understates regularization's effect: it does both improve numerical conditioning AND introduce bias."

- question: "Least-squares system identification formulates the parameter estimation problem as an overdetermined linear system y ≈ Hθ, which typically has more equations than unknowns."
  type: true-false
  answer: true
  explanation: "This is exactly right. Each row of H corresponds to one time step of observed data (typically past inputs and outputs). A system with, say, 4 parameters to identify might have 500 rows of data — 500 equations for 4 unknowns. This overdetermined system has no exact solution (noise means y ≠ Hθ for any θ exactly), so least-squares finds the θ that minimizes the sum of squared residuals. The overdetermination is desirable: more data means a better-conditioned estimate. Underdetermined systems (fewer equations than unknowns) are far harder and not uniquely solvable without additional constraints."

- question: "If the system being identified is nonlinear, least-squares estimation will fail to produce any useful model."
  type: true-false
  answer: false
  explanation: "Least-squares identifies the best *linear* approximation to the system — which is often useful even for mildly nonlinear systems in a neighborhood around an operating point. Additionally, the least-squares framework extends to nonlinear-in-parameters models through basis expansion: the regressor matrix H can contain nonlinear functions of the inputs and past outputs (e.g., H_k = [y_{k-1}, y_{k-1}², u_{k-1}, u_{k-1}²]), and the identification problem remains linear in the unknown coefficients. Even for strongly nonlinear systems, a linear ARX or ARMAX model identified by least squares may provide a useful control-design approximation. 'Will fail' overstates the limitation considerably."

- question: "Why must the input signal be 'persistently exciting' for least-squares system identification to succeed, and what happens if this condition is violated?"
  type: short-answer
  answer: "A system with n parameters (e.g., n poles and zeros) requires that the input excites all n independent 'directions' in the frequency domain — at least n distinct frequency components. Persistent excitation ensures the regressor matrix H has full column rank, making H^T·H invertible and the normal equations uniquely solvable. If the input lacks frequency content at some modes, H^T·H becomes singular or near-singular: the identification problem has infinitely many solutions (different parameter vectors predict the data equally well), so the algorithm cannot distinguish between them. In practice, a near-singular H^T·H produces numerically unstable estimates that are highly sensitive to small noise perturbations."
  explanation: "The geometric intuition: H^T·H being invertible means the input data 'spans' the parameter space — you can see the effect of every parameter independently. If two parameters always change together in the data (because the input never separates their effects), you cannot determine them individually. Persistent excitation is the input-design condition that guarantees this geometric spanning. Practical inputs like PRBS (pseudorandom binary sequences) or sinusoidal sweeps are explicitly designed to be persistently exciting across the relevant frequency band."
```

## Explainer

The fundamental problem system identification solves is this: you have a black box, you can feed it inputs and record outputs, and you want to discover the rules governing its behavior. From your transfer-function prerequisite, you know that a linear system is characterized by its poles and zeros — but that theory tells you the *form* of the model, not its *parameters*. System identification uses data to fill in the numbers. The least-squares framework turns this into a geometry problem: you are looking for the parameter vector **θ** whose predictions are as close as possible (in the squared-error sense) to the actual measurements.

The construction works by building a **regressor matrix** H, where each row captures the system's observable history at one time step. For an AR (autoregressive) model, row k contains past output values; for an ARX model it also contains past inputs. The measurement vector **y** stacks the corresponding current outputs. The system is now just a linear equation: y ≈ H·θ. This is typically overdetermined — more equations than unknowns, because you have many data points but few parameters — so there is no exact solution and you minimize the residual. The normal equations H^T·H·θ = H^T·y give the optimal **θ** directly. The invertibility of H^T·H is your prerequisite's condition for a well-posed system: if the input is not **persistently exciting** (doesn't probe all system modes), H^T·H becomes singular and the identification fails.

**Recursive least squares (RLS)** extends this to the case where data arrives sequentially. Rather than re-solving the normal equations with each new point, RLS maintains a running estimate and updates it efficiently. The update equation is a form of the Kalman filter: the new estimate equals the old estimate plus a gain times the **innovation** (the difference between what you predicted and what you actually observed). If you studied the LMS adaptive filter, you saw a stochastic approximation to gradient descent; RLS is the exact (non-stochastic) counterpart — it converges faster but requires more computation per step.

**Regularization** becomes essential when the model is complex relative to the data, or when H^T·H is nearly singular. Ridge regression (Tikhonov regularization) adds a penalty λ‖θ‖² to the cost, replacing the normal equations with (H^T·H + λI)·θ = H^T·y. The matrix H^T·H + λI is always invertible for λ > 0, providing numerical stability. The tradeoff is **bias versus variance**: larger λ shrinks parameter estimates toward zero (adding bias) but reduces sensitivity to noise (reducing variance). The optimal λ is typically chosen by cross-validation or by physical knowledge about the system's expected parameter magnitudes. This bias-variance tradeoff is the central tension in all of statistical learning, and system identification is where many engineers first encounter it concretely.
