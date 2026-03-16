---
id: state-space-canonical-forms
title: 'State-Space Canonical Forms: Controllable and Observable Forms'
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: transfer-function-derivation-differential-equations
  type: soft
builds-toward:
- state-transformation-similarity-transform
- observability-controllability-tests
- pole-placement-observer-design
tags:
- state-space
- canonical-forms
- controllable
- observable
stage: abstract-reasoning
status: draft
---

# State-Space Canonical Forms: Controllable and Observable Forms

## Core Idea
Controllable canonical form (companion form) reveals system controllability; observable canonical form reveals observability. Both are unique representations of the same system, obtained via similarity transformations. Canonical forms simplify controller and observer design by placing A, B, C matrices in special patterns where pole placement is straightforward.

## Explainer

When you first write a state-space model (x′ = Ax + Bu, y = Cx + Du), the A, B, and C matrices depend on which physical variables you chose as states. Rotate to a different basis — a different choice of state variables — and you get a different-looking but mathematically equivalent model. The key insight is that infinitely many state-space representations correspond to the same input-output transfer function. **Canonical forms** are special, standardized choices of that basis that reveal structural properties of the system and make design calculations tractable.

**Controllable canonical form** (also called companion form) restructures the model so that the A matrix takes on a companion matrix pattern — its last row contains the coefficients of the characteristic polynomial — while B is a simple column vector with a 1 in the last entry. This form makes it immediately obvious whether you can drive all modes from the input, and it makes **pole placement** by state feedback nearly mechanical: because the feedback gain vector directly modifies the coefficients of the characteristic polynomial, choosing desired closed-loop poles tells you exactly what gains to use.

**Observable canonical form** is the dual: it places A in a companion pattern and C in a simple row vector, making it straightforward to design a **Luenberger observer** (a reconstructor for unmeasured states). The duality between controllability and observability — a deep result in linear systems — means that the mathematics of observer design in observable canonical form mirrors exactly the mathematics of controller design in controllable canonical form. If you understand one, you understand both.

The conversion between your original state-space model and a canonical form is performed via a **similarity transformation**: x = Tx̃, where T is an invertible matrix. The new matrices are Ã = T⁻¹AT, B̃ = T⁻¹B, C̃ = CT. The eigenvalues — the poles of the system — are invariant under similarity transformations, so the transfer function is unchanged. To find T for controllable canonical form, you construct the controllability matrix [B, AB, A²B, …, Aⁿ⁻¹B] and use it to solve for T; for observable canonical form, you use the observability matrix similarly.

The practical payoff is this: canonical forms reduce the messy bookkeeping of general-purpose matrices to clean algebraic manipulation. When your A matrix is a companion matrix, choosing feedback gains to achieve desired pole locations is direct coefficient matching rather than solving a large linear system. This is why canonical forms appear so prominently in state-feedback and observer design — they are not just theoretical curiosities but workhorses of control system implementation.
