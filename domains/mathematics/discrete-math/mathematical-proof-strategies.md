---
id: mathematical-proof-strategies
title: Proof Strategies in Discrete Mathematics
domain: mathematics
course: discrete-math
prerequisites:
- id: formal-logic-propositions
  type: hard
- id: mathematical-induction-intro
  type: hard
builds-toward:
- counting-fundamentals-discrete
- divisibility-and-primes-discrete
tags:
- proofs
- induction
- contradiction
- strategy
stage: formal-systems
status: draft
---

# Proof Strategies in Discrete Mathematics

## Core Idea
Discrete proofs rely on five main strategies: direct proof, proof by contrapositive, proof by contradiction, proof by cases, and mathematical induction. Each is suited to different claim types—knowing which to apply is an essential skill.

## How It's Best Learned
Study worked examples of each proof type. Write multiple proofs of the same statement using different methods to see strengths and weaknesses. Induction requires both base case and inductive step clarity.

## Common Misconceptions
Proof by contradiction assumes the negation of the goal, not intermediate steps. Induction is not intuitive reasoning—the inductive step must be rigorous and valid for all values.

## Explainer

From your prerequisite in formal logic, you know that a mathematical statement is a proposition that is either true or false, and that logical connectives govern how propositions combine. Proof is the mechanism for establishing truth beyond doubt. The five main strategies differ not in rigor but in *direction*: each approaches the same destination via a different path. Choosing the right strategy is itself a skill, and it develops through exposure to many examples.

**Direct proof** is the default: assume the hypothesis, apply definitions and theorems, derive the conclusion. To prove "if n is even then n² is even," write n = 2k, compute n² = 4k² = 2(2k²), and observe the result is even. **Proof by contrapositive** rewrites "if P then Q" as "if not Q then not P," which is logically equivalent. This is valuable when the negation of Q is easier to work with than P. For example, "if n² is odd then n is odd" is easier proved as its contrapositive: "if n is even then n² is even" — which we just did directly. Same proof, different framing.

**Proof by contradiction** is more dramatic: assume both the hypothesis *and* the negation of the conclusion, then derive a logical impossibility. The classic example is proving √2 is irrational: assume it equals p/q in lowest terms, derive that p and q are both even, contradiction. The key discipline is that you assume the *negation of the entire goal statement*, not some intermediate claim — a common source of error. **Proof by cases** partitions the domain into exhaustive, mutually exclusive scenarios and proves the conclusion in each. "Every integer is either even or odd" licenses proving two cases; sometimes more are needed (e.g., n mod 3 gives three cases).

**Mathematical induction** is the most powerful strategy for statements indexed by natural numbers, and you've studied its mechanics as a prerequisite. The intuition is a chain of dominoes: prove the base case (the first domino falls), then prove the inductive step (if the k-th falls, so does the (k+1)-th), and the whole chain falls. The inductive step is not "the statement is true for k, therefore true for k+1" — that would be circular. Instead, you *assume* it holds for an arbitrary k (the **inductive hypothesis**) and *derive* that it holds for k+1 using that assumption as a tool. Strong induction allows the hypothesis to cover all values up to k, which is useful when n+1 depends on more than just n (e.g., the Fibonacci sequence). Recognizing which strategy to deploy first requires practice: when the goal is an equation or inequality, try direct or induction; when the conclusion seems hard to reach forward, try contrapositive or contradiction; when the domain naturally splits, try cases.
