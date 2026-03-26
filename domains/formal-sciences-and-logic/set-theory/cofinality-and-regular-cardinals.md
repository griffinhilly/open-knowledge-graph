---
id: cofinality-and-regular-cardinals
title: Cofinality and Regular Cardinals
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: transfinite-induction
  type: soft
- id: transfinite-recursion
  type: soft
- id: cardinality-and-countability
  type: soft
- id: cantor-theorem
  type: soft
builds-toward:
- independence-results-set-theory
tags:
- cofinality
- regular cardinals
- singular cardinals
- König's theorem
stage: formal-systems
status: validated
---
# Cofinality and Regular Cardinals

## Core Idea
The cofinality of an ordinal α, written cf(α), is the smallest ordinal β such that α is the supremum of a β-indexed sequence of ordinals less than α. A cardinal κ is regular if cf(κ) = κ (it cannot be written as a union of fewer than κ sets each of size less than κ); otherwise it is singular. Every successor cardinal ℵ_{α+1} is regular; limit cardinals like ℵ_ω may be singular (cf(ℵ_ω) = ω). Königʼs theorem states that cf(2^κ) > κ for all cardinals κ, placing a fundamental constraint on the continuum function: for example, 2^ℵ₀ cannot equal ℵ_ω.

## How It's Best Learned
Compute cofinalities directly: cf(ω) = ω (regular), cf(ω₁) = ω₁ (regular), cf(ℵ_ω) = ω (singular). Prove that every successor cardinal is regular. Apply König's theorem to rule out specific values for 2^ℵ₀: for instance, 2^ℵ₀ ≠ ℵ_ω because cf(ℵ_ω) = ω ≤ ℵ₀.

## Common Misconceptions
- 'Singular' cardinal is a precise technical term, not a judgment about pathological behavior — singular cardinals are perfectly well-defined and important.
- ℵ_ω is the ω-th aleph (the supremum of ℵ₀, ℵ₁, ℵ₂, ...), not ω steps beyond ℵ₀ in some other sense.

## Questions

```yaml
- question: "What is the cofinality of ℵ_ω?"
  type: multiple-choice
  options:
    - "cf(ℵ_ω) = ℵ_ω, because ℵ_ω is a well-defined limit cardinal and therefore regular"
    - "cf(ℵ_ω) = ω, because ℵ_ω = sup{ℵ₀, ℵ₁, ℵ₂, ...} and this sequence has length ω"
    - "cf(ℵ_ω) = ℵ₁, because ℵ_ω is an uncountable cardinal"
    - "cf(ℵ_ω) = ℵ_ω − 1, by definition of limit ordinals"
  answer: 1
  explanation: "ℵ_ω is the supremum of the sequence ℵ₀, ℵ₁, ℵ₂, ... — a sequence of length ω. No finite subsequence (or shorter sequence) has supremum ℵ_ω, so the minimum cofinal sequence length is ω, giving cf(ℵ_ω) = ω. Since ω < ℵ_ω, this means ℵ_ω is singular — it can be 'approached from below' by a mere countable sequence, despite being uncountable itself. This is the key contrast with ℵ₁, which is a successor cardinal: no countable sequence of countable ordinals can have supremum ℵ₁."

- question: "A set theorist proposes that the continuum 2^ℵ₀ might equal ℵ_ω. König's theorem rules this out. The correct argument is:"
  type: multiple-choice
  options:
    - "ℵ_ω is a singular cardinal, and the continuum must be a regular cardinal"
    - "cf(ℵ_ω) = ω = ℵ₀, but König's theorem requires cf(2^ℵ₀) > ℵ₀, which is a contradiction"
    - "ℵ_ω is too small to be the continuum — by Cantor's theorem, 2^ℵ₀ > ℵ_ω"
    - "König's theorem states that 2^ℵ₀ > ℵ_ω, which directly excludes this value"
  answer: 1
  explanation: "König's theorem states cf(2^κ) > κ for all infinite κ. Taking κ = ℵ₀: cf(2^ℵ₀) > ℵ₀. If 2^ℵ₀ = ℵ_ω, then cf(2^ℵ₀) = cf(ℵ_ω) = ω = ℵ₀. But cf(2^ℵ₀) > ℵ₀ requires cf(2^ℵ₀) ≥ ℵ₁ > ω. Contradiction. This argument holds regardless of additional axioms — it is an unconditional constraint from König's theorem alone, not contingent on the Continuum Hypothesis or forcing."

- question: "Nearly every infinite cardinal is regular, since regularity is a property shared by most alephs."
  type: true-false
  answer: false
  explanation: "Regularity fails for many limit cardinals. A cardinal κ is regular if cf(κ) = κ — it cannot be approached by a shorter sequence. Every successor cardinal (ℵ₁, ℵ₂, etc.) is regular. But limit cardinals like ℵ_ω, ℵ_{ω₁}, and many others are singular: cf(ℵ_ω) = ω < ℵ_ω. The regular/singular distinction is one of the most important in cardinal arithmetic, and singular cardinals are not pathological edge cases — they are the norm among uncountable limit cardinals."

- question: "König's theorem places an unconditional constraint on the continuum: regardless of what additional set-theoretic axioms are assumed, 2^ℵ₀ cannot equal ℵ_ω."
  type: true-false
  answer: true
  explanation: "König's theorem (cf(2^κ) > κ) is provable in ZFC without additional axioms. Its conclusion that 2^ℵ₀ ≠ ℵ_ω does not depend on the Continuum Hypothesis, forcing, or large cardinal axioms — it holds in every model of ZFC. This makes it one of the rare unconditional constraints on the continuum function, ruling out specific values of 2^ℵ₀ (any ℵ_α with cf(ℵ_α) ≤ ℵ₀) without needing to settle the question of what 2^ℵ₀ actually equals."

- question: "Explain the concept of cofinality by contrasting cf(ω) = ω with cf(ℵ_ω) = ω. What does it mean that these two very different cardinals have the same cofinality?"
  type: short-answer
  answer: "Cofinality of a limit ordinal is the length of the shortest cofinal sequence — one whose supremum equals the ordinal. For ω, the sequence 0, 1, 2, ... is cofinal with length ω, and no finite sequence suffices, so cf(ω) = ω. For ℵ_ω, the sequence ℵ₀, ℵ₁, ℵ₂, ... is cofinal with length ω, and again no shorter sequence suffices. Having the same cofinality ω means both can be 'snuck up on' by a countable sequence. For ω, this is expected — it is a countable ordinal. For ℵ_ω, this is remarkable: despite being a vastly larger (uncountable) cardinal, it is just as 'approachable from below' as ω, which is exactly what makes it singular."
  explanation: "The cofinality tells you how 'inaccessible' a limit cardinal is from below. Regular cardinals (like ℵ₁) require sequences of their own length to approach them — you can't sneak up on ℵ₁ with countably many steps. Singular cardinals like ℵ_ω can be approached much more efficiently than their size suggests. This distinction has deep consequences in combinatorics, cardinal arithmetic, and the independence results of set theory."
```

## Explainer

From your study of infinite cardinals, you know that the aleph sequence ℵ₀, ℵ₁, ℵ₂, ... extends through all ordinals: ℵ_α for every ordinal α. Successor cardinals like ℵ₁ = ℵ_{0+1} are defined as the next cardinal above the previous one. Limit cardinals like ℵ_ω are defined as suprema — ℵ_ω = sup{ℵ₀, ℵ₁, ℵ₂, ...}. **Cofinality** asks a finer question about such limit cardinals: how "approachable" is a cardinal from below?

The **cofinality** cf(κ) of a limit ordinal κ is the smallest cardinality of a cofinal subset — a set whose supremum is κ. Equivalently, it is the length of the shortest sequence that converges to κ. For ℵ_ω, the sequence ℵ₀, ℵ₁, ℵ₂, ... is cofinal and has length ω, and no shorter sequence suffices (ℵ_ω is not the supremum of any finite set). So cf(ℵ_ω) = ω. By contrast, cf(ℵ₁) = ℵ₁ itself — you cannot approach ℵ₁ from below via a countable sequence, because the supremum of countably many countable ordinals is countable, never ℵ₁.

A cardinal κ is **regular** if cf(κ) = κ — it cannot be written as the supremum of fewer than κ sets each smaller than κ. A cardinal is **singular** if cf(κ) < κ. Every successor cardinal is regular: ℵ_{α+1} cannot be the supremum of an ℵ_α-indexed sequence of cardinals each less than ℵ_{α+1}, because such a sequence would contain at most ℵ_α many cardinals each of size ≤ ℵ_α, and their union would have size ≤ ℵ_α · ℵ_α = ℵ_α < ℵ_{α+1}. Limit cardinals like ℵ_ω, ℵ_{ω₁}, etc., can be singular — ℵ_ω is the supremum of ω many smaller cardinals, so cf(ℵ_ω) = ω < ℵ_ω.

**König's theorem** states that cf(2^κ) > κ for every infinite cardinal κ. This is proved by a diagonal argument: a union of κ many sets each of size < 2^κ has size < 2^κ (by the cardinal arithmetic of cofinalities), so 2^κ cannot be the supremum of a κ-indexed sequence of smaller cardinals, meaning cf(2^κ) > κ. The striking application: 2^ℵ₀ cannot equal ℵ_ω, because cf(ℵ_ω) = ω = ℵ₀, which would require cf(2^ℵ₀) = ω ≤ ℵ₀ — contradicting König's theorem which requires cf(2^ℵ₀) > ℵ₀. Similarly, the continuum 2^ℵ₀ cannot be any ℵ_α with cf(ℵ_α) ≤ ℵ₀. This is one of the few unconditional constraints on the continuum function that holds regardless of additional set-theoretic axioms — no consistency proof or forcing argument can circumvent it.
