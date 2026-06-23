---
id: beth-numbers
title: Beth Numbers
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: axiom-of-power-set
  type: hard
- id: aleph-and-beth-hierarchy-introduction
  type: soft
- id: aleph-numbers
  type: soft
builds-toward:
- continuum-hypothesis
tags:
- beth
- beth numbers
- power set
- GCH
- cardinal exponentiation
stage: formal-systems
status: validated
---

# Beth Numbers

## Core Idea
The beth numbers ℶ₀, ℶ₁, ℶ₂, ... measure cardinality by iterated power set operations rather than by ordinal indexing. ℶ₀ = ℵ₀ (the cardinality of ℕ), and ℶ_{α+1} = 2^{ℶ_α} (the cardinality of the power set of a set of size ℶ_α). At limit ordinals, ℶ_λ = sup{ℶ_β : β < λ}. By Cantor's theorem, ℶ_{α+1} > ℶ_α, so the beth sequence is strictly increasing. The generalized continuum hypothesis (GCH) is equivalent to the statement that ℶ_α = ℵ_α for all ordinals α — that is, each power set operation produces exactly the next aleph. Without GCH, the beth and aleph sequences can diverge: we always have ℶ_α ≥ ℵ_α, but the gap can be arbitrarily large.

## How It's Best Learned
Compute the first few beth numbers: ℶ₀ = ℵ₀, ℶ₁ = 2^{ℵ₀} = |ℝ| (the continuum), ℶ₂ = 2^{2^{ℵ₀}} = |P(ℝ)|. Compare with the aleph sequence: ℵ₀ = ℶ₀ always, but ℵ₁ = ℶ₁ is exactly the continuum hypothesis. State GCH as 'the aleph and beth sequences are identical' and verify that this is equivalent to saying 2^{ℵ_α} = ℵ_{α+1} for all α.

## Common Misconceptions
- Beth numbers are not an alternative to aleph numbers — they measure a different thing. Alephs enumerate cardinals by ordinal rank; beths enumerate cardinals by power-set iteration.
- ℶ₁ is always equal to 2^{ℵ₀} (by definition), but whether ℶ₁ = ℵ₁ is independent of ZFC.

## Questions

```yaml
- question: "ℶ₁ is defined as 2^{ℵ₀}. What famous open mathematical question is precisely equivalent to asking whether ℶ₁ = ℵ₁?"
  type: multiple-choice
  options:
    - "Cantor's theorem: is every infinite set strictly smaller than its power set?"
    - "The axiom of choice: does every set have a well-ordering?"
    - "The continuum hypothesis: is there no cardinal strictly between ℵ₀ and 2^{ℵ₀}?"
    - "The axiom of regularity: do infinite sets ever contain themselves?"
  answer: 2
  explanation: "ℶ₁ = 2^{ℵ₀} by definition. ℵ₁ is the first uncountable cardinal — the smallest cardinal strictly larger than ℵ₀. Asking ℶ₁ = ℵ₁ is precisely asking whether 2^{ℵ₀} = ℵ₁, i.e., whether no uncountable cardinal exists below the power set of ℕ. This is the continuum hypothesis, proven independent of ZFC by Gödel and Cohen. Cantor's theorem (option A) is already proved — it shows ℶ₁ > ℵ₀, but says nothing about how much larger ℶ₁ is."

- question: "A set theorist asks: 'What is the cardinality of P(ℝ) — the power set of the real numbers?' The correct answer in beth notation is:"
  type: multiple-choice
  options:
    - "ℶ₁, because P(ℝ) is the power set of an uncountable set"
    - "ℶ₂, because |ℝ| = ℶ₁ and P(ℝ) = 2^{ℶ₁} = ℶ₂ by definition"
    - "ℵ₂, by the generalized continuum hypothesis"
    - "2^{ℵ₁}, since |ℝ| = ℵ₁ by the continuum hypothesis"
  answer: 1
  explanation: "|ℝ| = ℶ₁ = 2^{ℵ₀} by definition. Then |P(ℝ)| = 2^{|ℝ|} = 2^{ℶ₁} = ℶ₂. Beth notation is natural here precisely because ℶ₂ is defined as one power-set application above ℶ₁. Option C would only be correct if GCH holds (ℶ₁ = ℵ₁, so ℶ₂ = ℵ₂). Option D assumes CH (|ℝ| = ℵ₁), which is independent of ZFC. The clean beth answer — ℶ₂ — holds regardless of GCH, making it more robust."

- question: "For any ordinal α, the beth number ℶ_α is greater than or equal to the aleph number ℵ_α."
  type: true-false
  answer: true
  explanation: "This inequality holds in ZFC without assuming GCH. The proof is by transfinite induction: ℶ₀ = ℵ₀ (equality at 0). For successor ordinals, ℶ_{α+1} = 2^{ℶ_α} ≥ 2^{ℵ_α} ≥ ℵ_{α+1} (using the inductive hypothesis and König's theorem). At limit ordinals, the sup preserves the inequality. GCH strengthens this to equality everywhere; without GCH, the beths can strictly exceed the corresponding alephs by an arbitrary amount."

- question: "The beth and aleph sequences measure the same thing — the beth sequence is simply an alternative notation for the same aleph numbers."
  type: true-false
  answer: false
  explanation: "They measure fundamentally different things. The aleph sequence enumerates infinite cardinals by ordinal rank: ℵ₁ is the first uncountable cardinal, ℵ₂ is the next, defined by position in the ordering of all cardinals. The beth sequence enumerates cardinals by power-set iteration: ℶ₁ is |P(ℕ)|, ℶ₂ is |P(P(ℕ))|, regardless of their aleph-rank. They start equal (ℶ₀ = ℵ₀) but may diverge at all higher indices. They are equal for all α if and only if GCH holds — which is independent of ZFC."

- question: "What is the key difference between how aleph numbers and beth numbers measure the sizes of infinite sets?"
  type: short-answer
  answer: "Aleph numbers measure infinite cardinalities by ordinal rank — ℵ₁ is simply the first uncountable cardinal, ℵ₂ the next, defined by their position in the well-ordering of all infinite cardinals. Beth numbers measure cardinalities by power-set iteration — ℶ₁ = 2^{ℵ₀} is the cardinality of P(ℕ), ℶ₂ = 2^{ℶ₁} is the cardinality of P(P(ℕ)), each step applying one more power set. The sequences coincide at ℶ₀ = ℵ₀ but whether they remain equal at higher indices is exactly what GCH asserts — and GCH is independent of ZFC."
  explanation: "The practical value of the distinction: the beth hierarchy is the natural yardstick for cardinalities arising from actual constructions (power sets, function spaces), while the aleph hierarchy is the complete enumeration of all infinite cardinalities. You can state |ℝ| = ℶ₁ and |P(ℝ)| = ℶ₂ with certainty. Whether these equal ℵ₁ and ℵ₂ respectively depends on an independent axiom. Beth notation lets you reason about set sizes without committing to the open question of their rank among all cardinals."
```

## Explainer

You know that infinite cardinals form a strict hierarchy — Cantor's theorem guarantees that the power set P(A) always has strictly larger cardinality than A, so there is no largest infinite cardinal. You also know the axiom of power set guarantees P(A) exists for any set. The **beth numbers** make this tower of iterated power-set operations precise: each ℶ_α names the cardinality you reach after α applications of the power set to ℵ₀.

Define the sequence: **ℶ₀ = ℵ₀** (the cardinality of ℕ). **ℶ₁ = 2^{ℵ₀}** (the cardinality of P(ℕ)), which equals |ℝ| — the cardinality of the continuum. **ℶ₂ = 2^{ℶ₁} = 2^{2^{ℵ₀}}** (the cardinality of P(ℝ) = the cardinality of all functions ℝ → {0,1}). In general, ℶ_{α+1} = 2^{ℶ_α}. At limit ordinals λ, ℶ_λ = sup{ℶ_β : β < λ}. Each step applies one power set; Cantor's theorem guarantees ℶ_{α+1} > ℶ_α strictly at every successor step.

How do beth numbers relate to the aleph numbers? The aleph sequence ℵ₀, ℵ₁, ℵ₂, ... enumerates all infinite cardinals *by ordinal rank* — ℵ₁ is the first uncountable cardinal, ℵ₂ is the next, and so on. The beth sequence enumerates cardinals by *power-set iteration*. We always have ℶ_α ≥ ℵ_α — beth numbers grow at least as fast as alephs — but the two sequences can diverge. The statement **ℶ₁ = ℵ₁** is precisely the **continuum hypothesis (CH)**: the power set of ℕ has the smallest possible uncountable cardinality. The statement **ℶ_α = ℵ_α for all ordinals α** is the **generalized continuum hypothesis (GCH)**, which says the aleph and beth sequences are identical — every power set operation produces exactly the next aleph. Both CH and GCH are independent of ZFC: they can be neither proved nor disproved from the axioms.

The practical value of beth numbers is as a natural measuring system for cardinalities that arise from power sets. When you encounter |ℝ| = ℶ₁, |P(ℝ)| = ℶ₂, or the cardinality of all functions from ℝ to ℝ (also ℶ₂, since |ℝ^ℝ| = (ℶ₁)^{ℶ₁} = 2^{ℶ₁} = ℶ₂), you are reading beth numbers directly. The beth hierarchy is the natural yardstick for the geometry of infinity produced by power sets, independent of the open question of how those sizes compare to the official aleph ranking.
