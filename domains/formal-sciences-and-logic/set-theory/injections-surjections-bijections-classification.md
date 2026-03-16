---
id: injections-surjections-bijections-classification
title: Injections, Surjections, and Bijections
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: functions-and-mappings-formal
  type: hard
builds-toward:
- cardinality-and-equinumerosity
tags:
- injective
- surjective
- bijective
- one-to-one
- onto
stage: formal-systems
status: draft
---

# Injections, Surjections, and Bijections

## Core Idea
An injection preserves distinctness: f(a) = f(b) implies a = b. A surjection covers the codomain: every b ∈ B equals f(a) for some a. A bijection is both injective and surjective, establishing a perfect one-to-one correspondence. Bijections are invertible and preserve cardinality across sets.

## How It's Best Learned
Use definitions directly to prove properties. For example, f(x) = 2x on ℝ is bijective; f(x) = x² on ℝ is neither injective nor surjective, but becomes bijective when restricted to [0,∞) → [0,∞). Construct counterexamples to distinguish the concepts.

## Common Misconceptions
- Confusing 'onto' (surjective) with 'one-to-one' (injective). - Thinking a function must be defined by a formula; what matters is the assignment rule. - Assuming bijections exist only between finite sets (false; bijections exist between infinite sets of equal cardinality).

## Explainer

You already know that a **function** assigns to each element of a domain exactly one element of a codomain. The three classifications — injection, surjection, bijection — are about two different ways a function can "behave well" with respect to that assignment. Think of a function as an arrow diagram: each element on the left points to exactly one element on the right. The question is what patterns those arrows can form.

An **injection** (or one-to-one function) means no two elements on the left share the same target: every arrow lands in a distinct spot. Formally, f(a) = f(b) implies a = b. The contrapositive is equally useful: if a ≠ b, then f(a) ≠ f(b). A good mental image is that injections "spread out" — the domain can fit inside the codomain without collisions. The function f(x) = 2x from ℤ to ℤ is injective: different integers get sent to different even integers. The function f(x) = x² on ℝ is not injective because 3 and −3 both map to 9.

A **surjection** (or onto function) means every element on the right is hit by at least one arrow — nothing in the codomain is left uncovered. Formally, for every b in the codomain, there exists some a in the domain with f(a) = b. The function f(x) = x³ from ℝ to ℝ is surjective because every real number has a real cube root. But f(x) = x² from ℝ to ℝ is not surjective because negative numbers have no preimage. Notice that injectivity and surjectivity are independent: a function can have either, both, or neither. The codomain matters — f(x) = x² restricted to [0,∞) → [0,∞) becomes surjective.

A **bijection** achieves both simultaneously: it is a perfect one-to-one correspondence between domain and codomain. Every element on the left pairs with exactly one element on the right, and vice versa. Bijections are the "same size" certificates for sets — if you can exhibit a bijection between A and B, you have proven they have the same cardinality. This is profound: the bijection f(n) = 2n from ℕ to the even natural numbers proves the evens and the naturals are the same size, even though the evens seem "smaller." Bijections are also precisely the invertible functions: if f is a bijection, there is a unique function f⁻¹ that undoes it. This connection between bijections and invertibility will be central when you study cardinality, permutations, and group theory.
