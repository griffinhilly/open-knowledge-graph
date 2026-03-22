---
id: state-feedback-pole-placement
title: State Feedback and Pole Placement
domain: engineering
course: control-systems
prerequisites:
- id: controllability-and-observability
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: root-locus-method
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
builds-toward:
- luenberger-observer
tags:
- pole-placement
- state-feedback
- ackermann
- full-state-feedback
- regulator
stage: advanced
status: validated
---

# State Feedback and Pole Placement

## Core Idea
Full state feedback uses the control law u = −Kx to shape the eigenvalues of the closed-loop system matrix (A − BK) to any desired locations in the s-plane, arbitrarily assigning all closed-loop poles provided the system is controllable. Ackermann's formula K = eₙᵀ C_c⁻¹ φ(A) provides a closed-form expression for the gain vector, where φ(A) is the desired characteristic polynomial evaluated at the system matrix. Desired pole locations are chosen based on time-domain performance specifications (via the second-order prototype relationships) or LQR optimization. Full state feedback requires that all states be measurable — in practice a state observer must be combined with the controller.

## How It's Best Learned
Implement pole placement using scipy.signal.place_poles() for several plants and simulate closed-loop step responses to verify performance matches the specification implied by the chosen pole locations. Understand Ackermann's formula conceptually but use numerical tools for orders above 3.

## Common Misconceptions
- Placing poles further left makes the system faster but demands larger control effort and greater sensitivity to model parameter uncertainty — there is always a tradeoff.
- State feedback places closed-loop poles (eigenvalues of A−BK) but cannot move the zeros of the closed-loop transfer function, which still influence the step response shape.
- Ackermann's formula is educationally instructive but numerically poorly conditioned for high-order systems — dedicated numerical algorithms (place(), acker()) should be used in practice.

## Questions

```yaml
- question: "A control engineer designs a state feedback gain K that places all closed-loop poles at locations far into the left half-plane, achieving very fast settling. During physical implementation, what is the most likely practical problem?"
  type: multiple-choice
  options:
    - "The system will become unstable because eigenvalues with large negative real parts cause exponential growth"
    - "The controller will require very large actuator commands, amplify sensor noise, and be highly sensitive to model parameter errors"
    - "The closed-loop zeros will shift to the right half-plane, introducing instability through the zero dynamics"
    - "Ackermann's formula will become singular and fail to produce a valid gain vector for poles that far left"
  answer: 1
  explanation: "The fundamental pole-placement tradeoff: poles further left in the s-plane mean faster response, but require larger gains K. Larger K amplifies u = −Kx, demanding more actuator authority, amplifying any sensor noise present in x, and making the closed-loop behavior highly sensitive to errors in the model of A and B. Option C is the key misconception: state feedback places poles (eigenvalues of A−BK) but cannot affect the zeros of the closed-loop transfer function — they remain where they were in the open-loop plant."

- question: "A state feedback gain K is designed for a fully controllable plant, placing all closed-loop poles at well-damped locations in the left half-plane. Despite this, the closed-loop step response shows a significant undershoot before rising to the setpoint. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The pole placement calculation was performed incorrectly, leaving one pole in the right half-plane"
    - "The system has a right-half-plane zero that state feedback cannot relocate, which causes undershoot independently of the pole locations"
    - "The desired poles were not placed far enough into the left half-plane to overcome the initial transient"
    - "The Ackermann formula is only approximate, leaving residual eigenvalues near the imaginary axis"
  answer: 1
  explanation: "State feedback modifies the characteristic polynomial (denominator of the transfer function) but not the zeros (numerator roots). A right-half-plane zero causes non-minimum-phase behavior — the step response initially moves in the wrong direction (undershoot) regardless of how well the poles are placed. This is why knowing the zeros of your plant is essential before designing any controller: pole placement solves the pole problem completely but is powerless against zeros."

- question: "If a linear system is not fully controllable, no choice of gain matrix K can place all of the closed-loop eigenvalues at arbitrary desired locations."
  type: true-false
  answer: true
  explanation: "Controllability is exactly the condition that guarantees arbitrary pole placement. Uncontrollable modes correspond to directions in state space that the input u cannot reach — the control law u = −Kx cannot influence those eigenvalues regardless of K. In terms of the Ackermann formula, the controllability matrix C_c is singular for an uncontrollable system, making K undefined. The physical interpretation is that some part of the system dynamics is decoupled from the input and therefore cannot be modified by state feedback."

- question: "State feedback pole placement can be applied directly even when the system states are not directly measured, as long as the number of measured outputs equals the number of states."
  type: true-false
  answer: false
  explanation: "Full state feedback requires that all states x(t) be available for measurement — the control law is u = −Kx, which requires knowing x. When only outputs y = Cx are available (a subset or transformation of the states), you cannot compute −Kx directly, regardless of how many outputs there are. The solution is to pair the state feedback law with a Luenberger observer (state estimator) that reconstructs x from y. The separation principle guarantees that the controller and observer can be designed independently and combined correctly — but the observer is always necessary when states are unmeasured."

- question: "Why can state feedback arbitrarily place closed-loop poles but not closed-loop zeros, and what practical consequence does this have for step response design?"
  type: short-answer
  answer: "State feedback changes the closed-loop system matrix from A to (A−BK), which changes the characteristic polynomial and thus the poles (eigenvalues). The zeros of the closed-loop transfer function depend on the plant's B, C, and D matrices — specifically, on the numerator polynomial — which state feedback does not modify. Since K only appears in the denominator (through the characteristic polynomial of A−BK), the numerator (and thus the zeros) is invariant to K. Practically, this means right-half-plane zeros (causing undershoot) and imaginary-axis zeros (causing sustained oscillation in the numerator) persist after even perfect pole placement, limiting achievable step response shapes without additional design techniques."
  explanation: "This zero-invariance insight leads directly to more advanced techniques: zero-placement requires a different structure (e.g., output feedback with additional degrees of freedom, or two-degree-of-freedom controllers). It also motivates checking plant zeros as a first step in any pole-placement design — if the zeros are problematic, pole placement alone cannot fix the step response."
```

## Explainer

From your study of eigenvalues, you know that the eigenvalues of the system matrix A determine how a linear system evolves over time: negative real parts mean the system decays, positive real parts mean it grows, and the imaginary parts set the oscillation frequency. The fundamental insight of state feedback is that if you feed the current state back through a gain matrix K and apply u = −Kx as your input, the closed-loop system matrix becomes (A − BK), not A. You have effectively *replaced* the open-loop eigenvalues with whatever eigenvalues (A − BK) has — and K is a free design parameter you choose.

**Pole placement** is the technique of choosing K to make (A − BK) have exactly the eigenvalues you want. Recall from controllability theory that a system is controllable if and only if you can steer the state from anywhere to anywhere in finite time. That condition turns out to be exactly what guarantees you can choose K to place the closed-loop poles *anywhere* in the complex plane. The Ackermann formula formalizes this: given your desired pole locations, form the desired characteristic polynomial φ(s), evaluate it at the matrix A to get φ(A), then K = eₙᵀ Cₓ⁻¹ φ(A), where Cₓ is the controllability matrix. The formula is elegant but its real value is conceptual — it shows the calculation is always possible when controllability holds.

Choosing *where* to put the poles requires connecting eigenvalue locations to time-domain behavior. From the second-order prototype, you know that the dominant poles determine settling time and overshoot: poles with damping ratio ζ ≈ 0.7 give a well-damped response, while purely real poles give the fastest response with no overshoot. The rule of thumb is to place closed-loop poles further left in the complex plane than the open-loop poles to make the system faster. But there is a direct cost: poles further left require larger gains K, which demands more control effort (bigger actuator commands), amplifies sensor noise, and makes the system more sensitive to model errors. This tradeoff — performance versus robustness and control effort — is the central engineering judgment in pole placement.

One subtle point that trips up many learners: state feedback places all the poles of the system, but it cannot move the **zeros** of the closed-loop transfer function. Zeros remain where they were in the plant. If you have a zero close to the imaginary axis or in the right half-plane, it will still shape your step response (adding undershoot, overshoot, or slow modes) even after perfect pole placement. This is why pole placement alone is not always sufficient — you need to know the zeros of your plant as well.

Finally, the full-state feedback law assumes all states x are available for measurement. In practice, you typically can only measure outputs y = Cx, a subset of the full state. This is why state feedback leads naturally to the next topic: the Luenberger observer, which reconstructs unmeasured states from outputs so the feedback law can be applied. The separation principle says you can design the controller and observer independently — pole placement for one, observer gain design for the other — and they work correctly when combined.
