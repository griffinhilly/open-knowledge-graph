---
id: existence-proofs
title: Existence Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-by-contradiction
  type: soft
tags:
- existence
- proof
- quantifiers
stage: formal-systems
status: draft
---

# Existence Proofs

## Core Idea
An existence proof establishes that an object satisfying certain properties exists. This can be constructive (exhibiting the object explicitly) or non-constructive (showing non-existence leads to contradiction). Both are valid.

## Explainer

In mathematics, an **existence proof** answers the question "does there exist an object satisfying property P?" with a definitive yes. What counts as a valid answer — and which kind of answer is philosophically satisfying — has been debated by mathematicians for over a century, making existence proofs one of the most intellectually interesting topics in the methods-of-proof toolkit.

The most direct approach is a **constructive proof**: you actually exhibit the object. To prove there exists a prime number greater than 100, you can simply observe that 101 is prime and 101 > 100. Done. The object is in hand. Constructive proofs are the gold standard when available, because they not only confirm existence but also give you something to work with. If you need an algorithm, a specific value, or a counterexample, a constructive proof delivers it directly.

The alternative is a **non-constructive proof**: you show that the object's non-existence leads to a contradiction, and therefore it must exist — without ever producing it. You're familiar with this pattern from proof by contradiction. A famous example is the proof that there exist irrational numbers a and b such that aᵇ is rational. Consider √2^√2. Either this is rational (done — take a = b = √2) or it is irrational. If irrational, then (√2^√2)^√2 = √2² = 2, which is rational. So in either case we have an example — but we never determined which case holds. The object exists; we just don't know which one.

This non-constructive style can feel philosophically unsatisfying: you've proven something exists without ever finding it. Some mathematicians (constructivists) reject non-constructive proofs on principle. In mainstream mathematics, however, both methods are fully accepted. What makes an existence proof valid is logical correctness, not the ability to compute the witness. When you write an existence proof, always ask: is this constructive or non-constructive? If non-constructive, be explicit that you're using contradiction, and make sure the argument is airtight — you're asserting something exists that you cannot touch.
