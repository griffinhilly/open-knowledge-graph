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
- cardinality-and-countability-methods-of-proof
tags:
- functions
- injectivity
- surjectivity
- bijectivity
stage: formal-systems
status: validated
---

# Injective, Surjective, and Bijective Functions

## Core Idea
A function is injective (one-to-one) if different inputs map to different outputs. It is surjective (onto) if every element of the codomain is the range. A bijection is both injective and surjective, establishing a one-to-one correspondence between domain and codomain. Bijections are fundamental for comparing sizes of infinite sets.

## Questions

```yaml
- question: "Consider f: ℝ → ℝ defined by f(x) = x². Is this function surjective?"
  type: multiple-choice
  options:
    - "Yes — every positive real number has a square root, so the range includes almost everything"
    - "No — negative numbers are never outputs of x², so f does not cover the full codomain ℝ"
    - "Yes — f is defined for all real inputs, so it must hit all real outputs"
    - "It depends — surjectivity requires checking injectivity first"
  answer: 1
  explanation: "Surjectivity requires that every element of the codomain be reached. The codomain is ℝ (all reals), but x² ≥ 0 for all real x — negative numbers are never outputs. So f: ℝ → ℝ with f(x) = x² is NOT surjective. Note the contrast: if we restrict the codomain to [0, ∞), declaring f: ℝ → [0, ∞), the same formula becomes surjective. Surjectivity is a relationship between the range and the declared codomain, not just a property of the formula."

- question: "Which of the following correctly describes a bijection between two sets A and B?"
  type: multiple-choice
  options:
    - "A function where every element of A maps to a unique element of B, and |A| = |B|"
    - "A function that is both injective and surjective: no two inputs share an output, and every codomain element is reached"
    - "Any function from A to B that has an algebraically computable inverse formula"
    - "A function where every element of A is in the range of B"
  answer: 1
  explanation: "A bijection is precisely the combination of injectivity (no collisions — distinct inputs map to distinct outputs) and surjectivity (no gaps — every codomain element is reached). This creates a perfect one-to-one pairing. Option A is tempting but wrong: |A| = |B| is true for finite sets with a bijection, but for infinite sets |A| = |B| is defined *by* the existence of a bijection, making it circular. Option C is wrong: some bijections (e.g., Cantor's pairing function) have inverses that aren't simple formulas."

- question: "The function n ↦ 2n from ℤ to ℤ (mapping each integer to its double) is injective but not surjective."
  type: true-false
  answer: true
  explanation: "Injective: if 2m = 2n, then m = n — distinct inputs give distinct outputs. Not surjective: the odd integers (1, 3, 5, ...) are in the codomain ℤ but are never outputs of 2n. This illustrates that injectivity and surjectivity are independent properties: a function can have one without the other."

- question: "A bijection between an infinite set and one of its proper subsets is impractical — it would violate the principle that a whole is greater than its parts."
  type: true-false
  answer: false
  explanation: "This is false — and it is the defining counterintuitive feature of infinite sets. The function n ↦ 2n bijects ℤ with the even integers, a proper subset of ℤ. Dedekind used this property as the *definition* of an infinite set: a set is infinite if and only if it can be put into bijection with a proper subset of itself. The intuition that 'whole > part' holds for finite sets but breaks down for infinite ones."

- question: "Why can a bijection exist between an infinite set and one of its proper subsets, and what does this reveal about infinite cardinality?"
  type: short-answer
  answer: "For infinite sets, bijections can exist between a set and a proper subset because the 'size' of an infinite set is not exhausted by removing a finite (or even infinite) number of elements in the right way. For example, n ↦ 2n pairs every integer with a unique even integer — no element on either side is left unpaired — establishing a bijection despite the even integers being a proper subset of the integers. This reveals that infinite cardinality is not governed by the part-whole principle. Two infinite sets have the same cardinality if and only if a bijection exists between them, and this definition allows proper subsets to be 'equally large.'"
  explanation: "This distinction — finite intuitions failing for infinite sets — is the central insight of Cantorian set theory. It also explains why bijections are the right tool for comparing sizes: for finite sets, a bijection between A and B iff |A| = |B| matches our counting intuition; for infinite sets, bijection is the only coherent notion of 'same size.' Understanding this is essential for studying countability and uncountability."
```

## Explainer

From your study of functions, you know that f: A → B assigns each element of the domain A exactly one element of the codomain B. The **range** is the set of elements that actually get hit. Now we ask two sharper questions: does the function use its domain without collisions, and does it cover the codomain without gaps?

A function is **injective** (one-to-one) if distinct inputs always produce distinct outputs: a ≠ a' implies f(a) ≠ f(a'). Equivalently, if f(a) = f(a'), then a = a' — working backward from equal outputs forces equal inputs. The function f(x) = x³ on R is injective, since different numbers cube to different values. The function f(x) = x² is not injective, since both 2 and −2 map to 4. Injectivity says the function is "collision-free" — no two domain elements get merged into one output.

A function is **surjective** (onto) if every element of the codomain is reached: for every b ∈ B, there exists a ∈ A with f(a) = b. Notice that surjectivity is about the codomain, not just the range — it says the range *equals* the codomain, leaving no element of B unhit. The function f: R → R given by f(x) = x³ is surjective (every real is a cube of something), but f: R → R given by f(x) = x² is not (negative numbers are never outputs). However, f: R → [0, ∞) with f(x) = x² is surjective — by shrinking the codomain to match the range, we can make the same formula surjective.

A **bijection** is both injective and surjective: a perfect pairing where every element on each side participates exactly once. Bijections are the mathematical notion of "same size," called **cardinality**. For finite sets this is intuitive — a bijection between {1, 2, 3} and {a, b, c} confirms they both have 3 elements. For infinite sets, bijections reveal surprising structure: the function n ↔ 2n pairs every integer with a distinct even integer, establishing a bijection between Z and the even integers. This means they have the same cardinality, even though one appears to be a proper subset of the other. This counterintuitive fact — that an infinite set can biject with a proper subset — is the defining feature of infinite sets, and it will be central when you study countability.
