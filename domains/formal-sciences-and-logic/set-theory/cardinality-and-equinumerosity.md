---
id: cardinality-and-equinumerosity
title: Cardinality and Equinumerosity
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: injections-surjections-bijections-classification
  type: hard
- id: bijection-counting-principle
  type: soft
builds-toward:
- finite-sets-and-natural-numbers
- countably-infinite-sets
tags:
- cardinality
- equinumerosity
- size
- bijection
stage: formal-systems
status: validated
---

# Cardinality and Equinumerosity

## Core Idea
Two sets have the same cardinality if there exists a bijection between them. This extends the notion of set size beyond finite collections to all sets, allowing meaningful comparison of infinite sets. For any two sets A and B, exactly one of |A| < |B|, |A| = |B|, or |A| > |B| holds by the Cantor-Schröder-Bernstein theorem.

## How It's Best Learned
Construct explicit bijections: f(n) = 2n shows ℕ and the even natural numbers have equal cardinality. Use Cantor-Schröder-Bernstein: if injections f: A → B and g: B → A exist, then |A| = |B|. Verify with standard pairs: ℕ ≅ ℤ ≅ ℚ.

## Common Misconceptions
- Thinking ℕ and 2ℕ have different cardinalities because 2ℕ ⊂ ℕ (they are equinumerous). - Assuming cardinality is always a number; cardinality is an equivalence class of sets. - Confusing 'same cardinality' with 'same elements'—cardinality measures size, not identity.

## Questions

```yaml
- question: "The set of even natural numbers 2ℕ = {0, 2, 4, 6, ...} is a proper subset of ℕ = {0, 1, 2, 3, ...}. What is the relationship between their cardinalities?"
  type: multiple-choice
  options:
    - "|2ℕ| < |ℕ|, because 2ℕ is missing all the odd numbers"
    - "|2ℕ| = |ℕ|, because f(n) = 2n is a bijection from ℕ to 2ℕ"
    - "|2ℕ| = |ℕ|/2, since exactly half the natural numbers are even"
    - "|2ℕ| < |ℕ|, because a proper subset always has strictly smaller cardinality"
  answer: 1
  explanation: "Cardinality is defined by bijections, not subset relationships. f(n) = 2n maps every natural number to a unique even number (injective) and hits every even (surjective), so it is a bijection — by definition |2ℕ| = |ℕ|. The finite intuition that a proper subset must be smaller fails for infinite sets. In fact, being bijectable with a proper subset is Dedekind's definition of an infinite set."

- question: "To prove that the open interval (0,1) and all of ℝ have the same cardinality using Cantor-Schröder-Bernstein, which approach works?"
  type: multiple-choice
  options:
    - "Show both are countably infinite — all countably infinite sets have equal cardinality"
    - "Construct an injection (0,1) → ℝ via the identity, and an injection ℝ → (0,1) via (arctan(x)/π + ½), then conclude |(0,1)| = |ℝ| by CSB"
    - "Show a surjection ℝ → (0,1) and conclude the sets are equinumerous"
    - "Since (0,1) ⊂ ℝ, they cannot have the same cardinality"
  answer: 1
  explanation: "Cantor-Schröder-Bernstein (CSB) states: if injections f: A → B and g: B → A both exist, then |A| = |B|. For (0,1) and ℝ: the identity is an injection (0,1) → ℝ; the function arctan(x)/π + ½ maps ℝ injectively into (0,1) (it's strictly increasing and lands in (0,1)). Both injections exist, so CSB guarantees a bijection. Option D repeats the finite misconception that subset implies smaller cardinality — exactly what cardinality theory overturns."

- question: "The set of integers ℤ has strictly greater cardinality than ℕ, because ℤ contains all negative integers in addition to ℕ."
  type: true-false
  answer: false
  explanation: "Despite containing infinitely many more elements, ℤ and ℕ are equinumerous. An explicit bijection: f(0)=0, f(1)=−1, f(2)=1, f(3)=−2, f(4)=2, ... — interleaving the negative and positive integers. Every integer is hit exactly once. The lesson: for infinite sets, 'proper subset' does not imply 'smaller cardinality.' Both ℕ and ℤ are countably infinite, meaning they have cardinality ℵ₀ (aleph-null)."

- question: "The Cantor-Schröder-Bernstein theorem states: if there is an injection A → B and an injection B → A, then there exists a bijection between A and B."
  type: true-false
  answer: true
  explanation: "This is exactly CSB. An injection A → B establishes |A| ≤ |B|; an injection B → A establishes |B| ≤ |A|. CSB says these two inequalities together imply |A| = |B| — a bijection must exist, even though neither injection itself is the bijection. The theorem is non-trivial because constructing the bijection from two injections requires a careful set-theoretic argument. CSB makes cardinality comparison well-behaved: there are no two sets with |A| ≤ |B| and |B| ≤ |A| but |A| ≠ |B|."

- question: "Why does the existence of a bijection — rather than a counting argument — define 'same cardinality' for infinite sets?"
  type: short-answer
  answer: "For finite sets, counting works: two sets have the same cardinality iff both have the same natural number n of elements. But 'number of elements' doesn't generalize — you cannot point to a specific natural number as the 'count' of ℕ itself. Bijections generalize counting without needing a specific number: two sets are equinumerous iff their elements can be paired one-to-one with no leftovers. This works for finite sets (agreeing with ordinary counting) and extends to infinite sets, where it yields the surprising result that proper subsets can have equal cardinality to the whole."
  explanation: "Hilbert's Hotel illustrates the key point: an infinite hotel with all rooms occupied can accommodate a new guest by shifting everyone — room n → room n+1 — freeing room 1. The hotel is 'full' but not 'full' in the way a finite hotel is. Bijection-based cardinality captures this: |ℕ| = |ℕ ∪ {new guest}| because a bijection exists. This isn't a paradox — it's the defining property of infinite sets. The bijection definition is the mathematically correct way to compare sizes when counting by natural numbers breaks down."
```

## Explainer

You already understand injections, surjections, and bijections — functions with precise structural properties. Cardinality repurposes bijections as the measuring instrument for size. The definition is precise: two sets A and B are **equinumerous** (have the same **cardinality**, written |A| = |B|) if and only if there exists a bijection f: A → B. For finite sets this agrees with your intuitive notion of size: {a, b, c} and {1, 2, 3} have the same cardinality because f(a)=1, f(b)=2, f(c)=3 is a bijection. The powerful move is that this definition applies to infinite sets too, where your intuition about size breaks down.

The counterintuitive results follow immediately. Let **ℕ** = {0, 1, 2, 3, ...} and let **2ℕ** = {0, 2, 4, 6, ...} be the even natural numbers. Since 2ℕ ⊂ ℕ, it seems smaller. But the function f(n) = 2n is a bijection from ℕ to 2ℕ: every natural number maps to a unique even, and every even comes from some natural number. So |ℕ| = |2ℕ|. Similarly, f(n) = n+1 maps ℕ bijectively onto {1, 2, 3, ...}, and the function f(n) = (−1)^n · ⌊(n+1)/2⌋ maps ℕ bijectively onto ℤ. The key lesson: for infinite sets, "proper subset" does not imply "smaller cardinality." In fact, the ability to biject with a proper subset is a *definition* of being infinite (Dedekind infinite).

The **Cantor-Schröder-Bernstein theorem** is the main technical tool for proving equinumerosity without constructing an explicit bijection. It says: if there is an injection f: A → B and an injection g: B → A, then there is a bijection h: A → B and hence |A| = |B|. This is powerful because injections are often easier to construct than bijections. To show |ℝ| = |(0,1)|, you inject (0,1) into ℝ via the identity, and inject ℝ into (0,1) via the arctan function (scaled and shifted). Both injections exist, so the sets are equinumerous even though (0,1) is a bounded interval and ℝ is the whole line.

Cardinality defines a **partial order** on sets: |A| ≤ |B| if there is an injection A → B. The Cantor-Schröder-Bernstein theorem shows this is actually a total order on cardinalities: for any two sets, either |A| ≤ |B| or |B| ≤ |A| (assuming the axiom of choice). And the ordering is non-trivial for infinite sets: Cantor's diagonal argument shows |ℕ| < |ℝ| — the real numbers are *strictly* larger than the naturals, meaning no bijection between them exists. This means there are different **sizes of infinity**, and cardinality is the precise language for comparing them. You'll explore this hierarchy further when you study countable and uncountable sets.

