---
id: proving-by-cases
title: Proving by Cases and Exhaustion
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proving-by-direct-method
  type: hard
builds-toward:
- vacuous-truth-and-trivial-cases
tags:
- proof
- cases
- exhaustion
- disjunction
stage: formal-systems
status: draft
---

# Proving by Cases and Exhaustion

## Core Idea
To prove a statement P, divide the domain or hypothesis into mutually exclusive and exhaustive cases, then prove P in each case. If P holds in all cases, it holds in general. This method is used when a direct proof is unwieldy or when the proof naturally breaks into distinct scenarios.

## How It's Best Learned
Identify when a statement naturally breaks into cases (e.g., integer parity, modular arithmetic). Ensure all cases are covered and are mutually exclusive.

## Common Misconceptions
- Forgetting to cover all cases.
- Allowing cases to overlap without recognizing it.
- Assuming one case 'represents' the others without proving all.

## Explainer

You already know how to construct a direct proof: assume the hypothesis, then derive the conclusion through a chain of valid inference steps. But sometimes the path from hypothesis to conclusion is not a single straight line — the hypothesis splits into distinct scenarios that require different reasoning. **Proof by cases** is the technique for handling this: divide, conquer each piece separately, then reassemble.

The logical foundation is simple. Suppose you know that at least one of P₁, P₂, ..., Pₙ is true (the cases cover all possibilities), and you can prove Q from each Pᵢ individually. Then Q must be true. In symbols: if (P₁ ∨ P₂ ∨ ··· ∨ Pₙ) and (Pᵢ → Q for each i), then Q. The strength of the method is that within each case, you can use the case assumption as an additional hypothesis — an assumption not available in a general direct proof. That added assumption often makes what was intractable become straightforward.

The most important structural requirement is **exhaustiveness**: your cases must collectively cover the entire domain. If you prove a statement for even integers and odd integers separately, you have covered all integers — because every integer is either even or odd. But if you prove something for positive reals and negative reals and forget zero, your proof has a gap. Overlapping cases are fine (you can have more cases than necessary), but missing cases are fatal. Common natural case splits arise from: parity (even/odd), sign (positive/negative/zero), inequalities (x < 1, x = 1, x > 1), divisibility classes, and whether a particular element is in a set or not.

Consider proving that n² + n is always even for any integer n. A direct proof without cases is possible but feels awkward. With cases: if n is even, write n = 2k, then n² + n = 4k² + 2k = 2(2k² + k), which is even. If n is odd, write n = 2k + 1, then n² + n = (2k+1)² + (2k+1) = 4k² + 4k + 1 + 2k + 1 = 4k² + 6k + 2 = 2(2k² + 3k + 1), which is even. Both cases give even results; the cases are exhaustive; the proof is complete. The case structure does not just organize the proof — it actively enables each sub-proof by supplying the concrete form of n.
