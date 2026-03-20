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

## Explainer

From the Lebesgue integral, you know how to integrate measurable functions against a measure μ, and you know the integral is insensitive to changes on sets of measure zero. L^p spaces are built by collecting all measurable functions whose p-th power is Lebesgue integrable and packaging them into a single normed vector space. The idea is to turn the space of integrable functions into a geometric object where "distance" and "convergence" have precise meaning.

For a fixed p with 1 ≤ p < ∞, define ‖f‖_p = (∫|f|^p dμ)^(1/p). The **L^p space** L^p(X, μ) consists of all measurable functions f for which ‖f‖_p is finite. Two measurable functions define the same element of L^p if they agree μ-almost everywhere — functions that differ only on a null set are identified. This identification is essential for ‖f‖_p to be a genuine norm: without it, a nonzero function equal to zero a.e. would have ‖f‖_p = 0, violating the norm axiom. After identification, ‖f‖_p = 0 implies f = 0 as an L^p element (i.e., f = 0 a.e.).

The choice of exponent p controls which functions belong to the space and what kind of behavior is being controlled. L¹ requires the function to have a finite total area; L² requires the square to be integrable (the Hilbert space case, central to Fourier analysis and quantum mechanics); L^∞ requires the function to be essentially bounded, meaning bounded outside a null set. Larger p imposes stricter integrability conditions — roughly, functions in L^∞ must be globally tame, while L¹ tolerates spikes that decay quickly enough for their area to remain finite. These spaces are nested in different ways depending on whether the underlying measure space has finite or infinite total measure.

The crucial theorem is that L^p is a **Banach space** (a complete normed space) for every 1 ≤ p ≤ ∞. Completeness means that Cauchy sequences in the L^p norm always converge to a limit inside L^p — there are no "missing" functions. This is proved using the **Riesz-Fischer theorem**, whose key step is showing that if a series of L^p functions has summable norms, the series converges a.e. and in L^p norm. Completeness is what makes L^p spaces analytically powerful: you can pass to limits and stay inside the space.

The special case p = 2 makes L² a **Hilbert space**, because the L² norm arises from an inner product: ⟨f, g⟩ = ∫f·ḡ dμ. This inner product structure enables orthogonality, projections, and Fourier expansions — all the geometry of Hilbert spaces. For p ≠ 2, L^p is a Banach space but not a Hilbert space (the parallelogram law fails). The L^p norm for general p can be understood through **Hölder's inequality**: ∫|fg| ≤ ‖f‖_p · ‖g‖_q when 1/p + 1/q = 1, which makes p and q **conjugate exponents** and establishes the duality between L^p and L^q that is central to functional analysis.
