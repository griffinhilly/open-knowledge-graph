---
id: state-transformation-similarity-transform
title: State Transformations and Similarity Transformations
domain: engineering
course: control-systems
prerequisites:
- id: state-space-canonical-forms
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
builds-toward:
- observability-controllability-tests
- pole-placement-observer-design
tags:
- state-transformation
- similarity-transform
- change-of-basis
- invariants
stage: abstract-reasoning
status: draft
---

# State Transformations and Similarity Transformations

## Core Idea
State transformations x̄ = Tx change the state-space representation but not the input-output behavior. Ā = TAT⁻¹, B̄ = TB, C̄ = CT⁻¹. Similarity transformations preserve eigenvalues, transfer function, and controllability/observability properties. Diagonalization and modal forms are special cases used to decouple and simplify analysis.

## Explainer

The state-space representation of a system is not unique — there are infinitely many valid state-space descriptions that all produce identical input-output behavior. From your prerequisite on canonical forms, you already know that the same system can be written in controllable canonical form, observable canonical form, or other special structures. A **similarity transformation** is the mathematical operation that converts between these representations: replace the state vector x with a new state vector x̄ = Tx, where T is any invertible matrix. The transformed matrices Ā = TAT⁻¹, B̄ = TB, and C̄ = CT⁻¹ describe the same physical system in a new coordinate basis.

Why do eigenvalues survive the transformation? From your prerequisite on eigenvalues and eigenvectors, if Av = λv, then (TAT⁻¹)(Tv) = TAv = T(λv) = λ(Tv). The same scalar eigenvalue λ appears in the transformed system, with eigenvector Tv. Because the poles of the transfer function are precisely the eigenvalues of A, and because system stability depends only on pole locations, similarity transformations leave stability completely unchanged. Controllability and observability are also preserved — a system that can be driven from any initial state remains fully controllable after any coordinate change.

The most powerful application is **diagonalization**. If A has n linearly independent eigenvectors v₁, v₂, ..., vₙ, then choosing T = [v₁ v₂ ... vₙ] (the matrix whose columns are eigenvectors) transforms A into a diagonal matrix Λ = diag(λ₁, λ₂, ..., λₙ). In this **modal form**, each transformed state equation decouples: ẋ̄ᵢ = λᵢx̄ᵢ + B̄ᵢu. Mode i evolves independently of all others, controlled only by its own eigenvalue and input coupling. This makes analysis and simulation vastly simpler — you can study each mode of the system in isolation rather than solving a coupled system.

The deeper implication is that similarity transformations are a change of basis in state space, exactly analogous to rotating coordinate axes in geometry. Just as the distance between two points does not depend on which coordinate system you use to measure it, the input-output behavior of a dynamical system does not depend on which state variables you choose to represent it. Different canonical forms are simply convenient coordinate choices tailored to different analysis tasks: controllable canonical form facilitates pole placement, observable canonical form facilitates observer design, and diagonal form decouples the dynamics for modal analysis. The invariants — eigenvalues, transfer function, controllability/observability — are the true system properties, independent of the basis.
