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
stage: formal-systems
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

## Explainer

An **ultrafilter** on a set X is a maximal filter — a collection of "large" subsets of X closed under supersets and finite intersections, where for every subset either it or its complement belongs to the ultrafilter. From your study of ultrafilters, you know that a **nonprincipal ultrafilter** on ℕ contains no finite sets and captures a genuine notion of "almost all" that escapes any individual element. The central question motivating measurable cardinals is: can this idea be scaled up dramatically — can we put a nonprincipal ultrafilter on an uncountable cardinal κ that is closed under *κ-many* intersections simultaneously?

The obstacle is **κ-completeness**. An ultrafilter 𝒰 is κ-complete if it is closed under intersections of fewer than κ many of its members. Every ultrafilter is finitely complete by definition. But no nonprincipal ultrafilter on ω is ω₁-complete: the singletons {0}, {1}, {2}, ... partition ℕ into countably many pieces, and a countably complete nonprincipal ultrafilter would have to contain none of them — contradicting maximality. This argument generalizes: no countable or successors-of-countable cardinal can be measurable. The same logic kills uncountable cardinals built from below in any standard way, which is why measurable cardinals must be inaccessible and, in fact, lie far beyond all cardinals constructible within ZFC.

A **measurable cardinal** κ is defined precisely as an uncountable cardinal that carries a κ-complete nonprincipal ultrafilter on κ. Equivalently, there exists a two-valued measure on all subsets of κ — assigning 0 or 1 to each — that is κ-additive and assigns 0 to all singletons. Think of it as a {0,1}-valued probability measure that is simultaneously nonatomic (no individual point has positive measure) and closed under κ-many intersections. Such a cardinal must be regular (not reachable by any smaller cardinal via cofinality) and inaccessible (not reachable by power set or union operations from below), yet much larger than a mere inaccessible cardinal.

The deepest consequence is the **ultrapower construction**. Given measurable κ with ultrafilter 𝒰, one forms the ultrapower Ult(V, 𝒰) of the entire set-theoretic universe V, obtaining a transitive inner model M and a nontrivial elementary embedding j: V → M with **critical point** κ — meaning j(α) = α for all α < κ but j(κ) > κ. This embedding witnesses that κ cannot be "assembled from below": it is genuinely unreachable from the smaller universe. The existence of measurable cardinals is independent of ZFC (assuming ZFC is consistent, neither "a measurable cardinal exists" nor its negation is provable), but working at this level of the large cardinal hierarchy unlocks deep results about definable sets, determinacy of infinite games, and the structure of inner models — connections that would remain invisible within ZFC alone.
