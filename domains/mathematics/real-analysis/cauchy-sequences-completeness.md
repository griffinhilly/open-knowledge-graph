---
id: cauchy-sequences-completeness
title: Cauchy Sequences and Completeness
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- metric-space-topology
tags:
- cauchy
- completeness
- convergence
stage: advanced
status: validated
---

# Cauchy Sequences and Completeness

## Core Idea
A sequence (aₙ) is Cauchy if for every ε > 0, there exists N such that n, m > N implies |aₙ - aₘ| < ε. In ℝ, a sequence converges if and only if it is Cauchy. This characterization requires no knowledge of the limit beforehand, making it powerful for existence proofs. ℝ is 'complete' because Cauchy sequences always converge.

## Questions

```yaml
- question: "The Cauchy criterion is especially powerful for proving convergence in cases where:"
  type: multiple-choice
  options:
    - "The sequence is monotone and bounded, so the limit equals the supremum of the sequence"
    - "The sequence oscillates but eventually enters a bounded region"
    - "A limit exists but cannot be written in closed form — the Cauchy criterion requires no knowledge of the limit beforehand"
    - "The sequence is defined recursively and each term can be computed explicitly"
  answer: 2
  explanation: "The standard convergence definition requires knowing a candidate limit L and showing terms eventually stay within ε of L. Many deep existence proofs in analysis deal with limits that cannot be expressed in closed form — the whole point is to prove the limit exists without constructing it. The Cauchy criterion sidesteps this by asking only whether later terms cluster together, with no reference to any external target. Options A and D describe situations where the limit can be found or computed, which don't require the Cauchy criterion's special advantage."

- question: "The sequence 3, 3.1, 3.14, 3.141, 3.1415, … (successive rational approximations of π) is:"
  type: multiple-choice
  options:
    - "Cauchy in ℚ and convergent in ℚ, since the terms are clearly approaching a limit"
    - "Cauchy in ℚ but not convergent in ℚ, since π is irrational and does not exist in ℚ"
    - "Not Cauchy in ℚ because the differences between consecutive terms never reach exactly zero"
    - "Convergent in ℚ by the completeness of the rational numbers"
  answer: 1
  explanation: "The sequence is Cauchy in ℚ: for any ε > 0, all terms beyond some index are within ε of each other (they share many decimal places). But the only candidate limit is π, which is irrational — it is not in ℚ. A Cauchy sequence in ℚ has no obligation to converge in ℚ. This is the essential incompleteness of ℚ: it has 'holes' at the irrationals. Option D is wrong — ℚ is NOT complete, which is exactly the point of this example."

- question: "A sequence can be Cauchy without knowing its limit — the Cauchy property depends only on the mutual distances between terms, with no reference to any external target value."
  type: true-false
  answer: true
  explanation: "This is the defining feature that makes the Cauchy criterion useful. The condition |aₙ - aₘ| < ε for all n, m > N is an intrinsic property of the sequence: it only looks at how terms relate to each other, not to any external point. By contrast, the standard convergence definition |aₙ - L| < ε requires specifying L in advance. In ℝ, the two conditions are equivalent — but the Cauchy formulation is often the one you can verify when the limit is unknown."

- question: "Completeness is a theorem that can be derived from axioms shared by both ℝ and ℚ — it is not a fundamental property that distinguishes one number system from another."
  type: true-false
  answer: false
  explanation: "Completeness is one of the *defining* properties of ℝ, not a consequence of more basic axioms. ℚ satisfies the ordered field axioms just as ℝ does, but ℚ is not complete. Completeness is the additional axiom that distinguishes ℝ from ℚ — it was included in the construction of ℝ (via Dedekind cuts or Cauchy completion) precisely to plug the holes that ℚ leaves. You cannot prove completeness of ℝ from axioms that ℚ also satisfies."

- question: "What does it mean for a space to be 'complete,' and why does the rational number system ℚ fail this property?"
  type: short-answer
  answer: "A space is complete if every Cauchy sequence in it converges to a point in it — there are no 'holes' that Cauchy sequences can fall into. ℚ fails completeness because it contains Cauchy sequences whose natural limit is irrational. For example, the decimal approximations of √2 form a sequence where terms get arbitrarily close to each other (Cauchy), but their limit √2 is not rational — it does not exist in ℚ. The sequence 'wants' to converge but has nowhere to go within ℚ. ℝ was constructed specifically to ensure every such hole is filled."
  explanation: "Completeness is not an abstract nicety — it is what makes analysis work. Without completeness, you cannot be sure that objects defined as limits actually exist. The entire architecture of real analysis (intermediate value theorem, Riemann integral, etc.) depends on ℝ having no holes."
```

## Explainer

From ε-N convergence you know what it means for a sequence to converge to a limit L: for every ε > 0, the terms eventually stay within ε of L. But that definition has a built-in limitation — you need to *know L in advance*. Many of the deepest existence proofs in analysis require showing a limit exists without being able to write it down explicitly. The **Cauchy criterion** solves this: instead of asking "are the terms close to some target?", ask "are the terms close to *each other*?" If n, m > N implies |aₙ - aₘ| < ε, the sequence is **Cauchy** — and in ℝ, that is enough to guarantee convergence.

The intuition is that a sequence which keeps "settling down" — where later terms cluster together more and more tightly — must be approaching something. Crucially, being Cauchy makes no reference to a limit; it is an intrinsic property of the sequence itself. In ℝ, the two conditions are equivalent: convergence implies Cauchy (easy to prove using the triangle inequality), and Cauchy implies convergence (the hard direction, which uses the completeness of ℝ). The proof of the hard direction constructs a candidate limit using the Bolzano-Weierstrass theorem and then verifies it works.

**Completeness** is the property that makes this equivalence hold. Not every number system is complete. Consider the rational numbers ℚ: the sequence 1, 1.4, 1.41, 1.414, 1.4142, … (decimal approximations of √2) is Cauchy in ℚ — terms get arbitrarily close to each other — but it does not converge in ℚ, because its limit √2 is irrational. ℚ has "holes." ℝ was constructed precisely to plug those holes: every Cauchy sequence of real numbers converges to a real number. This is not a theorem you prove from more basic facts about ℝ — it is one of the *defining* properties of the real number system.

The Cauchy criterion is the standard tool for proving convergence when the limit cannot be computed explicitly. It also generalizes beautifully: the concept of a **complete metric space** (a central topic in metric space topology) is defined by exactly this property — every Cauchy sequence converges. The real line ℝ, Euclidean spaces ℝⁿ, and the space of continuous functions on a closed interval are all complete; ℚ and the open interval (0,1) are not. Recognizing completeness as a structural property, rather than an accident of ℝ, is the key conceptual shift this topic prepares you for.
