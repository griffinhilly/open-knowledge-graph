---
id: state-observer-full-and-partial-observation
title: 'State Observer: Full-State and Partial Observation'
domain: engineering
course: control-systems
prerequisites:
- id: observer-based-control
  type: hard
- id: state-space-representation-control
  type: hard
builds-toward:
- output-feedback-and-dynamic-compensation
tags:
- state-estimation
- observer-design
- luenberger-observer
- measurement-equation
stage: expert
status: validated
---

# State Observer: Full-State and Partial Observation

## Core Idea
When not all states are measured, a state observer estimates them from available measurements. The observer is a copy of the system with correction term proportional to measurement error: x̂̇ = Ax̂ + Bu + L(y − ŷ). Observer gain L can place observer eigenvalues anywhere in the LHP.

## Questions

```yaml
- question: "A control engineer places the observer eigenvalues at −50 ± 5j while the closed-loop controller poles are at −5 ± 2j. What is the most significant consequence of this choice?"
  type: multiple-choice
  options:
    - "The observer will be unstable because its poles are too far into the left half-plane"
    - "The observer will converge very rapidly but will heavily amplify sensor noise in the state estimates"
    - "The observer convergence will be too slow to track the plant, causing estimation lag"
    - "The closed-loop system will be unstable because observer poles must match controller poles"
  answer: 1
  explanation: "Observer eigenvalues much further left than controller poles mean the estimation error decays very quickly — which sounds desirable, but the large observer gain L needed to achieve this amplifies measurement noise and injects it into the state estimates fed to the controller. In practice, observer poles are typically placed 3–5× faster than controller poles to balance fast convergence against noise sensitivity. There is no requirement for observer and controller poles to match; the Separation Principle allows them to be placed independently."

- question: "A student derives that the estimation error e = x − x̂ satisfies ė = (A − LC)e. What is the most important design conclusion from this equation?"
  type: multiple-choice
  options:
    - "The error depends on the control input u, so the observer gain L must be updated at each timestep"
    - "By choosing L, we can assign the eigenvalues of (A − LC) anywhere in the complex plane (given observability), controlling how fast the estimation error decays to zero"
    - "The error decays to zero only if the initial state x(0) is known exactly so that e(0) = 0"
    - "The observer gain must be chosen so that A − LC has the same eigenvalues as the open-loop plant A"
  answer: 1
  explanation: "The key insight is that the error dynamics are homogeneous and decoupled from the input u. This means the error will converge to zero regardless of initial conditions, as long as (A − LC) is stable. Because L is a free design parameter, we can perform eigenvalue placement on (A − LC) — exactly analogous to placing closed-loop poles with state feedback — to set the convergence rate. Observability is the condition that guarantees arbitrary pole placement is possible."

- question: "The Separation Principle states that when an observer is combined with a state-feedback controller, the closed-loop eigenvalues are the union of the controller poles and the observer poles, so both can be designed independently."
  type: true-false
  answer: true
  explanation: "The Separation Principle is one of the most practically important results in linear control theory. It allows the designer to split a complex output-feedback problem into two independent sub-problems: choose the feedback gain K to place the controller poles where desired, then choose the observer gain L to place the observer poles. The combined system has all those poles — they do not interact. Without the Separation Principle, designing output-feedback controllers would require simultaneously satisfying both objectives, which is far more complex."

- question: "A full-order observer reconstructs only the unmeasured states, since there is no need to estimate states that can be directly measured."
  type: true-false
  answer: false
  explanation: "A full-order observer reconstructs ALL n states, including those that are directly measured. This is computationally redundant but simpler to design. A reduced-order observer reconstructs only the unmeasured states (of dimension n minus the number of outputs), which is more efficient but more involved to derive. The naming is counterintuitive: 'full-order' refers to the order of the observer being the same as the order of the plant, not to the completeness of what is measured."

- question: "Explain the core principle of the Luenberger observer: how does the correction term L(y − ŷ) cause the state estimate to converge to the true state even when initial conditions are unknown?"
  type: short-answer
  answer: "The observer runs a parallel model of the plant: x̂̇ = Ax̂ + Bu. Without correction, errors from imperfect initial conditions would persist indefinitely. The correction injects the difference between the measured output y and the predicted output ŷ = Cx̂ back into the state equation, scaled by L. Subtracting the observer equation from the true plant equation gives the error dynamics ė = (A − LC)e. This is a homogeneous linear ODE whose solutions decay to zero if (A − LC) is stable — which can be guaranteed by appropriate choice of L (given observability). The correction term continuously pushes the estimate toward the true state: whenever the model diverges from reality, the output mismatch (y − ŷ) grows and the correction signal increases, pulling the estimate back."
  explanation: "The elegance of the Luenberger observer is that convergence is guaranteed structurally — it depends only on the eigenvalues of (A − LC), not on the specific initial error or the input trajectory. This makes observer-based control tractable and robust to uncertain initial conditions."
```

## Explainer

Recall from state-space representation that the full internal behavior of a system is captured in its state vector x. In an ideal world you could measure every state and feed them directly into a state-feedback controller. In practice, sensors are expensive, states may be physically inaccessible (internal temperature of a combustion chamber, stress inside a sealed component), or measurement noise makes direct use unreliable. The observer solves this problem by constructing an estimate x̂ that converges to the true state x over time.

The central insight is that you can run a **parallel simulation** of your system alongside the real plant. Both receive the same input u, so if your model is perfect and the initial states match, the simulated states will track the real ones exactly. The problem is that initial conditions are never perfectly known. The fix is to continuously correct the simulation using the measurement error: you observe the real output y, compute what your simulation *predicts* the output should be (ŷ = Cx̂), and use the discrepancy (y − ŷ) as a correction signal. The **observer gain matrix L** scales this correction and injects it back into the state estimate. This is the **Luenberger observer** equation: x̂̇ = Ax̂ + Bu + L(y − ŷ).

To understand why this works, subtract the observer equation from the true plant equation. The **estimation error** e = x − x̂ satisfies ė = (A − LC)e. This is a homogeneous linear system, so the error decays to zero provided (A − LC) is stable — meaning all its eigenvalues have negative real parts. Because L is a free design parameter, you can place the eigenvalues of (A − LC) anywhere you like (provided the system is **observable**), just as you could place closed-loop poles with state feedback. Choosing eigenvalues further left in the complex plane makes the observer converge faster, at the cost of amplifying sensor noise.

The **full-order observer** reconstructs all n states even though some may already be measured. A **reduced-order observer** only estimates the unmeasured states, which is more efficient but more involved to design. In the Separation Principle, when an observer is combined with a state-feedback controller to form an output-feedback compensator, the controller and observer gains can be designed independently — the poles of the closed-loop system are simply the union of the feedback poles and the observer poles. This principle is what makes observer-based control tractable: solve two smaller eigenvalue placement problems rather than one large coupled one.
