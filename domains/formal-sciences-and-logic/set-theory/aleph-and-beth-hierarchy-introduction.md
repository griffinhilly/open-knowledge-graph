---
id: aleph-and-beth-hierarchy-introduction
title: The Aleph and Beth Hierarchies of Infinities
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: uncountable-sets-and-the-reals
  type: hard
- id: cardinal-comparison-and-schroeder-bernstein
  type: hard
builds-toward:
- aleph-numbers
- beth-numbers
- continuum-hypothesis
- infinite-cardinal-numbers
tags:
- hierarchy
- infinite-cardinals
- power-sets
stage: formal-systems
status: draft
---

# The Aleph and Beth Hierarchies of Infinities

## Core Idea
The aleph numbers ℵ₀, ℵ₁, ℵ₂, ... enumerate infinite cardinalities in increasing order; ℵ₀ is countable infinity, ℵ₁ the next larger cardinal. The beth numbers ℶ₀, ℶ₁, ℶ₂, ... are defined by iterating power sets: ℶ₀ = ℵ₀, ℶ_{n+1} = 2^{ℶ_n}. The continuum hypothesis asks whether ℶ₁ = ℵ₁.

## Explainer

You already know two infinite cardinalities: ℵ₀, the size of the natural numbers (and all countably infinite sets), and the cardinality of the real numbers (and all uncountably infinite sets). You also know from Cantor's theorem that the power set of any set is strictly larger — there is no surjection from a set to its power set. This creates an ascending chain of infinities, and the aleph and beth hierarchies give two different ways to name and organize them.

The **aleph numbers** (ℵ₀, ℵ₁, ℵ₂, ...) are defined axiomatically as the well-ordered infinite cardinals. ℵ₀ is the smallest infinite cardinal — the size of ℕ. ℵ₁ is the next infinite cardinal — the smallest uncountable cardinal, meaning there is no infinite cardinal strictly between ℵ₀ and ℵ₁ by definition. ℵ₂ is the next after that, and so on. The aleph hierarchy gives you the complete list of all infinite cardinals in order, but it is defined by well-ordering — it tells you the cardinals exist and are ordered, but not what they equal in terms of more familiar sets.

The **beth numbers** (ℶ₀, ℶ₁, ℶ₂, ...) are defined concretely by iterated power sets. ℶ₀ = ℵ₀ (the naturals). ℶ₁ = 2^{ℶ₀} = 2^{ℵ₀} — the cardinality of the power set of ℕ, which equals |ℝ|, the cardinality of the real numbers. ℶ₂ = 2^{ℶ₁}, the cardinality of the set of all real-valued functions on ℝ. Each beth number is the power set of its predecessor. The beth hierarchy grows rapidly — ℶ₁ already exceeds ℵ₀ and may exceed ℵ₁, ℵ₂, or more, depending on what axioms you assume.

The relationship between the two hierarchies is the heart of the matter. Because well-ordering (the aleph hierarchy) and power sets (the beth hierarchy) are different operations, there is no a priori reason they should coincide. The **Continuum Hypothesis** asks whether ℶ₁ = ℵ₁ — is the cardinality of the reals exactly the first uncountable cardinal, with no cardinals between ℵ₀ and 2^{ℵ₀}? The **Generalized Continuum Hypothesis** asks whether ℶ_α = ℵ_α for every ordinal α — do the two hierarchies always march in lockstep? Both hypotheses are independent of the standard axioms of set theory ZFC, meaning they can neither be proved nor disproved from those axioms alone. This independence is what makes the question deep: the gap between "the next well-ordered cardinal" and "the power set" is genuinely undetermined by the rules of set theory as we know them.
