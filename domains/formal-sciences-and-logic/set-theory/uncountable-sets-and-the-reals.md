---
id: uncountable-sets-and-the-reals
title: Uncountable Sets and Cantor's Diagonal Argument
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: countable-sets-and-enumeration
  type: hard
- id: cantor-pairing-and-enumerations
  type: soft
builds-toward:
- cardinal-comparison-and-schroeder-bernstein
- aleph-and-beth-hierarchy-introduction
tags:
- uncountability
- diagonal-argument
- continuum
stage: formal-systems
status: draft
---

# Uncountable Sets and Cantor's Diagonal Argument

## Core Idea
Cantor's diagonal argument proves no bijection exists between ℕ and ℝ: assuming a listing of all reals, construct a new real not on the list by flipping digits, creating a contradiction. Therefore ℝ is uncountable, disproving the notion that all infinities are equal and establishing a strict hierarchy of infinities.

## How It's Best Learned
Work through the diagonal argument for ℕ and ℝ explicitly; then see how the same proof adapts to show 𝒫(ℕ) is uncountable.

## Explainer

You already know, from your study of countable sets, that "infinite" does not mean "the same size." You can put ℕ and ℤ and ℚ into bijection with each other — each can be listed in a sequence that eventually reaches every element. The question is whether the same is true for ℝ. Cantor's diagonal argument answers: no. But the proof is not just a negative result — it is a constructive recipe for defeating any proposed listing.

Assume for contradiction that all real numbers in [0,1] can be listed: r₁, r₂, r₃, … . Write each as an infinite decimal expansion. Now focus on the **diagonal** of this infinite table — take the first decimal digit of r₁, the second decimal digit of r₂, the third digit of r₃, and so on. From this diagonal sequence, construct a new real number d by changing every digit (for instance, replace each digit d by 5 if it is not 5, and by 6 if it is 5). What is special about d? It differs from r₁ in position 1, from r₂ in position 2, and from rₙ in position n — so d cannot be anywhere on the list. But d is a well-defined real number in [0,1], which means the list was incomplete. This contradicts our assumption, so no such list exists: ℝ is **uncountable**.

The proof is often summarized as "there are more reals than naturals," but the deeper point is that the argument works by construction, not coincidence. Given any proposed listing, the diagonal procedure creates a real not on it. This means no listing strategy — however clever — can succeed. The argument also generalizes far beyond ℝ: for any set S, the same diagonal logic shows that 𝒫(S) (the power set, the set of all subsets) has strictly greater cardinality than S itself. There is no largest infinite set — the power set operation always produces a strictly larger one.

This establishes a **hierarchy of infinities**. The cardinality of ℕ is called **ℵ₀** (aleph-null); the cardinality of ℝ is called the **continuum**, often written **c** or **2^ℵ₀**, and it is strictly greater than ℵ₀. Whether there exists a cardinality strictly between ℵ₀ and c is the **Continuum Hypothesis** — a statement that turns out to be independent of the standard axioms of set theory (ZFC). You can neither prove nor disprove it from those axioms, which is itself one of the deepest results in twentieth-century logic. Cantor's diagonal argument is the tool that opens this entire world.
