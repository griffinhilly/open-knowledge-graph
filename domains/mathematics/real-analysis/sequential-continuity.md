---
id: sequential-continuity
title: Sequential Characterization of Continuity
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-delta-continuity
  type: hard
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-convergence-preserves-continuity
tags:
- continuity
- sequences
- equivalence
stage: advanced
status: draft
---

# Sequential Characterization of Continuity

## Core Idea
A function f is continuous at c if and only if for every sequence (xₙ) with xₙ → c, we have f(xₙ) → f(c). This equivalence allows switching between ε-δ and sequential definitions: use sequences when natural, ε-δ when rigor demands it. The equivalence is a fundamental tool for proofs.

## How It's Best Learned
Prove f(x) = x² is continuous at 2 using both definitions, then use sequences to show f(x) = ⌊x⌋ is not continuous at integers.

## Common Misconceptions
- Assuming sequences must approach the continuity point monotonically or regularly; any convergent sequence works.
- Forgetting the 'if and only if': the equivalence works in both directions.
- Thinking sequential continuity is weaker; it is equivalent to ε-δ continuity in ℝ.

## Explainer

You already have two tools: the ε-δ definition of continuity and the ε-N definition of sequence convergence. **Sequential continuity** is the bridge between them — it says that continuous functions and convergent sequences commute: you can take the function inside the limit. Formally, f is continuous at c if and only if, for every sequence (xₙ) converging to c, the sequence (f(xₙ)) converges to f(c). This is not a new concept layered on top of continuity — it is an exact restatement of what ε-δ continuity means, translated into sequential language.

The "only if" direction is the one most students master first: if f is ε-δ continuous at c and xₙ → c, then f(xₙ) → f(c). The proof is clean — given ε > 0, find δ from continuity, then use the convergence of xₙ to find N such that |xₙ − c| < δ for n ≥ N. The "if" direction — proving ε-δ continuity from the sequential condition — requires a proof by contradiction and is typically more surprising: assume f is *not* ε-δ continuous at c, construct a sequence xₙ → c with f(xₙ) ↛ f(c), contradicting the hypothesis.

The power of sequential continuity is in how it lets you choose your proof style to match the problem. The floor function ⌊x⌋ provides the clearest example of the sequential approach for *disproving* continuity: at any integer n, take the sequence xₙ = n − 1/n, which converges to n from below. Then f(xₙ) = n − 1 for all n, so f(xₙ) → n − 1 ≠ n = f(n). One sequence, one counterexample, proof complete. Doing the same job with ε-δ requires careful case analysis around the specific integer.

Sequences are particularly natural when working with limits of compositions, limits of function sequences, or arguments involving Bolzano-Weierstrass. If a proof begins "let (xₙ) be any sequence converging to c," you are in sequential mode. The equivalence guarantees that any conclusion you reach — continuity or discontinuity — is as rigorous as any ε-δ argument. The skill is recognizing which mode is cleaner for the problem at hand.
