---
id: discrete-time-control-systems
title: Discrete-Time Control Systems
domain: engineering
course: control-systems
prerequisites:
- id: digital-control-intro
  type: hard
- id: laplace-transform-control
  type: soft
tags:
- z-transform
- zero-order-hold
- pulse-transfer-function
- z-domain-stability
- discretization
- sampling-theorem
stage: advanced
status: draft
---

# Discrete-Time Control Systems

## Core Idea
Discrete-time control systems operate on sampled signals x[k] = x(kT) and are analyzed using the z-transform, where the transfer function H(z) = Y(z)/U(z) describes the input-output relationship in the z-domain. The zero-order hold (ZOH) models the digital-to-analog conversion that holds each computed control value constant between samples, and the ZOH-equivalent pulse transfer function G(z) = (1 − z⁻¹)·Z{G(s)/s} captures both the continuous plant dynamics and the hold effect. Stability in the z-domain requires all closed-loop poles to lie strictly inside the unit circle |z| = 1, analogous to the left half-plane requirement in the s-domain. The mapping z = e^{sT} relates s-plane and z-plane pole locations: the imaginary axis in the s-plane maps to the unit circle, the left half-plane maps to the interior of the unit circle, and the negative real s-axis maps to the interval (0, 1) on the real z-axis. Jury's stability criterion or the bilinear transformation w = (z − 1)/(z + 1) followed by Routh-Hurwitz can assess z-domain stability without computing roots explicitly. Discrete-time root locus and Bode plot techniques mirror their continuous-time counterparts but use the unit circle and the z = e^{jωT} frequency mapping respectively, with the critical frequency being the Nyquist frequency ω_s/2 = π/T.

## How It's Best Learned
Discretize a well-understood continuous-time system (e.g., a second-order plant with known pole locations) using the ZOH method at several sampling rates. Plot the z-plane pole locations alongside the original s-plane poles and verify the z = e^{sT} mapping. Design a discrete PID controller directly in the z-domain using root locus on the pulse transfer function, then simulate the closed-loop step response and compare with the continuous-time design to observe intersample ripple and latency effects.

## Common Misconceptions
- The z-transform is not simply the Laplace transform with z substituted for s — the z-transform is defined for sequences x[k], not continuous signals, and the relationship z = e^{sT} means the z-plane wraps the s-plane vertically with period jω_s, causing aliasing of high-frequency dynamics.
- A continuous-time system with poles on the negative real axis does not map to z-plane poles on the negative real z-axis — it maps to the positive real interval (0, 1), while negative real z-axis poles correspond to oscillatory s-plane modes at half the sampling frequency.
- Increasing the sampling rate does not always improve discrete-time controller performance — excessively fast sampling can amplify quantization noise, increase computational load, and approach the numerical precision limits of the controller hardware without meaningful performance benefit beyond a certain point.
