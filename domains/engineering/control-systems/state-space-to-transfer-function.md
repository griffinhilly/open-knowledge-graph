---
id: state-space-to-transfer-function
title: State-Space to Transfer Function Conversion
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: transfer-functions-control
  type: hard
tags:
- state-space
- transfer-function
- canonical-forms
- minimal-realization
- controllable-canonical-form
- observable-canonical-form
stage: advanced
status: draft
---

# State-Space to Transfer Function Conversion

## Core Idea
State-space models (ẋ = Ax + Bu, y = Cx + Du) and transfer functions G(s) = C(sI − A)⁻¹B + D are two representations of the same linear time-invariant system, and converting between them reveals important structural properties. The transfer function is obtained from the state-space model by G(s) = C·adj(sI − A)·B/det(sI − A) + D, where det(sI − A) gives the characteristic polynomial. Canonical forms provide standardized state-space representations: controllable canonical form places the characteristic polynomial coefficients directly in the last row of A with a specific B and C structure, making controllability transparent; observable canonical form is its dual, making observability transparent. A state-space realization is minimal if and only if it is both controllable and observable, meaning no pole-zero cancellations occur and the state dimension equals the transfer function's McMillan degree. Non-minimal realizations have a higher state dimension than necessary because hidden modes (uncontrollable or unobservable states) create pole-zero cancellations that disappear from the transfer function. Converting from transfer function to state-space always yields a minimal realization when using standard canonical forms, but converting a non-minimal state-space model to a transfer function and back loses the hidden modes permanently.

## How It's Best Learned
Start with a third-order state-space model and compute the transfer function by hand using the formula G(s) = C(sI − A)⁻¹B + D, verifying with MATLAB's tf(ss(A,B,C,D)) or Python's control.ss2tf(). Then construct the controllable and observable canonical forms for the same transfer function and confirm they have identical input-output behavior but different internal state variables. Finally, take a fourth-order state-space model with an uncontrollable mode, convert to transfer function, and observe the pole-zero cancellation that reduces the order — illustrating why minimality matters.

## Common Misconceptions
- Converting from state-space to transfer function and back does not recover the original state-space model — infinitely many state-space realizations share the same transfer function, related by similarity transformations x̃ = Tx.
- Pole-zero cancellations in the transfer function do not mean the cancelled mode is gone from the physical system — it is merely unobservable or uncontrollable, and it can still be unstable, causing the internal state to diverge even while the output appears well-behaved.
- Canonical forms are not just textbook exercises — controllable canonical form is essential for state feedback pole placement and observable canonical form is essential for observer design, because they guarantee the respective structural property by construction.
