---
id: lp-spaces
title: Lᵖ Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral
  type: hard
- id: vector-spaces
  type: hard
builds-toward:
- holder-inequality
tags:
- lp-spaces
- banach-spaces
stage: advanced
status: draft
---

# Lᵖ Spaces

## Core Idea
Lᵖ(μ) is the space of measurable functions with ∫|f|ᵖ dμ < ∞, identified modulo null sets, equipped with norm ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p). These are the fundamental function spaces in functional analysis and harmonic analysis.

## Explainer

From your study of vector spaces, you know that a norm is a way of measuring the "size" of an element. From the Lebesgue integral, you can integrate measurable functions. **Lᵖ spaces** combine both ideas: they are vector spaces of measurable functions, equipped with a norm built from integration. The defining idea is that f belongs to Lᵖ(μ) if the integral of |f|ᵖ is finite — meaning f is "p-th power integrable." The norm ‖f‖ₚ = (∫|f|ᵖ dμ)^(1/p) generalizes the familiar Euclidean length formula ‖v‖ = (Σvᵢ²)^(1/2) from finite dimensions by replacing the sum with an integral and the exponent 2 with p.

Different values of p emphasize different aspects of a function's behavior. **L¹** functions are simply integrable — they have finite total area. **L²** functions are square-integrable; L² is the only Lᵖ space that is also a Hilbert space (inner product space), with ⟨f, g⟩ = ∫fg dμ. This makes L² the natural home for Fourier series and quantum mechanics. **L∞** is a limiting case defined by the essential supremum: ‖f‖_∞ = inf{M : |f| ≤ M almost everywhere}, capturing the "maximum size" of a function while ignoring sets of measure zero. As p increases from 1 to ∞, the Lᵖ norm becomes increasingly sensitive to large peaks and less sensitive to the overall bulk of the function.

A key subtlety: Lᵖ functions are not individual functions but **equivalence classes** — two functions that differ only on a set of measure zero are identified as the same Lᵖ element. This is necessary to make the norm nondegenerate (‖f‖ₚ = 0 should imply f is "zero," but a function that is nonzero only on a null set has zero norm). This identification is philosophically natural in measure theory, where "almost everywhere" is the operative notion of truth.

The most important structural fact is that Lᵖ spaces are **Banach spaces** — complete normed vector spaces, meaning every Cauchy sequence converges to an element of the same space. Completeness is what makes Lᵖ spaces analytically tractable: limits of sequences stay in the space. The containment relationships between Lᵖ spaces depend on whether the measure space has finite or infinite total measure, but on a probability space (μ(X) = 1), we have the inclusion L∞ ⊆ Lq ⊆ Lp ⊆ L¹ whenever p ≤ q. These spaces, together with Hölder's inequality (your next topic), form the backbone of modern analysis.
