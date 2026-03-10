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
status: draft
---

# Continuum Hypothesis

## Core Idea
The continuum hypothesis (CH), proposed by Cantor in 1878, asserts there is no cardinal strictly between ℵ₀ (the cardinality of ℕ) and 2^ℵ₀ (the cardinality of ℝ): equivalently, 2^ℵ₀ = ℵ₁. Gödel showed in 1940 that CH cannot be refuted from ZFC (it holds in the constructible universe L); Cohen showed in 1963 that it cannot be proved from ZFC either (his forcing technique constructs models where 2^ℵ₀ = ℵ₂ or any other prescribed value). The independence of CH was the first major application of forcing and established that the size of the continuum is fundamentally undetermined by the standard axioms.

## How It's Best Learned
First situate CH: ℕ is countable, ℝ is uncountable, and the question is whether anything lies strictly between. Study Cantor's original formulation, then understand at the sketch level how Gödel's L witnesses CH cannot be disproved, and how forcing witnesses it cannot be proved. The independence result is as important as the statement.

## Common Misconceptions
- CH is not an open question awaiting a clever proof or counterexample — it is logically independent of ZFC, so neither proof nor disproof exists within the system.
- The generalized continuum hypothesis (GCH), asserting 2^ℵ_α = ℵ_{α+1} for all α, is also independent of ZFC.
