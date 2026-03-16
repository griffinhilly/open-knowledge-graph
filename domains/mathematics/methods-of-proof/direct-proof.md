---
id: direct-proof
title: Direct Proof
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proof-structure-and-terminology
  type: hard
builds-toward:
- proof-by-contrapositive
- mathematical-induction
tags:
- proof
- technique
- forward
stage: formal-systems
status: draft
---

# Direct Proof

## Core Idea
A direct proof assumes the hypothesis and uses valid logical steps to derive the conclusion. To prove p → q, assume p is true and show q must follow, establishing the implication.

## How It's Best Learned
Write the hypothesis as a given, list what follows step-by-step with justifications, and show how you reach the conclusion.

## Common Misconceptions
- Proving the converse (q → p) instead of the original statement (p → q).
- Assuming the conclusion is true at the start rather than deriving it.

## Explainer

You have already learned, from proof-structure-terminology, that a mathematical proof is a sequence of logical steps leading from accepted premises to a conclusion. A **direct proof** is the most natural way to build that sequence: start with what you're given, apply valid reasoning rules, and walk forward until you arrive at what you want to show.

The structure is always the same. To prove "if P, then Q," you write: "Assume P." Then you deduce a sequence of intermediate statements, each following from previous ones by a logical rule, a definition, or a known theorem. The proof ends when you reach Q. Every step needs a justification — "by definition of X," "by hypothesis," "by Theorem 5," "by algebraic manipulation." The chain of justifications is what makes it a proof rather than an assertion.

Consider proving: "If n is an even integer, then n² is even." Assume n is even. By definition of evenness, n = 2k for some integer k. Then n² = (2k)² = 4k² = 2(2k²). Since 2k² is an integer, n² has the form 2m for an integer m, so n² is even. Done. Notice the structure: unpack definitions, do algebra, repack into the definition of what you need to prove. This is the standard pattern for direct proofs about algebraic or divisibility claims.

The most common errors are subtle flips of direction. Proving the **converse** (assuming Q and deriving P) does not prove the original statement — it proves a different claim. Assuming the **conclusion** at the start and working backward also fails: if you write "suppose n² is even" in the middle of a proof that n² is even, you have assumed what you are trying to show, which is circular. The key discipline is: the hypothesis P is the only thing you are allowed to assume at the start. Everything else must be derived. If you find yourself needing to assume Q to make the argument work, that is a warning sign to check whether you have inverted the implication.
