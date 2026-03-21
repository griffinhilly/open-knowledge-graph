---
id: outer-measure-definition
title: 'Outer Measure: Definition and Properties'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: measure-spaces-definition
  type: hard
builds-toward:
- caratheodory-extension-theorem
tags:
- measure-theory
- outer-measure
stage: advanced
status: draft
---

# Outer Measure: Definition and Properties

## Core Idea
An outer measure μ*: 𝒫(X) → [0,∞] is monotone, countably subadditive, and satisfies μ*(∅) = 0. Outer measures are defined on all subsets, unlike measures. They serve as a tool for constructing measures via Carathéodory's theorem.

## Questions

```yaml
- question: "The Vitali set V ⊂ [0,1] is the standard example of a non-measurable set. What does the Lebesgue outer measure assign to V?"
  type: multiple-choice
  options:
    - "μ*(V) = 0, because non-measurable sets have no genuine size and are assigned zero by convention"
    - "μ*(V) is defined — outer measure assigns a value to every subset — but countable additivity fails on V, so it cannot be integrated into a consistent measure"
    - "μ*(V) is undefined, because outer measure is only defined on Lebesgue-measurable sets"
    - "μ*(V) = 1, because V is a subset of [0,1] and outer measure equals ordinary length for all bounded sets"
  answer: 1
  explanation: "Outer measure is defined on *all* subsets of ℝ — that is its whole point. So μ*(V) is a perfectly well-defined real number. The problem with V is not that outer measure fails to assign it a value, but that V fails Carathéodory's condition: it does not 'split' test sets cleanly, so countable additivity breaks down when V is involved. The Vitali construction shows that if you try to extend countable additivity to all subsets, you reach a contradiction — outer measure avoids this by replacing additivity with the weaker subadditivity."

- question: "What is the essential structural difference between a measure and an outer measure?"
  type: multiple-choice
  options:
    - "A measure is monotone; an outer measure satisfies μ*(A) ≤ μ*(B) only when A and B are disjoint"
    - "An outer measure is countably additive on disjoint sets, while a measure only achieves finite additivity"
    - "A measure is defined on a σ-algebra and is countably additive on disjoint sets; an outer measure is defined on all subsets but satisfies only countable subadditivity"
    - "An outer measure assigns ∞ to non-measurable sets; a measure assigns them 0 by convention"
  answer: 2
  explanation: "The key difference is domain and additivity property. A measure lives on a σ-algebra (a restricted collection of well-behaved sets) and is countably additive: μ(⋃ Eᵢ) = Σ μ(Eᵢ) exactly, for disjoint measurable sets. An outer measure is defined on the power set — every subset — but achieves only countable subadditivity: μ*(⋃ Aᵢ) ≤ Σ μ*(Aᵢ). This relaxation is deliberate: subadditivity can be defined universally; full additivity cannot. The Carathéodory construction then recovers a genuine measure by identifying which sets achieve exact additivity."

- question: "Since outer measure satisfies only countable subadditivity rather than countable additivity, it is a cruder and less useful tool than a measure for assigning sizes to sets."
  type: true-false
  answer: false
  explanation: "Subadditivity is a deliberate design choice, not a defect. The point of outer measure is precisely that it can be defined on *all* subsets, including non-measurable ones where genuine additivity fails. It functions as scaffolding: Lebesgue outer measure assigns every subset a candidate size, then Carathéodory's condition filters out the pathological sets where additivity breaks down, leaving a σ-algebra of measurable sets on which outer measure becomes a genuine measure. Without the outer measure construction, there would be no systematic way to identify which sets are measurable and build the Lebesgue measure."

- question: "Carathéodory's measurability condition requires that a set E split every subset A ⊆ X exactly — that is, μ*(A) = μ*(A ∩ E) + μ*(A ∩ Eᶜ) for *all* A, not just open or interval test sets."
  type: true-false
  answer: true
  explanation: "This universality is crucial and easy to underestimate. Carathéodory's condition is deliberately stringent: E must split *every* subset of X exactly, not just the 'nice' sets like open intervals. A set that splits open intervals exactly but fails for some pathological A would still cause overcounting and inconsistencies. The strength of requiring all A ⊆ X is what guarantees that the μ*-measurable sets form a σ-algebra and that μ* restricted to them is genuinely countably additive. Weakening the condition to only intervals or open sets would not achieve this."

- question: "Why is countable subadditivity a deliberate feature of outer measures rather than a limitation, and how does Carathéodory's condition recover the exactness that subadditivity gives up?"
  type: short-answer
  answer: "Subadditivity allows outer measure to be defined on every subset of X, including those where exact additivity is impossible (like non-measurable sets). This universality is the whole point — outer measure provides a consistent upper bound for size across all sets, without requiring those sets to be well-behaved. Exactness would require that overlapping covers never overcount, which fails for pathological sets. Carathéodory's condition then recovers exactness for the sets that deserve it: E is μ*-measurable if and only if it genuinely splits every test set without overcounting. For these sets, the subadditive inequality becomes an equality, and the restriction of μ* to the σ-algebra of measurable sets is a full countably additive measure. Subadditivity is the tool; Carathéodory's condition is the filter."
```

## Explainer

From your work on measure spaces, you know that a measure μ assigns sizes to sets in a σ-algebra in a countably additive way: μ(⋃ Eᵢ) = Σ μ(Eᵢ) for disjoint measurable sets. But this raises a bootstrapping problem: which sets should count as measurable in the first place? If you try to make every subset measurable and assign it a consistent, countably additive size, you run into paradoxes — the Vitali construction shows no such assignment can exist on all subsets of the real line. An **outer measure** is the technical device that navigates this problem by working with all subsets first, then identifying the well-behaved ones.

An outer measure μ*: 𝒫(X) → [0,∞] is defined on *all* subsets of X — not just the measurable ones. It satisfies three properties: μ*(∅) = 0, **monotonicity** (A ⊆ B implies μ*(A) ≤ μ*(B)), and **countable subadditivity** (μ*(⋃ Aᵢ) ≤ Σ μ*(Aᵢ)). The key contrast with a measure is in the last property: subadditivity is an inequality, not an equality. An outer measure may "overcount" when sets overlap, because it asks only for a consistent upper bound, not exact accounting.

The canonical example is the **Lebesgue outer measure** on ℝ: define μ*(A) = inf{Σ |Iₙ|: A ⊆ ⋃ Iₙ} where the infimum is over all countable covers of A by open intervals. This assigns a candidate "length" to every subset of ℝ, no matter how bizarre. Monotonicity holds because more sets can cover a smaller set; subadditivity holds because you can combine covers. But countable additivity fails on non-measurable sets — overlapping covers cannot be separated.

This is precisely the gap that **Carathéodory's theorem** closes. A set E is called **μ*-measurable** if it "splits" every test set A cleanly: μ*(A) = μ*(A ∩ E) + μ*(A ∩ Eᶜ). This condition says E does not cause overcounting — the outer measure of A is exactly the sum of the parts on each side of E. Carathéodory showed that the collection of all μ*-measurable sets forms a σ-algebra, and μ* restricted to this σ-algebra is a genuine measure. The outer measure is scaffolding: it builds candidate sizes for all sets, then the measurability condition filters out the pathological ones, leaving a clean measure space.
