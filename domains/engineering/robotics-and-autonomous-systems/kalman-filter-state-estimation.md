---
id: kalman-filter-state-estimation
title: Kalman Filter and State Estimation
domain: engineering
course: robotics-and-autonomous-systems
prerequisites: []
builds-toward:
- simultaneous-localization-and-mapping
tags:
- kalman-filter
- state-estimation
- filtering
- bayesian-inference
- sensor-fusion
- extended-kalman-filter
- unscented-kalman-filter
stage: expert
status: validated
---

# Kalman Filter and State Estimation

## Core Idea
The Kalman filter estimates the hidden state of a dynamic system (e.g., robot position and velocity) given noisy measurements and a model of how the system evolves. It is optimal for linear systems with Gaussian noise, minimizing mean-squared error. The algorithm alternates between prediction (using the motion model) and measurement update (using sensor readings). The filter maintains a Gaussian belief: state estimate plus covariance matrix representing uncertainty. As measurements are incorporated, uncertainty shrinks. The Extended Kalman Filter (EKF) handles nonlinear systems by linearizing around the current state. The Unscented Kalman Filter (UKF) avoids linearization by sampling the Gaussian. Variants enable sensor fusion (combining multiple noisy sensors) and SLAM (simultaneous localization and mapping).

## How It's Best Learned
Implement a scalar Kalman filter by hand: estimate a single quantity (e.g., temperature) from noisy measurements. Compute prediction covariance, measurement update, and observation residuals. Verify that uncertainty decreases as you incorporate measurements. Extend to 2D position estimation: predict motion using a constant-velocity model, update using GPS measurements. Observe how the filter balances model predictions (which drift over time) with measurements (which are noisy). Code an EKF for a nonlinear system (e.g., robot with nonlinear odometry). Compare with UKF. Experiment with tuning process and measurement noise covariances.

## Common Misconceptions
- The Kalman filter smooths measurement noise away; it optimally trades model predictions against noisy measurements, but it cannot create information not present in either source.
- Higher measurement frequency always improves estimates; if measurements are very noisy, lower frequency with more averaging is better. The filter's Kalman gain balances these.
- The Kalman filter is guaranteed to produce correct estimates; it is optimal only if the model is accurate and noise assumptions (Gaussian, white) are satisfied. Model errors cause divergence.
- Extended Kalman Filter linearization is always accurate; for highly nonlinear systems, the EKF linearization can diverge, leading to inconsistent estimates.

## Questions

```yaml
- question: "A scalar Kalman filter estimates the current robot position x given GPS measurements z. The motion model predicts x_pred = x_prev + v·dt (constant velocity). The measurement z = x + noise_measurement has variance σ_z². The filter maintains state estimate x_est and error covariance P. After prediction, P increases (uncertainty grows due to model imperfection); after measurement update, P decreases. Why does the filter trade these two sources?"
  type: multiple-choice
  options:
    - "The prediction is always correct, and the measurement is always wrong; the filter ignores measurements and trusts predictions"
    - "The measurement is always correct, and the prediction is always wrong; the filter ignores predictions and trusts measurements"
    - "Both prediction and measurement have errors. The filter computes the Kalman gain K = P/(P + σ_z²), which weights the measurement update based on relative uncertainties: if measurement noise is large, K is small and the update is small; if prediction uncertainty is large, K is large and the update is large"
    - "The filter randomly chooses between prediction and measurement"
  answer: 2
  explanation: "The Kalman gain K = P/(P + σ_z²) is the core insight. If the prediction covariance P is large (high uncertainty), K approaches 1 and the filter trusts the measurement. If the measurement noise σ_z² is large (measurement is unreliable), K approaches 0 and the filter trusts the prediction. For example, if P = σ_z², then K = 0.5, and the update is a 50-50 blend. This optimal weighting minimizes mean-squared error."

- question: "The Extended Kalman Filter (EKF) handles nonlinear systems by linearizing the nonlinear model around the current state. In the prediction step, the Jacobian matrix F is computed (linearization of the motion model). Why is accurate computation of F critical?"
  type: multiple-choice
  options:
    - "F doesn't matter; the EKF is guaranteed to work for any nonlinear system"
    - "F must accurately approximate the local slope of the nonlinear function; if F is inaccurate (poor linearization), the predicted covariance is wrong, leading to inconsistent estimates and potential filter divergence"
    - "F is only used to make computation faster; the EKF works the same with or without it"
    - "F must be computed numerically by finite differences; analytical Jacobians are always wrong"
  answer: 1
  explanation: "The Jacobian F = ∂f/∂x at the current state determines how state uncertainties propagate through the nonlinear motion model. A poor linearization means the covariance update P_pred = F·P·F^T is inaccurate. If you overestimate (overconfident) or underestimate (too uncertain) the prediction covariance, the Kalman gain becomes suboptimal. The filter can diverge: the estimate drifts while the filter's covariance remains low, causing measurements to be ignored. Careful Jacobian computation (analytically if possible, or numerically) is essential for EKF reliability."

- question: "A robot uses a Kalman filter to estimate position from noisy GPS measurements and wheel odometry. The filter state is [x, y, θ] (position and heading). When the robot turns a sharp corner, the linearization of the motion model (used in the EKF) becomes poor. The Unscented Kalman Filter (UKF) addresses this by:"
  type: multiple-choice
  options:
    - "Using a smaller time step to improve linearization accuracy"
    - "Sampling the Gaussian belief (generating sigma points) and propagating them through the nonlinear model directly, then recomputing the Gaussian from the transformed points, avoiding explicit linearization"
    - "Using a nonlinear solver to compute the Jacobian more accurately"
    - "Switching to a particle filter, which is always more accurate"
  answer: 1
  explanation: "The UKF's key innovation: instead of linearizing the model, it generates deterministically-chosen sample points (sigma points) from the Gaussian, propagates each through the actual nonlinear model, and recomputes the Gaussian. This captures nonlinearities better than linearization, especially for sharp turns where the motion model is highly nonlinear. The price is slightly higher computation, but UKF often outperforms EKF for nonlinear systems without requiring Jacobians. It is sometimes called 'the Kalman filter without the derivatives.'"

- question: "A Kalman filter's process noise covariance Q represents uncertainty in the motion model. If Q is set too low (assuming the model is very accurate when it's not), what happens to the filter estimate?"
  type: multiple-choice
  options:
    - "The filter trusts measurements too much and responds quickly to sensor noise"
    - "The filter trusts predictions too much and ignores measurements, causing the estimate to diverge as the model error accumulates"
    - "The filter's performance is unaffected; Q is just a tuning parameter"
    - "The filter becomes numerically unstable and crashes"
  answer: 1
  explanation: "Low Q means the filter believes the prediction is very accurate. During the update step, if the measurement contradicts the prediction, the Kalman gain K becomes small (the filter trusts the prediction over the measurement). If the model is actually inaccurate, the prediction drifts, but the filter doesn't correct it enough. This causes filter divergence: the estimate deviates from reality while the filter's uncertainty remains low. Proper tuning of Q and R (measurement noise) ensures the filter balances predictions and measurements correctly."

- question: "In sensor fusion, a robot combines measurements from multiple sensors: wheel odometry (fast, drifts), GPS (slow, absolute), and an IMU (fast, biased). How does the Kalman filter handle multiple sensors with different update rates and noise characteristics?"
  type: short-answer
  answer: "The Kalman filter can handle asynchronous, multiple sensors through flexible update steps. Each sensor measurement (whenever it arrives) generates an update step. The measurement matrix H and measurement noise covariance R are specific to each sensor. For odometry: H = [1, 0, 0, ...] (direct position measurement), R_odo is small (low noise). For GPS: H = [1, 0, 0, ...] (same position), R_GPS is larger (higher noise). For IMU: H relates acceleration to position changes (indirect), R_IMU depends on IMU quality. The filter processes measurements as they arrive, updating uncertainty based on each sensor's characteristics. Fast measurements (odometry, IMU) update frequently; slower measurements (GPS) update less often but with global constraints. The fusion automatically weights each sensor based on its covariance: high-quality, low-uncertainty measurements have large influence; low-quality measurements have small influence."
  explanation: "Multi-sensor fusion is where the Kalman filter shines. By explicitly modeling each sensor's noise and update rate, you get a principled way to combine them. This is standard in autonomous vehicles (combining GPS, IMU, wheel encoders, and sometimes LiDAR and cameras)."

- question: "A particle filter is an alternative to the Kalman filter for state estimation. Unlike the Kalman filter, which assumes Gaussian distributions, the particle filter represents the belief as a set of weighted samples (particles). When would a particle filter be preferable to a Kalman filter?"
  type: true-false
  answer: true
  explanation: "Correct. Particle filters are useful when the belief distribution is non-Gaussian (multimodal, with multiple peaks) or when the system is highly nonlinear and the Gaussian assumption is very poor. However, particle filters require more computation (many particles × propagation cost) and can suffer from particle degeneracy (a few particles dominate). The Kalman filter is efficient and optimal for linear Gaussian systems. Many robotics systems use hybrid approaches: Kalman filter for primary state (linear, single mode), particle filter for discrete mode tracking (e.g., which room am I in?) or for kidnapped robot problems (where the robot's initial position is unknown and multimodal)."
```

## Explainer

A robot moving through the environment needs to know its location. Sensors provide noisy measurements: GPS has meter-level error, wheel odometry drifts over time, IMU accelerometers are biased. The challenge: fuse these imperfect measurements into a good estimate of the true state (position, velocity, orientation). The Kalman filter is the optimal solution for linear systems with Gaussian noise.

The filter maintains a **belief**: a Gaussian distribution over the state, characterized by a mean estimate and a covariance matrix representing uncertainty. It operates in two phases:

**Prediction Phase**: Using the motion model, predict the state at the next time step:
- x_pred = f(x_est, u),  where u is the control input
- P_pred = F·P·F^T + Q, where F is the Jacobian of f, and Q is the process noise covariance

The motion model predicts where the robot should be. The covariance increases (uncertainty grows) because the model is imperfect (Q accounts for this unmodeled error).

**Update (Measurement) Phase**: When a measurement z arrives, correct the estimate:
- residual: y = z - H·x_pred, where H maps state to measurement space
- Kalman gain: K = P_pred·H^T / (H·P_pred·H^T + R), where R is measurement noise covariance
- update: x_est = x_pred + K·y
- update covariance: P = (I - K·H)·P_pred

The Kalman gain K is the key: it balances the prediction and the measurement. If the prediction is very certain (P is small), K is small and the measurement is largely ignored. If the prediction is uncertain (P is large), K is large and the measurement has strong influence. Similarly, if the measurement is very noisy (R is large), K is small; if the measurement is clean (R is small), K is large.

**Optimal property**: Under linear system dynamics and Gaussian noise, the Kalman filter minimizes the mean-squared error of the estimate. This is a remarkable result: the filter automatically weights predictions and measurements optimally given their respective uncertainties.

**Extended Kalman Filter (EKF)** extends this to nonlinear systems by linearizing the motion and measurement models around the current estimate using Jacobians. The linearization introduces approximation error, which can cause divergence for highly nonlinear systems. The EKF is widely used in robotics because many systems (robot kinematics, sensor models) are only mildly nonlinear, making linear approximations reasonable.

**Unscented Kalman Filter (UKF)** avoids explicit linearization by using a clever sampling strategy: the "unscented transform" generates sigma points whose statistics match the current Gaussian belief, propagates them through the true nonlinear model, and recomputes the Gaussian from the transformed points. This often provides better accuracy than EKF for strongly nonlinear systems without requiring Jacobians.

**Practical considerations**:
- **Tuning**: Q and R must be chosen appropriately. Too low Q causes the filter to trust inaccurate predictions; too high Q causes divergence. Too low R causes sensor noise to dominate; too high R ignores good measurements. Tuning often requires empirical testing or adaptive methods.
- **Initialization**: The initial state estimate and covariance must be reasonable. A poor initial state can cause slow convergence or divergence.
- **Sensor dropout**: If a sensor fails, the Kalman filter gracefully degrades: it relies more on predictions until the sensor recovers.
- **Non-Gaussian noise**: Real measurements often have non-Gaussian tails (outliers). Robust estimation (outlier rejection, huber loss) is sometimes applied before feeding data to the filter.

**Applications**: GPS-denied navigation (using IMU and odometry), SLAM (fusing odometry and landmarks), multi-sensor fusion in autonomous vehicles, target tracking, and any scenario requiring state estimation from noisy measurements. The Kalman filter is fundamental to modern robotics and control systems.
