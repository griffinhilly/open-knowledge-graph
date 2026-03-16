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

## Explainer

From your study of eigenvalues, you know that the eigenvalues of the system matrix A determine how a linear system evolves over time: negative real parts mean the system decays, positive real parts mean it grows, and the imaginary parts set the oscillation frequency. The fundamental insight of state feedback is that if you feed the current state back through a gain matrix K and apply u = −Kx as your input, the closed-loop system matrix becomes (A − BK), not A. You have effectively *replaced* the open-loop eigenvalues with whatever eigenvalues (A − BK) has — and K is a free design parameter you choose.

**Pole placement** is the technique of choosing K to make (A − BK) have exactly the eigenvalues you want. Recall from controllability theory that a system is controllable if and only if you can steer the state from anywhere to anywhere in finite time. That condition turns out to be exactly what guarantees you can choose K to place the closed-loop poles *anywhere* in the complex plane. The Ackermann formula formalizes this: given your desired pole locations, form the desired characteristic polynomial φ(s), evaluate it at the matrix A to get φ(A), then K = eₙᵀ Cₓ⁻¹ φ(A), where Cₓ is the controllability matrix. The formula is elegant but its real value is conceptual — it shows the calculation is always possible when controllability holds.

Choosing *where* to put the poles requires connecting eigenvalue locations to time-domain behavior. From the second-order prototype, you know that the dominant poles determine settling time and overshoot: poles with damping ratio ζ ≈ 0.7 give a well-damped response, while purely real poles give the fastest response with no overshoot. The rule of thumb is to place closed-loop poles further left in the complex plane than the open-loop poles to make the system faster. But there is a direct cost: poles further left require larger gains K, which demands more control effort (bigger actuator commands), amplifies sensor noise, and makes the system more sensitive to model errors. This tradeoff — performance versus robustness and control effort — is the central engineering judgment in pole placement.

One subtle point that trips up many learners: state feedback places all the poles of the system, but it cannot move the **zeros** of the closed-loop transfer function. Zeros remain where they were in the plant. If you have a zero close to the imaginary axis or in the right half-plane, it will still shape your step response (adding undershoot, overshoot, or slow modes) even after perfect pole placement. This is why pole placement alone is not always sufficient — you need to know the zeros of your plant as well.

Finally, the full-state feedback law assumes all states x are available for measurement. In practice, you typically can only measure outputs y = Cx, a subset of the full state. This is why state feedback leads naturally to the next topic: the Luenberger observer, which reconstructs unmeasured states from outputs so the feedback law can be applied. The separation principle says you can design the controller and observer independently — pole placement for one, observer gain design for the other — and they work correctly when combined.
