---
id: injective-surjective-bijective-functions
title: Injective, Surjective, and Bijective Functions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: functions-domain-codomain-range
  type: hard
builds-toward:
- function-composition-and-inverses
- cardinality-countability-infinity
tags:
- functions
- injectivity
- surjectivity
- bijectivity
stage: formal-systems
status: draft
---

# Injective, Surjective, and Bijective Functions

## Core Idea
A function is injective (one-to-one) if different inputs map to different outputs. It is surjective (onto) if every element of the codomain is the range. A bijection is both injective and surjective, establishing a one-to-one correspondence between domain and codomain. Bijections are fundamental for comparing sizes of infinite sets.

## Explainer

From your study of functions, you know that f: A → B assigns each element of the domain A exactly one element of the codomain B. The **range** is the set of elements that actually get hit. Now we ask two sharper questions: does the function use its domain without collisions, and does it cover the codomain without gaps?

A function is **injective** (one-to-one) if distinct inputs always produce distinct outputs: a ≠ a' implies f(a) ≠ f(a'). Equivalently, if f(a) = f(a'), then a = a' — working backward from equal outputs forces equal inputs. The function f(x) = x³ on R is injective, since different numbers cube to different values. The function f(x) = x² is not injective, since both 2 and −2 map to 4. Injectivity says the function is "collision-free" — no two domain elements get merged into one output.

A function is **surjective** (onto) if every element of the codomain is reached: for every b ∈ B, there exists a ∈ A with f(a) = b. Notice that surjectivity is about the codomain, not just the range — it says the range *equals* the codomain, leaving no element of B unhit. The function f: R → R given by f(x) = x³ is surjective (every real is a cube of something), but f: R → R given by f(x) = x² is not (negative numbers are never outputs). However, f: R → [0, ∞) with f(x) = x² is surjective — by shrinking the codomain to match the range, we can make the same formula surjective.

A **bijection** is both injective and surjective: a perfect pairing where every element on each side participates exactly once. Bijections are the mathematical notion of "same size," called **cardinality**. For finite sets this is intuitive — a bijection between {1, 2, 3} and {a, b, c} confirms they both have 3 elements. For infinite sets, bijections reveal surprising structure: the function n ↔ 2n pairs every integer with a distinct even integer, establishing a bijection between Z and the even integers. This means they have the same cardinality, even though one appears to be a proper subset of the other. This counterintuitive fact — that an infinite set can biject with a proper subset — is the defining feature of infinite sets, and it will be central when you study countability.
