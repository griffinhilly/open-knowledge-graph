---
id: continuum-hypothesis
title: Continuum Hypothesis
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: cantor-theorem
  type: hard
- id: infinite-cardinal-numbers
  type: hard
- id: cardinal-arithmetic
  type: soft
- id: cardinality-and-countability
  type: soft
- id: cantor-diagonalization
  type: soft
- id: uncountable-sets-and-cantor-diagonalization
  type: soft
builds-toward:
- independence-results-set-theory
tags:
- continuum hypothesis
- independence
- cardinals
- Cantor
- Godel
- Cohen
stage: formal-systems
status: validated
---

# Continuum Hypothesis

## Core Idea
The continuum hypothesis (CH), proposed by Cantor in 1878, asserts there is no cardinal strictly between ℵ₀ (the cardinality of ℕ) and 2^ℵ₀ (the cardinality of ℝ): equivalently, 2^ℵ₀ = ℵ₁. Gödel showed in 1940 that CH cannot be refuted from ZFC (it holds in the constructible universe L); Cohen showed in 1963 that it cannot be proved from ZFC either (his forcing technique constructs models where 2^ℵ₀ = ℵ₂ or any other prescribed value). The independence of CH was the first major application of forcing and established that the size of the continuum is fundamentally undetermined by the standard axioms.

## How It's Best Learned
First situate CH: ℕ is countable, ℝ is uncountable, and the question is whether anything lies strictly between. Study Cantor's original formulation, then understand at the sketch level how Gödel's L witnesses CH cannot be disproved, and how forcing witnesses it cannot be proved. The independence result is as important as the statement.

## Common Misconceptions
- CH is not an open question awaiting a clever proof or counterexample — it is logically independent of ZFC, so neither proof nor disproof exists within the system.
- The generalized continuum hypothesis (GCH), asserting 2^ℵ_α = ℵ_{α+1} for all α, is also independent of ZFC.

## Explainer

From Cantor's theorem, you know that the power set 𝒫(X) is strictly larger than X for any set X, so |𝒫(ℕ)| > |ℕ|. Since 𝒫(ℕ) has the same cardinality as ℝ (both equal 2^{ℵ₀}), there is a strict jump from ℕ to ℝ. The **Continuum Hypothesis (CH)** asks: is there any infinite cardinality strictly between |ℕ| = ℵ₀ and |ℝ| = 2^{ℵ₀}? Equivalently, is 2^{ℵ₀} = ℵ₁—does the cardinality of the reals equal the *first* uncountable cardinal? Cantor believed no such intermediate cardinality existed and worked intensively to prove it. The question became the first problem on Hilbert's famous 1900 list. The eventual answer was not a proof or a refutation but something more radical: the question is **independent of the standard axioms**.

To understand what independence means, recall that a statement is independent of an axiomatic system if neither it nor its negation can be derived from those axioms. Gödel showed in 1940 that CH *cannot be disproved* from ZFC by constructing **L**, the **constructible universe**. L is an inner model of ZFC—a class of sets built by an explicit staged construction where each set is "definable" from previously constructed sets. In L, the cardinality structure is as tight as possible: 2^{ℵ₀} = ℵ₁, and in fact the **Generalized Continuum Hypothesis** (GCH: 2^{ℵ_α} = ℵ_{α+1} for all α) holds. Since L is a legitimate model of ZFC, ZFC cannot prove CH is false.

Paul Cohen showed in 1963 that CH also *cannot be proved* from ZFC. His technique, **forcing**, adds new "generic" sets to a base model by specifying what properties they must satisfy without constructing them explicitly—analogous to adding a transcendental element to a field. By adding ℵ₂ many new real numbers through forcing while carefully preserving cardinal structure (not "collapsing" ℵ₁ to ℵ₀), Cohen produced a model of ZFC where 2^{ℵ₀} = ℵ₂, violating CH. **König's theorem** places the only constraint: 2^{ℵ₀} must have uncountable cofinality (it cannot be, e.g., ℵ_ω), but subject to this constraint, forcing can realize any prescribed value for 2^{ℵ₀}.

The independence of CH is philosophically profound. It is not a temporary gap in mathematical knowledge—it is a structural feature of ZFC. The question has a definite answer in each *model* of ZFC (true in L, false in Cohen's model) but no answer within ZFC alone. Some set theorists respond by seeking **new axioms** that resolve CH: large cardinal axioms and forcing axioms like **Martin's Maximum** tend to imply 2^{ℵ₀} = ℵ₂, suggesting CH is false. Others accept that set theory has multiple equally legitimate "universes" with no canonical size for the continuum. This divide—between those seeking a unique set-theoretic universe and those embracing a multiverse—is one of the central open debates in the foundations of mathematics today.
