---
id: lp-spaces-definition
title: 'L^p Spaces: Definition and Basic Properties'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- lp-norm-metric
- banach-spaces-definition
tags:
- lp-spaces
- functional-analysis
stage: advanced
status: draft
---

# L^p Spaces: Definition and Basic Properties

## Core Idea
For 1 ≤ p ≤ ∞, the space L^p(X, μ) is the set of measurable functions with ∫|f|^p < ∞ (or ess sup |f| < ∞ for p = ∞). Functions differing on a null set are identified. L^p is a Banach space under the p-norm.

## Questions

```yaml
- question: "Suppose we define L^p(ℝ) as the set of all measurable functions with ∫|f|^p < ∞, but WITHOUT identifying functions that agree almost everywhere. The function f that equals 1 at every rational number and 0 elsewhere would then be a nonzero element with ‖f‖_p = 0. Why is this a problem?"
  type: multiple-choice
  options:
    - "It violates the triangle inequality, since ‖f + g‖_p could exceed ‖f‖_p + ‖g‖_p"
    - "It means the distance between f and the zero function is undefined"
    - "It violates the definiteness axiom of a norm, which requires ‖f‖ = 0 if and only if f = 0"
    - "It means f is not a Lebesgue-measurable function"
  answer: 2
  explanation: "A norm must satisfy ‖f‖ = 0 ⟺ f = 0 (definiteness). The function equal to 1 on ℚ and 0 on ℝ\\ℚ is nonzero as a function, yet ∫|f|^p = 0 because ℚ has measure zero. Without identification of a.e.-equal functions, we have a seminorm, not a norm. By identifying functions that agree a.e., we ensure that ‖f‖_p = 0 implies f = 0 as an L^p element — i.e., f = 0 a.e."

- question: "On the finite measure space [0,1] with Lebesgue measure, which containment relationship holds between L^p spaces for p > q ≥ 1?"
  type: multiple-choice
  options:
    - "L^q ⊆ L^p — larger exponent means larger space"
    - "L^p ⊆ L^q — larger exponent means stricter integrability condition, so L^p is smaller"
    - "L^p and L^q are always equal on finite measure spaces"
    - "Neither contains the other; the spaces intersect but neither is a subset"
  answer: 1
  explanation: "On a finite measure space, if f ∈ L^p then f ∈ L^q for all q ≤ p — the larger exponent imposes a stricter condition, so L^p ⊆ L^q. Intuitively, requiring ∫|f|^p < ∞ for larger p is a stronger constraint, since it penalizes large values of |f| more heavily. This containment reverses on infinite measure spaces like ℝ, which is why stating the measure space matters."

- question: "L^2(X, μ) is special among L^p spaces because its norm arises from an inner product, making it a Hilbert space."
  type: true-false
  answer: true
  explanation: "The inner product ⟨f, g⟩ = ∫f·ḡ dμ satisfies all inner product axioms and generates the L^2 norm via ‖f‖_2 = √⟨f,f⟩. This inner product structure enables orthogonality, Fourier expansions, and projections — geometry that makes L^2 central to signal processing, quantum mechanics, and PDE theory. For p ≠ 2, the L^p norm cannot be derived from any inner product (the parallelogram law fails), so those spaces are Banach but not Hilbert."

- question: "Every L^p space for p ≥ 1 is a Hilbert space, since Banach spaces can always be equipped with an inner product that generates their norm."
  type: true-false
  answer: false
  explanation: "Only L^2 is a Hilbert space. For p ≠ 2, the L^p norm fails the parallelogram law (‖f+g‖² + ‖f−g‖² = 2‖f‖² + 2‖g‖²), which is a necessary condition for a norm to come from an inner product. This is not merely a technical failure — L^p spaces for p ≠ 2 genuinely lack the orthogonality geometry that defines Hilbert spaces. They are complete normed spaces (Banach spaces) but not inner product spaces."

- question: "Why must elements of L^p be equivalence classes of functions (identified up to sets of measure zero) rather than individual functions? What norm property would fail otherwise?"
  type: short-answer
  answer: "Without identification, a function that is nonzero on a measure-zero set but zero almost everywhere would have L^p norm equal to zero while not being the zero function. This violates definiteness — the norm axiom that ‖f‖ = 0 if and only if f = 0. By treating two functions as the same element of L^p whenever they agree almost everywhere, we restore definiteness: ‖f‖_p = 0 implies f = 0 in the a.e. sense, which is the only sense the Lebesgue integral can distinguish."
  explanation: "This identification is natural because the Lebesgue integral is itself insensitive to sets of measure zero — altering a function on a null set changes nothing about its integral. L^p inherits this insensitivity and promotes it to an equivalence relation, making the resulting space a genuine normed vector space rather than merely a seminormed one."
```

## Explainer

From the Lebesgue integral, you know how to integrate measurable functions against a measure μ, and you know the integral is insensitive to changes on sets of measure zero. L^p spaces are built by collecting all measurable functions whose p-th power is Lebesgue integrable and packaging them into a single normed vector space. The idea is to turn the space of integrable functions into a geometric object where "distance" and "convergence" have precise meaning.

For a fixed p with 1 ≤ p < ∞, define ‖f‖_p = (∫|f|^p dμ)^(1/p). The **L^p space** L^p(X, μ) consists of all measurable functions f for which ‖f‖_p is finite. Two measurable functions define the same element of L^p if they agree μ-almost everywhere — functions that differ only on a null set are identified. This identification is essential for ‖f‖_p to be a genuine norm: without it, a nonzero function equal to zero a.e. would have ‖f‖_p = 0, violating the norm axiom. After identification, ‖f‖_p = 0 implies f = 0 as an L^p element (i.e., f = 0 a.e.).

The choice of exponent p controls which functions belong to the space and what kind of behavior is being controlled. L¹ requires the function to have a finite total area; L² requires the square to be integrable (the Hilbert space case, central to Fourier analysis and quantum mechanics); L^∞ requires the function to be essentially bounded, meaning bounded outside a null set. Larger p imposes stricter integrability conditions — roughly, functions in L^∞ must be globally tame, while L¹ tolerates spikes that decay quickly enough for their area to remain finite. These spaces are nested in different ways depending on whether the underlying measure space has finite or infinite total measure.

The crucial theorem is that L^p is a **Banach space** (a complete normed space) for every 1 ≤ p ≤ ∞. Completeness means that Cauchy sequences in the L^p norm always converge to a limit inside L^p — there are no "missing" functions. This is proved using the **Riesz-Fischer theorem**, whose key step is showing that if a series of L^p functions has summable norms, the series converges a.e. and in L^p norm. Completeness is what makes L^p spaces analytically powerful: you can pass to limits and stay inside the space.

The special case p = 2 makes L² a **Hilbert space**, because the L² norm arises from an inner product: ⟨f, g⟩ = ∫f·ḡ dμ. This inner product structure enables orthogonality, projections, and Fourier expansions — all the geometry of Hilbert spaces. For p ≠ 2, L^p is a Banach space but not a Hilbert space (the parallelogram law fails). The L^p norm for general p can be understood through **Hölder's inequality**: ∫|fg| ≤ ‖f‖_p · ‖g‖_q when 1/p + 1/q = 1, which makes p and q **conjugate exponents** and establishes the duality between L^p and L^q that is central to functional analysis.
