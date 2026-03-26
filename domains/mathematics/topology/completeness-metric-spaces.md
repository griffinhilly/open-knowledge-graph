---
id: completeness-metric-spaces
title: Completeness in Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: metric-topology
  type: hard
- id: cauchy-sequences-and-completeness
  type: hard
builds-toward:
- contraction-mapping-theorem
- baire-category-theorem
tags:
- completeness
- cauchy-sequences
- metric-spaces
stage: advanced
status: validated
---
# Completeness in Metric Spaces

## Core Idea
A metric space is complete if every Cauchy sequence converges. Completeness is a metric property (not purely topological) that guarantees existence of limits. Many important spaces are complete: ℝⁿ, closed subsets of complete spaces, and function spaces with appropriate metrics. Completeness enables powerful existence theorems in analysis.

## Questions

```yaml
- question: "The open interval (0, 1) with the usual metric is homeomorphic to ℝ. What does this imply about the completeness of (0, 1)?"
  type: multiple-choice
  options:
    - "Since (0, 1) and ℝ are homeomorphic, (0, 1) must also be complete"
    - "Since (0, 1) and ℝ are homeomorphic, they share all metric properties including completeness"
    - "Homeomorphism preserves topological structure, not metric structure — (0, 1) can be incomplete even though ℝ is complete"
    - "The completeness of ℝ is inherited by any subset of ℝ under the induced metric"
  answer: 2
  explanation: "Completeness is a metric property, not a purely topological one. Two spaces can be homeomorphic (topologically identical) while differing in completeness. The interval (0, 1) is homeomorphic to ℝ, but (0, 1) is incomplete under the usual metric: the sequence 1/n is Cauchy but converges to 0, which lies outside (0, 1). The real line ℝ is complete. Options A and B embody the common error of conflating metric and topological structure. Option D is false — closed subsets of complete spaces are complete, but (0, 1) is not closed in ℝ."

- question: "Consider the sequence 1, 1.4, 1.41, 1.414, 1.4142, ... of rational decimal approximations to √2. In the metric space (ℚ, |·|), which of the following is true?"
  type: multiple-choice
  options:
    - "The sequence is not Cauchy, because its terms never stabilize at a rational number"
    - "The sequence is Cauchy and converges in ℚ to the irrational number √2"
    - "The sequence is Cauchy, but it does not converge in ℚ because √2 ∉ ℚ"
    - "The sequence is Cauchy in ℝ but not in ℚ, since Cauchy-ness depends on the ambient space"
  answer: 2
  explanation: "The sequence is Cauchy in ℚ: for any ε > 0, successive terms eventually differ by less than ε (the differences go to zero). Being Cauchy depends only on whether the terms become close to each other — it does not require knowing what the limit is. However, the limit √2 is irrational, so it is not in ℚ. The sequence is Cauchy but has no limit within ℚ. This is precisely the failure of completeness: ℚ has 'holes' at irrational numbers that Cauchy sequences can fall into. Option D is wrong because Cauchy-ness uses the same distances whether you consider the sequence in ℚ or in ℝ."

- question: "Every convergent sequence in a metric space is a Cauchy sequence, but not every Cauchy sequence converges."
  type: true-false
  answer: true
  explanation: "If a sequence converges to a limit L, then for any ε > 0, terms eventually get within ε/2 of L, so they get within ε of each other — the sequence is Cauchy. The converse fails in incomplete spaces: a Cauchy sequence in ℚ may converge to an irrational number not in ℚ. In a complete metric space, the two notions coincide — every Cauchy sequence converges. This equivalence is exactly what completeness guarantees."

- question: "If two metric spaces are homeomorphic, they must have the same completeness."
  type: true-false
  answer: false
  explanation: "Homeomorphism preserves topological structure (open sets, continuity, connectedness) but not metric structure. Completeness is a metric property that depends on the specific distance function, not just the topology. The spaces (0, 1) and ℝ are homeomorphic via a continuous bijection like x → tan(π(x − 1/2)), but ℝ is complete while (0, 1) is not. You can 'change' completeness by picking a different metric or by working in a subspace — something impossible with purely topological properties."

- question: "What does it mean for a metric space to be 'complete,' and why is the rational number line ℚ a standard example of an incomplete space?"
  type: short-answer
  answer: "A metric space is complete if every Cauchy sequence in the space converges to a point that is in the space. ℚ is incomplete because it contains Cauchy sequences whose limits are irrational. For example, the sequence of rational approximations to √2 is Cauchy (terms get arbitrarily close to each other) but has no limit within ℚ, since √2 ∉ ℚ. ℚ has 'holes' at irrational numbers — these are exactly the missing limits that Cauchy sequences try to reach but cannot find."
  explanation: "The definition separates two things: (1) internal coherence of the sequence (Cauchy property — terms cluster together) and (2) existence of a limit in the space. A complete space guarantees that if terms are clustering, there is a point in the space they are clustering toward. The reals ℝ are constructed precisely to fill these holes in ℚ, making ℝ the completion of ℚ."
```

## Explainer

From your study of Cauchy sequences, you know that a sequence is **Cauchy** if its terms become arbitrarily close to each other — without referencing any particular limit. A **complete metric space** is one in which every Cauchy sequence converges to a point that is actually *in* the space. The definition separates two things that can come apart: the internal coherence of a sequence (are its terms bunching together?) and the existence of a target (is there a point in the space for them to reach?).

The canonical example of incompleteness is the rationals ℚ with the usual metric. The sequence 1, 1.4, 1.41, 1.414, ... is Cauchy — successive terms differ by less than 10⁻ⁿ — yet it converges to √2, which is not rational. The sequence is perfectly well-behaved internally, but ℚ has a "hole" at √2. The reals ℝ are exactly the completion of ℚ: every such hole is filled. From your metric topology background, you know that a metric defines an ambient space; completeness asks whether that space has any missing points that Cauchy sequences can "fall into."

Not every topological property is preserved by completeness, and vice versa. Completeness is a **metric** property, not a purely topological one. Two homeomorphic spaces can differ in completeness: (0, 1) and ℝ are homeomorphic as topological spaces (there is a continuous bijection with continuous inverse between them), but (0, 1) with the usual metric is incomplete — the sequence 1/n is Cauchy but converges to 0, which is outside (0, 1). The real line ℝ is complete. This example shows that completeness can be broken by removing points or by choosing the "wrong" metric for a space.

The power of completeness lies in the existence theorems it enables. The **Contraction Mapping Theorem** (Banach Fixed-Point Theorem) guarantees that any contraction map on a complete metric space has a unique fixed point — a statement used in differential equations, numerical analysis, and computer science to prove iterative algorithms converge. The **Baire Category Theorem** tells you that complete metric spaces cannot be written as a countable union of nowhere-dense closed sets. Both results are impossible to state without completeness. The pattern is consistent: completeness is the hypothesis you need whenever you want to show that something you have constructed "inside" the space actually lives there. It is the guarantee that your space has no gaps for limiting objects to fall through.
