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
- id: cardinal-numbers-basic-theory
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
status: validated
---

# The Aleph and Beth Hierarchies of Infinities

## Core Idea
The aleph numbers ℵ₀, ℵ₁, ℵ₂, ... enumerate infinite cardinalities in increasing order; ℵ₀ is countable infinity, ℵ₁ the next larger cardinal. The beth numbers ℶ₀, ℶ₁, ℶ₂, ... are defined by iterating power sets: ℶ₀ = ℵ₀, ℶ_{n+1} = 2^{ℶ_n}. The continuum hypothesis asks whether ℶ₁ = ℵ₁.

## Questions

```yaml
- question: "The beth number ℶ₁ equals the cardinality of the real numbers. Which statement correctly describes its relationship to the aleph hierarchy?"
  type: multiple-choice
  options:
    - "ℶ₁ = ℵ₁ by definition, since both represent the first uncountable cardinal"
    - "ℶ₁ ≥ ℵ₁ for certain, but whether it equals ℵ₁, ℵ₂, or a larger cardinal depends on which axioms you assume"
    - "ℶ₁ = ℵ₀ because the real numbers can be encoded as natural numbers with the right bijection"
    - "ℶ₁ > ℵ₁ necessarily, because every power set produces a cardinal larger than the next aleph"
  answer: 1
  explanation: "ℶ₁ = 2^{ℵ₀}, the cardinality of the reals. By Cantor's theorem, 2^{ℵ₀} > ℵ₀, so ℶ₁ is uncountable. By definition of ℵ₁ as the smallest uncountable cardinal, ℶ₁ ≥ ℵ₁. But whether ℶ₁ equals ℵ₁ (the Continuum Hypothesis) or is larger (ℵ₂, ℵ₃, ...) is independent of ZFC. Option A conflates two different definitions: ℵ₁ is defined by well-ordering (the next cardinal after ℵ₀), while ℶ₁ is defined by power set (2^{ℵ₀}). These are different operations and need not produce the same result."

- question: "The Continuum Hypothesis asks whether ℵ₁ = ℶ₁ and is 'independent of ZFC.' What does independence mean here?"
  type: multiple-choice
  options:
    - "The question will be resolved once mathematicians develop a sufficiently powerful proof technique"
    - "ZFC can prove the hypothesis is true, but not that it is false"
    - "Neither the hypothesis nor its negation can be derived from ZFC's axioms — both are consistent with ZFC"
    - "The question is meaningless because infinite cardinalities are not mathematically well-defined"
  answer: 2
  explanation: "Independence means exactly this: you can add CH as an axiom to ZFC and get a consistent theory, and you can add its negation (¬CH) and also get a consistent theory. Gödel (1940) showed ZFC + CH is consistent; Cohen (1963) showed ZFC + ¬CH is consistent. The question is not unanswered for lack of effort — it is genuinely undetermined by the axioms as written, in the same way the parallel postulate is independent of the other Euclidean axioms. Any 'universe' of set theory satisfying ZFC can make CH true or false."

- question: "ℵ₁ is the smallest infinite cardinal strictly larger than ℵ₀, not by any particular construction, but by axiomatic definition of the aleph hierarchy."
  type: true-false
  answer: true
  explanation: "The aleph hierarchy is defined by well-ordering: ℵ₁ is the smallest cardinal greater than ℵ₀ by axiom — there is no infinite cardinal strictly between them by definition. This is purely ordinal and tells you nothing about what ℵ₁ 'looks like' as a set. By contrast, ℶ₁ is constructed concretely as 2^{ℵ₀} — the power set of the naturals. The two definitions are genuinely different operations, which is why their equality is a non-trivial conjecture."

- question: "The beth hierarchy and the aleph hierarchy are both defined the same way — by taking successors of infinite cardinals in increasing order."
  type: true-false
  answer: false
  explanation: "The aleph hierarchy is defined axiomatically as the well-ordered sequence of all infinite cardinals: ℵ₁ is the next cardinal after ℵ₀, ℵ₂ is the next after ℵ₁, and so on. The beth hierarchy is defined constructively by iterated power sets: ℶ_{n+1} = 2^{ℶ_n}. These are fundamentally different operations. 'The next well-ordered cardinal' and 'the power set of the previous cardinal' need not produce the same sequence — and whether they do (the Generalized Continuum Hypothesis) is precisely what ZFC cannot determine."

- question: "Why can't mathematicians simply prove or disprove the Continuum Hypothesis using standard set theory (ZFC)?"
  type: short-answer
  answer: "Because both CH and its negation are consistent with ZFC. Gödel (1940) showed that adding CH to ZFC produces no contradiction — he constructed a model of set theory where CH holds. Cohen (1963) showed that adding ¬CH also produces no contradiction — he constructed a model where CH fails. This means ZFC's axioms do not contain enough information to determine the size of the real number continuum relative to the aleph hierarchy. The axioms leave the question genuinely open, just as the parallel postulate is left open by the other Euclidean axioms."
  explanation: "This independence result is one of the deepest results in 20th-century mathematics. It reveals that the 'standard' axioms of set theory don't pin down the structure of infinite cardinalities precisely — the hierarchy of infinities has genuine degrees of freedom that ZFC doesn't resolve. Different consistent universes of set theory can have different answers to whether there is a cardinal between ℵ₀ and 2^{ℵ₀}."
```

## Explainer

You already know two infinite cardinalities: ℵ₀, the size of the natural numbers (and all countably infinite sets), and the cardinality of the real numbers (and all uncountably infinite sets). You also know from Cantor's theorem that the power set of any set is strictly larger — there is no surjection from a set to its power set. This creates an ascending chain of infinities, and the aleph and beth hierarchies give two different ways to name and organize them.

The **aleph numbers** (ℵ₀, ℵ₁, ℵ₂, ...) are defined axiomatically as the well-ordered infinite cardinals. ℵ₀ is the smallest infinite cardinal — the size of ℕ. ℵ₁ is the next infinite cardinal — the smallest uncountable cardinal, meaning there is no infinite cardinal strictly between ℵ₀ and ℵ₁ by definition. ℵ₂ is the next after that, and so on. The aleph hierarchy gives you the complete list of all infinite cardinals in order, but it is defined by well-ordering — it tells you the cardinals exist and are ordered, but not what they equal in terms of more familiar sets.

The **beth numbers** (ℶ₀, ℶ₁, ℶ₂, ...) are defined concretely by iterated power sets. ℶ₀ = ℵ₀ (the naturals). ℶ₁ = 2^{ℶ₀} = 2^{ℵ₀} — the cardinality of the power set of ℕ, which equals |ℝ|, the cardinality of the real numbers. ℶ₂ = 2^{ℶ₁}, the cardinality of the set of all real-valued functions on ℝ. Each beth number is the power set of its predecessor. The beth hierarchy grows rapidly — ℶ₁ already exceeds ℵ₀ and may exceed ℵ₁, ℵ₂, or more, depending on what axioms you assume.

The relationship between the two hierarchies is the heart of the matter. Because well-ordering (the aleph hierarchy) and power sets (the beth hierarchy) are different operations, there is no a priori reason they should coincide. The **Continuum Hypothesis** asks whether ℶ₁ = ℵ₁ — is the cardinality of the reals exactly the first uncountable cardinal, with no cardinals between ℵ₀ and 2^{ℵ₀}? The **Generalized Continuum Hypothesis** asks whether ℶ_α = ℵ_α for every ordinal α — do the two hierarchies always march in lockstep? Both hypotheses are independent of the standard axioms of set theory ZFC, meaning they can neither be proved nor disproved from those axioms alone. This independence is what makes the question deep: the gap between "the next well-ordered cardinal" and "the power set" is genuinely undetermined by the rules of set theory as we know them.
