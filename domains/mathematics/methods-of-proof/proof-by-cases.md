---
id: proof-by-cases
title: Proof by Cases (Proof by Exhaustion)
domain: mathematics
course: methods-of-proof
prerequisites:
- id: direct-proof
  type: hard
- id: vacuous-truth-and-trivial-cases
  type: soft
builds-toward:
- mathematical-induction
tags:
- proof
- cases
- exhaustion
stage: formal-systems
status: validated
---
# Proof by Cases (Proof by Exhaustion)

## Core Idea
Proof by cases partitions the hypothesis into exhaustive cases and proves the conclusion for each. If true in all cases, it's true in general. This method is essential when a universal approach is infeasible.

## How It's Best Learned
Identify natural partitions: parity (even/odd), sign (positive/negative/zero), or other exhaustive categories. Verify no cases are missed.

## Common Misconceptions
- Forgetting edge cases or overlapping regions.
- Believing a general proof is always preferable to cases when cases are clearer.

## Questions

```yaml
- question: "You want to prove that n² + n is even for all integers n. A classmate argues that you must find an algebraic manipulation working uniformly for all n, and that splitting into even/odd cases is a 'weaker' approach. Which response best captures the methodological truth?"
  type: multiple-choice
  options:
    - "The classmate is correct — proof by cases is only valid when no general proof exists"
    - "Proof by cases is fully rigorous and often the clearest proof; the even/odd case split gives a complete proof with no need for a 'better' alternative"
    - "Proof by cases works here but should be used only as a last resort when algebraic methods fail"
    - "Proof by cases requires mutually exclusive cases, so even/odd is invalid since some integers might be both"
  answer: 1
  explanation: "Proof by cases is not a fallback — it is a legitimate and often the *cleanest* proof strategy available. The odd/even partition is exhaustive (every integer is one or the other) and mutually exclusive, making it perfectly valid. Option D is wrong: overlapping cases are permitted — only exhaustiveness is required. Option A reflects a common but false hierarchy where 'general' proofs are inherently superior."

- question: "A student proves a statement 'for all integers n ≥ 0' using two cases: n is positive and n is negative. A reviewer says the proof has a critical gap. What is it?"
  type: multiple-choice
  options:
    - "The cases overlap — some integers are both positive and negative"
    - "The case n = 0 is omitted; zero is neither positive nor negative, so no case covers it"
    - "Proof by cases cannot be used for statements about integers — it only works for finite sets"
    - "There is no gap — if the proof works for positive and negative n, it works for all n ≥ 0"
  answer: 1
  explanation: "The partition {positive, negative} is not exhaustive over the domain {n ≥ 0} because n = 0 falls into neither case. This leaves a genuine gap: the conclusion has not been established for n = 0. A proof by cases is only complete when every element of the domain falls into at least one case. Forgetting edge cases like zero, or boundary values, is the most common error in case proofs."

- question: "In a proof by cases, the cases should be mutually exclusive — no element of the domain can fall into more than one case."
  type: true-false
  answer: false
  explanation: "Mutual exclusivity is not required. Only exhaustiveness is required: every element of the domain must fall into at least one case. Overlapping cases are perfectly valid — you simply prove the conclusion in each case, and since every instance is covered by at least one case, the proof is complete. The parity split (even/odd) happens to be both exhaustive and mutually exclusive, but the latter is a bonus, not a requirement."

- question: "A proof by cases is considered a fully rigorous mathematical proof, not a shortcut or fallback method."
  type: true-false
  answer: true
  explanation: "Proof by cases is a standard and rigorous proof technique, not a lesser substitute. It is often the *most* transparent proof available, especially in number theory and combinatorics, because it makes the reasoning in each sub-situation completely explicit. The mathematical community treats it as equal in rigor to direct proof, proof by contradiction, or any other method — provided the cases are exhaustive."

- question: "Why must the set of cases in a proof by cases be exhaustive, and what exactly goes wrong if an edge case is omitted?"
  type: short-answer
  answer: "The cases must be exhaustive because the proof only establishes the conclusion within each case it handles. If any instance falls outside all cases, the conclusion has simply not been proven for that instance — the proof has a gap. The final step of a case proof is: 'since every element of the domain falls into at least one case, and the conclusion holds in each case, it holds universally.' That step fails if even one element is unaccounted for. A proof that omits n = 0 while claiming to cover all non-negative integers is genuinely incomplete, not merely inelegant."
  explanation: "Exhaustiveness is what licenses the universal conclusion. Without it, you have proven the statement for some elements but not all. The common failure mode is forgetting boundary cases (zero, the empty set, a = b in 'a < b or a > b or a = b') — these are mathematically real instances that require explicit handling."
```

## Explainer

You've learned to write **direct proofs**, where you start from the hypothesis and derive the conclusion through a chain of logical steps. Proof by cases extends this when a single chain of reasoning can't handle all the ways the hypothesis can be true. The strategy is to partition all possibilities into a finite set of cases, prove the conclusion within each case separately, and then conclude that since the cases are exhaustive — every instance falls into at least one — the result holds in general.

The critical move is identifying the right partition. The partition must be **exhaustive**: every possible instance must fall into at least one of your cases; no situation should be left unaddressed. Common natural partitions are: **parity** (n is even vs. n is odd), **sign** (x > 0, x = 0, x < 0), or **membership** (n is in some set vs. n is not). You don't need the cases to be mutually exclusive — overlap is permitted — but you do need to handle each case completely.

Consider proving that n² + n is always even. You could factor: n² + n = n(n+1), and observe that consecutive integers always include one even number. But proof by cases makes this immediate. *Case 1: n is even.* Then n = 2k, so n(n+1) = 2k(2k+1) = 2·[k(2k+1)], which is even. *Case 2: n is odd.* Then n+1 is even, so n+1 = 2m, and n(n+1) = n·2m = 2·[nm], which is even. Since every integer is either even or odd, the cases are exhaustive, and the proof is complete. No algebraic ingenuity was required — just systematic enumeration.

An important mindset shift: proof by cases is not a fallback when you can't find a "better" proof. It is often the *cleanest* and most transparent proof available, especially in number theory and combinatorics. What distinguishes a rigorous case proof from hand-waving is the explicit verification that cases are exhaustive. A proof that leaves an edge case unhandled — say, forgetting n = 0 when proving something about non-negative integers — has a genuine gap, even if all other cases are airtight.
