---
id: proving-by-direct-method
title: Proving by Direct Method
domain: mathematics
course: methods-of-proof
prerequisites:
- id: conditional-implication-statements
  type: hard
- id: modus-ponens-and-modus-tollens
  type: soft
- id: universal-quantifier-introduction
  type: soft
builds-toward:
- proving-by-contrapositive
- proving-by-cases
tags:
- proof
- direct proof
- deduction
stage: formal-systems
status: draft
---

# Proving by Direct Method

## Core Idea
Direct proof establishes a conclusion P by assuming the hypothesis H and using logical deduction (modus ponens, substitution, algebra) to reach P. The structure is: assume H is true, then apply valid inferences to derive P. Direct proof is the most straightforward proof method.

## How It's Best Learned
Study well-written proofs and identify the hypothesis, conclusion, and steps of deduction. Write simple proofs and get feedback on clarity and rigor.

## Common Misconceptions
- Confusing assuming the hypothesis with circular reasoning.
- Skipping steps and claiming something is 'obvious'.
- Using the conclusion somewhere in the proof (begging the question).

## Explainer

Most mathematical theorems have the form "if H, then P" — a conditional statement. You've seen this in your study of conditional implication: the claim is not that H or P is unconditionally true, but that P follows from H. **Direct proof** is the method of taking that conditional seriously: assume H is true, then reason forward step by step until you reach P. Every step must be a valid logical inference — substitution, algebraic manipulation, applying a known theorem, or an application of modus ponens.

Here is a simple example. Theorem: if n is an odd integer, then n² is odd. Direct proof: assume n is odd. By definition of odd, n = 2k + 1 for some integer k. Then n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1. Since 2k² + 2k is an integer, n² has the form 2m + 1 and is therefore odd. The structure is: unpack the hypothesis (n is odd means n = 2k + 1), compute (square it), recognize the pattern (it's 2m + 1), invoke the definition (therefore odd). That's a direct proof.

A key confusion for beginners is whether assuming H is circular. It is not. Circular reasoning would be using P in order to prove P — sneaking the conclusion into the argument. Assuming H to prove P is exactly what the conditional "if H then P" licenses you to do. You are not asserting H is always true; you are saying "under the assumption that H holds, here is why P must also hold." This is precisely the force of modus ponens, which you've studied: from H and H → P, conclude P.

The other common failure mode is **begging the question** — using the conclusion at some step in the argument. For example, to prove that if n² is even then n is even, you might be tempted to say "since n² is even, n must be even." That is just restating the conclusion, not proving it. A correct direct proof would need more structure (in fact, this theorem is easier by contrapositive). Direct proof works best when the hypothesis, when unpacked, contains exactly the algebraic or logical machinery needed to produce the conclusion. When the hypothesis and conclusion feel far apart — when you'd need to "go backward" from the conclusion to find the argument — an indirect method (contrapositive or contradiction) is usually cleaner.
