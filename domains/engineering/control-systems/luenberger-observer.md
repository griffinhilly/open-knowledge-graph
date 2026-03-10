---
id: luenberger-observer
title: Luenberger Observer and State Estimation
domain: engineering
course: control-systems
prerequisites:
- id: controllability-and-observability
  type: hard
- id: state-feedback-pole-placement
  type: soft
- id: state-transition-matrix
  type: soft
tags:
- observer
- state-estimation
- luenberger
- separation-principle
- output-feedback
stage: advanced
status: draft
---

# Luenberger Observer and State Estimation

## Core Idea
A Luenberger observer is a dynamical system that estimates the full state vector x̂ from the available output y and known input u using the plant model: x̂̇ = Ax̂ + Bu + L(y − Cx̂), where L is the observer gain matrix chosen so that (A − LC) has stable, fast eigenvalues. The estimation error e = x − x̂ evolves as ė = (A − LC)e, decaying to zero exponentially if all eigenvalues of (A − LC) have negative real parts. By the separation principle, when a Luenberger observer is combined with a state-feedback controller (u = −Kx̂), the combined closed-loop poles are exactly the union of the independently designed controller poles and observer poles — they can be designed separately. Observer poles are conventionally placed 3–5 times faster than controller poles.

## How It's Best Learned
Design an observer for a 2nd order system by exploiting duality: observer gain L for (A, C) is the transpose of the state-feedback gain K for the dual system (Aᵀ, Cᵀ, Bᵀ). Simulate the combined observer-controller system and plot the state estimation error converging to zero.

## Common Misconceptions
- The observer maintains an internal model estimating the plant states — it does not modify the actual plant states, only the control signal computed from the estimates.
- The separation principle holds only for linear time-invariant systems; for nonlinear systems, controller and observer design generally cannot be decoupled.
- Making observer poles very fast reduces estimation lag but amplifies measurement noise in the state estimates — bandwidth of the observer should not exceed sensor noise characteristics.
