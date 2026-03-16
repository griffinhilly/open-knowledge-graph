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
stage: advanced
status: draft
---

# Characteristic Equation and Closed-Loop Stability

## Core Idea
The characteristic equation is formed from the closed-loop transfer function denominator (1 + loop gain = 0). Its roots are the closed-loop poles, which determine stability: all roots must be in the left half-plane for BIBO stability. The characteristic equation connects open-loop plant and controller parameters to closed-loop pole locations, making it the central equation for analyzing how design choices affect stability.

## Explainer

From your prerequisite on poles, zeros, and stability, you know that a system's poles determine its natural behavior: left-half-plane poles decay (stable), right-half-plane poles grow (unstable), and imaginary-axis poles oscillate without decaying (marginally stable). From feedback control fundamentals, you know that closing a feedback loop changes the effective system — the closed-loop transfer function is not the same as the open-loop plant. The **characteristic equation** is the algebraic tool that captures this change and lets you analyze stability without computing the full closed-loop response.

Consider a standard negative feedback loop: a plant G(s) and controller C(s) in the forward path, with unity feedback. The closed-loop transfer function is T(s) = G(s)C(s) / (1 + G(s)C(s)). The denominator is 1 + G(s)C(s). Setting the denominator equal to zero — **1 + G(s)C(s) = 0**, or equivalently G(s)C(s) = −1 — is the **characteristic equation**. Its solutions are the closed-loop poles. The connection to eigenvalues from your linear algebra prerequisite is exact: for a state-space model ẋ = Ax, the characteristic equation is det(sI − A) = 0, and its roots are the eigenvalues. Stability means all eigenvalues (poles) lie in the left half-plane.

The power of the characteristic equation is that it expresses closed-loop pole locations as a function of open-loop parameters. Suppose your controller is a simple gain K, so C(s) = K. Then the characteristic equation is 1 + K·G(s) = 0. If G(s) = 1/(s(s+2)), this becomes s² + 2s + K = 0. As K varies from 0 to ∞, the roots of this quadratic trace paths in the complex plane — this is the conceptual basis of the root locus method. For any specific K, you can ask: are both roots in the left half-plane? For this example, the roots are s = −1 ± √(1−K). When K < 1, two real negative roots (stable). When K = 1, a repeated root at s = −1 (stable, critically damped). When K > 1, complex roots with real part −1 (stable, underdamped). The characteristic equation tells you all of this without ever computing the full step response.

The characteristic equation also reveals why feedback control is not always stabilizing. Some plants have open-loop poles in the right half-plane. Feedback can move those poles to the left half-plane — this is the stabilization objective. But too much gain (high K) or poor controller design can push otherwise stable poles into the right half-plane. The characteristic equation is the precise tool for identifying which values of design parameters keep all closed-loop poles in the left half-plane. Everything downstream — Routh-Hurwitz criterion, root locus, and gain/phase margins — is a technique for answering this question efficiently for different types of systems.
