---
id: infinite-cardinal-numbers
title: Infinite Cardinal Numbers
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cardinality-and-countability
  type: hard
- id: von-neumann-ordinals
  type: hard
- id: well-ordering-theorem
  type: soft
- id: axiom-of-power-set
  type: soft
- id: transfinite-induction
  type: soft
- id: transfinite-recursion
  type: soft
- id: cardinal-numbers-basic-theory
  type: soft
- id: bijections-establish-equinumerosity
  type: hard
- id: countable-sets-and-countability
  type: soft
builds-toward:
- cantor-theorem
- cardinal-arithmetic
- continuum-hypothesis
- cofinality-and-regular-cardinals
tags:
- cardinals
- aleph
- infinite sets
- equinumerosity
- initial ordinals
stage: formal-systems
status: validated
---
# Infinite Cardinal Numbers

## Core Idea
A cardinal number measures the size of a set via bijection: two sets have the same cardinality if and only if there is a bijection between them. In ZFC, each infinite cardinal is represented as an initial ordinal — an ordinal not in bijection with any smaller ordinal. The infinite cardinals are indexed by ordinals via the aleph sequence: ℵ₀ (cardinality of ℕ), ℵ₁ (the next uncountable cardinal), ℵ₂, ..., ℵ_ω, .... The axiom of choice ensures every set has a cardinality comparable with all others; without choice, some sets cannot be well-ordered and thus have no aleph. The aleph hierarchy, defined by transfinite recursion on ordinals, provides a complete listing of all infinite cardinals.

## How It's Best Learned
Begin with countability and the distinction between ℵ₀ and uncountable sets. Then define initial ordinals formally: verify ω is the initial ordinal for ℵ₀, and construct ω₁ (the first uncountable ordinal) via the Hartogs number construction. Build the first few alephs and locate familiar sets (ℕ, ℚ, ℝ) within the hierarchy.

## Common Misconceptions
- ℵ₁ is the second infinite cardinal (the first uncountable one); it is NOT necessarily |ℝ| — whether |ℝ| = ℵ₁ is exactly the continuum hypothesis.
- The existence of ℵ₁ does not require exhibiting an uncountable set by construction; it follows by applying axiom of replacement to ω.

## Questions

```yaml
- question: "Which of the following correctly describes the relationship between ℵ₁ and the cardinality of the real numbers |ℝ|?"
  type: multiple-choice
  options:
    - "ℵ₁ = |ℝ| by definition, since ℝ is the first uncountable set constructed in standard mathematics"
    - "ℵ₁ < |ℝ| always, because 2^ℵ₀ is strictly larger than the first uncountable cardinal"
    - "Whether ℵ₁ = |ℝ| is independent of ZFC — it can neither be proved nor disproved from the standard axioms"
    - "ℵ₁ > |ℝ| because ω₁ contains more elements than the continuum"
  answer: 2
  explanation: "By Cantor's theorem, |ℝ| = 2^ℵ₀ > ℵ₀, so ℝ is uncountable. But ℵ₁ is defined as the *second* infinite cardinal — the first uncountable one — purely from ordinal theory, with no reference to ℝ. Whether 2^ℵ₀ = ℵ₁ (the continuum hypothesis) is a statement that Gödel showed cannot be disproved from ZFC and Cohen showed cannot be proved from ZFC. It is independent — both CH and ¬CH are consistent with ZFC."

- question: "ℵ₁ is by definition the cardinality of the real numbers ℝ."
  type: true-false
  answer: false
  explanation: "ℵ₁ is defined as the first uncountable cardinal — the unique initial ordinal ω₁, the smallest ordinal with no bijection to ω. The cardinality of ℝ is 2^ℵ₀, which is provably uncountable (by Cantor's diagonal argument) and thus at least ℵ₁. Whether |ℝ| = ℵ₁ exactly is the continuum hypothesis, which is independent of ZFC. The definition of ℵ₁ makes no reference to ℝ."

- question: "Explain the difference between a cardinal number and an ordinal number, and why every cardinal is an ordinal but not conversely."
  type: short-answer
  answer: "Ordinals measure order-type: they represent the isomorphism classes of well-ordered sets. Cardinals measure cardinality: two sets have the same cardinal if and only if there is a bijection between them. Every cardinal is an initial ordinal — an ordinal α such that no β < α has a bijection with α. But many ordinals are not initial: ω and ω+1 are different ordinals with the same cardinality ℵ₀, so ω+1 is not a cardinal. The infinite cardinals ℵ₀, ℵ₁, ℵ₂, ... form a proper subclass of the ordinals."
  explanation: "The key distinction is between order structure (which ordinals track) and mere size (which cardinals track). The ordinals ω, ω+1, ω+2, ... ω·2, ... are all countably infinite and thus have the same cardinality ℵ₀ even though they are all distinct ordinals. The cardinal ℵ₀ = ω is the first infinite initial ordinal; ℵ₁ = ω₁ is the next."
```

## Explainer

From your study of cardinality and countability, you know that two sets have the same size if and only if there is a bijection between them, and that infinite sets can have different cardinalities — Cantor's diagonal argument shows ℕ and ℝ are not in bijection. Infinite cardinal numbers are the formal system for measuring and comparing the sizes of infinite sets within ZFC.

In ZFC, each infinite cardinal is identified with a specific ordinal: an *initial ordinal*, meaning an ordinal that is not in bijection with any smaller ordinal. The smallest infinite cardinal is ℵ₀ = ω, the order-type of the natural numbers. The next infinite cardinal ℵ₁ is constructed as ω₁, the Hartogs number of ω: the set of all countable ordinals, which turns out to be the smallest uncountable ordinal. By the axiom of replacement, this set exists and has a well-defined cardinality strictly greater than ℵ₀. The process continues by transfinite recursion: ℵ_{α+1} is the Hartogs number of ℵ_α, and ℵ_λ = sup{ℵ_α : α < λ} for limit ordinals λ. This gives the aleph sequence ℵ₀, ℵ₁, ℵ₂, ..., ℵ_ω, ℵ_{ω+1}, ... indexing all infinite cardinals.

The relationship between ordinals and cardinals is important to keep straight. Ordinals measure order-type — ω and ω+1 are different ordinals because they have different well-order structures. But as sets they are in bijection (just move the last element), so they have the same cardinality ℵ₀. Cardinals are the initial ordinals: among all ordinals of a given cardinality, the smallest one. So ℵ₁ = ω₁, the smallest uncountable ordinal, is both the first uncountable cardinal and an ordinal. Every cardinal is an ordinal, but most ordinals are not cardinals.

A common and significant misconception: ℵ₁ is not defined as |ℝ|. The real numbers have cardinality 2^ℵ₀ (the size of the power set of ℕ), and Cantor's theorem guarantees 2^ℵ₀ > ℵ₀, so ℝ is uncountable. But 2^ℵ₀ could be ℵ₁, or ℵ₂, or ℵ_ω, or many other cardinals. Whether 2^ℵ₀ = ℵ₁ is exactly the continuum hypothesis (CH). Gödel showed in 1940 that ZFC cannot disprove CH, and Cohen showed in 1963 that ZFC cannot prove CH. CH is independent of ZFC — it is a genuinely undecidable statement in standard set theory.

The axiom of choice plays a hidden but essential role throughout this theory. Without the axiom of choice, not every set can be well-ordered, and therefore not every set has a cardinality in the aleph hierarchy. The axiom of choice guarantees that every set is in bijection with some initial ordinal, making the aleph sequence a complete classification of all cardinalities. This is why the axiom of choice is not merely a convenience but a structural prerequisite for the theory of infinite cardinals to work as described.
