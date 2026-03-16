---
id: linear-functionals-dual-spaces
title: Linear Functionals and Dual Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: bounded-linear-operators
  type: hard
builds-toward:
- hahn-banach-theorem
- hilbert-spaces-definition
tags:
- functional-analysis
- dual-spaces
stage: abstract-reasoning
status: draft
---

# Linear Functionals and Dual Spaces

## Core Idea
A linear functional is a bounded linear operator f: X → ℝ (or ℂ). The dual space X* is the Banach space of all continuous linear functionals with norm ‖f‖ = sup{|f(x)| : ‖x‖ ≤ 1}. Duality is central to functional analysis.

## Explainer

From bounded linear operators, you know that a bounded linear map T: X → Y between Banach spaces has a well-defined operator norm ‖T‖ = sup{‖Tx‖ : ‖x‖ ≤ 1}, and that boundedness is equivalent to continuity for linear maps. A **linear functional** is just the special case where the target space Y is ℝ (or ℂ) — the simplest possible Banach space, a single line. Every bounded linear operator you studied still applies here, but collapsing the target to a scalar produces surprising richness.

The collection of all continuous linear functionals on X is called the **dual space** X*, equipped with the operator norm ‖f‖ = sup{|f(x)| : ‖x‖ ≤ 1}. This makes X* itself a Banach space — you can add functionals, scale them, take limits, and the limit of a Cauchy sequence of functionals is again a continuous functional. The dual of the dual, denoted X**, is called the **bidual**. There is always a natural isometric embedding X ↪ X** sending x to the evaluation functional "evaluate everything at x." When this embedding is surjective — when X and X** are isometrically isomorphic — X is called **reflexive**.

Concrete examples ground the abstraction. For ℓᵖ (sequences with ‖·‖_p < ∞), the dual space is ℓ^q where 1/p + 1/q = 1. Every functional on ℓᵖ looks like f(x) = Σ aₙxₙ for some fixed sequence (aₙ) in ℓ^q. For L^p(μ) spaces, the same Hölder duality holds: (L^p)* ≅ L^q. In Hilbert spaces, the **Riesz Representation Theorem** is the most elegant version: every bounded linear functional on a Hilbert space H has the form f(x) = ⟨x, y⟩ for a unique y ∈ H, and ‖f‖ = ‖y‖. The dual of a Hilbert space is the Hilbert space itself.

Duality is not merely an abstract curiosity — it is a systematic way to "test" elements of X with controlled measurements. The **weak topology** on X is exactly the coarsest topology that makes every functional in X* continuous, and weak convergence (xₙ ⇀ x) means f(xₙ) → f(x) for every f ∈ X*. This is weaker than norm convergence but often easier to establish, and it underlies compactness arguments throughout analysis. The dual space is the instrument through which you study the original space from the outside.
