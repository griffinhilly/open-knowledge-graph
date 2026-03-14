---
id: zfc-independence-from-other-axioms
title: Independence in ZFC and Limitations of Axiomatization
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: inner-models-relative-consistency
  type: hard
- id: forcing-intro
  type: hard
tags:
- independence
- zfc
- continuum
- axioms
stage: formal-systems
status: draft
---

# Independence in ZFC and Limitations of Axiomatization

## Core Idea
The continuum hypothesis (CH) and the axiom of choice (AC) are independent of ZFC: both ZFC + CH and ZFC + ¬CH are consistent, as are ZFC + AC and ZFC + ¬AC (without choice, not AC). Gödel proved ZFC ⊢ Con(ZFC → Con(ZFC+CH)); Cohen's forcing proved ZFC ⊢ Con(ZFC → Con(ZFC + ¬CH)). These results show that ZFC cannot uniquely determine all mathematical truths.

## How It's Best Learned
Understand Gödel's proof that CH holds in L. Learn forcing: Cohen's extension of models to produce violations of CH. Compare model-theoretic and syntactic consistency. Discuss implications for mathematical truth and foundational pluralism.

## Common Misconceptions
- Assuming independence means both options are 'equally true' (truth in V may favor one; we simply cannot prove it in ZFC).
- Confusing statement independence with the consistency of negating axioms; independence refers to theorems, not axioms themselves.
