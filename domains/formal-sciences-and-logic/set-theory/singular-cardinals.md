---
id: singular-cardinals
title: Singular Cardinals
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cofinality-and-regular-cardinals
  type: hard
- id: cardinal-arithmetic
  type: hard
builds-toward:
- large-cardinals-intro
tags:
- singular cardinals
- regular cardinals
- cofinality
- König's theorem
- cardinal arithmetic
stage: formal-systems
status: draft
---

# Singular Cardinals

## Core Idea
An infinite cardinal κ is singular if it can be expressed as a supremum of fewer than κ cardinals each smaller than κ — equivalently, if cf(κ) < κ, where cf denotes cofinality. For example, ℵ_ω = sup{ℵ_n : n < ω} is singular because it is the supremum of countably many smaller cardinals, and ω < ℵ_ω. König's theorem places a fundamental constraint on cardinal arithmetic at singular cardinals: cf(2^κ) > κ for any cardinal κ, which implies, for instance, that 2^{ℵ₀} ≠ ℵ_ω. Singular cardinal combinatorics is one of the deepest areas of modern set theory, with Shelah's PCF theory revealing surprising constraints on the behavior of cardinal exponentiation at singular cardinals.

## How It's Best Learned
Verify that ℵ₁, ℵ₂, and ℵ_{ω₁} are regular (their cofinality equals themselves), then show ℵ_ω is singular by exhibiting a cofinal sequence of length ω. Prove König's theorem: given κ_i < λ_i for all i ∈ I, then Σκ_i < Πλ_i. Apply it to show cf(2^κ) > κ. Work through the consequence that certain values for the continuum are ruled out (e.g., 2^{ℵ₀} cannot be ℵ_ω) even without additional axioms.

## Common Misconceptions
- Singular cardinals are not rare or exotic — ℵ_ω, ℵ_{ω₁}, and ℵ_{ω+ω} are all singular. Any limit cardinal whose index is a limit ordinal of smaller cofinality is singular.
- The behavior of cardinal exponentiation at singular cardinals is not fully determined by ZFC, but it is far more constrained than at regular cardinals, thanks to PCF theory.

## Explainer

The cardinal hierarchy you know — ℵ₀, ℵ₁, ℵ₂, ... — does not end at the finite indexing. After all the ℵ_n comes ℵ_ω, the first cardinal with a limit ordinal as its subscript. This is the canonical **singular cardinal**, and understanding why requires your prerequisite concept of **cofinality**. Recall that cf(κ) is the least cardinality of a cofinal subset of κ — the smallest number of "steps" needed to reach κ from below. A cardinal is **regular** when cf(κ) = κ (you genuinely need κ-many steps), and **singular** when cf(κ) < κ (you can approach κ with fewer). ℵ_ω is singular because the sequence ℵ₀, ℵ₁, ℵ₂, ... is cofinal in ℵ_ω and has length ω = ℵ₀ < ℵ_ω. By contrast, ℵ₁ is regular: you cannot reach it from below with countably many countable cardinals, because the union of countably many countable sets is still countable.

The significance of this distinction crystallizes in **König's theorem**, one of the most useful tools in cardinal arithmetic. It states: for any indexed family where κᵢ < λᵢ for all i, the strict inequality Σᵢκᵢ < Πᵢλᵢ holds. The cofinality constraint follows as a special case: cf(2^κ) > κ for any κ. Apply this to the continuum. Suppose 2^{ℵ₀} = ℵ_ω. Then cf(ℵ_ω) = ω = ℵ₀, but König forces cf(2^{ℵ₀}) > ℵ₀. Since cf(ℵ_ω) = ω, the equation 2^{ℵ₀} = ℵ_ω would make cf(2^{ℵ₀}) = ω ≤ ℵ₀ — a direct violation. So without any additional axioms beyond ZFC, 2^{ℵ₀} ≠ ℵ_ω. More generally, 2^{ℵ₀} cannot equal any cardinal of cofinality ≤ ℵ₀. This rules out ℵ_ω, ℵ_{ω+ω}, and many others as candidates for the continuum — a constraint derived purely from the structure of cofinality and König's inequality.

Singular cardinals are not exotic edge cases — they are far more common than regular ones. Among uncountable cardinals in ZFC, all **successor cardinals** (ℵ₁, ℵ₂, ℵ₃, ...) are regular, but **limit cardinals** whose index has smaller cofinality — ℵ_ω, ℵ_{ω+ω}, ℵ_{ω₁}, ℵ_{ω_ω}, ... — are singular. The singular cardinals vastly outnumber the regular ones by density in the hierarchy. Their arithmetic, however, is far more constrained than it might appear. Shelah's **PCF (possible cofinalities) theory** established that ZFC alone implies 2^{ℵ_ω} < ℵ_{ω₄} whenever ℵ_ω is a strong limit cardinal — a concrete upper bound on a specific cardinal power, proved in ZFC without large cardinals or forcing. This was a major surprise: before PCF theory, it was widely expected that singular cardinal arithmetic was largely undetermined by ZFC.

What makes singular cardinals a frontier topic is the interplay between independence results and ZFC constraints. Large cardinal axioms — which you will study next — interact intimately with singular cardinals. The consistency of certain failure patterns for the **singular cardinal hypothesis** (the claim that 2^κ = κ⁺ for every singular strong limit κ) requires large cardinals of enormous strength, and conversely, the existence of certain large cardinals forces the GCH to fail below them. Forcing arguments can push the continuum to many values, but König's theorem acts as a hard boundary that no forcing can cross. The result is a rich structural theory in which cofinality becomes the organizing principle: singular cardinals are precisely the cardinals that can be "approached from below," and that approachability encodes surprising information about what their exponentials can be.
