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
builds-toward:
- luenberger-observer
tags:
- pole-placement
- state-feedback
- ackermann
- full-state-feedback
- regulator
stage: advanced
status: draft
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
