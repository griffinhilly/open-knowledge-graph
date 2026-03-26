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
- id: sequential-compactness
  type: soft
tags:
- sequential-compactness
- metric-spaces
stage: advanced
status: validated
---
# Sequential Compactness in Metric Spaces

## Core Idea
A space is sequentially compact if every sequence has a convergent subsequence. In metric spaces, sequential compactness and compactness are equivalent (by Bolzano-Weierstrass). In general spaces they differ; infinite products can be compact but not sequentially compact (Tychonoff). This equivalence makes metric spaces special.

## Questions

```yaml
- question: "You want to prove that a continuous function f: X → ℝ on a compact metric space X attains its maximum. Which characterization of compactness is most directly useful?"
  type: multiple-choice
  options:
    - "Open-cover compactness, because it directly gives a finite subcover of the preimages of an open cover of ℝ"
    - "Sequential compactness: take a sequence (xₙ) with f(xₙ) → sup f; extract a convergent subsequence xₙₖ → x*; continuity gives f(x*) = sup f"
    - "Complete plus totally bounded, because totally bounded spaces have finite ε-nets"
    - "The Lebesgue number lemma, which directly bounds how large f can be"
  answer: 1
  explanation: "Sequential compactness is the natural tool here. Let M = sup{f(x) : x ∈ X}. Choose xₙ with f(xₙ) → M. By sequential compactness, (xₙ) has a convergent subsequence xₙₖ → x* ∈ X. By continuity of f, f(x*) = lim f(xₙₖ) = M, so the supremum is attained. Open-cover compactness can also prove this result but requires constructing a cover of ℝ and working backward — more indirect. Sequential compactness aligns naturally with the sequence-based argument."

- question: "What fails in general topological spaces that makes the equivalence between sequential and open-cover compactness specific to metric spaces?"
  type: multiple-choice
  options:
    - "General topological spaces do not have a well-defined notion of distance, so sequences cannot be defined"
    - "In uncountable product spaces with the product topology, Tychonoff's theorem gives compactness but the space can fail to be sequentially compact — no metric is available to extract subsequences via a diagonal argument"
    - "Open covers do not exist in non-metrizable spaces"
    - "Subsequences always converge in compact spaces regardless of topology"
  answer: 1
  explanation: "Sequences can be defined in any topological space (using nets or filters to generalize, though sequences themselves are well-defined). The issue is that in spaces without a countable base (like uncountable products), sequences are too 'thin' to detect all the topology. Tychonoff's theorem says arbitrary products of compact spaces are compact (open-cover sense), yet {0,1}^ℝ is compact but not sequentially compact — some sequences have no convergent subsequences. In metric spaces, second-countability and total boundedness are available to extract subsequences via diagonal arguments, making the equivalence possible."

- question: "A topological space is sequentially compact if and only if it is compact in the open-cover sense."
  type: true-false
  answer: false
  explanation: "This equivalence holds for metric spaces but not for general topological spaces. Counterexamples exist in both directions: (1) uncountable products of compact spaces are compact by Tychonoff's theorem but may fail to be sequentially compact (no convergent subsequences for certain sequences); (2) the ordinal space [0, ω₁) is sequentially compact (every countable sequence has a convergent subsequence) but is not compact in the open-cover sense. The equivalence in metric spaces relies on special properties: separability, total boundedness, and the ability to use diagonal arguments on sequences."

- question: "In a metric space, if every sequence has a convergent subsequence (sequential compactness), then every open cover has a finite subcover (open-cover compactness)."
  type: true-false
  answer: true
  explanation: "This is exactly the metric-space equivalence theorem. The proof uses two key metric-space tools: total boundedness (sequential compactness implies the space can be covered by finitely many ε-balls for any ε) and the Lebesgue number lemma (for a sequentially compact metric space, every open cover has a Lebesgue number δ > 0 such that every δ-ball fits inside some cover element). Combining these gives a finite subcover: cover the space with finitely many δ/2-balls, each contained in a cover element."

- question: "Why does the Heine-Borel theorem characterize compact subsets of ℝⁿ as exactly the closed and bounded sets, and how does sequential compactness underlie this?"
  type: short-answer
  answer: "Closed and bounded implies sequentially compact in ℝⁿ: any sequence in a bounded set has a convergent subsequence by the Bolzano-Weierstrass theorem (applied coordinate by coordinate), and closedness ensures the limit remains in the set. Sequential compactness implies open-cover compactness in metric spaces (including ℝⁿ). Conversely, compact implies closed (compact subsets of Hausdorff spaces are closed) and bounded (the cover by unit balls has a finite subcover, bounding the diameter). The argument runs through sequential compactness as the natural intermediate: boundedness gives subsequences, closedness captures limits, and the metric-space equivalence converts this to open-cover compactness."
  explanation: "The Heine-Borel theorem is the prototype of compactness criteria, but its proof is cleaner when routed through sequential compactness. The Bolzano-Weierstrass theorem (every bounded real sequence has a convergent subsequence) is the foundational fact, applied dimension by dimension in ℝⁿ. This is why Heine-Borel fails in infinite-dimensional spaces: in ℓ² or C([0,1]), bounded sequences need not have convergent subsequences (the unit ball is closed and bounded but not compact). Compactness in infinite dimensions requires additional conditions — like the Arzelà-Ascoli theorem's equicontinuity — beyond mere boundedness and closedness."
```

## Explainer

You know that a space is **compact** in the open-cover sense when every open cover has a finite subcover. This is a powerful but abstract global condition. **Sequential compactness** approaches the same idea operationally: a metric space is sequentially compact if every infinite sequence in it has a subsequence that converges to a point in the space. The Bolzano-Weierstrass theorem from calculus — every bounded sequence in ℝ has a convergent subsequence — is the prototype: a closed bounded interval in ℝ is sequentially compact.

In a general topological space, these two notions diverge. Uncountable products with the product topology (Tychonoff spaces) can be compact by Tychonoff's theorem while failing to be sequentially compact. But in the concrete setting of metric spaces they coincide: a metric space is compact if and only if it is sequentially compact. The proof that sequential compactness implies compactness uses the metric structure in an essential way — specifically, the notion of **total boundedness** (for every ε > 0, the space can be covered by finitely many ε-balls) and the **Lebesgue number lemma** (every open cover of a sequentially compact metric space has a Lebesgue number δ > 0, meaning every ball of radius δ is contained in some cover element).

Why does the equivalence matter? Sequential compactness is often much easier to verify directly. For subsets of ℝⁿ, the **Heine-Borel theorem** characterizes compact sets as exactly the closed and bounded ones — and the argument runs through sequential compactness: bounded sequences in ℝⁿ have convergent subsequences (by applying Bolzano-Weierstrass coordinate by coordinate), and closedness ensures the limit stays in the set. For infinite-dimensional function spaces, sequential compactness is harder to achieve and the **Arzelà-Ascoli theorem** provides the right criterion: a family of functions is sequentially compact in the uniform metric iff it is uniformly bounded and equicontinuous.

The broader lesson is that in metric spaces you have three equivalent formulations of compactness — open-cover compactness, sequential compactness, and complete plus totally bounded. Each is the right tool for different arguments. Open covers work for abstract topological results (continuous images of compact sets are compact). Sequential compactness is natural for analysis (proving continuous functions on compact metric spaces attain their extrema). Complete plus totally bounded is useful in function spaces. In metric spaces, you can freely switch between these descriptions to use whichever makes the proof cleanest.
