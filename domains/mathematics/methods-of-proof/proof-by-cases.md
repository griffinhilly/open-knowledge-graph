---
id: proof-by-cases
title: Proof by Cases (Proof by Exhaustion)
domain: mathematics
course: methods-of-proof
prerequisites:
- id: direct-proof
  type: hard
builds-toward:
- mathematical-induction
tags:
- proof
- cases
- exhaustion
stage: formal-systems
status: draft
---

# Proof by Cases (Proof by Exhaustion)

## Core Idea
Proof by cases partitions the hypothesis into exhaustive cases and proves the conclusion for each. If true in all cases, it's true in general. This method is essential when a universal approach is infeasible.

## How It's Best Learned
Identify natural partitions: parity (even/odd), sign (positive/negative/zero), or other exhaustive categories. Verify no cases are missed.

## Common Misconceptions
- Forgetting edge cases or overlapping regions.
- Believing a general proof is always preferable to cases when cases are clearer.

## Explainer

You've learned to write **direct proofs**, where you start from the hypothesis and derive the conclusion through a chain of logical steps. Proof by cases extends this when a single chain of reasoning can't handle all the ways the hypothesis can be true. The strategy is to partition all possibilities into a finite set of cases, prove the conclusion within each case separately, and then conclude that since the cases are exhaustive — every instance falls into at least one — the result holds in general.

The critical move is identifying the right partition. The partition must be **exhaustive**: every possible instance must fall into at least one of your cases; no situation should be left unaddressed. Common natural partitions are: **parity** (n is even vs. n is odd), **sign** (x > 0, x = 0, x < 0), or **membership** (n is in some set vs. n is not). You don't need the cases to be mutually exclusive — overlap is permitted — but you do need to handle each case completely.

Consider proving that n² + n is always even. You could factor: n² + n = n(n+1), and observe that consecutive integers always include one even number. But proof by cases makes this immediate. *Case 1: n is even.* Then n = 2k, so n(n+1) = 2k(2k+1) = 2·[k(2k+1)], which is even. *Case 2: n is odd.* Then n+1 is even, so n+1 = 2m, and n(n+1) = n·2m = 2·[nm], which is even. Since every integer is either even or odd, the cases are exhaustive, and the proof is complete. No algebraic ingenuity was required — just systematic enumeration.

An important mindset shift: proof by cases is not a fallback when you can't find a "better" proof. It is often the *cleanest* and most transparent proof available, especially in number theory and combinatorics. What distinguishes a rigorous case proof from hand-waving is the explicit verification that cases are exhaustive. A proof that leaves an edge case unhandled — say, forgetting n = 0 when proving something about non-negative integers — has a genuine gap, even if all other cases are airtight.
