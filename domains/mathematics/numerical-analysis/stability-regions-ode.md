---
id: stability-regions-ode
title: Stability Regions and A-Stability
domain: mathematics
course: numerical-analysis
prerequisites:
- id: stiff-equations
  type: hard
tags:
- stability
- a-stability
- ode
stage: formal-systems
status: draft
---

# Stability Regions and A-Stability

## Core Idea
For the test problem dy/dt = λy with Re(λ) < 0, a numerical method is stable if |y_{n+1}| ≤ |y_n|. The stability region is the set of hλ values for which the method is stable. An A-stable method (like implicit Euler or Crank-Nicolson) is stable for all hλ with Re(hλ) < 0, making it safe for stiff problems. Explicit methods have bounded stability regions, severely limiting step size for stiff systems.

## Questions

```yaml
- question: "You apply forward Euler to dy/dt = −1000y using step size h = 0.005. The exact solution decays to zero, but the numerical solution oscillates wildly and blows up. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Forward Euler cannot handle exponentially decaying solutions — it requires the exact solution to be oscillatory"
    - "The step size places hλ outside the stability region of forward Euler, causing amplification even though the exact solution decays"
    - "The step size is too small for the method to track the fast decay accurately"
    - "Forward Euler requires a special initialization procedure for stiff equations that must have failed"
  answer: 1
  explanation: "For forward Euler applied to dy/dt = λy, the stability region is |1 + hλ| ≤ 1. Here λ = −1000 and h = 0.005, so hλ = −5. Then |1 + (−5)| = 4 > 1 — outside the stability region. The method amplifies errors each step, causing blowup even though the true solution decays. This is purely a stability problem, not an accuracy problem. The exact solution is smooth and slowly varying; the issue is that hλ falls outside the stability region."

- question: "What does it mean for a numerical ODE method to be A-stable?"
  type: multiple-choice
  options:
    - "The method is stable for all step sizes h > 0 when applied to any ODE"
    - "The method's stability region includes the entire left half of the complex hλ-plane — it is stable whenever the true solution decays"
    - "The method achieves at least second-order accuracy on the test problem dy/dt = λy"
    - "The method requires no step-size restriction when applied to any linear ODE"
  answer: 1
  explanation: "A-stability means the stability region contains all hλ with Re(hλ) < 0 — the entire left half-plane. Since the test problem has Re(λ) < 0 for decaying solutions, an A-stable method is stable for ANY step size h > 0 whenever the exact solution decays. This is what makes A-stable methods (like implicit Euler and Crank-Nicolson) safe for stiff problems — you never need to restrict h for stability reasons, only for accuracy."

- question: "For a stiff ODE, an explicit method may require an extremely small step size not because the solution changes rapidly, but because a large step size places hλ outside the method's stability region."
  type: true-false
  answer: true
  explanation: "This is the defining challenge of stiff equations. The exact solution may be smooth and slowly varying, but the ODE has eigenvalues with large negative real parts. For an explicit method like forward Euler, the stability region is bounded — it only contains hλ values in a small disk near the origin. To keep hλ inside this region when Re(λ) is very large and negative, h must be tiny. This step-size restriction is imposed by stability, not by the need for accuracy."

- question: "An A-stable method is stable for all step sizes h > 0, regardless of the ODE being solved."
  type: true-false
  answer: false
  explanation: "A-stability means stability for all hλ with Re(hλ) < 0 — that is, whenever the exact solution of the linear scalar test problem dy/dt = λy is decaying. It does not mean stability for arbitrary ODEs at arbitrarily large h in all situations. For nonlinear ODEs, additional considerations apply. A-stability guarantees no step-size restriction for the class of problems defined by the test equation — not unconditional stability for all ODEs."

- question: "Explain the difference between a numerical method's stability and its accuracy for ODEs, and why A-stability specifically matters for stiff problems."
  type: short-answer
  answer: "Accuracy refers to how closely the numerical solution approximates the true solution — governed by truncation error, which depends on the order of the method and step size. Stability refers to whether the numerical solution remains bounded when the true solution is bounded — governed by whether hλ lies within the stability region. For a stiff problem, Re(λ) is very large and negative. An explicit method has a bounded stability region, so hλ must be tiny to stay inside it, even if the true solution varies slowly and large steps would be accurate enough. An A-stable method's stability region covers the entire left half-plane, so no step-size restriction is imposed by stability — h can be chosen based on accuracy alone. This is why A-stability is specifically important for stiff problems."
  explanation: "The conceptual separation of stability from accuracy is the key insight. A student who understands only accuracy might think: 'the solution decays smoothly, so any reasonable step size should work.' But stability is a separate constraint — the method can blow up not because it's missing the solution's features, but because the arithmetic of the method amplifies errors when hλ falls outside the stability region."
```
