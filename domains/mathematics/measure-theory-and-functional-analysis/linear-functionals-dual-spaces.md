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
stage: expert
status: validated
---

# Linear Functionals and Dual Spaces

## Core Idea
A linear functional is a bounded linear operator f: X → ℝ (or ℂ). The dual space X* is the Banach space of all continuous linear functionals with norm ‖f‖ = sup{|f(x)| : ‖x‖ ≤ 1}. Duality is central to functional analysis.

## Questions

```yaml
- question: "The Riesz Representation Theorem states that every bounded linear functional on a Hilbert space H has the form f(x) = ⟨x, y⟩ for a unique y ∈ H. A student concludes: 'So H* and H are the same space.' What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The student is correct — H* and H are identical as sets and as normed spaces"
    - "H* is isometrically isomorphic to H, meaning there is a norm-preserving bijection, but H* is formally a distinct space whose elements are functionals, not vectors"
    - "H* is a proper subset of H for most Hilbert spaces"
    - "This isomorphism holds only for finite-dimensional Hilbert spaces"
  answer: 1
  explanation: "The Riesz theorem gives a natural isometric isomorphism between H and H*, but they are not literally the same object. H consists of vectors; H* consists of bounded linear functionals. The isomorphism says every functional can be 'identified with' a vector, and the identification preserves norms. The student's language is imprecise but points at the right idea: Hilbert spaces are 'self-dual' in this sense. Contrast this with ℓ¹, whose dual is ℓ^∞, which is a strictly larger space — very different from its original."

- question: "What is the dual space (ℓ²)*?"
  type: multiple-choice
  options:
    - "ℓ¹ — the space of absolutely summable sequences"
    - "ℓ^∞ — the space of bounded sequences"
    - "ℓ² itself — by the Riesz Representation Theorem for Hilbert spaces"
    - "c₀ — sequences converging to zero"
  answer: 2
  explanation: "ℓ² is a Hilbert space (with inner product ⟨x,y⟩ = Σ xₙȳₙ), so the Riesz Representation Theorem applies: every bounded functional on ℓ² has the form f(x) = Σ aₙxₙ for some (aₙ) ∈ ℓ², giving (ℓ²)* ≅ ℓ². The general Hölder duality rule (ℓᵖ)* ≅ ℓ^q where 1/p+1/q=1 gives 1/2+1/2=1, consistent with the self-dual answer. ℓ¹ is the dual of c₀; ℓ^∞ is the dual of ℓ¹. These are distinct cases that confirm ℓ² is exceptional."

- question: "A sequence (xₙ) converges weakly to x in a normed space X if and only if f(xₙ) → f(x) for every bounded linear functional f in X*."
  type: true-false
  answer: true
  explanation: "This is the definition of weak convergence. The weak topology on X is precisely the coarsest topology that makes every functional in X* continuous. Weak convergence is weaker than norm convergence: if ‖xₙ − x‖ → 0 (norm convergence) then f(xₙ) → f(x) for all f by continuity, but the converse fails in infinite-dimensional spaces. A standard example is the standard basis (eₙ) in ℓ², which converges weakly to 0 but has ‖eₙ‖ = 1 for all n."

- question: "If a sequence converges weakly in an infinite-dimensional Banach space, it must also converge in norm."
  type: true-false
  answer: false
  explanation: "Weak convergence does not imply norm convergence in infinite-dimensional spaces. The standard basis vectors (eₙ) in ℓ² converge weakly to 0 — for any f ∈ (ℓ²)*, represented by y ∈ ℓ², f(eₙ) = yₙ → 0 because y ∈ ℓ² means its terms go to zero. But ‖eₙ − 0‖ = ‖eₙ‖ = 1 for all n. This failure is one reason weak topology is useful: it allows sequences to 'converge' in a useful sense without the strong requirement of norm convergence, enabling compactness arguments unavailable in the norm topology."

- question: "Explain intuitively why the dual space X* can be thought of as a tool for 'testing' or 'measuring' elements of X, and why this perspective is useful in functional analysis."
  type: short-answer
  answer: "Each functional f ∈ X* extracts a single real number from any vector x ∈ X. The collection of all such measurements — the entire dual space — gives a complete picture of x: if f(x) = f(y) for all f ∈ X*, then x = y (by Hahn-Banach). Studying X through X* is like studying a physical object by all possible measurements you could take of it. This perspective is useful because dual space methods convert problems about vectors (which may be abstract functions or sequences) into problems about numbers, enabling existence proofs, compactness arguments, and optimization via duality."
  explanation: "The weak topology formalizes this: it is the topology on X induced by all the measurements in X*. Two points are 'close' in the weak topology if all functionals give nearby values on them. This topology is coarser than the norm topology, which is why weak compactness is easier to achieve — a powerful tool in proving existence theorems in PDEs, calculus of variations, and optimization."
```

## Explainer

From bounded linear operators, you know that a bounded linear map T: X → Y between Banach spaces has a well-defined operator norm ‖T‖ = sup{‖Tx‖ : ‖x‖ ≤ 1}, and that boundedness is equivalent to continuity for linear maps. A **linear functional** is just the special case where the target space Y is ℝ (or ℂ) — the simplest possible Banach space, a single line. Every bounded linear operator you studied still applies here, but collapsing the target to a scalar produces surprising richness.

The collection of all continuous linear functionals on X is called the **dual space** X*, equipped with the operator norm ‖f‖ = sup{|f(x)| : ‖x‖ ≤ 1}. This makes X* itself a Banach space — you can add functionals, scale them, take limits, and the limit of a Cauchy sequence of functionals is again a continuous functional. The dual of the dual, denoted X**, is called the **bidual**. There is always a natural isometric embedding X ↪ X** sending x to the evaluation functional "evaluate everything at x." When this embedding is surjective — when X and X** are isometrically isomorphic — X is called **reflexive**.

Concrete examples ground the abstraction. For ℓᵖ (sequences with ‖·‖_p < ∞), the dual space is ℓ^q where 1/p + 1/q = 1. Every functional on ℓᵖ looks like f(x) = Σ aₙxₙ for some fixed sequence (aₙ) in ℓ^q. For L^p(μ) spaces, the same Hölder duality holds: (L^p)* ≅ L^q. In Hilbert spaces, the **Riesz Representation Theorem** is the most elegant version: every bounded linear functional on a Hilbert space H has the form f(x) = ⟨x, y⟩ for a unique y ∈ H, and ‖f‖ = ‖y‖. The dual of a Hilbert space is the Hilbert space itself.

Duality is not merely an abstract curiosity — it is a systematic way to "test" elements of X with controlled measurements. The **weak topology** on X is exactly the coarsest topology that makes every functional in X* continuous, and weak convergence (xₙ ⇀ x) means f(xₙ) → f(x) for every f ∈ X*. This is weaker than norm convergence but often easier to establish, and it underlies compactness arguments throughout analysis. The dual space is the instrument through which you study the original space from the outside.
