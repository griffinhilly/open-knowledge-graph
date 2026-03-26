---
id: characteristic-equation-and-stability
title: Characteristic Equation and Closed-Loop Stability
domain: engineering
course: control-systems
prerequisites:
- id: poles-zeros-stability-analysis
  type: hard
- id: feedback-control-fundamentals
  type: hard
- id: characteristic-polynomial
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- natural-frequency-damping-second-order
- routh-hurwitz-criterion
tags:
- characteristic-equation
- stability
- poles
- closed-loop
stage: expert
status: validated
---

# Characteristic Equation and Closed-Loop Stability

## Core Idea
The characteristic equation is formed from the closed-loop transfer function denominator (1 + loop gain = 0). Its roots are the closed-loop poles, which determine stability: all roots must be in the left half-plane for BIBO stability. The characteristic equation connects open-loop plant and controller parameters to closed-loop pole locations, making it the central equation for analyzing how design choices affect stability.

## Questions

```yaml
- question: "A control engineer must stabilize an unstable robotic arm with open-loop transfer function G(s) = 1/(s − 1). She adds a proportional controller C(s) = K and closes the loop with unity feedback. What is the minimum gain K that achieves closed-loop stability?"
  type: multiple-choice
  options:
    - "Any positive K will stabilize the system, since feedback always moves poles toward the left half-plane"
    - "K > 1, because the characteristic equation s − 1 + K = 0 places the closed-loop pole at s = 1 − K, which is negative only when K > 1"
    - "K < 1, because a small gain is needed to avoid exciting the unstable mode"
    - "The system cannot be stabilized with a proportional controller because the open-loop pole at s = +1 is inherently unstable"
  answer: 1
  explanation: "The closed-loop characteristic equation is 1 + K·G(s) = 1 + K/(s−1) = 0, giving s − 1 + K = 0, so the closed-loop pole is at s = 1 − K. For left-half-plane stability: 1 − K < 0 requires K > 1. With K ≤ 1, the pole is at s ≥ 0 — unstable or marginally stable. This illustrates two key points: (1) the characteristic equation, not the open-loop poles, governs closed-loop stability, and (2) feedback CAN stabilize an unstable plant, but only with sufficient gain. Option A is the most tempting misconception — feedback does not automatically improve stability; it depends on design parameters."

- question: "A unity-feedback system has plant G(s) = 2/(s² + 3s + 2) and proportional controller C(s) = K. An engineer wants to find all values of K for which the closed-loop system is stable. What is the correct first step?"
  type: multiple-choice
  options:
    - "Find the poles of G(s) and check whether they are all in the left half-plane"
    - "Compute the closed-loop transfer function T(s) and analyze the roots of its numerator"
    - "Form the characteristic equation 1 + K·G(s) = 0 and analyze the roots of the resulting polynomial as a function of K"
    - "Compute the open-loop frequency response and apply the Nyquist stability criterion"
  answer: 2
  explanation: "Closed-loop stability depends on the roots of the closed-loop denominator, which is 1 + K·G(s) — the characteristic equation. The poles of G(s) (option A) are the open-loop poles, which change when the loop is closed; checking them says nothing about closed-loop stability. The numerator of T(s) (option B) contains the closed-loop zeros, which affect response shape but not stability. Option D (Nyquist) is a valid stability method but is equivalent to analyzing the characteristic equation — and forming the characteristic polynomial directly is the more direct algebraic approach for this problem type."

- question: "An open-loop unstable plant (with poles in the right half-plane) can be stabilized by closing a feedback loop with an appropriate controller, because the characteristic equation 1 + G(s)C(s) = 0 can have roots in different locations than the open-loop poles."
  type: true-false
  answer: true
  explanation: "Feedback fundamentally alters the system's effective dynamics. The closed-loop poles — roots of 1 + G(s)C(s) = 0 — are generally different from the open-loop poles of G(s) alone. For example, G(s) = 1/(s−1) has an open-loop pole at s = +1 (unstable), but with K > 1, the closed-loop pole moves to s = 1−K < 0 (stable). Stabilization of inherently unstable plants (aircraft, inverted pendulums, chemical reactors) is one of the primary engineering reasons to use feedback control. The characteristic equation is the tool that shows exactly which controller parameters achieve this."

- question: "Adding more gain to a stable feedback system generally makes it more robust, because a larger controller output provides stronger corrective action against disturbances."
  type: true-false
  answer: false
  explanation: "High gain can destabilize a stable closed-loop system. As gain K increases, the characteristic equation's roots trace paths in the complex plane (the root locus). For many plants, this path crosses into the right half-plane at a critical gain K_c — beyond which the system oscillates with growing amplitude and is unstable. For example, G(s) = 1/(s(s+1)(s+2)) is stable for small K but becomes unstable beyond a critical gain found from Routh-Hurwitz analysis. 'More gain = more stability' is a common and dangerous misconception. The characteristic equation must be analyzed over the full range of design parameters, not just at a single operating point."

- question: "Explain why the closed-loop stability of a feedback system cannot be determined by simply checking whether the open-loop plant poles are in the left half-plane."
  type: short-answer
  answer: "Closing a feedback loop creates a new effective system with different pole locations. The closed-loop poles are the roots of the characteristic equation 1 + G(s)C(s) = 0, not the poles of G(s) alone. An open-loop stable plant can become unstable when high gain or poor controller design pushes the characteristic equation's roots into the right half-plane — the closed-loop poles migrate as controller parameters change. Conversely, an open-loop unstable plant can be stabilized by feedback that moves the roots into the left half-plane. The open-loop poles are simply the roots of G(s)'s denominator; the characteristic equation creates a new denominator (1 + G(s)C(s)) whose roots govern the closed-loop natural modes and hence stability."
  explanation: "The intuitive confusion arises because students think of a 'stable plant' as intrinsically safe. But stability is a property of the closed-loop system, not the plant in isolation. Feedback fundamentally rewrites the system's characteristic equation — and the engineer's job is to ensure the new equation's roots are where desired. This is the entire motivation for techniques like root locus, Routh-Hurwitz, and Nyquist analysis: all are tools for analyzing the characteristic equation."
```

## Explainer

From your prerequisite on poles, zeros, and stability, you know that a system's poles determine its natural behavior: left-half-plane poles decay (stable), right-half-plane poles grow (unstable), and imaginary-axis poles oscillate without decaying (marginally stable). From feedback control fundamentals, you know that closing a feedback loop changes the effective system — the closed-loop transfer function is not the same as the open-loop plant. The **characteristic equation** is the algebraic tool that captures this change and lets you analyze stability without computing the full closed-loop response.

Consider a standard negative feedback loop: a plant G(s) and controller C(s) in the forward path, with unity feedback. The closed-loop transfer function is T(s) = G(s)C(s) / (1 + G(s)C(s)). The denominator is 1 + G(s)C(s). Setting the denominator equal to zero — **1 + G(s)C(s) = 0**, or equivalently G(s)C(s) = −1 — is the **characteristic equation**. Its solutions are the closed-loop poles. The connection to eigenvalues from your linear algebra prerequisite is exact: for a state-space model ẋ = Ax, the characteristic equation is det(sI − A) = 0, and its roots are the eigenvalues. Stability means all eigenvalues (poles) lie in the left half-plane.

The power of the characteristic equation is that it expresses closed-loop pole locations as a function of open-loop parameters. Suppose your controller is a simple gain K, so C(s) = K. Then the characteristic equation is 1 + K·G(s) = 0. If G(s) = 1/(s(s+2)), this becomes s² + 2s + K = 0. As K varies from 0 to ∞, the roots of this quadratic trace paths in the complex plane — this is the conceptual basis of the root locus method. For any specific K, you can ask: are both roots in the left half-plane? For this example, the roots are s = −1 ± √(1−K). When K < 1, two real negative roots (stable). When K = 1, a repeated root at s = −1 (stable, critically damped). When K > 1, complex roots with real part −1 (stable, underdamped). The characteristic equation tells you all of this without ever computing the full step response.

The characteristic equation also reveals why feedback control is not always stabilizing. Some plants have open-loop poles in the right half-plane. Feedback can move those poles to the left half-plane — this is the stabilization objective. But too much gain (high K) or poor controller design can push otherwise stable poles into the right half-plane. The characteristic equation is the precise tool for identifying which values of design parameters keep all closed-loop poles in the left half-plane. Everything downstream — Routh-Hurwitz criterion, root locus, and gain/phase margins — is a technique for answering this question efficiently for different types of systems.
