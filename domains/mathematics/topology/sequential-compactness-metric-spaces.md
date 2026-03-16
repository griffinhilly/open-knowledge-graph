---
id: sequential-compactness-metric-spaces
title: Sequential Compactness in Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-covers-finite-subcovers
  type: hard
- id: cauchy-sequences-metric-spaces
  type: soft
tags:
- sequential-compactness
- metric-spaces
stage: abstract-reasoning
status: draft
---

# Sequential Compactness in Metric Spaces

## Core Idea
A space is sequentially compact if every sequence has a convergent subsequence. In metric spaces, sequential compactness and compactness are equivalent (by Bolzano-Weierstrass). In general spaces they differ; infinite products can be compact but not sequentially compact (Tychonoff). This equivalence makes metric spaces special.

## Explainer

You know that a space is **compact** in the open-cover sense when every open cover has a finite subcover. This is a powerful but abstract global condition. **Sequential compactness** approaches the same idea operationally: a metric space is sequentially compact if every infinite sequence in it has a subsequence that converges to a point in the space. The Bolzano-Weierstrass theorem from calculus — every bounded sequence in ℝ has a convergent subsequence — is the prototype: a closed bounded interval in ℝ is sequentially compact.

In a general topological space, these two notions diverge. Uncountable products with the product topology (Tychonoff spaces) can be compact by Tychonoff's theorem while failing to be sequentially compact. But in the concrete setting of metric spaces they coincide: a metric space is compact if and only if it is sequentially compact. The proof that sequential compactness implies compactness uses the metric structure in an essential way — specifically, the notion of **total boundedness** (for every ε > 0, the space can be covered by finitely many ε-balls) and the **Lebesgue number lemma** (every open cover of a sequentially compact metric space has a Lebesgue number δ > 0, meaning every ball of radius δ is contained in some cover element).

Why does the equivalence matter? Sequential compactness is often much easier to verify directly. For subsets of ℝⁿ, the **Heine-Borel theorem** characterizes compact sets as exactly the closed and bounded ones — and the argument runs through sequential compactness: bounded sequences in ℝⁿ have convergent subsequences (by applying Bolzano-Weierstrass coordinate by coordinate), and closedness ensures the limit stays in the set. For infinite-dimensional function spaces, sequential compactness is harder to achieve and the **Arzelà-Ascoli theorem** provides the right criterion: a family of functions is sequentially compact in the uniform metric iff it is uniformly bounded and equicontinuous.

The broader lesson is that in metric spaces you have three equivalent formulations of compactness — open-cover compactness, sequential compactness, and complete plus totally bounded. Each is the right tool for different arguments. Open covers work for abstract topological results (continuous images of compact sets are compact). Sequential compactness is natural for analysis (proving continuous functions on compact metric spaces attain their extrema). Complete plus totally bounded is useful in function spaces. In metric spaces, you can freely switch between these descriptions to use whichever makes the proof cleanest.
