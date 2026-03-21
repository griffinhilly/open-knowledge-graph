---
id: measurable-cardinals-ultra-filters
title: Measurable Cardinals and Ultrafilters
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cardinal-arithmetic-infinite-sets
  type: hard
- id: ultrafilters-in-logic
  type: soft
builds-toward:
- large-cardinals-intro
- consistency-strength-large-cardinals
tags:
- measurable-cardinals
- ultrafilters
- large-cardinals
- measure
stage: advanced
status: draft
---

# Measurable Cardinals and Ultrafilters

## Core Idea
A cardinal κ is measurable if there exists a κ-complete nonprincipal ultrafilter on κ. Equivalently, there is a κ-additive {0,1}-valued measure on the power set of κ. Measurable cardinals are among the first large cardinals, lying far above ℵ₁ and beyond. Their existence is unprovable in ZFC but has deep consistency consequences.

## How It's Best Learned
Review ultrafilters on ℕ (principal filters, the 'nonstandard' points). Explain why no countable cardinal is measurable. Discuss κ-completeness and why measurable cardinals must be regular and inaccessible. Mention applications to ultraproducts and model theory.

## Common Misconceptions
- Assuming measurable cardinals exist in ZFC (they don't; adding their existence strengthens the theory).
- Confusing the ultrafilter (a collection of subsets) with a measure (a numerical function).

## Questions

```yaml
- question: "The partitioning argument shows that no nonprincipal ultrafilter on ℕ can be ω₁-complete. Why does this same argument imply that no successor cardinal (like ℵ₁ or ℵ₂) can be measurable?"
  type: multiple-choice
  options:
    - "Successor cardinals are too small to carry any nonprincipal ultrafilter at all"
    - "Any successor cardinal can be partitioned into its predecessor-many singletons, and a predecessor-complete nonprincipal ultrafilter cannot decide them consistently"
    - "Successor cardinals are not regular, so the κ-completeness condition fails trivially"
    - "The ultrapower construction requires inaccessible cardinals to be well-founded, not just successor cardinals"
  answer: 1
  explanation: "The partition argument runs as follows: κ is partitioned into κ-many singletons {α} for α < κ. A κ-complete nonprincipal ultrafilter must contain none of them (nonprincipal) yet must decide every subset (maximality). But the singletons cover κ entirely, so their complements cannot all be in the ultrafilter consistently. This applies to any cardinal reachable from below — including all successor cardinals — forcing measurable cardinals to be inaccessible. Option A is wrong because ultrafilters on ω exist; the issue is completeness. Option C is wrong: successor cardinals are regular."

- question: "In the ultrapower construction Ult(V, 𝒰), what is the significance of the critical point κ of the elementary embedding j: V → M?"
  type: multiple-choice
  options:
    - "It is the largest cardinal that is moved by j — everything above κ maps to itself"
    - "It is the smallest cardinal moved by j — j(α) = α for all α < κ, but j(κ) > κ"
    - "It is the cardinal at which V and M first disagree about which sets exist"
    - "It marks the boundary of κ-completeness: the ultrafilter is exactly κ-complete but not κ⁺-complete"
  answer: 1
  explanation: "The critical point is the *smallest* ordinal moved by j. All ordinals below κ are fixed — j(α) = α — but j(κ) > κ, witnessing that κ is genuinely 'unreachable from below.' This is the precise sense in which measurable cardinals cannot be assembled from smaller sets: any ordinal-building process internal to the universe fixes everything below κ. Option A reverses the definition. Option C describes a related but different phenomenon (agreement between V and M about sets)."

- question: "Every measurable cardinal is inaccessible."
  type: true-false
  answer: true
  explanation: "This follows from two separate arguments. First, measurability implies regularity: if κ were singular (reachable as a union of fewer-than-κ sets of size less than κ), the κ-completeness condition on the ultrafilter would be violated. Second, measurability implies strong limit (cannot be reached by power sets from below). Both properties together define inaccessibility. Measurable cardinals are not just inaccessible — they are vastly stronger — but inaccessibility is a necessary consequence."

- question: "Every inaccessible cardinal is measurable."
  type: true-false
  answer: false
  explanation: "This is a tempting but false reversal. Inaccessibility is a *necessary* condition for measurability, not a sufficient one. An inaccessible cardinal merely cannot be reached by successor operations or power sets from below. Measurability additionally requires the existence of a κ-complete nonprincipal ultrafilter on κ — a much stronger large cardinal axiom. The existence of inaccessible cardinals is already unprovable in ZFC; measurable cardinals sit far higher in the large cardinal hierarchy, with much greater consistency strength."

- question: "Why must a measurable cardinal κ be inaccessible, and why does κ-completeness play the central role in forcing this?"
  type: short-answer
  answer: "κ-completeness means the ultrafilter is closed under intersections of fewer than κ of its members. If κ were a successor cardinal λ⁺, we could partition κ into λ-many pieces of size λ; the ultrafilter's κ-completeness would require it to contain an intersection over λ-many complements of singletons — but that contradicts the nonprincipal requirement (no singleton can be in 𝒰) together with maximality. This forces κ to be a limit cardinal. The regularity argument then shows κ cannot be singular. Together, these properties give inaccessibility as a minimum threshold, below which the κ-complete ultrafilter simply cannot exist."
  explanation: "The key is that κ-completeness is a closure condition on intersections, and this closure condition clashes with the partition structure of any 'reachable' cardinal. Each time you try to construct κ from smaller pieces, those pieces generate a partition that breaks the ultrafilter. Only a cardinal truly unreachable from below can sustain the required completeness. This is why measurable cardinals belong to the large cardinal hierarchy above inaccessibles, Mahlo cardinals, and many other intermediate large cardinals."
```

## Explainer

An **ultrafilter** on a set X is a maximal filter — a collection of "large" subsets of X closed under supersets and finite intersections, where for every subset either it or its complement belongs to the ultrafilter. From your study of ultrafilters, you know that a **nonprincipal ultrafilter** on ℕ contains no finite sets and captures a genuine notion of "almost all" that escapes any individual element. The central question motivating measurable cardinals is: can this idea be scaled up dramatically — can we put a nonprincipal ultrafilter on an uncountable cardinal κ that is closed under *κ-many* intersections simultaneously?

The obstacle is **κ-completeness**. An ultrafilter 𝒰 is κ-complete if it is closed under intersections of fewer than κ many of its members. Every ultrafilter is finitely complete by definition. But no nonprincipal ultrafilter on ω is ω₁-complete: the singletons {0}, {1}, {2}, ... partition ℕ into countably many pieces, and a countably complete nonprincipal ultrafilter would have to contain none of them — contradicting maximality. This argument generalizes: no countable or successors-of-countable cardinal can be measurable. The same logic kills uncountable cardinals built from below in any standard way, which is why measurable cardinals must be inaccessible and, in fact, lie far beyond all cardinals constructible within ZFC.

A **measurable cardinal** κ is defined precisely as an uncountable cardinal that carries a κ-complete nonprincipal ultrafilter on κ. Equivalently, there exists a two-valued measure on all subsets of κ — assigning 0 or 1 to each — that is κ-additive and assigns 0 to all singletons. Think of it as a {0,1}-valued probability measure that is simultaneously nonatomic (no individual point has positive measure) and closed under κ-many intersections. Such a cardinal must be regular (not reachable by any smaller cardinal via cofinality) and inaccessible (not reachable by power set or union operations from below), yet much larger than a mere inaccessible cardinal.

The deepest consequence is the **ultrapower construction**. Given measurable κ with ultrafilter 𝒰, one forms the ultrapower Ult(V, 𝒰) of the entire set-theoretic universe V, obtaining a transitive inner model M and a nontrivial elementary embedding j: V → M with **critical point** κ — meaning j(α) = α for all α < κ but j(κ) > κ. This embedding witnesses that κ cannot be "assembled from below": it is genuinely unreachable from the smaller universe. The existence of measurable cardinals is independent of ZFC (assuming ZFC is consistent, neither "a measurable cardinal exists" nor its negation is provable), but working at this level of the large cardinal hierarchy unlocks deep results about definable sets, determinacy of infinite games, and the structure of inner models — connections that would remain invisible within ZFC alone.
