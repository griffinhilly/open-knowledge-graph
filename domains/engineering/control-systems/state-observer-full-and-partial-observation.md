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
stage: advanced
status: draft
---

# State Observer: Full-State and Partial Observation

## Core Idea
When not all states are measured, a state observer estimates them from available measurements. The observer is a copy of the system with correction term proportional to measurement error: x̂̇ = Ax̂ + Bu + L(y − ŷ). Observer gain L can place observer eigenvalues anywhere in the LHP.

## Explainer

Recall from state-space representation that the full internal behavior of a system is captured in its state vector x. In an ideal world you could measure every state and feed them directly into a state-feedback controller. In practice, sensors are expensive, states may be physically inaccessible (internal temperature of a combustion chamber, stress inside a sealed component), or measurement noise makes direct use unreliable. The observer solves this problem by constructing an estimate x̂ that converges to the true state x over time.

The central insight is that you can run a **parallel simulation** of your system alongside the real plant. Both receive the same input u, so if your model is perfect and the initial states match, the simulated states will track the real ones exactly. The problem is that initial conditions are never perfectly known. The fix is to continuously correct the simulation using the measurement error: you observe the real output y, compute what your simulation *predicts* the output should be (ŷ = Cx̂), and use the discrepancy (y − ŷ) as a correction signal. The **observer gain matrix L** scales this correction and injects it back into the state estimate. This is the **Luenberger observer** equation: x̂̇ = Ax̂ + Bu + L(y − ŷ).

To understand why this works, subtract the observer equation from the true plant equation. The **estimation error** e = x − x̂ satisfies ė = (A − LC)e. This is a homogeneous linear system, so the error decays to zero provided (A − LC) is stable — meaning all its eigenvalues have negative real parts. Because L is a free design parameter, you can place the eigenvalues of (A − LC) anywhere you like (provided the system is **observable**), just as you could place closed-loop poles with state feedback. Choosing eigenvalues further left in the complex plane makes the observer converge faster, at the cost of amplifying sensor noise.

The **full-order observer** reconstructs all n states even though some may already be measured. A **reduced-order observer** only estimates the unmeasured states, which is more efficient but more involved to design. In the Separation Principle, when an observer is combined with a state-feedback controller to form an output-feedback compensator, the controller and observer gains can be designed independently — the poles of the closed-loop system are simply the union of the feedback poles and the observer poles. This principle is what makes observer-based control tractable: solve two smaller eigenvalue placement problems rather than one large coupled one.
