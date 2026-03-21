---
id: aleph-numbers
title: Aleph Numbers
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: infinite-cardinal-numbers
  type: hard
- id: ordinal-numbers-and-order
  type: soft
builds-toward:
- beth-numbers
- continuum-hypothesis
tags:
- aleph
- cardinal numbers
- aleph-null
- aleph-one
- cardinal successor
stage: formal-systems
status: draft
---

# Aleph Numbers

## Core Idea
The aleph numbers ℵ₀, ℵ₁, ℵ₂, ... enumerate the infinite cardinal numbers in increasing order, indexed by ordinals. ℵ₀ is the cardinality of ℕ — the smallest infinite cardinal. ℵ₁ is the smallest cardinal greater than ℵ₀, ℵ₂ the smallest greater than ℵ₁, and in general ℵ_{α+1} is the cardinal successor of ℵ_α. At limit ordinals λ, ℵ_λ = sup{ℵ_β : β < λ}. Every infinite cardinal is an aleph (assuming the axiom of choice, which guarantees that every set can be well-ordered). The aleph sequence thus provides a complete, well-ordered enumeration of all infinite cardinalities.

## How It's Best Learned
Begin with ℵ₀ and its closure properties (ℵ₀ + ℵ₀ = ℵ₀, ℵ₀ · ℵ₀ = ℵ₀). Then define ℵ₁ as the cardinality of the set of all countable ordinals (ω₁), and verify that ω₁ is uncountable. Understand that the continuum hypothesis is precisely the claim ℵ₁ = 2^{ℵ₀}. Work through the distinction between 'the next cardinal' (ℵ_{α+1}) and 'the power set cardinal' (2^{ℵ_α}) — these are conceptually different operations that may or may not coincide.

## Common Misconceptions
- ℵ₁ is not defined as the cardinality of the reals — it is the smallest uncountable cardinal. Whether |ℝ| = ℵ₁ is the content of the continuum hypothesis, which is independent of ZFC.
- The aleph sequence requires the axiom of choice; without it, there can be infinite cardinals that are incomparable and do not appear in the aleph hierarchy.

## Questions

```yaml
- question: "A student claims: 'ℵ₁ is just another name for the cardinality of the real numbers — they're defined to be the same thing.' What is wrong with this claim?"
  type: multiple-choice
  options:
    - "Nothing is wrong — ℵ₁ and |ℝ| are equal by definition in standard set theory"
    - "ℵ₁ is defined as the smallest uncountable cardinal; whether |ℝ| = ℵ₁ is the continuum hypothesis, which is independent of ZFC"
    - "The student has the direction reversed — |ℝ| = ℵ₀ and ℵ₁ is strictly larger than the reals"
    - "ℵ₁ is not well-defined without additional axioms beyond ZFC"
  answer: 1
  explanation: "ℵ₁ is defined purely as the cardinal successor of ℵ₀ — the smallest uncountable cardinal, constructed as the cardinality of the set ω₁ of all countable ordinals. The cardinality of the reals is 2^{ℵ₀}, which is provably uncountable but whose position in the aleph hierarchy is not determined by ZFC alone. The continuum hypothesis (CH) is precisely the claim that 2^{ℵ₀} = ℵ₁. Gödel and Cohen together proved CH is independent of ZFC — it can neither be proved nor disproved. Defining ℵ₁ as |ℝ| conflates a definition with an open mathematical question."

- question: "What role does the axiom of choice play in the relationship between the aleph numbers and all infinite cardinalities?"
  type: multiple-choice
  options:
    - "The axiom of choice defines what the aleph numbers are — without it, ℵ₀ does not exist"
    - "Under the axiom of choice, every infinite cardinal equals ℵ_α for some ordinal α, making the alephs a complete account of all infinite cardinalities"
    - "The axiom of choice is needed only to define ℵ₁ and beyond; ℵ₀ exists without it"
    - "The axiom of choice guarantees that 2^{ℵ₀} = ℵ₁"
  answer: 1
  explanation: "The axiom of choice (AC) guarantees that every set can be well-ordered. This implies that every infinite cardinal is comparable to the ordinals and therefore equals ℵ_α for some ordinal α. Without AC, there can be infinite sets whose cardinality is incomparable to any aleph — 'wild' cardinals that fall outside the hierarchy entirely. With AC, the alephs exhaust all infinite cardinalities: every infinite set has a cardinality that appears somewhere in the sequence ℵ₀, ℵ₁, ℵ₂, .... Option D is false — AC says nothing about where 2^{ℵ₀} sits in the aleph hierarchy."

- question: "ℵ₁ is defined as the cardinality of the real number line."
  type: true-false
  answer: false
  explanation: "ℵ₁ is defined as the smallest uncountable cardinal — the cardinality of the set ω₁ of all countable ordinals. The cardinality of the real line is 2^{ℵ₀}, the cardinality of the power set of ℕ. Whether 2^{ℵ₀} = ℵ₁ is the continuum hypothesis, which is independent of ZFC. This is one of the most important conceptual distinctions in set theory: the cardinal successor operation (giving the next cardinal) and the power set operation (giving the cardinality of all subsets) are different constructions that happen to produce the same value only if the continuum hypothesis holds — which we cannot prove or disprove."

- question: "Under the axiom of choice, every infinite cardinal is equal to ℵ_α for some ordinal α, so the aleph sequence contains all infinite cardinalities."
  type: true-false
  answer: true
  explanation: "This is one of the most important consequences of the axiom of choice. AC implies the well-ordering theorem: every set can be well-ordered. Well-ordered sets have cardinalities that are aleph numbers (since every well-ordered cardinal is an initial ordinal, and initial ordinals are indexed by the aleph sequence). Therefore, assuming AC, no infinite cardinality 'falls between' alephs or is incomparable to them — the aleph hierarchy is complete and total. Without AC, this fails: there can be infinite cardinals that are incomparable and do not appear in the hierarchy."

- question: "What is the conceptual difference between ℵ₁ (the cardinal successor of ℵ₀) and 2^{ℵ₀} (the power set cardinal of ℵ₀), and why does the distinction matter?"
  type: short-answer
  answer: "ℵ₁ is defined by the successor operation on cardinals: it is the smallest cardinal strictly greater than ℵ₀, constructed as the cardinality of all countable ordinals. 2^{ℵ₀} is defined by the power set operation: it is the cardinality of the set of all subsets of a countably infinite set (equivalently, the cardinality of the real numbers). These are two genuinely different mathematical operations — successor and power set — that produce different cardinals in general. Whether they happen to produce the same cardinal (ℵ₁ = 2^{ℵ₀}) is the continuum hypothesis, proved by Gödel and Cohen to be independent of ZFC. The distinction matters because conflating them assumes the answer to an open (undecidable) question."
  explanation: "The continuum hypothesis is undecidable precisely because the successor operation and the power set operation are conceptually distinct. You can build models of set theory where 2^{ℵ₀} = ℵ₁ (Gödel's constructible universe L) and models where 2^{ℵ₀} = ℵ₂, ℵ₃, or even larger alephs (Cohen's forcing models). In all these models, ℵ₁ is still the smallest uncountable cardinal; it's just that the power set of ℕ lands at different positions in the aleph hierarchy depending on the model."
```

## Explainer

You already know about infinite cardinal numbers: the idea that two sets have the same cardinality when a bijection exists between them, and that not all infinities are the same size. The aleph numbers give infinite cardinals a systematic name and a complete well-ordered listing. The starting point, **ℵ₀** (aleph-null), is the cardinality of the natural numbers ℕ — the smallest infinite cardinal, as you verified when showing that ℤ, ℚ, and ℕ×ℕ are all countable. Any set that can be put in bijection with ℕ has cardinality ℵ₀.

The next step requires ordinal numbers. The set ω₁ of all countable ordinals (all ordinals in bijection with a subset of ℕ) is itself *not* countable — if it were, it would be a countable ordinal and would appear in itself, a contradiction. So ω₁ is an uncountable well-ordered set, and its cardinality is defined to be **ℵ₁**, the smallest uncountable cardinal. Continuing the pattern: ω₂ is the set of all ordinals of cardinality ≤ ℵ₁, and its cardinality is **ℵ₂**. In general, ℵ_{α+1} is the cardinality of the set of all ordinals of cardinality ≤ ℵ_α — the "next" infinite cardinal after ℵ_α. At limit ordinals λ (ordinals with no immediate predecessor), ℵ_λ is the supremum of all earlier alephs.

The critical conceptual distinction is between **ℵ_{α+1}** (the cardinal successor of ℵ_α, defined as the next larger cardinal) and **2^{ℵ_α}** (the power set cardinal, the cardinality of the set of all subsets of a set of size ℵ_α). These are conceptually different operations. Cardinal arithmetic tells us 2^{ℵ₀} is the cardinality of ℝ (and of the power set of ℕ), but where this cardinal sits in the aleph hierarchy is exactly the **continuum hypothesis**: the claim that 2^{ℵ₀} = ℵ₁. Gödel and Cohen together proved this is independent of ZFC — neither provable nor disprovable — so the relationship between power sets and the aleph hierarchy is genuinely undecidable from the standard axioms.

Finally, the axiom of choice is what makes the aleph numbers a *complete* account of infinite cardinality. Under the axiom of choice, every set can be well-ordered, and every infinite cardinal is therefore equal to ℵ_α for some ordinal α. Without choice, there can be infinite sets with cardinality incomparable to any aleph — "wild" cardinals that do not fit into the aleph hierarchy at all. With choice, the hierarchy is total: the alephs are *all* the infinite cardinals, and the question of how a set's cardinality relates to the alephs is always well-posed. This completeness of the aleph hierarchy under AC is one of the strongest arguments for adopting the axiom of choice as a set-theoretic foundation.
