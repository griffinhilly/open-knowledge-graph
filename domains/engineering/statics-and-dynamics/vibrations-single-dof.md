---
id: vibrations-single-dof
title: Vibrations of Single-DOF Systems
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: dynamics-newtons-second-law
  type: hard
- id: kinematics-particles-rectilinear
  type: hard
- id: simple-harmonic-motion
  type: hard
builds-toward: []
tags:
- dynamics
- vibrations
- natural frequency
- damping
- spring-mass systems
- free vibration
stage: formal-systems
status: draft
---

# Vibrations of Single-DOF Systems

## Core Idea
A single-degree-of-freedom vibrating system consists of a mass, a restoring element (spring), and optionally a damping element (dashpot). For undamped free vibration, Newton's second law yields the equation of motion m*x'' + k*x = 0, with the natural frequency omega_n = sqrt(k/m) and period tau = 2*pi/omega_n. The general solution x(t) = A*sin(omega_n*t + phi) describes simple harmonic motion. When viscous damping is added, the equation becomes m*x'' + c*x' + k*x = 0, characterized by the damping ratio zeta = c/(2*m*omega_n). If zeta < 1 (underdamped), the system oscillates with exponentially decaying amplitude at the damped frequency omega_d = omega_n*sqrt(1 - zeta^2). If zeta = 1 (critically damped) or zeta > 1 (overdamped), the system returns to equilibrium without oscillation. The logarithmic decrement delta = ln(x_n/x_{n+1}) = 2*pi*zeta/sqrt(1 - zeta^2) provides a practical way to measure damping from experimental decay data.

## How It's Best Learned
Derive the equation of motion from Newton's second law for a spring-mass-dashpot system, identify the natural frequency and damping ratio from the coefficients, and then write the solution form based on the damping regime. Work problems that ask for period, frequency, maximum displacement, and the number of cycles for amplitude to decay by a given factor. For rotational systems, draw the analogy: I*theta'' + c_t*theta' + k_t*theta = 0, with omega_n = sqrt(k_t/I).

## Common Misconceptions
- Measuring the spring displacement x from the undeformed spring length rather than from the static equilibrium position — using static equilibrium as the origin eliminates the gravity term from the equation of motion.
- Confusing natural frequency omega_n (in rad/s) with cyclic frequency f_n (in Hz) — they are related by f_n = omega_n/(2*pi).
- Assuming that any energy dissipation qualifies as viscous damping — Coulomb (dry) friction damping produces a linear amplitude decay, not exponential, and requires a different analysis.
