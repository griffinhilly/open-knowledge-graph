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
status: validated
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

## Questions

```yaml
- question: "An engineer records successive peak displacements of a vibrating structure: 10 mm, 7 mm, 4.9 mm. How should this system be classified?"
  type: multiple-choice
  options:
    - "Overdamped — it is clearly losing energy each cycle"
    - "Critically damped — the amplitude decays monotonically to zero"
    - "Underdamped — it oscillates with exponentially decaying amplitude"
    - "Cannot be classified without knowing the mass and stiffness separately"
  answer: 2
  explanation: "The presence of repeated oscillating peaks (10 → 7 → 4.9 mm) with decreasing amplitude is the signature of underdamped behavior (ζ < 1). Critically damped and overdamped systems do not oscillate — they return to equilibrium monotonically without crossing zero. The ratio of successive peaks (10/7 ≈ 7/4.9 ≈ 1.43) is consistent and can be used with the logarithmic decrement formula to extract ζ without knowing m, k, or c individually."

- question: "The spring stiffness of a single-DOF system is doubled while the mass remains constant. What happens to the natural frequency ω_n?"
  type: multiple-choice
  options:
    - "ω_n doubles"
    - "ω_n increases by a factor of √2"
    - "The period halves but ω_n is unchanged"
    - "ω_n is unchanged — it depends only on mass"
  answer: 1
  explanation: "The natural frequency is ω_n = √(k/m). Doubling k gives ω_n = √(2k/m) = √2 · √(k/m) — an increase by a factor of √2 ≈ 1.41. A common error is to double the result instead of taking the square root. This relationship also shows why stiffer systems (larger k) and lighter systems (smaller m) vibrate faster — both increase the ratio k/m."

- question: "A critically damped system (ζ = 1) oscillates at the damped natural frequency ω_d = ω_n√(1 − ζ²), just like an underdamped system, but with faster amplitude decay."
  type: true-false
  answer: false
  explanation: "When ζ = 1, the formula gives ω_d = ω_n√(1 − 1²) = 0. Critical damping means no oscillation at all — the system returns to equilibrium in minimum time without any oscillatory overshoot. The formula ω_d = ω_n√(1−ζ²) applies only to underdamped systems (ζ < 1). Critical damping is the boundary between oscillatory and non-oscillatory behavior, not a faster version of underdamped response."

- question: "The logarithmic decrement method allows you to measure the damping ratio ζ from experimental vibration data without independently knowing the mass, stiffness, or damping coefficient."
  type: true-false
  answer: true
  explanation: "The logarithmic decrement δ = ln(x_n/x_{n+1}) = 2πζ/√(1−ζ²) depends only on ζ. From recorded peak amplitudes, δ can be computed directly from their ratio, and ζ can then be solved algebraically. The individual values of m, k, and c are not needed — only their combination through ζ matters for the decay pattern. This makes the method extremely practical for field measurements and structural health monitoring."

- question: "Why does the damping ratio ζ (rather than the damping coefficient c) serve as the fundamental parameter for classifying a vibrating system's behavior?"
  type: short-answer
  answer: "The damping coefficient c alone does not determine behavior — a large c could be underdamped if m and k are also large, or overdamped if they are small. The damping ratio ζ = c / (2mω_n) normalizes c by the critical damping coefficient c_c = 2mω_n, making ζ dimensionless. This normalization means ζ < 1 always predicts oscillatory decay, ζ = 1 always means fastest non-oscillatory return, and ζ > 1 always means sluggish non-oscillatory return — regardless of the system's physical scale. A tiny MEMS device and a suspension bridge can both have ζ = 0.1 and their transient responses will look qualitatively identical, scaled only in amplitude and frequency."
  explanation: "This universality is what makes the single-DOF framework so powerful. The same parameter ζ classifies the behavior of a car suspension, a building under earthquake loading, a guitar string, and a circuit's step response. The framework repeats structurally for any vibrating system; only m, k, and c take different physical forms."
```

## Explainer

From your study of simple harmonic motion, you know that a restoring force proportional to displacement produces sinusoidal oscillation. Single-degree-of-freedom vibration analysis is what happens when you apply Newton's second law to a spring-mass system systematically, extract the governing parameters, and then generalize to damped systems. The architecture of the whole subject flows from a single equation of motion.

For an **undamped** spring-mass system, Newton's second law gives m*x'' = −k*x, which rearranges to m*x'' + k*x = 0. Every coefficient carries physical meaning: m is inertia (resisting acceleration) and k is stiffness (providing the restoring force). Dividing through by m gives x'' + (k/m)*x = 0, and the quantity ω_n = √(k/m) is the **natural frequency** — the rate at which the system oscillates if displaced and released. You should read ω_n physically: a stiffer spring (larger k) or lighter mass (smaller m) gives higher natural frequency. The solution x(t) = A sin(ω_n t + φ) is exactly the simple harmonic motion you already know, with amplitude A and phase φ set by initial conditions.

Adding a **dashpot** (viscous damper with constant c) introduces a velocity-proportional force: the equation becomes m*x'' + c*x' + k*x = 0. Two new parameters emerge. The **critical damping coefficient** c_c = 2m*ω_n is the value at which the system returns to equilibrium in minimum time without oscillating. The **damping ratio** ζ = c / c_c compares the actual damping to critical. The three regimes flow directly from ζ: if ζ < 1 (**underdamped**), the system oscillates at the reduced **damped natural frequency** ω_d = ω_n√(1−ζ²) with amplitude that decays as e^(−ζω_n t); if ζ = 1 (**critically damped**), the system returns to equilibrium as fast as possible with no overshoot; if ζ > 1 (**overdamped**), return is even slower and also non-oscillatory. Automobile suspensions are tuned to ζ ≈ 0.3–0.7 to balance ride comfort against unwanted oscillation.

The **logarithmic decrement** δ = ln(x_n / x_{n+1}) bridges theory and experiment. Because successive peaks of an underdamped oscillation decay by the factor e^(−ζω_n T_d) per cycle, the log of consecutive peak amplitudes directly yields ζ. This makes it practical to measure damping from recorded vibration data without ever knowing m, k, or c individually — a tool used routinely in structural health monitoring, modal testing, and machine diagnostics. The entire single-DOF framework — equation of motion, natural frequency, damping ratio, response regimes — repeats structurally for every vibrating system from a guitar string to a skyscraper; only m, k, and c take different physical forms.
