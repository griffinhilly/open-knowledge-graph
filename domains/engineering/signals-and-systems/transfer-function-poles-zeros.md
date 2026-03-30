---
id: transfer-function-poles-zeros
title: Transfer Function, Poles, and Zeros
domain: engineering
course: signals-and-systems
prerequisites:
- id: laplace-transform-properties-inverse
  type: hard
- id: lti-systems-and-impulse-response
  type: hard
builds-toward:
- pole-zero-plot-stability-analysis
- frequency-response-magnitude-phase
- bode-plot-construction-interpretation
tags:
- transfer-function
- poles
- zeros
stage: advanced
status: validated
---

# Transfer Function, Poles, and Zeros

## Core Idea
The transfer function H(s) = Y(s)/X(s) is the ratio of output to input in the Laplace domain and fully characterizes a linear system. Poles are roots of the denominator (determine stability and transient response); zeros are roots of the numerator (affect frequency response shape).

## Questions

```yaml
- question: "A system has transfer function H(s) = (s + 2) / ((s + 1)(s + 3)). Which values of s are the poles of this system?"
  type: multiple-choice
  options:
    - "s = −2 only"
    - "s = −1 and s = −3"
    - "s = 1 and s = 3"
    - "s = −2 and s = 0"
  answer: 1
  explanation: "Poles are the roots of the denominator polynomial. Setting (s+1)(s+3) = 0 gives s = −1 and s = −3. The zero (root of the numerator s+2 = 0) is at s = −2. A common confusion is swapping poles and zeros; remember: denominator → poles, numerator → zeros."

- question: "A system whose transfer function has a pole at s = 2 + 3j (positive real part) will produce a bounded, stable output for any bounded input."
  type: true-false
  answer: false
  explanation: "Poles with positive real parts correspond to exponentially growing components e^(σt) with σ > 0. The output grows without bound for any non-zero initial condition or input, making the system unstable. BIBO (bounded-input bounded-output) stability requires ALL poles to lie in the open left half of the s-plane, i.e., Re(s) < 0 for every pole."

- question: "Why is the transfer function H(s) = Y(s)/X(s) useful for analyzing LTI systems, rather than working directly with convolution in the time domain?"
  type: short-answer
  answer: "Convolution in the time domain becomes multiplication in the s-domain. H(s) encodes the system's complete input-output behavior as a single rational function, so the output for any input X(s) is just Y(s) = H(s)·X(s). This algebraic multiplication is far simpler than computing a convolution integral, and the pole-zero structure directly reveals stability, natural frequencies, and frequency response without solving differential equations."
  explanation: "The convolution theorem for the Laplace transform is the mathematical reason: if y(t) = h(t)*x(t) then Y(s) = H(s)X(s). The transfer function is essentially a compressed description of the system's impulse response in a form that makes composition of systems (cascades, feedback loops) trivial to analyze."
```

## Explainer

When you studied LTI systems and impulse responses, you found that the output y(t) of any LTI system is the convolution of the input x(t) with the system's impulse response h(t): y(t) = h(t) * x(t). Convolution is powerful but computationally awkward — it requires evaluating an integral for every input. The Laplace transform eliminates this burden: convolution in time becomes multiplication in the s-domain, so Y(s) = H(s) · X(s), where H(s) is the Laplace transform of the impulse response. The **transfer function** H(s) = Y(s)/X(s) is simply this ratio — a complete algebraic description of what the system does to any input.

For a physical system governed by a linear ODE with constant coefficients, taking the Laplace transform (assuming zero initial conditions) converts the differential equation into a polynomial equation in s. The transfer function is the resulting rational function — a ratio of two polynomials in s. The denominator polynomial is called the characteristic polynomial, and its roots are the **poles** of the system. The numerator polynomial's roots are the **zeros**.

Poles determine the system's natural behavior — the modes that appear in the transient response. Each pole at s = σ + jω contributes a term e^(σt)·cos(ωt + φ) to the impulse response. If σ < 0 (pole in the left half-plane), this term decays to zero — the system is stable. If σ > 0 (pole in the right half-plane), the term grows exponentially — the system is unstable. A purely imaginary pole (σ = 0) produces sustained oscillation at frequency ω. This is why pole locations in the complex s-plane directly reveal stability without ever solving the ODE.

Zeros, the roots of the numerator, control how the system weights different frequency components of the input. A zero near the imaginary axis at jω₀ tends to attenuate signals near frequency ω₀; zeros in the right half-plane (non-minimum phase systems) introduce phase complications. For frequency response analysis (which you will study with Bode plots), you evaluate H(s) along the imaginary axis by substituting s = jω.

The pole-zero representation is the bridge between the time-domain impulse response and the frequency-domain Bode plot. A single rational function H(s) — sometimes just a few poles and zeros — completely encodes a system's stability, transient response, and frequency behavior, which is why it sits at the center of control systems analysis.
