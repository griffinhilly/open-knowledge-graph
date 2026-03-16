---
id: state-space-analysis-realization
title: State-Space Representation and Realization
domain: engineering
course: signals-and-systems
prerequisites:
- id: transfer-function-poles-zeros
  type: hard
tags:
- state-space
- system-representation
- control
stage: advanced
status: draft
---

# State-Space Representation and Realization

## Core Idea
State-space representation uses first-order differential (or difference) equations: ẋ = Ax + Bu, y = Cx + Du. This form generalizes to MIMO systems, handles initial conditions naturally, and is preferred for numerical simulation and control design. Realization converts transfer functions into canonical state-space forms (observable, controllable, diagonal).

## Explainer

You already know that transfer functions characterize a system by its poles and zeros — the roots that determine stability and frequency response. But transfer functions describe only the input-output relationship, hiding any internal structure of the system. The **state-space representation** makes that internal structure explicit. The **state vector** x captures all the information needed to predict the system's future behavior given future inputs — it is the system's "memory" at each instant.

The four matrices have clear physical roles. **A** (the system matrix) governs how the state evolves on its own — its eigenvalues are the poles of the system, directly linking state-space to the transfer function picture you already know. **B** (the input matrix) specifies how each input channel drives each state variable. **C** (the output matrix) extracts the measured outputs from the state. **D** (the feedthrough matrix) models any direct path from input to output that bypasses the dynamics — it contributes a constant term to the transfer function at high frequency. Together, the transfer function H(s) = C(sI - A)⁻¹B + D shows exactly how A, B, C, D encode the pole-zero information from your earlier work.

The power of state-space becomes clear with MIMO (multiple-input, multiple-output) systems. A transfer function matrix for a MIMO system is unwieldy; a state-space model is a single unified description regardless of how many inputs and outputs are involved. State-space also handles initial conditions naturally — if x(0) ≠ 0, the response includes the homogeneous solution Ae^{At}x(0), capturing how stored energy at t=0 affects the output. Transfer functions implicitly assume zero initial conditions.

**Realization** is the inverse problem: given a transfer function H(s), find matrices A, B, C, D that produce it. The answer is not unique — many state-space models share the same transfer function. Canonical realizations are standardized choices. The **controllable canonical form** places the denominator polynomial coefficients directly in the last row of A, making the connection to the transfer function explicit and ensuring every state can be driven by the input. The **observable canonical form** is its transpose dual. The **diagonal (modal) form** diagonalizes A so each state variable evolves independently as a decoupled mode — particularly useful when the poles are distinct, since each diagonal entry of A is a pole and the system's behavior decomposes mode by mode. These canonical forms are the bridge between the frequency-domain analysis you know and the matrix-based world of modern control design.
