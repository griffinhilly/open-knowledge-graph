---
id: epsilon-delta-continuity
title: Epsilon-Delta Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: continuity-definition
  type: soft
- id: epsilon-n-convergence
  type: hard
builds-toward:
- sequential-continuity
- uniform-continuity
- rigorous-derivative-definition
tags:
- continuity
- epsilon-delta
- rigor
stage: advanced
status: draft
---

# Epsilon-Delta Continuity

## Core Idea
A function f is continuous at a point c if for every ε > 0, there exists δ > 0 such that |x - c| < δ implies |f(x) - f(c)| < ε. This formalizes 'small changes in input give small changes in output.' Continuity on a set means continuity at every point. It is the foundational definition for rigorous calculus.

## Questions

```yaml
- question: "Which statement correctly captures the ε-δ definition of continuity of f at c?"
  type: multiple-choice
  options: ["For some ε > 0, for all δ > 0, |x − c| < δ implies |f(x) − f(c)| < ε", "For all ε > 0, there exists δ > 0 such that |x − c| < δ implies |f(x) − f(c)| < ε", "For all δ > 0, there exists ε > 0 such that |f(x) − f(c)| < ε implies |x − c| < δ", "For all ε > 0, for all δ > 0, |x − c| < δ implies |f(x) − f(c)| < ε"]
  answer: 1
  explanation: "The correct quantifier order is 'for all ε, there exists δ' — ε is the adversarial challenge, δ is the response. Option A fails because 'for some ε' allows cherry-picking an easy ε rather than handling all of them. Option C reverses the implication direction (output tolerance implying input restriction). Option D claims one δ works for every ε simultaneously, which is a different (stronger) condition."

- question: "To prove f is continuous at c using the ε-δ definition, it suffices to exhibit one specific pair (ε₀, δ₀) that satisfies the condition."
  type: true-false
  answer: false
  explanation: "Continuity requires finding a valid δ for EVERY ε > 0, no matter how small. Verifying the condition for a single ε₀ says nothing about other values of ε. A complete proof must provide δ as a function of ε — a strategy that works universally. The same logic applies to sequence convergence: finding one N for one ε does not prove the sequence converges."

- question: "What does the ε-δ definition formalize that the informal notion of 'no jumps or holes' does not?"
  type: short-answer
  answer: "The ε-δ definition gives a quantitative, provable criterion: for any output tolerance ε, there is an input restriction δ that guarantees the output stays within ε. This handles pathological functions and non-geometric domains where 'no jumps' is ambiguous, and it produces checkable proofs."
  explanation: "Informal geometric descriptions fail for exotic functions (Dirichlet-type functions, functions on abstract metric spaces) where drawing a graph is impossible or misleading. The ε-δ formulation is domain-agnostic and admits rigorous proof by construction of δ from ε."
```

## Explainer

You have likely encountered continuity before as "no jumps or holes" — an intuition that works well for the functions encountered in introductory calculus. But in real analysis, intuition is not proof. The ε-δ definition gives continuity a precise, checkable meaning that works for any function on any metric space, including pathological cases where geometric intuition breaks down completely.

Read the definition as a challenge-response game between two players. The adversary picks any ε > 0 — a tolerance on the output: they are demanding that f(x) stay within ε of f(c). You must respond with a δ > 0 — a restriction on the input: you claim that keeping x within δ of c is sufficient to guarantee f(x) stays within ε of f(c). If you can always find a winning δ, no matter how small ε is chosen, then f is continuous at c. If even once the adversary can pick an ε for which no δ works, f is discontinuous there.

The quantifier structure — "for all ε, there exists δ" — is the precise counterpart to the sequence convergence definition you already know: "for all ε, there exists N." In sequence convergence, N is how far out you must go in the sequence; here, δ is how close you must stay in the domain. Your δ is allowed to depend on ε, and in general it must (smaller ε typically forces smaller δ). What is not required is a single δ that works for all ε at once; that stronger condition defines something else (uniform continuity, which you will study next).

To prove continuity constructively, work backward from what you need. To show f(x) = 2x is continuous at any c: given ε > 0, you need |f(x) − f(c)| = |2x − 2c| = 2|x − c| < ε. Setting δ = ε/2 gives 2|x − c| < 2(ε/2) = ε whenever |x − c| < δ. Done. The technique is always the same: manipulate |f(x) − f(c)| until you can bound it by something involving |x − c|, then choose δ to make that bound fall below ε.

Discontinuity is equally important. A function fails to be continuous at c if there exists some ε > 0 for which no δ works — meaning points x arbitrarily close to c can have f(x) far from f(c). The step function f(x) = 0 for x < 0, f(x) = 1 for x ≥ 0 fails at c = 0 with ε = 1/2: no matter how small δ is, negative x-values within (−δ, 0) satisfy f(x) = 0, which is distance 1 from f(0) = 1, exceeding ε. This definition will generalize immediately: uniform continuity (where δ depends only on ε, not on c), the rigorous derivative definition (a limit of a ratio), and eventually integration theory all use the same ε-δ template.
