---
id: state-space-representation-control
title: State-Space Representation
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: soft
- id: matrices-intro
  type: hard
- id: differential-equations-intro-separable
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-transformations
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: applications-linear-algebra-modeling
  type: hard
builds-toward:
- state-transition-matrix
- controllability-and-observability
tags:
- state-space
- state-variables
- A-matrix
- MIMO
- modern-control
stage: expert
status: validated
---

# State-Space Representation

## Core Idea
State-space representation describes a dynamical system using first-order matrix differential equations: ẋ = Ax + Bu, y = Cx + Du, where x is the state vector, u is the input, y is the output, and A, B, C, D are constant system matrices. Unlike transfer functions, state-space models naturally represent MIMO (multiple-input, multiple-output) systems and capture all internal dynamics including unobservable or uncontrollable modes. The eigenvalues of the A matrix are the system's natural frequencies (closed-loop poles). State variables are not unique — any invertible linear transformation yields an equivalent representation with different A, B, C matrices but identical input-output behavior.

## How It's Best Learned
Practice converting second-order differential equations into companion-form state space, then verify by computing H(s) = C(sI−A)⁻¹B + D and confirming it matches the original transfer function. Implement state-space simulations using scipy.signal.StateSpace.

## Common Misconceptions
- State variables need not be physical quantities — they are mathematical constructs chosen to make equations first-order, and infinitely many valid choices exist for the same system.
- Transfer functions can miss uncontrollable or unobservable modes that cancel in the ratio Y(s)/U(s); state-space models expose all internal dynamics.
- The D matrix (direct feedthrough) is zero for strictly proper systems (more denominator poles than numerator zeros), which includes most physical plants.

## Questions

```yaml
- question: "For the state-space system ẋ = Ax + Bu, y = Cx + Du, what do the eigenvalues of the A matrix represent?"
  type: multiple-choice
  options:
    - "The steady-state output values for a given constant input"
    - "The system's natural modes and poles — they determine stability and the character of the transient response"
    - "The number of independent inputs the system can accept simultaneously"
    - "The DC gain from each input to each output"
  answer: 1
  explanation: "The eigenvalues of A are the poles of the system — they are the values of s where det(sI - A) = 0, which is the characteristic equation. Eigenvalues with negative real parts correspond to stable decaying modes; positive real parts indicate instability; imaginary parts produce oscillation. This is exactly the same information as the poles of the transfer function H(s) = C(sI-A)⁻¹B + D."

- question: "For a given physical system, there is exactly one valid set of state variables, and those variables should correspond to measurable physical quantities like position and velocity."
  type: true-false
  answer: false
  explanation: "State variables are not unique. Any invertible linear transformation T applied to a valid state vector x yields new state variables x̃ = Tx, with transformed matrices Ã = TAT⁻¹, B̃ = TB, C̃ = CT⁻¹ — a different but equally valid representation of the same system. The input-output behavior (transfer function) is identical for all equivalent representations. State variables are mathematical constructs chosen for computational convenience, not necessarily tied to physical quantities."

- question: "What can a state-space model reveal about a system that a transfer function might conceal?"
  type: short-answer
  answer: "A transfer function can have pole-zero cancellations that hide internal modes that are either uncontrollable (inputs cannot excite them) or unobservable (they don't affect outputs). These hidden modes still exist in the physical system and can cause problems — an unobservable unstable mode means the system will blow up even though the transfer function appears stable. State-space models expose all internal dynamics, including these hidden modes."
  explanation: "The transfer function H(s) = Y(s)/U(s) is formed by a ratio where cancellations can occur. If a mode is both uncontrollable and unobservable, it appears as a pole-zero pair that cancels, vanishing from H(s). The state-space A matrix retains all eigenvalues, making every mode visible. This is why controllability and observability analysis is done in state-space, not from the transfer function."
```

## Explainer

You already know how to describe a linear system using a transfer function H(s) = Y(s)/U(s) — a ratio of polynomials in the Laplace variable s. Transfer functions work well for single-input, single-output (SISO) systems, but they hit two walls: they cannot naturally represent systems with multiple inputs and outputs (MIMO), and they can hide internal dynamics that cancel in the ratio. State-space representation solves both problems by working directly in the time domain with first-order matrix differential equations.

The key move is variable selection. Any differential equation of order n can be rewritten as n first-order equations by introducing state variables. For a second-order mechanical system mẍ + bẋ + kx = u, define x₁ = x (position) and x₂ = ẋ (velocity). Then ẋ₁ = x₂ and ẋ₂ = (u − bx₂ − kx₁)/m, which you write compactly as ẋ = Ax + Bu. The state vector [x₁, x₂] is the system's complete "memory" — given the current state and all future inputs, you can compute all future outputs. This is the fundamental role of the state: it separates the past from the future.

The A matrix is the heart of the representation. Its eigenvalues are the system's natural frequencies — the poles. An eigenvalue with negative real part corresponds to a stable, decaying mode. A positive real part means that mode grows without bound: instability. Complex conjugate eigenvalues with nonzero imaginary parts produce oscillation. These are exactly the poles you know from transfer functions, which is not a coincidence: the poles of H(s) = C(sI−A)⁻¹B + D are precisely the eigenvalues of A. The two representations are equivalent for what they predict about input-output behavior.

Where they diverge is in what they hide. A transfer function is formed by a ratio, and ratios can cancel. If a mode is uncontrollable — no input signal can excite it — and unobservable — it never appears in the output — then it cancels as a pole-zero pair in H(s) and becomes invisible. That mode still exists physically, and if it is unstable, the real system will diverge even while your transfer-function model predicts stability. State-space models retain all eigenvalues of A regardless of cancellations, making every internal mode visible. This is why stability analysis, controllability, and observability are always done in state-space.

One liberating insight is that state variables are not unique. Applying any invertible matrix T to the state vector gives new state variables x̃ = Tx, with different system matrices Ã = TAT⁻¹, B̃ = TB, C̃ = CT⁻¹, but the identical transfer function. Different choices of state variables are called different realizations of the same system. Companion form is good for reading off coefficients. Modal form (diagonalizing A) decouples the system into independent modes. Balanced realization is useful for model reduction. The freedom to choose is a tool, not an ambiguity.
