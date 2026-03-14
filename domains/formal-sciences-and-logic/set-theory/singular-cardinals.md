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
