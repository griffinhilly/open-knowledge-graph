---
id: signed-measures-hahn-jordan
title: Signed Measures and Hahn-Jordan Decomposition
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: radon-nikodym-theorem
  type: hard
- id: null-sets-almost-everywhere
  type: soft
tags:
- measure-theory
stage: expert
status: validated
---
# Signed Measures and Hahn-Jordan Decomposition

## Core Idea
A signed measure ν: F → ℝ is countably additive but can take negative values. Every signed measure decomposes uniquely as ν = ν⁺ - ν⁻ (Hahn-Jordan), where ν⁺, ν⁻ are mutually singular positive measures.

## Questions

```yaml
- question: "A signed measure ν on X can be written as ν = μ₁ − μ₂ for many pairs of positive measures. Under what additional condition on μ₁ and μ₂ is this decomposition guaranteed to be unique?"
  type: multiple-choice
  options:
    - "Both μ₁ and μ₂ must be σ-finite"
    - "μ₁ and μ₂ must be mutually singular — concentrated on disjoint measurable sets"
    - "The total variation μ₁ + μ₂ must be a finite measure"
    - "μ₁(X) must equal μ₂(X)"
  answer: 1
  explanation: "Mutual singularity is the key uniqueness condition: ν⁺ concentrates on the Hahn positive set P and ν⁻ concentrates on N = Pᶜ, so they assign zero mass to each other's supporting set. Without this constraint, you could add any positive measure λ to both μ₁ and μ₂ without changing the difference, giving infinitely many decompositions. σ-finiteness and finite total variation are useful regularity conditions but do not enforce uniqueness on their own."

- question: "The Hahn decomposition partitions X into a positive set P and a negative set N. For every measurable set E ⊆ N, which statement is correct about ν(E)?"
  type: multiple-choice
  options:
    - "ν(E) can be positive or negative depending on E's internal structure"
    - "ν(E) ≤ 0 — every measurable subset of N receives nonpositive signed measure"
    - "ν(E) = 0 because N contributes no mass to ν"
    - "ν(E) is undefined until the Jordan decomposition is computed"
  answer: 1
  explanation: "By definition of the Hahn decomposition, N is a negative set: every measurable subset of N has ν-measure ≤ 0. This is what makes the Jordan decomposition work — ν⁻(E) = −ν(E ∩ N) ≥ 0 for all E. The common misconception is treating N like a null set; N carries negative mass, not zero mass."

- question: "The total variation measure |ν| = ν⁺ + ν⁻ assigns nonnegative values to all measurable sets, even though ν itself may be negative on some sets."
  type: true-false
  answer: true
  explanation: "True. Since ν⁺ and ν⁻ are both positive measures, their sum |ν| is also a positive measure — it measures the total 'magnitude' of signed mass, analogous to the absolute value of a real number. |ν|(E) = ν⁺(E) + ν⁻(E) ≥ 0 always. This is why |ν| is called the total variation: it captures total mass regardless of sign."

- question: "The Hahn decomposition of a measurable space into a positive set P and a negative set N is largely unique — there is exactly one such partition with no ambiguity."
  type: true-false
  answer: false
  explanation: "False. The Hahn decomposition is unique only up to ν-null sets. If Z is a set with ν(E) = 0 for all measurable E ⊆ Z (a ν-null set), you can move Z from P to N or vice versa without violating the conditions, producing a different partition that still satisfies all requirements. The decomposition is essentially unique — any two Hahn decompositions differ only on null sets — but not absolutely unique."

- question: "Explain why the mutual singularity of ν⁺ and ν⁻ in the Jordan decomposition is both necessary for uniqueness and structurally natural given the Hahn decomposition."
  type: short-answer
  answer: "Mutual singularity means ν⁺ is concentrated on P (the Hahn positive set) and ν⁻ is concentrated on N = Pᶜ. These are disjoint sets, so the two measures have no overlap. This is structurally natural because the positive part of ν 'lives' on the region of X where ν is positive, and the negative part lives where ν is negative. Uniqueness follows: any other decomposition ν = μ₁ − μ₂ into mutually singular positive measures would require μ₁ to concentrate on some set and μ₂ on its complement, which must coincide with P and N (up to null sets). Without mutual singularity, you could shift mass between the two parts, breaking uniqueness."
  explanation: "The Jordan decomposition is canonical precisely because it extracts the intrinsic positive and negative regions of the measure — the Hahn decomposition reveals them. Mutual singularity is the minimal condition that prevents the artificial inflation of both parts by a common positive measure, and it follows directly from the geometry of the Hahn partition."
```

## Explainer

Standard measures assign nonnegative sizes to sets. A **signed measure** relaxes this: sets can have negative measure, representing a net quantity that allows cancellation. The motivating example is a difference of two ordinary measures: if μ and ν are both positive measures, then ν - μ is a signed measure. The Hahn-Jordan decomposition theorem says this is essentially the only structure — every signed measure is the difference of two positive measures, and the decomposition is unique under the constraint of mutual singularity.

The **Hahn decomposition** partitions the underlying space X into a positive set P (where ν assigns nonneg­ative values to all subsets) and a negative set N = Pᶜ (where ν assigns nonpositive values to all subsets). Think of it as dividing X into a net-positive region and a net-negative region. This partition is essentially unique up to null sets — the decomposition reflects an intrinsic property of ν rather than an arbitrary choice.

From the Hahn decomposition, the **Jordan decomposition** follows immediately: define ν⁺(E) = ν(E ∩ P) and ν⁻(E) = −ν(E ∩ N). Both ν⁺ and ν⁻ are positive measures, they are **mutually singular** (ν⁺ concentrates on P, ν⁻ on N, which are disjoint), and ν = ν⁺ − ν⁻. The **total variation** |ν| = ν⁺ + ν⁻ is the signed-measure analogue of the absolute value — it measures total mass, positive and negative combined.

Your prerequisite, the Radon-Nikodym theorem, tells you when a measure is absolutely continuous with respect to another, producing a density function dν/dμ. Signed measures extend this naturally: the Radon-Nikodym derivative dν/dμ can itself be a real-valued function that takes negative values on some sets. The Jordan decomposition then corresponds to decomposing dν/dμ into its positive and negative parts as a function. This bridge between signed measures and signed densities is what makes the decomposition analytically useful — it reduces measure-theoretic questions to real-variable ones.
