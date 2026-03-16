---
id: lp-norm-metric
title: L^p Norm and Metric Structure
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-spaces-definition
  type: hard
- id: metric-spaces-definition
  type: soft
builds-toward:
- holders-inequality
- minkowski-inequality-lp
tags:
- lp-spaces
- norms
stage: abstract-reasoning
status: draft
---

# L^p Norm and Metric Structure

## Core Idea
The L^p norm ‖f‖_p = (∫|f|^p dμ)^(1/p) defines a metric d(f,g) = ‖f - g‖_p on L^p. Proving this is a norm requires Minkowski's inequality, making L^p a normed (hence metric) space.

## Explainer

You already know what L^p(μ) is as a set — equivalence classes of measurable functions f where ∫|f|^p dμ is finite. Now the question is: can we measure *distance* between functions in this space? Defining a sensible notion of "how far apart" two functions are is what turns L^p from a mere set into a space with geometric structure.

For 1 ≤ p < ∞, the **L^p norm** is defined as ‖f‖_p = (∫|f|^p dμ)^(1/p). The case p = 2 is the most familiar: ‖f‖₂ = (∫f² dμ)^(1/2) is a direct analog of the Euclidean length formula ‖v‖ = √(v₁² + ... + vₙ²), with integrals replacing sums over coordinates. For p = 1, ‖f‖₁ = ∫|f| dμ is simply the total area under |f|. For p = ∞, the norm becomes ‖f‖_∞ = ess sup|f| — the essential supremum, the smallest bound that holds almost everywhere.

To be a genuine norm, ‖·‖_p must satisfy three axioms: (1) ‖f‖_p = 0 if and only if f = 0 a.e., (2) ‖cf‖_p = |c|‖f‖_p for scalars c, and (3) the **triangle inequality** ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p. The first two are immediate from the definition. The triangle inequality is **Minkowski's inequality**, and its proof is non-trivial — it requires Hölder's inequality as a lemma. Without Minkowski's inequality, d(f, g) = ‖f − g‖_p would not be a metric, and L^p would not be a normed space.

Once the norm is established, the metric d(f, g) = ‖f − g‖_p follows automatically. Different values of p capture different notions of closeness. Small L¹ distance means the total area between f and g is small — the functions could differ dramatically on a tiny set. Small L^∞ distance means f and g are uniformly close everywhere. The parameter p interpolates between these extremes: larger p penalizes large local deviations more heavily, making the norm increasingly sensitive to spikes. This flexibility makes the L^p family essential across analysis, probability, and partial differential equations.
